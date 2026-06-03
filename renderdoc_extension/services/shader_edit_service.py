"""
Shader edit and replacement service for RenderDoc.
"""

import hashlib
import json
import os
import re
import tempfile

import renderdoc as rd

from ..utils import Parsers


class ShaderEditService:
    """Shader edit/replacement operations."""

    _TEXT_SHADER_ENCODINGS = {
        "GLSL",
        "HLSL",
        "Slang",
        "SPIRVAsm",
        "OpenGLSPIRVAsm",
    }

    _KNOWN_SHADER_ENCODINGS = [
        "Unknown",
        "DXBC",
        "GLSL",
        "SPIRV",
        "SPIRVAsm",
        "HLSL",
        "DXIL",
        "OpenGLSPIRV",
        "OpenGLSPIRVAsm",
        "Slang",
    ]

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn
        self._resource_id_cache = {}

    def get_shader_edit_context(
        self,
        event_id,
        stage,
        materialize=True,
        max_inline_chars=2000,
    ):
        """Create a file-first shader editing context for one event/stage."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        max_inline_chars = self._safe_int(max_inline_chars, 2000)
        result = {"data": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            reflection = shader_ctx["reflection"]
            encoding_name = "Unknown"
            raw_bytes = None
            source_text = None
            source_reason = ""
            warnings = []

            if reflection:
                encoding_name = self._get_shader_encoding_name(reflection.encoding)
                raw_bytes = reflection.rawBytes

            if not reflection:
                source_reason = "Shader reflection/source bytes unavailable"
            elif not raw_bytes:
                source_reason = "Shader source payload is empty"
            elif encoding_name in self._TEXT_SHADER_ENCODINGS:
                try:
                    source_text = raw_bytes.decode("utf-8-sig")
                except UnicodeDecodeError as exc:
                    source_reason = (
                        "Failed to decode %s shader source as UTF-8: %s"
                        % (encoding_name, exc)
                    )
                    warnings.append(source_reason)
            else:
                source_reason = (
                    "Original source text is not available for %s shaders"
                    % encoding_name
                )

            disassembly_text = ""
            disassembly_error = ""
            if reflection:
                try:
                    targets = controller.GetDisassemblyTargets(True)
                    if targets:
                        pipeline_obj = (
                            shader_ctx["pipe"].GetComputePipelineObject()
                            if shader_ctx["stage_enum"] == rd.ShaderStage.Compute
                            else shader_ctx["pipe"].GetGraphicsPipelineObject()
                        )
                        disassembly_text = controller.DisassembleShader(
                            pipeline_obj, reflection, targets[0]
                        )
                    else:
                        disassembly_error = "No disassembly targets available"
                except Exception as exc:
                    disassembly_error = str(exc)
                    warnings.append("Failed to disassemble shader: %s" % str(exc))
            else:
                disassembly_error = "Shader reflection unavailable"

            result["data"] = {
                "event_id": int(event_id),
                "stage": shader_ctx["stage_name"],
                "stage_enum": shader_ctx["stage_enum"],
                "resource_id": shader_ctx["resource_id"],
                "entry_point": shader_ctx["entry_point"],
                "encoding": encoding_name,
                "source_text": source_text,
                "source_available": source_text is not None,
                "source_reason": source_reason,
                "disassembly_text": disassembly_text or "",
                "disassembly_error": disassembly_error,
                "target_shader_encodings": self._shader_encoding_names(
                    controller.GetTargetShaderEncodings()
                ),
                "output_textures": self._collect_output_textures(
                    shader_ctx["pipe"]
                ),
                "warnings": warnings,
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return self._materialize_context(
            result["data"],
            bool(materialize),
            max_inline_chars,
        )

    def build_shader_replacement(
        self,
        event_id,
        stage,
        source_path=None,
        source_text=None,
        encoding=None,
        entry_point=None,
    ):
        """Compile a replacement shader without applying it."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        source_bytes = self._load_replacement_source(source_path, source_text)
        result = {"data": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            reflection = shader_ctx["reflection"]
            selected_encoding = encoding
            if selected_encoding is None and reflection:
                selected_encoding = self._get_shader_encoding_name(reflection.encoding)
            if selected_encoding is None:
                result["error"] = (
                    "INVALID_ENCODING: encoding is required when shader "
                    "reflection is unavailable"
                )
                return

            try:
                source_encoding = self._parse_shader_encoding(selected_encoding)
            except ValueError as exc:
                result["error"] = str(exc)
                return

            selected_entry = entry_point or shader_ctx["entry_point"]
            compile_flags = rd.ShaderCompileFlags()

            try:
                replacement_id, compiler_output = controller.BuildTargetShader(
                    selected_entry,
                    source_encoding,
                    source_bytes,
                    compile_flags,
                    shader_ctx["stage_enum"],
                )
            except Exception as exc:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to build shader: %s" % str(exc)
                return

            success = replacement_id != rd.ResourceId.Null()
            if success:
                self._cache_resource_id(shader_ctx["shader"])
                self._cache_resource_id(replacement_id)
            result["data"] = {
                "success": success,
                "event_id": int(event_id),
                "stage": shader_ctx["stage_name"],
                "original_resource_id": shader_ctx["resource_id"],
                "replacement_resource_id": (
                    Parsers.canonical_resource_id(replacement_id)
                    if success
                    else None
                ),
                "entry_point": selected_entry,
                "encoding": self._get_shader_encoding_name(source_encoding),
                "compiler_output": compiler_output or "",
                "source_path": source_path,
                "context_dir": self._context_dir_for_shader(
                    shader_ctx["stage_name"],
                    shader_ctx["resource_id"],
                    int(event_id),
                ),
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])

        self._write_compile_log(result["data"])
        return result["data"]

    def apply_shader_replacement(self, original_resource_id, replacement_resource_id):
        """Apply a compiled replacement shader."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"success": False, "error": None}
        replacement_state = {"original": None, "replacement": None}

        def callback(controller):
            try:
                original = self._resolve_resource_id(controller, original_resource_id)
                replacement = self._resolve_resource_id(controller, replacement_resource_id)
            except ValueError as exc:
                result["error"] = str(exc)
                return

            try:
                controller.ReplaceResource(original, replacement)
                controller.ClearReplayCache()
                replacement_state["original"] = original
                replacement_state["replacement"] = replacement
                result["success"] = True
                result["original_resource_id"] = Parsers.canonical_resource_id(original)
                result["replacement_resource_id"] = Parsers.canonical_resource_id(replacement)
            except Exception as exc:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to replace resource: %s" % str(exc)

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])

        try:
            self.ctx.RegisterReplacement(
                replacement_state["original"],
                replacement_state["replacement"],
            )
            self.ctx.RefreshStatus()
        except Exception as exc:
            raise ValueError(
                "RESOURCE_QUERY_FAILED: failed to sync replacement status: %s"
                % str(exc)
            )

        return {
            "success": True,
            "original_resource_id": result["original_resource_id"],
            "replacement_resource_id": result["replacement_resource_id"],
            "replaced": True,
        }

    def remove_shader_replacement(self, resource_id):
        """Remove a replay-time shader replacement."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"success": False, "error": None}
        replacement_state = {"original": None}

        def callback(controller):
            try:
                original = self._resolve_resource_id(controller, resource_id)
            except ValueError as exc:
                result["error"] = str(exc)
                return

            try:
                controller.RemoveReplacement(original)
                controller.ClearReplayCache()
                replacement_state["original"] = original
                result["success"] = True
                result["resource_id"] = Parsers.canonical_resource_id(original)
            except Exception as exc:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to remove replacement: %s" % str(exc)

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])

        try:
            self.ctx.UnregisterReplacement(replacement_state["original"])
            self.ctx.RefreshStatus()
        except Exception as exc:
            raise ValueError(
                "RESOURCE_QUERY_FAILED: failed to sync replacement status: %s"
                % str(exc)
            )

        return {
            "success": True,
            "resource_id": result["resource_id"],
            "replaced": False,
        }

    def preview_event_output(
        self,
        event_id,
        output_path=None,
        output_index=0,
        format_type="PNG",
    ):
        """Save one output texture at an event for preview."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        output_index = self._safe_int(output_index, 0)
        result = {"data": None, "error": None}

        def callback(controller):
            controller.SetFrameEvent(event_id, True)
            pipe = controller.GetPipelineState()
            outputs = self._collect_output_textures(pipe)

            if output_index < 0 or output_index >= len(outputs):
                result["error"] = "INVALID_OUTPUT_INDEX: %d" % output_index
                return

            selected = outputs[output_index]
            tex_desc = self._find_texture_by_id(controller, selected["resource_id"])
            if tex_desc is None:
                result["error"] = "TEXTURE_NOT_FOUND: %s" % selected["resource_id"]
                return

            selected_output_path = output_path
            if selected_output_path is None:
                selected_output_path = self._default_preview_path(
                    int(event_id),
                    output_index,
                    format_type,
                )

            output_dir = os.path.dirname(selected_output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            tex_save = rd.TextureSave()
            tex_save.resourceId = tex_desc.resourceId
            tex_save.mip = 0
            tex_save.slice.sliceIndex = 0
            tex_save.alpha = rd.AlphaMapping.Preserve
            tex_save.destType = self._parse_file_type(format_type)

            try:
                controller.SaveTexture(tex_save, selected_output_path)
            except Exception as exc:
                result["error"] = "RESOURCE_QUERY_FAILED: failed to save preview: %s" % str(exc)
                return

            result["data"] = {
                "success": True,
                "event_id": int(event_id),
                "output_path": selected_output_path,
                "output_index": output_index,
                "format": format_type.upper(),
                "output": selected,
                "resource_id": selected["resource_id"],
                "width": tex_desc.width,
                "height": tex_desc.height,
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]

    def _resolve_shader_context(self, controller, event_id, stage):
        """Resolve the shader bound at an event/stage."""
        controller.SetFrameEvent(event_id, True)

        pipe = controller.GetPipelineState()
        stage_enum = Parsers.parse_stage(stage)
        shader = pipe.GetShader(stage_enum)

        if shader == rd.ResourceId.Null():
            return {
                "error": "RESOURCE_NOT_FOUND: no %s shader bound" % stage,
            }

        return {
            "error": None,
            "pipe": pipe,
            "stage_enum": stage_enum,
            "stage_name": Parsers.parse_stage_name(stage),
            "shader": shader,
            "resource_id": Parsers.canonical_resource_id(shader),
            "entry_point": pipe.GetShaderEntryPoint(stage_enum),
            "reflection": pipe.GetShaderReflection(stage_enum),
        }

    def _cache_resource_id(self, resource_id):
        """Cache a live ResourceId object for later replacement calls."""
        try:
            numeric_id = Parsers.extract_numeric_id(resource_id)
        except Exception:
            return
        self._resource_id_cache[numeric_id] = resource_id

    def _resolve_resource_id(self, controller, resource_id):
        """Resolve a resource ID string to a live RenderDoc ResourceId object."""
        try:
            numeric_id = Parsers.extract_numeric_id(resource_id)
        except Exception:
            raise ValueError("INVALID_RESOURCE_ID: %s" % resource_id)

        cached = self._resource_id_cache.get(numeric_id)
        if cached is not None:
            return cached

        for res in controller.GetResources():
            if Parsers.extract_numeric_id(res.resourceId) == numeric_id:
                self._cache_resource_id(res.resourceId)
                return res.resourceId

        for tex in controller.GetTextures():
            if Parsers.extract_numeric_id(tex.resourceId) == numeric_id:
                self._cache_resource_id(tex.resourceId)
                return tex.resourceId

        for buf in controller.GetBuffers():
            if Parsers.extract_numeric_id(buf.resourceId) == numeric_id:
                self._cache_resource_id(buf.resourceId)
                return buf.resourceId

        try:
            parsed = Parsers.parse_resource_id(resource_id)
            if Parsers.extract_numeric_id(parsed) == numeric_id:
                self._cache_resource_id(parsed)
                return parsed
        except Exception:
            pass

        raise ValueError("INVALID_RESOURCE_ID: %s" % resource_id)

    def _materialize_context(self, data, materialize, max_inline_chars):
        """Write context files and build the MCP response payload."""
        source_text = data.get("source_text")
        disassembly_text = data.get("disassembly_text") or ""
        disassembly_error = data.get("disassembly_error") or ""
        context_dir = None
        original_path = None
        working_path = None
        disassembly_path = None
        context_path = None
        working_preserved = False

        if materialize:
            context_dir = self._context_dir_for_shader(
                data["stage"],
                data["resource_id"],
                data["event_id"],
            )
            if not os.path.exists(context_dir):
                os.makedirs(context_dir)

            if source_text is not None:
                ext = self._extension_for_encoding(data["encoding"], data["stage"])
                original_path = os.path.join(context_dir, "original" + ext)
                working_path = os.path.join(context_dir, "working" + ext)
                self._write_text_file(original_path, source_text)
                if os.path.exists(working_path):
                    working_preserved = True
                else:
                    self._write_text_file(working_path, source_text)

            disassembly_path = os.path.join(context_dir, "disassembly.txt")
            if disassembly_text:
                self._write_text_file(disassembly_path, disassembly_text)
            else:
                self._write_text_file(
                    disassembly_path,
                    "Disassembly unavailable: %s\n" % disassembly_error,
                )

        source_info = {
            "available": source_text is not None,
            "editable": source_text is not None,
            "source_kind": "capture_text" if source_text is not None else "unavailable",
            "encoding": data["encoding"],
            "reason": data.get("source_reason", ""),
            "original_path": original_path,
            "working_path": working_path,
            "working_preserved": working_preserved,
        }
        if source_text is not None:
            source_info.update(
                self._text_summary(source_text, max_inline_chars)
            )

        disassembly_info = {
            "available": bool(disassembly_text),
            "path": disassembly_path,
            "error": disassembly_error,
        }
        disassembly_info.update(
            self._text_summary(disassembly_text, max_inline_chars)
        )

        payload = {
            "event_id": data["event_id"],
            "stage": data["stage"],
            "resource_id": data["resource_id"],
            "entry_point": data["entry_point"],
            "encoding": data["encoding"],
            "editable": source_text is not None,
            "source_kind": source_info["source_kind"],
            "context_dir": context_dir,
            "context_path": None,
            "source": source_info,
            "disassembly": disassembly_info,
            "target_shader_encodings": data.get("target_shader_encodings", []),
            "output_textures": data.get("output_textures", []),
            "warnings": data.get("warnings", []),
        }

        if materialize:
            context_path = os.path.join(context_dir, "context.json")
            payload["context_path"] = context_path
            self._write_json_file(context_path, payload)

        return payload

    def _load_replacement_source(self, source_path, source_text):
        """Load replacement source from a path or inline text."""
        if source_path:
            if not os.path.exists(source_path):
                raise ValueError(
                    "INVALID_SHADER_SOURCE: source_path does not exist: %s"
                    % source_path
                )
            with open(source_path, "rb") as f:
                return f.read()
        if source_text is not None:
            return source_text.encode("utf-8")
        raise ValueError("INVALID_SHADER_SOURCE: source_path or source_text is required")

    def _write_compile_log(self, data):
        """Write compiler output beside the materialized shader context."""
        context_dir = data.get("context_dir")
        if not context_dir:
            return
        if not os.path.exists(context_dir):
            os.makedirs(context_dir)
        compile_log_path = os.path.join(context_dir, "compile.log")
        self._write_text_file(compile_log_path, data.get("compiler_output", ""))
        data["compile_log_path"] = compile_log_path

    def _context_dir_for_shader(self, stage_name, resource_id, event_id):
        """Build the stable shader edit directory for a shader event."""
        capture_key = self._capture_key()
        resource_key = self._sanitize_path_part(resource_id.replace("::", "_"))
        return os.path.join(
            tempfile.gettempdir(),
            "renderdoc_mcp",
            "shaders",
            capture_key,
            "event_%d_%s_%s" % (int(event_id), stage_name, resource_key),
        )

    def _default_preview_path(self, event_id, output_index, format_type):
        """Build the default preview output path."""
        ext = self._file_extension_for_format(format_type)
        return os.path.join(
            tempfile.gettempdir(),
            "renderdoc_mcp",
            "shaders",
            self._capture_key(),
            "previews",
            "preview_%d_output_%d%s" % (int(event_id), int(output_index), ext),
        )

    def _capture_key(self):
        """Build a filesystem-safe capture key."""
        try:
            capture_path = self.ctx.GetCaptureFilename() or "no_capture"
        except Exception:
            capture_path = "no_capture"
        base = os.path.splitext(os.path.basename(capture_path))[0] or "capture"
        digest = hashlib.sha1(capture_path.encode("utf-8")).hexdigest()[:12]
        return "%s_%s" % (self._sanitize_path_part(base), digest)

    @staticmethod
    def _sanitize_path_part(value):
        """Sanitize one path component."""
        text = str(value)
        text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text)
        return text.strip("._") or "unnamed"

    @staticmethod
    def _write_text_file(path, text):
        """Write UTF-8 text."""
        with open(path, "w", encoding="utf-8") as f:
            f.write(text or "")

    @staticmethod
    def _write_json_file(path, payload):
        """Write JSON metadata."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True, ensure_ascii=False)

    @staticmethod
    def _text_summary(text, max_inline_chars):
        """Return metadata and a bounded preview for text."""
        if text is None:
            text = ""
        encoded = text.encode("utf-8")
        max_chars = max(0, int(max_inline_chars))
        return {
            "byte_length": len(encoded),
            "line_count": text.count("\n") + (1 if text else 0),
            "sha256": hashlib.sha256(encoded).hexdigest(),
            "preview": text[:max_chars],
            "preview_truncated": len(text) > max_chars,
        }

    @staticmethod
    def _extension_for_encoding(encoding_name, stage_name):
        """Choose a useful shader source extension."""
        if encoding_name == "HLSL":
            return ".hlsl"
        if encoding_name == "GLSL":
            if stage_name == "vertex":
                return ".vert"
            if stage_name == "compute":
                return ".comp"
            return ".frag"
        if encoding_name in ("SPIRVAsm", "OpenGLSPIRVAsm"):
            return ".spvasm"
        if encoding_name == "Slang":
            return ".slang"
        return ".shader"

    @staticmethod
    def _file_extension_for_format(format_type):
        """Choose an image extension for a RenderDoc file type."""
        upper = (format_type or "PNG").upper()
        if upper == "JPEG":
            upper = "JPG"
        if upper in ("PNG", "JPG", "BMP", "TGA", "EXR", "DDS", "HDR"):
            return "." + upper.lower()
        return ".png"

    @staticmethod
    def _parse_file_type(format_type):
        """Parse a texture save format."""
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
        return format_map.get((format_type or "PNG").upper(), rd.FileType.PNG)

    @classmethod
    def _parse_shader_encoding(cls, encoding):
        """Parse a shader encoding string to a RenderDoc enum value."""
        if encoding is None:
            raise ValueError("INVALID_ENCODING: encoding is required")
        if not isinstance(encoding, str):
            return encoding

        name = encoding.split(".")[-1]
        for known in cls._KNOWN_SHADER_ENCODINGS:
            if known.lower() == name.lower():
                return getattr(rd.ShaderEncoding, known)

        try:
            return rd.ShaderEncoding(int(encoding))
        except Exception:
            raise ValueError("INVALID_ENCODING: unknown shader encoding: %s" % encoding)

    @classmethod
    def _get_shader_encoding_name(cls, encoding):
        """Convert a RenderDoc shader encoding enum to a stable name."""
        if encoding is None:
            return "Unknown"
        name = getattr(encoding, "name", None)
        if name:
            return name
        try:
            numeric = int(encoding)
            if 0 <= numeric < len(cls._KNOWN_SHADER_ENCODINGS):
                return cls._KNOWN_SHADER_ENCODINGS[numeric]
        except (TypeError, ValueError):
            pass
        return str(encoding).split(".")[-1]

    @classmethod
    def _shader_encoding_names(cls, encodings):
        """Serialize shader encoding enum values."""
        return [cls._get_shader_encoding_name(encoding) for encoding in encodings]

    def _collect_output_textures(self, pipe):
        """Collect render/depth outputs from the current pipeline state."""
        output_textures = []

        try:
            for i, rt in enumerate(pipe.GetOutputTargets()):
                if rt.resource == rd.ResourceId.Null():
                    continue
                output_textures.append({
                    "resource_id": Parsers.canonical_resource_id(rt.resource),
                    "name": self._resource_name(rt.resource),
                    "type": "render_target",
                    "index": i,
                })
        except Exception:
            pass

        try:
            depth = pipe.GetDepthTarget()
            if depth.resource != rd.ResourceId.Null():
                output_textures.append({
                    "resource_id": Parsers.canonical_resource_id(depth.resource),
                    "name": self._resource_name(depth.resource),
                    "type": "depth_target",
                })
        except Exception:
            pass

        return output_textures

    def _find_texture_by_id(self, controller, resource_id):
        """Find a texture descriptor by ResourceId."""
        target_id = Parsers.extract_numeric_id(resource_id)
        for tex in controller.GetTextures():
            if Parsers.extract_numeric_id(tex.resourceId) == target_id:
                return tex
        return None

    def _resource_name(self, resource_id):
        """Read a resource name with safe fallback."""
        try:
            return self.ctx.GetResourceName(resource_id) or ""
        except Exception:
            return ""

    @staticmethod
    def _safe_int(value, default):
        """Parse int with a fallback."""
        try:
            return int(value)
        except (TypeError, ValueError):
            return default
