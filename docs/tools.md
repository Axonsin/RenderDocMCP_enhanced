# MCP Tools Reference

[中文](tools_zh.md)

Detailed reference for all RenderDoc MCP tools, including parameters, return values, and usage examples.

## Naming Conventions

| Term / field | Meaning |
|---|---|
| `event_id` (EID) | Frame event identifier; may refer to a state-setting API event. Used for shader replay-state queries and raw resource usage records. |
| `action_event_id` | The EID of an action, used consistently in action inputs and response records, including nested records, meshes, timings and search matches. |
| `action_id` | Separate, 1-based action ordinal. Never pass it as an EID. |
| `api_event_id` | EID of one API event associated with the selected action. It shares the EID namespace with `action_event_id`. |
| action / draw call | Action is the broader term: it includes draws, dispatches, copies, clears and marker nodes. Draw call means an actual draw. Search currently scans draw and dispatch actions. |

An action EID is not an ID assigned to a bundle of API calls. For example, API EIDs
340–343 may be associated with a draw whose `action_event_id` is 343 and whose
`action_id` is 12. API EID 341 selects an individual associated API event.
Raw resource usage and producer records retain `event_id`, including when no action
can be resolved. Shader queries retain `event_id` because they read replay state at
an event rather than requiring an exact action. Texture reads/exports accept an
optional exact `action_event_id`; omission uses the current UI replay position.
Texture responses identify an explicit action with `action_event_id`; implicit UI
positions use `event_id` because they may be intermediate API events.

Shader stages use `vertex`, `tess_control`, `tess_eval`, `geometry`, `fragment`,
`compute`, `task`, `mesh` as canonical response names where supported by RenderDoc.
Shader and pipeline tools accept the same shader-stage aliases, including
`hull`/`HS`/`TCS`, `domain`/`DS`/`TES`, and `pixel`/`PS`/`FS`.
Pipeline-only sections such as `vertex_input`, `rasterizer`, `framebuffer` are not
shader stages. Mesh `stage` values `VSIn`/`VSOut`/`GSOut` select mesh data locations.

Texture read/export inputs and response fields use `slice_index` for array layers
or cube faces; `depth_slice` selects a Z plane in a 3D texture. Mesh read/export
attribute filters use `attributes`. Pagination uses `offset`/`limit`, measured in
items (mesh vertices for mesh reads); buffer `offset`/`length` are byte ranges.

Action interfaces use `action_event_id` / `action_event_ids` / `action_event_id_range`.
Comparison uses `action_event_id_a` / `action_event_id_b` and response `action_a` /
`action_b`. `analyze_pass` returns `action_event_id_range`.
`exclude_marker_actions` excludes marker nodes; markers are themselves actions.
API-call context returns `name`, matching other action records.
`inspect_action.timing.action` contains the matched action timing.
Interfaces are checked against their current signatures.

## Recommended Workflow

A typical analysis workflow follows this pattern:

`get_capture_status` / `get_frame_summary` -> `get_actions` / `search_actions` -> `get_pipeline_state` / `get_shader_info` / `get_shader_source` / `get_shader_edit_context` / `get_mesh_data`

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

#### `get_actions`

Get the action tree (draws, dispatches, copies, clears and markers) with filtering support.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `include_children` | `bool` | No | `true` | Include child actions in hierarchy |
| `marker_filter` | `str` | No | | Only include actions under markers containing this string (partial match) |
| `exclude_markers` | `list[str]` | No | | Exclude actions under markers containing these strings |
| `action_event_id_range` | `dict` | No | | Event ID range as `{"min": ..., "max": ...}` |
| `exclude_marker_actions` | `bool` | No | `false` | If true, exclude marker actions |
| `flags_filter` | `list[str]` | No | | Only include actions with these flags (e.g. `["Drawcall", "Dispatch"]`) |

**Returns:** Hierarchical tree of actions including markers, draw calls, dispatches, and other GPU events.

**Examples:**
```
# Get the full action tree
get_actions(include_children=true)

# Filter by marker and event range
get_actions(marker_filter="Camera.Render", action_event_id_range={"min": 7372, "max": 7600})

# Only draw calls, exclude markers
get_actions(exclude_marker_actions=true, flags_filter=["Drawcall"])

# Exclude specific markers
get_actions(exclude_markers=["GUI.Repaint", "UIR.DrawChain"])
```

