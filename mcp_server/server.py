"""
RenderDoc MCP Server
FastMCP server providing access to RenderDoc capture data.
"""

from typing import Literal

from fastmcp import FastMCP

from .bridge.client import RenderDocBridge, RenderDocBridgeError

# Initialize FastMCP server
mcp = FastMCP(
    name="RenderDoc MCP Server",
    version="3.0.0",
)

# RenderDoc bridge client
bridge = RenderDocBridge()


def _optional_param(params: dict[str, object], name: str, value: object | None) -> None:
    """Add an optional bridge parameter when present."""
    if value is not None:
        params[name] = value


@mcp.tool
def get_capture_status(probe_replay: bool = True) -> dict:
    """
    Check if a capture is currently loaded in RenderDoc.
    Returns the capture status, API type, extension/renderdoc/IPC versions,
    and replay health (replay_healthy/replay_error) when loaded.
    """
    return bridge.call("get_capture_status", {"probe_replay": probe_replay})


@mcp.tool
def get_actions(
    include_children: bool = True,
    marker_filter: str | None = None,
    exclude_markers: list[str] | None = None,
    action_event_id_range: dict[str, int] | None = None,
    exclude_marker_actions: bool = False,
    flags_filter: list[str] | None = None,
) -> dict:
    """
    Get the action tree, including draws, dispatches, copies, clears and markers.

    Args:
        include_children: Include child actions in the hierarchy (default: True)
        marker_filter: Only include actions under markers containing this string (partial match)
        exclude_markers: Exclude actions under markers containing these strings (list of partial matches)
        action_event_id_range: Optional action_event_id range as {"min": ..., "max": ...}
        exclude_marker_actions: If True, exclude marker actions (PushMarker/PopMarker/SetMarker)
        flags_filter: Only include actions with these flags (list of flag names, e.g. ["Drawcall", "Dispatch"])

    Returns a hierarchical tree of actions including markers, draw calls,
    dispatches, and other GPU events.
    """
    params: dict[str, object] = {"include_children": include_children}
    _optional_param(params, "marker_filter", marker_filter)
    _optional_param(params, "exclude_markers", exclude_markers)
    _optional_param(params, "action_event_id_range", action_event_id_range)
    if exclude_marker_actions:
        params["exclude_marker_actions"] = exclude_marker_actions
    _optional_param(params, "flags_filter", flags_filter)
    return bridge.call("get_actions", params)


@mcp.tool
def get_frame_summary() -> dict:
    """
    Get a summary of the current capture frame.

    Returns statistics about the frame including:
    - API type (D3D11, D3D12, Vulkan, etc.)
    - Total action count
    - Statistics: draw calls, dispatches, clears, copies, presents, markers
    - Top-level markers with event IDs and child counts
    - Resource counts: textures, buffers
    """
    return bridge.call("get_frame_summary")


@mcp.tool
def inspect_action(action_event_id: int) -> dict:
    """
    Inspect one action using a compact analysis-oriented bundle.

    Args:
        action_event_id: The exact action EID to inspect

    Returns event details, timing, shader summaries, pipeline summaries,
    and mesh summary when the event is a draw call.
    """
    return bridge.call("inspect_action", {"action_event_id": action_event_id})


@mcp.tool
def summarize_capture() -> dict:
    """
    Summarize the loaded capture at a high level.

    Returns frame statistics, hot actions, major markers, and suggested
    entry points for deeper investigation.
    """
    return bridge.call("summarize_capture")


@mcp.tool
def search_actions(
    by: Literal["shader", "texture", "resource"],
    query: str,
    stage: str | None = None,
    action_event_id_range: dict[str, int] | None = None,
    time_budget_ms: int | None = None,
    max_matches: int | None = None,
    start_event_id: int | None = None,
) -> dict:
    """
    Search draw and dispatch actions by shader, texture or resource.

    Args:
        by: Search mode - shader, texture, or resource
        query: Shader name, texture name, or resource ID query
        stage: Optional shader stage filter; uses the same canonical names/aliases as Pipeline State
        action_event_id_range: Optional {"min": ..., "max": ...} action EID range
        time_budget_ms: Optional scan budget (default 8000). On expiry the scan
            stops and returns complete=false plus next_event_id instead of hanging.
        max_matches: Optional match cap (default 200)
        start_event_id: Resume cursor from a previous truncated result

    Returns a search result with matches, total_matches, scanned_count,
    complete/stopped_reason/next_event_id, scan_mode ("usage" or "pipeline")
    and elapsed_ms. Texture/resource searches use the Timeline usage index and
    only fall back to a pipeline scan when no usage is recorded.
    """
    params: dict[str, object] = {"by": by, "query": query}
    _optional_param(params, "stage", stage)
    _optional_param(params, "action_event_id_range", action_event_id_range)
    _optional_param(params, "time_budget_ms", time_budget_ms)
    _optional_param(params, "max_matches", max_matches)
    _optional_param(params, "start_event_id", start_event_id)
    return bridge.call("search_actions", params)


