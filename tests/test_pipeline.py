"""Pipeline/Texture Viewer contracts without a RenderDoc installation or GPU."""

import enum
import importlib.util
import json
import asyncio
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
NS = types.SimpleNamespace


class ResourceId(int):
    @staticmethod
    def Null():
        return ResourceId(0)


Stage = enum.IntEnum("ShaderStage", "Vertex Hull Domain Geometry Pixel Compute Task Mesh")
ActionFlags = enum.IntFlag("ActionFlags", {
    "Drawcall": 1, "Dispatch": 2, "Copy": 4, "Resolve": 8, "Clear": 16,
    "Indexed": 32, "MeshDispatch": 64})
VarType = enum.IntEnum("VarType", "Float UInt Struct")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def modules():
    rd = types.ModuleType("renderdoc")
    rd.ResourceId, rd.ShaderStage, rd.ActionFlags = ResourceId, Stage, ActionFlags
    qrd = types.ModuleType("qrenderdoc")
    qrd.CaptureViewer = object
    packages = {"renderdoc": rd, "qrenderdoc": qrd}
    for name in ("renderdoc_extension", "renderdoc_extension.services", "renderdoc_extension.utils"):
        packages[name] = types.ModuleType(name)
        packages[name].__path__ = []
    with patch.dict(sys.modules, packages):
        utils = packages["renderdoc_extension.utils"]
        utils.Parsers = load("renderdoc_extension.utils.parsers",
                             "renderdoc_extension/utils/parsers.py").Parsers
        utils.Helpers, utils.Serializers = NS(), NS()
        loaded = {}
        for name in ("resource_catalog", "structured_data", "replay_query", "pipeline_snapshot",
                     "shader_variables", "pipeline_queries", "pipeline_service",
                     "resource_service", "analysis_service"):
            loaded[name] = load("renderdoc_extension.services." + name,
                                "renderdoc_extension/services/" + name + ".py")
        handler = load("renderdoc_extension.request_handler", "renderdoc_extension/request_handler.py")
    return loaded, handler, rd


MODULES, HANDLER, RD = modules()
SERVICE = MODULES["pipeline_service"].PipelineService
FMT = NS(Name=lambda: "R8G8B8A8_UNORM")


def descriptor(rid=0, offset=0, size=512):
    return NS(resource=ResourceId(rid), view=ResourceId(0), secondary=ResourceId(0),
              byteOffset=offset, byteSize=size, firstMip=1, numMips=2, firstSlice=3,
              numSlices=1, elementByteSize=16, type="Image", flags=0, format=FMT)


def used(index=0, rid=10, array=0, unused=False, offset=1024, size=512):
    return NS(access=NS(index=index, arrayElement=array, staticallyUnused=unused,
                        descriptorStore=ResourceId(50), byteOffset=32 * (index + array)),
              descriptor=descriptor(rid, offset, size),
              sampler=NS(object=ResourceId(20), creationTimeConstant=False, maxLOD=1000))


def declaration(name, binding, space=0, size=0, texture=False, backed=True, variables=()):
    return NS(name=name, fixedBindNumber=binding, fixedBindSetOrSpace=space,
              byteSize=size, isTexture=texture, bufferBacked=backed, variables=list(variables))


def variable(name, value=1.5, members=()):
    return NS(name=name, type=VarType.Struct if members else VarType.Float,
              rows=1, columns=1, value=NS(f32v=[value]), members=list(members))


def layout(name, members=(), elements=1):
    return NS(name=name, byteOffset=16, type=NS(name="Struct" if members else "float",
              elements=elements, arrayByteStride=16, matrixByteStride=0, members=list(members)))


