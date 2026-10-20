"""
Pipeline state service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Parsers
from .pipeline_queries import PipelineQueries
from .replay_query import at_event


class PipelineService(PipelineQueries):
    """Pipeline state service"""

    _TEXT_SHADER_ENCODINGS = {
        "GLSL",
        "HLSL",
        "Slang",
        "SPIRVAsm",
        "OpenGLSPIRVAsm",
    }

    def get_shader_info(self, event_id, stage):
        """Get shader information for a specific stage"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"shader": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            pipe = shader_ctx["pipe"]
            stage_enum = shader_ctx["stage_enum"]
            reflection = shader_ctx["reflection"]

            shader_info = {
                "resource_id": shader_ctx["resource_id"],
                "entry_point": shader_ctx["entry_point"],
                "stage": shader_ctx["stage_name"],
            }

            # Get disassembly
            try:
                targets = controller.GetDisassemblyTargets(True)
                if targets:
                    pipeline_obj = (
                        pipe.GetComputePipelineObject()
                        if stage_enum == rd.ShaderStage.Compute
                        else pipe.GetGraphicsPipelineObject()
                    )
                    disasm = controller.DisassembleShader(
                        pipeline_obj, reflection, targets[0]
                    )
                    shader_info["disassembly"] = disasm
            except Exception as e:
                shader_info["disassembly_error"] = str(e)

            result["shader"] = shader_info

        at_event(self.ctx, self._invoke, event_id,
                 lambda controller, event: callback(controller), require_exact_action=False)

        if result["error"]:
            raise ValueError(result["error"])
        return result["shader"]

    def get_shader_source(self, event_id, stage):
        """Get original shader source text when the capture preserves it."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"shader_source": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            reflection = shader_ctx["reflection"]
            shader_source = {
                "resource_id": shader_ctx["resource_id"],
                "entry_point": shader_ctx["entry_point"],
                "stage": shader_ctx["stage_name"],
                "encoding": "Unknown",
                "source_available": False,
            }

            if not reflection:
                shader_source["reason"] = "Shader reflection/source bytes unavailable"
                result["shader_source"] = shader_source
                return

            encoding_name = self._get_shader_encoding_name(reflection.encoding)
            shader_source["encoding"] = encoding_name

            raw_bytes = reflection.rawBytes
            shader_source["byte_length"] = len(raw_bytes) if raw_bytes is not None else 0

            if not raw_bytes:
                shader_source["reason"] = "Shader source payload is empty"
                result["shader_source"] = shader_source
                return

            if encoding_name in self._TEXT_SHADER_ENCODINGS:
                try:
                    shader_source["source_text"] = raw_bytes.decode("utf-8-sig")
                    shader_source["source_available"] = True
                except UnicodeDecodeError as exc:
                    shader_source["reason"] = (
                        "Failed to decode %s shader source as UTF-8: %s"
                        % (encoding_name, exc)
                    )
                result["shader_source"] = shader_source
                return

            shader_source["reason"] = (
                "Original source text is not available for %s shaders"
                % encoding_name
            )
            result["shader_source"] = shader_source

        at_event(self.ctx, self._invoke, event_id,
                 lambda controller, event: callback(controller), require_exact_action=False)

        if result["error"]:
            raise ValueError(result["error"])
        return result["shader_source"]

    def _resolve_shader_context(self, controller, event_id, stage):
        """Resolve the currently bound shader and reflection for one event/stage."""
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

    @staticmethod
    def _get_shader_encoding_name(encoding):
        """Convert RenderDoc shader encoding enums to stable response strings."""
        if encoding is None:
            return "Unknown"
        return getattr(encoding, "name", str(encoding))
