# MCP Tools Reference

[中文](tools_zh.md)

Detailed reference for all RenderDoc MCP tools, including parameters, return values, and usage examples.

## Recommended Workflow

A typical analysis workflow follows this pattern:

`get_capture_status` / `get_frame_summary` -> `get_draw_calls` / `search_draws` -> `get_pipeline_state` / `get_shader_info` / `get_mesh_data`

---

## Global Operations

### Capture Management

#### `open_capture`

Open a RenderDoc capture file (.rdc). Closes any currently open capture.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `capture_path` | `str` | Yes | Full path to the capture file |

**Returns:** `{"success": true, "filename": "game.rdc", "api": "D3D11"}`

**Example:**
```
open_capture(capture_path="D:/captures/game.rdc")
```

---

#### `list_captures`

List all `.rdc` files in a directory.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `directory` | `str` | Yes | Directory path to search |

**Returns:** List with `filename`, `path`, `size_bytes`, `modified_time` per entry.

**Example:**
```
list_captures(directory="D:/captures")
# → {"count": 3, "captures": [{"filename": "game.rdc", "path": "D:/captures/game.rdc", "size_bytes": 12345, "modified_time": "..."}]}
```

---

#### `get_capture_status`

Check if a capture is currently loaded in RenderDoc. Returns the capture status and API type if loaded.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| *(none)* | | | |

**Returns:** `{"loaded": true, "api": "D3D11"}` or `{"loaded": false}`

**Example:**
```
get_capture_status()
```

---

### Frame Overview

#### `get_frame_summary`

Get frame-wide statistics and top-level marker summaries.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| *(none)* | | | |

**Returns:** API type, total action count, statistics (draw calls, dispatches, clears, copies, presents, markers), top-level markers with event IDs and child counts, resource counts (textures, buffers).

**Example:**
```
get_frame_summary()
```

---

#### `summarize_capture`

Builds on `get_frame_summary` with additional full-frame GPU timing, sorting, and deduplication. Returns a high-level overview with suggested investigation entry points.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| *(none)* | | | |

**Returns:** Frame statistics, `hot_actions` (Top 10 by GPU time), major markers, and `suggested_entry_points`.

**Example:**
```
summarize_capture()
```

---

### Action Navigation

#### `get_draw_calls`

Get the hierarchical tree of draw calls and actions with filtering support.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `include_children` | `bool` | No | `true` | Include child actions in hierarchy |
| `marker_filter` | `str` | No | | Only include actions under markers containing this string (partial match) |
| `exclude_markers` | `list[str]` | No | | Exclude actions under markers containing these strings |
| `event_id_range` | `dict` | No | | Event ID range as `{"min": ..., "max": ...}` |
| `event_id_min` | `int` | No | | Legacy lower bound alias for event ID range |
| `event_id_max` | `int` | No | | Legacy upper bound alias for event ID range |
| `only_actions` | `bool` | No | `false` | If true, exclude marker actions |
| `flags_filter` | `list[str]` | No | | Only include actions with these flags (e.g. `["Drawcall", "Dispatch"]`) |

**Returns:** Hierarchical tree of actions including markers, draw calls, dispatches, and other GPU events.

**Examples:**
```
# Get all draw calls with children
get_draw_calls(include_children=true)

# Filter by marker and event range
get_draw_calls(marker_filter="Camera.Render", event_id_min=7372, event_id_max=7600)

# Only draw calls, exclude markers
get_draw_calls(only_actions=true, flags_filter=["Drawcall"])

# Exclude specific markers
get_draw_calls(exclude_markers=["GUI.Repaint", "UIR.DrawChain"])
```

---

#### `search_draws`

Unified search for draw calls by shader, texture, or resource.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `by` | `"shader"` / `"texture"` / `"resource"` | Yes | Search mode |
| `query` | `str` | Yes | Shader name, texture name, or resource ID |
| `stage` | `str` | No | Shader stage filter (`"vertex"`, `"pixel"`, `"compute"`, etc.) — only for `by="shader"` |

