"""
Mesh data operations service for RenderDoc.

Provides mesh vertex/index data access and CSV export functionality.
Supports VSIn, VSOut, and GSOut stages.
"""

import csv
import os
import struct
from typing import Any, Optional, List, Dict

import renderdoc as rd


class MeshService:
    """Mesh data operations service"""

    # Format character mapping for struct unpacking
    _FORMAT_CHARS = None

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn
        # Initialize format chars lazily
        self._format_chars = None

    def _get_format_chars(self):
        """Get format character mapping for struct unpacking"""
        if self._format_chars is None:
            self._format_chars = {
                rd.CompType.UInt: "xBHxIxxxL",
                rd.CompType.SInt: "xbhxixxxl",
                rd.CompType.Float: "xxexfxxxd",
                rd.CompType.UNorm: "xBHxIxxxL",
                rd.CompType.UScaled: "xBHxIxxxL",
                rd.CompType.SNorm: "xbhxixxxl",
                rd.CompType.SScaled: "xbhxixxxl",
            }
        return self._format_chars

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
        if offset + required_size > len(buffer_data):
            return tuple([0.0] * fmt.compCount)

        value = struct.unpack_from(vertex_format, buffer_data, offset)

        # Handle normalized formats
        if fmt.compType == rd.CompType.UNorm:
            divisor = float((2 ** (fmt.compByteWidth * 8)) - 1)
            value = tuple(float(i) / divisor for i in value)
        elif fmt.compType == rd.CompType.SNorm:
            max_neg = -float(2 ** (fmt.compByteWidth * 8)) / 2
            divisor = float(-(max_neg - 1))
            value = tuple(
                (float(i) if (i == max_neg) else (float(i) / divisor))
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
        index_format = "B"
        if mesh.indexByteStride == 2:
            index_format = "H"
        elif mesh.indexByteStride == 4:
            index_format = "I"

        index_format = str(mesh.numIndices) + index_format

        if mesh.indexResourceId != rd.ResourceId.Null():
            ib_data = controller.GetBufferData(mesh.indexResourceId, mesh.indexByteOffset, 0)
            offset = mesh.indexOffset * mesh.indexByteStride
            indices = struct.unpack_from(index_format, ib_data, offset)
            return [i + mesh.baseVertex for i in indices]
        else:
            # Non-indexed draw
            return list(range(mesh.numIndices))

    def _get_mesh_inputs(self, controller, draw) -> list:
        """
        Get mesh input data (VSIn stage).

        Args:
            controller: ReplayController
            draw: ActionDescription (draw call)

        Returns:
            List of MeshFormat objects for each vertex attribute
        """
        state = controller.GetPipelineState()
        ib = state.GetIBuffer()
        vbs = state.GetVBuffers()
        attrs = state.GetVertexInputs()

        mesh_inputs = []
        for attr in attrs:
            if attr.perInstance:
                # Skip instanced attributes for now
                continue

            mesh_input = rd.MeshFormat()
            mesh_input.indexResourceId = ib.resourceId
            mesh_input.indexByteOffset = ib.byteOffset
            mesh_input.indexByteStride = ib.byteStride
            mesh_input.baseVertex = draw.baseVertex
            mesh_input.indexOffset = draw.indexOffset
            mesh_input.numIndices = draw.numIndices

            # Check if indexed draw
            if not (draw.flags & rd.ActionFlags.Indexed):
                mesh_input.indexResourceId = rd.ResourceId.Null()

            mesh_input.vertexByteOffset = (
                attr.byteOffset
                + vbs[attr.vertexBuffer].byteOffset
                + draw.vertexOffset * vbs[attr.vertexBuffer].byteStride
            )
            mesh_input.format = attr.format
            mesh_input.vertexResourceId = vbs[attr.vertexBuffer].resourceId
            mesh_input.vertexByteStride = vbs[attr.vertexBuffer].byteStride
            mesh_input.name = attr.name

            mesh_inputs.append(mesh_input)

        return mesh_inputs

    def _get_postvs_data(self, controller, draw, stage: str) -> Any:
        """
        Get post-vertex-shader or post-geometry-shader mesh data.

        Args:
            controller: ReplayController
            draw: ActionDescription
            stage: "VSOut" or "GSOut"

        Returns:
            MeshFormat object or None if not available
        """
        stage_map = {
            "VSOut": rd.MeshDataStage.VSOut,
            "GSOut": rd.MeshDataStage.GSOut,
        }
        mesh_stage = stage_map.get(stage, rd.MeshDataStage.VSOut)

        mesh = controller.GetPostVSData(0, 0, mesh_stage)

        # Check if valid
        if mesh.vertexResourceId == rd.ResourceId.Null():
            return None
        if hasattr(mesh, "status") and mesh.status:
            return None

        return mesh

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

    def get_mesh_summary(self, event_id: int) -> dict:
        """
        Get mesh summary information for an event.

        Args:
            event_id: Event ID of the draw call

        Returns:
            Dict with topology, vertex/index counts, attributes, bounding box
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("No capture loaded")

        result = {"summary": None, "error": None}

        def callback(controller):
            # Set frame event
            controller.SetFrameEvent(event_id, True)

            # Get action
            action = self.ctx.GetAction(event_id)
            if not action:
                result["error"] = f"No action at event {event_id}"
                return

            # Check if it's a draw call
            if not (action.flags & rd.ActionFlags.Drawcall):
                result["error"] = f"Event {event_id} is not a draw call"
                return

            # Get mesh inputs
            mesh_inputs = self._get_mesh_inputs(controller, action)

            # Build attribute info
            attributes = []
            for mesh in mesh_inputs:
                attr_info = {
                    "name": mesh.name,
                    "format": str(mesh.format.Name()),
                    "components": mesh.format.compCount,
                }
                attributes.append(attr_info)

            # Calculate bounding box if POSITION attribute exists
            bounding_box = None
            for mesh in mesh_inputs:
                if "POSITION" in mesh.name.upper() or "POS" in mesh.name.upper():
                    # Batch get buffer data
                    buffer_cache = self._batch_get_buffer_data(controller, [mesh])
                    indices = self._get_indices(controller, mesh_inputs[0])

                    min_pos = [float("inf")] * 3
                    max_pos = [float("-inf")] * 3

                    if mesh.vertexResourceId in buffer_cache:
                        buffer_data = buffer_cache[mesh.vertexResourceId]
                        for idx in indices[:1000]:  # Limit for performance
                            offset = mesh.vertexByteOffset + mesh.vertexByteStride * idx
                            pos = self._unpack_vertex_data(mesh.format, buffer_data, offset)
                            for i in range(min(3, len(pos))):
                                min_pos[i] = min(min_pos[i], pos[i])
                                max_pos[i] = max(max_pos[i], pos[i])

                    if min_pos[0] != float("inf"):
                        bounding_box = {
                            "min": min_pos,
                            "max": max_pos,
                        }
                    break

            # Determine topology
            topology = "Unknown"
            if mesh_inputs:
                topology = str(mesh_inputs[0].topology)

            # Get mesh name from resource
            mesh_name = ""
            if mesh_inputs:
                # Try to get name from vertex buffer first
                for mesh in mesh_inputs:
                    if mesh.vertexResourceId != rd.ResourceId.Null():
                        mesh_name = self._get_resource_name(controller, mesh.vertexResourceId)
                        if mesh_name:
                            break

                # Clean up name (remove common prefixes)
                if mesh_name:
                    import re
                    mesh_name = re.sub(r'^(vb_|VB_|vertexbuffer_|VertexBuffer_)', '', mesh_name)
                    mesh_name = re.sub(r'(_vb|_VB)$', '', mesh_name)

            # Fallback to action name if no resource name
            if not mesh_name:
                mesh_name = getattr(action, 'name', '')

            result["summary"] = {
                "event_id": event_id,
                "name": mesh_name,
                "topology": topology,
                "num_vertices": action.numIndices,
                "num_indices": action.numIndices if action.flags & rd.ActionFlags.Indexed else 0,
                "indexed": bool(action.flags & rd.ActionFlags.Indexed),
                "attributes": attributes,
                "bounding_box": bounding_box,
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["summary"]

    def get_mesh_data(
        self,
        event_id: int,
        stage: str = "VSIn",
        start_offset: int = 0,
        max_vertices: int = 100,
        attributes: Optional[List[str]] = None,
    ) -> dict:
        """
        Get mesh vertex and index data for a specific draw call.

        Args:
            event_id: Event ID of the draw call
            stage: Mesh data stage - "VSIn", "VSOut", or "GSOut"
            start_offset: Starting vertex offset for pagination (default: 0)
            max_vertices: Maximum number of vertices to return (default: 100, recommended: 100-500)
            attributes: Optional list of attribute names to include

        Returns:
            Dict with vertices, indices, topology, attribute info, total_count, has_more
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("No capture loaded")

        if stage not in ["VSIn", "VSOut", "GSOut"]:
            raise ValueError(f"Invalid stage: {stage}. Must be VSIn, VSOut, or GSOut")

        result = {"data": None, "error": None}

        def callback(controller):
            # Set frame event
            controller.SetFrameEvent(event_id, True)

            # Get action
            action = self.ctx.GetAction(event_id)
            if not action:
                result["error"] = f"No action at event {event_id}"
                return

            # Check if it's a draw call
            if not (action.flags & rd.ActionFlags.Drawcall):
                result["error"] = f"Event {event_id} is not a draw call"
                return

            # Get mesh data based on stage
            if stage == "VSIn":
                mesh_inputs = self._get_mesh_inputs(controller, action)
                if not mesh_inputs:
                    result["error"] = f"No mesh input data available for event {event_id}"
                    return
            else:
                # VSOut or GSOut
                postvs_mesh = self._get_postvs_data(controller, action, stage)
                if not postvs_mesh:
                    result["error"] = f"No {stage} data available for event {event_id}"
                    return
                # For post-VS, we need to get attribute info from shader reflection
                mesh_inputs = [postvs_mesh]

            # Filter attributes if specified
            if attributes and stage == "VSIn":
                attr_names_lower = [a.lower() for a in attributes]
                mesh_inputs = [
                    m for m in mesh_inputs
                    if any(n in m.name.lower() for n in attr_names_lower)
                ]
                if not mesh_inputs:
                    result["error"] = f"No matching attributes found: {attributes}"
                    return

            # Get indices
            if stage == "VSIn":
                all_indices = self._get_indices(controller, mesh_inputs[0])
            else:
                # For VSOut/GSOut, indices are typically sequential
                all_indices = list(range(mesh_inputs[0].numIndices))

            # Calculate pagination info
            total_count = len(all_indices)
            has_more = (start_offset + max_vertices) < total_count

            # Apply pagination
            end_offset = min(start_offset + max_vertices, total_count)
            indices = all_indices[start_offset:end_offset]
            truncated = total_count > max_vertices

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
                })

            # Process each vertex
            for idx in indices:
                vertex = {}
                for mesh in mesh_inputs:
                    if mesh.vertexResourceId == rd.ResourceId.Null():
                        continue

                    if mesh.vertexResourceId in buffer_cache:
                        buffer_data = buffer_cache[mesh.vertexResourceId]
                        offset = mesh.vertexByteOffset + mesh.vertexByteStride * idx
                        values = self._unpack_vertex_data(mesh.format, buffer_data, offset)

                        # Store as list
                        vertex[mesh.name] = list(values)[: mesh.format.compCount]

                vertices.append(vertex)

            # Determine topology
            topology = "Unknown"
            if mesh_inputs:
                topology = str(mesh_inputs[0].topology)

            result["data"] = {
                "event_id": event_id,
                "stage": stage,
                "topology": topology,
                "total_count": total_count,
                "start_offset": start_offset,
                "num_vertices": len(vertices),
                "num_indices": len(indices),
                "has_more": has_more,
                "truncated": truncated,
                "attributes": attribute_info,
                "vertices": vertices,
                "indices": list(indices) if stage == "VSIn" else [],
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]

    def export_mesh_csv(
        self,
        event_id: int,
        output_path: str,
        stage: str = "VSIn",
        include_attributes: Optional[List[str]] = None,
    ) -> dict:
        """
        Export mesh data to CSV file.

        The CSV format is compatible with csv_obj project:
        - First row is header: VTX,IDX,attr1.x,attr1.y,attr1.z,...
        - VTX: remapped vertex index (0-based)
        - IDX: original vertex index
        - Attribute columns: {attribute_name}.{component}

        Args:
            event_id: Event ID of the draw call
            output_path: Output CSV file path
            stage: Mesh data stage - "VSIn", "VSOut", or "GSOut"
            include_attributes: Optional list of attributes to include

        Returns:
            Dict with success status and export info
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("No capture loaded")

        if stage not in ["VSIn", "VSOut", "GSOut"]:
            raise ValueError(f"Invalid stage: {stage}. Must be VSIn, VSOut, or GSOut")

        result = {"success": False, "error": None}

        def callback(controller):
            # Set frame event
            controller.SetFrameEvent(event_id, True)

            # Get action
            action = self.ctx.GetAction(event_id)
            if not action:
                result["error"] = f"No action at event {event_id}"
                return

            # Check if it's a draw call
            if not (action.flags & rd.ActionFlags.Drawcall):
                result["error"] = f"Event {event_id} is not a draw call"
                return

            # Get mesh data based on stage
            if stage == "VSIn":
                mesh_inputs = self._get_mesh_inputs(controller, action)
                if not mesh_inputs:
                    result["error"] = f"No mesh input data available for event {event_id}"
                    return
            else:
                postvs_mesh = self._get_postvs_data(controller, action, stage)
                if not postvs_mesh:
                    result["error"] = f"No {stage} data available for event {event_id}"
                    return
                mesh_inputs = [postvs_mesh]

            # Filter attributes if specified
            if include_attributes and stage == "VSIn":
                attr_names_lower = [a.lower() for a in include_attributes]
                mesh_inputs = [
                    m for m in mesh_inputs
                    if any(n in m.name.lower() for n in attr_names_lower)
                ]
                if not mesh_inputs:
                    result["error"] = f"No matching attributes found: {include_attributes}"
                    return

            # Get indices
            if stage == "VSIn":
                indices = self._get_indices(controller, mesh_inputs[0])
            else:
                indices = list(range(mesh_inputs[0].numIndices))

            # Batch get buffer data
            buffer_cache = self._batch_get_buffer_data(controller, mesh_inputs)

            # Build CSV data
            component_suffixes = [".x", ".y", ".z", ".w"]

            # Build header
            header = ["VTX", "IDX"]
            for mesh in mesh_inputs:
                if mesh.format.Special():
                    continue
                for i in range(mesh.format.compCount):
                    header.append(f"{mesh.name}{component_suffixes[i]}")

            # Process vertices with deduplication
            unique_vertices = {}  # {original_idx: [attr_values...]}
            triangle_stream = []  # remapped indices

            for idx in indices:
                if idx not in unique_vertices:
                    attribute_values = []
                    for mesh in mesh_inputs:
                        if mesh.format.Special():
                            continue
                        if mesh.vertexResourceId in buffer_cache:
                            buffer_data = buffer_cache[mesh.vertexResourceId]
                            offset = mesh.vertexByteOffset + mesh.vertexByteStride * idx
                            values = self._unpack_vertex_data(mesh.format, buffer_data, offset)
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
            for idx in indices:
                if idx in remap:
                    triangle_stream.append(remap[idx])

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
                    idx_file.write(f"{remapped_idx}\n")

            result["success"] = True
            result["output_path"] = output_path
            result["index_path"] = index_path
            result["vertex_count"] = len(unique_vertices)
            result["index_count"] = len(triangle_stream)
            result["stage"] = stage
            result["format"] = "CSV"

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result
