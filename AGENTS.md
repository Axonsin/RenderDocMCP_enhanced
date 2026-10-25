# RenderDoc MCP Server

版本 2.0.0，最低 RenderDoc 1.46。服务器/扩展 API 契约均为 2。迁移见 docs/migration_v2.md。

作为 RenderDoc UI 扩展运行的 MCP 服务器。帮助 AI 助手访问 RenderDoc 的捕获数据，辅助 DirectX 11/12 图形调试。

## 架构

**混合进程分离方式**:

```
Codex/AI Client (stdio)
        │
        ▼
MCP Server Process (标准 Python + FastMCP 3.x)
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

术语统一：action 的 EID 用 `action_event_id`（列表/范围用 `action_event_ids` /
`action_event_id_range`），独立 action 序号用 `action_id`，关联 API event 的 EID 用
`api_event_id`。shader 状态查询、原始 usage 及隐式 UI replay 位置保留通用 `event_id`。
shader 阶段统一返回 `fragment` / `tess_control` / `tess_eval` 等名称，接受 pixel/PS/FS、
hull/HS、domain/DS 等别名；网格 VSIn/VSOut/GSOut 表示不同的数据位置。
纹理数组层/立方体面用 `slice_index`；网格读取/导出的属性筛选用 `attributes`。
完整字段规则及破坏性改名见 docs/tools_zh.md 的“术语与字段约定”。

| 工具名 | 说明 |
|---------|------|
| `list_captures` | 获取指定目录内的 .rdc 文件列表 |
| `open_capture` | 打开捕获文件（现有捕获会自动关闭） |
| `get_capture_status` | 确认捕获加载状态、版本/协议与回放健康 |
| `get_actions` | action 列表（含 marker/draw/dispatch/copy/clear，支持层级与过滤） |
| `get_frame_summary` | 帧整体统计信息（draw call 数量、标记列表等） |
| `search_actions` | 按 shader/texture/resource 搜索 draw 和 dispatch action（支持 EID 范围、时间预算与续扫游标） |
| `get_action_details` | action 的元数据、绘制计数、偏移及输出资源（参数 action_event_id） |
| `get_action_api_calls` | action 关联 API 调用列表及按路径展开的参数树（API Inspector） |
| `get_action_timings` | 获取 action 的 GPU 执行时间 |
| `inspect_action` | 单个 action 的紧凑详情（时间、shader、管线、网格摘要） |
| `summarize_capture` | 捕获整体摘要 |
| `trace_resource_usage` | 资源整帧 usage，含 Timeline 五类分类、计数和筛选 |
| `trace_action_dependencies` | 追踪单个 action 的直接资源依赖与生产者 |
| `diff_actions` | 比较两个 action 的状态差异 |
| `analyze_pass` | 将一个 marker 子树/pass 汇总为整体工作负载 |
| `get_shader_info` | Shader 身份、入口点和反汇编 |
| `get_shader_source` | 获取 RenderDoc Edit/View 可见的原始 shader 源码（文本编码时） |
| `get_shader_edit_context` | 获取 GLSL/SPIR-V 的可编辑文本及编译路径 |
| `replace_shader` | 编译并应用 shader 替换（当前捕获会话内生效） |
| `revert_shader` | 还原原始 shader 并刷新 RenderDoc |
| `list_shader_replacements` | 查询生效替换与各编辑会话状态 |
| `export_shader_source` | 导出编辑后的 shader 源码（UTF-8，不覆盖已有文件） |
| `get_buffer_contents` | 支持 action_event_id 的事件后缓冲读取并恢复 replay；缓冲区数据获取（按数值 ID 匹配；偏移/长度指定；单次上限 256 KiB 可分页） |
| `list_resources` | 全部 API 对象目录（支持类型/名称过滤、排序和分页） |
| `inspect_resource` | 资源元数据、父/派生关系、使用统计和初始化调用目录 |
| `get_resource_initialization` | 初始化调用目录和按索引路径展开的参数树 |
| `get_texture_info` | 纹理元数据 |
| `get_texture_data` | 纹理像素数据获取（支持 mip/slice/3D 切片） |
| `save_texture` | 将纹理保存为图片文件（支持 PNG/JPG/BMP/TGA/EXR/DDS/HDR） |
| `get_pipeline_state` | Action 管线总览、阶段状态和诊断 |
| `get_pipeline_stage` | 阶段绑定、descriptor 信息和固定功能状态 |
| `inspect_pipeline_binding` | 绑定范围、资源身份和常量树展开 |
| `get_action_textures` | Action 输入/输出纹理与 FS/FB 等阶段标签 |
| `get_mesh_summary` | 获取网格概要信息（管线拓扑、`num_vertices` 保留 `numIndices` 语义、`unique_vertex_count` 为去重引用数、多属性包围盒；支持 instance 选择） |
| `get_mesh_data` | 获取网格顶点/索引数据（支持 VSIn/VSOut/GSOut 阶段与 instance 选择） |
| `export_mesh_csv` | 将网格导出为 CSV 文件（支持 instance 选择；无可导出属性时报 `MESH_SIGNATURE_UNAVAILABLE`） |
| `dump_draws` | 异步批量导出：output_dir + draw列表/marker/EID范围，状态、取消、纹理额度暂停及续跑 |
| `get_replay_context` | 当前/配置/官方协议发现的远端主机与服务状态 |
| `get_job_status` | 分页作业状态、阶段、进度、错误与结果清单 |
| `cancel_job` | 请求协作取消；原生加载不能强行中断 |
| `resume_job` | 同会话/修订内续跑暂停或已取消作业 |
| `export_shader_bundle` | 异步导出原始 Shader、反射、反汇编、已捕获源码及哈希 |
| `compare_texture_events` | 异步比较两个 action 后同一纹理 ROI 的数值 |
| `get_pixel_history` | 异步原生像素历史；按设备能力与原生有效性返回 |

### get_actions 过滤选项

```python
get_actions(
    include_children=True,      # 包含子 action
    marker_filter="Camera.Render",  # 仅获取此标记下的内容
    exclude_markers=["GUI.Repaint", "UIR.DrawChain"],  # 排除的标记
    action_event_id_range={"min": 7372, "max": 7600},  # action EID 范围
    exclude_marker_actions=True,          # 排除标记（仅 draw call）
    flags_filter=["Drawcall", "Dispatch"],  # 仅特定标志
)
```

### 捕获管理工具

```python
# 列举目录内的捕获文件
list_captures(directory="D:\\captures")
# → {"count": 3, "captures": [{"filename": "game.rdc", "path": "...", "size_bytes": 12345, "modified_time": "..."}, ...]}