---

#### `search_actions`

Search draw and dispatch actions by shader, texture, or resource.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `by` | `"shader"` / `"texture"` / `"resource"` | Yes | Search mode |
| `query` | `str` | Yes | Shader name, texture name, or resource ID |
| `stage` | `str` | No | Shader stage filter (`"vertex"`, `"fragment"`, `"compute"`, etc.) — only for `by="shader"` |

**Returns:** `{"matches": [...], "total_matches": 3, "scanned_count": 150}`

**Examples:**
```
search_actions(by="shader", query="Toon", stage="fragment")
search_actions(by="texture", query="CharacterSkin")
search_actions(by="resource", query="ResourceId::12345")
```

---

### Resource Space Browsing

These read-only tools expose the Resource Inspector data without changing the selected event or resource. IDs, chunk indices and parameter paths belong to the currently loaded capture. All pages require `offset >= 0` and `1 <= limit <= 500` and return `total_count`, `offset`, `limit`, `returned_count`, and `has_more`.

#### `list_resources`

List every API object from `GetResources()`, including devices, memory, shaders, views and command buffers.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `resource_type` | `str` | `"all"` | `all` or an exact snake_case RenderDoc ResourceType |
| `name_filter` | `str` | `None` | Case-insensitive display-name substring |
| `offset` | `int` | `0` | First matching resource |
| `limit` | `int` | `50` | Page size, 1–500 |
| `sort_by` | `str` | `"name"` | `name` or numeric `resource_id`; ID breaks name ties |

Each item contains only `resource_id`, `name`, and `resource_type`. Display names include user renames. `texture` and `swapchain_image` are distinct type filters.

```python
list_resources()  # All API objects
list_resources(resource_type="memory", sort_by="resource_id")
list_resources(resource_type="texture", name_filter="Scene", offset=50)
```

#### `inspect_resource`

Parameters: required `resource_id: str`, `related_offset: int = 0`, `related_limit: int = 50`.

Returns `resource` (identity), `metadata` (texture/buffer details, otherwise `{}`), `related_resources`, `usage`, and `initialization`.

- Related items contain `relationship: "parent" | "derived"` and a resource identity. Parents precede derived resources; each group is sorted by display name and numeric ID. Missing referenced objects retain their IDs with `missing: true`.
- `usage` contains availability, `usage_count`, distinct `event_count` and raw `usage_counts`, without event records. Unsupported object types return `available: false, reason: "unsupported_resource_type"`. Successful empty queries return zero counts. A driver failure is reported as `reason: "query_failed"` with an error.
- `initialization` contains the first 20 call-directory items (`chunk_index`, `name`, `child_count`) and pagination. Continue with `get_resource_initialization(offset=20)`. Invalid directory indices are preserved with an error. Section failures do not discard the remaining inspection result.

```python
inspect_resource(resource_id="ResourceId::86983")
inspect_resource(resource_id="ResourceId::86826", related_offset=50)
```

#### `get_resource_initialization`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `resource_id` | `str` | Required | Resource whose initialization is inspected |
| `chunk_index` | `int` | `None` | Omit to list calls; otherwise use a returned index belonging to this resource |
| `child_path` | `list[int]` | `[]` | Raw child indices from a returned node, relative to the selected chunk |
| `offset` | `int` | `0` | Offset in the call directory or visible immediate children |
| `limit` | `int` | `50` | Page size, 1–500 |

Without `chunk_index`, returns a paginated call directory. With it, returns `node` and paginated `children`. Each node has `name`, `type`, `basic_type`, `child_path` and raw `child_count`; scalar nodes also contain `value`. Structures and arrays expand one level per request. Hidden children are excluded from child pages, but returned paths retain raw indices so duplicate names and hidden siblings cannot make paths ambiguous. Child-page totals count visible children.

Enums/flags retain their numeric value and any available `display_value`. Resource-valued parameters contain resource identities. Binary data is represented by `byte_size` and `content_omitted`, never payload bytes. Text values/display strings are limited to 4096 characters with `<field>_truncated` and `<field>_length`. Non-finite floats use `value: null` and a `non_finite` label.

