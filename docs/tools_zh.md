# MCP 工具参考

所有 RenderDoc MCP 工具的详细参考文档，包含参数、返回值和使用示例。

[English](tools.md)

## 术语与字段约定

| 术语 / 字段 | 含义 |
|---|---|
| `event_id`（EID） | 帧内事件编号，可以指向设置状态的 API event。用于 shader 的 replay 状态查询和资源原始 usage 记录。 |
| `action_event_id` | 产生该 action 的事件 EID。所有 action 接口的输入和返回记录统一使用此字段，包括嵌套记录、网格、时间和搜索结果。 |
| `action_id` | 独立的 action 序号，从 1 开始。不能当作 EID 传入。 |
| `api_event_id` | 指定 action 关联的某条 API event 的 EID，与 `action_event_id` 属于同一套 EID。 |
| action / draw call | action 包含 draw、dispatch、copy、clear 和 marker 节点；draw call 专指绘制。搜索目前扫描 draw 和 dispatch。 |

action EID 不是把几个 API 调用打包后重新分配的编号。例如 EID 340–343 关联到一个
draw，其 `action_event_id` 是 343，`action_id` 可以是 12；`api_event_id=341`
用于选择其中一条 API event。
资源 usage 和生产者记录保留通用 `event_id`，即使无法解析出对应 action 也能返回。
shader 查询读取指定事件的 replay 状态，不要求精确 action，因此保留 `event_id`。
纹理读取/导出可显式指定精确 `action_event_id`；省略时使用 UI 当前 replay 位置。
返回值在显式指定 action 时使用 `action_event_id`，省略参数时使用 `event_id`，
因为 UI 当前 replay 位置可能是中间 API event。

shader 阶段统一返回 `vertex`、`tess_control`、`tess_eval`、`geometry`、`fragment`、
`compute`、`task`、`mesh`（以 RenderDoc 支持为准）。shader 和管线接口接受相同的
shader 阶段别名，包括 `hull`/`HS`/`TCS`、`domain`/`DS`/`TES`、`pixel`/`PS`/`FS`。
管线专用的 `vertex_input`、`rasterizer`、`framebuffer` 不属于 shader 阶段。
网格的 `VSIn`/`VSOut`/`GSOut` 表示数据位置，保持独立。

纹理读取/导出的数组层或立方体面参数及返回字段统一为 `slice_index`；`depth_slice`
表示 3D 纹理的 Z 切片。网格读取/导出的属性筛选统一为 `attributes`。
分页统一用 `offset`/`limit`，单位是条目（网格读取为顶点条目）；buffer 的
`offset`/`length` 表示字节范围。

action 接口使用 `action_event_id`、`action_event_ids`、`action_event_id_range`。
比较接口参数为 `action_event_id_a`/`action_event_id_b`，返回 `action_a`/`action_b`；
`analyze_pass` 返回 `action_event_id_range`。
`exclude_marker_actions` 排除 marker 节点，marker 本身也是 action。
API 调用上下文的名称字段为 `name`；`inspect_action.timing.action` 是匹配的时间记录。
接口仅按照当前签名校验参数。

## 推荐流程

一个典型的分析流程通常遵循以下模式：

`get_capture_status` / `get_frame_summary` -> `get_actions` / `search_actions` -> `get_pipeline_state` / `get_shader_info` / `get_shader_source` / `get_shader_edit_context` / `get_mesh_data`

---

## 全局操作能力

### 捕获管理

#### `open_capture`

打开 RenderDoc 捕获文件 (.rdc)。会自动关闭当前已打开的捕获。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `capture_path` | `str` | 是 | 捕获文件的完整路径 |

**返回值：** `{"success": true, "filename": "game.rdc", "api": "D3D11"}`

**示例：**
```
open_capture(capture_path="D:/captures/game.rdc")
```

---

#### `list_captures`

列出目录中所有 `.rdc` 文件。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `directory` | `str` | 是 | 要搜索的目录路径 |

**返回值：** 包含 `filename`、`path`、`size_bytes`、`modified_time` 的列表。

**示例：**
```
list_captures(directory="D:/captures")
# → {"count": 3, "captures": [{"filename": "game.rdc", "path": "D:/captures/game.rdc", "size_bytes": 12345, "modified_time": "..."}]}
```

---

#### `get_capture_status`

检查 RenderDoc 中是否已加载捕获，并报告运行版本、IPC 协议版本与回放健康状态。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** `{"loaded": true, "api": "D3D11", "filename": "...", "remote_replay": false,
"replay_healthy": true, "replay_error": null, "extension_version": "...",
"renderdoc_version": "...", "ipc_version": 2}`。`replay_healthy` 为 replay 控制器探针结果
（`GetAPIProperties` + `GetFatalErrorStatus` 往返）；驱动/设备失效时为 `false` 并带
`replay_error`。未加载捕获时 `replay_healthy` 为 `null`，版本字段仍返回，可用于核对
客户端连接的扩展与协议版本。

**示例：**
```
get_capture_status()
```

---

### 帧概览

#### `get_frame_summary`

获取整帧统计信息和顶层 marker 摘要。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** API 类型、action 总数、统计信息（draw calls、dispatches、clears、copies、presents、markers）、顶层 marker（含 event ID 和子级数量）、资源数量（纹理、缓冲区）。

**示例：**
```
get_frame_summary()
```

---

#### `summarize_capture`

在 `get_frame_summary` 之上额外获取全帧 GPU 时间并进行排序去重，返回高层概览与建议的分析入口。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** 帧统计信息、`hot_actions`（GPU 时间 Top 10）、主要 marker、`suggested_entry_points`。

**示例：**
```
summarize_capture()
```

---

### Action 导航

#### `get_actions`

获取 draw call 和 action 的层级结构，支持过滤。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `include_children` | `bool` | 否 | `true` | 包含子级 action |
| `marker_filter` | `str` | 否 | | 仅包含标记路径中包含此字符串的 action（部分匹配） |
| `exclude_markers` | `list[str]` | 否 | | 排除标记路径中包含这些字符串的 action |
| `action_event_id_range` | `dict` | 否 | | event ID 范围，格式为 `{"min": ..., "max": ...}` |
| `exclude_marker_actions` | `bool` | 否 | `false` | 为 true 时排除 marker action |
| `flags_filter` | `list[str]` | 否 | | 仅包含具有这些标志的 action（如 `["Drawcall", "Dispatch"]`） |