@mcp.tool
def get_action_api_calls(
    action_event_id: int, api_event_id: int | None = None,
    child_path: list[int] | None = None, offset: int = 0, limit: int = 50,
) -> dict:
    """Read an action's associated API calls, like API Inspector.

    action_event_id must identify an action. Omit api_event_id to list its API events
    in capture order with EID, API name, chunk index and parameter availability.
    Follow has_more/offset to retrieve all calls. These are ActionDescription.events,
    not all historical calls that contributed to the current pipeline state.

    Pass an item's api_event_id to inspect its root parameters. Reuse
    returned child_path indices to expand a structure/array one level at a time.
    offset/limit paginate the call list or the selected node's visible children.
    limit is 1..500. Resource parameters include IDs/names; binary contents are
    omitted and text previews are bounded. Missing chunks report an explicit
    unavailable reason. This query does not change the selected event.
    """
    return bridge.call("get_action_api_calls", {
        "action_event_id": action_event_id, "api_event_id": api_event_id,
        "child_path": child_path, "offset": offset, "limit": limit,
    })


@mcp.tool
def get_action_details(action_event_id: int) -> dict:
    """Get an action's metadata, draw counts, offsets and output resources.

    action_event_id identifies the action to inspect and is also returned.
    action_id is the separate action ordinal. Use get_action_api_calls for
    associated API calls and their parameter trees.
    """
    return bridge.call("get_action_details", {"action_event_id": action_event_id})


@mcp.tool
def get_action_timings(
    action_event_ids: list[int] | None = None,
    marker_filter: str | None = None,
    exclude_markers: list[str] | None = None,
) -> dict:
    """
    Get GPU timing information for actions (draw calls, dispatches, etc.).

    Args:
        action_event_ids: Optional list of specific event IDs to get timings for.
                   If not specified, returns timings for all actions.
        marker_filter: Only include actions under markers containing this string (partial match).
        exclude_markers: Exclude actions under markers containing these strings.

    Returns timing data including:
    - available: Whether GPU timing counters are supported
    - unit: Time unit (typically "seconds")
    - timings: List of {action_event_id, name, duration_seconds, duration_ms}
    - total_duration_ms: Sum of all durations
    - count: Number of timing entries

    Note: GPU timing counters may not be available on all hardware/drivers.
    """
    params: dict[str, object] = {}
    if action_event_ids is not None:
        params["action_event_ids"] = action_event_ids
    if marker_filter is not None:
        params["marker_filter"] = marker_filter
    if exclude_markers is not None:
        params["exclude_markers"] = exclude_markers
    return bridge.call("get_action_timings", params)


@mcp.tool
def get_shader_info(
    event_id: int,
    stage: str,
) -> dict:
    """
    Get shader information for a specific stage at a given event.

    Args:
        event_id: The event ID to inspect the shader at
        stage: Canonical shader stage (vertex, tess_control, tess_eval, geometry, fragment,
            compute, task, mesh); aliases such as VS/HS/DS/PS/FS/pixel are accepted

    Returns shader identity, entry point and disassembly. Use get_pipeline_stage
    and inspect_pipeline_binding for bindings and constant values.
    """
    return bridge.call("get_shader_info", {"event_id": event_id, "stage": stage})


@mcp.tool
def get_shader_source(
    event_id: int,
    stage: str,
) -> dict:
    """
    Get original shader source text for a specific stage at a given event.

    Args:
        event_id: The event ID to inspect the shader at
        stage: Canonical shader stage (vertex, tess_control, tess_eval, geometry, fragment,
            compute, task, mesh); aliases such as VS/HS/DS/PS/FS/pixel are accepted

    Returns source_text for text-backed shader encodings and metadata-only
    responses when the capture only contains binary shader payloads.
    """
    return bridge.call("get_shader_source", {"event_id": event_id, "stage": stage})


