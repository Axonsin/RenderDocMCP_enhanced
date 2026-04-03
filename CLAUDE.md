# RenderDoc MCP Server

作为 RenderDoc UI 扩展运行的 MCP 服务器。帮助 AI 助手访问 RenderDoc 的捕获数据，辅助 DirectX 11/12 图形调试。

## 架构

**混合进程分离方式**:

```
Claude/AI Client (stdio)
        │
        ▼
MCP Server Process (标准 Python + FastMCP 2.0)
        │ File-based IPC (%TEMP%/renderdoc_mcp/)
        ▼
RenderDoc Process (Extension + File Polling)
```

## 项目结构

```
RenderDocMCP/
├── mcp_server/                        # MCP 服务器
│   ├── server.py                      # FastMCP 入口点
│   ├── config.py                      # 配置
│   └── bridge/
│       └── client.py                  # 基于文件的 IPC 客户端
│
├── renderdoc_extension/               # RenderDoc 扩展
│   ├── __init__.py                    # register()/unregister()
│   ├── extension.json                 # 清单文件
│   ├── socket_server.py               # 基于文件的 IPC 服务器
│   ├── request_handler.py             # 请求处理
│   ├── renderdoc_facade.py            # RenderDoc API 封装
│   └── services/
│       ├── mesh_service.py            # 网格数据处理服务
│
└── scripts/
    └── install_extension.py           # 扩展安装脚本
```

## MCP 工具

| 工具名 | 说明 |
|---------|------|
| `list_captures` | 获取指定目录内的 .rdc 文件列表 |
| `open_capture` | 打开捕获文件（现有捕获会自动关闭） |
| `get_capture_status` | 确认捕获加载状态 |
| `get_draw_calls` | Draw call 列表（支持层级结构、过滤） |
| `get_frame_summary` | 帧整体统计信息（draw call 数量、标记列表等） |
| `search_draws` | 按 shader/texture/resource 搜索 draw call |
| `get_draw_call_details` | 特定 draw call 的详情 |
| `get_action_timings` | 获取 action 的 GPU 执行时间 |
| `get_shader_info` | 着色器反汇编/常量缓冲区/资源绑定 |
| `get_shader_source` | 获取 RenderDoc Edit/View 可见的原始 shader 源码（文本编码时） |
| `get_buffer_contents` | 缓冲区数据获取（支持偏移/长度指定） |
| `list_resources` | 资源枚举（texture/buffer，支持名称过滤和分页） |
| `get_texture_info` | 纹理元数据 |
| `get_texture_data` | 纹理像素数据获取（支持 mip/slice/3D 切片） |
| `save_texture` | 将纹理保存为图片文件（支持 PNG/JPG/BMP/TGA/EXR/DDS/HDR） |
| `get_pipeline_state` | 管线状态（含 `input_textures`/`output_textures` 摘要） |
| `get_mesh_summary` | 获取网格概要信息（拓扑、顶点数、属性、包围盒） |
| `get_mesh_data` | 获取网格顶点/索引数据（支持 VSIn/VSOut/GSOut 阶段） |
| `export_mesh_csv` | 将网格导出为 CSV 文件 |

更多, 请参考docs内的markdown API.

## MCP 服务器启动

通过 FastMCP 框架实现，启动流程：

1. **入口点定义**：`pyproject.toml` 中定义命令行入口
2. **执行 main()**：运行 `renderdoc-mcp` 命令时调用 `mcp.run()`. renderdoc-mcp已被uv注册为命令
3. **通信机制**：
   - 与 MCP 客户端（Claude）：通过 stdio 通信
   - 与 RenderDoc 扩展：通过文件 IPC（`%TEMP%/renderdoc_mcp/`）

**使用方式**：

```bash
# 安装后直接运行
renderdoc-mcp
```

在 Claude Code 配置中添加：
```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

**启动顺序**：
1. 先启动 RenderDoc（扩展自动加载）
2. MCP 服务器由 Claude 客户端自动启动.

## 通信协议

基于文件的 IPC:
- IPC 目录: `%TEMP%/renderdoc_mcp/`
- `request.json`: 请求（MCP 服务器 → RenderDoc）
- `response.json`: 响应（RenderDoc → MCP 服务器）
- `lock`: 写入中的锁文件
- 轮询间隔: 100ms（RenderDoc 端）

## 开发注意事项

- RenderDoc 内置 Python 没有 socket/QtNetwork 模块，因此采用基于文件的 IPC
- RenderDoc 扩展仅使用 Python 3.6 标准库, 注意混合版本. 语法必须兼容3.6.
- 开发过程 MUST 使用uv tool install . --editable 进行覆盖安装以更新MCP服务器, MUST带有`--editable`后缀
- 对 ReplayController 的访问通过 `BlockInvoke` 进行

## 参考链接

- [FastMCP](https://github.com/jlowin/fastmcp)
- [RenderDoc Python API](https://renderdoc.org/docs/python_api/index.html)
- [RenderDoc Extension Registration](https://renderdoc.org/docs/how/how_python_extension.html)