**返回值：** 包含 marker、draw call、dispatch 和其他 GPU 事件的层级树结构。

**示例：**
```
# 获取完整 action 树
get_actions(include_children=true)

# 按 marker 和 event 范围过滤
get_actions(marker_filter="Camera.Render", action_event_id_range={"min": 7372, "max": 7600})

# 仅 draw call，排除 marker
get_actions(exclude_marker_actions=true, flags_filter=["Drawcall"])

# 排除特定 marker
get_actions(exclude_markers=["GUI.Repaint", "UIR.DrawChain"])
```

---

#### `search_actions`

按 shader、texture 或 resource 搜索 draw 和 dispatch action。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `by` | `"shader"` / `"texture"` / `"resource"` | 是 | 搜索模式 |
| `query` | `str` | 是 | shader 名称、纹理名称或 resource ID |
| `stage` | `str` | 否 | shader 阶段过滤（`"vertex"`、`"fragment"`、`"compute"` 等）— 仅在 `by="shader"` 时有效 |
| `action_event_id_range` | `{"min": int, "max": int}` | 否 | 只扫描该 action EID 范围 |
| `time_budget_ms` | `int` | 否 | 扫描预算，默认 8000；到点停止并返回续扫游标，不再让客户端超时 |
| `max_matches` | `int` | 否 | 匹配数上限，默认 200 |
| `start_event_id` | `int` | 否 | 上次截断结果里的 `next_event_id`，从该 EID 起续扫 |

**返回值：** `{"matches": [...], "total_matches": 3, "scanned_count": 150}`，另含
`complete`、`stopped_reason`（`null` / `"time_budget"` / `"max_matches"`）、
`next_event_id`、`scan_mode`（`"usage"` 或 `"pipeline"`）、`elapsed_ms`、
`scan_failures`（无法读取的 action 数）与 `scan_error`（首个失败原因）；全部扫描失败时
报 `RESOURCE_QUERY_FAILED`，恢复 replay 位置失败时报 `REPLAY_RESTORE_FAILED`。

`by="texture"` / `by="resource"` 先用 Timeline usage 索引把候选 action 缩到真正使用该
资源的 draw/dispatch（`scan_mode="usage"`），只有 usage 为空时才退回逐 action 的
pipeline 扫描。资源与 shader 一律按数值 ID 匹配（`ResourceId` 不能由 int 构造）。

当 `complete=false` 时，用 `start_event_id=next_event_id` 续扫；该游标包含自身，指向
下一个尚未处理的 action。`scanned_count` 为本次实际尝试数。预算包含候选准备，
但无法中断单次 replay/API 调用。usage 路径不移动 replay，也不获取逐 action 管线状态。

**示例：**
```
search_actions(by="shader", query="Toon", stage="fragment")
search_actions(by="texture", query="CharacterSkin")
search_actions(by="resource", query="ResourceId::12345")
search_actions(by="resource", query="ResourceId::12345",
               action_event_id_range={"min": 940, "max": 1533})
```

---

### 资源空间浏览

以下只读工具对应 Resource Inspector 的数据，不改变当前选中的事件或资源。资源 ID、chunk 索引和参数路径仅属于当前捕获。所有分页要求 `offset >= 0`、`1 <= limit <= 500`，返回 `total_count`、`offset`、`limit`、`returned_count`、`has_more`。

#### `list_resources`

通过 `GetResources()` 枚举全部 API 对象，包括 Device、Memory、Shader、View、CommandBuffer 等。

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `resource_type` | `str` | `"all"` | `all` 或 RenderDoc ResourceType 的小写下划线名称，精确匹配 |
| `name_filter` | `str` | `None` | 显示名称的子串匹配，不区分大小写 |
| `offset` | `int` | `0` | 匹配结果的起始位置 |
| `limit` | `int` | `50` | 每页 1–500 项 |
| `sort_by` | `str` | `"name"` | 按 `name` 或数字 `resource_id` 排序；同名时按数字 ID 排序 |

每项仅包含 `resource_id`、`name`、`resource_type`。名称包含 RenderDoc 中的用户重命名。`texture` 与 `swapchain_image` 是独立的类型过滤值。

```python
list_resources()  # 全部 API 对象
list_resources(resource_type="memory", sort_by="resource_id")
list_resources(resource_type="texture", name_filter="Scene", offset=50)
```

#### `inspect_resource`

参数：必填 `resource_id: str`，可选 `related_offset: int = 0`、`related_limit: int = 50`。

返回 `resource`（身份）、`metadata`（纹理/缓冲区详情，其他类型为 `{}`）、`related_resources`、`usage`、`initialization`。

- 关联资源包含 `relationship: "parent" | "derived"` 和资源身份。父资源优先，各组按名称和数字 ID 排序。关联目标不存在时仍保留 ID，并标记 `missing: true`。
- `usage` 包含可用状态、使用记录数 `usage_count`、去重事件数 `event_count`、原始用途统计 `usage_counts`，不包含事件列表。不适用时为 `available: false, reason: "unsupported_resource_type"`；查询成功但没有记录时计数为零；驱动查询失败时为 `reason: "query_failed"`，附带错误。
- `initialization` 返回前 20 项初始化调用目录（`chunk_index`、`name`、`child_count`）及分页信息，后续通过 `get_resource_initialization(offset=20)` 读取。无效目录索引保留并标注错误。某一区域失败不丢弃其余检查结果。

```python
inspect_resource(resource_id="ResourceId::86983")
inspect_resource(resource_id="ResourceId::86826", related_offset=50)
```

#### `get_resource_initialization`

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `resource_id` | `str` | 必填 | 被检查的资源 |
| `chunk_index` | `int` | `None` | 省略时列举调用；指定时必须使用属于该资源的返回索引 |
| `child_path` | `list[int]` | `[]` | 相对于所选 chunk 的原始子节点索引路径，直接复用返回值 |
| `offset` | `int` | `0` | 调用目录或当前节点可见子节点的分页偏移 |
| `limit` | `int` | `50` | 每页 1–500 项 |

省略 `chunk_index` 返回分页调用目录；指定后返回 `node` 和分页 `children`。每个节点包含 `name`、`type`、`basic_type`、`child_path`、原始 `child_count`；标量另有 `value`。结构体与数组每次只展开一层。子节点分页隐藏 Hidden 字段，但路径保留原始索引，因此同名字段及隐藏兄弟节点不会导致路径歧义。分页总数按可见子节点计算。

