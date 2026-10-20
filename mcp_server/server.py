"""
RenderDoc MCP Server
FastMCP server providing access to RenderDoc capture data.
"""

from typing import Literal

from fastmcp import FastMCP

from .bridge.client import RenderDocBridge, RenderDocBridgeError
from .config import settings

# Initialize FastMCP server
mcp = FastMCP(
    name="RenderDoc MCP Server",
)

# RenderDoc bridge client
bridge = RenderDocBridge(host=settings.renderdoc_host, port=settings.renderdoc_port)


def _optional_param(params: dict[str, object], name: str, value: object | None) -> None:
    """Add an optional bridge parameter when present."""
    if value is not None:
        params[name] = value


@mcp.tool
def get_capture_status() -> dict:
    """
    Check if a capture is currently loaded in RenderDoc.
    Returns the capture status and API type if loaded.
    """
    return bridge.call("get_capture_status")


@mcp.tool
def get_draw_calls(
    include_children: bool = True,
    marker_filter: str | None = None,
    exclude_markers: list[str] | None = None,
    event_id_range: dict[str, int] | None = None,
    event_id_min: int | None = None,
    event_id_max: int | None = None,
    only_actions: bool = False,
    flags_filter: list[str] | None = None,
) -> dict:
    """
    Get the list of all draw calls and actions in the current capture.

    Args:
        include_children: Include child actions in the hierarchy (default: True)
        marker_filter: Only include actions under markers containing this string (partial match)
        exclude_markers: Exclude actions under markers containing these strings (list of partial matches)
        event_id_range: Optional event_id range as {"min": ..., "max": ...}
        event_id_min: Legacy lower bound alias for event_id range
        event_id_max: Legacy upper bound alias for event_id range
        only_actions: If True, exclude marker actions (PushMarker/PopMarker/SetMarker)
        flags_filter: Only include actions with these flags (list of flag names, e.g. ["Drawcall", "Dispatch"])

    Returns a hierarchical tree of actions including markers, draw calls,
    dispatches, and other GPU events.
    """
    params: dict[str, object] = {"include_children": include_children}
    _optional_param(params, "marker_filter", marker_filter)
    _optional_param(params, "exclude_markers", exclude_markers)
    if event_id_range is not None:
        params["event_id_range"] = event_id_range
    else:
        _optional_param(params, "event_id_min", event_id_min)
        _optional_param(params, "event_id_max", event_id_max)
    if only_actions:
        params["only_actions"] = only_actions
    _optional_param(params, "flags_filter", flags_filter)
    return bridge.call("get_draw_calls", params)


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
def inspect_event(event_id: int) -> dict:
    """
    Inspect one event using a compact analysis-oriented bundle.

    Args:
        event_id: The event ID to inspect

    Returns event details, timing, shader summaries, pipeline summaries,
    and mesh summary when the event is a draw call.
    """
    return bridge.call("inspect_event", {"event_id": event_id})


@mcp.tool
def summarize_capture() -> dict:
    """
    Summarize the loaded capture at a high level.

    Returns frame statistics, hot actions, major markers, and suggested
    entry points for deeper investigation.
    """
    return bridge.call("summarize_capture")


@mcp.tool
def search_draws(
    by: Literal["shader", "texture", "resource"],
    query: str,
    stage: Literal["vertex", "hull", "domain", "geometry", "pixel", "compute"] | None = None,
) -> dict:
    """
    Search draw calls using a canonical search interface.

    Args:
        by: Search mode - shader, texture, or resource
        query: Shader name, texture name, or resource ID query
        stage: Optional shader stage filter for shader searches

    Returns a search result with matches, total_matches, and scanned_count.
    """
    params: dict[str, object] = {"by": by, "query": query}
    _optional_param(params, "stage", stage)
    return bridge.call("search_draws", params)


