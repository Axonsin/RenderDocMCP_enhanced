"""Resource Inspector contracts without a RenderDoc installation or GPU."""

import enum
import asyncio
import base64
import importlib.util
import json
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


Kind = enum.IntEnum("ResourceType", "Unknown Device Memory Buffer Texture Shader View SwapchainImage")
Basic = enum.IntEnum("SDBasic", "Chunk Struct Array Null Buffer String Enum UnsignedInteger "
                     "SignedInteger Float Boolean Character Resource GPUAddress")
Flags = enum.IntFlag("SDTypeFlags", {"NoFlags": 0, "Hidden": 2, "HasCustomString": 1})
Usage = enum.IntEnum("ResourceUsage", "Clear CS_RWResource CS_Resource CopyDst")
ActionFlags = enum.IntFlag("ActionFlags", {"PushMarker": 1, "PopMarker": 2, "SetMarker": 4})


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def modules():
    rd = types.ModuleType("renderdoc")
    rd.ResourceType, rd.ResourceId, rd.SDBasic = Kind, ResourceId, Basic
    rd.SDTypeFlags, rd.ActionFlags = Flags, ActionFlags
    rd.BufferCategory = enum.IntFlag("BufferCategory",
                                   {"Vertex": 1, "Index": 2, "Constants": 4,
                                    "ReadWrite": 8, "Indirect": 16})
    rd.ShaderStage = enum.IntEnum("ShaderStage", "Vertex Hull Domain Geometry Pixel Compute")
    packages = {"renderdoc": rd}
    for name in ("renderdoc_extension", "renderdoc_extension.services", "renderdoc_extension.utils"):
        packages[name] = types.ModuleType(name)
        packages[name].__path__ = []
    with patch.dict(sys.modules, packages):
        utils = packages["renderdoc_extension.utils"]
        utils.Parsers = load("renderdoc_extension.utils.parsers",
                             "renderdoc_extension/utils/parsers.py").Parsers
        utils.Helpers = NS()
        utils.Serializers = NS(serialize_flags=lambda value: [])
        for name in ("resource_catalog", "structured_data", "replay_query", "resource_service", "analysis_service",
                     "action_service"):
            module = load("renderdoc_extension.services." + name,
                          "renderdoc_extension/services/" + name + ".py")
            if name == "resource_service":
                resource = module
            if name == "analysis_service":
                analysis = module
            if name == "action_service":
                action = module
        services = packages["renderdoc_extension.services"]
        for name in ("CaptureManager", "ActionService", "SearchService", "ResourceService",
                     "PipelineService", "ShaderEditService", "MeshService", "AnalysisService",
                     "BatchService"):
            setattr(services, name, object)
        facade = load("renderdoc_extension.renderdoc_facade",
                      "renderdoc_extension/renderdoc_facade.py")
        handler = load("renderdoc_extension.request_handler",
                       "renderdoc_extension/request_handler.py")
    return resource, analysis, facade, handler, action


RESOURCE, ANALYSIS, FACADE, HANDLER, ACTION = modules()


class Node:
    def __init__(self, name, basic=Basic.Struct, value=None, children=(), flags=0,
                 display="", byte_size=0):
        self.name = name
        self.type = NS(name=basic.name, basetype=basic, flags=flags, byteSize=byte_size)
        self.value, self.children = value, list(children)
        self.data = NS(string=display, basic=NS(u=value, i=value, c=value))

    def NumChildren(self):
        return len(self.children)

    def GetChild(self, index):
        return self.children[index]

    def AsResourceId(self):
        return self.value

    def AsString(self):
        return self.value

    def AsBool(self):
        return self.value

    def AsFloat(self):
        return self.value


def desc(rid, kind, name, parents=(), derived=(), chunks=()):
    return NS(resourceId=ResourceId(rid), type=kind, name=name,
              parentResources=[ResourceId(i) for i in parents],
              derivedResources=[ResourceId(i) for i in derived],
              initialisationChunks=list(chunks))


