"""
Mesh data operations service for RenderDoc.

Provides mesh vertex/index data access and CSV export functionality.
Supports VSIn, VSOut, and GSOut stages.

VSIn reads the raw vertex buffers (including per-instance attributes at a
selectable instance index). VSOut/GSOut derive attribute layout from the
shader output signature because the MeshFormat returned by GetPostVSData
does not carry per-attribute names. Post-VS buffers are packed differently
per backend (D3D/GL stream-out vs Vulkan std430), so offsets are computed
per API and validated against the reported vertex stride - a layout that
does not fit fails loudly instead of decoding misaligned data.
"""

import csv
import os
import re
import struct
import math
from collections import OrderedDict
from typing import Any, Optional, List

import renderdoc as rd

from .replay_query import at_event

_MESH_STAGES = ("VSIn", "VSOut", "GSOut")
_NO_REGISTER = 0xFFFFFFFF  # rd.SigParameter.NoIndex


def _validate_instance(instance):
    if type(instance) is not int or instance < 0:
        raise ValueError("INVALID_INSTANCE: non-negative integer required")
    return instance


def _align_up(value, alignment):
    if alignment <= 0:
        return value
    remainder = value % alignment
    if remainder:
        return value + alignment - remainder
    return value


class _AttributeEntry(object):
    """Attribute-style view over one post-VS output signature element."""

    def __init__(self, **fields):
        for name, value in fields.items():
            setattr(self, name, value)