枚举/位标志同时保留数字值和可用的 `display_value`；资源引用返回资源身份。二进制只返回 `byte_size` 与 `content_omitted`。文本值和显示字符串最多 4096 字符，截断时提供 `<field>_truncated`、`<field>_length`。非有限浮点数以 `value: null` 和 `non_finite` 标签表示。

```python
get_resource_initialization(resource_id="ResourceId::86983")
# 使用前一步返回的 chunk_index 与 child_path，以下索引仅为示例：
get_resource_initialization(resource_id="ResourceId::86983", chunk_index=42)
get_resource_initialization(resource_id="ResourceId::86983", chunk_index=42, child_path=[1])
```

无效分页、排序、资源类型、chunk 归属及节点路径返回参数错误；资源不存在、未加载捕获和底层查询失败返回运行时错误。本版仅对纹理/缓冲区（含具有纹理描述符的交换链图像）查询 usage。初始化参数描述创建和设置过程，当前资源内容仍通过数据读取工具获取。

**迁移说明：** `list_resources` 默认列举全部资源，返回紧凑身份；原先读取的尺寸、格式、大小改从 `inspect_resource(...)["metadata"]` 获取，也可继续使用 `get_texture_info`。`trace_resource_usage` 移除重复的 `reads`/`writes` 数组，统一读取分页 `events`，按 Timeline `category` 分类（通过 `categories` 筛选）并通过 `has_more` 翻页；其 `resource` 同样改为紧凑身份。`event_count` 为去重 EID 数，`usage_count`/`total_count` 为使用记录数。

安装/重新加载新版扩展并重启 MCP 服务后，打开捕获，运行 `python scripts/validate_resources_live.py --resource-id ResourceId::86983`（替换为当前捕获中的 ID）。该只读脚本输出 JSON 报告，供对照 Resource Inspector 检查，不改变当前选择。自动化测试使用模拟绑定和真实文件 IPC，不能替代真实捕获验证。

---

## 局部数据分析能力

### Shader 会话编辑

支持 GLSL、Vulkan SPIR-V、OpenGL SPIR-V。替换影响所有引用原始 shader 资源的 draw，
仅在当前捕获会话生效，不写入 `.rdc`。HLSL / DXBC / DXIL 编辑为 TODO。

| 工具 | 参数 | 作用 |
|------|------|------|
| `get_shader_edit_context` | `event_id: int, stage: str, mode: str = "auto"` | 获取编辑 ID、可编辑代码、编译路径与状态 |
| `replace_shader` | `edit_id: str, source_text: str` | 编译并应用；失败保留上一次成功替换 |
| `revert_shader` | `edit_id: str` | 还原原始 shader；允许重复调用 |
| `list_shader_replacements` | 无 | `items` 列出生效的替换，`sessions` 同时包含准备、失败和冲突的会话 |
| `export_shader_source` | `edit_id: str, output_path: str` | 以 UTF-8 导出最近提交的文本，已有文件不覆盖 |

`stage` 统一使用 `vertex / tess_control / tess_eval / geometry / fragment / compute / task / mesh`。
`mode` 支持 `auto / original / glsl / spirv_asm`：原始 GLSL 直接编辑；SPIR-V 自动优先使用
SPIRV-Cross → GLSL → 编译器，缺少完整路径时回退到 spirv-dis → 汇编 → spirv-as。
显式选择模式时不回退。`original` 仅支持捕获中的文本 GLSL；伪代码不是可编译源码。
已有编辑会话时 `auto` 复用该会话及当前表示，以便查询提交结果；还原后可显式选择另一种模式。
不管理工程 include，提交内容必须是单份可编译文本。工具与路径来自 RenderDoc 的
Settings → Shader Processing 配置，不硬编码。一个资源的多入口编辑暂不支持。

```python
edit = get_shader_edit_context(event_id=123, stage="fragment", mode="auto")
# 根据 edit["source_text"] 修改代码，保留资源绑定与输入输出接口。
result = replace_shader(edit_id=edit["edit_id"], source_text=modified_source)
# 应检查 last_attempt_status == "applied"，并读取 log 中的警告/错误。
get_pipeline_state(action_event_id=123)
# 使用已有 get_texture_data / save_texture 对比相同输出纹理的修改前后结果。
export_shader_source(edit_id=edit["edit_id"], output_path="D:/captures/edited_shader.glsl")
revert_shader(edit_id=edit["edit_id"])
```

上下文同时返回 `source_text`（最近提交或初始文本）和 `applied_source_text`（当前成功应用的文本），
以及入口、编码、编译器、`revision`、`applied`、`last_attempt_status` 和 `log`。
编译失败返回 `last_attempt_status="compile_failed"`，不等于 IPC 调用失败；`applied=true` 也可能
代表上一版仍在生效。导出返回 `matches_applied_source`，失败草稿仍可导出。

编辑 ID 在关闭捕获、重新打开同一路径或卸载扩展后失效。检测到人工编辑器/其他来源的替换时
报 `SHADER_EDIT_CONFLICT`，应先在原编辑器还原。切换表示方式前也须还原。

编辑调用超时为 120 秒。`RESULT_PENDING` 表示请求已提交但结果未知，**禁止自动重试替换**；
先调用 `list_shader_replacements()`，或以原 event/stage 获取上下文确认状态。
`SHADER_TOOL_MISSING` 指明缺少的转换路径；`INVALID_EDIT_ID` 表示会话已失效；
`OUTPUT_FILE_EXISTS` 表示导出目标已存在。

安装更新：`uv tool install . --editable`，执行 `python scripts/install_extension.py`，再在
RenderDoc 的扩展管理器重新加载 Bridge（或重启 RenderDoc），并重新连接 MCP 客户端。

自动化验证：`python -m unittest discover -s tests -v`。真实验收应分别覆盖 OpenGL GLSL、
Vulkan SPIR-V 和 OpenGL SPIR-V，检查无修改往返、颜色修改、失败保留、连续替换、还原和共享资源。

移动端捕获须先在 RenderDoc 底部选择对应设备的 **Replay Context** 并打开捕获；
`get_capture_status()` 和 shader 编辑上下文的 `remote_replay=true` 才证明操作走远端回放。
例如 hkrpg 的捕获必须在已通过 ADB 连接的移动设备上验收。
反编译/编译工具运行在主机，生成的 shader 通过远端 replay controller 在移动 GPU 上替换和回放。
可对已打开的移动端捕获执行：