@mcp.tool
def get_shader_edit_context(
    event_id: int,
    stage: str,
    mode: Literal["auto", "original", "glsl", "spirv_asm"] = "auto",
) -> dict:
    """Prepare editable GLSL/SPIR-V text and its compilation path for an event/stage.

    stage uses the same canonical shader names and aliases as get_pipeline_stage.

    Auto prefers original GLSL, otherwise decompiled GLSL with an assembly fallback.
    Returns edit_id, source_text, compiler, entry points, logs and replacement state.
    Reuse edit_id for replace/revert/export. IDs expire when the capture closes.
    A replacement affects ALL draws using the original shader resource.
    HLSL/DXBC/DXIL editing is TODO. No capture file is modified.
    """
    return bridge.call("get_shader_edit_context", {"event_id": event_id, "stage": stage, "mode": mode})


@mcp.tool
def replace_shader(edit_id: str, source_text: str) -> dict:
    """Compile text and replace a shader in the current capture session.

    Check last_attempt_status='applied' and the compiler log; compilation failures
    keep the last successful replacement. Inspect/save output textures to verify
    the visual result. A timeout is an UNKNOWN result: query
    list_shader_replacements/get_shader_edit_context before deciding what to do;
    never automatically retry a timed-out replacement.
    """
    return bridge.call("replace_shader", {"edit_id": edit_id, "source_text": source_text})


@mcp.tool
def revert_shader(edit_id: str) -> dict:
    """Restore the original shader, release the replacement and refresh the UI.

    Reverting twice is safe. Does not overwrite changes owned by other editors.
    """
    return bridge.call("revert_shader", {"edit_id": edit_id})


@mcp.tool
def list_shader_replacements() -> dict:
    """List active MCP shader replacements and all edit-session attempt states.

    items contains active replacements; sessions also contains prepared, failed,
    reverted or conflicting edits. Use this to resolve a timed-out operation.
    """
    return bridge.call("list_shader_replacements")


@mcp.tool
def export_shader_source(edit_id: str, output_path: str) -> dict:
    """Export latest submitted text (or initial text) as UTF-8 to an absolute path.

    Refuses existing files. Failed submissions can be exported; check
    last_attempt_status and matches_applied_source in the result.
    """
    return bridge.call("export_shader_source", {"edit_id": edit_id, "output_path": output_path})


@mcp.tool
def get_buffer_contents(
    resource_id: str,
    offset: int = 0,
    length: int = 0,
    action_event_id: int | None = None,
) -> dict:
    """
    Read the contents of a buffer resource.

    Args:
        resource_id: The resource ID of the buffer to read
        offset: Byte offset to start reading from (default: 0)
        length: Number of bytes to read, 0 for entire buffer (default: 0)

    Returns buffer data as base64-encoded bytes along with metadata.
    """
    return bridge.call(
        "get_buffer_contents",
        {"resource_id": resource_id, "offset": offset, "length": length, "action_event_id": action_event_id},
    )


@mcp.tool
def list_resources(
    resource_type: str = "all",
    name_filter: str | None = None,
    offset: int = 0,
    limit: int = 50,
    sort_by: Literal["name", "resource_id"] = "name",
) -> dict:
    """
    List all capture API objects, matching the Resource Inspector resource list.

    Args:
        resource_type: all, or a snake_case RenderDoc ResourceType such as texture,
            buffer, device, memory, shader, view, pipeline_state, command_buffer,
            swapchain_image, descriptor_store, or acceleration_structure.
        name_filter: Optional partial name match (case-insensitive)
        offset: Starting index for pagination (default: 0)
        limit: Maximum number of resources to return (default: 50)
        sort_by: Stable name or numeric resource_id order.

    Returns compact resource_id/name/resource_type identities and pagination.
    Use inspect_resource for metadata and related resources.
    """
    params: dict[str, object] = {
        "resource_type": resource_type,
        "offset": offset,
        "limit": limit,
        "sort_by": sort_by,
    }
    _optional_param(params, "name_filter", name_filter)
    return bridge.call("list_resources", params)


