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
| `find_draws_by_shader` | 按着色器名称反向搜索 draw call |
| `find_draws_by_texture` | 按纹理名称反向搜索 draw call |
| `find_draws_by_resource` | 按资源 ID 反向搜索 draw call |
| `get_draw_call_details` | 特定 draw call 的详情 |
| `get_action_timings` | 获取 action 的 GPU 执行时间 |
| `get_shader_info` | 着色器源码/常量缓冲区 |
| `get_buffer_contents` | 缓冲区数据获取（支持偏移/长度指定） |
| `get_texture_info` | 纹理元数据 |
| `get_texture_data` | 纹理像素数据获取（支持 mip/slice/3D 切片） |
| `save_texture` | 将纹理保存为图片文件（支持 PNG/JPG/BMP/TGA/EXR/DDS/HDR） |
| `get_pipeline_state` | 管线状态整体 |
| `get_mesh_summary` | 获取网格概要信息（拓扑、顶点数、属性、包围盒） |
| `get_mesh_data` | 获取网格顶点/索引数据（支持 VSIn/VSOut/GSOut 阶段） |
| `export_mesh_csv` | 将网格导出为 CSV 文件 |

### get_draw_calls 过滤选项

```python
get_draw_calls(
    include_children=True,      # 包含子 action
    marker_filter="Camera.Render",  # 仅获取此标记下的内容
    exclude_markers=["GUI.Repaint", "UIR.DrawChain"],  # 排除的标记
    event_id_min=7372,          # event_id 范围起始
    event_id_max=7600,          # event_id 范围结束
    only_actions=True,          # 排除标记（仅 draw call）
    flags_filter=["Drawcall", "Dispatch"],  # 仅特定标志
)
```

### 捕获管理工具

```python
# 列举目录内的捕获文件
list_captures(directory="D:\\captures")
# → {"count": 3, "captures": [{"filename": "game.rdc", "path": "...", "size_bytes": 12345, "modified_time": "..."}, ...]}

# 打开捕获文件（现有捕获会自动关闭）
open_capture(capture_path="D:\\captures\\game.rdc")
# → {"success": true, "filename": "game.rdc", "api": "D3D11"}
```

### 反向搜索工具

```python
# 按着色器名搜索（部分匹配）
find_draws_by_shader(shader_name="Toon", stage="pixel")

# 按纹理名搜索（部分匹配）
find_draws_by_texture(texture_name="CharacterSkin")

# 按资源 ID 搜索（完全匹配）
find_draws_by_resource(resource_id="ResourceId::12345")
```

### GPU 时间获取

```python
# 获取所有 action 的时间
get_action_timings()
# → {"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}

# 仅获取特定事件 ID
get_action_timings(event_ids=[100, 200, 300])

# 按标记过滤
get_action_timings(marker_filter="Camera.Render", exclude_markers=["GUI.Repaint"])
```

**注意**: GPU 时间计数器在某些硬件/驱动上可能不可用。
如果返回 `available: false`，则该捕获无法获取时间信息。

### 纹理导出

```python
# 将纹理保存为 PNG 文件
save_texture(
    resource_id="ResourceId::2495",
    output_path="D:/output/texture.png"
)
# → {"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}

# 指定格式和选项
save_texture(
    resource_id="ResourceId::2495",
    output_path="D:/output/texture.exr",
    format_type="EXR",           # PNG, JPG, BMP, TGA, EXR, DDS, HDR
    mip=-1,                      # -1 表示导出所有 mip 级别
    slice_index=0,               # 数组切片或立方体面索引
    alpha_mode="blend_to_black"  # preserve, discard, blend_to_black
)

# 立方体贴图面索引: 0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-
```

**注意**: 这是推荐的纹理保存方式，会自动处理格式转换。

### 网格数据工具

```python
# 获取网格概要信息
get_mesh_summary(event_id=1234)
# → {
#     "event_id": 1234,
#     "topology": "TriangleList",
#     "num_vertices": 3024,
#     "num_indices": 9072,
#     "indexed": true,
#     "attributes": [
#         {"name": "POSITION", "format": "R32G32B32_FLOAT", "components": 3},
#         {"name": "NORMAL", "format": "R32G32B32_FLOAT", "components": 3}
#     ],
#     "bounding_box": {"min": [-10.0, -5.0, -2.0], "max": [10.0, 5.0, 2.0]}
# }

# 获取网格顶点和索引数据（分页方式）
# 建议：每次获取 100-500 顶点，避免数据过大
get_mesh_data(
    event_id=1234,
    stage="VSIn",           # VSIn, VSOut, GSOut
    start_offset=0,         # 起始偏移量（分页）
    max_vertices=100,       # 每次获取的顶点数（建议 100-500）
    attributes=["POSITION", "NORMAL", "TEXCOORD"]  # 可选，过滤属性
)
# → {
#     "vertices": [
#         {"POSITION": [1.0, 2.0, 3.0], "NORMAL": [0.0, 1.0, 0.0], "TEXCOORD": [0.5, 0.5]},
#         ...
#     ],
#     "indices": [0, 1, 2, 3, 4, 5, ...],
#     "topology": "TriangleList",
#     "total_count": 3024,      # 总顶点数
#     "start_offset": 0,        # 当前偏移
#     "has_more": true,         # 是否有更多数据
#     "truncated": false
# }

# 分页获取下一批数据
get_mesh_data(event_id=1234, start_offset=100, max_vertices=100)

# 导出网格为 CSV 文件（与 csv_obj 项目兼容）
export_mesh_csv(
    event_id=1234,
    output_path="D:/output/mesh.csv",
    stage="VSIn",
    include_attributes=["POSITION", "NORMAL", "TEXCOORD"]  # 可选
)
# → {
#     "success": true,
#     "output_path": "D:/output/mesh.csv",
#     "index_path": "D:/output/mesh.idx",
#     "vertex_count": 3024,
#     "index_count": 9072
# }
```

**数据阶段说明**：
- `VSIn`: 顶点着色器输入（原始顶点缓冲区数据）
- `VSOut`: 顶点着色器输出（变换后的顶点数据）
- `GSOut`: 几何着色器输出

**分页说明**：
- 使用 `start_offset` 和 `max_vertices` 进行分页
- `total_count` 表示总顶点数
- `has_more` 表示是否还有更多数据
- 建议每次获取 100-500 顶点

**CSV 格式说明**：
- 第一行为表头：`VTX,IDX,in_POSITION0.x,in_POSITION0.y,...`
- VTX: 去重后的顶点索引
- IDX: 原始顶点索引
- 属性命名格式：`in_{语义名}{语义索引}.{分量}`
- 索引 sidecar 文件（.idx）：每行一个重映射后的顶点索引

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
- RenderDoc 扩展仅使用 Python 3.6 标准库
- 对 ReplayController 的访问通过 `BlockInvoke` 进行

## 参考链接

- [FastMCP](https://github.com/jlowin/fastmcp)
- [RenderDoc Python API](https://renderdoc.org/docs/python_api/index.html)
- [RenderDoc Extension Registration](https://renderdoc.org/docs/how/how_python_extension.html)