```bash
python scripts/validate_shader_edit_remote.py --event-id 2069 --output-dir build/shader-edit-validation/mobile-run
# 可选：指定候选 draw 验证共享 shader 的影响，脚本先核对实际绑定。
python scripts/validate_shader_edit_remote.py --event-id 2808 --shared-event-ids 2799 2792 --output-dir build/shader-edit-validation/shared-run
```

按实际捕获选择 event，输出目录必须尚不存在。脚本验证原始往返、颜色修改、失败保留、连续替换、
汇编往返、源码导出及图像/像素哈希，结束时还原，不关闭当前捕获。`scripts/validate_shader_edit.py`
是单独实例的本地回放辅助脚本，禁止用它本地加载 hkrpg 捕获。

### Pipeline 状态

#### `get_pipeline_state`

`get_pipeline_state(action_event_id)` 返回紧凑总览：API、pipeline 资源身份、阶段状态、
可用栏目、绑定计数和问题摘要。参数必须是准确的 action EID。
旧 `event_id` 参数和完整 `shaders`、`input_textures`、`output_textures` 聚合字段已移除。

#### `get_pipeline_stage`

```python
get_pipeline_state(action_event_id=343)
get_pipeline_stage(action_event_id=343, stage="FS")
get_pipeline_stage(action_event_id=343, stage="FS", section="constant_buffers", offset=0, limit=50)
```

参数：`action_event_id`、`stage`、`section="overview"`、`show_unused=False`、
`show_empty=False`、`offset=0`、`limit=50`（1–500）。overview 列出可用栏目。
统一阶段：`vertex_input`、`vertex`、`tess_control`、`tess_eval`、`geometry`、`task`、
`mesh`、`rasterizer`、`fragment`、`framebuffer`、`compute`。
支持 VS、HS/TCS、DS/TES、GS、AS/TS、MS、FS/PS、CS、FB/OM 别名；显示名称跟随 API。

| 阶段 | 栏目 |
|---|---|
| Vertex Input | `assembly`、`attributes`、`buffers` |
| Shader 阶段 | `shader`、`descriptors`、`resources`、`samplers`、`constant_buffers`、`push_constants` |
| Rasterizer | `rasterizer`、`viewports`、`scissors`、`multisample` |
| Framebuffer | `attachments`、`blend`、`depth_stencil` |
| Compute | Shader 栏目和 `dispatch` |

列表统一返回 `items`、`total_count`、`offset`、`limit`、`returned_count`、`has_more`。
阶段区分 `enabled`、`disabled`、`not_applicable`、`unavailable`；栏目失败明确返回
`available=false` 和原因，部分可用数据仍保留。Vulkan 补齐原生 descriptor set/layout、
动态偏移、descriptor buffer、rasterizer、多重采样和 renderpass 信息；其他 API 提供通用
绑定与状态，尚未支持的原生细节明确标记。
默认过滤确定未使用的正常绑定及无关空槽，缺失必需绑定和范围异常仍可见。
`possibly_used` 不代表 GPU 实际访问证明。总览计数包含过滤器隐藏的绑定。

#### `inspect_pipeline_binding`

```python
rows = get_pipeline_stage(action_event_id=343, stage="FS", section="constant_buffers")
binding_id = rows["items"][0]["binding_id"]
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id)
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id, section="variables")
# 使用上一条响应中的 child_path 继续展开。
inspect_pipeline_binding(action_event_id=343, binding_id=binding_id,
                         section="variables", child_path=[0], offset=0, limit=50)
```

参数：`action_event_id`、`binding_id`、`section="details"|"variables"`、
`child_path=None`、`offset=0`、`limit=50`。details 默认不解码常量。
每条绑定保留阶段、原生 set/space 与 binding、reflection 索引、数组元素、声明名称和资源身份。
Buffer 范围是实际有效字节范围，Vulkan dynamic offset 已包含，不重复累加。
`constant_buffer_range_too_small` 用 `required_bytes` 与 `provided_bytes` 表示
例如“需要 720 字节，提供 512 字节”，不据此断言执行发生越界读取。
直接常量不要求存在 buffer；`push_constants` 栏目承载非 buffer-backed 常量块，具体种类
由 API 与反射名称表达。variables 返回一层布局和值、整数路径和分页，不展开整个大数组。
任意 storage buffer 的字节读取继续使用已有 buffer 工具。

`binding_id` 是工具返回的不透明标识，限定在当前捕获、action 和绑定内容中，重载同一捕获也会失效。
`binding_key` 用于语义位置比较，不作为详情查询参数。
用 `resource.resource_id` 继续调用 `inspect_resource`、`trace_resource_usage`、
`get_resource_initialization`；全帧名称用于展示和搜索，不保证唯一。

#### `get_action_textures`

```python
get_action_textures(action_event_id=343, direction="all", offset=0, limit=50)
get_action_textures(action_event_id=343, direction="input", stage="FS")
get_action_textures(action_event_id=343, direction="output")
get_texture_data(action_event_id=343, resource_id="ResourceId::487", mip=0, slice_index=0)
save_texture(action_event_id=343, resource_id="ResourceId::487",
             output_path="D:/output/texture.png")
```

参数：`action_event_id`、`direction="all"|"input"|"output"`、可选 `stage`、
`show_unused=False`、`show_empty=False`、`offset=0`、`limit=50`。
返回一个分页绑定列表，含 FS/FB 等标签、shader 声明名、全帧资源身份、用途、尺寸、格式和 view 子资源范围。
同一纹理的多个阶段、槽位或数组元素分别保留。Read-write image 同时匹配 input/output，
在 all 中只出现一次。Framebuffer 表示输出绑定，不声称一定写入；depth/stencil 的写入状态
和可获取的 attachment access 信息独立报告。
Copy/resolve 使用 action 的显式 source/destination 与子资源；clear 返回已知目标，
无法取得的子资源范围明确标记。非 shader action 不混入遗留的 shader 绑定。

本工具不生成图片预览。`get_texture_data` 和 `save_texture` 增加可选 `action_event_id`：
指定时读取该 action **执行后** 的纹理，省略时沿用 UI 当前事件；响应包含实际事件和
`event_phase="after"`。即使纹理标记为 input，像素查询也不代表每次 shader 访问时的历史快照。
查询成功或失败均恢复 UI 对应的 replay 事件，不改变 UI 选择。

