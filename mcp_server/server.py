"""
RenderDoc MCP Server
FastMCP 2.0 server providing access to RenderDoc capture data.
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
        event_id_min: Only include actions with event_id >= this value
        event_id_max: Only include actions with event_id <= this value
        only_actions: If True, exclude marker actions (PushMarker/PopMarker/SetMarker)
        flags_filter: Only include actions with these flags (list of flag names, e.g. ["Drawcall", "Dispatch"])

    Returns a hierarchical tree of actions including markers, draw calls,
    dispatches, and other GPU events.
    """
    params: dict[str, object] = {"include_children": include_children}
    if marker_filter is not None:
        params["marker_filter"] = marker_filter
    if exclude_markers is not None:
        params["exclude_markers"] = exclude_markers
    if event_id_min is not None:
        params["event_id_min"] = event_id_min
    if event_id_max is not None:
        params["event_id_max"] = event_id_max
    if only_actions:
        params["only_actions"] = only_actions
    if flags_filter is not None:
        params["flags_filter"] = flags_filter
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
def find_draws_by_shader(
    shader_name: str,
    stage: Literal["vertex", "hull", "domain", "geometry", "pixel", "compute"] | None = None,
) -> dict:
    """
    Find all draw calls using a shader with the given name (partial match).

    Args:
        shader_name: Partial name to search for in shader names or entry points
        stage: Optional shader stage to search (if not specified, searches all stages)

    Returns a list of matching draw calls with event IDs and match reasons.
    """
    params: dict[str, object] = {"shader_name": shader_name}
    if stage is not None:
        params["stage"] = stage
    return bridge.call("find_draws_by_shader", params)


@mcp.tool
def find_draws_by_texture(texture_name: str) -> dict:
    """
    Find all draw calls using a texture with the given name (partial match).

    Args:
        texture_name: Partial name to search for in texture resource names

    Returns a list of matching draw calls with event IDs and match reasons.
    Searches SRVs, UAVs, and render targets.
    """
    return bridge.call("find_draws_by_texture", {"texture_name": texture_name})


@mcp.tool
def find_draws_by_resource(resource_id: str) -> dict:
    """
    Find all draw calls using a specific resource ID (exact match).

    Args:
        resource_id: Resource ID to search for (e.g. "ResourceId::12345" or "12345")

    Returns a list of matching draw calls with event IDs and match reasons.
    Searches shaders, SRVs, UAVs, render targets, and depth targets.
    """
    return bridge.call("find_draws_by_resource", {"resource_id": resource_id})


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

    Returns shader disassembly, constant buffer values, and resource bindings.
    """
    return bridge.call("get_shader_info", {"event_id": event_id, "stage": stage})


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
def list_textures(
    name_filter: str | None = None,
    offset: int = 0,
    limit: int = 50,
) -> dict:
    """
    List all textures in the current capture with optional filtering and pagination.

    Args:
        name_filter: Optional partial name match (case-insensitive).
                    E.g. "Character" matches "CharacterSkin_Diffuse", "CharacterNormal", etc.
        offset: Starting index for pagination (default: 0)
        limit: Maximum number of textures to return (default: 50)

    Returns a list of textures with metadata:
    - textures: List of {resource_id, name, width, height, depth, format, mip_levels,
              array_size, byte_size, dimension, cubemap, msaa_samples}
    - total_count: Total number of textures matching the filter
    - offset/limit: Current pagination state
    - returned_count: Number of textures in this response
    """
    params: dict[str, object] = {"offset": offset, "limit": limit}
    if name_filter is not None:
        params["name_filter"] = name_filter
    return bridge.call("list_textures", params)


@mcp.tool
def list_buffers(
    name_filter: str | None = None,
    offset: int = 0,
    limit: int = 50,
) -> dict:
    """
    List all buffers in the current capture with optional filtering and pagination.

    Args:
        name_filter: Optional partial name match (case-insensitive).
                    E.g. "Camera" matches "CameraCB", "CameraData", etc.
        offset: Starting index for pagination (default: 0)
        limit: Maximum number of buffers to return (default: 50)

    Returns a list of buffers with metadata:
    - buffers: List of {resource_id, name, byte_size, creation_flags}
              creation_flags can include: "Vertex", "Index", "Constants", "ReadWrite", "Indirect"
    - total_count: Total number of buffers matching the filter
    - offset/limit: Current pagination state
    - returned_count: Number of buffers in this response
    """
    params: dict[str, object] = {"offset": offset, "limit": limit}
    if name_filter is not None:
        params["name_filter"] = name_filter
    return bridge.call("list_buffers", params)


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
) -> dict:
    """
    Read the pixel data of a texture resource.

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
    params = {"resource_id": resource_id, "mip": mip, "slice": slice, "sample": sample}
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
) -> dict:
    """
    Save a texture to an image file.

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
        },
    )


@mcp.tool
def get_pipeline_state(event_id: int) -> dict:
    """
    Get the full graphics pipeline state at a specific event.

    Args:
        event_id: The event ID to get pipeline state at

    Returns detailed pipeline state including:
    - Bound shaders with entry points for each stage
    - Shader resources (SRVs): textures and buffers with dimensions, format, slot, name
    - UAVs (RWTextures/RWBuffers): resource details with dimensions and format
    - Samplers: addressing modes, filter settings, LOD parameters
    - Constant buffers: slot, size, variable count
    - Render targets and depth target
    - Viewports and input assembly state
    """
    return bridge.call("get_pipeline_state", {"event_id": event_id})


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
    start_offset: int = 0,
    max_vertices: int = 100,
    attributes: list[str] | None = None,
) -> dict:
    """
    Get mesh vertex and index data for a specific draw call (with pagination).

    IMPORTANT: For large meshes, use pagination instead of requesting all data at once.
    Recommended: Request 100-500 vertices per call, use start_offset for pagination.

    Args:
        event_id: The event ID of the draw call to inspect
        stage: Mesh data stage - VSIn (input), VSOut (vertex shader output), GSOut (geometry output)
        start_offset: Starting vertex offset for pagination (default: 0)
        max_vertices: Maximum number of vertices to return (default: 100, max recommended: 500)
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
    params: dict[str, object] = {
        "event_id": event_id,
        "stage": stage,
        "start_offset": start_offset,
        "max_vertices": max_vertices,
    }
    if attributes is not None:
        params["attributes"] = attributes
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