**Returns:** `{"matches": [...], "total_matches": 3, "scanned_count": 150}`

**Examples:**
```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

---

### Resource Space Browsing

#### `list_resources`

List textures or buffers with a unified paginated interface.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `resource_type` | `"texture"` / `"buffer"` | Yes | | Resource family to list |
| `name_filter` | `str` | No | | Partial name match (case-insensitive) |
| `offset` | `int` | No | `0` | Starting index for pagination |
| `limit` | `int` | No | `50` | Maximum resources to return |

**Returns:** `{"items": [...], "total_count": 150, "offset": 0, "limit": 50, "returned_count": 50}`

**Examples:**
```
# List textures with name filter
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)

# List buffers
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)

# Paginated access
list_resources(resource_type="texture", offset=50, limit=50)
```

---

## Local Data Analysis

### Pipeline State

#### `get_pipeline_state`

Get the full graphics pipeline state at a specific event. Includes bound shaders, resource bindings, samplers, constant buffers, render targets, input/output texture summaries, viewports, and input assembly state.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID to inspect |

**Returns:** Detailed pipeline state with `input_textures` / `output_textures` summaries.

**Example:**
```
get_pipeline_state(event_id=123)
# → { ..., "input_textures": [{"resource_id": "ResourceId::2495", "name": "CharacterDiffuse", ...}],
#        "output_textures": [{"resource_id": "ResourceId::3001", "type": "render_target", ...}],
#        "input_count": 3, "output_count": 2 }
```

---

#### `get_shader_info`

Get shader information for a specific stage at a given event. Includes disassembly, constant buffer values, and resource bindings.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID |
| `stage` | `str` | Yes | Shader stage: `"vertex"`, `"hull"`, `"domain"`, `"geometry"`, `"pixel"`, `"compute"` |

**Returns:** Shader resource ID, entry point, stage, disassembly, constant buffers, resource bindings.

**Example:**
```
get_shader_info(event_id=123, stage="pixel")
```

---

### Resource Data Access

#### `get_texture_info`

Get metadata about a texture resource.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resource_id` | `str` | Yes | The resource ID (e.g. `"ResourceId::2495"`) |

**Returns:** Dimensions, format, mip levels, array size, and other properties.

**Example:**
```
get_texture_info(resource_id="ResourceId::2495")
```

---

#### `get_texture_data`

Read the pixel data of a texture resource. Returns base64-encoded bytes.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `resource_id` | `str` | Yes | | The resource ID |
| `mip` | `int` | No | `0` | Mip level to retrieve |
| `slice` | `int` | No | `0` | Array slice or cube face index (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-) |
| `sample` | `int` | No | `0` | MSAA sample index |
| `depth_slice` | `int` | No | | For 3D textures only, extract a specific depth slice. If omitted, returns full volume. |

**Returns:** Base64-encoded pixel data with metadata (dimensions, format).

**Examples:**
```
# Get mip 0 of a 2D texture
get_texture_data(resource_id="ResourceId::123")

# Get a specific mip level
get_texture_data(resource_id="ResourceId::123", mip=2)

# Get a specific face of a cubemap (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(resource_id="ResourceId::456", slice=3)

# Get a specific depth slice of a 3D texture
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

---

#### `get_buffer_contents`

Read the contents of a buffer resource. Returns base64-encoded bytes.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `resource_id` | `str` | Yes | | The resource ID |
| `offset` | `int` | No | `0` | Byte offset to start reading from |
| `length` | `int` | No | `0` | Number of bytes to read (0 = entire buffer) |

**Returns:** Base64-encoded buffer data with metadata.

**Examples:**
```
# Get entire buffer
get_buffer_contents(resource_id="ResourceId::123")

# Get 512 bytes from offset 256
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

