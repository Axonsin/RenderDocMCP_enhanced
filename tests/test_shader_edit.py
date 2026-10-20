"""Stateful shader-edit tests without a RenderDoc installation or GPU."""

import enum
import importlib.util
import json
import os
from pathlib import Path
import sys
import shlex
import subprocess
import tempfile
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


class Encoding(enum.IntEnum):
    Unknown, DXBC, GLSL, SPIRV, SPIRVAsm, HLSL, DXIL, OpenGLSPIRV, OpenGLSPIRVAsm = range(9)


class Stage(enum.IntEnum):
    Vertex, Hull, Domain, Geometry, Pixel, Compute = range(6)


class ResourceId(int):
    def __new__(cls, value=0):
        return int.__new__(cls, value)

    @staticmethod
    def Null():
        return ResourceId()


class Flags:
    def __init__(self):
        self.flags = []


class Reflection:
    def __init__(self):
        self.encoding = Encoding.GLSL
        self.stage = Stage.Pixel
        self.entryPoint = "main"
        self.rawBytes = b"#version 450\nvoid main() {}"
        self.debugInfo = types.SimpleNamespace(compileFlags=Flags())


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def shader_modules():
    """Isolate binding fakes so tests do not import the extension entrypoint."""
    rd = types.ModuleType("renderdoc")
    rd.ShaderEncoding, rd.ShaderStage, rd.ResourceId = Encoding, Stage, ResourceId
    # Real RenderDoc 1.46 does not expose a ShaderReflection constructor.
    rd.ShaderReflection, rd.ShaderCompileFlags = None, Flags
    rd.ShaderCompileFlag = types.SimpleNamespace
    rd.ActionFlags = types.SimpleNamespace(Drawcall=1, Dispatch=2)
    qrd = types.ModuleType("qrenderdoc")
    qrd.CaptureViewer = object
    packages = {"renderdoc": rd, "qrenderdoc": qrd}
    for name in ("renderdoc_extension", "renderdoc_extension.services", "renderdoc_extension.utils"):
        packages[name] = types.ModuleType(name)
        packages[name].__path__ = []
    with patch.dict(sys.modules, packages):
        parsers = load_module("renderdoc_extension.utils.parsers", "renderdoc_extension/utils/parsers.py")
        packages["renderdoc_extension.utils"].Parsers = parsers.Parsers
        packages["renderdoc_extension.utils"].Helpers = types.SimpleNamespace(
            get_all_shader_stages=lambda: list(Stage), flatten_actions=lambda actions: list(actions))
        packages["renderdoc_extension.utils"].Serializers = types.SimpleNamespace()
        shader = load_module("renderdoc_extension.services.shader_edit_service",
                             "renderdoc_extension/services/shader_edit_service.py")
        for dependency in ("resource_catalog", "structured_data", "replay_query", "pipeline_snapshot",
                           "shader_variables", "pipeline_queries"):
            load_module("renderdoc_extension.services." + dependency,
                        "renderdoc_extension/services/" + dependency + ".py")
        pipeline = load_module("renderdoc_extension.services.pipeline_service",
                               "renderdoc_extension/services/pipeline_service.py")
        handler = load_module("renderdoc_extension.request_handler", "renderdoc_extension/request_handler.py")
        search = load_module("renderdoc_extension.services.search_service", "renderdoc_extension/services/search_service.py")
    return shader, pipeline, handler, search


SHADER, PIPELINE, HANDLER, SEARCH = shader_modules()


class Tool:
    def __init__(self, input_encoding, output_encoding, name):
        self.input, self.output, self.name = input_encoding, output_encoding, name
        self.executable = sys.executable  # A real portable executable for discovery checks.
        self.args = ""
        self.calls = []
        self.fail = False
        self.hook = None

    def DefaultArguments(self):
        return "--test-defaults"

    def DisassembleShader(self, window, reflection, args):
        self.calls.append(("decompile", reflection.encoding, bytes(reflection.rawBytes)))
        source = (b"OpEntryPoint Fragment %main \"main\"" if self.output in
                  (Encoding.SPIRVAsm, Encoding.OpenGLSPIRVAsm) else b"#version 450\nvoid main() {}")
        return types.SimpleNamespace(result=b"" if self.fail else source, log="decompiler log")

    def CompileShader(self, window, source, entry, stage, version, args):
        self.calls.append((source, entry, stage, version, args))
        if self.hook:
            self.hook()
        return types.SimpleNamespace(result=b"" if self.fail or "INVALID" in source else b"SPIRV",
                                     log="compiler error" if self.fail or "INVALID" in source else "compiler log")


