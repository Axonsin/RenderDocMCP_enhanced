"""Adversarial regressions for bounded resource/mesh/search queries."""
import struct
from types import SimpleNamespace as NS
from unittest.mock import patch

import pytest
import test_shader_edit as shader_tests
import test_resources as resource_tests
import test_mesh as mesh_tests


def search_fixture(usages=None):
    ctx = shader_tests.Context()
    ctx.event = 99
    ctx.GetRootActions = lambda: [NS(eventId=e, flags=1, events=[],
                                    GetName=lambda _: "draw") for e in (1, 2, 3)]
    ctx.GetStructuredFile = lambda: None
    ctx.GetResources = lambda: [NS(resourceId=shader_tests.ResourceId(7), name="skin")]
    ctx.GetTextures = lambda: []
    ctx.GetBuffers = lambda: []
    ctx.GetResourceName = lambda rid: "skin"
    ctx.GetUsage = lambda rid: [NS(eventId=e) for e in (usages or [])]
    ctx.GetReadOnlyResources = lambda *_: [NS(descriptor=NS(resource=shader_tests.ResourceId(7)),
                                            access=NS(index=0))]
    ctx.GetReadWriteResources = lambda *_: []
    ctx.GetOutputTargets = lambda: []
    ctx.GetDepthTarget = lambda: NS(resource=shader_tests.ResourceId.Null())
    ctx.moves = []
    ctx.SetFrameEvent = lambda event, force: ctx.moves.append((event, force))
    return ctx, shader_tests.SEARCH.SearchService(ctx, ctx.invoke)


def test_empty_texture_usage_falls_back_and_range_precedes_replay():
    ctx, service = search_fixture()
    result = service.search_actions("texture", "skin", action_event_id_range={"min": 2, "max": 2})
    assert [m["action_event_id"] for m in result["matches"]] == [2]
    assert result["scan_mode"] == "pipeline"
    assert result["scanned_count"] == 1
    assert ctx.moves == [(2, True), (99, True)]


def test_usage_is_authoritative_without_pipeline_replay():
    ctx, service = search_fixture([1, 3])
    ctx.GetPipelineState = lambda: pytest.fail("usage path fetched pipeline state")
    result = service.search_actions("resource", "7")
    assert [m["action_event_id"] for m in result["matches"]] == [1, 3]
    assert result["scan_mode"] == "usage"
    assert ctx.moves == []


def test_usage_api_event_maps_to_owning_action():
    ctx, service = search_fixture([11])
    ctx.GetRootActions = lambda: [NS(eventId=12, flags=1, events=[NS(eventId=11)],
                                    GetName=lambda _: "draw")]
    assert service.search_actions("resource", "7")["matches"][0]["action_event_id"] == 12


def test_resume_is_inclusive_and_counts_processed_actions():
    ctx, service = search_fixture([1, 2, 3])
    first = service.search_actions("resource", "7", max_matches=1)
    assert first["stopped_reason"] == "max_matches"
    assert first["next_event_id"] == 2
    assert first["scanned_count"] == 1
    second = service.search_actions("resource", "7", start_event_id=first["next_event_id"])
    assert [m["action_event_id"] for m in second["matches"]] == [2, 3]
    assert second["complete"]
    assert second["next_event_id"] is None


def test_budget_includes_preparation_and_preserves_unprocessed_cursor():
    ctx, service = search_fixture([1])
    clock = [0.0]
    def usage(rid):
        clock[0] = 1.0
        return [NS(eventId=1)]
    ctx.GetUsage = usage
    with patch.object(shader_tests.SEARCH.time, "monotonic", lambda: clock[0]):
        result = service.search_actions("resource", "7", time_budget_ms=1)
    assert result["stopped_reason"] == "time_budget"
    assert result["next_event_id"] == 1
    assert result["scanned_count"] == 0
    assert ctx.moves == []


def test_match_cap_precedes_budget_when_both_reached():
    ctx, service = search_fixture()
    clock = [0.0]
    def pipe():
        clock[0] = 1.0
        return ctx
    ctx.GetPipelineState = pipe
    with patch.object(shader_tests.SEARCH.time, "monotonic", lambda: clock[0]):
        result = service.search_actions("texture", "skin", max_matches=1, time_budget_ms=1)
    assert result["stopped_reason"] == "max_matches"
    assert result["next_event_id"] == 2
    assert ctx.moves[-1] == (99, True)