```python
get_resource_initialization(resource_id="ResourceId::86983")
# Use chunk_index and child_path returned by the previous response:
get_resource_initialization(resource_id="ResourceId::86983", chunk_index=42)
get_resource_initialization(resource_id="ResourceId::86983", chunk_index=42, child_path=[1])
```

Invalid pagination, sort keys, resource types, chunk ownership and paths produce invalid-parameter errors. Missing resources and capture/query failures produce runtime errors. Only textures/buffers (including swapchain images with texture descriptors) have usage queries in this version. Initialization describes creation/setup, not current buffer or texture contents.

**Migration:** `list_resources` now defaults to all objects and returns compact identities; move width/format/size reads to `inspect_resource(...)["metadata"]` (or existing `get_texture_info`). `trace_resource_usage` returns one paginated `events` list instead of duplicate `reads`/`writes` lists; use Timeline `category` / the `categories` filter and follow `has_more`. Its `resource` is also a compact identity. `event_count` counts distinct EIDs; `usage_count`/`total_count` count usage records.

After installing/reloading the updated extension and restarting the MCP server, open a capture and run `python scripts/validate_resources_live.py --resource-id ResourceId::86983` (substitute an ID from that capture). The read-only script prints a JSON report for comparison with Resource Inspector and leaves the current selection unchanged. Automated tests use simulated bindings and real file IPC; they do not replace this live check.

---

## Local Data Analysis

### Session-scoped Shader Editing

Supports GLSL, Vulkan SPIR-V and OpenGL SPIR-V. Replacement affects every draw referencing
the original shader resource, lasts only for the open capture session, and does not write
the `.rdc` file. HLSL / DXBC / DXIL editing is TODO.

| Tool | Parameters | Behavior |
|------|------------|----------|
| `get_shader_edit_context` | `event_id: int, stage: str, mode: str = "auto"` | Prepare editable text, edit ID, compiler path and status |
| `replace_shader` | `edit_id: str, source_text: str` | Compile and apply; compilation failure preserves the previous successful replacement |
| `revert_shader` | `edit_id: str` | Restore the original shader; repeat calls are safe |
| `list_shader_replacements` | None | Active replacements in `items`; all prepared/failed/conflicting edits in `sessions` |
| `export_shader_source` | `edit_id: str, output_path: str` | Export latest submitted text as UTF-8; refuse existing files |

Stages use the canonical `vertex / tess_control / tess_eval / geometry / fragment / compute / task / mesh` names.
Modes: `auto / original / glsl / spirv_asm`. Auto uses original GLSL, or prefers a complete
SPIRV-Cross → GLSL → compiler path, falling back to spirv-dis → assembly → spirv-as when
that path is unavailable. Explicit modes never fall back. `original` requires captured
GLSL text; pseudocode is not compilable source.
Auto reuses an existing edit and its current representation when querying submitted results;
after reverting, an explicit mode can prepare a different representation.
Submit one self-contained source text; project include management and editing multiple
entry points of one resource are not supported.
Tools are selected from RenderDoc's Settings → Shader Processing configuration.

```python
edit = get_shader_edit_context(event_id=123, stage="fragment", mode="auto")
# Modify edit["source_text"], preserving bindings and stage interfaces.
result = replace_shader(edit_id=edit["edit_id"], source_text=modified_source)
# Check last_attempt_status == "applied" and inspect warnings/errors in log.
get_pipeline_state(action_event_id=123)
# Compare the same output texture using get_texture_data / save_texture.
export_shader_source(edit_id=edit["edit_id"], output_path="D:/captures/edited_shader.glsl")
revert_shader(edit_id=edit["edit_id"])
```

The context contains `source_text` (latest submission or initial text), `applied_source_text`
(the successfully applied text), entry points, encodings, compiler, `revision`, `applied`,
`last_attempt_status`, and `log`. Compilation failure returns `compile_failed` as an ordinary
result; `applied=true` can mean the previous version is still active. Export reports
`matches_applied_source`; failed drafts remain exportable.

IDs expire on capture close, reopening the same path, or extension unload. External editor
replacements produce `SHADER_EDIT_CONFLICT`; revert in their owning editor first. Revert
before switching editing representations. Missing conversion tools produce `SHADER_TOOL_MISSING`;
expired IDs produce `INVALID_EDIT_ID`; export collisions produce `OUTPUT_FILE_EXISTS`.

