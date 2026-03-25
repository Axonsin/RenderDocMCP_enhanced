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

| Tool | Description |
|------|-------------|
| `get_capture_status` | Check capture loading status |
| `get_draw_calls` | Get draw call list with hierarchical structure |
| `get_draw_call_details` | Get details of a specific draw call |
| `get_shader_info` | Get shader source code and constant buffer values |
| `get_buffer_contents` | Get buffer contents (Base64) |
| `get_texture_info` | Get texture metadata |
| `get_texture_data` | Get texture pixel data (Base64) |
| `get_pipeline_state` | Get pipeline state |

## Examples

### Get Draw Calls

```
get_draw_calls(include_children=true)
```

### Get Shader Info

```
get_shader_info(event_id=123, stage="pixel")
```

### Get Pipeline State

```
get_pipeline_state(event_id=123)
```

### Get Texture Data

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

### Partial Buffer Data Retrieval

```
# Get entire buffer
get_buffer_contents(resource_id="ResourceId::123")

# Get 512 bytes from offset 256
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+

> **Note**: Tested only on Windows + DirectX 11 environment.
> It may work on Linux/macOS + Vulkan/OpenGL environments, but this is unverified.

## License

MIT
