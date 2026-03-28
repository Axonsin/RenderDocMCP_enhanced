# RenderDoc MCP Server Enhanced

[English](README.md) | [日本語](README_ja.md) | [中文](README_zh.md)

> 这是一个基于 [RenderDocMCP](https://github.com/halby24/RenderDocMCP) 的 fork，重点优化了跨 API 兼容性（尤其是 OpenGL 场景）以及 MCP 工具面的设计与调用。

RenderDoc MCP Enhanced 允许 AI 助手基于 RenderDoc 捕获数据进行更高效的图形调试、渲染分析与优化建议生成。
![img.png](docs/images/preview.png)

## 架构

本项目采用基于 FastMCP 2.0 的进程分离架构。

`uv` 负责注册全局命令 `renderdoc-mcp`，AI 客户端（如 Claude）在检测到该 MCP 命令后将会启动 MCP Server。

MCP Server 通过 stdio 与 AI 客户端通信，并通过文件 IPC 将请求转发给运行在 RenderDoc 内置 Python 3.6 环境中的扩展。

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

### 系统环境要求

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+
- Windows

> **注意**：当前仅在 Windows 环境下完成验证。
> 理论上该架构也可能适用于 Linux，但目前尚未进行测试与适配验证。

### 1. 安装 RenderDoc 扩展
克隆本仓库后，在项目根目录执行：
```bash
python scripts/install_extension.py
```
执行该脚本后，扩展会被安装到 `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge`。

### 2. 在 RenderDoc 中启用扩展

1. 启动 RenderDoc
2. Tools > Manage Extensions
3. 启用 "RenderDoc MCP Bridge"

### 3. 安装 MCP 服务器
在项目根目录执行：
```bash
uv tool install . # 从当前目录安装
uv tool update-shell  # 将 renderdoc-mcp 添加到 PATH
```
重启终端后，`renderdoc-mcp` 命令将可用。

> **注意**：使用 `--editable` 可以让源码修改立即生效，适合开发调试场景。
> 对于常规使用场景，执行 `uv tool install .` 即可。

### 4. 配置 MCP 客户端

也可以直接在本项目目录下启动 Claude Code。Claude Code 会自动检测 `.mcp.json` 并在当前会话中注册该 MCP 服务器。

一般更推荐使用项目级配置，以避免全局 MCP 配置影响其他工作区的上下文环境。
![claudeprojectmcp.gif](docs/images/claudeprojectmcp.gif)

#### Claude Desktop（全局配置）

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

#### Claude Code / 其他兼容 MCP 的客户端（全局配置）

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


## 使用方法

1. 启动 RenderDoc 并打开捕获文件 (.rdc)
2. 从 MCP 客户端（如 Claude）访问 RenderDoc 数据

## 设计理念

本项目在原始实现基础上，重点优化了 MCP 工具面的组织方式、命名一致性与调用体验。

目标是以更少、更稳定、更易组合的接口，覆盖更高频的 RenderDoc 分析需求，并让 AI 更容易进行链式调用。

#### Canonicalization
同类能力尽量收敛为统一入口，而不是拆分为多个语义相近的 MCP 命令。

例如，将多个 draw 搜索接口合并为 `search_draws`，将资源枚举统一为 `list_resources`，并通过参数区分具体类型与查询维度。

#### Shape Consistency
不同工具应尽量遵循一致的参数风格与返回结构，而不是各自定义一套形态。

例如，分页结果统一采用 `items / total_count / offset / limit`，搜索结果统一采用 `matches / total_matches / scanned_count`。

#### Progressive Disclosure
整套 MCP 工具按照以下三层能力组织：

- **全局操作能力**：面向 capture / frame / resource space 的导航、定位与全局摘要，用于回答“当前应看什么、范围有多大、从哪里入手”。
- **局部数据分析能力**：面向具体 event、shader、texture、buffer、mesh 的深入分析，用于回答“某个具体点上发生了什么”。
- **上层工具能力**：面向导出、保存与下游处理等工作流能力，用于回答“如何复用, 我要看到资源”。
![img.png](docs/images/organization.png)

## 所有 MCP 工具

### 全局操作能力

- `open_capture` - 从 MCP 客户端直接打开捕获文件
- `list_captures` - 列出目录中的 `.rdc` 文件
- `get_capture_status` - 检查捕获加载状态
- `get_frame_summary` - 获取整帧统计与顶层 marker 摘要
- `get_draw_calls` - 获取 draw call / action 层级并支持过滤
- `search_draws` - 按 shader、texture、resource 统一搜索 draw call
- `list_resources` - 用一个分页接口列出 texture 或 buffer

### 局部数据分析能力

- `get_draw_call_details` - 获取特定 draw call 的详细信息
- `get_action_timings` - 获取 action 的 GPU 时间
- `get_shader_info` - 获取 shader 反汇编、常量缓冲区和绑定信息
- `get_pipeline_state` - 获取完整管线状态，并附带精简的输入/输出纹理摘要
- `get_texture_info` - 获取纹理元数据
- `get_texture_data` - 获取纹理像素数据（Base64）
- `get_buffer_contents` - 获取缓冲区内容（Base64）
- `get_mesh_summary` - 获取网格拓扑、数量、属性和包围盒
- `get_mesh_data` - 分页获取网格数据

### 上层工具能力

- `save_texture` - 保存纹理到图片文件（PNG/JPG/BMP/TGA/EXR/DDS/HDR）
- `export_mesh_csv` - 为下游工作流导出网格 CSV

## 使用以及方法调用示例

### 推荐流程

一个典型的分析流程通常是：

`get_capture_status` / `get_frame_summary` → `get_draw_calls` / `search_draws` → `get_pipeline_state` / `get_shader_info` / `get_mesh_data`

### 全局搜索 draw call

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

`get_pipeline_state` 的返回中也包含精简的 `input_textures` / `output_textures` 摘要。

### 使用 Canonical 分页获取网格数据

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


## TODO

当前版本重点完成了工具面精简、接口 canonical 化、跨 API 兼容性增强，以及 RenderDoc Python 3.6 环境下的扩展适配。

后续将根据测试结果继续清理兼容层工具，并逐步添加更高层的分析能力(目前的计划是组装模型相关的上层工具). 补上热更模块.

## 许可证

MIT