`inspect_action` 改为返回管线总览 `pipeline`、不分页的 `bindings` / `textures` 和
`fixed_function`。`diff_actions` 比较完整绑定位置及范围，包含 buffer/sampler 和固定功能状态，
忽略 action 专属 token。`get_shader_info` 不再返回常量值和资源绑定集合。

自动验证：`python -m unittest discover -s tests -v`。
手动安装并重载更新后的扩展后，可运行
`python scripts/validate_pipeline_live.py --action-event-id 343 --stage FS`
与真实面板对照。脚本只读取已经打开的捕获，不导出图片或切换 UI 选择。

---

#### `get_shader_info`

获取指定 event 处特定阶段的 shader 信息。包含 shader 身份、入口点和反汇编；绑定与常量通过管线工具查询。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | event ID |
| `stage` | `str` | 是 | shader 阶段：`"vertex"`、`"tess_control"`、`"tess_eval"`、`"geometry"`、`"fragment"`、`"compute"` |

**返回值：** shader resource ID、入口点、阶段和反汇编。

**示例：**
```
get_shader_info(event_id=123, stage="fragment")
```

---

#### `get_shader_source`

获取指定 event 处特定阶段的原始 shader 源码；仅当捕获中保留了文本型源码时返回 `source_text`。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | event ID |
| `stage` | `str` | 是 | shader 阶段：`"vertex"`、`"tess_control"`、`"tess_eval"`、`"geometry"`、`"fragment"`、`"compute"` |

**返回值：** shader resource ID、入口点、阶段、编码类型、`source_available`，以及文本编码下的 `source_text`。对于 DXBC / DXIL / 二进制 SPIR-V 等格式，返回元数据和说明原始源码不可直接获得的 `reason`。

**示例：**
```
get_shader_source(event_id=123, stage="fragment")
# → {"resource_id": "ResourceId::42", "encoding": "GLSL", "source_available": true, "source_text": "..."}
```

---

#### `get_shader_edit_context`