Editing calls time out after 120 seconds. `RESULT_PENDING` means the request was submitted
but its result is unknown: **never automatically retry a replacement**. Query
`list_shader_replacements()` or get the context for the same event/stage to confirm state.

Update with `uv tool install . --editable` and `python scripts/install_extension.py`, reload
the Bridge in RenderDoc's extension manager (or restart RenderDoc), then reconnect the MCP client.
Run automated checks with `python -m unittest discover -s tests -v`. Validate unchanged
roundtrips, color changes, failed compilation, repeated replacement, restoration and shared
shader effects separately on real OpenGL GLSL, Vulkan SPIR-V and OpenGL SPIR-V captures.

For mobile captures, select the device's **Replay Context** in RenderDoc before opening
the capture. Both `get_capture_status()` and the edit context report `remote_replay=true`
when replay runs remotely. hkrpg captures must be validated on the connected mobile device.
Decompiler/compiler tools run on the host; replacement and replay run on the mobile GPU.
Validate an already-open mobile capture with:

```bash
python scripts/validate_shader_edit_remote.py --event-id 2069 --output-dir build/shader-edit-validation/mobile-run
# Optional shared-shader candidates; actual bindings are verified first.
python scripts/validate_shader_edit_remote.py --event-id 2808 --shared-event-ids 2799 2792 --output-dir build/shader-edit-validation/shared-run
```

Choose an event appropriate for the capture and a new output directory. The script records
roundtrip/color/failure/repeated-edit/assembly/export results and images/pixel hashes,
and restores its replacement without closing the capture. `scripts/validate_shader_edit.py`
is a separate-instance local replay helper and refuses to load hkrpg captures locally.

### Pipeline State

#### `get_pipeline_state`

`get_pipeline_state(action_event_id)` returns a compact Pipeline State overview: API,
pipeline identities, stage status, available sections, binding counts and diagnostics.
It requires an exact action EID. The former `event_id` argument and aggregate
`shaders` / `input_textures` / `output_textures` response fields have been removed.

#### `get_pipeline_stage`

```python
get_pipeline_state(action_event_id=343)
get_pipeline_stage(action_event_id=343, stage="FS")
get_pipeline_stage(action_event_id=343, stage="FS", section="constant_buffers", offset=0, limit=50)
```

Arguments: `action_event_id`, `stage`, `section="overview"`, `show_unused=False`,
`show_empty=False`, `offset=0`, `limit=50` (1–500). Overview advertises sections.
Stage identifiers: `vertex_input`, `vertex`, `tess_control`, `tess_eval`, `geometry`,
`task`, `mesh`, `rasterizer`, `fragment`, `framebuffer`, `compute`. Aliases include
VS, HS/TCS, DS/TES, GS, AS/TS, MS, FS/PS, CS and FB/OM; display labels follow the API.

| Stage | Sections |
|---|---|
| Vertex Input | `assembly`, `attributes`, `buffers` |
| Shader stages | `shader`, `descriptors`, `resources`, `samplers`, `constant_buffers`, `push_constants` |
| Rasterizer | `rasterizer`, `viewports`, `scissors`, `multisample` |
| Framebuffer | `attachments`, `blend`, `depth_stencil` |
| Compute | Shader sections plus `dispatch` |

Lists return `items`, `total_count`, `offset`, `limit`, `returned_count`, `has_more`.
Stage state distinguishes `enabled`, `disabled`, `not_applicable`, `unavailable`.
Section failures return `available=false` with a reason/errors; partial resource rows
remain visible. Vulkan includes native descriptor sets/layouts, dynamic offsets,
descriptor-buffer metadata, rasterizer, multisample and renderpass state. Other APIs
expose common bindings/state and explicitly mark unsupported native details.
Default filters hide definitely unused bindings and irrelevant empty slots, while
preserving missing-required and invalid-range diagnostics. `possibly_used` is not
proof of dynamic GPU access. Counts in overview include hidden bindings.

#### `inspect_pipeline_binding`

```python
rows = get_pipeline_stage(action_event_id=343, stage="FS", section="constant_buffers")
binding_id = rows["items"][0]["binding_id"]
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id)
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id, section="variables")
# Expand using child_path returned by the previous query.
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id,
                         section="variables", child_path=[0], offset=0, limit=50)
```

