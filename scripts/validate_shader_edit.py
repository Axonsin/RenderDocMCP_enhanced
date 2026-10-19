"""Run in a separate qrenderdoc --ui-python process, never against a working UI.

Set RD_SHADER_CAPTURE to a local capture, RD_SHADER_OUTPUT to a new output folder,
and RD_SHADER_REPO to the repository root (defaults to the working directory).
Optionally set RD_SHADER_EVENT to a pixel-shader draw. No capture is saved.
Writes report.json, source and before/after PNGs. A GPU is required.
"""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import traceback

import renderdoc as rd

output = Path(os.environ["RD_SHADER_OUTPUT"])
output.mkdir(parents=True, exist_ok=True)


def progress(stage):
    (output / "progress.txt").write_text(stage, encoding="utf-8")


progress("importing extension")
sys.path.insert(0, os.environ.get("RD_SHADER_REPO", os.getcwd()))
from renderdoc_extension.services.shader_edit_service import ShaderEditService
from renderdoc_extension.services.resource_service import ResourceService


def validate(ctx, output, report):
    capture = os.environ["RD_SHADER_CAPTURE"]
    if "hkrpg" in os.path.basename(capture).lower():
        raise RuntimeError("hkrpg validation requires a mobile remote replay session. "
                           "Open it with RenderDoc's mobile Replay Context and validate through MCP; "
                           "this standalone local-replay script must not load it.")
    progress("loading capture")
    ctx.LoadCapture(capture, rd.ReplayOptions(), capture, False, True)
    progress("capture loaded")
    if not ctx.IsCaptureLoaded():
        raise RuntimeError("Capture could not be opened for local replay")
    def trace(frame, event, arg):
        if event == "line" and frame.f_code.co_filename.endswith("shader_edit_service.py"):
            with (output / "trace.txt").open("a", encoding="utf-8") as handle:
                handle.write("%s:%s\n" % (frame.f_code.co_name, frame.f_lineno))
        return trace

    def invoke(callback):
        def call(controller):
            if os.environ.get("RD_SHADER_TRACE"):
                sys.settrace(trace)
            try:
                callback(controller)
            finally:
                sys.settrace(None)
        ctx.Replay().BlockInvoke(call)

    service = ShaderEditService(ctx, invoke)
    textures = ResourceService(ctx, ctx.Replay().BlockInvoke)
    try:
        def find(controller):
            draws = []

            def visit(actions):
                for action in actions:
                    if action.flags & rd.ActionFlags.Drawcall:
                        draws.append(action.eventId)
                    visit(action.children)

            visit(controller.GetRootActions())
            requested = os.environ.get("RD_SHADER_EVENT")
            for event in ([int(requested)] if requested else reversed(draws)):
                controller.SetFrameEvent(event, True)
                pipe = controller.GetPipelineState()
                reflection = pipe.GetShaderReflection(rd.ShaderStage.Pixel)
                targets = pipe.GetOutputTargets()
                if reflection and targets and targets[0].resource != rd.ResourceId.Null():
                    return event, targets[0].resource
            raise RuntimeError("No pixel shader draw with a color target found")

        event, texture = service._replay(find)
        report["event_id"] = event
        ctx.SetEventID([], event, event, True)

        def pixels(controller):
            controller.SetFrameEvent(event, True)
            return hashlib.sha256(bytes(controller.GetTextureData(texture, rd.Subresource()))).hexdigest()

        def image(name):
            textures.save_texture(str(texture), str(output / (name + ".png")))

        before = service._replay(pixels)
        image("before")
        progress("preparing edit")
        if os.environ.get("RD_SHADER_TRACE"):
            sys.settrace(trace)
        edit = service.get_shader_edit_context(event, "pixel")
        report["context"] = {k: v for k, v in edit.items() if k not in ("source_text", "applied_source_text")}
        source = edit["source_text"]
        progress("compiling unchanged source")
        service.export_shader_source(edit["edit_id"], str(output / "initial.glsl"))
        result = service.replace_shader(edit["edit_id"], source)
        report["roundtrip"] = result
        if result["last_attempt_status"] != "applied":
            raise RuntimeError("Unchanged shader did not compile; see roundtrip log")
        report["roundtrip_equal"] = service._replay(pixels) == before
        failed = service.replace_shader(edit["edit_id"], "THIS IS AN INVALID SHADER")
        report["failure_preserves_replacement"] = (failed["last_attempt_status"] == "compile_failed"
                                                     and failed["applied"])
        result = service.replace_shader(edit["edit_id"], source)
        report["repeat_applied"] = result["last_attempt_status"] == "applied"

        if edit["encoding"] == "GLSL":
            outputs = re.findall(r"\bout\s+(?:(?:highp|mediump|lowp)\s+)?vec4\s+(\w+)\s*(?:;|$)",
                                 source, re.MULTILINE)
            variable = outputs[0] if outputs else (
                "gl_FragColor" if "gl_FragColor" in source else
                "gl_FragData[0]" if "gl_FragData" in source else None)
            if variable:
                modified, count = re.subn(r"\bvoid\s+main\s*\(", "void mcp_original_main(", source, count=1)
                if count:
                    modified += "\nvoid main() { mcp_original_main(); %s = vec4(1,0,1,1); }\n" % variable
                    report["color_edit"] = service.replace_shader(edit["edit_id"], modified)
                    if report["color_edit"]["last_attempt_status"] == "applied":
                        report["color_pixels_changed"] = service._replay(pixels) != before
                        image("modified")
                        service.export_shader_source(edit["edit_id"], str(output / "modified.glsl"))
        service.revert_shader(edit["edit_id"])
        report["restored_equal"] = service._replay(pixels) == before
        image("restored")
        service.revert_shader(edit["edit_id"])
        if edit["original_encoding"] in ("SPIRV", "OpenGLSPIRV"):
            progress("compiling assembly")
            assembly = service.get_shader_edit_context(event, "pixel", "spirv_asm")
            report["assembly"] = service.replace_shader(assembly["edit_id"], assembly["source_text"])
            report["assembly_equal"] = service._replay(pixels) == before
            service.revert_shader(assembly["edit_id"])
        stale_id = service.get_shader_edit_context(event, "pixel")["edit_id"]
        ctx.CloseCapture()
        ctx.LoadCapture(capture, rd.ReplayOptions(), capture, False, True)
        try:
            service.revert_shader(stale_id)
            report["reopen_rejects_old_id"] = False
        except ValueError as exc:
            report["reopen_rejects_old_id"] = str(exc).startswith("INVALID_EDIT_ID:")
        report["completed"] = True
    finally:
        service.dispose()
        ctx.CloseCapture()


def run():
    report = {"renderdoc_version": rd.GetVersionString(), "completed": False}
    try:
        validate(pyrenderdoc, output, report)
    except Exception:
        report["error"] = traceback.format_exc()
    finally:
        with (output / "report.json").open("w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, ensure_ascii=False)
        pyrenderdoc.GetMainWindow().Widget().close()


pyrenderdoc.InvokeOntoUIThread(run)