@mcp.tool
def get_action_api_calls(
    action_event_id: int, api_event_id: int | None = None,
    child_path: list[int] | None = None, offset: int = 0, limit: int = 50,
) -> dict:
    """Read a draw/dispatch action's associated API calls, like API Inspector.

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
def get_draw_call_details(event_id: int) -> dict:
    """
    Get detailed information about a specific draw call.

    Args:
        event_id: The event ID of the draw call to inspect

    Includes vertex/index counts, resource outputs, and other metadata.
    """
    return bridge.call("get_draw_call_details", {"event_id": event_id})


@mcp.tool
def get_action_timings(
    event_ids: list[int] | None = None,
    marker_filter: str | None = None,
    exclude_markers: list[str] | None = None,
) -> dict:
    """
    Get GPU timing information for actions (draw calls, dispatches, etc.).

    Args:
        event_ids: Optional list of specific event IDs to get timings for.
                   If not specified, returns timings for all actions.
        marker_filter: Only include actions under markers containing this string (partial match).
        exclude_markers: Exclude actions under markers containing these strings.

    Returns timing data including:
    - available: Whether GPU timing counters are supported
    - unit: Time unit (typically "seconds")
    - timings: List of {event_id, name, duration_seconds, duration_ms}
    - total_duration_ms: Sum of all durations
    - count: Number of timing entries

    Note: GPU timing counters may not be available on all hardware/drivers.
    """
    params: dict[str, object] = {}
    if event_ids is not None:
        params["event_ids"] = event_ids
    if marker_filter is not None:
        params["marker_filter"] = marker_filter
    if exclude_markers is not None:
        params["exclude_markers"] = exclude_markers
    return bridge.call("get_action_timings", params)


@mcp.tool
def get_shader_info(
    event_id: int,
    stage: Literal["vertex", "hull", "domain", "geometry", "pixel", "compute"],
) -> dict:
    """
    Get shader information for a specific stage at a given event.

    Args:
        event_id: The event ID to inspect the shader at
        stage: The shader stage (vertex, hull, domain, geometry, pixel, compute)

    Returns shader identity, entry point and disassembly. Use get_pipeline_stage
    and inspect_pipeline_binding for bindings and constant values.
    """
    return bridge.call("get_shader_info", {"event_id": event_id, "stage": stage})


@mcp.tool
def get_shader_source(
    event_id: int,
    stage: Literal["vertex", "hull", "domain", "geometry", "pixel", "compute"],
) -> dict:
    """
    Get original shader source text for a specific stage at a given event.

    Args:
        event_id: The event ID to inspect the shader at
        stage: The shader stage (vertex, hull, domain, geometry, pixel, compute)

    Returns source_text for text-backed shader encodings and metadata-only
    responses when the capture only contains binary shader payloads.
    """
    return bridge.call("get_shader_source", {"event_id": event_id, "stage": stage})


@mcp.tool
def get_shader_edit_context(
    event_id: int,
    stage: Literal["vertex", "hull", "domain", "geometry", "pixel", "compute"],
    mode: Literal["auto", "original", "glsl", "spirv_asm"] = "auto",
) -> dict:
    """Prepare editable GLSL/SPIR-V text and its compilation path for an event/stage.

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
        {"resource_id": resource_id, "offset": offset, "length": length},
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
    slice: int = 0,
    sample: int = 0,
    depth_slice: int | None = None,
    action_event_id: int | None = None,
) -> dict:
    """
    Read texture pixels after action_event_id (or the current UI event if omitted).

    Args:
        resource_id: The resource ID of the texture to read
        mip: Mip level to retrieve (default: 0)
        slice: Array slice or cube face index (default: 0)
               For cube maps: 0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-
        sample: MSAA sample index (default: 0)
        depth_slice: For 3D textures only, extract a specific depth slice (default: None = full volume)
                     When specified, returns only the 2D slice at that depth index

    Returns texture pixel data as base64-encoded bytes along with metadata
    including dimensions at the requested mip level and format information.
    """
    params = {"resource_id": resource_id, "mip": mip, "slice": slice, "sample": sample,
              "action_event_id": action_event_id}
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
    event_id_min: int | None = None,
    event_id_max: int | None = None,
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
        event_id_min: Legacy lower event bound alias
        event_id_max: Legacy upper event bound alias
        before_event_id: Optional event ID used to compute the latest prior writer
        offset: First usage record to return after filtering.
        limit: Page size, from 1 to 500 (default 100).
        categories: Optional Timeline categories, combined with OR. None selects all;
            [] selects none. Other event/marker filters are combined with AND.

    Returns raw usage, Timeline category, and legacy inferred access per record.
    category_counts contains all five categories, including zeros. GenMips/Copy/Resolve
    are read_write; Discard/Clear are clear, matching the RenderDoc Timeline.
    Counts and writer summaries cover records matching ALL filters before pagination.
    Counts are usage records, not distinct EIDs or merged visual timeline markers.
    Legacy access/read_count/write_count remain independent from Timeline categories.
    Non-texture/buffer objects report unavailable usage rather than a missing ID.
    """
    params: dict[str, object] = {"resource_id": resource_id, "offset": offset, "limit": limit}
    _optional_param(params, "marker_filter", marker_filter)
    _optional_param(params, "exclude_markers", exclude_markers)
    _optional_param(params, "categories", categories)
    if event_id_range is not None:
        params["event_id_range"] = event_id_range
    else:
        _optional_param(params, "event_id_min", event_id_min)
        _optional_param(params, "event_id_max", event_id_max)
    _optional_param(params, "before_event_id", before_event_id)
    return bridge.call("trace_resource_usage", params)


@mcp.tool
def trace_event_dependencies(event_id: int) -> dict:
    """
    Trace the immediate resource dependencies of one event.

    Args:
        event_id: The event to inspect

    Returns stage-grouped input resources, input-assembly buffers, output resources,
    and likely producer events for major inputs.
    """
    return bridge.call("trace_event_dependencies", {"event_id": event_id})


@mcp.tool
def diff_events(event_id_a: int, event_id_b: int) -> dict:
    """
    Compare two events and report material state differences.

    Args:
        event_id_a: The first event ID
        event_id_b: The second event ID

    Returns shader, resource binding, draw parameter, mesh, and timing differences.
    """
    return bridge.call("diff_events", {"event_id_a": event_id_a, "event_id_b": event_id_b})


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
def open_capture(capture_path: str) -> dict:
    """
    Open a RenderDoc capture file (.rdc).

    Args:
        capture_path: Full path to the capture file to open

    Returns success status and information about the opened capture.
    Note: This will close any currently open capture.
    """
    return bridge.call("open_capture", {"capture_path": capture_path})


@mcp.tool
def get_mesh_summary(event_id: int) -> dict:
    """
    Get a summary of mesh data for a specific draw call event.

    Args:
        event_id: The event ID of the draw call to inspect

    Returns mesh information including:
    - topology: Primitive topology (TriangleList, LineList, etc.)
    - num_vertices: Total vertex count
    - num_indices: Total index count (0 if non-indexed)
    - indexed: Whether the draw call uses an index buffer
    - attributes: List of vertex attributes with their formats
    - bounding_box: Min/max bounds if position attribute available
    """
    return bridge.call("get_mesh_summary", {"event_id": event_id})


@mcp.tool
def get_mesh_data(
    event_id: int,
    stage: Literal["VSIn", "VSOut", "GSOut"] = "VSIn",
    offset: int = 0,
    limit: int = 100,
    start_offset: int = 0,
    max_vertices: int = 100,
    attributes: list[str] | None = None,
) -> dict:
    """
    Get mesh vertex and index data for a specific draw call (with pagination).

    IMPORTANT: For large meshes, use pagination instead of requesting all data at once.
    Recommended: Request 100-500 vertices per call, use offset/limit for pagination.

    Args:
        event_id: The event ID of the draw call to inspect
        stage: Mesh data stage - VSIn (input), VSOut (vertex shader output), GSOut (geometry output)
        offset: Canonical starting vertex offset for pagination (default: 0)
        limit: Canonical maximum number of vertices to return (default: 100, max recommended: 500)
        start_offset: Legacy alias for offset
        max_vertices: Legacy alias for limit
        attributes: Optional list of attribute names to include (e.g., ["POSITION", "NORMAL", "TEXCOORD"])
                   If None, all attributes are included.

    Returns mesh data including:
    - vertices: List of vertex data, each vertex is a dict of attribute_name -> values
    - indices: Index buffer data (empty for non-indexed draws)
    - topology: Primitive topology
    - attribute_info: Metadata about each attribute
    - total_count: Total number of vertices in the mesh
    - has_more: Whether more vertices are available
    - truncated: Whether data was truncated

    Example pagination usage:
        # First page
        result = get_mesh_data(event_id=123, start_offset=0, max_vertices=100)
        # Next page
        result = get_mesh_data(event_id=123, start_offset=100, max_vertices=100)
    """
    if offset == 0 and start_offset != 0:
        offset = start_offset
    if limit == 100 and max_vertices != 100:
        limit = max_vertices

    params: dict[str, object] = {
        "event_id": event_id,
        "stage": stage,
        "offset": offset,
        "limit": limit,
        "start_offset": offset,
        "max_vertices": limit,
    }
    _optional_param(params, "attributes", attributes)
    return bridge.call("get_mesh_data", params)


@mcp.tool
def export_mesh_csv(
    event_id: int,
    output_path: str,
    stage: Literal["VSIn", "VSOut", "GSOut"] = "VSIn",
    include_attributes: list[str] | None = None,
) -> dict:
    """
    Export mesh data to a CSV file.

    Args:
        event_id: The event ID of the draw call to export
        output_path: Output file path (e.g. "D:/output/mesh.csv")
        stage: Mesh data stage - VSIn (input), VSOut (vertex shader output), GSOut (geometry output)
        include_attributes: Optional list of attributes to include
                           If None, all available attributes are included.

    Returns success status and mesh info including:
    - output_path: Path to the exported CSV file
    - index_path: Path to the index sidecar file (.idx)
    - vertex_count: Number of exported vertices
    - index_count: Number of indices
    - format: Export format (always "CSV")

    The CSV format is compatible with csv_obj project:
    - First row: VTX, IDX, attribute columns
    - Subsequent rows: vertex data with deduplication
    - Index file (.idx): remapped triangle stream
    """
    params: dict[str, object] = {
        "event_id": event_id,
        "output_path": output_path,
        "stage": stage,
    }
    if include_attributes is not None:
        params["include_attributes"] = include_attributes
    return bridge.call("export_mesh_csv", params)


def main():
    """Run the MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
