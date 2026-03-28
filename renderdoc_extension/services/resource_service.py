"""
Resource information service for RenderDoc.
"""

import os
import base64

import renderdoc as rd

from ..utils import Parsers


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

    @staticmethod
    def _build_paginated_result(items, offset, limit):
        """Build a canonical paginated result payload."""
        total_count = len(items)
        paginated = items[offset:offset + limit]
        return {
            "items": paginated,
            "total_count": total_count,
            "offset": offset,
            "limit": limit,
            "returned_count": len(paginated),
            "has_more": offset + len(paginated) < total_count,
        }

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

    def list_resources(self, resource_type, name_filter=None, offset=0, limit=50):
        """List capture resources using a canonical resource-list interface."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        if resource_type not in ("texture", "buffer"):
            raise ValueError("INVALID_RESOURCE_TYPE: resource_type must be texture or buffer")

        result = {"data": None}

        def callback(controller):
            if resource_type == "texture":
                items = [
                    self._serialize_texture_item(tex)
                    for tex in controller.GetTextures()
                ]
            else:
                items = [
                    self._serialize_buffer_item(buf)
                    for buf in controller.GetBuffers()
                ]

            if name_filter is not None:
                items = [
                    item for item in items
                    if name_filter.lower() in item["name"].lower()
                ]

            result["data"] = self._build_paginated_result(items, offset, limit)
            result["data"]["resource_type"] = resource_type

        self._invoke(callback)
        return result["data"]

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
            tex_save.alpha = alpha_map.get(alpha_mode.lower(), rd.AlphaMapping.Preserve)

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
            tex_save.destType = format_map.get(format_type.upper(), rd.FileType.PNG)

            # Ensure output directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)

            # Save texture
            controller.SaveTexture(tex_save, output_path)

            result["success"] = True
            result["output_path"] = output_path
            result["resource_id"] = Parsers.canonical_resource_id(resource_id)
            result["format"] = format_type.upper()
            result["width"] = tex_desc.width
            result["height"] = tex_desc.height
            result["mip"] = mip
            result["slice"] = slice_index

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result

    def get_buffer_contents(self, resource_id, offset=0, length=0):
        """Get buffer data"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"data": None, "error": None}

        def callback(controller):
            # Parse resource ID
            try:
                rid = Parsers.parse_resource_id(resource_id)
            except Exception:
                result["error"] = "INVALID_RESOURCE_ID: %s" % resource_id
                return

            # Find buffer
            buf_desc = None
            for buf in controller.GetBuffers():
                if buf.resourceId == rid:
                    buf_desc = buf
                    break

            if not buf_desc:
                result["error"] = "BUFFER_NOT_FOUND: %s" % resource_id
                return

            # Get data
            actual_length = length if length > 0 else buf_desc.length
            data = controller.GetBufferData(rid, offset, actual_length)

            result["data"] = {
                "resource_id": Parsers.canonical_resource_id(rid),
                "length": len(data),
                "total_size": buf_desc.length,
                "offset": offset,
                "content_base64": base64.b64encode(data).decode("ascii"),
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
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

    def get_texture_data(self, resource_id, mip=0, slice=0, sample=0, depth_slice=None):
        """Get texture pixel data."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

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
            if slice < 0 or (max_slices > 1 and slice >= max_slices):
                result["error"] = "INVALID_SLICE: %d (texture has %d slices)" % (
                    slice,
                    max_slices,
                )
                return

            # Validate sample for MSAA
            if sample < 0 or (tex_desc.msSamp > 1 and sample >= tex_desc.msSamp):
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
            sub.slice = slice
            sub.sample = sample

            # Get texture data
            try:
                data = controller.GetTextureData(tex_desc.resourceId, sub)
            except Exception as e:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to get texture data: %s" % str(e)
                return

            # Extract depth slice for 3D textures if requested
            output_depth = mip_depth
            if is_3d and depth_slice is not None:
                total_size = len(data)
                bytes_per_slice = total_size // mip_depth
                slice_start = depth_slice * bytes_per_slice
                slice_end = slice_start + bytes_per_slice
                data = data[slice_start:slice_end]
                output_depth = 1

            result["data"] = {
                "resource_id": Parsers.canonical_resource_id(tex_desc.resourceId),
                "width": mip_width,
                "height": mip_height,
                "depth": output_depth,
                "mip": mip,
                "slice": slice,
                "sample": sample,
                "depth_slice": depth_slice,
                "format": str(tex_desc.format.Name()),
                "dimension": str(tex_desc.type),
                "is_3d": is_3d,
                "total_depth": mip_depth if is_3d else 1,
                "data_length": len(data),
                "content_base64": base64.b64encode(data).decode("ascii"),
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]
