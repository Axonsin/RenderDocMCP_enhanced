# RenderDoc MCP Server

[日本語](README_ja.md) | [中文](README_zh.md)

An MCP server that runs as a RenderDoc UI extension. It enables AI assistants to access RenderDoc capture data and assist with DirectX 11/12 graphics debugging.

## Architecture

```
Claude/AI Client (stdio)
        │
        ▼
MCP Server Process (Python + FastMCP 2.0)
        │ File-based IPC (%TEMP%/renderdoc_mcp/)
        ▼
RenderDoc Process (Extension)
```

Since the built-in Python in RenderDoc does not have the socket module, file-based IPC is used for communication.

## Setup

### 1. Install RenderDoc Extension

```bash
python scripts/install_extension.py
```

The extension will be installed to `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge`.

### 2. Enable Extension in RenderDoc

1. Launch RenderDoc
2. Tools > Manage Extensions
3. Enable "RenderDoc MCP Bridge"

### 3. Install MCP Server

```bash
uv tool install . # Install from current directory
uv tool update-shell  # Add renderdoc-mcp command to PATH
```

After restarting your shell, the `renderdoc-mcp` command will be available.

> **Note**: Use `--editable` to reflect source code changes immediately (useful for development).
> For a stable installation, use `uv tool install .`.

### 4. Configure MCP Client

#### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

#### Claude Code

Add to `.mcp.json`:

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

>You can also open shell to wake Claude Code in this root-dir. Claude Code will automatically detect `.mcp.json` and register the MCP server (in this session).

## Usage

1. Launch RenderDoc and open a capture file (.rdc)
2. Access RenderDoc data from your MCP client (Claude, etc.)

## MCP Tools

### Core inspection

- `get_capture_status` - Check capture loading status
- `get_draw_calls` - Get draw call/action hierarchy with filters
- `get_frame_summary` - Get frame-wide statistics and top-level markers
- `get_draw_call_details` - Get details of a specific draw call
- `get_action_timings` - Get GPU timings for actions
- `get_shader_info` - Get shader disassembly, constant buffers, and bindings
- `get_pipeline_state` - Get detailed pipeline state plus concise input/output texture summaries
- `get_mesh_summary` - Get mesh topology, counts, attributes, and bounds
- `get_mesh_data` - Get paginated mesh data

### Canonical search and resource tools

- `search_draws` - Search draw calls by shader, texture, or resource usage
- `list_resources` - List textures or buffers with one paginated interface
- `get_texture_info` - Get texture metadata
- `get_texture_data` - Get texture pixel data (Base64)
- `get_buffer_contents` - Get buffer contents (Base64)
- `save_texture` - Save texture to image file (PNG/JPG/BMP/TGA/EXR/DDS/HDR)

### Workflow and advanced tools

- `open_capture` - Open a capture file from the MCP client
- `list_captures` - List `.rdc` files in a directory
- `export_mesh_csv` - Export mesh data for downstream workflows

### Compatibility aliases

These legacy tools still work during migration, but new prompts and examples should prefer the canonical tools above:

- `find_draws_by_shader`
- `find_draws_by_texture`
- `find_draws_by_resource`
- `list_textures`
- `list_buffers`
- `get_event_textures`

## Examples

### Search draw calls by shader/texture/resource

```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

### List textures or buffers

```
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)
```

### Get draw calls

```
get_draw_calls(include_children=true)
```

### Get Shader Info

```
get_shader_info(event_id=123, stage="pixel")
```

### Get pipeline state

```
get_pipeline_state(event_id=123)
```

The response now includes concise `input_textures` and `output_textures` summaries, so most prompts no longer need to call `get_event_textures`.

### Get mesh data with canonical paging

```
get_mesh_data(event_id=1234, offset=0, limit=100)
get_mesh_data(event_id=1234, offset=100, limit=100)
```

### Get texture data

```
get_texture_data(resource_id="ResourceId::123")
get_texture_data(resource_id="ResourceId::123", mip=2)
get_texture_data(resource_id="ResourceId::456", slice=3)
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

### Partial buffer data retrieval

```
get_buffer_contents(resource_id="ResourceId::123")
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

### Save texture to file

```
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG")
```

## Migration notes

- Prefer `search_draws(...)` over `find_draws_by_*`.
- Prefer `list_resources(...)` over `list_textures(...)` and `list_buffers(...)`.
- Prefer `offset` / `limit` for mesh pagination; `start_offset` / `max_vertices` remain accepted for compatibility.
- Prefer `get_pipeline_state(...)` when you need concise read/write texture summaries.

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+

> **Note**: Tested only on Windows + DirectX 11 environment.
> It may work on Linux/macOS + Vulkan/OpenGL environments, but this is unverified.

## License

MIT