Arguments: `action_event_id`, `binding_id`, `section="details"|"variables"`,
`child_path=None`, `offset=0`, `limit=50`. Details do not decode variables.
Bindings retain stage, native set/space and binding, reflection index, array element,
shader declaration name and resource identity. Buffer ranges are effective byte
ranges; Vulkan dynamic offsets are already included and never added twice.
`constant_buffer_range_too_small` reports `required_bytes` and `provided_bytes`
(e.g. 720 vs 512), not a claim that execution performed an out-of-bounds read.
Direct constants do not require a buffer resource. `push_constants` includes
non-buffer-backed constant blocks; their reflected names describe the API-specific kind.
Variables expand one level with reflected layout, scalar/vector/matrix values and
integer child paths. Large structs/arrays stay paginated; binary buffer decoding
remains the responsibility of existing buffer tools.

`binding_id` is opaque and valid only for the current capture, action and binding
contents. Reloading even the same capture invalidates IDs. `binding_key` identifies
a semantic location for comparisons; it is not an inspector argument.
Use `resource.resource_id` for `inspect_resource`, `trace_resource_usage`, and
`get_resource_initialization`. Resource names are display/search values, not unique IDs.

#### `get_action_textures`

```python
get_action_textures(action_event_id=343, direction="all", offset=0, limit=50)
get_action_textures(action_event_id=343, direction="input", stage="FS")
get_action_textures(action_event_id=343, direction="output")
get_texture_data(action_event_id=343, resource_id="ResourceId::487", mip=0, slice_index=0)
save_texture(action_event_id=343, resource_id="ResourceId::487",
             output_path="D:/output/texture.png")
```

Arguments: `action_event_id`, `direction="all"|"input"|"output"`, optional `stage`,
`show_unused=False`, `show_empty=False`, `offset=0`, `limit=50`.
Returns one paginated list of bindings with stage labels (FS/FB etc.), declaration
names, capture resource identities, roles, dimensions/format and view subresources.
The same texture at different stages/slots/array elements remains separate.
Read-write images match both direction filters but occur once in `all`.
Framebuffer outputs describe bindings, not guaranteed writes. Depth/stencil write
state and available attachment-access information are reported separately.
Copy/resolve use explicit action source/destination subresources. Clear reports its
known target, with unavailable subresource detail marked explicitly. Other actions
never inherit stale shader bindings as their own texture inputs.

No image preview is generated. `get_texture_data` and `save_texture` accept optional
`action_event_id`: supplied means pixels **after** that action; omitted means the
current UI replay event. Responses include the event and `event_phase="after"`.
A texture marked input is still read at the requested after-action event, not a
historical snapshot of each shader access. Queries restore the UI replay event
on success and failure without changing the UI selection.

`inspect_action` now returns overview `pipeline`, unpaged `bindings` / `textures`
and `fixed_function`. `diff_actions` compares complete binding positions and ranges,
including buffers/samplers and fixed-function state, ignoring action-scoped tokens.
`get_shader_info` no longer returns constant values or resource binding collections.

Automated tests: `python -m unittest discover -s tests -v`.
After manually installing/reloading the updated extension, compare the live UI with
`python scripts/validate_pipeline_live.py --action-event-id 343 --stage FS`.
The script reads the already-open capture and does not export images or select a UI event.

---

#### `get_shader_info`

Get shader information for a specific stage at a given event. Includes shader identity, entry point and disassembly; bindings and constants are available through the pipeline tools.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID |
| `stage` | `str` | Yes | Shader stage: `"vertex"`, `"tess_control"`, `"tess_eval"`, `"geometry"`, `"fragment"`, `"compute"` |

**Returns:** Shader resource ID, entry point, stage and disassembly.

**Example:**
```
get_shader_info(event_id=123, stage="fragment")
```

---

#### `get_shader_source`

