# RenderDoc MCP Server Enhanced

[English](README.md) | [日本語](README_ja.md) | [中文](README_zh.md)

> This is a fork of [RenderDocMCP](https://github.com/halby24/RenderDocMCP), focusing on cross-API compatibility (especially OpenGL scenes) and MCP tool interface design improvements.

RenderDoc MCP Enhanced enables AI assistants to perform more efficient graphics debugging, rendering analysis, and optimization suggestions based on RenderDoc capture data.

![img.png](docs/images/preview.png)

## Architecture

This project uses a process-separation architecture based on FastMCP 2.0.

`uv` registers the global command `renderdoc-mcp`. When AI clients (like Claude) detect this MCP command, they will start the MCP Server.

The MCP Server communicates with the AI client via stdio, and forwards requests to the extension running in RenderDoc's built-in Python 3.6 environment via file-based IPC.

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

### System Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+
- Windows

> **Note**: Currently only tested on Windows environment.
> The architecture may theoretically work on Linux, but this has not been tested or adapted yet.

### 1. Install RenderDoc Extension

After cloning this repository, run in the project root:
```bash
python scripts/install_extension.py
```
The extension will be installed to `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge`.

### 2. Enable Extension in RenderDoc

1. Launch RenderDoc
2. Tools > Manage Extensions
3. Enable "RenderDoc MCP Bridge"

### 3. Install MCP Server

Run in the project root:
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

#### Claude Code / Other MCP-compatible clients

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

You can also open Claude Code directly in this project directory. Claude Code will automatically detect `.mcp.json` and register the MCP server for the current session.

Using project-level configuration is generally recommended to avoid global MCP settings affecting other workspace contexts.

![claudeprojectmcp.gif](docs/images/claudeprojectmcp.gif)

## Usage

1. Launch RenderDoc and open a capture file (.rdc)
2. Access RenderDoc data from your MCP client (Claude, etc.)

## Design Philosophy

This project focuses on optimizing the MCP tool interface organization, naming consistency, and calling experience on top of the original implementation.

The goal is to cover higher-frequency RenderDoc analysis needs with fewer, more stable, and more composable interfaces, making it easier for AI to perform chained calls.

#### Canonicalization

Similar capabilities are consolidated into a unified entry point rather than being split into multiple semantically similar MCP commands.

For example, multiple draw search interfaces are merged into `search_draws`, resource enumeration is unified as `list_resources`, and specific types and query dimensions are distinguished through parameters.

#### Shape Consistency

Different tools should follow consistent parameter styles and return structures rather than each defining its own format.

For example, paginated results uniformly use `items / total_count / offset / limit`, and search results uniformly use `matches / total_matches / scanned_count`.

#### Progressive Disclosure

The entire MCP toolset is organized into three capability tiers:

- **Global Operations**: Navigation, targeting, and global summaries for capture / frame / resource space — answering "what should I look at, how big is the scope, where do I start".
- **Local Data Analysis**: Deep analysis of specific events, shaders, textures, buffers, and meshes — answering "what happened at this specific point".
- **Upper-level Tools**: Export, save, and downstream workflow capabilities — answering "how do I reuse this, I want to see the resource".

![img.png](docs/images/organization.png)

## MCP Tools

### Global Operations

- `open_capture` - Open a capture file directly from the MCP client
- `list_captures` - List `.rdc` files in a directory
- `get_capture_status` - Check capture loading status
- `get_frame_summary` - Get frame-wide statistics and top-level marker summaries
- `get_draw_calls` - Get draw call / action hierarchy with filtering
- `search_draws` - Unified search for draw calls by shader, texture, or resource
- `list_resources` - List textures or buffers with one paginated interface

### Local Data Analysis

- `get_draw_call_details` - Get detailed information about a specific draw call
- `get_action_timings` - Get GPU timings for actions
- `get_shader_info` - Get shader disassembly, constant buffers, and bindings
- `get_pipeline_state` - Get full pipeline state with concise input/output texture summaries
- `get_texture_info` - Get texture metadata
- `get_texture_data` - Get texture pixel data (Base64)
- `get_buffer_contents` - Get buffer contents (Base64)
- `get_mesh_summary` - Get mesh topology, counts, attributes, and bounds
- `get_mesh_data` - Get paginated mesh data

### Upper-level Tools

- `save_texture` - Save texture to image file (PNG/JPG/BMP/TGA/EXR/DDS/HDR)
- `export_mesh_csv` - Export mesh CSV for downstream workflows

## Examples

### Recommended Workflow

A typical analysis workflow is usually:

`get_capture_status` / `get_frame_summary` → `get_draw_calls` / `search_draws` → `get_pipeline_state` / `get_shader_info` / `get_mesh_data`

### Search draw calls globally

```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

### List resources uniformly

```
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)
```

### Get draw calls

```
get_draw_calls(include_children=true)
```

### Get shader info

```
get_shader_info(event_id=123, stage="pixel")
```

### Get pipeline state

```
get_pipeline_state(event_id=123)
```

The response includes concise `input_textures` / `output_textures` summaries.

### Get mesh data with canonical paging

```
get_mesh_data(event_id=1234, offset=0, limit=100)
get_mesh_data(event_id=1234, offset=100, limit=100)
```

### Get texture data

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

### Partial buffer data retrieval

```
# Get entire buffer
get_buffer_contents(resource_id="ResourceId::123")

# Get 512 bytes from offset 256
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

### Save texture to file

```
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG")
```

## TODO

The current version focuses on tool interface simplification, interface canonicalization, cross-API compatibility enhancements, and extension adaptation under RenderDoc's Python 3.6 environment.

Future work will continue to clean up compatibility layer tools based on testing results, and gradually add higher-level analysis capabilities (current plan is to build upper-level tools for model assembly). Adding hot-reload module.

## License

MIT
