"""Mesh tool regressions (SNorm decode, post-VS signatures, instances, replay safety)."""

import enum
import importlib.util
import struct
import tempfile
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
NS = types.SimpleNamespace


class ResourceId(int):
    @staticmethod
    def Null():
        return ResourceId(0)


# Mirrors the real renderdoc.CompType: no Double/Half members (those var types
# are carried as Float with a wider compByteWidth).
CompType = enum.IntEnum(
    "CompType", "Typeless Float UNorm SNorm UInt SInt UScaled SScaled Depth UNormSRGB")
VarType = enum.IntEnum(
    "VarType", "Float Double Half SInt UInt SShort UShort SLong ULong SByte UByte Bool Enum Struct")
ActionFlags = enum.IntFlag("ActionFlags", {"Drawcall": 1, "Indexed": 2, "Instanced": 4})
ShaderStage = enum.IntEnum("ShaderStage", "Vertex Hull Domain Geometry Pixel")
MeshDataStage = enum.IntEnum("MeshDataStage", "VSIn VSOut GSOut")
ShaderBuiltin = enum.IntEnum("ShaderBuiltin", "Position")
ResourceFormatType = enum.IntEnum("ResourceFormatType", "Undefined Regular")


class MeshFormat:
    def __init__(self):
        self.indexResourceId = ResourceId.Null()
        self.indexByteOffset = 0
        self.indexByteStride = 0
        self.baseVertex = 0
        self.numIndices = 0
        self.vertexByteOffset = 0
        self.format = None
        self.vertexResourceId = ResourceId.Null()
        self.vertexByteStride = 0
        self.name = ""
        self.topology = "TriangleList"
        self.instanced = False


class ResourceFormat:
    def __init__(self):
        self.compType = CompType.Float
        self.type = ResourceFormatType.Regular
        self.compCount = 1
        self.compByteWidth = 4

    def Name(self):
        return "FORMAT(%s x%d b%d)" % (self.compType.name, self.compCount, self.compByteWidth)

    def Special(self):
        return self.type != ResourceFormatType.Regular

    def BGRAOrder(self):
        return False


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_module(service_name):
    rd = types.ModuleType("renderdoc")
    rd.ResourceId, rd.CompType, rd.VarType = ResourceId, CompType, VarType
    rd.ActionFlags, rd.ShaderStage, rd.MeshDataStage = ActionFlags, ShaderStage, MeshDataStage
    rd.MeshFormat, rd.ResourceFormat, rd.ShaderBuiltin = MeshFormat, ResourceFormat, ShaderBuiltin
    rd.ResourceFormatType = ResourceFormatType
    packages = {"renderdoc": rd}
    for name in ("renderdoc_extension", "renderdoc_extension.services"):
        packages[name] = types.ModuleType(name)
        packages[name].__path__ = []
    with patch.dict(sys.modules, packages):
        load("renderdoc_extension.services.replay_query",
             "renderdoc_extension/services/replay_query.py")
        return load("renderdoc_extension.services." + service_name,
                    "renderdoc_extension/services/" + service_name + ".py")


MESH = load_module("mesh_service")
CAPTURE = load_module("capture_manager")


class Pipe:
    def __init__(self, controller):
        self._controller = controller

    def GetIBuffer(self):
        return self._controller.ib

    def GetVBuffers(self):
        return self._controller.vbs

    def GetVertexInputs(self):
        return self._controller.vertex_inputs

    def GetShaderReflection(self, stage):
        return self._controller.reflections.get(stage)

    def GetShader(self, stage):
        return self._controller.bound_shaders.get(stage, ResourceId.Null())

    def HasAlignedPostVSData(self, stage):
        return self._controller.aligned_postvs.get(stage, False)

    def GetRasterizedStream(self):
        return self._controller.rasterized_stream