class Controller:
    def __init__(self):
        self.resources = [
            desc(86983, Kind.Buffer, "Buffer 86983", [190, 86826], [99], [0, 1]),
            desc(190, Kind.Device, "Device 190", derived=[86983]),
            desc(86826, Kind.Memory, "Memory 86826", derived=[86983]),
            desc(200, Kind.Shader, "Shader 200"), desc(201, Kind.View, "View 201"),
            desc(202, Kind.Texture, "Same"), desc(203, Kind.SwapchainImage, "Same"),
        ]
        self.buffers = [NS(resourceId=self.resources[0].resourceId, length=11040, creationFlags=8)]
        self.textures = [NS(resourceId=r.resourceId, width=8, height=8, depth=1,
                            format=NS(Name=lambda: "RGBA8"), mips=1, arraysize=1,
                            byteSize=256, type="Texture2D", cubemap=False, msSamp=1)
                         for r in self.resources if r.type in (Kind.Texture, Kind.SwapchainImage)]
        self.chunks = [
            Node("vkCreateBuffer", Basic.Chunk, children=[
                Node("device", Basic.Resource, self.resources[1].resourceId),
                Node("CreateInfo", children=[
                    Node("size", Basic.UnsignedInteger, 11040),
                    Node("internal", Basic.UnsignedInteger, 99, flags=Flags.Hidden),
                    Node("usage", Basic.Enum, 3, flags=Flags.HasCustomString, display="A | B"),
                    Node("size", Basic.UnsignedInteger, 22),
                ]),
            ]),
            Node("vkBindBufferMemory", Basic.Chunk, children=[
                Node("memory", Basic.Resource, self.resources[2].resourceId),
                Node("memoryOffset", Basic.UnsignedInteger, 98304),
            ]),
            Node("unrelated"),
        ]
        self.usages = [NS(eventId=eid, usage=use, view=ResourceId(view)) for eid, use, view in
                       [(10, Usage.Clear, 0), (20, Usage.CS_RWResource, 201),
                        (30, Usage.CS_Resource, 0)]]
        self.fail_usage = False
        self.fail_structured = False
        self.usage_calls = []

    def GetResources(self):
        return self.resources

    def GetTextures(self):
        return self.textures

    def GetBuffers(self):
        return self.buffers

    def GetUsage(self, rid):
        # OpenGL-style bindings must receive the actual catalog object.
        assert rid is self.resources[0].resourceId
        self.usage_calls.append(rid)
        if self.fail_usage:
            raise RuntimeError("driver query failed")
        return self.usages

    def GetStructuredFile(self):
        if self.fail_structured:
            raise RuntimeError("structured data unavailable")
        return NS(chunks=self.chunks)

    def GetRootActions(self):
        draw = NS(eventId=20, flags=0, children=[], GetName=lambda _: "Dispatch")
        return [NS(eventId=1, flags=ActionFlags.PushMarker, children=[draw],
                   GetName=lambda _: "Compute Pass #1")]


class ResourceTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.names = {}
        self.loaded = True
        self.invokes = 0
        self.in_callback = False
        self.ctx = NS(IsCaptureLoaded=lambda: self.loaded, GetResourceName=self.name,
                      CurEvent=lambda: 1)
        self.service = RESOURCE.ResourceService(self.ctx, self.invoke)
        self.analysis = ANALYSIS.AnalysisService(self.ctx, self.invoke, None, None, self.service, None)
        self.facade = FACADE.RenderDocFacade.__new__(FACADE.RenderDocFacade)
        self.facade._resource, self.facade._analysis = self.service, self.analysis
        self.facade._action = ACTION.ActionService(self.ctx, self.invoke)
        self.handler = HANDLER.RequestHandler(self.facade)

    def name(self, rid):
        return self.names.get(int(rid), next((r.name for r in self.controller.resources
                                             if int(r.resourceId) == int(rid)), ""))

    def invoke(self, callback):
        self.assertFalse(self.in_callback, "nested BlockInvoke")
        self.invokes += 1
        self.in_callback = True
        try:
            callback(self.controller)
        finally:
            self.in_callback = False

    def test_full_directory_filters_stable_order_and_rename(self):
        result = self.service.list_resources()
        self.assertEqual(result["total_count"], 7)
        self.assertEqual(set(result["items"][0]), {"resource_id", "name", "resource_type"})
        self.assertEqual(self.service.list_resources("texture")["total_count"], 1)
        self.assertEqual(self.service.list_resources("swapchain_image")["total_count"], 1)
        page = self.service.list_resources(name_filter="sAmE", offset=1, limit=1)
        self.assertEqual(page["items"][0]["resource_id"], "ResourceId::203")
        self.names[190] = "Renamed"
        self.assertEqual(self.service.list_resources(name_filter="renamed")["total_count"], 1)
        ids = [i["resource_id"] for i in self.service.list_resources(sort_by="resource_id")["items"]]
        self.assertEqual(ids[0], "ResourceId::190")
        self.assertEqual(self.controller.usage_calls, [])

    def test_inspection_matches_buffer_relations_and_summary(self):
        result = self.service.inspect_resource("86983")
        json.dumps(result, allow_nan=False)
        self.assertEqual(self.invokes, 1)
        self.assertEqual(result["metadata"]["byte_size"], 11040)
        relations = result["related_resources"]["items"]
        self.assertEqual([i["relationship"] for i in relations], ["parent", "parent", "derived"])
        self.assertTrue(relations[2]["missing"])
        self.assertEqual(result["usage"]["event_count"], 3)
        self.assertNotIn("events", result["usage"])
        self.assertEqual(result["initialization"]["items"][1]["name"], "vkBindBufferMemory")
        self.assertEqual(self.service.inspect_resource("86983", 2, 1)["related_resources"]["items"],
                         relations[2:])

    def test_many_relations_and_initialization_calls_are_paged(self):
        self.controller.resources[0].derivedResources = [ResourceId(i) for i in range(1000, 1600)]
        self.controller.resources[0].initialisationChunks = [0] * 25
        result = self.service.inspect_resource("86983")
        self.assertEqual(result["related_resources"]["total_count"], 602)
        self.assertEqual(result["related_resources"]["returned_count"], 50)
        self.assertEqual(result["initialization"]["returned_count"], 20)
        self.assertTrue(result["initialization"]["has_more"])
        self.assertEqual(self.service.get_resource_initialization("86983", offset=20)["returned_count"], 5)

    def test_usage_unavailable_empty_and_failure_are_distinct(self):
        self.assertEqual(self.service.inspect_resource("190")["usage"]["reason"], "unsupported_resource_type")
        self.assertFalse(self.analysis.trace_resource_usage("190")["available"])
        self.controller.usages = []
        self.assertTrue(self.service.inspect_resource("86983")["usage"]["available"])
        self.controller.fail_usage = True
        self.controller.fail_structured = True
        result = self.service.inspect_resource("86983")
        self.assertEqual(result["usage"]["reason"], "query_failed")
        self.assertEqual(result["initialization"]["reason"], "query_failed")
        self.assertEqual(result["metadata"]["byte_size"], 11040)
        with self.assertRaisesRegex(ValueError, "RESOURCE_QUERY_FAILED"):
            self.analysis.trace_resource_usage("86983")

    def test_usage_paging_preserves_unmatched_actions_and_global_summaries(self):
        result = self.analysis.trace_resource_usage("86983", before_event_id=25, offset=2, limit=1)
        self.assertEqual(result["total_count"], 3)
        self.assertEqual(result["events"][0]["event_id"], 30)
        self.assertEqual(result["latest_writer_before_event"]["event_id"], 20)
        self.assertEqual(result["read_count"], 2)
        self.assertEqual(result["write_count"], 2)
        self.assertNotIn("reads", result)
        result = self.analysis.trace_resource_usage("86983", marker_filter="compute")
        self.assertEqual(result["total_count"], 1)
        self.assertEqual(result["events"][0]["view_resource_id"], "ResourceId::201")
        self.assertEqual(result["events"][0]["marker_path"], "Compute Pass #1")
        self.assertEqual(self.analysis.trace_resource_usage("86983", event_id_range={"min": 25})["total_count"], 1)
        self.assertEqual(self.analysis.trace_resource_usage("86983", exclude_markers=["compute"])["total_count"], 0)

    def test_multiple_usages_at_one_event_have_distinct_record_and_event_counts(self):
        self.controller.usages.append(NS(eventId=20, usage=Usage.CS_Resource, view=ResourceId(0)))
        result = self.analysis.trace_resource_usage("86983", limit=1)
        self.assertEqual((result["usage_count"], result["event_count"]), (4, 3))
        self.assertEqual(self.service.inspect_resource("86983")["usage"]["event_count"], 3)

    def test_timeline_mapping_covers_renderdoc_usage_enum(self):
        usage_enum = load("timeline_usage_enum", "stubs/renderdoc/_ResourceUsage.py").ResourceUsage
        groups = {
            "read": ("Unused VertexBuffer IndexBuffer VS_Constants HS_Constants DS_Constants "
                     "GS_Constants PS_Constants CS_Constants TS_Constants MS_Constants All_Constants "
                     "VS_Resource HS_Resource DS_Resource GS_Resource PS_Resource CS_Resource "
                     "TS_Resource MS_Resource All_Resource InputTarget Indirect ResolveSrc CopySrc"),
            "write": "StreamOut ColorTarget DepthStencilTarget ResolveDst CopyDst CPUWrite",
            "read_write": ("VS_RWResource HS_RWResource DS_RWResource GS_RWResource PS_RWResource "
                           "CS_RWResource TS_RWResource MS_RWResource All_RWResource GenMips Copy Resolve"),
            "barrier": "Barrier",
            "clear": "Clear Discard",
        }
        expected = {name: category for category, names in groups.items() for name in names.split()}
        self.assertEqual(set(expected), {item.name for item in usage_enum})
        for name, category in expected.items():
            with self.subTest(usage=name):
                self.assertEqual(self.analysis._classify_timeline_usage(name), category)
        # Timeline's final else branch also renders an unrecognised usage as Reads.
        self.assertEqual(self.analysis._classify_timeline_usage("FutureUsage"), "read")

    def test_timeline_counts_filters_and_original_usage(self):
        values = [(10, "Clear"), (20, "Barrier"), (20, "GenMips"),
                  (30, "Discard"), (30, "CopyDst"), (40, "PS_Resource"), (40, "FutureUsage")]
        self.controller.usages = [NS(eventId=eid, usage=use, view=ResourceId(201))
                                  for eid, use in values]
        result = self.analysis.trace_resource_usage("86983", offset=1, limit=1)
        self.assertEqual(result["category_counts"], {
            "read": 2, "write": 1, "read_write": 1, "barrier": 1, "clear": 2})
        self.assertEqual((result["usage_count"], result["event_count"]), (7, 4))
        self.assertEqual(result["events"][0]["usage"], "Barrier")
        self.assertEqual(result["events"][0]["category"], "barrier")
        self.assertEqual(result["events"][0]["access"], "other")
        self.assertEqual(result["events"][0]["view_resource_id"], "ResourceId::201")
        result = self.analysis.trace_resource_usage(
            "86983", categories=["clear", "barrier", "clear"], event_id_range={"min": 20},
            before_event_id=31, limit=1)
        self.assertEqual(result["category_counts"], {
            "read": 0, "write": 0, "read_write": 0, "barrier": 1, "clear": 1})
        self.assertEqual(result["usage_counts"], {"Barrier": 1, "Discard": 1})
        self.assertEqual(result["latest_writer_before_event"]["event_id"], 30)
        self.assertEqual(result["total_count"], 2)
        self.assertTrue(result["has_more"])
        result = self.analysis.trace_resource_usage(
            "86983", categories=["read_write"], marker_filter="compute")
        self.assertEqual(result["events"][0]["usage"], "GenMips")
        self.assertEqual(result["events"][0]["category"], "read_write")
        self.assertEqual(result["events"][0]["access"], "write")  # dependency access classification
        result = self.analysis.trace_resource_usage("86983", categories=[])
        self.assertTrue(result["available"])
        self.assertEqual(result["total_count"], 0)
        self.assertEqual(sum(result["category_counts"].values()), 0)
        self.assertIsNone(result["latest_writer"])
        result = self.analysis.trace_resource_usage("86983", categories=["clear"], offset=100)
        self.assertEqual(result["events"], [])
        self.assertEqual(result["category_counts"]["clear"], 2)

    def test_invalid_timeline_categories_rejected_by_handler(self):
        for categories in ("clear", ["Clear"], ["other"], [None], [1], {}):
            response = self.handler.handle({
                "id": "invalid-category", "method": "trace_resource_usage",
                "params": {"resource_id": "86983", "categories": categories}})
            self.assertEqual(response["error"]["code"], -32602)
            self.assertIn("INVALID_USAGE_CATEGORIES", response["error"]["message"])

    def test_initialization_paths_hidden_fields_and_duplicate_names(self):
        root = self.service.get_resource_initialization("86983", 0)
        self.assertEqual(root["children"]["items"][1]["child_path"], [1])
        self.assertEqual(root["children"]["items"][0]["value"]["resource_id"], "ResourceId::190")
        result = self.service.get_resource_initialization("86983", 0, [1], 1, 1)
        node = result["children"]["items"][0]
        self.assertEqual(node["child_path"], [1, 2])
        self.assertEqual(node["display_value"], "A | B")
        self.assertEqual(node["value"], 3)
        second = self.service.get_resource_initialization("86983", 0, [1, 3])
        self.assertEqual(second["node"]["value"], 22)
        self.assertEqual(second["children"]["total_count"], 0)
        memory = self.service.get_resource_initialization("86983", 1)
        self.assertEqual(memory["children"]["items"][1]["value"], 98304)

    def test_structured_scalars_arrays_and_truncation_are_json_safe(self):
        self.controller.chunks[0] = Node("root", Basic.Chunk, children=[
            Node("null", Basic.Null), Node("blob", Basic.Buffer, byte_size=999999),
            Node("text", Basic.String, "x" * 5000), Node("signed", Basic.SignedInteger, -4),
            Node("nan", Basic.Float, float("nan")), Node("bool", Basic.Boolean, True),
            Node("array", Basic.Array, children=[Node("e", Basic.UnsignedInteger, i) for i in range(1000)]),
            Node("char", Basic.Character, "x"), Node("gpu", Basic.GPUAddress, 2 ** 63),
        ])
        result = self.service.get_resource_initialization("86983", 0)
        json.dumps(result, allow_nan=False)
        items = result["children"]["items"]
        self.assertIsNone(items[0]["value"])
        self.assertTrue(items[1]["content_omitted"])
        self.assertEqual(items[1]["byte_size"], 999999)
        self.assertEqual(len(items[2]["value"]), 4096)
        self.assertTrue(items[2]["value_truncated"])
        self.assertEqual(items[3]["value"], -4)
        self.assertTrue(items[5]["value"])
        page = self.service.get_resource_initialization("86983", 0, [6], offset=995, limit=5)
        self.assertEqual(page["children"]["total_count"], 1000)
        self.assertEqual(page["children"]["items"][0]["value"], 995)
        self.assertFalse(page["children"]["has_more"])

    def test_validation_and_route_error_codes(self):
        for method, params, code in [
            ("list_resources", {"resource_type": "nonsense"}, -32602),
            ("list_resources", {"sort_by": "size"}, -32602),
            ("list_resources", {"offset": -1}, -32602),
            ("list_resources", {"limit": 501}, -32602),
            ("inspect_resource", {"resource_id": "nope"}, -32602),
            ("inspect_resource", {"resource_id": "999"}, -32000),
            ("inspect_resource", {"resource_id": "190", "related_limit": True}, -32602),
            ("get_resource_initialization", {"resource_id": "86983", "chunk_index": 2}, -32602),
            ("get_resource_initialization", {"resource_id": "86983", "chunk_index": 0,
                                             "child_path": [9]}, -32602),
            ("get_resource_initialization", {"resource_id": "86983", "child_path": [1]}, -32602),
            ("get_resource_initialization", {"resource_id": "86983", "child_path": 0}, -32602),
            ("get_resource_initialization", {"resource_id": "86983", "chunk_index": True}, -32602),
        ]:
            with self.subTest(method=method, params=params):
                result = self.handler.handle({"id": 1, "method": method, "params": params})
                self.assertEqual(result["error"]["code"], code)
        self.loaded = False
        with self.assertRaisesRegex(ValueError, "CAPTURE_NOT_LOADED"):
            self.service.list_resources()

    def test_catalog_is_request_local_and_failures_are_not_silenced(self):
        self.controller.resources[0].name = "changed capture"
        self.assertEqual(self.service.inspect_resource("86983")["resource"]["name"], "changed capture")
        self.controller.GetResources = lambda: (_ for _ in ()).throw(RuntimeError("catalog failed"))
        with self.assertRaisesRegex(RuntimeError, "catalog failed"):
            self.service.list_resources()

    def test_mcp_functions_route_all_new_parameters(self):
        from mcp_server import server
        calls = []

        def call(method, params):
            calls.append((method, params))
            response = self.handler.handle(json.loads(json.dumps(
                {"id": "contract", "method": method, "params": params})))
            if "error" in response:
                raise AssertionError(response)
            return json.loads(json.dumps(response["result"], allow_nan=False))

        with patch.object(server.bridge, "call", call):
            self.assertEqual(server.list_resources(sort_by="resource_id", offset=1, limit=1)["returned_count"], 1)
            self.assertEqual(server.inspect_resource("86983", related_offset=2, related_limit=1)
                             ["related_resources"]["items"][0]["relationship"], "derived")
            self.assertEqual(server.get_resource_initialization("86983", 0, [1, 3])["node"]["value"], 22)
            result = server.trace_resource_usage("86983", event_id_range={"min": 20},
                                                 before_event_id=25, offset=1, limit=1)
            self.assertEqual(result["events"][0]["event_id"], 30)
            self.assertEqual(result["total_count"], 2)
        self.assertEqual(len(calls), 4)

    def test_tools_roundtrip_through_real_file_ipc(self):
        # Reuse the isolated IPC fixture; no running RenderDoc process is needed.
        from test_bridge import BridgeTests, CLIENT
        from mcp_server import server
        fixture = BridgeTests("test_concurrent_clients_are_serialized")
        fixture.setUp()
        try:
            fixture.server.handler = self.handler
            fixture.start_server()
            with patch.object(server, "bridge", CLIENT.RenderDocBridge()):
                self.assertEqual(server.list_resources(resource_type="device")["total_count"], 1)
                self.assertEqual(server.inspect_resource("86983")["metadata"]["byte_size"], 11040)
                self.assertEqual(server.get_resource_initialization("86983", 1, [1])["node"]["value"], 98304)
                self.assertEqual(server.trace_resource_usage("86983", offset=1, limit=1)
                                 ["events"][0]["event_id"], 20)
                usage = server.trace_resource_usage("86983", categories=["clear"], limit=1)
                self.assertEqual(usage["events"][0]["usage"], "Clear")
                self.assertEqual(usage["category_counts"]["clear"], 1)
                self.assertEqual(usage["total_count"], 1)
                self.assertEqual(server.trace_resource_usage("86983", categories=[])["events"], [])
                self.prepare_api_action()
                self.assertEqual(server.get_action_api_calls(action_event_id=343)["total_count"], 4)
                self.assertEqual(server.get_action_api_calls(action_event_id=343, api_event_id=343, child_path=[0])["node"]["value"], 29835)
                with self.assertRaises(CLIENT.RenderDocBridgeError):
                    server.get_resource_initialization("86983", 2)
        finally:
            fixture.tearDown()

    def prepare_api_action(self):
        self.controller.chunks = [
            Node("vkCmdBindPipeline", Basic.Chunk, children=[
                Node("pipeline", Basic.Resource, ResourceId(200))]),
            Node("vkCmdSetVertexInputEXT", Basic.Chunk, children=[
                Node("bindings", Basic.Array, children=[
                    Node("binding", children=[Node("stride", Basic.UnsignedInteger, 32)])])]),
            Node("vkCmdBindDescriptorSets", Basic.Chunk),
            Node("vkCmdDrawIndexed", Basic.Chunk, children=[
                Node("indexCount", Basic.UnsignedInteger, 29835),
                Node("instanceCount", Basic.UnsignedInteger, 1)]),
        ]
        action = NS(eventId=343, GetName=lambda _: "vkCmdDrawIndexed(29835, 1)",
                    events=[NS(eventId=340 + i, chunkIndex=i) for i in range(4)])
        self.ctx.GetAction = lambda eid: action if eid == 343 else None
        return action

    def test_action_details_schema_and_real_file_ipc(self):
        from test_bridge import BridgeTests, CLIENT
        from mcp_server import server

        tools = {tool.name: tool for tool in asyncio.run(server.mcp.list_tools())}
        self.assertEqual(len(tools), 37)
        batch_schema = tools["dump_draws"].parameters
        self.assertEqual(batch_schema["required"], ["action_event_ids"])
        self.assertEqual(set(batch_schema["properties"]), {
            "action_event_ids", "mesh_dir", "texture_dir", "export_meshes",
            "export_textures", "max_textures", "summary_path"})
        for old in ("get_draw_call_details", "get_draw_calls", "search_draws",
                    "inspect_event", "diff_events", "trace_event_dependencies"):
            self.assertNotIn(old, tools)
        for name in ("get_action_details", "inspect_action", "trace_action_dependencies",
                     "get_mesh_summary", "get_mesh_data", "export_mesh_csv"):
            properties = tools[name].parameters["properties"]
            self.assertIn("action_event_id", properties)
            self.assertNotIn("event_id", properties)
        self.assertIn("action_event_ids", tools["get_action_timings"].parameters["properties"])
        self.assertEqual(set(tools["get_actions"].parameters["properties"]), {
            "include_children", "marker_filter", "exclude_markers", "action_event_id_range",
            "exclude_marker_actions", "flags_filter"})
        self.assertEqual(set(tools["get_mesh_data"].parameters["properties"]), {
            "action_event_id", "stage", "offset", "limit", "attributes", "instance"})
        self.assertEqual(set(tools["trace_resource_usage"].parameters["properties"]), {
            "resource_id", "marker_filter", "exclude_markers", "event_id_range",
            "before_event_id", "offset", "limit", "categories"})
        self.assertIn("exclude_marker_actions", tools["get_actions"].parameters["properties"])
        self.assertIn("event_id", tools["get_shader_info"].parameters["properties"])
        self.assertIn("event_id_range", tools["trace_resource_usage"].parameters["properties"])
        self.assertIn("slice_index", tools["get_texture_data"].parameters["properties"])
        self.assertNotIn("slice", tools["get_texture_data"].parameters["properties"])
        self.assertIn("attributes", tools["export_mesh_csv"].parameters["properties"])
        self.assertNotIn("include_attributes", tools["export_mesh_csv"].parameters["properties"])
        schema = tools["get_action_details"].parameters
        self.assertEqual(schema["required"], ["action_event_id"])
        self.assertEqual(set(schema["properties"]), {"action_event_id"})

        action = self.prepare_api_action()
        action.actionId, action.flags = 12, 0
        action.numIndices, action.numInstances = 29835, 2
        action.baseVertex, action.vertexOffset = -2, 3
        action.instanceOffset, action.indexOffset = 4, 5
        action.outputs = [ResourceId(202), ResourceId.Null()]
        action.depthOut = ResourceId(203)
        selected = []
        self.controller.SetFrameEvent = lambda eid, force: selected.append(eid)

        fixture = BridgeTests("test_concurrent_clients_are_serialized")
        fixture.setUp()
        try:
            fixture.server.handler = self.handler
            fixture.start_server()
            with patch.object(server, "bridge", CLIENT.RenderDocBridge()):
                result = server.get_action_details(action_event_id=343)
                self.assertEqual(result, {
                    "action_event_id": 343, "action_id": 12,
                    "name": "vkCmdDrawIndexed(29835, 1)", "flags": [],
                    "num_indices": 29835, "num_instances": 2,
                    "base_vertex": -2, "vertex_offset": 3,
                    "instance_offset": 4, "index_offset": 5,
                    "outputs": [{"index": 0, "resource_id": "202"}],
                    "depth_output": "203",
                })
                # SetFrameEvent(target) then SetFrameEvent(restore): the query
                # must move replay to the action and restore the UI position.
                self.assertEqual(selected, [343, 1])
                self.loaded = False
                with self.assertRaisesRegex(CLIENT.RenderDocBridgeError, "CAPTURE_NOT_LOADED"):
                    server.get_action_details(action_event_id=343)
        finally:
            fixture.tearDown()

    def test_handler_uses_current_signatures_for_parameter_validation(self):
        for method, params, code in [
            ("unknown_tool", {}, -32601),
            ("get_action_details", {}, -32602),
            ("get_action_timings", {"unknown_argument": [343]}, -32602),
            ("get_actions", {"unknown_argument": True}, -32602),
        ]:
            with self.subTest(method=method, params=params):
                result = self.handler.handle({"id": 1, "method": method, "params": params})
                self.assertEqual(result["error"]["code"], code)
                if params:
                    self.assertIn("unexpected parameter(s)", result["error"]["message"])

    def test_action_tree_timings_and_summary_use_action_eids(self):
        from mcp_server import server

        rd = ACTION.rd
        flags = enum.IntFlag("ActionFlags", {name: 1 << i for i, name in enumerate(
            "Drawcall Dispatch Clear PushMarker PopMarker SetMarker Present Copy Resolve GenMips "
            "PassBoundary Indexed Instanced Auto Indirect ClearColor ClearDepthStencil BeginPass EndPass".split())})
        with patch.dict(sys.modules, {"renderdoc": rd}):
            serializers = load("action_serializers_under_test", "renderdoc_extension/utils/serializers.py")
        draw = NS(eventId=343, actionId=12, flags=flags.Drawcall, numIndices=3,
                  numInstances=1, children=[], GetName=lambda _: "Draw")
        root = NS(eventId=1, actionId=1, flags=flags.PushMarker, numIndices=0,
                  numInstances=0, children=[draw], GetName=lambda _: "Pass")
        self.controller.GetRootActions = lambda: [root]
        self.controller.GetAPIProperties = lambda: NS(pipelineType="Vulkan")
        self.controller.EnumerateCounters = lambda: [7]
        self.controller.DescribeCounter = lambda _: NS(unit="Seconds")
        self.controller.FetchCounters = lambda _: [NS(eventId=343, counter=7, value=NS(d=0.001))]

        def call(method, params=None):
            response = self.handler.handle({"id": 1, "method": method, "params": params or {}})
            self.assertNotIn("error", response)
            return response["result"]

        with patch.object(rd, "ActionFlags", flags), \
                patch.object(rd, "GPUCounter", NS(EventGPUDuration=7), create=True), \
                patch.object(ACTION, "Serializers", serializers.Serializers), \
                patch.object(ACTION, "Helpers", NS(count_children=lambda _: 1)), \
                patch.object(ANALYSIS, "Helpers", NS(get_all_shader_stages=lambda: [])), \
                patch.object(server.bridge, "call", call):
            result = server.get_actions(exclude_marker_actions=True,
                                        action_event_id_range={"min": 343, "max": 343})
            self.assertEqual(result["total_count"], 1)
            self.assertEqual(result["items"][0]["action_event_id"], 343)
            self.assertEqual(result["items"][0]["action_id"], 12)
            self.assertNotIn("event_id", result["items"][0])
            timing = server.get_action_timings(action_event_ids=[343])["timings"][0]
            self.assertEqual(timing["action_event_id"], 343)
            self.assertNotIn("event_id", timing)
            self.facade._analysis._action = self.facade._action
            summary = server.summarize_capture()
            self.assertEqual(summary["top_level_markers"][0]["action_event_id"], 1)
            self.assertEqual(summary["hot_actions"][0]["action_event_id"], 343)
            self.assertEqual(summary["suggested_entry_points"][-1]["action_event_id"], 343)
            self.controller.GetPipelineState = lambda: NS()
            self.ctx.GetAction = lambda eid: draw if eid == 343 else None
            self.controller.SetFrameEvent = lambda *args: None
            dependencies = server.trace_action_dependencies(action_event_id=343)
            self.assertEqual(dependencies["action_event_id"], 343)
            self.assertNotIn("event_id", dependencies)
            workload = server.analyze_pass(marker_filter="Pass")
            self.assertEqual(workload["action_event_id_range"], {"min": 343, "max": 343})
            self.assertEqual(workload["top_timed_actions"][0]["action_event_id"], 343)

    def test_mesh_read_and_export_share_action_eid_contract(self):
        from mcp_server import server

        packages = {"renderdoc": ACTION.rd}
        for name in ("renderdoc_extension", "renderdoc_extension.services"):
            packages[name] = types.ModuleType(name)
            packages[name].__path__ = []
        with patch.dict(sys.modules, packages):
            load("renderdoc_extension.services.replay_query",
                 "renderdoc_extension/services/replay_query.py")
            module = load("renderdoc_extension.services.mesh_service",
                          "renderdoc_extension/services/mesh_service.py")
        mesh = module.MeshService(self.ctx, self.invoke)
        self.facade._mesh = mesh
        action = NS(eventId=343, flags=3, numIndices=3)
        self.ctx.GetAction = lambda _: action
        self.controller.SetFrameEvent = lambda *args: None
        fmt = NS(Name=lambda: "R32G32B32_FLOAT", compCount=3, compByteWidth=4,
                 compType="Float", Special=lambda: False)
        attribute = NS(name="POSITION", format=fmt, topology="TriangleList",
                       vertexResourceId=ResourceId(86983), vertexByteOffset=0, vertexByteStride=12)
        mesh._get_mesh_inputs = lambda *_: [attribute]
        mesh._get_indices = lambda *_: [0, 1, 2]
        mesh._batch_get_buffer_data = lambda *_: {attribute.vertexResourceId: struct.pack(
            "<9f", 0, 0, 0, 1, 0, 0, 0, 1, 0)}
        mesh._unpack_vertex_data = lambda fmt, data, offset: struct.unpack_from("<3f", data, offset)

        def call(method, params):
            response = self.handler.handle({"id": 1, "method": method, "params": params})
            self.assertNotIn("error", response)
            return response["result"]

        with patch.object(ACTION.rd, "ActionFlags", NS(Drawcall=1, Indexed=2)), \
                patch.object(ACTION.rd, "CompType", NS(Float="Float"), create=True), \
                patch.object(server.bridge, "call", call), tempfile.TemporaryDirectory() as directory:
            summary = server.get_mesh_summary(action_event_id=343)
            self.assertEqual(summary["action_event_id"], 343)
            page = server.get_mesh_data(action_event_id=343, offset=1, limit=1)
            self.assertEqual(page["action_event_id"], 343)
            self.assertEqual(page["instance"], 0)
            self.assertEqual(page["items"], [{"POSITION": [1.0, 0.0, 0.0]}])
            self.assertNotIn("event_id", page)
            exported = server.export_mesh_csv(action_event_id=343,
                                               output_path=str(Path(directory) / "mesh.csv"),
                                               attributes=["POSITION"])
            self.assertEqual(exported["action_event_id"], 343)
            self.assertEqual(Path(exported["index_path"]).read_text().splitlines(), ["0", "1", "2"])

    def test_buffer_read_failures_propagate_and_validate(self):
        with self.assertRaisesRegex(ValueError, "INVALID_PAGINATION"):
            self.service.get_buffer_contents("86983", offset=-1)
        with self.assertRaisesRegex(ValueError, "INVALID_PAGINATION"):
            self.service.get_buffer_contents("86983", length=-1)

        def boom(rid, offset, length):
            raise RuntimeError("read failed")

        self.controller.GetBufferData = boom
        with self.assertRaisesRegex(ValueError, "RESOURCE_QUERY_FAILED"):
            self.service.get_buffer_contents("86983")

    def test_buffer_contents_match_numeric_ids(self):
        """Regression: ResourceId cannot be constructed from an int in the bindings."""
        payload = struct.pack("<4f", 1.0, 2.0, 3.0, 4.0)
        seen = {}
        # An opaque binding-owned ID: no integer constructor or writable .id.
        class OpaqueId:
            __slots__ = ()

            def __int__(self):
                return 86983

        rid = OpaqueId()
        self.controller.GetBuffers = lambda: [NS(resourceId=rid, length=11040)]

        def read(rid, offset, length):
            seen["rid"] = rid
            return payload[offset:offset + length]

        self.controller.GetBufferData = read
        data = self.service.get_buffer_contents("ResourceId::86983", 0, 8)

        self.assertEqual(int(seen["rid"]), 86983)
        self.assertIs(seen["rid"], rid)
        self.assertEqual(data["resource_id"], "ResourceId::86983")
        self.assertEqual(data["length"], 8)
        self.assertEqual(data["total_size"], 11040)
        self.assertFalse(data["truncated"])
        self.assertEqual(base64.b64decode(data["content_base64"]), payload[:8])

    def test_export_mesh_csv_rejects_attribute_less_export(self):
        """Post-VS attributes with a special format must fail, not export VTX/IDX only."""
        packages = {"renderdoc": ACTION.rd}
        for name in ("renderdoc_extension", "renderdoc_extension.services"):
            packages[name] = types.ModuleType(name)
            packages[name].__path__ = []
        with patch.dict(sys.modules, packages):
            load("renderdoc_extension.services.replay_query",
                 "renderdoc_extension/services/replay_query.py")
            module = load("renderdoc_extension.services.mesh_service",
                          "renderdoc_extension/services/mesh_service.py")
        mesh = module.MeshService(self.ctx, self.invoke)
        action = NS(eventId=343, flags=3, numIndices=3)
        self.ctx.GetAction = lambda _: action
        self.controller.SetFrameEvent = lambda *args: None
        fmt = NS(Name=lambda: "Undefined", compCount=4, Special=lambda: True)
        attribute = NS(name="_sig0", format=fmt, topology="TriangleList",
                       vertexResourceId=ResourceId(86983), vertexByteOffset=0,
                       vertexByteStride=16, numIndices=3,
                       indexResourceId=ResourceId(0), indexByteOffset=0,
                       indexByteStride=2, baseVertex=0)
        mesh._get_postvs_inputs = lambda *_: [attribute]

        with patch.object(ACTION.rd, "ActionFlags", NS(Drawcall=1, Indexed=2)), \
                patch.object(mesh, "_batch_get_buffer_data") as read, \
                patch("builtins.open") as write:
            with self.assertRaisesRegex(ValueError, "MESH_SIGNATURE_UNAVAILABLE"):
                mesh.export_mesh_csv(343, str(ROOT / "must-not-write.csv"), stage="VSOut")
            read.assert_not_called()
            write.assert_not_called()

    def test_action_details_rejects_an_intermediate_api_eid(self):
        action = self.prepare_api_action()
        # Some adapters may resolve an intermediate EID to its enclosing action.
        self.ctx.GetAction = lambda _: action
        with self.assertRaisesRegex(ValueError, "INVALID_ACTION_EVENT_ID"):
            self.facade.get_action_details(action_event_id=341)

    def test_api_inspector_list_pagination_and_parameter_expansion(self):
        self.prepare_api_action()
        service = self.facade._action
        calls = service.get_action_api_calls(343)
        self.assertEqual(calls["name"], "vkCmdDrawIndexed(29835, 1)")
        self.assertNotIn("action_name", calls)
        self.assertEqual([e["api_event_id"] for e in calls["items"]], [340, 341, 342, 343])
        self.assertEqual(calls["items"][0]["name"], "vkCmdBindPipeline")
        page = service.get_action_api_calls(343, offset=2, limit=1)
        self.assertEqual(page["items"][0]["api_event_id"], 342)
        self.assertTrue(page["has_more"])
        self.assertEqual(service.get_action_api_calls(343, 343)["children"]["items"][0]["value"], 29835)
        self.assertEqual(service.get_action_api_calls(343, 341, [0, 0, 0])["node"]["value"], 32)
        resource = service.get_action_api_calls(343, 340)["children"]["items"][0]["value"]
        self.assertEqual(resource["resource_id"], "ResourceId::200")
        self.assertEqual(resource["name"], "Shader 200")
        json.dumps(calls, allow_nan=False)
        # Controller has no SetFrameEvent: any replay-selection mutation would fail.

    def test_api_inspector_missing_chunks_empty_actions_and_ownership(self):
        action = self.prepare_api_action()
        service = self.facade._action
        action.events[0].chunkIndex = 0xFFFFFFFF
        action.events[1].chunkIndex = 999
        items = service.get_action_api_calls(343)["items"]
        self.assertEqual(items[0]["reason"], "no_chunk")
        self.assertEqual(items[1]["reason"], "invalid_chunk_index")
        expanded = service.get_action_api_calls(343, 340)
        self.assertFalse(expanded["api_call"]["available"])
        self.assertNotIn("node", expanded)
        for params in [
            {"action_event_id": 342}, {"action_event_id": 343, "api_event_id": 999},
            {"action_event_id": 343, "api_event_id": 343, "child_path": [9]},
            {"action_event_id": 343, "child_path": [0]}, {"action_event_id": 343, "limit": 0},
            {"action_event_id": True}, {"action_event_id": 343, "api_event_id": False},
        ]:
            with self.subTest(params=params):
                response = self.handler.handle({"id": 1, "method": "get_action_api_calls",
                                                "params": params})
                self.assertEqual(response["error"]["code"], -32602)
        action.events = []
        self.assertEqual(service.get_action_api_calls(343)["items"], [])
        self.loaded = False
        with self.assertRaisesRegex(ValueError, "CAPTURE_NOT_LOADED"):
            service.get_action_api_calls(343)


if __name__ == "__main__":
    unittest.main()