@mcp.tool
def inspect_resource(
    resource_id: str, related_offset: int = 0, related_limit: int = 50,
) -> dict:
    """Inspect one API object: metadata, parent/derived resources, usage counts,
    and the first 20 initialization calls. Related resources are paginated.
    Use trace_resource_usage for events and get_resource_initialization for
    call-directory pagination and parameter expansion. Unavailable sections
    carry an explicit reason; no event selection is changed.
    """
    return bridge.call("inspect_resource", {
        "resource_id": resource_id, "related_offset": related_offset,
        "related_limit": related_limit,
    })


@mcp.tool
def get_resource_initialization(
    resource_id: str, chunk_index: int | None = None,
    child_path: list[int] | None = None, offset: int = 0, limit: int = 50,
) -> dict:
    """List initialization calls, or expand a selected call's parameter tree.

    Omit chunk_index for the paginated call directory. Otherwise pass a returned
    chunk_index and child_path (raw child indices, default root []) to retrieve
    that node and one page of visible immediate children. Reuse returned paths
    to expand structures/arrays. Binary contents are omitted; text previews are
    limited to 4096 characters with explicit truncation. limit must be 1..500.
    """
    return bridge.call("get_resource_initialization", {
        "resource_id": resource_id, "chunk_index": chunk_index,
        "child_path": child_path, "offset": offset, "limit": limit,
    })


@mcp.tool
def get_texture_info(resource_id: str) -> dict:
    """
    Get metadata about a texture resource.

    Args:
        resource_id: The resource ID of the texture

    Includes dimensions, format, mip levels, and other properties.
    """
    return bridge.call("get_texture_info", {"resource_id": resource_id})


@mcp.tool
def get_texture_data(
    resource_id: str,
    mip: int = 0,
    slice_index: int = 0,
    sample: int = 0,
    depth_slice: int | None = None,
    action_event_id: int | None = None,
    output_mode: Literal["auto", "inline", "file"] = "auto",
    output_dir: str | None = None,
    aspect: Literal["all", "depth", "stencil"] = "all",
    region: dict[str, int] | None = None,
) -> dict:
    """
    Read texture pixels after action_event_id (or the current UI event if omitted).

    Args:
        resource_id: The resource ID of the texture to read
        mip: Mip level to retrieve (default: 0)
        slice_index: Array slice or cube face index (default: 0)
               For cube maps: 0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-
        sample: MSAA sample index (default: 0)
        depth_slice: For 3D textures only, extract a specific depth slice (default: None = full volume)
                     When specified, returns only the 2D slice at that depth index

    Auto returns <=256 KiB inline, otherwise a hashed binary file and sidecar.
    D16/D24S8 depth/stencil and verified ROI selection are numeric, never PNG.
    Returns raw texture pixel data along with metadata
    including dimensions at the requested mip level and format information.
    """
    params = {"resource_id": resource_id, "mip": mip, "slice_index": slice_index, "sample": sample,
              "action_event_id": action_event_id, "output_mode": output_mode, "output_dir": output_dir,
              "aspect": aspect, "region": region}
    if depth_slice is not None:
        params["depth_slice"] = depth_slice
    return bridge.call("get_texture_data", params)


@mcp.tool
def save_texture(
    resource_id: str,
    output_path: str,
    format_type: Literal["PNG", "JPG", "BMP", "TGA", "EXR", "DDS", "HDR"] = "PNG",
    mip: int = 0,
    slice_index: int = 0,
    alpha_mode: Literal["preserve", "discard", "blend_to_black"] = "preserve",
    action_event_id: int | None = None,
) -> dict:
    """
    Save a texture after action_event_id (or the current UI event if omitted).

    Args:
        resource_id: The resource ID of the texture to save (e.g. "ResourceId::2495")
        output_path: Output file path (e.g. "D:/output/texture.png")
        format_type: Output format - PNG (default), JPG, BMP, TGA, EXR, DDS, HDR
        mip: Mip level to save, -1 for all mips (default: 0)
        slice_index: Array slice or cube face index (default: 0)
                     For cube maps: 0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-
        alpha_mode: Alpha channel handling (default: preserve)
                    - preserve: Keep alpha channel
                    - discard: Remove alpha channel
                    - blend_to_black: Blend alpha with black background

    Returns success status and texture info including dimensions and output path.
    This is the recommended way to save textures as it handles format conversion automatically.
    """
    return bridge.call(
        "save_texture",
        {
            "resource_id": resource_id,
            "output_path": output_path,
            "format_type": format_type,
            "mip": mip,
            "slice_index": slice_index,
            "alpha_mode": alpha_mode,
            "action_event_id": action_event_id,
        },
    )