Get original shader source text for a specific stage at a given event when the capture preserves text-backed source.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event_id` | `int` | Yes | The event ID |
| `stage` | `str` | Yes | Shader stage: `"vertex"`, `"tess_control"`, `"tess_eval"`, `"geometry"`, `"fragment"`, `"compute"` |

**Returns:** Shader resource ID, entry point, stage, encoding, `source_available`, and `source_text` for text-backed encodings. For binary encodings such as DXBC/DXIL/SPIR-V, returns metadata plus a `reason` explaining why original source text is unavailable.

**Example:**
```
get_shader_source(event_id=123, stage="fragment")
# → {"resource_id": "ResourceId::42", "encoding": "GLSL", "source_available": true, "source_text": "..."}
```

---

#### `get_shader_edit_context`

Prepare editable GLSL/SPIR-V text and its compilation path for an event/stage. See [Session-scoped Shader Editing](#session-scoped-shader-editing) for the full edit/replace workflow.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `event_id` | `int` | Yes | | The event ID |
| `stage` | `str` | Yes | | Shader stage: `"vertex"`, `"tess_control"`, `"tess_eval"`, `"geometry"`, `"fragment"`, `"compute"` |
| `mode` | `str` | No | `"auto"` | Representation to prepare: `auto / original / glsl / spirv_asm` |

**Returns:** `edit_id`, `source_text`, `applied_source_text`, entry points, encodings, compiler, `revision`, `applied`, `last_attempt_status`, and `log`. Reuse `edit_id` with `replace_shader` / `revert_shader` / `export_shader_source`.

**Example:**
```
edit = get_shader_edit_context(event_id=123, stage="fragment", mode="auto")
# → {"edit_id": "...", "source_text": "...", "compiler": "...", "applied": false, ...}
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
| `action_event_id` | `int` | No | current UI event | Read after this exact action; restore replay afterwards |
| `mip` | `int` | No | `0` | Mip level to retrieve |
| `slice_index` | `int` | No | `0` | Array slice or cube face index (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-) |
| `sample` | `int` | No | `0` | MSAA sample index |
| `depth_slice` | `int` | No | | For 3D textures only, extract a specific depth slice. If omitted, returns full volume. |

**Returns:** Base64-encoded pixel data with metadata (dimensions, format).

**Examples:**
```
# Get mip 0 of a 2D texture
get_texture_data(action_event_id=123, resource_id="ResourceId::123")

# Get a specific mip level
get_texture_data(action_event_id=123, resource_id="ResourceId::123", mip=2)

# Get a specific face of a cubemap (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(action_event_id=123, resource_id="ResourceId::456", slice_index=3)

# Get a specific depth slice of a 3D texture
get_texture_data(action_event_id=123, resource_id="ResourceId::789", depth_slice=5)
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
| `action_event_id` | `int` | Yes | The event ID of the draw call |

**Returns:** Topology, vertex/index counts, whether indexed, vertex attributes with formats, bounding box.

**Example:**
```
get_mesh_summary(action_event_id=1234)
# → {"topology": "TriangleList", "num_vertices": 3024, "num_indices": 9072, "indexed": true,
#    "attributes": [{"name": "POSITION", "format": "R32G32B32_FLOAT", "components": 3}, ...],
#    "bounding_box": {"min": [-10.0, -5.0, -2.0], "max": [10.0, 5.0, 2.0]}}
```

---

#### `get_mesh_data`

Get mesh vertex and index data for a specific draw call with pagination support.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `action_event_id` | `int` | Yes | | The event ID |
| `stage` | `str` | No | `"VSIn"` | Mesh data stage: `"VSIn"` (input), `"VSOut"` (vertex shader output), `"GSOut"` (geometry output) |
| `offset` | `int` | No | `0` | Starting vertex offset for pagination |
| `limit` | `int` | No | `100` | Max vertices to return (recommended: 100-500) |
| `attributes` | `list[str]` | No | | Filter to specific attribute names (e.g. `["POSITION", "NORMAL"]`). If omitted, all attributes included. |

**Returns:** `items`, `indices`, `topology`, `attributes`, `total_count`, `has_more`, `truncated`.

**Examples:**
```
# First page
get_mesh_data(action_event_id=1234, offset=0, limit=100)

# Next page
get_mesh_data(action_event_id=1234, offset=100, limit=100)

