# RenderDoc MCP 使用契约（共用）

本契约自包含：不依赖仓库内其他文档即可使用。工具名与响应字段以**实际发现的 MCP 工具
schema 与响应为准**——以下记录的是当前已知的能力面与语义，作为阅读 schema 时的地图，
不是替你跳过发现步骤。

## 1. 工具发现优先

- 每次会话先列出可用的 MCP 服务器与工具，读取其 schema，再选择方法。
- 不假设函数签名、参数名或服务别名；不同版本的扩展可能增删工具或改名。
- 按能力选择工具：能用现有工具组合完成的，不引入原生脚本或 UI 补取。

## 2. 健康核对是固定第一步

任何业务查询之前，先调用状态/健康类工具核对：

- 捕获是否加载、图形 API、文件名；
- **回放健康**：响应中的 replay 健康字段（如 `replay_healthy`/`replay_error`）；
- 版本与协议一致性：扩展版本、RenderDoc 版本、IPC 协议版本与预期是否相符。

健康核对不通过时先排障（见故障诊断方法），不要带病进入分析或重建。版本不符的旧捕获
结论不能直接沿用。

## 3. 读取策略：先概要，后分页，大文件落盘

1. 先取紧凑概要（帧摘要、action 树的过滤子集、网格摘要、资源目录分页）。
2. 锁定目标事件/资源后，再按分页读取明细（网格顶点、常量树、资源初始化目录）。
3. 大网格与大纹理一律导出为文件（CSV/图片），不在对话中倾倒数组。
4. 信息质量和正确性优先于调用次数；但要避免重复读取同一数据——配合证据契约的缓存键。

## 4. 术语与字段约定

- `ResourceId`：捕获内**所有** API 对象的统一标识，规范形式 `ResourceId::数字`——
  不只纹理/缓冲区，还包括 Device、Shader、View、Sampler、Memory、管线等全部类型，
  与 RenderDoc Resource Inspector 的对象目录同源。需要统计/枚举全部资源时用资源
  目录工具（默认全类型，支持类型与名称过滤、排序、分页）；单对象的详情、父/派生
  关系与初始化调用用资源检查类工具。注意 usage/Timeline 追踪只对纹理和缓冲区有
  意义，其他类型会返回不支持。`ResourceId::0` 是空绑定哨兵，表示"该槽位无绑定"。
- `action_event_id`：action 的事件编号（EID），绝大多数 action 类接口的统一入参；
  列表与范围用复数形式；关联的单条 API 调用用 `api_event_id`；独立的 action 序号是
  `action_id`，**不能**当 EID 使用。少数直接查询回放状态的接口用通用 `event_id`。
- Shader 阶段统一名称：`vertex` / `tess_control` / `tess_eval` / `geometry` /
  `fragment` / `compute`；接受 pixel/PS/FS、hull/HS、domain/DS 等别名输入。
  管线的 `vertex_input` / `rasterizer` / `framebuffer` 不是 Shader 阶段。
- 网格数据位置：`VSIn`（顶点着色器输入，含 per-instance 属性）/ `VSOut`（顶点输出）/
  `GSOut`（最后活动阶段的最终输出，可能是 Geometry 或曲面细分）。
- 纹理子资源：数组层/立方体面用 `slice_index`，3D 的 Z 切片用 `depth_slice`，
  MSAA 用 `sample`；网格属性筛选用 `attributes`；分页 `offset`/`limit` 单位是条目
  （网格为顶点），缓冲区读取的 `offset`/`length` 单位是字节。
- 绑定类接口的 `binding_id` 是临时令牌：只在同一捕获、同一 action 的上一条响应内有效，
  不能跨 action 或跨查询复用。
- 逐实例数据：网格类接口的 `instance` 参数选择实例；超界会收到参数错误，先查
  action 的实例数再选值。

## 5. 响应语义要点

- 错误有稳定码前缀（`INVALID_*` 为参数问题，`CAPTURE_NOT_LOADED` /
  `RESOURCE_NOT_FOUND` / `RESOURCE_QUERY_FAILED` / `MESH_SIGNATURE_UNAVAILABLE` /
  `REPLAY_RESTORE_FAILED` 等为运行时问题）。收到错误先读前缀分类，再决定重试或上报。
- 网格后处理（VSOut/GSOut）数据的属性布局由服务端按目标管线输出签名推导并校验；
  报 `MESH_SIGNATURE_UNAVAILABLE` 说明签名或布局提示缺失，应换方法（如改读 VSIn 或
  检查该阶段是否真的有输出），不要自行猜偏移解析原始缓冲。