@mcp.tool
def get_pipeline_state(action_event_id: int) -> dict:
    """Get a compact Pipeline State overview for an exact action event.

    Returns API, pipeline kind, stage status, section availability, binding counts
    and diagnostics. Use get_pipeline_stage for rows and get_action_textures for
    the Texture Viewer input/output list. Queries restore the UI replay event.
    """
    return bridge.call("get_pipeline_state", {"action_event_id": action_event_id})


@mcp.tool
def get_pipeline_stage(
    action_event_id: int, stage: str, section: str = "overview",
    show_unused: bool = False, show_empty: bool = False, offset: int = 0, limit: int = 50,
) -> dict:
    """Inspect one Pipeline State stage; overview lists available sections.

    Stages: vertex_input, vertex, tess_control, tess_eval, geometry, task, mesh,
    rasterizer, fragment, framebuffer, compute. VS/FS/PS/CS/FB/OM aliases work.
    Shader sections: shader, descriptors, resources, samplers, constant_buffers,
    push_constants. Other sections are advertised by overview. List limit 1..500.
    Missing required bindings remain visible regardless of the empty/unused filters.
    """
    return bridge.call("get_pipeline_stage", dict(
        action_event_id=action_event_id, stage=stage, section=section,
        show_unused=show_unused, show_empty=show_empty, offset=offset, limit=limit))


@mcp.tool
def inspect_pipeline_binding(
    action_event_id: int, binding_id: str, section: Literal["details", "variables"] = "details",
    child_path: list[int] | None = None, offset: int = 0, limit: int = 50,
) -> dict:
    """Inspect a returned binding_id in the same capture and action.

    details returns resource identities, effective view/buffer ranges and issues.
    variables decodes one constant binding and expands one level at child_path;
    use returned child_path values to expand further (limit 1..500). IDs become
    invalid after capture reload or binding changes. Resource IDs link to Resource
    Inspector tools; binding IDs preserve stage, array element and range context.
    """
    return bridge.call("inspect_pipeline_binding", dict(
        action_event_id=action_event_id, binding_id=binding_id, section=section,
        child_path=child_path, offset=offset, limit=limit))


@mcp.tool
def get_action_textures(
    action_event_id: int, direction: Literal["all", "input", "output"] = "all",
    stage: str | None = None, show_unused: bool = False, show_empty: bool = False,
    offset: int = 0, limit: int = 50,
) -> dict:
    """List action texture bindings as a Texture Viewer view (no pixel preview).

    Each row has stage label, shader binding name, capture resource identity,
    roles and view subresources. Repeated resource bindings are preserved.
    Read-write images match both input/output filters but occur once in all.
    Supports draw/dispatch and copy/resolve/clear targets. Binding/use information
    does not prove dynamic GPU access. Use resource.resource_id with texture and
    Resource Inspector tools; pass action_event_id explicitly to pixel/export calls.
    """
    return bridge.call("get_action_textures", dict(
        action_event_id=action_event_id, direction=direction, stage=stage,
        show_unused=show_unused, show_empty=show_empty, offset=offset, limit=limit))


@mcp.tool
def trace_resource_usage(
    resource_id: str,
    marker_filter: str | None = None,
    exclude_markers: list[str] | None = None,
    event_id_range: dict[str, int] | None = None,
    before_event_id: int | None = None,
    offset: int = 0,
    limit: int = 100,
    categories: list[Literal["read", "write", "read_write", "barrier", "clear"]] | None = None,
) -> dict:
    """
    Trace how a resource is read, written, and consumed across matching events.

    Args:
        resource_id: The resource to trace
        marker_filter: Optional marker-path substring filter
        exclude_markers: Optional marker substrings to exclude
        event_id_range: Optional event range as {"min": ..., "max": ...}
        before_event_id: Optional event ID used to compute the latest prior writer
        offset: First usage record to return after filtering.
        limit: Page size, from 1 to 500 (default 100).
        categories: Optional Timeline categories, combined with OR. None selects all;
            [] selects none. Other event/marker filters are combined with AND.

    Returns raw usage, Timeline category, and inferred access per record.
    category_counts contains all five categories, including zeros. GenMips/Copy/Resolve
    are read_write; Discard/Clear are clear, matching the RenderDoc Timeline.
    Counts and writer summaries cover records matching ALL filters before pagination.
    Counts are usage records, not distinct EIDs or merged visual timeline markers.
    Inferred access/read_count/write_count remain independent from Timeline categories.
    Non-texture/buffer objects report unavailable usage rather than a missing ID.
    """
    params: dict[str, object] = {"resource_id": resource_id, "offset": offset, "limit": limit}
    _optional_param(params, "marker_filter", marker_filter)
    _optional_param(params, "exclude_markers", exclude_markers)
    _optional_param(params, "categories", categories)
    _optional_param(params, "event_id_range", event_id_range)
    _optional_param(params, "before_event_id", before_event_id)
    return bridge.call("trace_resource_usage", params)