class Context:
    def __init__(self, encoding=Encoding.GLSL):
        self.loaded = True
        self.viewers = []
        self.ui = {}
        self.replay_replacements = {}
        self.freed = []
        self.built = []
        self.next_id = 100
        self.original = ResourceId(7)
        self.reflection = Reflection()
        self.reflection.encoding = encoding
        self.selected_event, self.event = 42, 41
        self.restores = []
        self.tools = []
        self.accepted = [encoding]
        self.mutable = True
        self.in_replay = False
        self.ui_checks = 0

    def IsCaptureLoaded(self):
        return self.loaded

    def AddCaptureViewer(self, viewer):
        self.viewers.append(viewer)

    def RemoveCaptureViewer(self, viewer):
        self.viewers.remove(viewer)

    def _ui_thread(self):
        if self.in_replay:
            raise AssertionError("UI operation on replay thread")
        self.ui_checks += 1

    def IsResourceReplaced(self, original):
        self._ui_thread()
        return original in self.ui

    def GetResourceReplacement(self, original):
        self._ui_thread()
        return self.ui.get(original, ResourceId.Null())

    def RegisterReplacement(self, original, replacement):
        self._ui_thread()
        self.ui[original] = replacement

    def UnregisterReplacement(self, original):
        self._ui_thread()
        self.ui.pop(original, None)

    def Config(self):
        self._ui_thread()
        return types.SimpleNamespace(ShaderProcessors=self.tools)

    def GetMainWindow(self):
        return types.SimpleNamespace(Widget=lambda: None)

    def CurEvent(self):
        return self.event

    def CurSelectedEvent(self):
        return self.selected_event

    def SetEventID(self, exclude, selected, event, force):
        self._ui_thread()
        self.restores.append((selected, event, force))

    def invoke(self, callback):
        self.in_replay = True
        try:
            callback(self)
        finally:
            self.in_replay = False

    def GetAPIProperties(self):
        return types.SimpleNamespace(shadersMutable=self.mutable, pipelineType="API", remoteReplay=False)

    def SetFrameEvent(self, event, force):
        self.replay_event = event

    def GetPipelineState(self):
        return self

    def GetShader(self, stage):
        return self.original

    def GetShaderReflection(self, stage):
        return self.reflection

    def GetShaderEntryPoint(self, stage):
        return self.reflection.entryPoint

    def GetShaderEntryPoints(self, shader):
        return [types.SimpleNamespace(name=self.reflection.entryPoint, stage=self.reflection.stage)]

    def GetTargetShaderEncodings(self):
        return self.accepted

    def BuildTargetShader(self, entry, encoding, source, flags, stage):
        self.built.append((entry, encoding, source, [(f.name, f.value) for f in flags.flags], stage))
        if b"INVALID" in source:
            return ResourceId.Null(), "syntax error"
        self.next_id += 1
        return ResourceId(self.next_id), "build warning"

    def ReplaceResource(self, original, replacement):
        self.replay_replacements[original] = replacement

    def RemoveReplacement(self, original):
        self.replay_replacements.pop(original, None)

    def FreeTargetResource(self, resource):
        assert resource not in self.replay_replacements.values(), "free of active resource"
        self.freed.append(resource)

    def close_and_reopen(self):
        self.loaded = False
        self.ui.clear()
        self.replay_replacements.clear()
        for viewer in list(self.viewers):
            viewer.OnCaptureClosed()
        self.loaded = True
        for viewer in list(self.viewers):
            viewer.OnCaptureLoaded()