class Pipe:
    def __init__(self):
        self.reflection = NS(
            readOnlyResources=[declaration("albedo", 7, texture=True)],
            readWriteResources=[declaration("storage", 3, texture=True)],
            samplers=[declaration("linear", 8)],
            constantBlocks=[
                declaration("uniforms1985", 2, 1, 720, variables=[layout("material", [layout("roughness")])]),
                declaration("push", 0, size=16, backed=False, variables=[layout("scalar")]),
            ])
        self.readonly = [used(rid=11), used(rid=11, array=1)]
        self.readwrite = [used(rid=11)]
        self.samplers = [used(rid=0)]
        self.constants = [used(rid=10), used(index=1, rid=0, offset=0, size=16)]

    def Abbrev(self, stage):
        return {Stage.Pixel: "FS", Stage.Vertex: "VS", Stage.Compute: "CS"}.get(stage, stage.name)

    def OutputAbbrev(self):
        return "FB"

    def GetShader(self, stage):
        return ResourceId(30 if stage in (Stage.Pixel, Stage.Vertex, Stage.Compute) else 0)

    def GetShaderReflection(self, stage):
        return self.reflection

    def GetShaderEntryPoint(self, stage):
        return "main"

    def GetComputePipelineObject(self):
        return ResourceId(40)

    GetGraphicsPipelineObject = GetComputePipelineObject

    def GetReadOnlyResources(self, stage, onlyUsed):
        return self.readonly

    def GetReadWriteResources(self, stage, onlyUsed):
        return self.readwrite

    def GetSamplers(self, stage, onlyUsed):
        return self.samplers

    def GetConstantBlocks(self, stage, onlyUsed):
        return self.constants

    def GetConstantBlock(self, stage, index, array):
        return self.constants[index]

    def GetPrimitiveTopology(self):
        return "TriangleList"

    def IsRestartEnabled(self):
        return False

    def GetRestartIndex(self):
        return 0xffffffff

    def GetVertexInputs(self):
        return [NS(used=True, vertexBuffer=0, genericEnabled=False, name="POSITION")]

    def GetVBuffers(self):
        return [NS(resourceId=ResourceId(10), byteOffset=0, byteSize=2048, byteStride=16)]

    def GetIBuffer(self):
        return NS(resourceId=ResourceId(10), byteOffset=0, byteSize=100, byteStride=2)

    def GetRasterState(self):
        return NS(cullMode="Back", frontCCW=True, fillMode="Solid")

    def GetOutputTargets(self):
        return [descriptor(11)]

    def GetDepthTarget(self):
        return descriptor(11)

    def GetDepthResolveTarget(self):
        return descriptor()

    def GetColorBlends(self):
        return [NS(enabled=True, writeMask=7)]

    def GetBlendFactor(self):
        return [1, 1, 1, 1]

    def IsIndependentBlendingEnabled(self):
        return True

    def GetDepthTestState(self):
        return NS(depthWrites=False, depthEnable=True)

    def IsStencilTestEnabled(self):
        return False

    def GetStencilFaces(self):
        return [NS(writeMask=0), NS(writeMask=0)]