@mcp.tool
def trace_action_dependencies(action_event_id: int) -> dict:
    """
    Trace the immediate resource dependencies of one action.

    Args:
        action_event_id: The exact action EID to inspect

    Returns stage-grouped input resources, input-assembly buffers, output resources,
    and likely producer events for major inputs.
    """
    return bridge.call("trace_action_dependencies", {"action_event_id": action_event_id})


@mcp.tool
def diff_actions(action_event_id_a: int, action_event_id_b: int) -> dict:
    """
    Compare two actions and report material state differences.

    Args:
        action_event_id_a: The first event ID
        action_event_id_b: The second event ID

    Returns shader, resource binding, draw parameter, mesh, and timing differences.
    """
    return bridge.call("diff_actions", {"action_event_id_a": action_event_id_a, "action_event_id_b": action_event_id_b})


@mcp.tool
def analyze_pass(marker_filter: str, exclude_markers: list[str] | None = None) -> dict:
    """
    Summarize a pass or marker subtree as one workload.

    Args:
        marker_filter: Marker-path substring selecting the pass subtree
        exclude_markers: Optional marker substrings to exclude

    Returns action counts, main shaders, representative resources, top timed actions,
    and conservative workload warnings.
    """
    params: dict[str, object] = {"marker_filter": marker_filter}
    _optional_param(params, "exclude_markers", exclude_markers)
    return bridge.call("analyze_pass", params)


@mcp.tool
def list_captures(directory: str) -> dict:
    """
    List all RenderDoc capture files (.rdc) in the specified directory.

    Args:
        directory: The directory path to search for capture files

    Returns a list of capture files with their metadata including:
    - filename: The capture file name
    - path: Full path to the file
    - size_bytes: File size in bytes
    - modified_time: Last modified timestamp (ISO format)
    """
    return bridge.call("list_captures", {"directory": directory})


@mcp.tool
def open_capture(capture_path: str, file_location: Literal["local", "remote"] = "local",
                 replay_target: Literal["current", "local", "remote"] = "current",
                 remote_host: str | None = None, job_id: str | None = None) -> dict:
    """Submit an asynchronous capture load. Query get_job_status; never retry blindly.

    file_location identifies the file, replay_target identifies where replay runs.
    A local capture replayed remotely is uploaded using RenderDoc's official API.
    Explicit remote hosts may be started with the configured official launch flow.
    Native load calls cannot be forcibly cancelled.
    """
    return bridge.call("open_capture", dict(capture_path=capture_path, file_location=file_location,
                                           replay_target=replay_target, remote_host=remote_host, job_id=job_id))


@mcp.tool
def get_mesh_summary(action_event_id: int, instance: int = 0, view_index: int = 0) -> dict:
    """
    Get a summary of mesh data for a specific draw call event.

    Args:
        action_event_id: The event ID of the draw call to inspect
        instance: Instance index for instanced attributes and post-VS data (default: 0)

    Returns mesh information including:
    - topology: Primitive topology (TriangleList, LineList, etc.)
    - num_vertices: Total vertex count
    - num_indices: Total index count (0 if non-indexed)
    - indexed: Whether the draw call uses an index buffer
    - attributes: List of vertex attributes with their formats
    - bounding_box: Min/max bounds if position attribute available
    """
    return bridge.call(
        "get_mesh_summary", {"action_event_id": action_event_id, "instance": instance, "view_index": view_index}
    )