class Controller:
    def __init__(self):
        self.event = 99
        self.events = []
        self.api = "D3D11"
        self.ib = NS(resourceId=ResourceId.Null(), byteOffset=0, byteStride=0)
        self.vbs = []
        self.vertex_inputs = []
        # stage enum -> reflection NS(outputSignature=[...]) or None
        self.reflections = {}
        # stage enum -> bound shader resource (empty = not bound)
        self.bound_shaders = {}
        # MeshDataStage enum -> bool (Vulkan VSOut uses aligned compute buffers)
        self.aligned_postvs = {}
        self.rasterized_stream = 0
        self.postvs = None
        self.postvs_calls = []
        self.buffers = {}

    def SetFrameEvent(self, event, force):
        self.event = event
        self.events.append(event)

    def GetPipelineState(self):
        return Pipe(self)

    def GetAPIProperties(self):
        return NS(pipelineType=self.api)

    def GetPostVSData(self, instance, view, stage):
        self.postvs_calls.append((instance, view, stage))
        return self.postvs

    def GetBufferData(self, rid, offset, length):
        return self.buffers.get(int(rid), b"")

    def GetBuffers(self):
        return []

    def GetResources(self):
        return []


class Context:
    def __init__(self, controller):
        self.controller = controller
        self.action = NS(eventId=343, actionId=7, numIndices=3, numInstances=4,
                         vertexOffset=30, baseVertex=0, indexOffset=0, instanceOffset=0,
                         flags=ActionFlags.Drawcall | ActionFlags.Indexed,
                         name="DrawBox")
        self.loaded = True

    def IsCaptureLoaded(self):
        return self.loaded

    def CurEvent(self):
        return 99

    def GetAction(self, eid):
        return self.action if eid == 343 else None

    def invoke(self, callback):
        callback(self.controller)


def postvs_mesh(rid=7, stride=32, base=0):
    return NS(vertexResourceId=ResourceId(rid), vertexByteStride=stride,
              vertexByteOffset=base,
              topology="TriangleList", numIndices=3, indexResourceId=ResourceId.Null(),
              indexByteOffset=0, indexByteStride=0, baseVertex=0, status=0)


def sig(name, reg, comps, var_type=VarType.Float, system_value=None, stream=0):
    return NS(semanticIdxName=name, semanticName=name.rstrip("0123456789"), varName="",
              regIndex=reg, compCount=comps, varType=var_type, systemValue=system_value,
              stream=stream)


class MeshDecodeTests(unittest.TestCase):
    def setUp(self):
        self.unpack = MESH.MeshService(NS(), lambda cb: None)._unpack_vertex_data

    def test_snorm_maps_full_signed_range(self):
        snorm8 = NS(compType=CompType.SNorm, compCount=1, compByteWidth=1,
                    BGRAOrder=lambda: False)
        self.assertEqual(self.unpack(snorm8, b"\x00", 0), (0.0,))
        self.assertAlmostEqual(self.unpack(snorm8, b"\x7f", 0)[0], 1.0)
        self.assertAlmostEqual(self.unpack(snorm8, b"\x80", 0)[0], -1.0)
        self.assertAlmostEqual(self.unpack(snorm8, b"\x40", 0)[0], 64.0 / 127.0)
        snorm16 = NS(compType=CompType.SNorm, compCount=1, compByteWidth=2,
                     BGRAOrder=lambda: False)
        self.assertAlmostEqual(self.unpack(snorm16, struct.pack("<h", 32767), 0)[0], 1.0)
        self.assertAlmostEqual(self.unpack(snorm16, struct.pack("<h", -32768), 0)[0], -1.0)

    def test_unorm_decode_is_unchanged(self):
        unorm8 = NS(compType=CompType.UNorm, compCount=1, compByteWidth=1,
                    BGRAOrder=lambda: False)
        self.assertAlmostEqual(self.unpack(unorm8, b"\xff", 0)[0], 1.0)
        self.assertAlmostEqual(self.unpack(unorm8, b"\x00", 0)[0], 0.0)
        self.assertAlmostEqual(self.unpack(unorm8, b"\x80", 0)[0], 128.0 / 255.0)

    def test_half_and_double_decode_via_float_byte_width(self):
        half = NS(compType=CompType.Float, compCount=1, compByteWidth=2,
                  BGRAOrder=lambda: False)
        self.assertAlmostEqual(self.unpack(half, struct.pack("<e", 0.5), 0)[0], 0.5)
        double = NS(compType=CompType.Float, compCount=1, compByteWidth=8,
                    BGRAOrder=lambda: False)
        self.assertAlmostEqual(self.unpack(double, struct.pack("<d", 1.25), 0)[0], 1.25)

    def test_64bit_integers_decode_full_width(self):
        # 'l'/'L' are only 4 bytes on Windows; 8-byte integers must use q/Q
        ulong = NS(compType=CompType.UInt, compCount=1, compByteWidth=8,
                   BGRAOrder=lambda: False)
        self.assertEqual(
            self.unpack(ulong, struct.pack("<Q", 0x1122334455667788), 0),
            (0x1122334455667788,))
        slong = NS(compType=CompType.SInt, compCount=2, compByteWidth=8,
                   BGRAOrder=lambda: False)
        self.assertEqual(
            self.unpack(slong, struct.pack("<qq", -1, 0x7FFFFFFFFFFFFFFF), 0),
            (-1, 0x7FFFFFFFFFFFFFFF))


class MeshDataTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.ctx = Context(self.controller)
        self.mesh = MESH.MeshService(self.ctx, self.ctx.invoke)

    def test_vsout_attributes_come_from_output_signature(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4), sig("TEXCOORD0", 1, 3)])}
        self.controller.buffers[7] = struct.pack("<7f", 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)

        result = self.mesh.get_mesh_data(343, stage="VSOut")

        self.assertEqual([a["name"] for a in result["attributes"]],
                         ["SV_POSITION0", "TEXCOORD0"])
        vertex = result["items"][0]
        self.assertEqual(vertex["SV_POSITION0"], [1.0, 2.0, 3.0, 4.0])
        self.assertEqual(vertex["TEXCOORD0"], [5.0, 6.0, 7.0])
        self.assertNotIn("event_id", result)

    def test_d3d_layout_hoists_position_and_pads_to_four(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("COLOR0", 1, 4), sig("POSITION", 0, 3, system_value=ShaderBuiltin.Position)])}
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "VSOut", 0)
        self.assertEqual([i.name for i in inputs], ["POSITION", "COLOR0"])
        self.assertEqual(inputs[0].vertexByteOffset, 0)    # position first, padded 4*4
        self.assertEqual(inputs[1].vertexByteOffset, 16)

    def test_aligned_vulkan_layout_and_unaligned_packed(self):
        # Aligned (Vulkan VSOut compute-built): signature order, vec4 alignment
        self.controller.aligned_postvs = {MeshDataStage.VSOut: True}
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("A", 0, 3), sig("B", 1, 3), sig("C", 2, 2)])}
        self.controller.postvs = postvs_mesh(stride=48)
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "VSOut", 0)
        # float3 @0 (12B) -> align 16; float3 @16 -> 28 -> align 16 -> 32; float2 @32
        self.assertEqual([i.vertexByteOffset for i in inputs], [0, 16, 32])

        # Unaligned (D3D/GL/Vulkan GSOut): packed running offsets, no alignment
        self.controller.aligned_postvs = {}
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "VSOut", 0)
        self.assertEqual([i.vertexByteOffset for i in inputs], [0, 12, 24])

    def test_multi_stream_gsout_filters_by_rasterized_stream(self):
        self.controller.postvs = postvs_mesh()
        # Multi-stream outputs only exist on geometry shaders
        self.controller.bound_shaders = {ShaderStage.Geometry: ResourceId(9)}
        self.controller.reflections = {ShaderStage.Geometry: NS(outputSignature=[
            sig("A", 0, 4, stream=0),
            sig("B", 1, 4, stream=1),
            sig("C", 2, 4, stream=1),
        ])}
        self.controller.rasterized_stream = 1
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "GSOut", 0)
        self.assertEqual([i.name for i in inputs], ["B", "C"])
        self.assertEqual([i.vertexByteOffset for i in inputs], [0, 16])

    def test_vsout_always_reads_stream_zero(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4, stream=0)])}
        # A downstream geometry shader rasterizing stream 1 must not filter
        # the vertex-stage signature
        self.controller.rasterized_stream = 1
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "VSOut", 0)
        self.assertEqual([i.name for i in inputs], ["SV_POSITION0"])

    def test_gsout_disabled_rasterizer_falls_back_to_stream_zero(self):
        self.controller.postvs = postvs_mesh()
        self.controller.bound_shaders = {ShaderStage.Geometry: ResourceId(9)}
        self.controller.reflections = {ShaderStage.Geometry: NS(outputSignature=[
            sig("A", 0, 4, stream=0),
            sig("B", 1, 4, stream=1),
        ])}
        # Rasterizer disabled -> GetRasterizedStream() returns -1, read stream 0
        self.controller.rasterized_stream = -1
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "GSOut", 0)
        self.assertEqual([i.name for i in inputs], ["A"])

    def test_layout_exceeding_stride_fails_loudly(self):
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("A", 0, 4), sig("B", 1, 4), sig("C", 2, 4)])}
        self.controller.postvs = postvs_mesh(stride=32)
        with self.assertRaisesRegex(ValueError, "MESH_SIGNATURE_UNAVAILABLE"):
            self.mesh._get_postvs_inputs(self.controller, self.ctx.action, "VSOut", 0)

    def test_postvs_base_offset_is_included(self):
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4)])}
        self.controller.postvs = postvs_mesh(base=640)  # e.g. instance 20 of stride 32
        inputs = self.mesh._get_postvs_inputs(
            self.controller, self.ctx.action, "VSOut", 20)
        self.assertEqual(inputs[0].vertexByteOffset, 640)

    def test_gsout_falls_back_to_domain_only_when_geometry_unbound(self):
        self.controller.postvs = postvs_mesh()
        # No geometry shader bound -> tessellation (domain) output is used
        self.controller.reflections = {
            ShaderStage.Domain: NS(outputSignature=[sig("SV_POSITION0", 0, 4)]),
        }
        self.controller.buffers[7] = struct.pack("<4f", 1.0, 2.0, 3.0, 4.0)
        result = self.mesh.get_mesh_data(343, stage="GSOut")
        self.assertEqual([a["name"] for a in result["attributes"]], ["SV_POSITION0"])

        # A bound geometry shader must use its own reflection, even if the
        # domain stage also has a signature available.
        self.controller.bound_shaders = {ShaderStage.Geometry: ResourceId(9)}
        self.controller.reflections = {
            ShaderStage.Geometry: NS(outputSignature=[sig("GSOUT_A", 0, 4)]),
            ShaderStage.Domain: NS(outputSignature=[sig("SV_POSITION0", 0, 4)]),
        }
        self.controller.buffers[7] = struct.pack("<8f", 9.0, 9.0, 9.0, 9.0, 1.0, 2.0, 3.0, 4.0)
        result = self.mesh.get_mesh_data(343, stage="GSOut")
        self.assertEqual([a["name"] for a in result["attributes"]], ["GSOUT_A"])
        self.assertEqual(result["items"][0]["GSOUT_A"], [9.0, 9.0, 9.0, 9.0])

    def test_gsout_bound_geometry_with_broken_reflection_fails_loudly(self):
        self.controller.postvs = postvs_mesh()
        self.controller.bound_shaders = {ShaderStage.Geometry: ResourceId(9)}
        self.controller.reflections = {
            ShaderStage.Geometry: None,
            ShaderStage.Domain: NS(outputSignature=[sig("SV_POSITION0", 0, 4)]),
        }
        with self.assertRaisesRegex(ValueError, "MESH_SIGNATURE_UNAVAILABLE"):
            self.mesh.get_mesh_data(343, stage="GSOut")

    def test_vsout_without_signature_fails_loudly(self):
        self.controller.postvs = postvs_mesh()
        with self.assertRaisesRegex(ValueError, "MESH_SIGNATURE_UNAVAILABLE"):
            self.mesh.get_mesh_data(343, stage="VSOut")

    def test_postvs_failure_propagates_instead_of_silent_none(self):
        def broken(instance, view, stage):
            raise RuntimeError("driver not loaded")

        self.controller.GetPostVSData = broken
        with self.assertRaisesRegex(RuntimeError, "driver not loaded"):
            self.mesh.get_mesh_data(343, stage="VSOut")

    def test_vsout_signature_types_drive_format(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("DATA0", 0, 2, VarType.UInt), sig("HALVES0", 1, 4, VarType.Half)])}
        result = self.mesh.get_mesh_data(343, stage="VSOut")
        data, halves = result["attributes"]
        self.assertEqual(data["format"], "FORMAT(UInt x2 b4)")
        # Post-VS buffers expand small types to 32 bits: Half decodes as float32
        self.assertEqual(halves["format"], "FORMAT(Float x4 b4)")

    def test_export_csv_uses_signature_names(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4), sig("TEXCOORD0", 1, 3)])}
        self.controller.buffers[7] = struct.pack("<7f", 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)
        with tempfile.TemporaryDirectory() as directory:
            result = self.mesh.export_mesh_csv(343, str(Path(directory) / "mesh.csv"),
                                               stage="VSOut")
            header = Path(result["output_path"]).read_text().splitlines()[0]
            self.assertIn("SV_POSITION0.x", header)
            self.assertIn("SV_POSITION0.w", header)
            self.assertIn("TEXCOORD0.z", header)
            self.assertEqual(result["vertex_count"], 3)

    def test_vsin_reads_selected_instance(self):
        self.controller.vbs = [
            NS(resourceId=ResourceId(1), byteOffset=0, byteStride=12),
            NS(resourceId=ResourceId(2), byteOffset=0, byteStride=16),
        ]
        position_format, seed_format = ResourceFormat(), ResourceFormat()
        position_format.compCount, seed_format.compCount = 3, 4
        self.controller.vertex_inputs = [
            NS(used=True, genericEnabled=False, perInstance=False, instanceRate=0,
               name="POSITION", vertexBuffer=0, byteOffset=0, format=position_format),
            NS(used=True, genericEnabled=False, perInstance=True, instanceRate=1,
               name="SEED", vertexBuffer=1, byteOffset=4, format=seed_format),
        ]

        inputs = self.mesh._get_mesh_inputs(self.controller, self.ctx.action, 2)
        self.assertEqual(inputs[0].vertexByteOffset, 30 * 12)  # vertexOffset * stride
        self.assertEqual(inputs[1].vertexByteOffset, 4 + 2 * 16)  # instance * stride
        self.assertEqual(inputs[1].vertexResourceId, ResourceId(2))
        self.assertTrue(inputs[1].instanced)

        # StartInstanceLocation shifts the whole read window
        self.ctx.action.instanceOffset = 7
        inputs = self.mesh._get_mesh_inputs(self.controller, self.ctx.action, 0)
        self.assertEqual(inputs[1].vertexByteOffset, 4 + 7 * 16)

        # Step rate divides only the 0-based instance index, not the window base
        self.controller.vertex_inputs[1].instanceRate = 2
        inputs = self.mesh._get_mesh_inputs(self.controller, self.ctx.action, 5)
        self.assertEqual(inputs[1].vertexByteOffset, 4 + (7 + 5 // 2) * 16)

        # Rate 0 reads element 0 constantly across instances
        self.controller.vertex_inputs[1].instanceRate = 0
        inputs = self.mesh._get_mesh_inputs(self.controller, self.ctx.action, 3)
        self.assertEqual(inputs[1].vertexByteOffset, 4 + 7 * 16)

    def test_per_instance_attribute_is_constant_across_vertices(self):
        self.ctx.action = NS(eventId=343, actionId=7, numIndices=3, numInstances=4,
                             vertexOffset=0, baseVertex=0, indexOffset=0,
                             instanceOffset=0, flags=ActionFlags.Drawcall, name="DrawBox")
        self.controller.vbs = [
            NS(resourceId=ResourceId(1), byteOffset=0, byteStride=12),
            NS(resourceId=ResourceId(2), byteOffset=0, byteStride=16),
        ]
        position_format, seed_format = ResourceFormat(), ResourceFormat()
        position_format.compCount, seed_format.compCount = 3, 4
        self.controller.vertex_inputs = [
            NS(used=True, genericEnabled=False, perInstance=False, instanceRate=0,
               name="POSITION", vertexBuffer=0, byteOffset=0, format=position_format),
            NS(used=True, genericEnabled=False, perInstance=True, instanceRate=1,
               name="SEED", vertexBuffer=1, byteOffset=0, format=seed_format),
        ]
        self.controller.buffers[1] = struct.pack("<9f", 0, 0, 0, 1, 0, 0, 0, 1, 0)
        self.controller.buffers[2] = struct.pack("<8f", 1, 2, 3, 4, 5, 6, 7, 8)

        result = self.mesh.get_mesh_data(343, instance=1)
        self.assertEqual(result["total_count"], 3)
        seeds = [vertex["SEED"] for vertex in result["items"]]
        self.assertEqual(seeds, [[5.0, 6.0, 7.0, 8.0]] * 3)
        self.assertTrue(result["attributes"][1]["instanced"])

    def test_postvs_data_receives_instance_index(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4)])}
        self.controller.buffers[7] = struct.pack("<4f", 1.0, 2.0, 3.0, 4.0)
        self.mesh.get_mesh_data(343, stage="VSOut", instance=3)
        self.assertEqual(self.controller.postvs_calls,
                         [(3, 0, MeshDataStage.VSOut)])

    def test_invalid_stage_and_instance_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "INVALID_STAGE"):
            self.mesh.get_mesh_data(343, stage="PostTLAS")
        with self.assertRaisesRegex(ValueError, "INVALID_INSTANCE"):
            self.mesh.get_mesh_data(343, instance=-1)
        with self.assertRaisesRegex(ValueError, "INVALID_INSTANCE"):
            self.mesh.export_mesh_csv(343, "out.csv", instance=-1)
        with self.assertRaisesRegex(ValueError, "INVALID_INSTANCE"):
            self.mesh.get_mesh_data(343, instance="1")

    def test_instance_beyond_draw_count_is_rejected(self):
        self.controller.postvs = postvs_mesh()
        self.controller.reflections = {ShaderStage.Vertex: NS(outputSignature=[
            sig("SV_POSITION0", 0, 4)])}
        with self.assertRaisesRegex(ValueError, "INVALID_INSTANCE: 4"):
            self.mesh.get_mesh_data(343, stage="VSOut", instance=4)

        self.ctx.action.numInstances = 1
        with self.assertRaisesRegex(ValueError, "INVALID_INSTANCE: 2"):
            self.mesh.get_mesh_summary(343, instance=2)

    def test_queries_restore_replay_position(self):
        self.mesh.get_mesh_summary(343)
        self.assertEqual(self.controller.events, [343, 99])
        self.mesh.get_mesh_summary(343, instance=2)
        self.assertEqual(self.controller.events, [343, 99] * 2)

    def test_summary_reports_instance_and_attributes(self):
        summary = self.mesh.get_mesh_summary(343)
        self.assertEqual(summary["action_event_id"], 343)
        self.assertEqual(summary["instance"], 0)
        self.assertEqual(summary["name"], "DrawBox")
        self.assertEqual(summary["indexed"], True)