---

#### `get_mesh_summary`

Get a summary of mesh data for a specific draw call event.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID of the draw call |

**Returns:** Topology, vertex/index counts, whether indexed, vertex attributes with formats, bounding box.

**Example:**
```
get_mesh_summary(event_id=1234)
# → {"topology": "TriangleList", "num_vertices": 3024, "num_indices": 9072, "indexed": true,
#    "attributes": [{"name": "POSITION", "format": "R32G32B32_FLOAT", "components": 3}, ...],
#    "bounding_box": {"min": [-10.0, -5.0, -2.0], "max": [10.0, 5.0, 2.0]}}
```

---

#### `get_mesh_data`

Get mesh vertex and index data for a specific draw call with pagination support.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `event_id` | `int` | Yes | | The event ID |
| `stage` | `str` | No | `"VSIn"` | Mesh data stage: `"VSIn"` (input), `"VSOut"` (vertex shader output), `"GSOut"` (geometry output) |
| `offset` | `int` | No | `0` | Starting vertex offset for pagination |
| `limit` | `int` | No | `100` | Max vertices to return (recommended: 100-500) |
| `start_offset` | `int` | No | `0` | Legacy alias for `offset` |
| `max_vertices` | `int` | No | `100` | Legacy alias for `limit` |
| `attributes` | `list[str]` | No | | Filter to specific attribute names (e.g. `["POSITION", "NORMAL"]`). If omitted, all attributes included. |

**Returns:** `vertices`, `indices`, `topology`, `attribute_info`, `total_count`, `has_more`, `truncated`.

**Examples:**
```
# First page
get_mesh_data(event_id=1234, offset=0, limit=100)

# Next page
get_mesh_data(event_id=1234, offset=100, limit=100)

# Filter specific attributes
get_mesh_data(event_id=1234, offset=0, limit=100, attributes=["POSITION", "NORMAL", "TEXCOORD"])
```

---

### Action Metadata

#### `get_draw_call_details`

Get detailed information about a specific draw call.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID of the draw call |

**Returns:** Vertex/index counts, resource outputs, and other metadata.

**Example:**
```
get_draw_call_details(event_id=123)
```

---

#### `get_action_timings`

Get GPU timing information for actions.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `event_ids` | `list[int]` | No | | Specific event IDs. If omitted, returns all actions. |
| `marker_filter` | `str` | No | | Only include actions under markers containing this string |
| `exclude_markers` | `list[str]` | No | | Exclude actions under markers containing these strings |

**Returns:** `{"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}`

> **Note:** GPU timing counters may not be available on all hardware/drivers. If `available` is `false`, timing data cannot be retrieved.

**Examples:**
```
# All actions
get_action_timings()

# Specific event IDs
get_action_timings(event_ids=[100, 200, 300])

# Filter by marker
get_action_timings(marker_filter="Camera.Render", exclude_markers=["GUI.Repaint"])
```

---

### Composite Analysis

Cross-dimensional queries that orchestrate multiple services on top of atomic tools.

#### `inspect_event`

Inspect one event with a compact analysis-oriented bundle. Returns details, timing, shader summaries, pipeline summaries, and mesh summary when the event is a draw call.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID to inspect |

**Returns:** Event details, timing, shader summaries, pipeline summaries, mesh summary.

**Example:**
```
inspect_event(event_id=1517)
```

---

#### `trace_resource_usage`

Trace how a resource is read, written, and consumed across matching events.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `resource_id` | `str` | Yes | | The resource to trace |
| `marker_filter` | `str` | No | | Marker-path substring filter |
| `exclude_markers` | `list[str]` | No | | Marker substrings to exclude |
| `event_id_range` | `dict` | No | | Event range as `{"min": ..., "max": ...}` |
| `event_id_min` | `int` | No | | Legacy lower event bound alias |
| `event_id_max` | `int` | No | | Legacy upper event bound alias |
| `before_event_id` | `int` | No | | Compute the latest prior writer before this event |