class ShaderEditTests(unittest.TestCase):
    def setUp(self):
        self.ctx = Context()
        self.service = SHADER.ShaderEditService(self.ctx, self.ctx.invoke)
        self.service._decompile = lambda tool, reflection: tool.DisassembleShader(None, reflection, "")

    def prepare(self, mode="auto"):
        return self.service.get_shader_edit_context(12, "pixel", mode)

    def spirv(self, opengl=False):
        native = Encoding.OpenGLSPIRV if opengl else Encoding.SPIRV
        assembly = Encoding.OpenGLSPIRVAsm if opengl else Encoding.SPIRVAsm
        self.ctx.reflection.encoding = native
        self.ctx.reflection.rawBytes = b"\x03\x02\x23\x07\x00\x03\x01\x00"  # SPIR-V 1.3.
        self.ctx.accepted = [native]
        cross = Tool(native, Encoding.GLSL, "cross")
        glslang = Tool(Encoding.GLSL, native, "glslang")
        dis = Tool(native, assembly, "dis")
        assembler = Tool(assembly, native, "as")
        self.ctx.tools = [cross, glslang, dis, assembler]
        return cross, glslang, dis, assembler

    def test_glsl_prepare_and_restore_selected_event(self):
        edit = self.prepare()
        self.assertEqual(edit["mode"], "original")
        self.assertEqual(edit["compiler"], "Builtin")
        self.assertEqual(self.ctx.restores[-1], (42, 41, True))
        self.assertIn("All draws", edit["scope"])

    def test_glsl_can_compile_to_opengl_spirv_when_required(self):
        self.ctx.accepted = [Encoding.OpenGLSPIRV]
        self.ctx.tools = [Tool(Encoding.GLSL, Encoding.OpenGLSPIRV, "glslang GL")]
        edit = self.prepare()
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(self.ctx.built[-1][1], Encoding.OpenGLSPIRV)

    def test_invalid_inputs_do_not_build(self):
        with self.assertRaisesRegex(ValueError, "INVALID_EVENT_ID"):
            self.service.get_shader_edit_context(0, "pixel")
        with self.assertRaisesRegex(ValueError, "INVALID_STAGE"):
            self.service.get_shader_edit_context(12, "fragment")
        edit = self.prepare()["edit_id"]
        for source in ("", " ", "void main() {}\x00"):
            with self.assertRaisesRegex(ValueError, "INVALID_SHADER_SOURCE"):
                self.service.replace_shader(edit, source)
        with self.assertRaisesRegex(ValueError, "INVALID_OUTPUT_PATH"):
            self.service.export_shader_source(edit, "relative.glsl")
        self.assertFalse(self.ctx.built)

    def test_immutable_capture_is_rejected(self):
        self.ctx.mutable = False
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_CAPTURE_FEATURE"):
            self.prepare()

    def test_api_without_legacy_mutability_flag_is_supported(self):
        self.ctx.GetAPIProperties = lambda: types.SimpleNamespace(pipelineType="OpenGL", remoteReplay=False)
        self.assertEqual(self.prepare()["compiler"], "Builtin")

    def test_remote_replay_is_reported_from_replay_controller(self):
        self.ctx.GetAPIProperties = lambda: types.SimpleNamespace(pipelineType="Vulkan", remoteReplay=True)
        self.assertTrue(self.prepare()["remote_replay"])

    def test_multiple_spirv_entrypoints_are_rejected_before_editing(self):
        self.spirv()
        self.ctx.GetShaderEntryPoints = lambda shader: ["first", "second"]
        with self.assertRaisesRegex(ValueError, "multiple entry points"):
            self.prepare()

    def test_revert_ui_failure_keeps_replacement_alive(self):
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "void main() {}")
        previous = self.ctx.ui[self.ctx.original]
        self.ctx.UnregisterReplacement = lambda original: (_ for _ in ()).throw(RuntimeError("UI failure"))
        with self.assertRaisesRegex(RuntimeError, "UI failure"):
            self.service.revert_shader(edit)
        self.assertEqual(self.ctx.replay_replacements[self.ctx.original], previous)
        self.assertNotIn(previous, self.ctx.freed)

    def test_representation_change_requires_revert(self):
        self.spirv()
        edit = self.prepare()
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        with self.assertRaisesRegex(ValueError, "SHADER_EDIT_CONFLICT"):
            self.prepare("spirv_asm")
        self.service.revert_shader(edit["edit_id"])
        assembly = self.prepare("spirv_asm")
        self.assertNotEqual(edit["edit_id"], assembly["edit_id"])

    def test_ui_registration_failure_rolls_back_replay_and_keeps_old_resource(self):
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "void main() { /* previous */ }")
        old = self.ctx.ui[self.ctx.original]
        register = self.ctx.RegisterReplacement

        def fail_new(original, replacement):
            if replacement != old:
                raise RuntimeError("UI registration failed")
            register(original, replacement)

        self.ctx.RegisterReplacement = fail_new
        with self.assertRaisesRegex(RuntimeError, "UI registration failed"):
            self.service.replace_shader(edit, "void main() { /* new */ }")
        self.assertEqual(self.ctx.ui[self.ctx.original], old)
        self.assertEqual(self.ctx.replay_replacements[self.ctx.original], old)
        self.assertNotIn(old, self.ctx.freed)
        self.assertTrue(self.service.list_shader_replacements()["items"])

    def test_replace_failure_then_replace_and_idempotent_revert(self):
        edit = self.prepare()["edit_id"]
        first = self.service.replace_shader(edit, "void main() { /* A */ }")
        old = self.ctx.ui[self.ctx.original]
        failed = self.service.replace_shader(edit, "INVALID")
        self.assertTrue(failed["applied"])
        self.assertEqual(failed["last_attempt_status"], "compile_failed")
        self.assertEqual(self.ctx.ui[self.ctx.original], old)
        context = self.prepare()
        self.assertEqual(context["source_text"], "INVALID")
        self.assertIn("/* A */", context["applied_source_text"])
        second = self.service.replace_shader(edit, "void main() { /* B */ }")
        self.assertEqual(second["revision"], first["revision"] + 1)
        self.assertEqual(self.ctx.freed, [old])
        self.service.revert_shader(edit)
        self.service.revert_shader(edit)
        self.assertEqual(len(self.ctx.freed), 2)
        self.assertFalse(self.ctx.ui)
        self.assertFalse(self.ctx.replay_replacements)

    def test_initial_failure_is_queryable_in_sessions(self):
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "INVALID")
        state = self.service.list_shader_replacements()
        self.assertEqual(state["items"], [])
        self.assertEqual(state["sessions"][0]["last_attempt_status"], "compile_failed")

    def test_spirv_glsl_path_and_version(self):
        cross, compiler, _, _ = self.spirv()
        edit = self.prepare()
        self.assertEqual(edit["mode"], "glsl")
        self.assertEqual(edit["spirv_version"], "spirv1.3")
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(self.ctx.built[-1][1], Encoding.SPIRV)
        self.assertEqual(compiler.calls[-1][3], "spirv1.3")
        self.assertTrue(cross.calls)

    def test_auto_fallback_requires_a_complete_roundtrip(self):
        _, compiler, _, assembler = self.spirv()
        self.ctx.tools.remove(compiler)
        edit = self.prepare()
        self.assertEqual(edit["mode"], "spirv_asm")
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertIn("--target-env spv1.3", assembler.calls[-1][-1])

    def test_explicit_glsl_does_not_fallback(self):
        _, compiler, _, _ = self.spirv()
        self.ctx.tools.remove(compiler)
        with self.assertRaisesRegex(ValueError, "SHADER_TOOL_MISSING"):
            self.prepare("glsl")

    def test_opengl_spirv_cannot_use_vulkan_compiler(self):
        _, compiler, _, _ = self.spirv(True)
        compiler.output = Encoding.SPIRV
        self.ctx.accepted.append(Encoding.SPIRV)
        with self.assertRaisesRegex(ValueError, "SHADER_TOOL_MISSING"):
            self.prepare("glsl")
        edit = self.prepare("spirv_asm")
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(self.ctx.built[-1][1], Encoding.OpenGLSPIRV)

    def test_missing_executable_is_not_a_compilation_path(self):
        self.spirv()
        for tool in self.ctx.tools:
            tool.executable = "missing-shader-tool-12345.exe"
        with self.assertRaisesRegex(ValueError, "SHADER_TOOL_MISSING"):
            self.prepare()

    def test_original_binary_and_pseudocode_are_not_source_modes(self):
        self.spirv()
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_SHADER_ENCODING"):
            self.prepare("original")
        with self.assertRaisesRegex(ValueError, "INVALID_EDIT_MODE"):
            self.prepare("pseudocode")

    def test_custom_entry_is_preserved_when_glsl_is_main(self):
        _, compiler, _, _ = self.spirv()
        self.ctx.reflection.entryPoint = "MyFragment"
        edit = self.prepare()
        self.assertEqual(edit["source_entry_point"], "main")
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(compiler.calls[-1][1], "MyFragment")
        self.assertIn("--source-entrypoint main -e {entry_point}", compiler.calls[-1][-1])

    def test_original_compile_metadata_is_filtered_for_decompiled_source(self):
        self.spirv()
        self.ctx.reflection.debugInfo.compileFlags.flags = [
            types.SimpleNamespace(name="@spirver", value="spirv1.2"),
            types.SimpleNamespace(name="@cmdline", value="old incompatible arguments")]
        edit = self.prepare()
        self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(self.ctx.built[-1][3], [("@spirver", "spirv1.2")])

    def test_compiler_failure_does_not_build_or_release(self):
        _, compiler, _, _ = self.spirv()
        edit = self.prepare()
        compiler.fail = True
        result = self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertEqual(result["last_attempt_status"], "compile_failed")
        self.assertEqual(self.ctx.built, [])
        self.assertEqual(self.ctx.freed, [])

    def test_same_path_reopen_invalidates_old_ids(self):
        old = self.prepare()["edit_id"]
        self.ctx.close_and_reopen()
        with self.assertRaisesRegex(ValueError, "INVALID_EDIT_ID"):
            self.service.replace_shader(old, "void main() {}")
        self.assertNotEqual(self.prepare()["edit_id"], old)

    def test_capture_close_during_compilation_never_applies(self):
        _, compiler, _, _ = self.spirv()
        edit = self.prepare()
        compiler.hook = self.ctx.close_and_reopen
        with self.assertRaisesRegex(ValueError, "INVALID_EDIT_ID"):
            self.service.replace_shader(edit["edit_id"], edit["source_text"])
        self.assertFalse(self.ctx.built)

    def test_external_replacement_before_or_after_prepare(self):
        self.ctx.ui[self.ctx.original] = ResourceId(999)
        with self.assertRaisesRegex(ValueError, "SHADER_EDIT_CONFLICT"):
            self.prepare()
        self.ctx.ui.clear()
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "void main() {}")
        self.ctx.ui[self.ctx.original] = ResourceId(999)
        self.ctx.replay_replacements[self.ctx.original] = ResourceId(999)
        for action in (lambda: self.service.replace_shader(edit, "void main() {}"),
                       lambda: self.service.revert_shader(edit)):
            with self.assertRaisesRegex(ValueError, "SHADER_EDIT_CONFLICT"):
                action()
        self.assertTrue(self.service.list_shader_replacements()["sessions"][0]["conflict"])
        self.service.dispose()
        self.assertEqual(self.ctx.ui[self.ctx.original], 999)
        self.assertEqual(len(self.ctx.freed), 1)

    def test_export_utf8_and_refuse_overwrite(self):
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "INVALID // 测试")
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "shader.glsl")
            result = self.service.export_shader_source(edit, path)
            self.assertFalse(result["matches_applied_source"])
            self.assertEqual(Path(path).read_text(encoding="utf-8"), "INVALID // 测试")
            with self.assertRaisesRegex(ValueError, "OUTPUT_FILE_EXISTS"):
                self.service.export_shader_source(edit, path)

    def test_dispose_reverts_and_unregisters(self):
        edit = self.prepare()["edit_id"]
        self.service.replace_shader(edit, "void main() {}")
        self.service.dispose()
        self.assertFalse(self.ctx.viewers)
        self.assertFalse(self.ctx.ui)
        self.assertEqual(len(self.ctx.freed), 1)

    def test_unsupported_directx_is_explicit(self):
        for encoding in (Encoding.HLSL, Encoding.DXBC, Encoding.DXIL):
            self.ctx.reflection.encoding = encoding
            with self.assertRaisesRegex(ValueError, "HLSL/DXBC/DXIL editing is TODO"):
                self.prepare()

    def test_existing_source_reader_still_returns_original(self):
        pipeline = PIPELINE.PipelineService(self.ctx, self.ctx.invoke)
        source = pipeline.get_shader_source(12, "pixel")
        self.assertTrue(source["source_available"])
        self.assertEqual(source["source_text"], self.ctx.reflection.rawBytes.decode("utf-8"))
        self.spirv()
        self.assertFalse(pipeline.get_shader_source(12, "pixel")["source_available"])

    def test_search_matches_event_specific_pipeline_snapshots(self):
        self.ctx.replay_event = 1
        self.ctx.GetRootActions = lambda: [types.SimpleNamespace(
            eventId=eid, flags=1, GetName=lambda file: "draw") for eid in (1, 2)]
        self.ctx.GetStructuredFile = lambda: None

        def set_event(event, fetch_snapshot):
            if fetch_snapshot:
                self.ctx.replay_event = event

        self.ctx.SetFrameEvent = set_event
        self.ctx.GetShader = lambda stage: (ResourceId(7 if self.ctx.replay_event == 1 else 8)
                                           if stage == Stage.Pixel else ResourceId.Null())
        search = SEARCH.SearchService(self.ctx, self.ctx.invoke)
        result = search.search_draws("resource", "ResourceId::7")
        self.assertEqual([item["event_id"] for item in result["matches"]], [1])

    def test_new_routes_and_error_classification(self):
        handler = HANDLER.RequestHandler(self.service)
        response = handler.handle({"id": "test", "method": "get_shader_edit_context",
                                   "params": {"event_id": 12, "stage": "pixel"}})
        edit = response["result"]["edit_id"]
        response = handler.handle({"id": "replace", "method": "replace_shader",
                                   "params": {"edit_id": edit, "source_text": "void main() {}"}})
        self.assertTrue(response["result"]["applied"])
        invalid = handler.handle({"id": "bad", "method": "revert_shader",
                                  "params": {"edit_id": "expired"}})
        self.assertEqual(invalid["error"]["code"], -32602)

    def test_compiler_arguments_with_installed_spirv_tools(self):
        config_path = Path(os.environ.get("APPDATA", "")) / "qrenderdoc" / "UI.config"
        if not config_path.is_file():
            self.skipTest("RenderDoc shader-tool configuration is not installed")
        tools = json.loads(config_path.read_text(encoding="utf-8-sig")).get("ShaderProcessors", [])
        assembler = next((t for t in tools if t.get("input") == int(Encoding.SPIRVAsm)
                          and t.get("output") == int(Encoding.SPIRV)
                          and Path(t.get("executable", "")).is_file()), None)
        if assembler is None:
            self.skipTest("Configured SPIR-V assembler is unavailable")
        source = ('OpCapability Shader\nOpMemoryModel Logical GLSL450\n'
                  'OpEntryPoint Fragment %main "main"\nOpExecutionMode %main OriginUpperLeft\n'
                  '%void = OpTypeVoid\n%fn = OpTypeFunction %void\n'
                  '%main = OpFunction %void None %fn\n%entry = OpLabel\nOpReturn\nOpFunctionEnd\n')
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "shader.spvasm"
            output_path = Path(directory) / "shader.spv"
            input_path.write_text(source, encoding="utf-8")
            for version in ("spirv1.0", "spirv1.3"):
                with self.subTest(version=version):
                    record = {"compiler": types.SimpleNamespace(DefaultArguments=lambda: ""),
                              "source_encoding": Encoding.SPIRVAsm, "spirv_version": version}
                    args = SHADER.ShaderEditService._compiler_arguments(record)
                    result = subprocess.run([assembler["executable"]] + shlex.split(args) +
                                            ["-o", str(output_path), str(input_path)],
                                            capture_output=True, timeout=10)
                    self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", "replace"))
                    self.assertEqual(SHADER.ShaderEditService._spirv_version(output_path.read_bytes()), version)


if __name__ == "__main__":
    unittest.main()
