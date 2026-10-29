# RenderDoc MCP 使用契约（共用）

本契约自包含：不依赖仓库内其他文档即可使用。工具名与响应字段以**实际发现的 MCP 工具
schema 与响应为准**——以下记录的是当前已知的能力面与语义，作为阅读 schema 时的地图，
不是替你跳过发现步骤。完整参数及默认值见仓库 `docs/tool_schemas.json`，版本迁移
历史见 `docs/migration_v3.md`。

## 1. 工具发现优先

- 每次会话先列出可用的 MCP 服务器与工具，读取其 schema，再选择方法。
- 不假设函数签名、参数名或服务别名；不同版本的扩展可能增删工具或改名。
- 按能力选择工具：能用现有工具组合完成的，不引入原生脚本或 UI 补取。

## 2. 健康核对是固定第一步

任何业务查询之前，先调用状态/健康类工具核对：

- 捕获是否加载、图形 API、文件名；
- **回放健康**：响应中的 replay 健康字段（如 `replay_healthy`/`replay_error`）；
- 版本与协议一致性：扩展版本、RenderDoc 版本、IPC 协议版本与预期是否相符
  （当前 API 契约为 **3**、文件 IPC 为 **2**；MCP 服务器与扩展必须成套同版本，
  混部直接报 `API_VERSION_MISMATCH`，不会进入部分兼容模式）。

断连、fatal 或 API 不一致时回放查询直接失败，不返回看似合法的空管线。健康核对不通过
时先排障（见故障诊断方法），不要带病进入分析或重建；需要证据时用
`get_replay_diagnostics` 取不依赖 UI/回放线程的本机诊断包（返回路径、哈希与告警）。
诊断日志只保存请求元数据、阶段、UTC 时间、耗时和读回字节数，不保存完整像素、缓冲和
shader；请求/IPC 日志各轮转三份、每份 10 MiB，本机/设备日志摘录各上限 2 MiB，不自动
上传证据。设备日志默认关闭，只有用户要求或明确同意采集时才设置
`include_device_logs=True`：设备诊断复用已配置 ADB，仅调用 get-state、shell ps -A 和
有界 crash logcat，总时限 20 秒，不执行安装、reset 或服务重启；ADB 服务不存在时降级为
不可用，设备证据失败仍交付本机包。版本不符的旧捕获结论不能直接沿用。

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
  （网格为绘制引用序列），缓冲区读取的 `offset`/`length` 单位是字节。
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
- `get_texture_data` 的 `output_mode` 为 auto/inline/file：auto 下原始负载 <=256 KiB
  内联返回，更大负载落盘为带 SHA-256 的二进制文件 + JSON sidecar（默认目录为系统
  临时目录 renderdoc_mcp/artifacts/<session>/<unique-id>/，响应保留路径、字节数与
  `metadata_path`，不重复大块数据）；强制 inline 超过 256 KiB 报 `RESOURCE_LIMIT`。
  消费时按 `output_mode` 分支，auto/file 读取返回的 path 与 `metadata_path` 并核验
  哈希，不要求 `content_base64` 恒存在。
- `aspect` 为 all/depth/stencil：D16、D24S8 已验证，depth 输出归一化 float32 LE、
  stencil 输出 uint8；其他未验证格式只保留原始导出并标记 `layout_available=false`，
  拒绝猜测解码。`region={x,y,width,height}` 用左上原点选择 ROI，上限 262144 像素，
  原始子资源上限 64 MiB；元数据区分 source_format/output_format、端序、
  row_pitch/slice_pitch、通道/位布局、原点、数值域、sample 和 provenance。
- `save_texture` 仍是可视图片转换，不能替代上述数值导出。
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

## 6. 作业、来源与数值验证

- 要求 MCP 与扩展均为 3.1.0、RenderDoc >=1.46、API contract=3；核对构建指纹。
- open_capture/dump_draws/export_shader_bundle/compare_texture_events/get_pixel_history/run_script
  返回 job_id。通过 get_job_status 查询；paused 可补充纹理额度，cancel/resume 为协作操作。
  原生调用不能强行取消。stalled 或提交超时不证明失败，保留原 job_id 查询，勿盲目重试。
  RESULT_PENDING 代表提交后结果未知，不可自动重提；IPC 临时文件访问冲突只重读同一
  响应，不重复提交原生操作，清理失败不丢已验证结果；排查断连时最后成功调用不能直接
  认定为原因。
- file_location 区分本地/远端文件；replay_target 区分回放位置。远端路径不创建本地占位。
- 作业期间其它回放查询返回 REPLAY_BUSY；健康探针未运行时不把 null 当健康成功。
- 缓存和产物绑定 capture_session、replay_revision、事件与子资源；跨加载或替换失效。
  所有服务共享 capture_session/replay_revision；shader 编辑器自身代次是独立的
  edit_session；重开捕获后 binding_id 与旧作业一并失效。
- run_script 需要服务器环境变量 RENDERDOC_MCP_ALLOW_SCRIPTS=1；脚本为 Python 3.6 语法，
  在 replay 线程单步执行，注入 pyrenderdoc/controller、renderdoc/rd 与 mcp 助手
  （progress/log/cancelled/check_cancel/artifact/set_result/keep_event）。取消只在脚本调用
  mcp.check_cancel() 处生效；作业不可 resume（JOB_NOT_RESUMABLE），重跑换新 job_id；
  脚本全文落 jobs/<job_id>/script.py，异常落 traceback.txt。
- dump_draws 默认 `export_constants=True`，export_shader_bundle 默认
  `include_event_context=True` 且 `export_constants=True`：逐事件保存原始常量、完整
  布局与解码值，并关联事件绑定、采样器与签名；只要 shader 证据时可显式关闭。常量按
  事件和有效绑定范围读取，不跨事件仅凭 buffer ID/offset 命中缓存。常量 JSON 保存
  类型、数组/矩阵 stride、存储与解码顺序，附原始字节文件和哈希；相同内容可去重，但
  来源记录分别保留。合法未绑定项标记 skipped；必要导出失败进入错误清单并影响完成
  状态。完整常量值不进入工具响应或作业摘要。
- 常量按绑定反射路径与布局读取；GetConstantBlock 已含 dynamic offset。原始字节的矩阵
  主序/stride 与 ShaderVariable 解码后的 row-major 数值分开记录。SInt 使用 s32v。
- 不从块大小、槽位、固定步长或数值形状推断 ObjectToWorld。矩阵只来自反射确认；
  语义需 shader 证据。没有反射时不扫描任意 buffer 猜变换。
- post-VS 使用原生返回的重映射索引；分页按绘制引用，CSV 顶点表去重，.idx 保留 restart。
  用完整 xyzw、NDC 或屏幕位置核验。恒值输出先核对独立原生读取，不预判未落盘或不可用。
- Shader 大文本用 export_shader_bundle 落盘。ROI 使用 compare_texture_events 数值差分；
  默认 storage 域，linear 仅转换 sRGB RGB；`aspect=all/depth/stencil` 可对指定 MSAA
  样本做颜色/深度/模板数值比较，不隐式 resolve。差分是观测结果，不等于独立 draw 贡献。
- get_pixel_history 是原生历史；先核对能力与数值有效性，不能用 ROI 差分冒充。

## 7. 禁止事项

- 绕过 MCP 直接用原生脚本读取 RDC 或调用 RenderDoc 内部接口——除非用户显式授权，
  并如实标注来源。
- 把 UI 或原生补取的结果记成纯 MCP 成功。
- 在未核对健康的情况下把空结果当真值进入下游。