def test_shader_entrypoint_still_matches_when_other_name_matches():
    ctx, service = search_fixture()
    ctx.GetResourceName = lambda rid: "main"
    ctx.GetShader = lambda stage: shader_tests.ResourceId(8)
    result = service.search_actions("shader", "main")
    assert len(result["matches"]) == 3


def test_no_texture_name_match_does_no_replay():
    ctx, service = search_fixture()
    assert service.search_actions("texture", "missing")["matches"] == []
    assert ctx.moves == []


def test_scan_failure_and_restore_failure_are_reported():
    ctx, service = search_fixture()
    def fail(event, force):
        raise RuntimeError("replay failed")
    ctx.SetFrameEvent = fail
    with pytest.raises(RuntimeError, match="^REPLAY_RESTORE_FAILED:.*RESOURCE_QUERY_FAILED"):
        service.search_actions("texture", "skin")


@pytest.mark.parametrize("options", [
    {"time_budget_ms": "1"}, {"max_matches": True}, {"start_event_id": 0},
    {"action_event_id_range": {}}, {"action_event_id_range": {"min": 2, "max": 1}},
])
def test_invalid_search_options_fail_before_replay(options):
    ctx, service = search_fixture()
    with pytest.raises(ValueError, match="^INVALID_"):
        service.search_actions("resource", "7", **options)
    assert ctx.moves == []


def buffer_fixture(size):
    rid = resource_tests.ResourceId(7)
    controller = NS(GetBuffers=lambda: [NS(resourceId=rid, length=size)])
    ctx = NS(IsCaptureLoaded=lambda: True)
    return controller, resource_tests.RESOURCE.ResourceService(ctx, lambda cb: cb(controller))


@pytest.mark.parametrize("size,offset", [(0, 0), (16, 16)])
def test_empty_buffer_read_never_passes_zero_length_to_renderdoc(size, offset):
    controller, service = buffer_fixture(size)
    controller.GetBufferData = lambda *_: pytest.fail("len=0 reads to end in RenderDoc")
    result = service.get_buffer_contents("7", offset)
    assert result["length"] == 0
    assert result["next_offset"] is None


def test_buffer_cap_clamp_and_unknown_size():
    controller, service = buffer_fixture(300000)
    calls = []
    def read(rid, offset, length):
        calls.append((offset, length))
        return b"x" * length
    controller.GetBufferData = read
    result = service.get_buffer_contents("7")
    assert calls == [(0, 262144)]
    assert result["truncated"] and result["next_offset"] == 262144
    result = service.get_buffer_contents("7", 299999, 100)
    assert result["length"] == 1 and result["next_offset"] is None
    with pytest.raises(ValueError, match="^INVALID_PAGINATION"):
        service.get_buffer_contents("7", 300001)
    controller.GetBuffers = lambda: [NS(resourceId=resource_tests.ResourceId(7))]
    with pytest.raises(ValueError, match="^RESOURCE_QUERY_FAILED"):
        service.get_buffer_contents("7")


def test_resource_description_has_no_size_and_texture_is_not_buffer():
    controller, service = buffer_fixture(0)
    controller.GetBuffers = lambda: []
    controller.GetResources = lambda: [NS(resourceId=resource_tests.ResourceId(7),
                                         type="Buffer", name="buffer")]
    with pytest.raises(ValueError, match="^RESOURCE_QUERY_FAILED"):
        service.get_buffer_contents("7")
    controller.GetResources = lambda: [NS(resourceId=resource_tests.ResourceId(7),
                                         type="Texture", byteSize=16)]
    with pytest.raises(ValueError, match="^BUFFER_NOT_FOUND"):
        service.get_buffer_contents("7")


def test_postvs_format_explicitly_becomes_regular():
    controller = mesh_tests.Controller()
    ctx = mesh_tests.Context(controller)
    service = mesh_tests.MESH.MeshService(ctx, ctx.invoke)
    controller.postvs = mesh_tests.postvs_mesh(stride=16)
    controller.reflections = {mesh_tests.ShaderStage.Vertex:
                             NS(outputSignature=[mesh_tests.sig("POSITION", 0, 4)])}
    class DefaultUndefined(mesh_tests.ResourceFormat):
        def __init__(self):
            super().__init__()
            self.type = mesh_tests.ResourceFormatType.Undefined
    with patch.object(mesh_tests.MESH.rd, "ResourceFormat", DefaultUndefined):
        attrs = service._get_postvs_inputs(controller, ctx.action, "VSOut", 0)
    assert not attrs[0].format.Special()