# 打开捕获文件（现有捕获会自动关闭）
job = open_capture(capture_path="D:\\captures\\game.rdc")
get_job_status(job_id=job["job_id"])
# → {"job_id": "...", "status": "queued", ...}

# 确认捕获加载状态与回放健康
get_capture_status()
# → {"loaded": true, "api": "D3D11", "filename": "...", "remote_replay": false,
#    "replay_healthy": true, "replay_error": null,
#    "extension_version": "...", "renderdoc_version": "...", "ipc_version": 2}
# replay_healthy 为 replay 控制器探针（GetAPIProperties + GetFatalErrorStatus）；
# 断连/驱动失效时为 false 并带 replay_error。未加载捕获时仍返回版本字段。
```

### 资源枚举与检查工具

```python
list_resources()  # 默认 all，覆盖 Device/Memory/Shader/View/Texture/Buffer 等全部 API 对象
list_resources(resource_type="texture", name_filter="Character", offset=0, limit=50)
# items 每项为 resource_id/name/resource_type；包含 total_count/returned_count/has_more 等分页信息。
# texture 与 swapchain_image 独立过滤，支持 sort_by="name" 或 "resource_id"。

inspect_resource(resource_id="ResourceId::86983")
# resource、metadata、related_resources、usage、initialization。
# related_resources 包含 parent/derived 关系，可用 related_offset/related_limit 分页。
# usage 为统计；initialization 为前 20 项调用目录。

get_resource_initialization(resource_id="ResourceId::86983", offset=20)
# 指定返回的 chunk_index 和 child_path 后，读取目标节点及一页可见子节点。
get_resource_initialization(resource_id="ResourceId::86983", chunk_index=42, child_path=[1])
```

分页要求 offset >= 0、1 <= limit <= 500。纹理尺寸/格式、缓冲区大小等详情改从
`inspect_resource.metadata` 获取。`trace_resource_usage` 统一返回分页 events（默认 limit=100），
不再返回重复的 reads/writes 数组；统计与写入摘要基于分页前全部匹配记录。
`event_count` 为去重 EID 数，`usage_count` 为记录数。初始化参数每次只展开一层，路径使用
原始子节点索引；大块二进制仅返回大小，超长文本明确标记截断。详细契约见 docs/tools_zh.md。

### 反向搜索工具

```python
search_actions(by="shader", query="Toon", stage="fragment")
search_actions(by="texture", query="CharacterSkin")
search_actions(by="resource", query="ResourceId::12345")
search_actions(by="resource", query="ResourceId::12345",
               action_event_id_range={"min": 940, "max": 1533})
