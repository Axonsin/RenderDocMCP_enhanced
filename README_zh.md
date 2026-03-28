# RenderDoc MCP Server

[English](README.md) | [日本語](README_ja.md)

作为 RenderDoc UI 扩展运行的 MCP 服务器。它使 AI 助手能够访问 RenderDoc 捕获数据，并协助 DirectX 11/12 图形调试。

## 架构

```
Claude/AI Client (stdio)
        │
        ▼
MCP Server Process (Python + FastMCP 2.0)
        │ File-based IPC (%TEMP%/renderdoc_mcp/)
        ▼
RenderDoc Process (Extension)
```

由于 RenderDoc 内置的 Python 没有 socket 模块，因此使用基于文件的 IPC 进行通信。

## 安装设置

### 1. 安装 RenderDoc 扩展

```bash
python scripts/install_extension.py
```

扩展将安装到 `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge`。

### 2. 在 RenderDoc 中启用扩展

1. 启动 RenderDoc
2. Tools > Manage Extensions
3. 启用 "RenderDoc MCP Bridge"

### 3. 安装 MCP 服务器

```bash
uv tool install . # 从当前目录安装
uv tool update-shell  # 把renderdoc-mcp添加到 PATH
```

重启终端后，`renderdoc-mcp` 命令将可用。

> **注意**: 使用 `--editable` 可以使源代码更改立即生效（开发时很有用）。
> 如需稳定版安装，请使用 `uv tool install .`。

### 4. 配置 MCP 客户端

#### Claude Desktop

添加到 `claude_desktop_config.json`:

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

添加到 `.mcp.json`:

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```
>还可以让Claude Code在此目录下打开(在这个目录下打开终端 -> claude command)。Claude Code将自动检测“.mcp.json”并注册mcp服务器（在此会话中）。


## 使用方法

1. 启动 RenderDoc 并打开捕获文件 (.rdc)
2. 从 MCP 客户端（如 Claude）访问 RenderDoc 数据

## MCP 工具列表

### 核心分析工具

- `get_capture_status` - 检查捕获加载状态
- `get_draw_calls` - 获取 draw call / action 层级并支持过滤
- `get_frame_summary` - 获取整帧统计与顶层 marker 摘要
- `get_draw_call_details` - 获取特定 draw call 的详细信息
- `get_action_timings` - 获取 action 的 GPU 时间
- `get_shader_info` - 获取 shader 反汇编、常量缓冲区和绑定信息
- `get_pipeline_state` - 获取完整管线状态，并附带精简的输入/输出纹理摘要
- `get_mesh_summary` - 获取网格拓扑、数量、属性和包围盒
- `get_mesh_data` - 分页获取网格数据

### Canonical 搜索与资源工具

- `search_draws` - 按 shader、texture、resource 统一搜索 draw call
- `list_resources` - 用一个分页接口列出 texture 或 buffer
- `get_texture_info` - 获取纹理元数据
- `get_texture_data` - 获取纹理像素数据 (Base64)
- `get_buffer_contents` - 获取缓冲区内容 (Base64)
- `save_texture` - 保存纹理到图片文件 (PNG/JPG/BMP/TGA/EXR/DDS/HDR)

### 工作流 / 高级工具

- `open_capture` - 从 MCP 客户端直接打开捕获文件
- `list_captures` - 列出目录中的 `.rdc` 文件
- `export_mesh_csv` - 为下游工作流导出网格 CSV

## 使用示例

### 统一搜索 draw call

```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

### 统一列出资源

```
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)
```

### 获取绘制调用列表

```
get_draw_calls(include_children=true)
```

### 获取着色器信息

```
get_shader_info(event_id=123, stage="pixel")
```

### 获取管线状态

```
get_pipeline_state(event_id=123)
```

`get_pipeline_state` 的返回中包含精简版的 `input_textures` / `output_textures` 摘要。

### 按 canonical 分页获取网格数据

```
get_mesh_data(event_id=1234, offset=0, limit=100)
get_mesh_data(event_id=1234, offset=100, limit=100)
```

### 获取纹理数据

```
# 获取 2D 纹理的 mip 0
get_texture_data(resource_id="ResourceId::123")

# 获取特定的 mip 级别
get_texture_data(resource_id="ResourceId::123", mip=2)

# 获取立方体贴图的特定面 (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(resource_id="ResourceId::456", slice=3)

# 获取 3D 纹理的特定深度切片
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

### 部分缓冲区数据获取

```
# 获取整个缓冲区
get_buffer_contents(resource_id="ResourceId::123")

# 从偏移量 256 获取 512 字节
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

### 保存纹理到文件

```
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG")
```

## 系统要求

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+

> **注意**: 仅在 Windows + DirectX 11 环境下测试过。
> 可能在 Linux/macOS + Vulkan/OpenGL 环境下也能工作，但未经测试验证。

## 许可证

MIT