class MeshService:
    """Mesh data operations service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn
        # Initialize format chars lazily
        self._format_chars = None
        self._var_type_maps = None

    def _get_format_chars(self):
        """Get format character mapping for struct unpacking.

        Index by compByteWidth; CompType only exposes Float/UNorm/SNorm/UInt/SInt
        families, with Double/Half data carried by Float + wider byte widths
        ('e' decodes IEEE half floats, 'd' doubles).
        """
        if self._format_chars is None:
            # 8-byte integers must use q/Q: native 'l'/'L' are 4 bytes on Windows
            self._format_chars = {
                rd.CompType.UInt: "xBHxIxxxQ",
                rd.CompType.SInt: "xbhxixxxq",
                rd.CompType.Float: "xxexfxxxd",
                rd.CompType.UNorm: "xBHxIxxxQ",
                rd.CompType.UScaled: "xBHxIxxxQ",
                rd.CompType.SNorm: "xbhxixxxq",
                rd.CompType.SScaled: "xbhxixxxq",
            }
        return self._format_chars

    def _get_var_type_maps(self):
        """Map reflection VarType to ResourceFormat comp type and byte width.

        The real CompType enum has no Double/Half members: those var types are
        represented as Float with the appropriate compByteWidth (struct 'e'/'d'
        handle the actual decoding).
        """
        if self._var_type_maps is None:
            comp_types = {
                rd.VarType.Float: rd.CompType.Float,
                rd.VarType.Double: rd.CompType.Float,
                rd.VarType.Half: rd.CompType.Float,
                rd.VarType.SInt: rd.CompType.SInt,
                rd.VarType.SShort: rd.CompType.SInt,
                rd.VarType.SLong: rd.CompType.SInt,
                rd.VarType.SByte: rd.CompType.SInt,
                rd.VarType.Enum: rd.CompType.SInt,
                rd.VarType.Bool: rd.CompType.UInt,
                rd.VarType.UInt: rd.CompType.UInt,
                rd.VarType.UShort: rd.CompType.UInt,
                rd.VarType.ULong: rd.CompType.UInt,
                rd.VarType.UByte: rd.CompType.UInt,
            }
            byte_widths = {
                rd.VarType.Double: 8,
                rd.VarType.Half: 2,
                rd.VarType.SLong: 8,
                rd.VarType.ULong: 8,
                rd.VarType.SShort: 2,
                rd.VarType.UShort: 2,
                rd.VarType.SByte: 1,
                rd.VarType.UByte: 1,
            }
            self._var_type_maps = (comp_types, byte_widths)
        return self._var_type_maps

    def _unpack_vertex_data(self, fmt, buffer_data: bytes, offset: int) -> tuple:
        """
        Unpack vertex data from buffer based on format.

        Args:
            fmt: ResourceFormat object
            buffer_data: Raw buffer bytes
            offset: Byte offset into buffer

        Returns:
            Tuple of component values
        """
        format_chars = self._get_format_chars()

        # Build struct format string
        vertex_format = str(fmt.compCount) + format_chars[fmt.compType][fmt.compByteWidth]

        # Check if offset is valid
        required_size = struct.calcsize(vertex_format)
        if offset < 0 or offset + required_size > len(buffer_data):
            raise ValueError("MESH_DATA_OUT_OF_BOUNDS: attribute byte range %d..%d exceeds %d" %
                             (offset, offset + required_size, len(buffer_data)))

        value = struct.unpack_from(vertex_format, buffer_data, offset)

        # Handle normalized formats
        if fmt.compType == rd.CompType.UNorm:
            divisor = float((2 ** (fmt.compByteWidth * 8)) - 1)
            value = tuple(float(i) / divisor for i in value)
        elif fmt.compType == rd.CompType.SNorm:
            # Signed normalization: max_pos = 2^(bits-1) - 1 (127 for 8-bit),
            # and the most negative value maps to -1.0.
            max_neg = -float(2 ** (fmt.compByteWidth * 8)) / 2
            divisor = -max_neg - 1.0
            value = tuple(
                (-1.0 if (i == max_neg) else (float(i) / divisor))
                for i in value
            )

        # Handle BGRA order
        if fmt.BGRAOrder():
            value = tuple(value[i] for i in [2, 1, 0, 3])

        return value

    def _get_indices(self, controller, mesh) -> list:
        """
        Extract index data from mesh.

        Args:
            controller: ReplayController
            mesh: MeshFormat object

        Returns:
            List of indices
        """
        # Determine index format
        if mesh.indexResourceId != rd.ResourceId.Null():
            if mesh.indexByteStride not in (1, 2, 4):
                raise ValueError("MESH_INVALID_INDEX_FORMAT: index width must be 1, 2 or 4")
            offset = mesh.indexByteOffset + getattr(mesh, "indexOffset", 0) * mesh.indexByteStride
            if offset < 0:
                raise ValueError("MESH_DATA_OUT_OF_BOUNDS: negative index offset")
            size = mesh.numIndices * mesh.indexByteStride
            ib_data = controller.GetBufferData(mesh.indexResourceId, offset, size) if size else b""
            if len(ib_data) < size:
                raise ValueError("MESH_DATA_SHORT_READ: index buffer has %d bytes, expected %d" %
                                 (len(ib_data), size))
            indices = struct.unpack_from("<%d%s" % (
                mesh.numIndices, {1: "B", 2: "H", 4: "I"}[mesh.indexByteStride]), ib_data)
            restart = None
            try:
                pipe = controller.GetPipelineState()
                if pipe.IsRestartEnabled() and getattr(mesh, "allowRestart", True):
                    restart = pipe.GetRestartIndex() & ((1 << (8 * mesh.indexByteStride)) - 1)
            except AttributeError:
                pass
            result = [-1 if i == restart else i + mesh.baseVertex for i in indices]
            if any(i < 0 and i != -1 for i in result):
                raise ValueError("MESH_DATA_OUT_OF_BOUNDS: negative effective vertex index")
            # -1 is reserved exclusively for primitive restart.
            if any(i + mesh.baseVertex == -1 and i != restart for i in indices):
                raise ValueError("MESH_DATA_OUT_OF_BOUNDS: negative effective vertex index")
            return result
        else:
            # Non-indexed draw
            return list(range(mesh.numIndices))

    def _get_mesh_inputs(self, controller, draw, instance=0) -> list:
        """
        Get mesh input data (VSIn stage), including per-instance attributes.

        Args:
            controller: ReplayController
            draw: ActionDescription (draw call)
            instance: Instance index (0-based within the draw, i.e. relative to
                the draw's instanceOffset which is added here)

        Returns:
            List of MeshFormat objects for each vertex attribute
        """
        state = controller.GetPipelineState()
        ib = state.GetIBuffer()
        vbs = state.GetVBuffers()
        attrs = state.GetVertexInputs()

        mesh_inputs = []
        for attr in attrs:
            if not getattr(attr, "used", True):
                continue
            generic = bool(getattr(attr, "genericEnabled", False))
            vb_index = attr.vertexBuffer
            if not generic and (vb_index is None or vb_index < 0 or vb_index >= len(vbs)):
                raise ValueError("MESH_DATA_UNAVAILABLE: required vertex binding missing for %s" % attr.name)
            vb = (vbs[vb_index] if not generic else
                  _AttributeEntry(byteOffset=0, byteStride=0, resourceId=rd.ResourceId.Null()))

            attr_offset = attr.byteOffset + vb.byteOffset
            instanced = bool(getattr(attr, "perInstance", False))
            if instanced:
                # Native mesh read rule: start-instance shifts the whole window
                # (instanceOffset * stride), while the rate divides only the
                # 0-based instance index; rate 0 reads element 0 constantly.
                rate = getattr(attr, "instanceRate", 0) or 0
                inst_idx = (instance // rate) if rate > 0 else 0
                window = (getattr(draw, "instanceOffset", 0) or 0) + inst_idx
                attr_offset += window * vb.byteStride
            else:
                attr_offset += draw.vertexOffset * vb.byteStride

            mesh_input = _AttributeEntry()
            mesh_input.indexResourceId = ib.resourceId
            mesh_input.indexByteOffset = ib.byteOffset
            mesh_input.indexByteStride = ib.byteStride
            mesh_input.baseVertex = draw.baseVertex
            mesh_input.indexOffset = draw.indexOffset
            mesh_input.numIndices = draw.numIndices
            mesh_input.instanced = instanced
            mesh_input.topology = state.GetPrimitiveTopology() if hasattr(state, "GetPrimitiveTopology") else "Unknown"

            # Check if indexed draw
            if not (draw.flags & rd.ActionFlags.Indexed):
                mesh_input.indexResourceId = rd.ResourceId.Null()

            mesh_input.vertexByteOffset = attr_offset
            mesh_input.format = attr.format
            mesh_input.vertexResourceId = vb.resourceId
            mesh_input.vertexByteStride = vb.byteStride
            mesh_input.name = attr.name
            mesh_input.source_vertex_buffer = vb_index
            mesh_input.source_attribute_offset = attr.byteOffset
            mesh_input.source_binding_offset = vb.byteOffset
            mesh_input.source_instance_rate = getattr(attr, "instanceRate", 0)
            if generic:
                value_field = ("uintValue" if attr.format.compType == rd.CompType.UInt else
                               "intValue" if attr.format.compType == rd.CompType.SInt else "floatValue")
                mesh_input.constant_value = list(getattr(attr.genericValue, value_field))[:attr.format.compCount]

            mesh_inputs.append(mesh_input)

        return mesh_inputs

    def _get_postvs_data(self, controller, draw, stage: str, instance: int = 0, view_index: int = 0) -> Any:
        """
        Get post-vertex-shader or post-geometry-shader mesh data.

        Args:
            controller: ReplayController
            draw: ActionDescription
            stage: "VSOut" or "GSOut"
            instance: Instance index (post-VS buffers are stored per instance)

        Returns:
            MeshFormat object or None if not available
        """
        stage_map = {
            "VSOut": rd.MeshDataStage.VSOut,
            "GSOut": rd.MeshDataStage.GSOut,
        }
        mesh_stage = stage_map.get(stage, rd.MeshDataStage.VSOut)

        _validate_instance(view_index)
        try:
            count = max(1, controller.GetPipelineState().MultiviewBroadcastCount())
        except AttributeError:
            count = 1
        if view_index >= count:
            raise ValueError("INVALID_VIEW_INDEX: view_index exceeds multiview count")
        mesh = controller.GetPostVSData(instance, view_index, mesh_stage)

        # Check if valid
        if mesh is None or mesh.vertexResourceId == rd.ResourceId.Null():
            return None
        if hasattr(mesh, "status") and mesh.status:
            raise ValueError("MESH_DATA_UNAVAILABLE: %s" % mesh.status)

        return mesh

    def _get_postvs_inputs(self, controller, action, stage: str, instance: int, view_index: int = 0) -> list:
        """
        Build per-attribute entries for VSOut/GSOut from the shader output signature.

        GetPostVSData returns a single MeshFormat without per-attribute names, so
        attribute layout comes from the producing stage's reflection output signature.
        GSOut is the output of the last active stage: geometry when one is bound,
        otherwise the final tessellation (domain) stage. Layout follows the native
        mesh viewer: entries filtered by rasterized stream, position hoisted to
        the front, and 32-bit-expanded components with vec4 alignment only when
        HasAlignedPostVSData reports an aligned (compute-built) buffer.
        """
        mesh = self._get_postvs_data(controller, action, stage, instance, view_index)
        if mesh is None:
            return []

        state = controller.GetPipelineState()
        if stage == "VSOut":
            candidates = (rd.ShaderStage.Vertex,)
            mesh_stage = rd.MeshDataStage.VSOut
        else:
            # Only fall back to the domain stage when no geometry shader is
            # actually bound; a bound stage with a broken reflection must fail
            # loudly rather than be reinterpreted as tessellation output.
            try:
                gs_bound = state.GetShader(rd.ShaderStage.Geometry) != rd.ResourceId.Null()
            except Exception:
                gs_bound = True
            if gs_bound:
                candidates = (rd.ShaderStage.Geometry,)
            else:
                candidates = (rd.ShaderStage.Domain,)
            mesh_stage = rd.MeshDataStage.GSOut

        signature = []
        for reflection_stage in candidates:
            try:
                reflection = state.GetShaderReflection(reflection_stage)
            except Exception:
                reflection = None
            signature = list(getattr(reflection, "outputSignature", None) or []) \
                if reflection is not None else []
            if signature:
                break
        if not signature:
            raise ValueError(
                "MESH_SIGNATURE_UNAVAILABLE: no %s output signature at event %d"
                % (stage, action.eventId)
            )

        try:
            aligned = bool(state.HasAlignedPostVSData(mesh_stage))
            rasterized_stream = int(state.GetRasterizedStream())
        except Exception as exc:
            # Without the layout hints any offset guess could silently decode
            # misaligned data; fail instead.
            raise ValueError(
                "MESH_SIGNATURE_UNAVAILABLE: post-VS layout hints unavailable: %s" % exc
            )

        # Native viewer rule: VSOut always reads stream 0 regardless of the
        # rasterized stream; GSOut follows the rasterized stream but a disabled
        # rasterizer (-1) falls back to stream 0 like the D3D backend does.
        if stage == "VSOut":
            selected_stream = 0
        else:
            selected_stream = rasterized_stream if rasterized_stream >= 0 else 0
        return self._signature_to_inputs(
            signature, mesh, aligned, selected_stream)

    @staticmethod
    def _signature_name(sig) -> str:
        return (
            getattr(sig, "semanticIdxName", "")
            or getattr(sig, "semanticName", "")
            or getattr(sig, "varName", "")
        )

    def _postvs_layout(self, signature, aligned, rasterized_stream):
        """Compute (sig, byte_offset) pairs following the native mesh viewer.

        Entries whose stream does not match the rasterized stream (multi-stream
        geometry outputs) and OutputIndices system values are skipped. Position
        is hoisted to the front unconditionally. Offsets run packed at
        elemSize per component, where elemSize is 8 for 64-bit types and 4 for
        everything else (small types are stored expanded to 32 bits); vec4
        alignment applies only when HasAlignedPostVSData reports an aligned,
        compute-built buffer (Vulkan VSOut).
        """
        output_indices = getattr(rd.ShaderBuiltin, "OutputIndices", object())
        position_value = getattr(rd.ShaderBuiltin, "Position", object())

        def keep(sig):
            if getattr(sig, "stream", 0) != rasterized_stream:
                return False
            if getattr(sig, "systemValue", None) == output_indices:
                return False
            return bool(self._signature_name(sig))

        entries = [sig for sig in signature if keep(sig)]
        _, byte_widths = self._get_var_type_maps()

        def elem_size(var_type):
            return 8 if byte_widths.get(var_type, 4) > 4 else 4

        ordered = ([sig for sig in entries
                    if getattr(sig, "systemValue", None) == position_value] +
                   [sig for sig in entries
                    if getattr(sig, "systemValue", None) != position_value])

        layout = []
        offset = 0
        for sig in ordered:
            size = elem_size(getattr(sig, "varType", None))
            comps = getattr(sig, "compCount", 0) or 4
            if getattr(sig, "systemValue", None) == position_value and comps < 4:
                # D3D stream-out pads SV_Position to a full float4
                comps = 4
            if aligned:
                if comps == 2:
                    offset = _align_up(offset, 2 * size)
                elif comps > 2:
                    offset = _align_up(offset, 4 * size)
            layout.append((sig, offset))
            offset += comps * size
        return layout

    def _signature_to_inputs(self, signature, mesh, aligned, rasterized_stream) -> list:
        """Convert SigParameter entries into attribute-style mesh inputs."""
        layout = self._postvs_layout(signature, aligned, rasterized_stream)
        if not layout:
            return []

        stride = getattr(mesh, "vertexByteStride", 0) or 0
        base = getattr(mesh, "vertexByteOffset", 0) or 0
        if stride <= 0:
            raise ValueError(
                "MESH_SIGNATURE_UNAVAILABLE: post-VS vertex stride is 0 at instance base %d"
                % base
            )

        comp_types, byte_widths = self._get_var_type_maps()
        inputs = []
        for sig, offset in layout:
            name = self._signature_name(sig)
            fmt = rd.ResourceFormat()
            var_type = getattr(sig, "varType", None)
            fmt.compType = comp_types.get(var_type, rd.CompType.Float)
            # Post-VS buffers store every component expanded to at least 32 bits
            width = byte_widths.get(var_type, 4)
            fmt.compByteWidth = width if width > 4 else 4
            comps = getattr(sig, "compCount", 0)
            comps = comps if comps and comps > 0 else 4
            fmt.compCount = comps
            # ResourceFormat.Special() is driven by `type`; a default-constructed
            # format leaves it non-regular, which made exporters skip every
            # post-VS attribute as "special" and Name() report Undefined.
            fmt.type = rd.ResourceFormatType.Regular

            size = fmt.compByteWidth * comps
            if offset + size > stride:
                raise ValueError(
                    "MESH_SIGNATURE_UNAVAILABLE: attribute %s at byte %d exceeds "
                    "reported vertex stride %d"
                    % (name, offset, stride)
                )

            inputs.append(_AttributeEntry(
                name=name,
                format=fmt,
                instanced=False,
                vertexResourceId=mesh.vertexResourceId,
                vertexByteStride=mesh.vertexByteStride,
                # Per-instance data starts at the reported instance base offset
                vertexByteOffset=base + offset,
                topology=mesh.topology,
                numIndices=mesh.numIndices,
                indexResourceId=mesh.indexResourceId,
                indexByteOffset=mesh.indexByteOffset,
                indexByteStride=mesh.indexByteStride,
                baseVertex=mesh.baseVertex,
                indexOffset=0,
                allowRestart=getattr(mesh, "allowRestart", True),
                native_status=getattr(mesh, "status", ""),
                position_semantic=getattr(sig, "systemValue", None) == getattr(rd.ShaderBuiltin, "Position", object()),
            ))
        return inputs

    def _vertex_byte_offset(self, mesh, idx) -> int:
        """Byte address of vertex idx for one attribute.

        Per-instance attributes carry one value shared by all vertices; the
        instance offset is already baked into vertexByteOffset, so no per-vertex
        stride advance applies.
        """
        if idx < 0:
            raise ValueError("MESH_DATA_OUT_OF_BOUNDS: negative vertex index")
        if getattr(mesh, "instanced", False):
            return mesh.vertexByteOffset
        return mesh.vertexByteOffset + mesh.vertexByteStride * idx

    def _batch_get_buffer_data(
        self, controller, mesh_data: list
    ) -> dict:
        """
        Batch get buffer data for performance optimization.

        Args:
            controller: ReplayController
            mesh_data: List of MeshFormat objects

        Returns:
            Dict mapping ResourceId to buffer bytes
        """
        buffer_cache = {}
        for mesh in mesh_data:
            res_id = mesh.vertexResourceId
            if (
                res_id != rd.ResourceId.Null()
                and res_id not in buffer_cache
            ):
                buffer_cache[res_id] = controller.GetBufferData(res_id, 0, 0)
        return buffer_cache

    def _read_attribute(self, mesh, buffers, idx):
        if hasattr(mesh, "constant_value"):
            return mesh.constant_value
        if mesh.vertexResourceId not in buffers:
            raise ValueError("MESH_DATA_SHORT_READ: missing required attribute buffer")
        return self._unpack_vertex_data(mesh.format, buffers[mesh.vertexResourceId],
                                        self._vertex_byte_offset(mesh, idx))

    def _get_resource_name(self, controller, resource_id) -> str:
        """Get resource name from RenderDoc"""
        if resource_id == rd.ResourceId.Null():
            return ""

        # Try to get from buffer list
        try:
            for buf in controller.GetBuffers():
                if buf.resourceId == resource_id:
                    if hasattr(buf, 'customName') and buf.customName:
                        return buf.customName
                    if hasattr(buf, 'name') and buf.name:
                        return buf.name
        except:
            pass

        # Try to get from resource list
        try:
            for res in controller.GetResources():
                if res.resourceId == resource_id and hasattr(res, 'name') and res.name:
                    return res.name
        except:
            pass

        return ""

    def _require_instance_in_range(self, action, action_event_id, instance):
        """Reject instance indices beyond the draw's instance count."""
        num_instances = getattr(action, "numInstances", 1) or 1
        if instance >= num_instances:
            raise ValueError(
                "INVALID_INSTANCE: %d (action at event %d has %d instance(s))"
                % (instance, action_event_id, num_instances)
            )

    def _compute_bounding_box(self, controller, mesh_inputs):
        """Compute the bounding box from the first position-like attribute."""
        position_mesh = None
        for mesh in mesh_inputs:
            attr_name = (mesh.name or "").upper()
            if "POSITION" in attr_name or "POS" in attr_name:
                position_mesh = mesh
                break
        if position_mesh is None:
            return None

        buffer_cache = self._batch_get_buffer_data(controller, [position_mesh])
        indices = self._get_indices(controller, mesh_inputs[0])

        min_pos = [float("inf")] * 3
        max_pos = [float("-inf")] * 3

        if position_mesh.vertexResourceId in buffer_cache:
            buffer_data = buffer_cache[position_mesh.vertexResourceId]
            for idx in indices[:1000]:  # Limit for performance
                byte_offset = self._vertex_byte_offset(position_mesh, idx)
                pos = self._unpack_vertex_data(
                    position_mesh.format, buffer_data, byte_offset
                )
                for i in range(min(3, len(pos))):
                    min_pos[i] = min(min_pos[i], pos[i])
                    max_pos[i] = max(max_pos[i], pos[i])

        if min_pos[0] != float("inf"):
            return {"min": min_pos, "max": max_pos}
        return None

    def _resolve_mesh_name(self, controller, mesh_inputs, action) -> str:
        """Pick a mesh name from the vertex buffer resource, falling back to the action."""
        mesh_name = ""
        for mesh in mesh_inputs:
            if mesh.vertexResourceId != rd.ResourceId.Null():
                mesh_name = self._get_resource_name(controller, mesh.vertexResourceId)
                if mesh_name:
                    break

        if mesh_name:
            mesh_name = re.sub(r'^(vb_|VB_|vertexbuffer_|VertexBuffer_)', '', mesh_name)
            mesh_name = re.sub(r'(_vb|_VB)$', '', mesh_name)

        if not mesh_name:
            mesh_name = getattr(action, 'name', '')
        return mesh_name

    @staticmethod
    def _enum_name(value) -> str:
        return getattr(value, "name", str(value).split(".")[-1])

    @staticmethod
    def _exportable(mesh):
        return not mesh.format.Special() and 1 <= mesh.format.compCount <= 4

    def _attribute_bounding_boxes(self, controller, mesh_inputs, indices):
        """Bounding boxes for 3-component float attributes plus a position guess.

        Reflection names are stripped on many mobile captures (attributes arrive
        as `_input0`), so the position stream is inferred: a POSITION/POS
        semantic wins; otherwise the first attribute whose samples are not
        unit-length (i.e. not a normal) is used. Every computed box is returned
        so callers can verify the choice.
        """
        sample = [i for i in indices if i != -1][:1000]
        eligible = [mesh for mesh in mesh_inputs
                    if not mesh.format.Special()
                    and mesh.format.compCount >= 3
                    and mesh.format.compType == rd.CompType.Float
                    and not getattr(mesh, "instanced", False)]
        buffer_cache = self._batch_get_buffer_data(controller, eligible) if sample else {}
        boxes = OrderedDict()
        normal_like = {}
        for mesh in eligible:
            fmt = mesh.format
            buffer_data = buffer_cache.get(mesh.vertexResourceId)
            if buffer_data is None:
                continue
            mn = [float("inf")] * 3
            mx = [float("-inf")] * 3
            unit = 0
            counted = 0
            for idx in sample:
                try:
                    offset = self._vertex_byte_offset(mesh, idx)
                    size = fmt.compCount * fmt.compByteWidth
                    if offset < 0 or offset + size > len(buffer_data):
                        continue
                    values = self._unpack_vertex_data(
                        fmt, buffer_data, offset
                    )
                except Exception:
                    continue
                if len(values) < 3 or not all(math.isfinite(v) for v in values[:3]):
                    continue
                counted += 1
                length = (values[0] ** 2 + values[1] ** 2 + values[2] ** 2) ** 0.5
                if 0.9 <= length <= 1.1:
                    unit += 1
                for i in range(3):
                    mn[i] = min(mn[i], values[i])
                    mx[i] = max(mx[i], values[i])
            if counted == 0 or mn[0] == float("inf"):
                continue
            boxes[mesh.name] = {"min": mn, "max": mx}
            normal_like[mesh.name] = (float(unit) / counted) > 0.9

        chosen = None
        source = None
        for name in boxes:
            upper = name.upper()
            if "POSITION" in upper or "POS" in upper:
                chosen, source = name, "semantic"
                break
        if chosen is None:
            for name in boxes:
                if not normal_like.get(name, False):
                    chosen, source = name, "inferred_non_unit_length"
                    break
        if chosen is None and boxes:
            chosen = next(iter(boxes))
            source = "first_three_component_attribute"
        return boxes, chosen, source

    def get_mesh_summary(self, action_event_id: int, instance: int = 0, view_index: int = 0) -> dict:
        """
        Get mesh summary information for an event.

        Args:
            action_event_id: Event ID of the draw call
            instance: Instance index for instanced attributes

        Returns:
            Dict with topology, vertex/index counts, attributes and bounding box
        """
        _validate_instance(instance)
        _validate_instance(view_index)
        if view_index:
            raise ValueError("INVALID_VIEW_INDEX: VSIn does not have a multiview selection")

        def operation(controller, target):
            action = self.ctx.GetAction(action_event_id)
            if not (action.flags & rd.ActionFlags.Drawcall):
                raise ValueError(
                    "INVALID_ACTION_EVENT_ID: event %d is not a draw call"
                    % action_event_id
                )
            self._require_instance_in_range(action, action_event_id, instance)

            mesh_inputs = self._get_mesh_inputs(controller, action, instance)

            attributes = []
            for mesh in mesh_inputs:
                attributes.append({
                    "name": mesh.name,
                    "format": str(mesh.format.Name()),
                    "components": mesh.format.compCount,
                    "instanced": bool(getattr(mesh, "instanced", False)),
                    "source": {"resource_id": str(mesh.vertexResourceId),
                               "vertex_byte_offset": mesh.vertexByteOffset,
                               "vertex_byte_stride": mesh.vertexByteStride,
                               "vertex_buffer_slot": getattr(mesh, "source_vertex_buffer", None),
                               "attribute_byte_offset": getattr(mesh, "source_attribute_offset", None),
                               "binding_byte_offset": getattr(mesh, "source_binding_offset", None),
                               "instance_rate": getattr(mesh, "source_instance_rate", None)},
                    "exportable": self._exportable(mesh),
                })

            # Topology comes from the pipeline state: ActionDescription.topology
            # is Unknown on some captures (e.g. Vulkan dynamic state).
            topology = "Unknown"
            topology_source = "unavailable"
            try:
                topology = self._enum_name(controller.GetPipelineState().GetPrimitiveTopology())
                topology_source = "pipeline"
            except Exception:
                if mesh_inputs:
                    topology = self._enum_name(mesh_inputs[0].topology)
                    topology_source = "mesh"

            indexed = bool(action.flags & rd.ActionFlags.Indexed)
            indices_available = True
            if indexed:
                try:
                    if not mesh_inputs or mesh_inputs[0].indexResourceId == rd.ResourceId.Null():
                        raise ValueError("index buffer unavailable")
                    indices = self._get_indices(controller, mesh_inputs[0])
                except Exception:
                    indices = []
                    indices_available = False
                unique_vertex_count = len(set(indices) - {-1}) if indices_available else None
            else:
                indices = list(range(action.numIndices))
                unique_vertex_count = action.numIndices

            boxes, bbox_name, bbox_source = self._attribute_bounding_boxes(
                controller, mesh_inputs, indices
            )

            return {
                "action_event_id": action_event_id,
                "instance": instance,
                "view_index": view_index,
                "name": self._resolve_mesh_name(controller, mesh_inputs, action),
                "topology": topology,
                "topology_source": topology_source,
                "num_vertices": action.numIndices,
                "unique_vertex_count": unique_vertex_count,
                "indices_available": indices_available,
                "num_indices": action.numIndices if indexed else 0,
                "indexed": indexed,
                "attributes": attributes,
                "bounding_box": boxes.get(bbox_name) if bbox_name else None,
                "bounding_box_source": bbox_name,
                "bounding_box_basis": bbox_source,
                "bounding_box_inferred": bool(bbox_source and bbox_source != "semantic"),
                "bounding_boxes": boxes,
            }

        return at_event(self.ctx, self._invoke, action_event_id, operation)

    def get_mesh_data(
        self,
        action_event_id: int,
        stage: str = "VSIn",
        offset: int = 0,
        limit: int = 100,
        attributes: Optional[List[str]] = None,
        instance: int = 0,
        view_index: int = 0,
    ) -> dict:
        """
        Get mesh vertex and index data for a specific draw call.

        Args:
            action_event_id: Event ID of the draw call
            stage: Mesh data stage - "VSIn", "VSOut", or "GSOut"
            offset: Canonical starting vertex offset for pagination (default: 0)
            limit: Canonical maximum number of vertices to return (default: 100, recommended: 100-500)
            attributes: Optional list of attribute names to include
            instance: Instance index for instanced attributes and post-VS data

        Returns:
            Dict with items, indices, topology, attributes, total_count, has_more
        """
        if stage not in _MESH_STAGES:
            raise ValueError("INVALID_STAGE: %s. Must be VSIn, VSOut, or GSOut" % stage)
        _validate_instance(instance)
        _validate_instance(view_index)
        if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 500:
            raise ValueError("INVALID_PAGINATION: offset >= 0, 1 <= limit <= 500 required")

        def operation(controller, target):
            action = self.ctx.GetAction(action_event_id)
            if not (action.flags & rd.ActionFlags.Drawcall):
                raise ValueError(
                    "INVALID_ACTION_EVENT_ID: event %d is not a draw call"
                    % action_event_id
                )
            self._require_instance_in_range(action, action_event_id, instance)

            if stage == "VSIn":
                mesh_inputs = self._get_mesh_inputs(controller, action, instance)
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no mesh input data available for event %d"
                        % action_event_id
                    )
            else:
                # VSOut or GSOut: attributes come from the shader output signature
                mesh_inputs = self._get_postvs_inputs(controller, action, stage, instance, view_index)
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no %s data available for event %d"
                        % (stage, action_event_id)
                    )

            # Filter attributes if specified
            if attributes:
                attr_names_lower = [a.lower() for a in attributes]
                mesh_inputs = [
                    m for m in mesh_inputs
                    if any(n in m.name.lower() for n in attr_names_lower)
                ]
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no matching attributes found: %s"
                        % ", ".join(attributes)
                    )

            # Get indices
            if stage == "VSIn" and view_index:
                raise ValueError("INVALID_VIEW_INDEX: VSIn does not have multiview data")
            all_indices = self._get_indices(controller, mesh_inputs[0])

            # Calculate pagination info
            total_count = len(all_indices)
            has_more = (offset + limit) < total_count

            # Apply pagination
            end_offset = min(offset + limit, total_count)
            indices = all_indices[offset:end_offset]
            truncated = total_count > limit

            # Batch get buffer data for performance
            buffer_cache = self._batch_get_buffer_data(controller, mesh_inputs)

            # Extract vertex data
            vertices = []
            attribute_info = []

            # Build attribute info
            for mesh in mesh_inputs:
                attribute_info.append({
                    "name": mesh.name,
                    "format": str(mesh.format.Name()),
                    "components": mesh.format.compCount,
                    "instanced": bool(getattr(mesh, "instanced", False)),
                    "source": {"resource_id": str(mesh.vertexResourceId),
                               "vertex_byte_offset": mesh.vertexByteOffset,
                               "vertex_byte_stride": mesh.vertexByteStride,
                               "vertex_buffer_slot": getattr(mesh, "source_vertex_buffer", None),
                               "instance_rate": getattr(mesh, "source_instance_rate", None)},
                })

            # Process each vertex
            for idx in indices:
                vertex = {}
                if idx == -1:
                    vertices.append({"primitive_restart": True})
                    continue
                for mesh in mesh_inputs:
                    values = self._read_attribute(mesh, buffer_cache, idx)
                    vertex[mesh.name] = list(values)[:mesh.format.compCount]

                vertices.append(vertex)

            # Determine topology
            topology = "Unknown"
            if mesh_inputs:
                topology = str(mesh_inputs[0].topology)

            return {
                "action_event_id": action_event_id,
                "instance": instance,
                "view_index": view_index,
                "stage": stage,
                "topology": topology,
                "items": [{k: [v if not isinstance(v, float) or math.isfinite(v) else None for v in values]
                           if isinstance(values, list) else values for k, values in vertex.items()}
                          for vertex in vertices],
                "offset": offset,
                "limit": limit,
                "returned_count": len(vertices),
                "total_count": total_count,
                "num_vertices": len(vertices),
                "num_indices": len(indices),
                "has_more": has_more,
                "truncated": truncated,
                "attributes": attribute_info,
                "indices": list(indices),
                "unique_vertex_count": len(set(all_indices) - {-1}),
                "index_domain": "input" if stage == "VSIn" else "post_transform",
                "native_status": getattr(mesh_inputs[0], "native_status", ""),
                "data_quality": self._quality(vertices, mesh_inputs, offset, total_count),
            }

        return at_event(self.ctx, self._invoke, action_event_id, operation)

    def export_mesh_csv(
        self,
        action_event_id: int,
        output_path: str,
        stage: str = "VSIn",
        attributes: Optional[List[str]] = None,
        instance: int = 0,
        view_index: int = 0,
    ) -> dict:
        """
        Export mesh data to CSV file.

        The CSV format:
        - First row is header: VTX,IDX,attr1.x,attr1.y,attr1.z,...
        - VTX: remapped vertex index (0-based)
        - IDX: original vertex index
        - Attribute columns: {attribute_name}.{component}

        Args:
            action_event_id: Event ID of the draw call
            output_path: Output CSV file path
            stage: Mesh data stage - "VSIn", "VSOut", or "GSOut"
            attributes: Optional list of attributes to include
            instance: Instance index for instanced attributes and post-VS data

        Returns:
            Dict with success status and export info
        """
        if stage not in _MESH_STAGES:
            raise ValueError("INVALID_STAGE: %s. Must be VSIn, VSOut, or GSOut" % stage)
        _validate_instance(instance)
        _validate_instance(view_index)
        if stage == "VSIn" and view_index:
            raise ValueError("INVALID_VIEW_INDEX: VSIn does not have multiview data")

        def operation(controller, target):
            action = self.ctx.GetAction(action_event_id)
            if not (action.flags & rd.ActionFlags.Drawcall):
                raise ValueError(
                    "INVALID_ACTION_EVENT_ID: event %d is not a draw call"
                    % action_event_id
                )
            self._require_instance_in_range(action, action_event_id, instance)

            if stage == "VSIn":
                mesh_inputs = self._get_mesh_inputs(controller, action, instance)
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no mesh input data available for event %d"
                        % action_event_id
                    )
            else:
                mesh_inputs = self._get_postvs_inputs(controller, action, stage, instance, view_index)
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no %s data available for event %d"
                        % (stage, action_event_id)
                    )

            # Filter attributes if specified
            if attributes:
                attr_names_lower = [a.lower() for a in attributes]
                mesh_inputs = [
                    m for m in mesh_inputs
                    if any(n in m.name.lower() for n in attr_names_lower)
                ]
                if not mesh_inputs:
                    raise ValueError(
                        "RESOURCE_NOT_FOUND: no matching attributes found: %s"
                        % ", ".join(attributes)
                    )

            # Fail before reading buffers when nothing is exportable: a
            # special/undefined format cannot produce attribute columns.
            if not any(self._exportable(mesh) for mesh in mesh_inputs):
                raise ValueError(
                    "MESH_SIGNATURE_UNAVAILABLE: no exportable attributes for %s "
                    "at event %d" % (stage, action_event_id)
                )

            # Get indices
            if stage == "VSIn" and view_index:
                raise ValueError("INVALID_VIEW_INDEX: VSIn does not have multiview data")
            indices = self._get_indices(controller, mesh_inputs[0])

            # Batch get buffer data
            buffer_cache = self._batch_get_buffer_data(controller, mesh_inputs)

            # Build CSV data
            component_suffixes = [".x", ".y", ".z", ".w"]

            # Build header
            header = ["VTX", "IDX"]
            for mesh in mesh_inputs:
                if not self._exportable(mesh):
                    continue
                for i in range(mesh.format.compCount):
                    header.append("%s%s" % (mesh.name, component_suffixes[i]))

            # Process vertices with deduplication
            unique_vertices = {}  # {original_idx: [attr_values...]}

            for idx in indices:
                if idx == -1:
                    continue
                if idx not in unique_vertices:
                    attribute_values = []
                    for mesh in mesh_inputs:
                        if not self._exportable(mesh):
                            continue
                        values = self._read_attribute(mesh, buffer_cache, idx)
                        for j in range(mesh.format.compCount):
                            attribute_values.append(values[j])
                    unique_vertices[idx] = attribute_values

            # Build remapping
            remap = {}
            rows = []
            for new_vtx, original_idx in enumerate(unique_vertices.keys()):
                remap[original_idx] = new_vtx
                row = [new_vtx, original_idx]
                row.extend(unique_vertices[original_idx])
                rows.append(row)

            # Build triangle stream
            triangle_stream = []  # remapped indices
            for idx in indices:
                if idx == -1:
                    triangle_stream.append(-1)
                elif idx in remap:
                    triangle_stream.append(remap[idx])

            # A header without attribute columns means every attribute was
            # dropped as "special": fail loudly instead of writing a file that
            # only contains VTX/IDX and reporting success.
            if len(header) <= 2:
                raise ValueError(
                    "MESH_SIGNATURE_UNAVAILABLE: no exportable attributes for %s "
                    "at event %d" % (stage, action_event_id)
                )

            # Ensure output directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)

            # Write CSV file
            with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
                writer.writerows(rows)

            # Write index sidecar file
            index_path = os.path.splitext(output_path)[0] + ".idx"
            with open(index_path, "w", encoding="utf-8") as idx_file:
                for remapped_idx in triangle_stream:
                    idx_file.write("%d\n" % remapped_idx)

            exported = sorted(mesh.name for mesh in mesh_inputs if self._exportable(mesh))
            skipped = sorted(
                mesh.name for mesh in mesh_inputs if not self._exportable(mesh)
            )
            return {
                "success": True,
                "action_event_id": action_event_id,
                "instance": instance,
                "view_index": view_index,
                "restart_index": -1,
                "topology": str(mesh_inputs[0].topology),
                "native_status": getattr(mesh_inputs[0], "native_status", ""),
                "data_quality": self._quality([
                    {m.name: list(self._read_attribute(m, buffer_cache, idx)) for m in mesh_inputs
                     if self._exportable(m)} if idx != -1 else {"primitive_restart": True}
                    for idx in indices[:1000]
                ], mesh_inputs, 0, len(indices)),
                "output_path": output_path,
                "index_path": index_path,
                "vertex_count": len(unique_vertices),
                "index_count": len(triangle_stream),
                "stage": stage,
                "format": "CSV",
                "exported_attributes": exported,
                "skipped_attributes": skipped,
            }

        return at_event(self.ctx, self._invoke, action_event_id, operation)

    @staticmethod
    def _quality(vertices, inputs, offset, total):
        sample = vertices[:1000]
        seen = set()
        nonfinite = 0
        points = []
        for vertex in sample:
            flat = []
            for values in vertex.values():
                if isinstance(values, (tuple, list)):
                    flat.extend(values)
            nonfinite += sum(isinstance(x, float) and not math.isfinite(x) for x in flat)
            seen.add(tuple(flat))
            if len(flat) >= 3 and all(isinstance(x, (int, float)) and math.isfinite(x) for x in flat[:3]):
                points.append(flat[:3])
        warnings = []
        if nonfinite:
            warnings.append("non_finite_components")
        if sample and len(seen) < len(sample):
            warnings.append("repeated_attribute_rows_may_be_legal")
        box = ({"min": [min(p[i] for p in points) for i in range(3)],
                "max": [max(p[i] for p in points) for i in range(3)]} if points else None)
        position = next((m.name for m in inputs if getattr(m, "position_semantic", False)), None)
        degenerate, tested = 0, 0
        if position and inputs and str(inputs[0].topology).split(".")[-1] == "TriangleList":
            triangle = []
            for vertex in sample:
                if vertex.get("primitive_restart"):
                    triangle = []
                    continue
                p = vertex.get(position)
                if p is None or len(p) < 3 or not all(math.isfinite(v) for v in p[:3]):
                    triangle = []
                    continue
                triangle.append(p[:3])
                if len(triangle) == 3:
                    a, b, c = triangle
                    u, v = [b[i] - a[i] for i in range(3)], [c[i] - a[i] for i in range(3)]
                    cross = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
                    degenerate += int(all(x == 0 for x in cross))
                    tested += 1
                    triangle = []
        if degenerate:
            warnings.append("degenerate_position_triangles_may_be_legal_or_unavailable_postvs")
        constants = []
        for mesh in inputs:
            values = [tuple(v[mesh.name]) for v in sample if mesh.name in v]
            if len(values) > 1 and len(set(values)) == 1:
                constants.append(mesh.name)
        position_points = [v[position][:3] for v in sample if position and position in v
                           and len(v[position]) >= 3 and all(math.isfinite(x) for x in v[position][:3])]
        position_bounds = ({"min": [min(p[i] for p in position_points) for i in range(3)],
                            "max": [max(p[i] for p in position_points) for i in range(3)]}
                           if position_points else None)
        return {"sample_offset": offset, "sample_count": len(sample), "total_count": total,
                "nonfinite_components": nonfinite,
                "duplicate_row_count": len(sample) - len(seen),
                "duplicate_row_ratio": (len(sample) - len(seen)) / float(len(sample)) if sample else None,
                "constant_attributes": constants, "uv_semantics": "not_inferred",
                "position_bounds": position_bounds,
                "first_attribute_bounds": box, "position_semantics": "builtin_position" if position else "unverified",
                "position_attribute": position, "triangles_tested": tested,
                "degenerate_triangles": degenerate if tested else None,
                "warnings": warnings}
