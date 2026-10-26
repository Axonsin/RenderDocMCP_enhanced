"""
Resource information service for RenderDoc.
"""

import os
import base64

import renderdoc as rd

from .replay_query import at_event, guard_for
from .texture_export import select as select_texture, transport as transport_texture
from .texture_values import MAX_SUBRESOURCE_BYTES, decoder

from ..utils import Parsers
from .resource_catalog import (
    build_catalog, enum_name, identity, paginate, query_usage,
    resolve_resource, resource_type as type_name, validate_page,
)
from .structured_data import read_node

# Inline responses stay small enough for the MCP transport; callers page with
# offset/length for larger buffers.
MAX_INLINE_BYTES = 256 * 1024


class ResourceService:
    """Resource information service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    @staticmethod
    def _parse_buffer_flags(flags):
        """Parse BufferCategory flags to human-readable list"""
        flag_names = []
        if flags & rd.BufferCategory.Vertex:
            flag_names.append("Vertex")
        if flags & rd.BufferCategory.Index:
            flag_names.append("Index")
        if flags & rd.BufferCategory.Constants:
            flag_names.append("Constants")
        if flags & rd.BufferCategory.ReadWrite:
            flag_names.append("ReadWrite")
        if flags & rd.BufferCategory.Indirect:
            flag_names.append("Indirect")
        if not flag_names:
            flag_names.append("None")
        return flag_names

    def _serialize_texture_item(self, tex):
        """Serialize texture descriptor to a canonical resource item."""
        name = ""
        try:
            name = self.ctx.GetResourceName(tex.resourceId)
        except Exception:
            pass

        return {
            "resource_type": "texture",
            "resource_id": Parsers.canonical_resource_id(tex.resourceId),
            "name": name,
            "width": tex.width,
            "height": tex.height,
            "depth": tex.depth,
            "format": str(tex.format.Name()),
            "mip_levels": tex.mips,
            "array_size": tex.arraysize,
            "byte_size": tex.byteSize,
            "dimension": str(tex.type),
            "cubemap": tex.cubemap,
            "msaa_samples": tex.msSamp,
        }

    def _serialize_buffer_item(self, buf):
        """Serialize buffer descriptor to a canonical resource item."""
        name = ""
        try:
            name = self.ctx.GetResourceName(buf.resourceId)
        except Exception:
            pass

        return {
            "resource_type": "buffer",
            "resource_id": Parsers.canonical_resource_id(buf.resourceId),
            "name": name,
            "byte_size": buf.length,
            "creation_flags": self._parse_buffer_flags(buf.creationFlags),
        }

    def _query(self, operation):
        """Run a read-only query once on the replay thread."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        result = {}

        def callback(controller):
            # Propagate explicitly: SWIG callbacks may not propagate Python exceptions.
            try:
                result["data"] = operation(controller)
            except Exception as exc:
                result["error"] = exc

        self._invoke(callback)
        if "error" in result:
            raise result["error"]
        return result["data"]

    def list_resources(self, resource_type="all", name_filter=None, offset=0,
                       limit=50, sort_by="name"):
        """List all API objects, with compact identities and stable pagination."""
        validate_page(offset, limit)
        kinds = {type_name(value) for value in rd.ResourceType}
        if resource_type not in kinds | {"all"}:
            raise ValueError("INVALID_RESOURCE_TYPE: unknown type: %s" % resource_type)
        if sort_by not in ("name", "resource_id"):
            raise ValueError("INVALID_SORT: expected name or resource_id")

        def operation(controller):
            catalog = build_catalog(controller, descriptors=False)
            items = [identity(self.ctx, res.resourceId, catalog)
                     for res in catalog["resources"].values()]
            items = [item for item in items
                     if (resource_type == "all" or item["resource_type"] == resource_type)
                     and (name_filter is None or name_filter.lower() in item["name"].lower())]
            items.sort(key=lambda item: (
                item["name"].casefold() if sort_by == "name" else "",
                Parsers.extract_numeric_id(item["resource_id"])))
            result = paginate(items, offset, limit)
            result["resource_type"] = resource_type
            return result
        return self._query(operation)

    def _metadata(self, resource, catalog):
        numeric = int(resource.resourceId)
        if numeric in catalog["textures"]:
            data = self._serialize_texture_item(catalog["textures"][numeric])
        elif numeric in catalog["buffers"]:
            data = self._serialize_buffer_item(catalog["buffers"][numeric])
        else:
            return {}
        return {key: value for key, value in data.items()
                if key not in ("name", "resource_id", "resource_type")}

    def _initialization_directory(self, resource, structured_file, offset, limit):
        indices = list(resource.initialisationChunks)
        result = paginate(indices, offset, limit)
        result["available"] = True
        items = []
        for index in result["items"]:
            if 0 <= index < len(structured_file.chunks):
                chunk = structured_file.chunks[index]
                items.append({"chunk_index": int(index), "name": str(chunk.name),
                              "child_count": chunk.NumChildren()})
            else:
                items.append({"chunk_index": int(index),
                              "error": "INVALID_CHUNK_INDEX"})
        result["items"] = items
        return result

    def inspect_resource(self, resource_id, related_offset=0, related_limit=50):
        """Inspect identity, metadata, immediate relations and compact summaries."""
        validate_page(related_offset, related_limit)

        def operation(controller):
            catalog = build_catalog(controller)
            resource = resolve_resource(resource_id, catalog)
            related = []
            for relationship, ids in (("parent", resource.parentResources),
                                      ("derived", resource.derivedResources)):
                group = []
                for rid in ids:
                    item = identity(self.ctx, rid, catalog)
                    item["relationship"] = relationship
                    group.append(item)
                group.sort(key=lambda item: (item["name"].casefold(),
                                             Parsers.extract_numeric_id(item["resource_id"])))
                related.extend(group)
            result = {
                "resource": identity(self.ctx, resource.resourceId, catalog),
                "metadata": self._metadata(resource, catalog),
                "related_resources": paginate(related, related_offset, related_limit),
            }
            try:
                status, usages = query_usage(controller, resource, catalog)
                if status["available"]:
                    counts = {}
                    for usage in usages:
                        name = enum_name(usage.usage)
                        counts[name] = counts.get(name, 0) + 1
                    status.update({"usage_count": len(usages),
                                   "event_count": len({u.eventId for u in usages}),
                                   "usage_counts": counts})
                result["usage"] = status
            except Exception as exc:
                result["usage"] = {"available": False, "reason": "query_failed",
                                   "error": str(exc)}
            try:
                result["initialization"] = self._initialization_directory(
                    resource, controller.GetStructuredFile(), 0, 20)
            except Exception as exc:
                result["initialization"] = {
                    "available": False, "reason": "query_failed", "error": str(exc)}
            return result
        return self._query(operation)

    def get_resource_initialization(self, resource_id, chunk_index=None,
                                    child_path=None, offset=0, limit=50):
        """List initialization calls or expand one parameter node by raw indices."""
        validate_page(offset, limit)
        if child_path is not None and (
                not isinstance(child_path, list) or
                any(type(i) is not int or i < 0 for i in child_path)):
            raise ValueError("INVALID_CHILD_PATH: expected non-negative child indices")
        if chunk_index is not None and (type(chunk_index) is not int or chunk_index < 0):
            raise ValueError("INVALID_CHUNK_INDEX: expected a non-negative integer")
        if chunk_index is None and child_path:
            raise ValueError("INVALID_CHILD_PATH: chunk_index is required")

        def operation(controller):
            catalog = build_catalog(controller, descriptors=False)
            resource = resolve_resource(resource_id, catalog)
            structured_file = controller.GetStructuredFile()
            if chunk_index is None:
                result = self._initialization_directory(resource, structured_file, offset, limit)
            else:
                if (chunk_index not in resource.initialisationChunks or
                        chunk_index >= len(structured_file.chunks)):
                    raise ValueError("INVALID_CHUNK_INDEX: chunk does not belong to this resource")
                result = read_node(structured_file.chunks[chunk_index],
                                   [] if child_path is None else child_path,
                                   self.ctx, catalog, offset, limit)
                result["chunk_index"] = chunk_index
            result["resource"] = identity(self.ctx, resource.resourceId, catalog)
            return result
        return self._query(operation)

    def _find_texture_by_id(self, controller, resource_id):
        """Find texture by resource ID"""
        target_id = Parsers.extract_numeric_id(resource_id)
        for tex in controller.GetTextures():
            tex_id_str = str(tex.resourceId)
            tex_id = Parsers.extract_numeric_id(tex_id_str)
            if tex_id == target_id:
                return tex
        return None

    def save_texture(
        self,
        resource_id,
        output_path,
        format_type="PNG",
        mip=0,
        slice_index=0,
        alpha_mode="preserve",
        action_event_id=None,
    ):
        """
        Save texture to file.

        Args:
            resource_id: The resource ID of the texture (e.g. "ResourceId::2495")
            output_path: Output file path
            format_type: Output format (PNG, JPG, BMP, TGA, EXR, DDS, HDR)
            mip: Mip level to save (-1 for all mips)
            slice_index: Array slice or cube face index
            alpha_mode: Alpha handling (preserve, discard, blend_to_black)

        Returns:
            dict with success status and texture info
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"success": False, "error": None}

        def callback(controller):
            # Find texture
            tex_desc = self._find_texture_by_id(controller, resource_id)
            if not tex_desc:
                result["error"] = "TEXTURE_NOT_FOUND: %s" % resource_id
                return

            # Create TextureSave configuration
            tex_save = rd.TextureSave()
            tex_save.resourceId = tex_desc.resourceId
            tex_save.mip = mip
            tex_save.slice.sliceIndex = slice_index

            # Set alpha mode
            alpha_map = {
                "preserve": rd.AlphaMapping.Preserve,
                "discard": rd.AlphaMapping.Discard,
                "blend_to_black": rd.AlphaMapping.BlendToColor,
            }
            alpha_key = (alpha_mode or "").lower()
            if alpha_key not in alpha_map:
                raise ValueError(
                    "INVALID_ALPHA_MODE: %s (must be preserve, discard, or blend_to_black)"
                    % alpha_mode
                )
            tex_save.alpha = alpha_map[alpha_key]

            # Set output format
            format_map = {
                "PNG": rd.FileType.PNG,
                "JPG": rd.FileType.JPG,
                "JPEG": rd.FileType.JPG,
                "BMP": rd.FileType.BMP,
                "TGA": rd.FileType.TGA,
                "EXR": rd.FileType.EXR,
                "DDS": rd.FileType.DDS,
                "HDR": rd.FileType.HDR,
            }
            format_key = (format_type or "").upper()
            if format_key not in format_map:
                raise ValueError(
                    "INVALID_FORMAT_TYPE: %s (must be PNG, JPG, BMP, TGA, EXR, DDS, or HDR)"
                    % format_type
                )
            tex_save.destType = format_map[format_key]

            # Ensure output directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)

            # Save texture
            saved = controller.SaveTexture(tex_save, output_path)
            if not saved.OK():
                raise RuntimeError("TEXTURE_SAVE_FAILED: %s" % saved.Message())

            result["success"] = True
            result["output_path"] = output_path
            result["resource_id"] = Parsers.canonical_resource_id(resource_id)
            result["format"] = format_key
            result["width"] = tex_desc.width
            result["height"] = tex_desc.height
            result["mip"] = mip
            if mip < 0:
                # RenderDoc writes every mip only for DDS; other formats fall
                # back to mip 0, so report the mip that was actually saved.
                if format_key == "DDS":
                    result["mip_selection"] = "all"
                else:
                    result["mip_selection"] = 0
                    result["mip_note"] = (
                        "mip=-1 saves all mips only for DDS; saved mip 0"
                    )
            result["slice_index"] = slice_index
            result["color_space"] = (
                "srgb"
                if tex_desc.format.compType == rd.CompType.UNormSRGB
                else "linear"
            )

        def scoped(controller, event):
            callback(controller)
            if "data" in result and isinstance(result["data"], dict):
                result["data"]["action_event_id" if action_event_id is not None else "event_id"] = event
                result["data"]["event_phase"] = "after"
            else:
                result["action_event_id" if action_event_id is not None else "event_id"] = event
                result["event_phase"] = "after"
        at_event(self.ctx, self._invoke, action_event_id, scoped)

        if result["error"]:
            raise ValueError(result["error"])
        return result

    def get_buffer_contents(self, resource_id, offset=0, length=0, action_event_id=None):
        """Get buffer data"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        if type(offset) is not int or offset < 0:
            raise ValueError("INVALID_PAGINATION: offset must be a non-negative byte offset")
        if type(length) is not int or length < 0:
            raise ValueError("INVALID_PAGINATION: length must be a non-negative byte count")

        result = {"data": None, "error": None}

        def callback(controller):
            # Compare numeric IDs. Constructing a ResourceId from an int is not
            # supported by the bindings (only default/copy constructors exist),
            # and assigning `.id` leaves the underlying value null, so an ID
            # equality check can never match.
            try:
                numeric = Parsers.extract_numeric_id(resource_id)
                if numeric <= 0:
                    raise ValueError()
            except (TypeError, ValueError):
                result["error"] = "INVALID_RESOURCE_ID: %s" % resource_id
                return

            def find_buffer():
                try:
                    for buf in controller.GetBuffers():
                        try:
                            if int(buf.resourceId) == numeric:
                                size = getattr(buf, "length", None)
                                if size is None:
                                    raise ValueError("buffer descriptor has no length")
                                return buf, int(size)
                        except (TypeError, OverflowError):
                            continue
                except AttributeError:
                    pass
                # ResourceDescription has no size field in the real API.
                # Only accept explicitly typed buffer descriptors with a known
                # length from adapters; never treat a texture byteSize as a buffer.
                try:
                    for res in controller.GetResources():
                        try:
                            if int(res.resourceId) != numeric:
                                continue
                            if str(getattr(res, "type", "")).split(".")[-1] != "Buffer":
                                continue
                            size = getattr(res, "length", None)
                            if size is None:
                                size = getattr(res, "byteSize", None)
                            if size is not None:
                                return res, int(size)
                            raise ValueError("buffer size unavailable in ResourceDescription")
                        except ValueError:
                            raise
                        except Exception:
                            continue
                except AttributeError:
                    pass
                return None, 0

            try:
                buf_desc, total_size = find_buffer()
                if not buf_desc:
                    result["error"] = "BUFFER_NOT_FOUND: %s" % resource_id
                    return
                if offset > total_size:
                    result["error"] = (
                        "INVALID_PAGINATION: offset %d exceeds buffer size %d"
                        % (offset, total_size)
                    )
                    return

                requested = (length if length > 0 else total_size - offset)
                available = max(0, total_size - offset)
                actual_length = min(requested, available, MAX_INLINE_BYTES)
                # RenderDoc defines len=0 as 'read to end', not an empty read.
                data = (controller.GetBufferData(buf_desc.resourceId, offset, actual_length)
                        if actual_length else b"")
                if actual_length and not data:
                    raise ValueError("buffer read returned no bytes before end of buffer")
                data = data[:actual_length]
                consumed = offset + len(data)
                truncated = len(data) < requested
                result["data"] = {
                    "resource_id": Parsers.canonical_resource_id(buf_desc.resourceId),
                    "length": len(data),
                    "total_size": total_size,
                    "offset": offset,
                    "read_range": {"byte_offset": offset, "byte_length": len(data),
                                   "end_exclusive": offset + len(data)},
                    "requested_bytes": requested,
                    "truncated": truncated,
                    "next_offset": consumed if truncated and consumed < total_size else None,
                    "max_inline_bytes": MAX_INLINE_BYTES,
                    "content_base64": base64.b64encode(data).decode("ascii"),
                }
            except Exception as exc:
                # Exceptions must survive the SWIG BlockInvoke callback boundary.
                result["error"] = "RESOURCE_QUERY_FAILED: failed to get buffer data: %s" % str(exc)

        def scoped(controller, event):
            callback(controller)
            if result["data"] is not None:
                result["data"]["action_event_id" if action_event_id is not None else "event_id"] = event
                result["data"]["event_phase"] = "after"
                result["data"]["source"] = "raw_buffer"
        at_event(self.ctx, self._invoke, action_event_id, scoped)

        if result["error"]:
            raise ValueError(result["error"])
        result["data"]["replay_restored"] = True
        return result["data"]

    def get_texture_info(self, resource_id):
        """Get texture metadata"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"texture": None, "error": None}

        def callback(controller):
            try:
                tex_desc = self._find_texture_by_id(controller, resource_id)

                if not tex_desc:
                    result["error"] = "TEXTURE_NOT_FOUND: %s" % resource_id
                    return

                result["texture"] = {
                    "resource_id": Parsers.canonical_resource_id(tex_desc.resourceId),
                    "width": tex_desc.width,
                    "height": tex_desc.height,
                    "depth": tex_desc.depth,
                    "array_size": tex_desc.arraysize,
                    "mip_levels": tex_desc.mips,
                    "format": str(tex_desc.format.Name()),
                    "dimension": str(tex_desc.type),
                    "msaa_samples": tex_desc.msSamp,
                    "byte_size": tex_desc.byteSize,
                }
            except Exception as e:
                import traceback
                result["error"] = "RESOURCE_QUERY_FAILED: %s\n%s" % (str(e), traceback.format_exc())

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["texture"]

    def get_texture_data(self, resource_id, mip=0, slice_index=0, sample=0, depth_slice=None, action_event_id=None,
                         output_mode="auto", output_dir=None, aspect="all", region=None):
        """Get texture pixel data."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        if output_mode not in ("auto", "inline", "file") or aspect not in ("all", "depth", "stencil"):
            raise ValueError("INVALID_REQUEST: invalid texture output_mode or aspect")
        result = {"data": None, "error": None}

        def callback(controller):
            tex_desc = self._find_texture_by_id(controller, resource_id)

            if not tex_desc:
                result["error"] = "TEXTURE_NOT_FOUND: %s" % resource_id
                return

            # Validate mip level
            if mip < 0 or mip >= tex_desc.mips:
                result["error"] = "INVALID_MIP_LEVEL: %d (texture has %d mips)" % (
                    mip,
                    tex_desc.mips,
                )
                return

            # Validate slice for array/cube textures
            max_slices = tex_desc.arraysize
            if tex_desc.cubemap:
                max_slices = tex_desc.arraysize * 6
            if slice_index < 0 or slice_index >= max_slices:
                result["error"] = "INVALID_SLICE: %d (texture has %d slices)" % (
                    slice_index,
                    max_slices,
                )
                return

            # Validate sample for MSAA
            if sample < 0 or sample >= max(1, tex_desc.msSamp):
                result["error"] = "INVALID_SAMPLE: %d (texture has %d samples)" % (
                    sample,
                    tex_desc.msSamp,
                )
                return

            # Calculate dimensions at this mip level
            mip_width = max(1, tex_desc.width >> mip)
            mip_height = max(1, tex_desc.height >> mip)
            mip_depth = max(1, tex_desc.depth >> mip)

            # Validate depth_slice for 3D textures
            is_3d = tex_desc.depth > 1
            if depth_slice is not None:
                if not is_3d:
                    result["error"] = "INVALID_DEPTH_SLICE: depth_slice can only be used with 3D textures"
                    return
                if depth_slice < 0 or depth_slice >= mip_depth:
                    result["error"] = "INVALID_DEPTH_SLICE: %d (texture has %d depth at mip %d)" % (
                        depth_slice,
                        mip_depth,
                        mip,
                    )
                    return

            # Create subresource specification
            sub = rd.Subresource()
            sub.mip = mip
            sub.slice = slice_index
            sub.sample = sample

            # Reject known oversized subresources before native readback.
            try:
                size = decoder(tex_desc.format)[0]
                if mip_width*mip_height*mip_depth*size > MAX_SUBRESOURCE_BYTES:
                    raise ValueError("RESOURCE_LIMIT: raw subresource exceeds 64 MiB")
            except (AttributeError, ValueError) as exc:
                if str(exc).startswith("RESOURCE_LIMIT:"):
                    raise
            # Get texture data
            try:
                data = controller.GetTextureData(tex_desc.resourceId, sub)
            except Exception as e:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to get texture data: %s" % str(e)
                return

            data = bytes(data)
            source_data_length = len(data)
            if not data:
                raise ValueError("RESOURCE_QUERY_FAILED: empty texture subresource readback")
            if len(data) > MAX_SUBRESOURCE_BYTES:
                raise ValueError("RESOURCE_LIMIT: raw subresource exceeds 64 MiB")
            # Extract depth slice for 3D textures if requested
            output_depth = mip_depth
            if is_3d and depth_slice is not None:
                total_size = len(data)
                bytes_per_slice = total_size // mip_depth
                slice_start = depth_slice * bytes_per_slice
                slice_end = slice_start + bytes_per_slice
                data = data[slice_start:slice_end]
                output_depth = 1

            api = str(controller.GetAPIProperties().pipelineType).split(".")[-1]
            data, layout, selected_width, selected_height = select_texture(data, tex_desc.format, mip_width, mip_height, output_depth, aspect, region, api in ("Vulkan", "D3D11", "D3D12"))
            layout["api"] = api
            # Data diagnostics: zero-length indicates an unreadable subresource;
            # all-zero bytes can be legitimate (cleared resource) but is worth flagging.
            warnings = []
            all_zero = False
            if len(data) == 0:
                warnings.append(
                    "Texture data returned 0 bytes; the subresource may be unreadable "
                    "(replay or driver issue)."
                )
            else:
                all_zero = not any(data)
                if all_zero:
                    warnings.append(
                        "All data bytes are zero. This can be legitimate (cleared resource) "
                        "or a symptom of a replay problem; verify against the texture viewer."
                    )

            result["data"] = {
                "resource_id": Parsers.canonical_resource_id(tex_desc.resourceId),
                "width": mip_width,
                "height": mip_height,
                "depth": output_depth,
                "mip": mip,
                "slice_index": slice_index,
                "sample": sample,
                "depth_slice": depth_slice,
                "format": str(tex_desc.format.Name()),
                "dimension": str(tex_desc.type),
                "is_3d": is_3d,
                "total_depth": mip_depth if is_3d else 1,
                "color_space": (
                    "srgb"
                    if tex_desc.format.compType == rd.CompType.UNormSRGB
                    else "linear"
                ),
                "data_length": len(data),
                "source_data_length": source_data_length,
                "source_dimensions": [mip_width, mip_height, mip_depth],
                "all_zero": all_zero,
                "_raw": data,
            }
            result["data"].update(layout, width=selected_width, height=selected_height)
            if warnings:
                result["data"]["warnings"] = warnings

        def scoped(controller, event):
            callback(controller)
            if "data" in result and isinstance(result["data"], dict):
                result["data"]["action_event_id" if action_event_id is not None else "event_id"] = event
                result["data"]["event_phase"] = "after"
            else:
                result["action_event_id" if action_event_id is not None else "event_id"] = event
                result["event_phase"] = "after"
        at_event(self.ctx, self._invoke, action_event_id, scoped)

        if result["error"]:
            raise ValueError(result["error"])
        metadata = result["data"]
        guard = guard_for(self.ctx)
        session = guard.session.capture_session if guard else "unknown"
        if guard:
            metadata["provenance"] = guard.session.describe()
            guard.phase("texture_transport", readback_bytes=metadata["source_data_length"], output_bytes=len(metadata["_raw"]))
        raw = metadata.pop("_raw")
        return transport_texture(raw, metadata, output_mode, output_dir, session)