# → {
#     "matches": [...],
#     "scanned_count": 150,
#     "total_matches": 3,
#     "complete": true,
#     "stopped_reason": null,
#     "next_event_id": null,
#     "scan_mode": "usage"
# }
```

- `by="texture"` / `by="resource"` 先走 Timeline usage 索引缩小候选
  （`scan_mode="usage"`），只有 usage 为空时才退回逐 action 的 pipeline 扫描。
- 资源与 shader 一律按**数值 ID** 比较（`ResourceId` 不能由 int 构造）。
- 扫描有 `time_budget_ms`（默认 8000）与 `max_matches`（默认 200）；截断时
  `complete=false`、`stopped_reason` 非空，用 `start_event_id=next_event_id` 续扫，
  不要把截断结果当空结果。

### 管线与事件纹理

```python
get_pipeline_state(action_event_id=343)
get_pipeline_stage(action_event_id=343, stage="FS", section="constant_buffers")
# binding_id 使用上一条响应返回的值。
inspect_pipeline_binding(action_event_id=343, binding_id="<returned-id>", section="variables", child_path=[])
get_action_textures(action_event_id=343, direction="input", stage="FS")
get_action_textures(action_event_id=343, direction="output")
get_texture_data(resource_id="ResourceId::487", action_event_id=343)
```

- Pipeline State 使用总览→阶段→绑定详情；旧 event_id 参数与纹理聚合响应已移除。
- 阶段和纹理列表支持 offset/limit（1–500），show_unused/show_empty 默认 false，异常条目仍保留。
- 纹理列表按绑定保留多次引用，不按 resource_id 去重；read-write 同时匹配 input/output。
- binding_id 限当前捕获/action/绑定内容；resource.resource_id 继续关联资源 Inspector 工具。
- 常量范围包含 Vulkan dynamic offset；不要再次相加。变量只在显式 variables 查询时解码。
- get_texture_data/save_texture 的可选 action_event_id 指定 action 执行后的内容，查询后恢复 UI replay 事件。
- inspect_action/diff_actions 使用完整共享快照，包含 buffer/sampler/固定功能状态，比较不受公开工具分页影响。
- get_shader_info 仅保留 shader 身份、入口点和反汇编。
- trace_resource_usage(resource_id, categories=["barrier", "clear"]) 按 Timeline 分类筛选；category_counts 包含 read/write/read_write/barrier/clear 五类，统计全部筛选后分页前的 usage 记录。GenMips 属于 read_write，Discard 属于 clear；原始 usage 和旧 access 语义保留。

### GPU 时间获取

```python
# 获取所有 action 的时间
get_action_timings()
# → {"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}

# 仅获取特定事件 ID
get_action_timings(action_event_ids=[100, 200, 300])

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
    action_event_id=343,
    output_path="D:/output/texture.png"
)
# → {"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}

# 指定格式和选项
save_texture(
    resource_id="ResourceId::2495",
    action_event_id=343,
    output_path="D:/output/texture.exr",
    format_type="EXR",           # PNG, JPG, BMP, TGA, EXR, DDS, HDR
    mip=-1,                      # -1 表示导出所有 mip（仅 DDS 生效；其他格式实际保存 mip 0，
                                 # 响应以 mip_selection/mip_note 报告实际范围）
    slice_index=0,               # 数组切片或立方体面索引
    alpha_mode="blend_to_black"  # preserve, discard, blend_to_black
)