# Filter specific attributes
get_mesh_data(action_event_id=1234, offset=0, limit=100, attributes=["POSITION", "NORMAL", "TEXCOORD"])
```

---

### Action Metadata

#### `get_action_api_calls`

Read the API Inspector data for a draw/dispatch action without changing the selected event.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `action_event_id` | `int` | Required | Exact action EID, not an intermediate state-setting API event |
| `api_event_id` | `int` | `None` | Omit to list calls; select an item's `api_event_id` to expand its parameters |
| `child_path` | `list[int]` | `[]` | Raw child-index path returned by a previous expansion |
| `offset` | `int` | `0` | Offset in calls or visible immediate children |
| `limit` | `int` | `50` | Page size, 1–500 |

The list preserves `ActionDescription.events` order and includes all associated calls through pagination: the events since the previous action, not every historical state-setting call. Returns `action_event_id`, `name`, and paginated `items` with `api_event_id`, `name`, `chunk_index`, `available`, and raw `child_count` when available.

Selecting `api_event_id` returns `api_call`, `node`, and paginated `children`. Parameter expansion shares the resource-initialization serializer: one level at a time, hidden children omitted, raw index paths preserved, resource IDs/names included, binary contents omitted, and text previews bounded to 4096 characters. Calls without structured chunks remain in the list with `available: false` and `reason: "no_chunk"` or `"invalid_chunk_index"`; selecting them returns `api_call` without a parameter tree. An API EID outside the requested action returns `INVALID_API_EVENT_ID`.

```python
get_action_api_calls(action_event_id=343)  # For example, API EIDs 340–343
get_action_api_calls(action_event_id=343, offset=50)  # Continue if has_more is true
get_action_api_calls(action_event_id=343, api_event_id=343)  # vkCmdDrawIndexed parameters
# Use a child_path returned above to expand a specific parameter:
get_action_api_calls(action_event_id=343, api_event_id=341, child_path=[0])
```

---

#### `get_action_details`

Get an action's metadata, draw counts, offsets and output resources.
For associated API calls and parameter trees, use `get_action_api_calls`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action_event_id` | `int` | Yes | The event ID of the action |

**Returns:** `action_event_id`, `action_id`, `name`, `flags`, draw counts (`num_indices`, `num_instances`), draw offsets, `outputs` and optional `depth_output`.
The response identifies the action with `action_event_id`; `action_id` is its separate action ordinal.

**Example:**
```
get_action_details(action_event_id=123)
```

---

#### `get_action_timings`

Get GPU timing information for actions.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `action_event_ids` | `list[int]` | No | | Specific event IDs. If omitted, returns all actions. |
| `marker_filter` | `str` | No | | Only include actions under markers containing this string |
| `exclude_markers` | `list[str]` | No | | Exclude actions under markers containing these strings |

**Returns:** `{"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}`

> **Note:** GPU timing counters may not be available on all hardware/drivers. If `available` is `false`, timing data cannot be retrieved.

**Examples:**
```
# All actions
get_action_timings()

# Specific event IDs
get_action_timings(action_event_ids=[100, 200, 300])

# Filter by marker
get_action_timings(marker_filter="Camera.Render", exclude_markers=["GUI.Repaint"])
```

---

### Composite Analysis

Cross-dimensional queries that orchestrate multiple services on top of atomic tools.

#### `inspect_action`

Inspect one action with a compact analysis-oriented bundle. Returns details, timing, shader summaries, pipeline summaries, and mesh summary when the event is a draw call.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action_event_id` | `int` | Yes | The event ID to inspect |

**Returns:** Event details, timing, shader summaries, pipeline summaries, mesh summary.

**Example:**
```
inspect_action(action_event_id=1517)
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
| `before_event_id` | `int` | No | | Compute the latest prior writer before this event |
| `categories` | `list[str]` | No | all | Timeline categories: `read`, `write`, `read_write`, `barrier`, `clear` |
| `offset` | `int` | No | `0` | Offset after filtering |
| `limit` | `int` | No | `100` | Page size, 1–500 |

**Returns:** `available`, compact `resource`, paginated `events`, pagination fields, roles, usage/read/write counts, and writer summaries. Counts and writers cover all matching records before pagination. `before_event_id` only affects the prior-writer summary. Each event retains raw `usage`, optional `view_resource_id`, marker context and inferred `access` (`access_source: "usage_classification"`). Unknown actions retain EID/usage unless marker filters require known context. Unsupported objects return an explicit unavailable reason; successful empty queries remain available. UI EID-range merging is not performed.

Each event includes `category`; `category_counts` always contains all five keys, including zeros, matching Timeline Reads / Writes / Read/Write / Barriers / Clears.