@mcp.tool
def get_mesh_data(
    action_event_id: int,
    stage: Literal["VSIn", "VSOut", "GSOut"] = "VSIn",
    offset: int = 0,
    limit: int = 100,
    attributes: list[str] | None = None,
    instance: int = 0,
    view_index: int = 0,
) -> dict:
    """
    Get mesh vertex and index data for a specific draw call (with pagination).

    IMPORTANT: For large meshes, use pagination instead of requesting all data at once.
    Recommended: Request 100-500 vertices per call, use offset/limit for pagination.

    Args:
        action_event_id: The event ID of the draw call to inspect
        stage: Mesh data stage - VSIn (input), VSOut (vertex shader output), GSOut (geometry output)
        offset: Starting draw-reference offset for pagination (default: 0)
        limit: Maximum draw references to return (default: 100, maximum: 500)
        attributes: Optional list of attribute names to include (e.g., ["POSITION", "NORMAL", "TEXCOORD"])
                   If None, all attributes are included.
        instance: Instance index for instanced attributes and post-VS data (default: 0)

    Returns mesh data including:
    - items: List of vertex data, each vertex is a dict of attribute_name -> values
    - indices: Effective vertex references for all stages (-1 for primitive restart)
    - topology: Primitive topology
    - attributes: Metadata about each attribute
    - total_count: Total number of draw references (unique_vertex_count is separate)
    - has_more: Whether more vertices are available
    - truncated: Whether data was truncated

    Example pagination usage:
        # First page
        result = get_mesh_data(action_event_id=123, offset=0, limit=100)
        # Next page
        result = get_mesh_data(action_event_id=123, offset=100, limit=100)
    """
    params: dict[str, object] = {
        "action_event_id": action_event_id,
        "stage": stage,
        "offset": offset,
        "limit": limit,
        "instance": instance,
        "view_index": view_index,
    }
    _optional_param(params, "attributes", attributes)
    return bridge.call("get_mesh_data", params)


@mcp.tool
def export_mesh_csv(
    action_event_id: int,
    output_path: str,
    stage: Literal["VSIn", "VSOut", "GSOut"] = "VSIn",
    attributes: list[str] | None = None,
    instance: int = 0,
    view_index: int = 0,
) -> dict:
    """
    Export mesh data to a CSV file.

    Args:
        action_event_id: The event ID of the draw call to export
        output_path: Output file path (e.g. "D:/output/mesh.csv")
        stage: Mesh data stage - VSIn (input), VSOut (vertex shader output), GSOut (geometry output)
        attributes: Optional list of attributes to include
                           If None, all available attributes are included.
        instance: Instance index for instanced attributes and post-VS data (default: 0)

    Returns success status and mesh info including:
    - output_path: Path to the exported CSV file
    - index_path: Path to the index sidecar file (.idx)
    - vertex_count: Number of exported vertices
    - index_count: Number of indices
    - format: Export format (always "CSV")

    The CSV format:
    - First row: VTX, IDX, attribute columns
    - Subsequent rows: vertex data with deduplication
    - Index file (.idx): remapped triangle stream
    """
    params: dict[str, object] = {
        "action_event_id": action_event_id,
        "output_path": output_path,
        "stage": stage,
        "instance": instance,
        "view_index": view_index,
    }
    if attributes is not None:
        params["attributes"] = attributes
    return bridge.call("export_mesh_csv", params)


@mcp.tool()
def dump_draws(output_dir: str, action_event_ids: list[int] | None = None,
               marker_filter: str | None = None, action_event_id_range: dict[str, int] | None = None,
               mesh_stage: Literal["VSIn", "VSOut", "GSOut"] = "VSIn",
               instances: list[int] | None = None, view_index: int = 0,
               export_meshes: bool = True, export_textures: bool = True,
               max_textures: int = 48, max_texture_edge: int | None = None,
               skip_depth: bool = False, job_id: str | None = None,
               export_constants: bool = True) -> dict:
    """Submit a resumable export into output_dir/<job_id>/.

    Select exactly one of explicit draw IDs, a marker, or an EID range. Range/marker
    selectors resolve real draws. Instances default to [0]. Texture allowance
    exhaustion pauses the job; resume_job supplies a fresh allowance. All exports
    retain event, binding and subresource provenance. No object-matrix inference.
    """
    return bridge.call("dump_draws", dict(output_dir=output_dir, action_event_ids=action_event_ids,
        marker_filter=marker_filter, action_event_id_range=action_event_id_range, mesh_stage=mesh_stage,
        instances=instances, view_index=view_index, export_meshes=export_meshes, export_textures=export_textures,
        max_textures=max_textures, max_texture_edge=max_texture_edge, skip_depth=skip_depth, job_id=job_id,
        export_constants=export_constants))