def test_unreadable_indices_do_not_fabricate_geometry():
    controller = mesh_tests.Controller()
    ctx = mesh_tests.Context(controller)
    service = mesh_tests.MESH.MeshService(ctx, ctx.invoke)
    result = service.get_mesh_summary(343)
    assert result["num_vertices"] == 3  # preserve the existing count contract
    assert result["unique_vertex_count"] is None
    assert not result["indices_available"]
    assert result["bounding_box"] is None
    assert controller.events == [343, 99]


def test_bounds_skip_special_nonfinite_and_out_of_range_data():
    controller = mesh_tests.Controller()
    service = mesh_tests.MESH.MeshService(NS(), lambda cb: cb(controller))
    fmt = mesh_tests.ResourceFormat()
    fmt.compCount = 3
    attr = NS(name="POSITION", format=fmt, vertexResourceId=mesh_tests.ResourceId(1),
              vertexByteOffset=0, vertexByteStride=12, instanced=False)
    controller.buffers[1] = struct.pack("<6f", 2, 3, 4, float("nan"), 0, 0)
    boxes, name, basis = service._attribute_bounding_boxes(controller, [attr], [0, 1, 999])
    assert boxes["POSITION"] == {"min": [2, 3, 4], "max": [2, 3, 4]}
    assert name == "POSITION" and basis == "semantic"
    fmt.type = mesh_tests.ResourceFormatType.Undefined
    assert service._attribute_bounding_boxes(controller, [attr], [0])[0] == {}


def test_partial_usage_failure_falls_back_without_dropping_resources():
    ctx, service = search_fixture()
    ctx.GetResources = lambda: [NS(resourceId=shader_tests.ResourceId(r)) for r in (7, 8)]
    def usage(rid):
        if int(rid) == 8:
            raise RuntimeError("usage unavailable")
        return [NS(eventId=1)]
    ctx.GetUsage = usage
    result = service.search_actions("texture", "skin")
    assert result["scan_mode"] == "pipeline"
    assert [m["action_event_id"] for m in result["matches"]] == [1, 2, 3]


def test_mesh_unique_count_is_additive_and_topology_is_from_pipeline():
    controller = mesh_tests.Controller()
    ctx = mesh_tests.Context(controller)
    service = mesh_tests.MESH.MeshService(ctx, ctx.invoke)
    fmt = mesh_tests.ResourceFormat()
    fmt.compCount = 3
    attr = NS(name="POSITION", format=fmt, vertexResourceId=mesh_tests.ResourceId(1),
              vertexByteOffset=0, vertexByteStride=12, instanced=False,
              indexResourceId=mesh_tests.ResourceId(2), topology="Unknown")
    service._get_mesh_inputs = lambda *_: [attr]
    service._get_indices = lambda *_: [0, 1, 1]
    controller.GetPipelineState = lambda: NS(GetPrimitiveTopology=lambda: "TriangleList")
    controller.buffers[1] = struct.pack("<6f", 2, 3, 4, 5, 6, 7)
    result = service.get_mesh_summary(343)
    assert result["num_vertices"] == 3
    assert result["unique_vertex_count"] == 2
    assert result["indices_available"]
    assert result["topology"] == "TriangleList"
    assert result["topology_source"] == "pipeline"
    assert result["bounding_box"] == {"min": [2, 3, 4], "max": [5, 6, 7]}


def test_nonindexed_vsout_and_dotted_export_names():
    from unittest.mock import mock_open
    controller = mesh_tests.Controller()
    ctx = mesh_tests.Context(controller)
    ctx.action.flags = mesh_tests.ActionFlags.Drawcall
    service = mesh_tests.MESH.MeshService(ctx, ctx.invoke)
    controller.postvs = mesh_tests.postvs_mesh(stride=16)
    controller.reflections = {mesh_tests.ShaderStage.Vertex:
                             NS(outputSignature=[mesh_tests.sig("output.position", 0, 4)])}
    controller.buffers[7] = struct.pack("<12f", *range(12))
    result = service.get_mesh_data(343, stage="VSOut")
    assert result["items"][1]["output.position"] == [4, 5, 6, 7]
    with patch("builtins.open", mock_open()):
        exported = service.export_mesh_csv(343, "review.csv", stage="VSOut")
    assert exported["vertex_count"] == 3
    assert exported["exported_attributes"] == ["output.position"]
    assert exported["skipped_attributes"] == []
    assert controller.events[-1] == 99