- `GenMips`, `Copy`, `Resolve` and shader RWResource usages are `read_write`.
- `Clear` and `Discard` are `clear`; `Barrier` is `barrier`.
- StreamOut, ColorTarget, DepthStencilTarget, CopyDst, ResolveDst and CPUWrite are `write`; all remaining usages follow Timeline's default `read` branch.

Selections in `categories` are ORed and combined with marker/event filters using AND. Omission selects all; `[]` selects none; invalid categories produce a parameter error. All counts, totals and writer summaries cover records **after all filters, before pagination**. Category counts measure usage records, not distinct EIDs or merged on-screen markers; multiple usages at one EID remain separate.

Original `usage` and `usage_counts` are retained. `access`, `read_count` and `write_count` describe dependency access semantics, independent of Timeline presentation: Clear still counts as a write and GenMips retains access=write. Use `category` and `category_counts` to match the panel.

Classification reference: [RenderDoc TimelineBar.cpp](https://github.com/baldurk/renderdoc/blob/v1.x/qrenderdoc/Windows/TimelineBar.cpp).

**Example:**
```
trace_resource_usage(resource_id="ResourceId::2495")
trace_resource_usage(resource_id="ResourceId::2495", categories=["barrier", "clear"], limit=50)
trace_resource_usage(resource_id="ResourceId::2495", marker_filter="Forward", before_event_id=1517)
```

---

#### `trace_action_dependencies`

Trace the immediate resource dependencies of one action.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action_event_id` | `int` | Yes | The event to inspect |

**Returns:** Stage-grouped input resources, input-assembly buffers, output resources, and likely producer events for major inputs.

**Example:**
```
trace_action_dependencies(action_event_id=1517)
```

---

#### `diff_actions`

Compare two actions and report material state differences.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action_event_id_a` | `int` | Yes | The first event ID |
| `action_event_id_b` | `int` | Yes | The second event ID |

**Returns:** Shader, resource binding, draw parameter, mesh, and timing differences.

**Example:**
```
diff_actions(action_event_id_a=100, action_event_id_b=200)
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
| `action_event_id` | `int` | No | current UI event | Read after this exact action; restore replay afterwards |
| `output_path` | `str` | Yes | | Output file path (e.g. `"D:/output/texture.png"`) |
| `format_type` | `str` | No | `"PNG"` | Output format: `"PNG"`, `"JPG"`, `"BMP"`, `"TGA"`, `"EXR"`, `"DDS"`, `"HDR"` |
| `mip` | `int` | No | `0` | Mip level to save (`-1` = all mips) |
| `slice_index` | `int` | No | `0` | Array slice or cube face index (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-) |
| `alpha_mode` | `str` | No | `"preserve"` | Alpha handling: `"preserve"`, `"discard"`, `"blend_to_black"` |

**Returns:** `{"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}`

**Examples:**
```
# Save as PNG
save_texture(action_event_id=123, resource_id="ResourceId::123", output_path="D:/output/texture.png")

# Save as JPG with alpha blending
save_texture(action_event_id=123, resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG", alpha_mode="blend_to_black")

# Export all mip levels as DDS
save_texture(action_event_id=123, resource_id="ResourceId::2495", output_path="D:/output/texture.dds", format_type="DDS", mip=-1)
```

---

#### `export_mesh_csv`

Export mesh data to a CSV file, compatible with the [csv_obj](https://github.com/nicbarker/csv_obj) project.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `action_event_id` | `int` | Yes | | The event ID of the draw call |
| `output_path` | `str` | Yes | | Output file path (e.g. `"D:/output/mesh.csv"`) |
| `stage` | `str` | No | `"VSIn"` | Mesh data stage: `"VSIn"`, `"VSOut"`, `"GSOut"` |
| `attributes` | `list[str]` | No | | Filter to specific attributes. If omitted, all attributes included. |

**Returns:** `{"success": true, "output_path": "D:/output/mesh.csv", "index_path": "D:/output/mesh.idx", "vertex_count": 3024, "index_count": 9072}`

**CSV format:**
- First row: `VTX,IDX,in_POSITION0.x,in_POSITION0.y,...`
- VTX: deduplicated vertex index
- IDX: original vertex index
- Index sidecar file (`.idx`): remapped triangle stream

**Example:**
```
export_mesh_csv(action_event_id=1234, output_path="D:/output/mesh.csv", stage="VSIn", attributes=["POSITION", "NORMAL", "TEXCOORD"])
```