@mcp.tool()
def get_replay_context() -> dict:
    """Get the current/known replay hosts and cached service states without moving replay."""
    return bridge.call("get_replay_context")


@mcp.tool()
def get_replay_diagnostics(output_dir: str | None = None, include_device_logs: bool = False,
                           remote_host: str | None = None) -> dict:
    """Collect persisted local diagnostics without the UI/replay thread.

    Device logs require explicit opt-in; configured ADB read-only commands are
    bounded to 20 seconds and 2 MiB. Never restarts or installs device services.
    Returns artifact paths/hashes, warnings and manifest_path, not full logs.
    """
    return bridge.call("get_replay_diagnostics", dict(output_dir=output_dir,
        include_device_logs=include_device_logs, remote_host=remote_host))


@mcp.tool()
def get_job_status(job_id: str, offset: int = 0, limit: int = 100) -> dict:
    """Get persisted job progress/results. Pagination uses items; limit is 1..500.

    A completed job is not a certification of reconstruction or user acceptance.
    stalled means no recent progress, not proof that the native operation failed.
    Batch items are compact summaries; details_path points to full persisted
    bindings/layouts, while artifact_paths lists exported files.
    """
    return bridge.call("get_job_status", dict(job_id=job_id, offset=offset, limit=limit))


@mcp.tool()
def cancel_job(job_id: str) -> dict:
    """Request cooperative cancellation between steps. Native calls cannot be interrupted."""
    return bridge.call("cancel_job", {"job_id": job_id})


@mcp.tool()
def resume_job(job_id: str, texture_budget: int = 48) -> dict:
    """Resume a paused/cancelled export in the same capture/replay revision."""
    return bridge.call("resume_job", dict(job_id=job_id, texture_budget=texture_budget))


@mcp.tool()
def export_shader_bundle(action_event_id: int, stage: str, output_dir: str,
                         job_id: str | None = None, include_event_context: bool = True,
                         export_constants: bool = True) -> dict:
    """Submit a shader evidence export: raw bytes, reflection, disassembly and embedded sources.

    Source text is only included when actually preserved in the capture. Returns a
    job_id; large shader payloads remain on disk with hashes, not in tool replies.
    """
    return bridge.call("export_shader_bundle", dict(action_event_id=action_event_id, stage=stage,
                                                   output_dir=output_dir, job_id=job_id,
                                                   include_event_context=include_event_context, export_constants=export_constants))


@mcp.tool()
def compare_texture_events(resource_id: str, action_event_id_a: int, action_event_id_b: int,
                           region: dict[str, int], output_dir: str, mip: int = 0, slice_index: int = 0,
                           sample: int = 0, depth_slice: int = 0,
                           value_domain: Literal["storage", "linear"] = "storage", job_id: str | None = None,
                           aspect: Literal["all", "depth", "stencil"] = "all") -> dict:
    """Submit typed b-minus-a ROI comparison of the same texture after two actions.

    region={x,y,width,height}, origin top-left. Max ROI 262144 pixels; max raw
    subresource 64 MiB. Supports regular numeric formats, R10G10B10A2 and R11G11B10
    on Vulkan/D3D11/D3D12; unsupported formats are explicit errors, never PNG fallbacks.
    Linear domain applies sRGB decoding to RGB only. Difference is an observation,
    not an isolated draw contribution. Full signed float64 differences are saved on disk.
    """
    return bridge.call("compare_texture_events", dict(resource_id=resource_id,
        action_event_id_a=action_event_id_a, action_event_id_b=action_event_id_b,
        region=region, output_dir=output_dir, mip=mip, slice_index=slice_index,
        sample=sample, depth_slice=depth_slice, value_domain=value_domain, job_id=job_id, aspect=aspect))


@mcp.tool()
def get_pixel_history(resource_id: str, x: int, y: int, action_event_id: int, output_dir: str,
                      mip: int = 0, slice_index: int = 0, sample: int = 0, job_id: str | None = None) -> dict:
    """Submit native pixel history up to the action. Origin top-left; check availability.

    Query get_job_status for paginated fragments and the evidence manifest. Native
    validity restrictions are retained; failed fragments can lack defined values.
    """
    return bridge.call("get_pixel_history", dict(resource_id=resource_id, x=x, y=y,
        action_event_id=action_event_id, output_dir=output_dir, mip=mip,
        slice_index=slice_index, sample=sample, job_id=job_id))


def main():
    """Run the MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