class CaptureStatusTests(unittest.TestCase):
    def _service(self, ctx, invoke):
        return CAPTURE.CaptureManager(ctx, invoke, runtime_info={
            "extension_version": "1.0.1a1",
            "renderdoc_version": "1.46",
            "ipc_version": 2,
        })

    def test_status_reports_versions_and_healthy_replay(self):
        ctx = NS(IsCaptureLoaded=lambda: True, GetCaptureFilename=lambda: "frame.rdc")

        def invoke(callback):
            callback(NS(
                GetAPIProperties=lambda: NS(pipelineType="D3D11", remoteReplay=False),
                GetFatalErrorStatus=lambda: NS(OK=lambda: True, Message=lambda: ""),
            ))

        status = self._service(ctx, invoke).get_capture_status()
        self.assertTrue(status["loaded"])
        self.assertEqual(status["extension_version"], "1.0.1a1")
        self.assertEqual(status["renderdoc_version"], "1.46")
        self.assertEqual(status["ipc_version"], 2)
        self.assertIs(status["replay_healthy"], True)
        self.assertIsNone(status["replay_error"])
        self.assertEqual(status["api"], "D3D11")
        self.assertIn("api", status)
        self.assertIn("filename", status)

    def test_status_surfaces_fatal_replay_error(self):
        ctx = NS(IsCaptureLoaded=lambda: True, GetCaptureFilename=lambda: "frame.rdc")

        def invoke(callback):
            callback(NS(
                GetAPIProperties=lambda: NS(pipelineType="D3D11", remoteReplay=False),
                GetFatalErrorStatus=lambda: NS(OK=lambda: False, Message=lambda: "device removed"),
            ))

        status = self._service(ctx, invoke).get_capture_status()
        self.assertIs(status["replay_healthy"], False)
        self.assertIn("device removed", status["replay_error"])

    def test_status_surfaces_transport_failure(self):
        ctx = NS(IsCaptureLoaded=lambda: True, GetCaptureFilename=lambda: "frame.rdc")

        def invoke(callback):
            raise RuntimeError("replay controller disconnected")

        status = self._service(ctx, invoke).get_capture_status()
        self.assertIs(status["replay_healthy"], False)
        self.assertIn("disconnected", status["replay_error"])
        # Response contract: api/filename keys stay present even on failure
        self.assertIsNone(status["api"])
        self.assertEqual(status["filename"], "frame.rdc")

    def test_unloaded_status_still_reports_versions(self):
        ctx = NS(IsCaptureLoaded=lambda: False)
        status = self._service(ctx, lambda cb: None).get_capture_status()
        self.assertFalse(status["loaded"])
        self.assertIsNone(status["replay_healthy"])
        self.assertEqual(status["ipc_version"], 2)
        self.assertEqual(status["extension_version"], "1.0.1a1")


class RestoreFailureTests(unittest.TestCase):
    def test_stable_prefix_leads_merged_error(self):
        spec = importlib.util.spec_from_file_location(
            "replay_query_under_test",
            ROOT / "renderdoc_extension/services/replay_query.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        result = {}
        module.record_restore_failure(result, RuntimeError("boom"))
        self.assertTrue(str(result["error"]).startswith("REPLAY_RESTORE_FAILED"))

        result = {"error": ValueError("INVALID_MARKER_FILTER: no actions matched")}
        module.record_restore_failure(result, RuntimeError("boom"))
        message = str(result["error"])
        self.assertTrue(message.startswith("REPLAY_RESTORE_FAILED"))
        self.assertIn("INVALID_MARKER_FILTER", message)
        self.assertIn("boom", message)


if __name__ == "__main__":
    unittest.main()