class Controller:
    def __init__(self):
        self.pipe = Pipe()
        self.event = 99
        self.events, self.decode_calls = [], []
        self.enumerations = 0
        self.api = "Vulkan"
        pipeline = NS(pipelineResourceId=ResourceId(40),
                      pipelineComputeLayoutResourceId=ResourceId(41),
                      pipelinePreRastLayoutResourceId=ResourceId(42),
                      pipelineFragmentLayoutResourceId=ResourceId(43),
                      descriptorBuffers=[],
                      descriptorSets=[NS(descriptorSetResourceId=ResourceId(50),
                          layoutResourceId=ResourceId(51), pushDescriptor=False,
                          dynamicOffsets=[NS(descriptorByteOffset=0, dynamicBufferByteOffset=256)])])
        self.native = NS(graphics=pipeline, compute=pipeline,
                         viewportScissor=NS(viewportScissors=[
                             NS(vp=NS(x=0, width=100, enabled=False), scissor=NS(x=0, width=50)),
                             NS(vp=NS(x=100, width=200, enabled=True), scissor=NS(x=100, width=60))]),
                         rasterizer=NS(depthBias=2.0, frontCCW=True),
                         multisample=NS(rasterSamples=4, sampleMask=[255]),
                         depthStencil=NS(depthWriteEnable=False),
                         currentPass=NS(renderpass=NS(depthstencilAttachment=0),
                                        framebuffer=NS(attachments=[NS(depthReadOnly=True)])))

    def SetFrameEvent(self, event, force):
        self.event = event
        self.events.append(event)

    def GetPipelineState(self):
        return self.pipe

    def GetAPIProperties(self):
        return NS(pipelineType=self.api)

    def GetVulkanPipelineState(self):
        return self.native

    def GetD3D11PipelineState(self):
        return NS(rasterizer=NS(viewports=[NS(width=100)], scissors=[NS(width=50)]),
                  outputMerger=NS(depthTarget=NS(depthReadOnly=True)))

    GetD3D12PipelineState = GetD3D11PipelineState
    GetGLPipelineState = GetD3D11PipelineState

    def GetResources(self):
        self.enumerations += 1
        return [NS(resourceId=ResourceId(i), type="Texture" if i == 11 else "Buffer",
                   name="resource %s" % i) for i in (10, 11, 20, 30, 40, 41, 42, 43, 50, 51)]

    def GetTextures(self):
        return [NS(resourceId=ResourceId(11), width=128, height=128, depth=1,
                   arraysize=6, mips=4, msSamp=1, format=FMT, cubemap=False, type="Texture2D")]

    def GetBuffers(self):
        return [NS(resourceId=ResourceId(10), length=8192)]

    def GetCBufferVariableContents(self, *args):
        self.decode_calls.append(args)
        return [variable("material", members=[variable("roughness")])]