**Returns:** Resource metadata, usage roles, read/write event lists, and writer summaries.

**Example:**
```
trace_resource_usage(resource_id="ResourceId::2495")
trace_resource_usage(resource_id="ResourceId::2495", marker_filter="Forward", before_event_id=1517)
```

---

#### `trace_event_dependencies`

Trace the immediate resource dependencies of one event.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event to inspect |

**Returns:** Stage-grouped input resources, input-assembly buffers, output resources, and likely producer events for major inputs.

**Example:**
```
trace_event_dependencies(event_id=1517)
```

---

#### `diff_events`

Compare two events and report material state differences.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id_a` | `int` | Yes | The first event ID |
| `event_id_b` | `int` | Yes | The second event ID |

**Returns:** Shader, resource binding, draw parameter, mesh, and timing differences.

**Example:**
```
diff_events(event_id_a=100, event_id_b=200)
```

---

#### `analyze_pass`

Summarize one marker subtree or pass as a coherent workload.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `marker_filter` | `str` | Yes | | Marker-path substring selecting the pass subtree |
| `exclude_markers` | `list[str]` | No | | Marker substrings to exclude |

**Returns:** Action counts, main shaders, representative resources, top timed actions, and conservative workload warnings.

**Example:**
```
analyze_pass(marker_filter="ShadowPass")
analyze_pass(marker_filter="Forward", exclude_markers=["GUI"])
```

---

## Upper-level Tools

### Resource Export

#### `save_texture`

Save a texture to an image file. Handles format conversion automatically.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `resource_id` | `str` | Yes | | The resource ID (e.g. `"ResourceId::2495"`) |
| `output_path` | `str` | Yes | | Output file path (e.g. `"D:/output/texture.png"`) |
| `format_type` | `str` | No | `"PNG"` | Output format: `"PNG"`, `"JPG"`, `"BMP"`, `"TGA"`, `"EXR"`, `"DDS"`, `"HDR"` |
| `mip` | `int` | No | `0` | Mip level to save (`-1` = all mips) |
| `slice_index` | `int` | No | `0` | Array slice or cube face index (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-) |
| `alpha_mode` | `str` | No | `"preserve"` | Alpha handling: `"preserve"`, `"discard"`, `"blend_to_black"` |

**Returns:** `{"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}`

**Examples:**
```
# Save as PNG
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")

# Save as JPG with alpha blending
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG", alpha_mode="blend_to_black")

# Export all mip levels as DDS
save_texture(resource_id="ResourceId::2495", output_path="D:/output/texture.dds", format_type="DDS", mip=-1)
```

---

#### `export_mesh_csv`

Export mesh data to a CSV file, compatible with the [csv_obj](https://github.com/nicbarker/csv_obj) project.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `event_id` | `int` | Yes | | The event ID of the draw call |
| `output_path` | `str` | Yes | | Output file path (e.g. `"D:/output/mesh.csv"`) |
| `stage` | `str` | No | `"VSIn"` | Mesh data stage: `"VSIn"`, `"VSOut"`, `"GSOut"` |
| `include_attributes` | `list[str]` | No | | Filter to specific attributes. If omitted, all attributes included. |

**Returns:** `{"success": true, "output_path": "D:/output/mesh.csv", "index_path": "D:/output/mesh.idx", "vertex_count": 3024, "index_count": 9072}`

**CSV format:**
- First row: `VTX,IDX,in_POSITION0.x,in_POSITION0.y,...`
- VTX: deduplicated vertex index
- IDX: original vertex index
- Index sidecar file (`.idx`): remapped triangle stream

**Example:**
```
export_mesh_csv(event_id=1234, output_path="D:/output/mesh.csv", stage="VSIn", include_attributes=["POSITION", "NORMAL", "TEXCOORD"])
```