- 纹理数据响应携带 `color_space`、`all_zero`、`warnings` 等诊断字段，消费前先读；
  纹理导出响应以 `mip_selection` 报告实际保存的 mip 范围。
- 状态类工具返回回放健康与版本信息；把它的响应当作每次长程操作的入口检查点。
- `get_buffer_contents` 按**数值 ID** 匹配（`ResourceId` 不能由 int 构造）；
  单次内联上限 256 KiB，超出返回 `truncated=true` 与 `next_offset`，按该偏移分页；
  资源不存在报 `BUFFER_NOT_FOUND`，`offset` 超出缓冲报 `INVALID_PAGINATION`。
- `search_actions` 的 `complete=false` / `stopped_reason` / `next_event_id` 是**截断**而非
  空结果；`scan_mode="usage"` 表示候选来自 Timeline usage 索引（较快），`"pipeline"`
  表示逐 action 扫描。续扫用 `start_event_id=next_event_id`，大捕获上先给
  `action_event_id_range` 缩小范围。
- `get_mesh_summary` 的 `topology` 取自管线状态（`topology_source="pipeline"`）；
  `num_vertices` 保留 draw 的 numIndices；新增 `unique_vertex_count` 为去重引用顶点数
  （索引不可读时为 null，`indices_available=false`）；反射名被剥离时位置流由启发式推断，看
  `bounding_box_source` / `bounding_box_basis` / `bounding_box_inferred`，并用
  `bounding_boxes` 核对其它三分量属性。
- `export_mesh_csv` 在没有任何可导出属性时报 `MESH_SIGNATURE_UNAVAILABLE`（不会再写出
  只有 `VTX,IDX` 的“成功”文件）；`exported_attributes` / `skipped_attributes` 用于
  核对实际写入磁盘的内容。

## 6. 逐对象变换：先看 shader，再读第二个常量绑定

阴影/角色/合批对象常常"用共享矩阵投影后落在错误位置"，这不代表几何不可还原。
先确认 VS 实际怎么算位置，再决定读哪个绑定：

1. `get_shader_info(event_id=<draw>, stage="vertex")` 读 SPIR-V 的 `main()`，找到写入
   `BuiltIn(Position)` 的那条链。常见形态是 `clip = MVP @ (S @ position)`：`MVP` 来自
   一个 `float4[4]`（std140 里通常是 `Offset(288)`），`S` 来自**另一个** `DescriptorSet`
   的 `Binding`（例如 `set 1, binding 2` 的 `_child0`，`Offset(0)`）。
2. `get_pipeline_stage(action_event_id, stage="vertex", section="constant_buffers")` 给出每个
   绑定的 `buffer_range.byte_offset` 与 `byte_size`；`binding_name` 与反射索引可对上结构体。
3. `get_buffer_contents(resource_id, offset, length)` 读块。`S` 只需前 **64 B**：按**列主序**
   解 4×4（前 3 个 float4 是 3×3，第 4 个是平移，`w=1`）。校验 3×3 行/列正交且 `det≈1`，
   否则说明选错了绑定或结构体。
4. 闭合验证：`clip = MVP @ S @ v` 与 `get_mesh_data(stage="VSOut")` 的 clip 逐分量比对；
   `z` 应到 1e-6 量级。**若 VSOut 全是同一个常量**（该 draw 的 post-VS 数据未落盘），
   这只是采样不可用，不代表变换错误——改用 NDC 包围盒与参考截图核对。
5. 放进 DCC 时不要重新推导相机：保持 `world = CameraToWorld @ ModelView @ S`，相机用
   `CameraToWorld`，等价于让 DCC 复算 `P @ View @ world @ v = MVP @ S @ v`。

槽位提示：同类 draw 的常量块常以固定步长连续分配且与 draw 顺序一致。用 2–3 个已知
`byte_offset` 拟合 `offset = base + stride × index`，命中后再批量直读，可省掉逐 draw 的
`get_pipeline_stage`。

## 7. 禁止事项

- 绕过 MCP 直接用原生脚本读取 RDC 或调用 RenderDoc 内部接口——除非用户显式授权，
  并如实标注来源。
- 把 UI 或原生补取的结果记成纯 MCP 成功。
- 在未核对健康的情况下把空结果当真值进入下游。