为指定 event/阶段准备可编辑的 GLSL/SPIR-V 文本及其编译路径。完整的编辑/替换流程见 [Shader 会话编辑](#shader-会话编辑)。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `event_id` | `int` | 是 | | event ID |
| `stage` | `str` | 是 | | shader 阶段：`"vertex"`、`"tess_control"`、`"tess_eval"`、`"geometry"`、`"fragment"`、`"compute"` |
| `mode` | `str` | 否 | `"auto"` | 要准备的表示形式：`auto / original / glsl / spirv_asm` |

**返回值：** `edit_id`、`source_text`、`applied_source_text`、入口点、编码、编译器、`revision`、`applied`、`last_attempt_status` 和 `log`。将 `edit_id` 配合 `replace_shader` / `revert_shader` / `export_shader_source` 使用。

**示例：**
```
edit = get_shader_edit_context(event_id=123, stage="fragment", mode="auto")
# → {"edit_id": "...", "source_text": "...", "compiler": "...", "applied": false, ...}
```

---

### 资源数据读取

#### `get_texture_info`

获取纹理资源的元数据。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `resource_id` | `str` | 是 | 资源 ID（如 `"ResourceId::2495"`） |

**返回值：** 尺寸、格式、mip 级别、数组大小等属性。

**示例：**
```
get_texture_info(resource_id="ResourceId::2495")
```

---

#### `get_texture_data`

读取纹理资源的像素数据。返回 Base64 编码的字节。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID |
| `action_event_id` | `int` | 否 | UI 当前事件 | 读取指定 action 执行后的内容，随后恢复 replay |
| `mip` | `int` | 否 | `0` | 要获取的 mip 级别 |
| `slice_index` | `int` | 否 | `0` | 数组切片或立方体贴图面索引（0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-） |
| `sample` | `int` | 否 | `0` | MSAA 采样索引 |
| `depth_slice` | `int` | 否 | | 仅限 3D 纹理，提取特定深度切片。省略时返回完整体积。 |

**返回值：** Base64 编码的像素数据，含元数据（尺寸、格式）。`color_space` 标明源数据的
存储色彩域（`srgb`/`linear`，按格式 compType 判定）；`all_zero` 表示全部字节为零（可能是
合法的清零资源，也可能是回放故障，需对照纹理查看器确认）；`warnings` 在数据长度为 0 或
全零时给出诊断提示。

**示例：**
```
# 获取 2D 纹理的 mip 0
get_texture_data(action_event_id=123, resource_id="ResourceId::123")

# 获取特定的 mip 级别
get_texture_data(action_event_id=123, resource_id="ResourceId::123", mip=2)

# 获取立方体贴图的特定面 (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(action_event_id=123, resource_id="ResourceId::456", slice_index=3)

# 获取 3D 纹理的特定深度切片
get_texture_data(action_event_id=123, resource_id="ResourceId::789", depth_slice=5)
```

---

#### `get_buffer_contents`

读取缓冲区资源的内容。返回 Base64 编码的字节。`offset`/`length` 为非负字节值，负值或
`offset` 超过缓冲大小时报 `INVALID_PAGINATION`；回放读取失败报 `RESOURCE_QUERY_FAILED`，
资源不存在报 `BUFFER_NOT_FOUND`，不再静默返回空数据。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID（`ResourceId::123` 或纯数字） |
| `offset` | `int` | 否 | `0` | 开始读取的字节偏移量 |
| `length` | `int` | 否 | `0` | 要读取的字节数（0 = 从 offset 到末尾） |

**返回值：** `resource_id`、`length`（本次字节数）、`total_size`、`offset`、
`requested_bytes`、`truncated`、`next_offset`、`max_inline_bytes`、`content_base64`。

单次内联上限 256 KiB；超过时 `truncated=true` 并给出 `next_offset`，按该偏移继续读取。
资源查找按**数值 ID** 匹配（`ResourceId` 无法由 int 构造），因此 `ResourceId::123` 与
`123` 等价。

**示例：**
```
# 获取整个缓冲区（超过 256 KiB 会分页）
get_buffer_contents(resource_id="ResourceId::123")

# 从偏移量 256 获取 512 字节
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

---

#### `get_mesh_summary`

获取特定 draw call 事件的网格数据摘要。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `action_event_id` | `int` | 是 | | draw call 的 event ID |
| `instance` | `int` | 否 | `0` | 实例索引，用于 per-instance 属性与 post-VS 数据选择 |

**返回值：** 拓扑结构、顶点/索引数量、是否使用索引缓冲、顶点属性及其格式、
包围盒。字段包括 `topology`、`topology_source`（`"pipeline"`）、`num_vertices`、
`unique_vertex_count`、`indices_available`、`num_indices`、`indexed`、`attributes`（含 `exportable`）、`bounding_box`、
`bounding_box_source`、`bounding_box_basis`、`bounding_box_inferred`、`bounding_boxes`。

- `topology` 取自管线状态（`GetPrimitiveTopology()`）；`ActionDescription.topology`
  在部分捕获（如 Vulkan 动态状态）为 `Unknown`，不再直接透传。
- `num_vertices` 保留历史语义：等于该 draw 的 `numIndices`（非索引绘制即顶点数）。
  去重后的“被索引引用顶点数”在 `unique_vertex_count`；索引缓冲读不到时它为 `null`，
  同时 `indices_available=false`。
- 反射名被剥离时属性名可能是 `_input0`，因此位置流按启发式推断：优先 `POSITION`/`POS`
  语义；否则取第一个“非单位长度”的三分量 float 属性（法线通常是单位长度）。
  `bounding_boxes` 给出所有三分量 float 属性的包围盒，便于核对；推断结果
  `bounding_box_inferred=true`。包围盒采样前 1000 个引用，跳过 special 格式、
  越界与非有限值；`topology_source` 也可能是 `mesh` 或 `unavailable`。

**示例：**
```
get_mesh_summary(action_event_id=1234)
# → {"topology": "TriangleList", "topology_source": "pipeline",
#    "num_vertices": 3024, "num_indices": 9072, "indexed": true,
#    "attributes": [{"name": "POSITION", "format": "R32G32B32_FLOAT",
#                    "components": 3, "exportable": true}, ...],
#    "bounding_box": {"min": [-10.0, -5.0, -2.0], "max": [10.0, 5.0, 2.0]},
#    "bounding_box_source": "POSITION", "bounding_box_basis": "semantic",
#    "bounding_box_inferred": false}
```

---

#### `get_mesh_data`

获取特定 draw call 的网格顶点和索引数据，支持分页。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `action_event_id` | `int` | 是 | | event ID |
| `stage` | `str` | 否 | `"VSIn"` | 网格数据阶段：`"VSIn"`（输入）、`"VSOut"`（顶点着色器输出）、`"GSOut"`（几何着色器输出） |
| `offset` | `int` | 否 | `0` | 分页起始顶点偏移量 |
| `limit` | `int` | 否 | `100` | 最大返回顶点数（建议：100-500） |
| `attributes` | `list[str]` | 否 | | 过滤特定属性名称（如 `["POSITION", "NORMAL"]`）。省略时包含所有属性。 |
| `instance` | `int` | 否 | `0` | 实例索引。VSIn 的 per-instance 属性按 `instance * byteStride`（含 instanceRate 折算）寻址；VSOut/GSOut 读取对应实例的 post-VS 数据。 |

**返回值：** `items`、`indices`、`topology`、`attributes`、`total_count`、`has_more`、`truncated`。

VSOut/GSOut 的属性名与布局来自产生该数据的 shader 阶段输出签名（VSOut 为 Vertex；
GSOut 按实际绑定判断——有 Geometry shader 用 Geometry，否则取 Domain/曲面细分最终输出；
`GetPostVSData` 返回的 MeshFormat 不含逐属性名字）。字节偏移按原生网格查看器规则计算：
先按光栅化 stream 过滤签名（多 stream geometry 输出），SV_Position/gl_Position 无条件
提前（D3D 将 Position 补齐为 float4）；分量统一按 32 位存储展开（64 位类型占 8 字节），
仅当 `HasAlignedPostVSData` 为真（如 Vulkan VSOut 的计算着色器缓冲）时才做 std430 vec4
对齐。计算结果会用返回的 `vertexByteStride` 校验，放不下时报 `MESH_SIGNATURE_UNAVAILABLE`
而不是解码错位数据。逐实例数据基址（`vertexByteOffset`）已包含在属性地址中。签名为空时
报 `MESH_SIGNATURE_UNAVAILABLE`，post-VS 数据缺失时报 `RESOURCE_NOT_FOUND`。

**示例：**
```
# 第一页
get_mesh_data(action_event_id=1234, offset=0, limit=100)

# 下一页
get_mesh_data(action_event_id=1234, offset=100, limit=100)

# 过滤特定属性
get_mesh_data(action_event_id=1234, offset=0, limit=100, attributes=["POSITION", "NORMAL", "TEXCOORD"])
```

---

### Action 元信息

#### `get_action_api_calls`

读取 draw/dispatch 对应的 API Inspector 数据，不改变当前选中的事件。

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `action_event_id` | `int` | 必填 | 精确的 action EID，不是中间的状态设置 API 事件 |
| `api_event_id` | `int` | `None` | 省略时列举调用；指定列表项的 `api_event_id` 后展开参数 |
| `child_path` | `list[int]` | `[]` | 复用上次返回的原始子节点索引路径 |
| `offset` | `int` | `0` | 调用列表或当前节点可见子节点的分页偏移 |
| `limit` | `int` | `50` | 每页 1–500 项 |

列表保留 `ActionDescription.events` 的顺序，通过分页可读取全部关联调用：即上一个 action 之后的事件，不代表所有历史状态设置调用。返回 `action_event_id`、`name` 和分页 `items`；每项包含 `api_event_id`、`name`、`chunk_index`、`available`，数据可用时包含原始 `child_count`。

指定 `api_event_id` 后返回 `api_call`、`node` 和分页 `children`。参数展开复用资源初始化的序列化逻辑：每次一层，隐藏 Hidden 子节点、保留原始索引路径、展示资源 ID/名称，二进制省略内容，文本预览限制为 4096 字符。没有结构化 chunk 的调用仍保留在列表中，标记 `available: false` 和 `reason: "no_chunk"` 或 `"invalid_chunk_index"`；选中后只返回 `api_call`，不返回参数树。API EID 不属于指定 action 时返回 `INVALID_API_EVENT_ID`。

```python
get_action_api_calls(action_event_id=343)  # 例如关联 API EID 340–343
get_action_api_calls(action_event_id=343, offset=50)  # has_more 为 true 时继续
get_action_api_calls(action_event_id=343, api_event_id=343)  # vkCmdDrawIndexed 参数
# 使用上一步返回的 child_path 展开具体参数：
get_action_api_calls(action_event_id=343, api_event_id=341, child_path=[0])
```

---

#### `get_action_details`

获取 action 的元数据、绘制计数、偏移及输出资源。
关联 API 调用及参数树请使用 `get_action_api_calls`。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action_event_id` | `int` | 是 | action 的 event ID |

**返回值：** `action_event_id`、`action_id`、`name`、`flags`、绘制计数（`num_indices`、`num_instances`）、绘制偏移、`outputs` 和可选的 `depth_output`。
返回值使用 `action_event_id` 标识 action 的 EID；`action_id` 是独立的 action 序号。

**示例：**
```
get_action_details(action_event_id=123)
```

---

#### `get_action_timings`

获取 action 的 GPU 时间信息。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `action_event_ids` | `list[int]` | 否 | | 指定的 event ID 列表。省略时返回所有 action。 |
| `marker_filter` | `str` | 否 | | 仅包含标记路径中包含此字符串的 action |
| `exclude_markers` | `list[str]` | 否 | | 排除标记路径中包含这些字符串的 action |

**返回值：** `{"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}`

> **注意：** GPU 时间计数器在某些硬件/驱动上可能不可用。如果 `available` 为 `false`，则无法获取时间数据。

**示例：**
```
# 所有 action
get_action_timings()

# 指定 event ID
get_action_timings(action_event_ids=[100, 200, 300])

# 按 marker 过滤
get_action_timings(marker_filter="Camera.Render", exclude_markers=["GUI.Repaint"])
```

---

### 组合分析

在原子工具之上编排多个服务的跨维度复合查询，帮助快速获得全局视图。

#### `inspect_action`

对单个 action 做复合检查，返回紧凑的详情、时间、shader 摘要、管线摘要与网格摘要。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action_event_id` | `int` | 是 | 要检查的 action EID ID |

**返回值：** event 详情、时间、shader 摘要、管线摘要、网格摘要。

**示例：**
```
inspect_action(action_event_id=1517)
```

---

#### `trace_resource_usage`

追踪资源在匹配事件中的读取、写入与消费过程。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 要追踪的资源 |
| `marker_filter` | `str` | 否 | | marker 路径子串过滤 |
| `exclude_markers` | `list[str]` | 否 | | 要排除的 marker 子串 |
| `event_id_range` | `dict` | 否 | | event 范围，格式为 `{"min": ..., "max": ...}` |
| `before_event_id` | `int` | 否 | | 计算此 event 之前的最近写入者 |
| `categories` | `list[str]` | 否 | 全部 | Timeline 分类多选：`read`、`write`、`read_write`、`barrier`、`clear` |
| `offset` | `int` | 否 | `0` | 过滤后的分页偏移 |
| `limit` | `int` | 否 | `100` | 每页 1–500 项 |

**返回值：** `available`、紧凑 `resource`、分页 `events`、分页字段、用途/读写统计及写入事件摘要。统计与写入摘要基于分页前全部匹配记录；`before_event_id` 只影响此前写入摘要。事件保留原始 `usage`、可选 `view_resource_id`、marker 和推导的 `access`（`access_source: "usage_classification"`）。缺失 action 的记录仍保留 EID/usage；指定 marker 条件时无法确认 marker 的记录不匹配。不适用与成功空结果分别表达。首版不合并 UI 的 EID 区间。

每条事件新增 `category`，汇总的 `category_counts` 始终包含五类（含零计数），对应 Timeline 的 Reads / Writes / Read/Write / Barriers / Clears。

- `GenMips`、`Copy`、`Resolve` 及各 shader 的 RWResource 属于 `read_write`。
- `Clear` 和 `Discard` 属于 `clear`；`Barrier` 属于 `barrier`。
- StreamOut、ColorTarget、DepthStencilTarget、CopyDst、ResolveDst、CPUWrite 属于 `write`；其余按 Timeline 默认分支归为 `read`。

`categories` 内为 OR，与 marker/事件范围条件为 AND。省略表示全部，`[]` 表示不选任何分类，非法分类返回参数错误。所有计数、分页总数及写入摘要均基于**全部筛选后、分页前**的记录。分类计数是 usage 记录数，不是去重 EID 数或屏幕上可能合并的三角标记数；同一 EID 的多条 usage 保留。

原始 `usage`、`usage_counts` 完整保留。已有 `access`、`read_count`、`write_count` 保持原先的读写语义，与 Timeline 分类独立，例如 Clear 仍计为写入，GenMips 的旧 access 仍为 write。对齐面板时使用 `category` 与 `category_counts`。

分类依据：[RenderDoc TimelineBar.cpp](https://github.com/baldurk/renderdoc/blob/v1.x/qrenderdoc/Windows/TimelineBar.cpp)。

**示例：**
```
trace_resource_usage(resource_id="ResourceId::2495")
trace_resource_usage(resource_id="ResourceId::2495", categories=["barrier", "clear"], limit=50)
trace_resource_usage(resource_id="ResourceId::2495", marker_filter="Forward", before_event_id=1517)
```

---

#### `trace_action_dependencies`

追踪单个 action 的直接资源依赖。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action_event_id` | `int` | 是 | 要检查的 action EID |

**返回值：** 按阶段分组的输入资源、输入装配缓冲区、输出资源、主要输入的候选 producer event。

**示例：**
```
trace_action_dependencies(action_event_id=1517)
```

---

#### `diff_actions`

对比两个 action，突出关键状态差异。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action_event_id_a` | `int` | 是 | 第一个 action EID |
| `action_event_id_b` | `int` | 是 | 第二个 action EID |

**返回值：** shader、资源绑定、绘制参数、网格和时间差异。

**示例：**
```
diff_actions(action_event_id_a=100, action_event_id_b=200)
```

---

#### `analyze_pass`

将一个 marker 子树或 pass 汇总为一个整体工作负载。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `marker_filter` | `str` | 是 | | marker 路径子串，用于选择 pass 子树 |
| `exclude_markers` | `list[str]` | 否 | | 要排除的 marker 子串 |

**返回值：** action 数量、主要 shader、代表性资源、耗时最高的 action、保守的工作负载警告，以及 `scan_failures`/`scan_error`（部分 action 无法读取时的计数与原因）。

**示例：**
```
analyze_pass(marker_filter="ShadowPass")
analyze_pass(marker_filter="Forward", exclude_markers=["GUI"])
```

---

## 上层工具能力

### 资源导出

#### `save_texture`

将纹理保存为图片文件。自动处理格式转换。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID（如 `"ResourceId::2495"`） |
| `action_event_id` | `int` | 否 | UI 当前事件 | 读取指定 action 执行后的内容，随后恢复 replay |
| `output_path` | `str` | 是 | | 输出文件路径（如 `"D:/output/texture.png"`） |
| `format_type` | `str` | 否 | `"PNG"` | 输出格式：`"PNG"`、`"JPG"`、`"BMP"`、`"TGA"`、`"EXR"`、`"DDS"`、`"HDR"`；未知值报 `INVALID_FORMAT_TYPE`，不再静默回退 PNG |
| `mip` | `int` | 否 | `0` | 要保存的 mip 级别（`-1` = 所有 mip；**仅 DDS 会真正写出全部 mip**，其他格式 RenderDoc 实际保存 mip 0，响应以 `mip_selection` 报告实际保存范围并附 `mip_note`） |
| `slice_index` | `int` | 否 | `0` | 数组切片或立方体贴图面索引（0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-） |
| `alpha_mode` | `str` | 否 | `"preserve"` | Alpha 处理：`"preserve"`、`"discard"`、`"blend_to_black"`；未知值报 `INVALID_ALPHA_MODE` |

**返回值：** `{"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}`，
含 `color_space`（描述**源纹理**的存储色彩域 `srgb`/`linear`）。注意导出文件中的数值域
取决于输出格式与转换路径——部分格式（如 DDS）会保留源格式与编码，不能一概假定"已解码"
或"未解码"，请按实际导出格式处理。

**示例：**
```
# 保存为 PNG
save_texture(action_event_id=123, resource_id="ResourceId::123", output_path="D:/output/texture.png")

# 保存为 JPG，alpha 混合到黑色背景
save_texture(action_event_id=123, resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG", alpha_mode="blend_to_black")

# 导出所有 mip 级别为 DDS
save_texture(action_event_id=123, resource_id="ResourceId::2495", output_path="D:/output/texture.dds", format_type="DDS", mip=-1)
```

---

#### `export_mesh_csv`

将网格数据导出为 CSV 文件。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `action_event_id` | `int` | 是 | | draw call 的 event ID |
| `output_path` | `str` | 是 | | 输出文件路径（如 `"D:/output/mesh.csv"`） |
| `stage` | `str` | 否 | `"VSIn"` | 网格数据阶段：`"VSIn"`、`"VSOut"`、`"GSOut"` |
| `attributes` | `list[str]` | 否 | | 过滤特定属性。省略时包含所有属性。 |
| `instance` | `int` | 否 | `0` | 实例索引，用于 per-instance 属性与 post-VS 数据选择 |

**返回值：** `{"success": true, "output_path": "D:/output/mesh.csv", "index_path": "D:/output/mesh.idx", "vertex_count": 3024, "index_count": 9072, "exported_attributes": ["_input0", "_input1"], "skipped_attributes": []}`

没有任何可导出属性时（例如 post-VS 签名格式为 `Undefined`，所有属性都被判定为
special）直接报 `MESH_SIGNATURE_UNAVAILABLE`，**不会**再写出只有 `VTX,IDX` 的“成功”
文件。`skipped_attributes` 列出被跳过的属性名。

**CSV 格式说明：**
- 第一行：`VTX,IDX,in_POSITION0.x,in_POSITION0.y,...`（VSOut/GSOut 列名来自输出签名，如 `SV_POSITION0.x`）
- VTX：去重后的顶点索引
- IDX：原始顶点索引
- 索引 sidecar 文件（`.idx`）：重映射后的三角形流

**示例：**
```
export_mesh_csv(action_event_id=1234, output_path="D:/output/mesh.csv", stage="VSIn", attributes=["POSITION", "NORMAL", "TEXCOORD"])
```

---

#### `dump_draws`

一次 IPC 请求批量导出 draw 的几何与材质相关状态。需要已加载捕获。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `action_event_ids` | `list[int]` | 是 | | 1–256 个 draw 的 action EID |
| `mesh_dir` | `str` | 条件必填 | | `export_meshes=true` 时必须提供；保存 `vsIn_<EID>.csv` 和 `.idx` |
| `texture_dir` | `str` | 条件必填 | | `export_textures=true` 时必须提供；保存 `tex_<资源数值ID>.png` |
| `export_meshes` | `bool` | 否 | `true` | 导出 VSIn 网格，固定使用 instance 0 |
| `export_textures` | `bool` | 否 | `true` | 导出 vertex/fragment 阶段输入贴图，本次请求内按资源 ID 去重 |
| `max_textures` | `int` | 否 | `48` | 本次请求选取的不同贴图导出数量上限；复用已有同名文件也占额度 |
| `summary_path` | `str` | 否 | | 完整结果的 JSON 路径；省略且提供 `mesh_dir` 时使用 `<mesh_dir>/_batch_summary.json` |

**返回值：** 有汇总路径时返回 `summary_path`、`draw_count`、`ok_count`、
`failed_count`、`textures_saved` 和最多前 5 个失败条目 `failed`。完整 JSON 包含
`draws`、`textures`、`textures_deferred` 及 draw 计数；没有汇总路径时直接返回完整结果。
每个成功 draw 包含网格路径（启用导出时）、`vertex_shader`、`pixel_shader`、
`constants`（常量缓冲范围）、`textures`、`blend`、`depth` 和 `object_matrix`。
单个 draw 处理失败时记录 `ok=false` 和 `error` 并继续；非 draw 条目记录
`skipped="not_a_draw"`，不计入成功或失败数。

**导出范围：** PNG 固定使用 mip 0、slice 0 并保留 alpha；跳过宽或高超过 4096
以及匹配深度格式标记的纹理。已有同名 PNG 直接复用，网格和汇总 JSON 会覆盖。
`object_matrix` 仅尝试读取 vertex 阶段大小为 720 字节的常量绑定，从绑定偏移取前
16 个 float；这是特定布局假设，需核对 shader 后才能当作物体变换。未找到时为 `null`。

**示例：**
```python
dump_draws(action_event_ids=[343, 350], mesh_dir="D:/output/meshes",
           texture_dir="D:/output/textures")

# 只查看状态，不导出文件；直接返回完整结果
dump_draws(action_event_ids=[343], export_meshes=False, export_textures=False)
```