class Context:
    def __init__(self, controller):
        self.controller, self.viewers = controller, []
        self.action = NS(eventId=343, flags=ActionFlags.Drawcall | ActionFlags.Indexed,
                         dispatchDimension=[2, 3, 4], dispatchThreadsDimension=[8, 8, 1],
                         copySource=ResourceId(11), copyDestination=ResourceId(11),
                         copySourceSubresource=NS(mip=1, slice=2, sample=0),
                         copyDestinationSubresource=NS(mip=2, slice=3, sample=0))
        self.loaded = True

    def IsCaptureLoaded(self):
        return self.loaded

    def GetAction(self, eid):
        return self.action if eid == 343 else None

    def CurEvent(self):
        return 99

    def GetResourceName(self, rid):
        return "2D Image 487" if rid == 11 else "Buffer %s" % rid

    def AddCaptureViewer(self, viewer):
        self.viewers.append(viewer)

    def RemoveCaptureViewer(self, viewer):
        self.viewers.remove(viewer)

    def invoke(self, callback):
        callback(self.controller)


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.ctx = Context(self.controller)
        self.service = SERVICE(self.ctx, self.ctx.invoke)

    def stage(self, section, **kwargs):
        return self.service.get_pipeline_stage(343, "FS", section, **kwargs)

    def test_overview_and_fixed_function(self):
        result = self.service.get_pipeline_state(343)
        self.assertEqual(result["action_event_id"], 343)
        self.assertEqual(result["action"]["action_event_id"], 343)
        self.assertNotIn("event_id", result["action"])
        self.assertNotIn("input_textures", result)
        self.assertNotIn("shaders", result)
        stages = {s["stage"]: s for s in result["stages"]}
        self.assertEqual(stages["fragment"]["status"], "enabled")
        self.assertEqual(stages["geometry"]["status"], "disabled")
        self.assertEqual(stages["compute"]["status"], "not_applicable")
        viewports = self.service.get_pipeline_stage(343, "rasterizer", "viewports")
        self.assertEqual(viewports["total_count"], 2)  # disabled first viewport does not truncate
        multi = self.service.get_pipeline_stage(343, "rasterizer", "multisample")
        self.assertEqual(multi["data"]["rasterSamples"], 4)
        self.assertEqual(self.controller.event, 99)
        json.dumps(result, allow_nan=False)

    def test_shader_stage_aliases_match_pipeline_and_shader_parsers(self):
        parsers = MODULES["pipeline_snapshot"].Parsers
        for canonical, aliases in {
            "fragment": ("fragment", "pixel", "PS", "FS"),
            "tess_control": ("tess_control", "hull", "HS", "TCS"),
            "tess_eval": ("tess_eval", "domain", "DS", "TES"),
            "task": ("task", "AS", "TS"), "mesh": ("mesh", "MS"),
        }.items():
            for alias in aliases:
                with self.subTest(stage=alias):
                    self.assertEqual(parsers.parse_stage_name(alias), canonical)
                    self.assertEqual(self.service.get_pipeline_stage(343, alias)["stage"], canonical)

    def test_identity_indices_ranges_and_no_eager_decode(self):
        rows = self.stage("constant_buffers")["items"]
        row = rows[0]
        self.assertEqual(row["location"]["reflection_index"], 0)
        self.assertEqual(row["location"]["binding"], 2)
        self.assertEqual(row["location"]["set_or_space"], 1)
        self.assertEqual(row["required_bytes"], 720)
        self.assertEqual(row["provided_bytes"], 512)
        self.assertEqual(row["buffer_range"]["byte_offset"], 1024)
        self.assertEqual(row["issues"][0]["code"], "constant_buffer_range_too_small")
        self.assertFalse(self.controller.decode_calls)
        native = self.stage("descriptors")["items"]
        self.assertEqual(native[0]["dynamic_offsets"][0]["dynamicBufferByteOffset"], 256)

    def test_variables_exact_offset_and_paths(self):
        row = self.stage("constant_buffers")["items"][0]
        result = self.service.inspect_pipeline_binding(343, row["binding_id"], "variables")
        self.assertEqual(self.controller.decode_calls[-1][-2:], (1024, 512))
        self.assertEqual(result["children"]["items"][0]["child_path"], [0])
        result = self.service.inspect_pipeline_binding(343, row["binding_id"], "variables", [0])
        self.assertEqual(result["children"]["items"][0]["value"], [1.5])
        with self.assertRaisesRegex(ValueError, "INVALID_CHILD_PATH"):
            self.service.inspect_pipeline_binding(343, row["binding_id"], "variables", [9])
        self.assertEqual(self.controller.event, 99)

    def test_direct_constants_not_missing(self):
        row = self.stage("push_constants")["items"][0]
        self.assertTrue(row["bound"])
        self.assertFalse(row["issues"])
        result = self.service.inspect_pipeline_binding(343, row["binding_id"], "variables")
        self.assertTrue(result["available"])
        self.assertEqual(self.controller.decode_calls[-1][-3:], (ResourceId(0), 0, 16))

    def test_combined_and_implicit_sampler_states(self):
        row = self.stage("resources")["items"][0]
        self.assertEqual(row["combined_sampler"]["resource"]["resource_id"], "ResourceId::20")
        self.controller.pipe.samplers[0].sampler.object = ResourceId(0)
        self.controller.pipe.samplers[0].sampler.type = "Sampler"
        sampler = self.stage("samplers")["items"][0]
        self.assertTrue(sampler["bound"])
        self.assertIsNone(sampler["resource"])
        self.assertFalse(sampler["issues"])

    def test_texture_bindings_preserved_and_rw_filter(self):
        result = self.service.get_action_textures(343)
        inputs = [r for r in result["items"] if r["stage"] == "fragment"]
        self.assertEqual(len(inputs), 3)
        self.assertEqual(len(set(r["binding_id"] for r in inputs)), 3)
        self.assertTrue(all(r["resource"]["name"] == "2D Image 487" for r in inputs))
        outputs = self.service.get_action_textures(343, "output", "FS")["items"]
        self.assertEqual(len(outputs), 1)
        self.assertEqual(outputs[0]["roles"], ["input", "output"])
        self.assertEqual(outputs[0]["subresources"]["first_slice"], 3)

    def test_filters_preserve_missing_required(self):
        self.controller.pipe.readonly = [used(rid=0), used(rid=11, array=1, unused=True)]
        result = self.stage("resources")
        self.assertEqual(len(result["items"]), 2)  # missing input and RW
        self.assertEqual(result["items"][0]["issues"][0]["code"], "required_binding_missing")
        all_rows = self.stage("resources", show_unused=True)
        self.assertEqual(all_rows["total_count"], 3)
        page = self.stage("resources", show_unused=True, offset=1, limit=1)
        self.assertTrue(page["has_more"])

    def test_tokens_capture_action_and_binding_scoped(self):
        row = self.stage("constant_buffers")["items"][0]
        self.service.inspect_pipeline_binding(343, row["binding_id"])
        self.controller.pipe.constants[0].descriptor.byteOffset += 16
        with self.assertRaisesRegex(ValueError, "INVALID_BINDING_ID"):
            self.service.inspect_pipeline_binding(343, row["binding_id"])
        row = self.stage("constant_buffers")["items"][0]
        self.service.OnCaptureClosed()
        self.service.OnCaptureLoaded()
        with self.assertRaisesRegex(ValueError, "INVALID_BINDING_ID"):
            self.service.inspect_pipeline_binding(343, row["binding_id"])

    def test_reflection_missing_and_direct_access_retained(self):
        self.controller.pipe.reflection = None
        self.controller.pipe.readonly[0].access.index = 65535
        rows = self.stage("resources")["items"]
        self.assertEqual(rows[0]["binding_name"], "")
        self.assertIn("descriptor_store", rows[0]["location"])
        self.assertEqual(rows[0]["resource"]["name"], "2D Image 487")

    def test_compute_and_transfer_dont_inherit_graphics(self):
        self.ctx.action.flags = ActionFlags.Dispatch
        rows = self.service.get_action_textures(343)["items"]
        self.assertTrue(all(r["stage"] == "compute" for r in rows))
        for kind in (ActionFlags.Copy, ActionFlags.Resolve, ActionFlags.Clear):
            self.ctx.action.flags = kind
            result = self.service.get_action_textures(343)
            self.assertTrue(all(r["stage"] == "transfer" for r in result["items"]))
            self.assertEqual(len(result["items"]), 1 if kind == ActionFlags.Clear else 2)
            if kind != ActionFlags.Clear:
                self.assertEqual(result["items"][0]["subresources"]["mip"], 1)
        self.ctx.action.copyDestination = ResourceId(0)
        self.assertFalse(self.service.get_action_textures(343)["available"])

    def test_common_apis_report_native_limits(self):
        for api in ("D3D11", "D3D12", "OpenGL"):
            self.controller.api = api
            self.assertEqual(self.service.get_action_textures(343)["total_count"], 8)
            self.assertFalse(self.stage("descriptors")["data"]["native"]["available"])
            view = self.service.get_pipeline_stage(343, "rasterizer", "viewports")
            self.assertEqual(view["total_count"], 1)

    def test_failed_query_restores_and_section_failure_explicit(self):
        def fail():
            raise RuntimeError("driver unavailable")
        self.controller.GetResources = fail
        with self.assertRaisesRegex(RuntimeError, "driver unavailable"):
            self.service.get_pipeline_state(343)
        self.assertEqual(self.controller.events, [343, 99])
        self.controller.GetResources = lambda: []
        self.controller.pipe.GetReadOnlyResources = lambda *a: fail()
        result = self.stage("resources")
        self.assertFalse(result["available"])
        self.assertTrue(result["items"])  # partial RW data preserved
        self.assertFalse(self.service.get_action_textures(343)["available"])

    def test_validation_and_single_catalog(self):
        self.service.get_pipeline_state(343)
        self.assertEqual(self.controller.enumerations, 1)
        for event in (True, "343", 0, 342):
            with self.assertRaises(ValueError):
                self.service.get_pipeline_state(event)
        with self.assertRaisesRegex(ValueError, "INVALID_PAGINATION"):
            self.stage("resources", limit=0)
        with self.assertRaisesRegex(ValueError, "INVALID_STAGE"):
            self.service.get_pipeline_stage(343, "unknown")
        with self.assertRaisesRegex(ValueError, "INVALID_DIRECTION"):
            self.service.get_action_textures(343, "both")

    def test_range_overflow_and_no_false_size_issue(self):
        descriptor = self.controller.pipe.constants[0].descriptor
        descriptor.byteSize = 720
        self.assertFalse(self.stage("constant_buffers")["items"][0]["issues"])
        descriptor.byteOffset = 8190
        issues = self.stage("constant_buffers")["items"][0]["issues"]
        self.assertEqual(issues[0]["code"], "buffer_range_out_of_bounds")

    def test_set_positions_and_reflection_reordering(self):
        pipe = self.controller.pipe
        original = self.stage("resources")["items"][0]
        pipe.reflection.readOnlyResources.insert(0, declaration("other_set", 7, space=1, texture=True))
        pipe.readonly = [used(index=1, rid=11), used(index=0, rid=11)]
        rows = self.stage("resources")["items"]
        self.assertEqual(original["binding_key"], rows[0]["binding_key"])
        self.assertNotEqual(rows[0]["binding_key"], rows[1]["binding_key"])
        self.assertEqual(rows[1]["location"]["set_or_space"], 1)

    def test_inspect_action_keeps_shader_without_resources_and_restores_mesh(self):
        pipe = self.controller.pipe
        pipe.readonly, pipe.readwrite, pipe.samplers, pipe.constants = [], [], [], []
        actions = NS(get_action_details=lambda action_event_id: {"name": "draw", "flags": ["Drawcall"]},
                     get_action_timings=lambda **args: {"available": False})
        def mesh_query(event):
            self.controller.SetFrameEvent(event, True)
            return {"num_vertices": 3}
        analysis = MODULES["analysis_service"].AnalysisService(
            self.ctx, self.ctx.invoke, actions, self.service, None,
            NS(get_mesh_summary=mesh_query))
        result = analysis.inspect_action(343)
        self.assertEqual(result["action_event_id"], 343)
        self.assertNotIn("event_id", result)
        self.assertTrue(any(s["stage"] == "fragment" for s in result["shaders"]))
        self.assertEqual(self.controller.event, 99)

    def test_analysis_unpaged_and_action_tokens_excluded_from_diff(self):
        self.controller.pipe.readonly = [used(rid=11, array=i) for i in range(70)]
        snap = self.service.analysis_snapshot(343)
        self.assertGreater(len(snap["textures"]), 140)
        analysis = MODULES["analysis_service"].AnalysisService(
            self.ctx, self.ctx.invoke, None, self.service, None, None)
        event = {"action_event_id": 1, "shaders": [], "bindings": snap["bindings"], "textures": snap["textures"],
                 "fixed_function": snap["fixed_function"], "details": {}}
        other = json.loads(json.dumps(event))
        other["action_event_id"] = 2
        for row in other["bindings"]:
            row["binding_id"] = "other_action_token"
        analysis.inspect_action = lambda event_id: event if event_id == 1 else other
        result = analysis.diff_actions(1, 2)
        self.assertEqual(result["action_a"]["action_event_id"], 1)
        self.assertEqual(result["action_b"]["action_event_id"], 2)
        self.assertFalse(result["differences"]["binding_changes"]["changed"])

    def test_texture_pixels_and_export_use_explicit_action_and_restore(self):
        service = MODULES["resource_service"].ResourceService(self.ctx, self.ctx.invoke)
        RD.Subresource = NS
        RD.TextureSave = lambda: NS(slice=NS())
        RD.AlphaMapping = NS(Preserve=0, Discard=1, BlendToColor=2)
        RD.FileType = NS(**{n: n for n in ("PNG", "JPG", "BMP", "TGA", "EXR", "DDS", "HDR")})
        calls = []
        self.controller.GetTextureData = lambda rid, sub: bytes([self.controller.event % 256])
        self.controller.SaveTexture = lambda save, path: (
            calls.append((self.controller.event, save.mip, save.slice.sliceIndex))
            or NS(OK=lambda: True))
        data = service.get_texture_data("11", mip=1, slice_index=3, action_event_id=343)
        self.assertEqual(data["action_event_id"], 343)
        self.assertEqual(data["slice_index"], 3)
        self.assertNotIn("slice", data)
        self.assertEqual(data["content_base64"], "Vw==")
        self.assertEqual(self.controller.event, 99)
        current = service.get_texture_data("11")
        self.assertEqual(current["event_id"], 99)
        self.assertNotIn("action_event_id", current)
        with tempfile.TemporaryDirectory() as directory:
            result = service.save_texture("11", str(Path(directory) / "texture.png"),
                                          mip=1, slice_index=3, action_event_id=343)
            self.assertEqual(result["event_phase"], "after")
            self.assertEqual(calls[-1], (343, 1, 3))
            self.controller.SaveTexture = lambda *args: NS(OK=lambda: False, Message=lambda: "failed")
            with self.assertRaisesRegex(RuntimeError, "TEXTURE_SAVE_FAILED"):
                service.save_texture("11", str(Path(directory) / "failed.png"), action_event_id=343)
        self.assertEqual(self.controller.event, 99)
        with self.assertRaisesRegex(ValueError, "INVALID_SAMPLE"):
            service.get_texture_data("11", sample=1, action_event_id=343)

    def test_array_variables_bounded_expansion_and_nonfinite(self):
        adapter = MODULES["shader_variables"].read_variables
        arrays = [variable("lights", members=[variable("[%s]" % i, float("inf")) for i in range(5)])]
        decl = [layout("lights", elements=5)]
        result = adapter(arrays, decl, [0], 2, 2)
        self.assertTrue(result["children"]["has_more"])
        item = result["children"]["items"][0]
        self.assertEqual(item["child_path"], [0, 2])
        self.assertEqual(item["layout"]["byte_offset"], 48)
        json.dumps(result, allow_nan=False)
        with self.assertRaisesRegex(ValueError, "INVALID_CHILD_PATH"):
            adapter(arrays, decl, [True], 0, 50)

    def test_public_tools_real_file_ipc_and_schema(self):
        try:
            from mcp_server import server
        except ImportError:
            self.skipTest("FastMCP unavailable")
        from test_bridge import BridgeTests, CLIENT
        fixture = BridgeTests("test_concurrent_clients_are_serialized")
        fixture.setUp()
        try:
            fixture.server.handler = HANDLER.RequestHandler(self.service)
            fixture.start_server()
            with patch.object(server, "bridge", CLIENT.RenderDocBridge()):
                result = server.get_pipeline_state(action_event_id=343)
                self.assertEqual(result["pipeline_kind"], "graphics")
                rows = server.get_pipeline_stage(343, "FS", "constant_buffers")["items"]
                binding_id = rows[0]["binding_id"]
                expanded = server.inspect_pipeline_binding(343, binding_id, "variables", [0])
                self.assertEqual(expanded["children"]["items"][0]["value"], [1.5])
                self.assertGreater(server.get_action_textures(343)["total_count"], 0)
                with self.assertRaises(CLIENT.RenderDocBridgeError):
                    server.get_pipeline_stage(343, "FS", "invalid")
                with self.assertRaises(CLIENT.RenderDocBridgeError):
                    server.bridge.call("get_pipeline_state", {"event_id": 343})
            tools = asyncio.run(server.mcp.list_tools())
            schema = next(t.parameters for t in tools if t.name == "get_pipeline_state")
            self.assertEqual(schema["required"], ["action_event_id"])
            self.assertNotIn("event_id", schema["properties"])
        finally:
            fixture.tearDown()


if __name__ == "__main__":
    unittest.main()