# 立方体贴图面索引: 0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-
```

**注意**: 这是推荐的纹理保存方式，会自动处理格式转换。

### 网格数据工具

```python
# 获取网格概要信息
get_mesh_summary(action_event_id=1234, instance=0)  # instance 用于逐实例属性/post-VS 选择
# → {
#     "action_event_id": 1234,
#     "instance": 0,
#     "topology": "TriangleList",
#     "num_vertices": 9072,
#     "unique_vertex_count": 3024,
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
    action_event_id=1234,
    stage="VSIn",           # VSIn, VSOut, GSOut
    offset=0,               # 起始偏移量（分页）
    limit=100,              # 每次获取的绘制引用数（建议 100-500）
    attributes=["POSITION", "NORMAL", "TEXCOORD"],  # 可选，过滤属性
    instance=0              # 可选，实例索引（VSIn per-instance 按 instance*stride 寻址；
                            #  VSOut/GSOut 读取对应实例的 post-VS 数据）
)
# → {
#     "action_event_id": 1234,
#     "instance": 0,
#     "stage": "VSIn",
#     "topology": "TriangleList",
#     "items": [
#         {"POSITION": [1.0, 2.0, 3.0], "NORMAL": [0.0, 1.0, 0.0], "TEXCOORD": [0.5, 0.5]},
#         ...
#     ],
#     "indices": [0, 1, 2, 3, 4, 5, ...],
#     "offset": 0,
#     "limit": 100,
#     "returned_count": 100,
#     "total_count": 9072,
#     "has_more": true,
#     "truncated": false,
#     "attributes": [...]
# }

# 分页获取下一批数据
get_mesh_data(action_event_id=1234, offset=100, limit=100)

# 导出网格为 CSV 文件
export_mesh_csv(
    action_event_id=1234,
    output_path="D:/output/mesh.csv",
    stage="VSIn",
    attributes=["POSITION", "NORMAL", "TEXCOORD"],  # 可选
    instance=0  # 可选
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
- `VSIn`: 顶点着色器输入（原始顶点缓冲区数据，含 per-instance 属性）
- `VSOut`: 顶点着色器输出（属性名/布局来自 Vertex 输出签名）
- `GSOut`: 管线最后活动阶段的最终输出（按实际绑定判断：有 Geometry 用 Geometry，
  否则 Domain/曲面细分；偏移按原生网格查看器规则计算——按光栅化 stream 过滤、
  Position 提前、分量按 32 位展开，仅 HasAlignedPostVSData 时做 vec4 对齐，
  并用 vertexByteStride 校验）

**分页说明**：
- 使用 `offset` 和 `limit` 进行分页
- `total_count` 表示总绘制引用数，`returned_count` 为本次返回数量
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
   - 与 MCP 客户端（Codex）：通过 stdio 通信
   - 与 RenderDoc 扩展：通过文件 IPC（`%TEMP%/renderdoc_mcp/`）

**使用方式**：

```bash
# 安装后直接运行
renderdoc-mcp
```

在 Codex 配置中添加：
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
2. MCP 服务器由 Codex 客户端自动启动.

## 通信协议

基于文件的 IPC:
- IPC 目录: `%TEMP%/renderdoc_mcp/`
- `request.json`: 请求（MCP 服务器 → RenderDoc）
- `response_<request_id>.json`: 响应（RenderDoc → MCP 服务器）
- `call.lock`: MCP 客户端间的 OS 事务锁；request/response 通过临时文件原子发布
- `jobs/<job_id>.json`：原子作业元数据；`jobs/<job_id>/items/` 保存独立条目
- `jobs/controls/<job_id>.cancel.json`：MCP 原子发布取消请求，由扩展在步骤间协作处理
- `get_job_status` 直接读取作业快照；UI 模态停滞时仍能报告阶段与持续时间，不能据此认定原生调用失败
- 批处理状态页只返回紧凑条目，完整绑定／常量布局从 details_path 对应文件读取；不要反复倾倒完整清单进上下文
- 轮询间隔: 100ms（RenderDoc 端）

## 开发注意事项

- RenderDoc 内置 Python 没有 socket/QtNetwork 模块，因此采用基于文件的 IPC
- RenderDoc 扩展仅使用 Python 3.6 标准库
- 对 ReplayController 的访问通过 `BlockInvoke` 进行。
- 异步作业通过 `AsyncInvoke` 分步访问 ReplayController，不嵌套 `BlockInvoke`，不保存控制器对象。
- 后台 Python 工作线程仅做清单写入和数值运算；不能访问 Qt 或 ReplayController，以免阻塞 UI 保活。
- 需要语法支持可以参考项目内的stubs文件夹，记录了renderdoc python module的模块语法支持。

## 参考链接

- [FastMCP](https://github.com/PrefectHQ/fastmcp)
- [RenderDoc Python API](https://renderdoc.org/docs/python_api/index.html)
- [RenderDoc Extension Registration](https://renderdoc.org/docs/how/how_python_extension.html)
