# RenderDoc MCP Server 重构：评估与修订

> 版本：2026-10-20  
> 性质：架构评估 + 修订后的方案，不含实现代码。  
> 约束：本次**只做静态分析**，没有启动或尝试启动任何 RenderDoc 进程（qrenderdoc/renderdoccmd/renderdoc/wscript/cscript/Start-Process/--ui-python/LoadCapture），没有做实机回放、UI 操作、双实例、headless 导入、shader 编译或 MCP 客户端抓包。  
> 证据基线：仓库代码逐行阅读；RenderDoc 源码来自 `D:/Projects/renderdoc`，分支 **`feature/renderdic_customhook`**，`git describe --tags --long` = **`v1.45-354-g5f3763615`**，commit `5f3763615e5717e41b826bb392cd554a9a782fb6`（2026-10-03）。这不是干净的 v1.x 或 master：`git log v1.45..HEAD` 显示 qrenderdoc UI 文件有 fork 改动（包括“同步上游 RenderDoc v1.46 并保留 RenderDic 扩展”）。因此本文 UI 结论只对该 checkout 成立；目标发布版本必须先固定。  
> 本次实际执行的检查：`rg -c "^@mcp.tool" mcp_server/server.py` → 30；`./.venv/Scripts/python.exe` 调 `mcp.list_tools()` → 30 个工具、`annotations=None`、`get_capture_status` 的 `output_schema={"additionalProperties": true, "type": "object"}`；`rg -a -o "PYTHON3[0-9]\.dll" D:/Projects/renderdoc/x64/Release/pymodules/renderdoc.pyd` → `PYTHON36.dll`；`./.venv/Scripts/python.exe -V` → 3.12.9；`python -V` → 3.13.9；`find D:/Projects/RenderDoc_Pro_1.36_64 -maxdepth 2 -iname 'renderdoc.pyd'` → 无结果（只有 `python36.dll`）；`./.venv/Scripts/python.exe -c "find_spec('docket')"` → `ModuleSpec(...site-packages\docket\__init__.py)`；`python - <<PY` 的 SQLite FTS5 测试（见 §7.7）；`rg` 读取 `mcp/types.py:27` → `LATEST_PROTOCOL_VERSION = "2025-11-25"`。  
> 输入材料：第一版评估 `.zcode/workflow-drafts/first-evaluation.md`；上一轮草案 `out/renderdoc-mcp-refactor-draft.md`（**已被本文取代**；其中 D3D11 GetUsage、headless 可选性等结论有误，以本文为准）；四份调研【MCP 规范】【RenderDoc 能力】【仓库现状】【同类实践】以及两轮复核意见是本次对话输入，**不在仓库中**，无法用 git 历史追溯。  
> 术语：**headless** = 独立进程加载 `renderdoc` 模块回放，不启动 UI；**WARP** = D3D11/12 的软件光栅化回退；**SD** = RenderDoc 的 structured data（序列化 API 数据）；**FTS5** = SQLite 全文检索扩展；**mailbox** = 每实例的请求/响应目录；**operation/job** = 带 id、状态、结果的异步操作；**generation** = 一次 capture 加载的代际（同路径重开即新代际）；**replay cursor** = ReplayController 当前 `SetFrameEvent` 的位置；**UI context** = 已提交的 event/资源/面板状态快照。

---

## 0. 决策摘要：现在做什么、先不做什么

**现在做（按顺序）：**

1. **先交付单实例 v1，注册 15 个工具**（`rd_index` 在 step 7 前不注册，见 §8）。内容包括：工具契约、annotations/outputSchema、结构化错误、载荷文件化、capture 代际、UI 快照/导航。它不依赖 headless，也不依赖多实例 IPC。
2. **把 `rd_capture_open` 改成 operation 模型**：返回 `operation_id`，由 `rd_job` 轮询；默认 `launch_if_missing=false`、`new_instance=false`，**不默认启动新实例**。对大 capture 或没有现成实例的场景，调用方显式传 `new_instance=true` 或 `launch_if_missing=true`。
3. **并行做两个有时限的 spike**：headless 模块可用性（Python 3.6 + 匹配的 RenderDoc core + GPU）和 per-instance IPC 双实例隔离。两者都是高风险前置条件，**没有通过之前不承诺** `scope=all_captures` 和多实例切换。
4. **UI 快照只做“可观测的已提交状态”**：用 `Has*()` 保护 getter，绝不因为读上下文而惰性创建面板；用 250ms 轮询补 CaptureViewer 回调覆盖不到的状态；`ui_seq` 只代表已观测字段的变化。
5. **读工具的 replay cursor 恢复改用 replay 线程直接 `SetFrameEvent`**，不用 `SetEventID`，避免触发 `RefreshUIStatus`/EventBrowser 滚动；异步扫描用分批 AsyncInvoke + 导航代际检查。

**先不做：**

- 不做逐面板 1:1 工具；不承诺 Pixel History/API Inspector/Statistics/PerformanceCounter 的 **UI 状态**（但 Statistics 数据、PerformanceCounter 数据可以重建，见 §3.1）。
- 不在 headless spike 通过前做 `all_captures` 索引/搜索；不做一个“看起来支持全部 capture、实际只覆盖已打开 capture”的搜索。
- 不用 MCP Tasks 作为主路径；不依赖 `resource_link`；不把大二进制 inline base64 作为默认。
- 不在 UI 线程里做长循环；不把 `SetEventID` 当内部 cursor 恢复 API；不在多实例时自动 fallback 到共享 mailbox。
- 不在 v1 支持远程/Android replay；不在默认配置里启动 qrenderdoc 实例。

---

## 1. 原构想、术语与验收

### 1.1 用户原话（据输入）

| 层 | 原始诉求（用户输入） | 验收标准（本文建议，不是用户原话） |
|---|---|---|
| 基础层 | “完全复刻 RenderDoc 的面板，同步 renderdoc 前端 UI 的刷新（例如跳转到对应 drawcall 的时候就应跳过去）。” | 主分析面板的数据/信息模型可查询；导航会驱动 EventBrowser 选中/滚动；能显示对应面板；不要求像素/布局复刻。 |
| 交互层 | “可以通过读取用户现在在 renderdoc 前端的候选状态进行辅助调整，例如跳转到用户要求的操作。” | 能读出已提交的 event/资源/面板状态，用于“这个 drawcall/这张 texture”的指代；不承诺 hover/未确认候选。 |
| 进阶层 | “为高级操作以及超广度搜索执行指引，例如针对一个 texture 的整个 rdc 搜索、模糊搜索、\|\| 搜索等，或者联合多个 renderdoc 实例之间的切换、自由打开/切换 renderdoc。” | 单 capture 资源使用搜索；跨 capture 索引/搜索；多实例路由；可显式启动/切换；长任务可追踪。 |

**哪些是本文的重定义：** “基础层 = 主分析面板语义对等 + 导航同步”是本文的重定义，不是用户原话；用户原话是“完全复刻面板”。本文认为字面复刻不可行（§3.1），因此把它降级为可验收的语义对等。类似地，“交互层 = 显式 UI context”是本文的重定义；“进阶层 = operation + per-instance IPC + headless”也是本文的工程化拆解。阅读时不要把本文的重定义当成用户原意。

### 1.2 关键术语（6-8 个词）

- **headless**：独立 Python 进程加载 `renderdoc` 模块并 `OpenCapture`，不启动 qrenderdoc UI；需要与 Python ABI 匹配的 `renderdoc.pyd`。
- **WARP**：D3D11/12 的软件光栅化回退；没有独显时仍可能 replay，但性能/兼容性有限。
- **SD**：RenderDoc 的 structured data；`CaptureFile.GetStructuredData()` 可解码 API 数据而不做 graphics API 调用，适合无 GPU 的浅层解析。
- **FTS5**：SQLite 全文检索；支持 token/prefix/OR/trigram substring，不内建编辑距离模糊。
- **mailbox**：每实例一个目录，放 request/response/heartbeat；用来替代当前全局单槽。
- **operation/job**：带 opaque id、状态、进度、结果路径的异步操作；用于 capture 加载、深扫描、索引。
- **generation**：一次 capture 加载的代际；同一路径重开必须产生新 generation。
- **replay cursor**：ReplayController 当前的 `SetFrameEvent` 位置；与 UI 的 `CurEvent`/`CurSelectedEvent` 不是同一概念。

---

## 2. 总体判断与五维切分

### 2.1 总体判断

三层需求是真实的，但它是**产品能力成熟度/路线图的切分**，不是代码模块或工具面的分类轴：

- “基础层”是数据读取 + 主分析面板的语义对等；
- “交互层”不是一层工具，而是所有工具共享的**上下文输入**；
- “进阶层”混合了跨 capture 搜索、长任务、多实例路由、进程生命周期和副作用，彼此正交。

作为路线图，“先数据、再上下文、再跨实例/跨捕获”基本正确；作为架构，应该按**状态所有者 + 执行位置 + 作用域 + 副作用 + 载荷**切。

### 2.2 五维矩阵

| 维度 | 取值 | 设计含义 |
|---|---|---|
| 状态所有者 | server / extension / headless worker | 谁持有权威状态，谁能崩溃/重启 |
| 执行位置 | UI 线程 / replay 线程 / 独立进程 | 是否阻塞 UI，是否占用 replay |
| 作用域 | event / capture / capture file / workspace | 需要什么 handle，是否需要索引 |
| 副作用 | 读 / 改 UI / 改 replay 状态 / 写文件 / 改 capture | annotations 与二次确认 |
| 载荷 | 小内联 / 文件 / 图像内容 / job 结果 | token 与客户端能力 |

### 2.3 三层裁决摘要

| 层 | 裁决 | 一句话理由 |
|---|---|---|
| 基础层 | **按字面“完全复刻面板”不可行；主分析面板语义对等 + 导航有条件可行** | qrenderdoc 只暴露部分面板的数据模型；UI 状态不可读，但 Statistics/PerformanceCounter 数据可重建；`View*` 必须 `AddDockWindow`/`show`。 |
| 交互层 | **有条件可行** | 可读已提交的 event/资源/面板状态；读不到 hover/候选/全局 selected resource；`Get*` 惰性构造会创建隐藏面板，必须 `Has*` 保护。 |
| 进阶层 | **有条件可行；现有 IPC 上按当前描述不可行** | 单 capture `GetUsage` 便宜；跨 capture 需要 headless/索引；多实例需要 per-instance mailbox；capture 加载会卡 UI 线程。 |

---

## 3. 逐层可行性裁决

### 3.1 基础层：**按字面“完全复刻面板”不可行；“主分析面板语义对等 + 导航”有条件可行**

**不可行的部分（静态已核）：**

1. **面板 UI 状态没有统一 getter。** `Has*()` 只判断单例指针非空（`CaptureContext.h:237-265`）；`Get*()` 首次调用会创建窗口并 `setupDockWindow(..., true)` 立即 hide（`CaptureContext.cpp:2347-2356` GetEventBrowser、`:2383-2392` GetTextureViewer、`:2531-2540` GetResourceInspector、`:2916-2921` setupDockWindow）。`StatisticsViewer` 只有 `Widget()`；`PerformanceCounterViewer` 只有 `Widget()`/`UpdateDurationColumn()`（`QRDInterface.h:1452-1550`）。
2. **没有全局 selected resource。** `ICaptureContext` 只有 `CurEvent/CurSelectedEvent/CurAction/CurSelectedAction`；资源选择分散在 `ITextureViewer.GetCurrentResource()` 和 `IResourceInspector.CurrentResource()`（`QRDInterface.h:826,1043`）。
3. **`View*` 窗口不会自动显示。** `ViewShader/ViewBuffer/ViewTextureAsBuffer/ViewPixelHistory` 只 new 窗口，不 show、不 dock（`CaptureContext.cpp:2746-2812`）；文档写 “opened, but not shown”（`QRDInterface.h:3298-3395`）。`RaiseDockWindow()` 只在父级是 `ToolWindowManagerArea` 时切 tab，否则只 warning（`ToolWindowManager.cpp:549-569`）；必须 `AddDockWindow`（`CaptureContext.cpp:2972-3000`）或 `Widget().show()`。
4. **不能从 viewer 接口读 UI 状态，不等于数据不能重建。** 复核意见正确指出：`StatisticsViewer::GenerateReport` 直接从 `ctx.CurRootActions()/GetTextures()/GetBuffers()/FrameInfo()` 重建统计（`StatisticsViewer.cpp:678-684`）；`PerformanceCounterViewer` 通过 `controller->FetchCounters()` 取数（`PerformanceCounterViewer.cpp:344`；`FetchCounters` 是公开 API，`renderdoc_replay.h:803`）。因此 `rd_overview` 可以交付**语义等价的统计与计数器**；读不到的是 viewer 的行/列/选择/展开状态。上一版把“Statistics/PerformanceCounter 内容”整体排除，是过度收缩，已修正。
5. **`CurPipelineState()` “恒有效”不等于可用。** 无 capture 时它是 `&m_DummyPipelineState`（`CaptureContext.cpp:1570-1572`），工具必须先检查 `IsCaptureLoaded()`。

**可行的部分：**

- Event Browser 的信息模型 → `rd_events`；
- Pipeline State Viewer → `rd_event(sections=pipeline)`；
- Texture Viewer → `rd_resources` + `rd_resource_data` + `rd_ui_act(show_panel=texture_viewer)`；
- Mesh Viewer → `rd_mesh`；
- Shader Viewer → `rd_shader` / `rd_shader_edit`；
- Resource Inspector 的使用链 → `rd_resource_usage`；
- Timeline 时间 → `rd_overview(include_timings=true)` / `rd_event(sections=timing)`；
- Statistics/PerformanceCounter 数据 → `rd_overview(sections=statistics/counters)`；
- “跳到对应 drawcall” → `rd_ui_act(action=navigate)` + `SetEventID`。

**导航细节（静态已核）：** `SetEventID(exclude, selectedEventId, eventId, force=False)` 更新 selected/effective 两个 EID，经 tagged `AsyncInvoke` 执行 `SetFrameEvent` 并同步等待；capture 未加载或 `eventId > m_LastAction->eventId` 时 no-op（`CaptureContext.cpp:1695-1748`；`QRDInterface.h:2424-2436`）。EventBrowser 的 `OnEventChanged` 用 `CurSelectedEvent()` 选中并 `ExpandNode→scrollTo`（`EventBrowser.cpp:4115-4124,5815-5853`）。所以：EventBrowser 必须已存在；`force=True` 才能在同一 event 时也触发；过滤器隐藏该 event 时选中会失败；EventBrowser 的 `OnSelectedEventChanged` 是空实现，真正生效的是 `OnEventChanged`。

**版本边界：** 本结论对应 `feature/renderdic_customhook` / `v1.45-354-g5f3763615`。上一轮复核提到“master 的 AddCaptureViewer 只剩两个回调”，本次没有给出 master commit，也没有在本地复现；本文**删除该说法**，只声明本地 checkout 是三个回调（`CaptureContext.h:135-145`）。目标发布版本必须先固定到官方 tag（例如 1.36/1.46）并重核 UI 行为。

### 3.2 交互层：**有条件可行**

**可读的（已提交状态，不是候选/hover）：**

| 状态 | API | 条件 |
|---|---|---|
| capture/加载 | `IsCaptureLoaded()`、`GetCaptureFilename()` | 无 capture 代际，需要新加 |
| effective event | `CurEvent()` | replay 实际到达 |
| selected event | `CurSelectedEvent()` | 用户选中的行/marker |
| selected/current action | `CurSelectedAction()`、`CurAction()` | |
| Texture Viewer 当前资源 | `GetTextureViewer().GetCurrentResource()` | **只在 `HasTextureViewer()` 为真时调用** |
| 子资源 | `GetSelectedSubresource()` | 同上 |
| display/zoom/overlay/picked/histogram/channel | `GetTextureDisplay()`、`GetZoomLevel()`、`IsZoomAutoFit()`、`GetTextureOverlay()`、`GetPickedLocation()`、`GetHistogramRange()`、`GetChannelVisibility()` | `QRDInterface.h:906-939` |
| Event Browser filter | `GetCurrentFilterText()` | 只在 `HasEventBrowser()` 为真时调用 |
| Resource Inspector 当前资源 | `CurrentResource()` | 只在 `HasResourceInspector()` 为真时调用 |
| 面板是否构造过 | `Has*()` | **不代表可见** |

**读不到的：** hover/未确认候选；全局 selected resource；PipelineStateViewer 当前 stage（只有 `SelectPipelineStage()`）；BufferViewer 当前 instance/view/stage（只有 setter）；ShaderViewer 滚动位置；Statistics/PerformanceCounter viewer 的 UI 状态；面板可见性/焦点（`Has*` 只表示构造过；`Widget().isVisible()` 依赖 PySide2 且未实测）。

**必须处理的三个坑（已按复核修订）：**

1. **惰性构造器不是只读。** 一个标为 `readOnlyHint=true` 的 `rd_ui_context` 如果直接调用 `GetTextureViewer()/GetEventBrowser()/GetResourceInspector()`，会创建隐藏面板、改变布局/会话。实现必须先 `Has*()`，为假时返回 `null` 并标 `fields_unknown`；绝不为了读上下文而创建面板。
2. **CaptureViewer 回调覆盖不全。** 用户只换纹理 tab、mip、zoom、overlay 或 filter 时，未必有 capture/event 回调。`ui_seq` 不能声称覆盖所有 UI 变化；增加 250ms 的 UI 线程轮询，只读已构造面板的 getter，比较 fingerprint；变化时递增 `ui_seq` 并写 `status.json`。状态里带 `observed_at`、`sources`、`fields_unknown`。
3. **恢复 cursor 不能用 SetEventID。** `SetEventID` 末尾 `RefreshUIStatus` 会对所有未被 exclude 的 viewer 调 `OnSelectedEventChanged/OnEventChanged`（`CaptureContext.cpp:1695-1748,1826-1835`），EventBrowser 的 `OnEventChanged` 又会 `SelectEvent→ExpandNode→scrollTo`（`EventBrowser.cpp:4115-4124`）。读工具的内部恢复应直接在 replay 线程 `BlockInvoke(SetFrameEvent(saved, True))`，不触发 UI 回调；异步任务还要检查导航代际，不能把用户在任务期间从 A 导航到 B 的选择覆盖回 A。

**MCP 侧：** 如果协商到 2026-07-28，协议级 session 已移除，跨请求状态必须用显式 handle（【MCP 规范】finding 5；规范页 `https://modelcontextprotocol.io/specification/2026-07-28/server/tools#stateful-tools`）。本仓库 SDK 实际最高 2025-11-25（`mcp/types.py:27`；`mcp/shared/version.py:3`），仍可能有 session，但不应把业务状态寄托在 session 上。`instance_id`/`capture_id` 始终显式传递；默认只在“唯一活实例”时推导，多实例报错。

### 3.3 进阶层：**有条件可行；现有 IPC 上按当前描述不可行**

**现有 IPC 的硬约束（静态已核）：**

- 固定目录、固定 `request.json` 单槽、`host/port` 死参数（`client.py:16-20,35-38`；`socket_server.py:16-19,25-34`）。
- 请求体无 instance/capture 标识（`client.py:91-96`）；两个实例 100ms 轮询同一文件，先 `os.remove` 的赢（`socket_server.py:43-46,74-99`）；任一实例 stop 会删共享文件（`socket_server.py:36-41,52-58,65-72`）。
- 普通工具 30s、5 个 shader 编辑方法 120s（`client.py:22-23,39-40,97`）；超时后扩展仍可能执行并写 `response_<id>.json`；未提交 pending 请求会永久挡住后续调用（`client.py:103-108`；`socket_server.py:107-114`；`tests/test_bridge.py:107-129`）。
- 请求在 UI 线程 QTimer 槽内同步执行，replay 经 `BlockInvoke`（`socket_server.py:43-46,74-99`；`renderdoc_facade.py:58-60`）。长扫描/大 capture 加载会冻结 UI。
- **多实例当前是共享单槽，不是隔离 mailbox。** 复核的“refuted”针对当前实现成立；本方案要求新增 per-instance mailbox，属于改造项，不是现有事实。

**能力可行性（修订后）：**

| 能力 | 可行性 | 代价/条件 |
|---|---|---|
| 单 capture 内“这个 resource 在哪些 event 被用” | 可行，`GetUsage()` 是加载期预计算的 per-resource 表 | 查询是 map lookup + O(k) 拷贝；D3D11 的 `AddUsage` 记录 draw/dispatch 绑定，**copy/clear/resolve/discard/genmips/CPUWrite 由 wrapper 直接写 `m_ResourceUses`**（`d3d11_context_wrap.cpp:5821-5826,6521-6526,6759-7003`；`d3d11_context1_wrap.cpp:473-478,570`）；完整性按 API/路径不同，但“D3D11 只覆盖 draw/dispatch”是错误结论 |
| 单 capture 内按名字/模糊/OR 搜 marker/resource/event | 可行 | 已加载 capture 的 `ctx.CurRootActions()`/`GetTextures()`/`GetBuffers()` 不需要 replay；shader 名需要逐 event pipeline，需 replay |
| 跨多个 .rdc 搜索 | 可行但不应该占用 GUI 实例 | `OpenFile` 只解码容器/元数据（`capture_access.rst:46`）；枚举 action/resource 需要 `OpenCapture`（replay）或解析 SD；headless 模块默认不发布，且绑定 Python 次版本 |
| 多实例切换 | 技术可行 | 需要 per-instance mailbox + heartbeat + 显式 handle；没有标准 MCP 路由原语 |
| 自由打开/切换 RenderDoc | 技术可行 | 启动 qrenderdoc（位置参数传 capture，`qrenderdoc.cpp:475-486`），等待 heartbeat；涉及进程所有权和数据丢失 |
| 整个 rdc 搜 texture 像素内容 | 不在 v1 | 需要逐 draw 回读/扫描，代价高；v1 搜 usage/绑定/元数据 |

**Headless 是 gating prerequisite，不是普通步骤（复核 O1，已接受并核实）：**

- 官方文档明确：RenderDoc 默认**不发布**可被外部 Python 解释器导入的模块；绑定与 Python major-and-minor 版本绑定（`docs/python_api/python_module.rst:18`）。
- 本地源码构建的 `x64/Release/pymodules/renderdoc.pyd` 链接 `PYTHON36.dll`（`rg -a -o "PYTHON3[0-9]\.dll" ...` 输出）；MCP server 的 `.venv/Scripts/python.exe -V` 是 **3.12.9**（不是复核写的 3.13.9；全局 `python -V` 是 3.13.9，两个解释器都不是 3.6）。
- `RenderDoc_Pro_1.36_64` 安装目录只有 `python36.dll`，`find ... -iname 'renderdoc.pyd'` **没有结果**。要用 headless，必须额外获得/构建匹配 Python 3.6 的 `renderdoc.pyd`，并部署 Python 3.6 运行时/标准库 zip；这不是 `find_spec` 检查能覆盖的。
- 因此：**`scope=all_captures` 在 headless spike 通过前不可交付**；v1 只承诺 current capture + 已在 GUI 打开过的 capture 的浅索引。深索引还额外需要 GPU/WARP 和匹配的 RenderDoc core。

---

## 4. 五维矩阵到模块/工具的映射

### 4.1 模块映射

| 模块 | 状态所有者 | 执行位置 | 作用域 | 副作用 | 载荷 |
|---|---|---|---|---|---|
| ToolFacade / WorkspaceCoordinator | server | 线程池/事件循环 | workspace/instance | 无（路由） | 小 JSON |
| JobManager / IndexStore | server | 后台线程/进程 | job/capture file | 写 job/index 文件 | 结果路径+摘要 |
| SessionState / UiContextService | extension | UI 线程 | capture/instance | 读状态、写 status | 小 JSON |
| UiActionService | extension | UI 线程 | event/capture | 改 UI | 小 JSON |
| ReplayExecutor / QueryServices | extension | replay 线程（分批） | event/capture | 读 replay cursor（scoped） | 结构化数据；大结果转文件 |
| ShaderEditService | extension | UI 线程 + replay | capture generation | 改 replay 资源/UI replacement | 源码/日志/状态 |
| Headless Worker | worker | 独立进程 | capture file/workspace | 写索引/结果 | 文件+摘要 |

### 4.2 工具映射（15 v1 + 1 后置）

| 工具 | 状态所有者 | 执行位置 | 作用域 | 副作用 | 载荷 |
|---|---|---|---|---|---|
| `rd_captures` | server+extension | server + 读 status | instance/workspace | 无 | 小 JSON |
| `rd_capture_open` | extension/server | UI 线程（operation） | instance/capture | destructive（关闭当前 capture） | operation 状态 |
| `rd_overview` | extension | replay（短） | capture/pass | 无 | 统计/计时/计数器，分页 |
| `rd_events` | extension | replay/缓存 | capture | 无 | action 树，分页 |
| `rd_event` | extension | replay（短） | event | 无（scoped cursor） | sections，按需文件 |
| `rd_resources` | extension | 缓存/短 replay | capture | 无 | 资源列表，分页 |
| `rd_resource_data` | extension | replay | event/resource | 写新文件 | 预览/统计/文件 |
| `rd_resource_usage` | extension/worker | replay/独立进程 | capture/workspace | 无 | usage 列表+completeness |
| `rd_shader` | extension | replay | event/resource | 无 | 源码/反汇编，按需文件 |
| `rd_shader_edit` | extension | UI+replay | capture generation | destructive（session） | 状态/日志 |
| `rd_search` | server/worker/extension | 索引/独立进程 | capture/workspace | 无 | 谓词结果+coverage |
| `rd_mesh` | extension | replay | event | 写新文件（export） | summary/page/CSV |
| `rd_ui_context` | extension | UI 线程（读 status） | instance/capture | 无（不创建面板） | 小 JSON |
| `rd_ui_act` | extension | UI 线程 | event/resource/panel | 改 UI | 小 JSON |
| `rd_job` | server | 事件循环/文件 | job | 取消改 job | 状态/结果路径 |
| `rd_index`（post-v1） | worker/server | 独立进程 | workspace | 写索引 | coverage/job |

---

## 5. 与第一版评估的共识与分歧（摘要）

详细逐条见 **附录 A**。摘要：

- **同意**：不要逐面板 1:1；交互层是横切上下文；多实例需要 per-instance；长任务需要 job；30 个工具重叠严重；错误应结构化；`View*` 不能靠 `RaiseDockWindow`（第一版写错）。
- **部分同意/修正**：三层按难度切不适合做工具分类，但四维是检查表不是分层；`GetUsage` 便宜但不是 O(1)，且 D3D11 覆盖范围比第一版/上一版说的更广；`save_texture` 不 base64；导航不是 destructive；FTS5 不原生支持拼写模糊；读工具会遗留 replay cursor。
- **不同意/需要补充**：跨 capture 索引不是“不需要 replay”；headless 不是可选步骤；`ui_context` 不能直接调用惰性 getter；`SetEventID` 不能用于内部恢复；`get_mesh_summary` 不能同时属于 `rd_event` 和 `rd_mesh`。

---

## 6. MCP 规范约束与工具设计原则

> 说明：以下规范结论来自本次任务提供的【MCP 规范】调研材料；本轮**没有重新抓取**规范页。SDK 版本为本机直接核实。无法直接核对的客户端行为标为未验证。

| 主题 | 结论 | 溯源 | 状态 |
|---|---|---|---|
| 协议版本 | 最新规范 2026-07-28 移除协议级 session，要求跨调用状态用显式、不可猜测的 handle；`tools/list` 不得随连接/其它请求副作用变化 | `https://modelcontextprotocol.io/specification/2026-07-28/changelog`；`.../server/tools#stateful-tools` | 来自调研材料，未在客户端实测 |
| 本仓库 SDK | `mcp` 1.25.0 最高 `LATEST_PROTOCOL_VERSION = "2025-11-25"` | `mcp/types.py:27`；`mcp/shared/version.py:3`；`mcp-1.25.0.dist-info/METADATA` | 本机已核 |
| annotations | 默认悲观：`readOnlyHint=false, destructiveHint=true, idempotentHint=false, openWorldHint=true`；annotation 是 hint，不是安全边界 | `https://raw.githubusercontent.com/modelcontextprotocol/specification/main/schema/2026-07-28/schema.ts`；`https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations` | 来自调研材料 |
| outputSchema | 声明后 server 必须返回符合 schema 的 structuredContent；建议同时回填 TextContent；错误是否必须符合 schema 规范未明确 | `https://modelcontextprotocol.io/specification/2026-07-28/server/tools#structured-content` | 来自调研材料；错误行为未验证 |
| progress/cancel | 核心可选机制，稳定但不持久；progress 递增、完成停止；取消是协作式 | `https://modelcontextprotocol.io/specification/2026-07-28/basic/utilities/progress`；`.../cancellation` | 来自调研材料 |
| Tasks | 已从核心移为 `io.modelcontextprotocol/tasks` 扩展，需双方 opt-in；客户端矩阵未列 Tasks | `https://modelcontextprotocol.io/extensions/tasks/overview`；`https://modelcontextprotocol.io/extensions/client-matrix` | 来自调研材料；客户端未实测 |
| token 预算 | Anthropic 建议默认 25k token 上限；分页/范围/过滤/截断；工具定义占上下文 1%-5% 时考虑 progressive discovery | `https://www.anthropic.com/engineering/writing-tools-for-agents`；MCP client best practices | 来自调研材料；未测量 |
| GUI 自动化 | snapshot + 不透明 ref/uid + action；没有标准多实例路由 | Playwright MCP snapshots；Chrome DevTools MCP tool-reference | 来自调研材料 |

**设计原则：**

1. annotations 是 hint，不是安全边界；真正的边界在路径校验、拒绝覆盖、显式实例、进程所有权。
2. 工具列表静态；能力缺失返回 `TOOL_UNAVAILABLE`/`UNSUPPORTED_*`，不动态增删工具。
3. 声明 outputSchema 的工具返回结构化结果；错误用 `isError:true` + 文本 JSON，不承诺错误 structuredContent 符合 schema。
4. 长任务用自建 opaque job/operation handle，不依赖 MCP Tasks；任务生命周期写在工具描述里。
5. 大载荷用文件/图像内容/分页，不默认 inline base64；`resource_link` 支持未知，不作为唯一通道。
6. 每个工具回答一个唯一问题；工具数量不是目标，先测 schema token/first-call 正确率。

**关于 Tasks 的修订（审读意见 5）：** 上一版写“本机 `find_spec('docket') == None`”是**错误**的——本次在 `.venv` 实测 `docket` 存在（`ModuleSpec(...site-packages\docket\__init__.py)`），`fastmcp.server.tasks` 也存在。不用 Tasks 的真实理由是：官方扩展需双方 opt-in、客户端矩阵未列、FastMCP 的 task=True 对 sync function 会报错（`.venv/Lib/site-packages/fastmcp/utilities/tasks.py:78-79`：“Background tasks require async functions”），而本仓库工具是 sync。该错误已从正文删除。

---

## 7. 目标架构

### 7.1 进程与模块（按状态所有者，不按三层）

```
AI Client (stdio)
   │
   ▼
MCP Server (Python 3.10+, FastMCP 3)
   ├─ ToolFacade：15 个 v1 静态工具 + schema/annotations
   ├─ WorkspaceCoordinator：实例发现/路由、capture 代际、默认解析
   ├─ JobManager：operation/job 状态机、持久化、结果落盘
   ├─ IndexStore：SQLite FTS5（浅/深索引、覆盖度）
   └─ WorkerSupervisor：headless worker 启动/限额（可选）
   │  per-instance file IPC
   ▼
RenderDoc Extension (Py3.6, UI 进程)
   ├─ SessionState：capture generation、ui_seq、observed_at
   ├─ UiContextService：Has* 保护 + 250ms 轮询 + 防抖写 status.json
   ├─ UiActionService：SetEventID/Show*/AddDockWindow/ViewTexture/Inspect
   ├─ ReplayExecutor：短 BlockInvoke、分批 AsyncInvoke、scoped SetFrameEvent
   ├─ QueryServices：action/resource/pipeline/mesh/shader 批量提取
   └─ ShaderEditService：generation + edit_id + revision + 冲突检测
   │  可选
   ▼
Headless Worker (独立 Python + renderdoc.pyd)
   ├─ OpenCaptureFile/OpenFile + SD 解析（浅索引，可无 GPU）
   ├─ OpenCapture + 逐 event 扫描（深索引，需 GPU/WARP）
   └─ 跨 capture 搜索/批量 usage
```

- **Server 不做 RenderDoc import**，不持有隐式“当前实例/capture”；`rd_captures` 的目录列举在 server 侧（`os.listdir/stat`）。
- **Extension 只做必须在进程内做的事**；不做跨 capture 编排；长扫描不放在 UI 线程。
- **Headless worker 是可选能力**，缺失时 `rd_index`/`all_captures` 明确返回 `TOOL_UNAVAILABLE`，不静默降级。

### 7.2 线程与执行器

- Extension Python 在 UI 线程（`docs/python_api/in_depth/threading.rst:9`）；`CaptureViewer` 回调也在 UI 线程。
- UI 线程只做短操作（目标 <1s）。短 `BlockInvoke` 可接受；长扫描必须：
  - **分批 AsyncInvoke**：每批 N 个 event（例如 50 或 250ms 预算），回调返回后用 `QTimer.singleShot(0)`/`InvokeOntoUIThread` 调度下一批，让 replay 线程在批次间处理 UI 的 `SetEventID`；不要把整个循环塞进一个 AsyncInvoke（Codex 会诊）。
  - 或 **headless worker**：完全不占 GUI replay。
- 取消：job 的 `cancel_requested` 文件/标志，在批次边界检查；`AsyncInvoke` 的同 tag 去重不是取消机制。
- 关闭 capture：`CloseThread` 会等当前 replay 回调返回再 drain 队列（`ReplayManager.cpp:286-307,509-520`）；批次化后每次回调很短，关闭不会被长循环拖住。`OnCaptureClosed` 取消该 generation 的 job。
- 所有 replay-bound 读必须 **scoped**：记录 `ctx.CurEvent()`、`ctx.CurSelectedEvent()`、`ui_nav_seq`；结束后：
  - 若 `ui_nav_seq` 未变：在 replay 线程 `BlockInvoke(lambda c: c.SetFrameEvent(saved_event, True))`，**不调用 `SetEventID`**，不触发 viewer 回调；
  - 若 `ui_nav_seq` 变了：直接 `SetFrameEvent(ctx.CurEvent(), True)`（最新 UI event）或跳过，让已排队的 UI 导航完成；绝不覆盖用户新选择。
  - 元数据/usage 查询不需要 `SetFrameEvent` 的，完全不碰 cursor。
- MCP server 的 sync 工具在线程池执行，stdout 只给协议；日志走 stderr/文件。

### 7.3 IPC v3：per-instance、每请求文件、原子领取

**复核 O2/O6 指出的单槽竞态必须消除。** 改为：

```
%TEMP%/renderdoc_mcp/
  instances/<instance_id>/
    heartbeat.json
    status.json
    requests/<request_id>.json       # server 原子写入
    processing/<request_id>.json     # extension 原子 rename 领取
    responses/<request_id>.json      # extension 原子写入
    operations/<operation_id>.json   # capture-load 等长操作状态
    jobs/<job_id>.json               # 扩展侧 job 进度（可选）
  jobs/<job_id>/                     # server/headless 结果
  index/                             # SQLite（持久目录，不放 %TEMP% 更稳）
```

- **原子领取**：extension 列出 `requests/`，把 `requests/<id>.json` `os.rename` 到 `processing/<id>.json`（同卷原子）；只有领取者处理。server 不会替换已领取的请求；超时后只把未领取的 `requests/<id>.json` 移到 `expired/` 并写响应。这样不会出现“客户端替换 pending 文件、扩展删掉新请求继续执行旧请求”的竞态。
- **每请求文件**，不是单槽；多个 MCP server 进程可以安全提交，extension 串行处理（replay 是单线程）。
- **响应** `responses/<id>.json`，原子写；server 读取后删除；late response 保留 TTL 诊断。
- **operation**：capture load 这种不适合“请求-响应 30s”的操作，写 `operations/<id>.json`，状态 `accepted/running/succeeded/failed`；`rd_job` 直接读文件/持久 registry，不依赖 extension 再处理请求。
- **心跳** 1s：pid、started_at、capture_path、capture_id、api、ext_version、capabilities、busy、current_request_id、last_event、updated_at。`busy=true` 且心跳旧 → `unresponsive`，不是立即判死；`busy` 超过最大阈值（如 120s）仍需标记 `unresponsive` 并允许显式 `force`，不能让实例永久免疫死亡判定（Codex 会诊）。
- **清理**：extension 启动/停止只清理自己的目录；server 确认心跳过期后清理，保留 24h；绝不删除根目录或其他实例。
- **多 server 客户端**：不再需要全局 `call.lock`；每请求文件 + extension 串行足够。per-instance 可保留一个轻量写锁用于 heartbeat/status 原子写。

### 7.4 多实例与路由

- `instance_id = rd-<pid>-<8hex>`；`capture_id = instance_id + load generation (UUID) + path hash`。capture 关闭/重载后旧 `capture_id` 返回 `STALE_CAPTURE`。
- `rd_captures` 扫描 `instances/`，返回 instance、pid、capture path、capture_id、api、last_event、busy、capabilities、index coverage。
- 解析规则：**显式 `instance_id` > 唯一活实例 > 报错列出候选**；不做“前台窗口/最近活跃”默认。
- `rd_capture_open`：
  - **默认不启动实例**：`launch_if_missing=false`、`new_instance=false`（审读意见 4，统一默认）。
  - **新实例**：`new_instance=true` 或（无活实例且 `launch_if_missing=true`）时，用配置的 qrenderdoc 路径 + capture 位置参数启动（`qrenderdoc.cpp:475-486`），等待 heartbeat 匹配；适合大 capture，不打断用户当前实例。
  - **已有实例**：先 `GetCaptureModifications()`（`QRDInterface.h:2559`）；有未保存修改且 `discard_unsaved=false` → `CAPTURE_MODIFIED`；然后写 operation，调用 `ctx.LoadCapture`（会无条件 `CloseCapture`，`CaptureContext.cpp:921-926`）。UI 会显示 RenderDoc 的模态进度对话框（`CaptureContext.cpp:954-976`）；返回 `operation_id`，不占 30s 请求-响应。
  - `idempotency_key` 映射到 operation；重复调用返回同一 `operation_id`，不重复加载；`rd_job` 可取回最终结果（复核 O2）。
  - 只管理自己启动的子进程；不杀用户启动的实例。
- `rd_ui_act(focus)` 用 `BringToFront()`，返回实际 `focused`（官方不保证成功）。
- 工具列表静态；能力缺失返回 `TOOL_UNAVAILABLE`/`UNSUPPORTED_*`，不动态增删工具。

### 7.5 长任务/操作

- **普通读工具默认同步**，不再给所有工具 `wait_ms`（复核 O9）：`rd_events`/`rd_overview`/`rd_event`/`rd_resources`/`rd_shader` 走现有 30s 级别，超时返回可操作错误/建议缩小范围，不强制 job。
- **长能力工具**才使用 operation/job：
  - `rd_capture_open`（加载/启动）；
  - `rd_search(scope=all_captures)`（索引/扫描）；
  - `rd_resource_usage` 的全帧深扫描（如果超出预算）；
  - `rd_index`（建索引，post-v1）；
  - `rd_shader_edit(apply)` 的编译（如果无法在 UI 线程外做）。
- 状态机：`accepted/queued/running/cancel_requested/cancelled/succeeded/failed/interrupted/invalidated`。
- **持久化**：SQLite `jobs` 表（或 JSONL）+ 结果文件；server 重启后加载终态 job，running 标 `interrupted`；`rd_job(list)` 可恢复；`rd_job(result)` 按 `result_path` 读取；`JOB_NOT_FOUND` 只用于真的没有记录/结果（复核 missing）。
- 取消协作式，不回滚；capture 关闭/重载使 job `invalidated`。
- 不使用 MCP Tasks 作为主路径；未来可把 `job_id` 映射到 Tasks 扩展。

### 7.6 UI 快照与刷新矩阵

**快照：**

- `rd_ui_context` 只读 `status.json`，不直接调用惰性 getter；extension 侧：
  - `Has*()` 为假 → 字段 `null`，列入 `fields_unknown`；
  - `Has*()` 为真 → 读 `GetCurrentResource/GetSelectedSubresource/GetTextureDisplay/GetZoomLevel/GetTextureOverlay/GetPickedLocation/GetHistogramRange/GetChannelVisibility/GetCurrentFilterText/CurrentResource`；
  - 250ms 轮询 fingerprint；变化才递增 `ui_seq`、写 `status.json`（防抖 150–250ms）；
  - `observed_at`、`sources`（callback/poll）、`ui_seq` 一起返回；`ui_seq` 只覆盖已观测字段。
- `constructed_panels` 来自 `Has*()`；`visible` 为 `null/unknown`，除非 PySide2 `Widget().isVisible()` 可用（未实测）。`focused_panel` 默认 `unknown`，不发明全局“当前面板”。

**刷新矩阵（明确“同步前端 UI”到底做什么）：**

| 操作 | 刷新哪些面板 | 机制 | 注意 |
|---|---|---|---|
| `rd_capture_open`（新实例） | 新进程默认布局 | qrenderdoc 启动时加载 capture | 不影响旧实例 |
| `rd_capture_open`（已有实例） | 所有已构造 viewer | `LoadCapture` → `OnCaptureLoaded`（`CaptureContext.cpp:995-1028`） | UI 模态进度；会关闭当前 capture；不主动创建未构造面板 |
| `rd_ui_act(navigate)` | EventBrowser（若存在）、pipeline/texture/mesh viewer（若存在） | `SetEventID(force=True)` → `RefreshUIStatus` | EventBrowser 不存在则不滚动；返回 `scrolled`/`panel_existed` |
| `rd_ui_act(show_panel)` | 指定面板 | `Show*` 或 `AddDockWindow` | `View*` 必须 `AddDockWindow`，不是 `RaiseDockWindow` |
| `rd_shader_edit(apply/revert)` | replacement 相关 viewer | `RegisterReplacement`/`UnregisterReplacement`；可选 `RefreshStatus()` | 可能滚动 EventBrowser；`refresh_ui` 默认 true，读工具不刷新 |
| 读工具（events/event/resources/shader/usage） | 不刷新 | 内部 `SetFrameEvent` 恢复，不调 `SetEventID` | 不改变用户 UI；不创建面板 |
| `rd_resource_data`/`rd_mesh` | 不刷新 | 只读 replay/resource 数据 | 写文件不触发 UI |

### 7.7 搜索与索引（修订）

- **浅索引**：capture 加载时从 `ctx.CurRootActions()`/`GetTextures()`/`GetBuffers()` 取 action/marker/资源名（无 replay），由 extension 推给 server；只覆盖已在 GUI 打开的 capture。
- **深索引**：headless `OpenCapture` 逐 event 取 shader/pipeline/usage；需要可导入的 `renderdoc.pyd` + 匹配 Python 3.6 + GPU/WARP。也可用 `OpenFile` + `GetStructuredData` 做无 GPU 的浅层解析，但同样需要模块。
- **Bootstrap（复核 O3）**：加 `rd_index` 工具/operation（post-v1）：
  - `mode=shallow`：对目录/文件列表建立浅索引（优先用现有 GUI 推送；headless SD 可用时走 SD）；
  - `mode=deep`：headless replay；
  - 返回 `coverage: {requested, indexed, skipped, deep, errors}`；
  - `rd_search(scope=all_captures)` 只返回已索引 capture，并在响应里带 `coverage`；未索引文件不静默跳过，列在 `skipped`；
  - 没有 headless 时，`deep` 返回 `TOOL_UNAVAILABLE`；`shallow` 只能覆盖 GUI 打开过的 capture，或明确提示需要逐个打开。
- **查询模型（Codex 会诊）**：不用 `terms+fields` 的扁平结构，改成有类型的谓词树，支持 AND/OR 和 `same_event`：
  ```json
  {
    "op": "and",
    "same_event": true,
    "predicates": [
      {"field": "marker_path", "match": "contains", "value": "Bloom"},
      {"field": "resource_name", "match": "fuzzy", "value": "Normal"},
      {"field": "shader_name", "match": "contains", "value": "Toon"},
      {"field": "shader_stage", "match": "eq", "value": "pixel"}
    ]
  }
  ```
  `same_event=true` 表示所有谓词必须落在同一个 event/action 上；`false` 返回独立匹配并带 provenance。字段枚举：`marker_path/event_name/action_name/resource_name/resource_id/shader_name/shader_entry/shader_stage/usage_kind/event_id/api`。`match`: `eq/contains/prefix/fuzzy`（不开放任意 regex）。
- **FTS5 的真实能力**：本机 SQLite 3.50.2 实测 `bloom*`、`bloom OR tonemap`、trigram `Downs` 可用；`Blom` 不匹配 `Bloom`。FTS5 只做前缀/子串/布尔预筛；typo 容忍用规范化 + Levenshtein 重排或 spellfix1。
- **返回实体**：`{kind: event|resource|shader|capture, capture_ref, event_id?, resource_id?, score, evidence:[{field,value}]}`；跨 capture 结果按 `capture_file_id` 分组，不把不同 capture 的同号 ResourceId 当同一资源。

### 7.8 句柄、数据时间点与身份

- `instance_id`：进程级，`rd-<pid>-<8hex>`。
- `capture_file_id`：文件级，绝对路径 + size + mtime（+ 可选 hash）；用于索引/跨 capture 结果。
- `capture_id`：加载代际级，`instance_id + UUID + path hash`；同一路径重开必变；旧 event/resource 引用返回 `STALE_CAPTURE`。
- `resource_ref`：`{capture_id, resource_id}`；**不能**跨 capture 复用裸 ResourceId（ResourceId 只是 uint64，`resourceid.h`；不同 capture 可能同号）。
- `event_ref`：`{capture_id, event_id}`；event_id 只在同一 capture 代际内有意义。
- `edit_id`：shader 编辑记录，绑定 `capture_id`，跨代际失效。
- `job_id`/`operation_id`：server 生成的不透明 UUID；绑定 `instance_id`/`capture_id`（或 `capture_file_id` + `index_version`）；TTL/生命周期写在工具描述里。
- `ui_seq`：扩展观测到的 UI 变化序号；只覆盖已观测字段；响应带 `observed_at`。
- **数据时间点（Codex 会诊）**：`rd_resource_data` 必须接受 `event_id?`（默认当前 event），因为 texture/buffer 内容随 event 变化；返回 `event_id`、`source`（`gui_session`/`capture_file`）、`session_modifications`（是否有 shader replacement/session 修改）。headless 结果读原始文件，不能冒充 GUI 当前会话结果。
- **数据来源**：GUI 结果 `source=gui_session`；索引/headless 结果 `source=capture_file` + `index_version`；两者在响应里区分。

### 7.9 错误、载荷、注解

- 错误：`isError:true`，文本 JSON `{ok:false,error:{code,message,hint,retryable,outcome_unknown,candidates}}`；不承诺错误 structuredContent 符合 outputSchema。
- 错误码：`INSTANCE_NOT_FOUND`、`INSTANCE_AMBIGUOUS`、`CAPTURE_NOT_LOADED`、`CAPTURE_CHANGED`、`CAPTURE_MODIFIED`、`UNSUPPORTED_REMOTE_REPLAY`、`EVENT_NOT_FOUND`、`RESOURCE_NOT_FOUND`、`UNSUPPORTED_CAPTURE_FEATURE`、`INVALID_ARGUMENT`、`BUSY`、`TIMEOUT_OUTCOME_UNKNOWN`、`JOB_NOT_FOUND`、`JOB_CANCELLED`、`TOOL_UNAVAILABLE`、`FILE_EXISTS`。
- 载荷：
  - Texture：默认元数据 + 统计 + 小 PNG 预览（image content，<=512×512）或文件路径；`mode=file` 写 PNG/EXR/DDS；`mode=inline` 只在显式请求且 <=64KB 时给 base64，供不能读文件的客户端；默认不 inline。
  - Buffer：默认长度/hash/前 256B hex；`mode=file` 写 `.bin`；`mode=inline` 显式且限制大小。
  - Shader：<50KB 文本；否则文件 + 预览。
  - Action 树：默认根层 + 子节点计数，`cursor/limit` 展开，单次上限后 `next_cursor`。
  - Mesh：单页 <=500 顶点；`total_count` 必须是顶点数，不是索引数（修 `mesh_service.py:337-338,430-441` 的 bug）。
- 注解：15 个 v1 工具全部显式四注解；本地 closed-world，`openWorldHint=false`；navigation `readOnly=false, destructive=false, idempotent=true`；导出 `readOnly=false, destructive=false, idempotent=false`；shader edit/capture open `destructive=true`。

---

## 8. 工具面草案

### 8.1 锁定定义：v1 注册 15 个工具；`rd_index` 是 post-v1

**v1（15 个，全部注册）：**

| # | name | 回答什么问题 | sideEffect | annotations |
|---|---|---|---|---|
| 1 | `rd_captures` | 有哪些实例/各自加载哪个 capture/目录里有哪些 .rdc/索引覆盖如何？该用哪个 handle？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 2 | `rd_capture_open` | 把 capture 打开/切换到某实例（或显式启动新实例）后，operation/capture_id 是什么？ | destructive/cross-capture | `readOnly=false; destructive=true; idempotent=false; openWorld=false` |
| 3 | `rd_overview` | 这一帧/pass 的统计、时间、统计/计数器、先看哪些 event？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 4 | `rd_events` | 某 marker/区间/标志下有哪些 action，层级/分页是什么？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 5 | `rd_event` | 这个 event 的详情/管线/依赖/时间是什么；和另一个 event 比哪里变了？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 6 | `rd_resources` | 当前 capture 有哪些 texture/buffer，按名称/格式过滤后是什么？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 7 | `rd_resource_data` | 这个资源在指定 event 的内容/统计是什么，如何导出/预览？ | file-write（不改 capture） | `readOnly=false; destructive=false; idempotent=false; openWorld=false` |
| 8 | `rd_resource_usage` | 这个资源在整帧/整个 capture 的哪些 event 被读/写/消费，完整性如何？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 9 | `rd_shader` | 这个 event/资源绑定的 shader 源码/反汇编/反射/常量/绑定是什么？ | read-only | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 10 | `rd_shader_edit` | 如何准备/应用/还原/列出/导出当前会话的 shader 替换？ | destructive（session replay state only） | `readOnly=false; destructive=true; idempotent=false; openWorld=false` |
| 11 | `rd_search` | 这帧/已索引 capture 里哪些 event/resource/shader 匹配谓词树？ | read-only（可能 operation） | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 12 | `rd_mesh` | 这个 draw 的网格 summary/分页/导出是什么？ | file-write for export；其余 read-only | `readOnly=false; destructive=false; idempotent=false; openWorld=false` |
| 13 | `rd_ui_context` | 用户当前已提交的 event/资源/面板/过滤状态是什么？ | read-only（UI 状态） | `readOnly=true; destructive=false; idempotent=true; openWorld=false` |
| 14 | `rd_ui_act` | 把用户 UI 导航/显示到正在讨论的 event/资源/面板。 | ui-state | `readOnly=false; destructive=false; idempotent=true; openWorld=false` |
| 15 | `rd_job` | 长操作/任务现在什么状态、结果在哪、能否取消？ | job-control | `readOnly=false; destructive=false; idempotent=true; openWorld=false` |

**Post-v1（第 16 个，step 7 前不注册）：`rd_index`**  
回答“哪些 capture 已索引/覆盖到什么程度，如何为目录建/刷新浅/深索引？”；sideEffect 写索引；annotations `readOnly=false; destructive=false; idempotent=true; openWorld=false`。v1 的 `rd_search(scope=all_captures)` 在 `rd_index` 不存在时返回 `TOOL_UNAVAILABLE` 或仅 `indexed_captures`，不静默宣称覆盖全部。

**参数要点（修订）：**

- 公共：`instance_id?`、`capture_id?`；**不再有公共 `wait_ms`**（复核 O9）。
- `rd_capture_open`：`capture_path`、`instance_id?`、`launch_if_missing?=false`、`new_instance?=false`、`discard_unsaved?=false`、`idempotency_key?`；返回 `operation_id`、`state`。
- `rd_overview`：`marker?`、`include_timings?`、`sections?`（stats/statistics/counters/suggestions）。
- `rd_event`：`event_id`、`sections?`（summary/pipeline/resources/shader/timing/dependencies）、`compare_to?`；**不含 mesh**。
- `rd_resource_data`：`resource_id`、`event_id?`（默认当前 event）、`subresource?`、`mode?`（auto/preview/stats/file/inline）、`output_path?`、`max_dimension?`。
- `rd_resource_usage`：`resource_id` 或 `name_query?`、`usage_kinds?`、`marker?`、`event_range?`、`group_by?`；返回 `usage_status/completeness`；删除 `include_unbound`。
- `rd_search`：`query`（谓词树，§7.7）、`scope?`（current_capture/indexed_captures/all_captures）、`limit?`、`cursor?`。
- `rd_mesh`：`event_id`、`stage?`、`mode?`（summary/page/export）、`offset?`、`limit?`、`attributes?`、`output_path?`。
- `rd_ui_context`：`include?`（events/texture/resource_inspector/filters）；不提供 `panels` 可见性承诺。
- `rd_ui_act`：`action`（navigate/show_panel/select_resource/set_texture_view/set_event_filter/focus）、`ensure_panels?`、`event_id?`、`selected_event_id?`、`panel?`、`resource_id?`、`subresource?`、`overlay?`、`zoom?`、`filter_text?`。
- `rd_job`：`action`（status/result/cancel/list）、`job_id?`、`instance_id?`。
- `rd_index`（post-v1）：`directory?`、`captures?`、`mode?`（shallow/deep）、`refresh?`。

### 8.2 合并映射（30 → 15 v1 + post-v1）

| 新工具 | 合并旧工具 | 说明 |
|---|---|---|
| `rd_captures` | `get_capture_status` + `list_captures` | 实例/捕获/目录/索引覆盖；返回 capture_id |
| `rd_capture_open` | `open_capture` | operation 模型、显式新实例、未保存检查、幂等键 |
| `rd_overview` | `get_frame_summary` + `summarize_capture` + `analyze_pass` + `get_action_timings`（汇总） | 统计/计数器数据重建 |
| `rd_events` | `get_draw_calls` | 统一 marker/range/flags；分页 |
| `rd_event` | `inspect_event` + `get_draw_call_details` + `get_pipeline_state` + `trace_event_dependencies` + `diff_events` + `get_action_timings`（单事件） | **不含 mesh**；`compare_to` 取代 diff |
| `rd_resources` | `list_resources` + `get_texture_info` | 统一 texture/buffer |
| `rd_resource_data` | `get_texture_data` + `get_buffer_contents` + `save_texture` | event 绑定、文件/预览/统计、inline 仅显式 |
| `rd_resource_usage` | `trace_resource_usage` + `search_draws(by=resource/texture)` | usage_status/completeness；sentinel 处理 |
| `rd_shader` | `get_shader_info` + `get_shader_source` | parts |
| `rd_shader_edit` | `get_shader_edit_context` + `replace_shader` + `revert_shader` + `list_shader_replacements` + `export_shader_source` | action 枚举；revision |
| `rd_search` | `search_draws`（全部）+ 跨 capture | 谓词树；coverage |
| `rd_mesh` | `get_mesh_summary` + `get_mesh_data` + `export_mesh_csv` | **mesh 唯一入口** |
| `rd_ui_context` | 新 | Has* 保护 + 轮询 |
| `rd_ui_act` | 新 | navigate/show/select/view/filter/focus |
| `rd_job` | 新；替代 `RESULT_PENDING` 无入口 | 持久化 operation/job |
| `rd_index`（post-v1） | 新 | 浅/深索引 bootstrap |

### 8.3 牺牲与测量门

**牺牲：**

1. 逐面板 1:1 没有；Pixel History/API Inspector/Statistics/PerformanceCounter 的 **UI 状态**不承诺；数据可重建的统计/计数器由 `rd_overview` 提供。
2. `get_draw_call_details/inspect_event/diff_events` 独立入口没有；变成 `rd_event` 的 sections/compare_to，schema 变大。
3. `analyze_pass` 变成 `rd_overview(marker=...)`，可发现性下降。
4. `rd_shader_edit(prepare)` 被归入 destructive 工具；客户端可能对 prepare 也弹确认（过度警告）。
5. `rd_resource_data` 默认不 inline base64；脚本化客户端要读文件；旧 `get_texture_data` 的 `content_base64` 只在 legacy 模式保留。
6. 旧工具名/别名默认消失；legacy 模式见 §8.4。
7. `rd_index` 后置；没有 headless 时 all_captures 不可用，不是“部分可用”。
8. mesh 摘要不再出现在 `rd_event`，只走 `rd_mesh`；agent 需要知道这个唯一入口。

**测量门（回应复核“15 工具更省 token 未验证”）：**

- 不把 15 当事实；先测量：
  - `tools/list` 的 JSON token 数（新 vs 旧 vs 拆分方案）；
  - 典型任务的 first-call 正确率（选对工具/选对 sections）；
  - 完成同一任务的总 token/调用次数；
  - `rd_event`/`rd_resource_data` 的 schema 大小是否超过预算。
- 若 `rd_event`/`rd_resource_data` 的联合 schema 明显更贵或更易误用，就拆成更小的工具（例如 `rd_event_pipeline`、`rd_resource_export`），不为了“15”牺牲可用性。工具数量是结果，不是目标。

### 8.4 兼容层（回应复核 missing）

- 默认：只注册 **15 个 v1 新工具**（`rd_index` 后置，不计）。
- `RENDERDOC_MCP_LEGACY_TOOLS=1`：额外注册 30 个 legacy adapter，`tools/list` = **45**（若未来注册 `rd_index` 则为 46）；adapter 保留旧响应形状（`content_base64`、`event_id_min/max`、`start_offset/max_vertices`、旧错误文本），内部调用新服务。默认关闭；保留两个 minor 版本；文档写弃用窗口。
- 如果客户端无法处理 45 个工具，就只能用默认新工具面；legacy 模式是显式 opt-in，不是隐式 fallback。
- 不在多实例时自动 fallback 到共享 mailbox；旧共享 mailbox 只允许单实例模式，且启动时打印警告。

---

## 9. 落地路线图（修订）

| step | 做什么 | why | risk |
|---|---|---|---|
| 1 | **Spike A：headless 可用性**（时间盒） | 需要确认能否获得/构建匹配 Python 3.6 的 `renderdoc.pyd`、Python 3.6 运行时、匹配的 RenderDoc core，以及 GPU/WARP。这是 `all_captures`/深索引的 gating prerequisite；失败则明确砍掉。 | 本机源码 pyd 链 `PYTHON36.dll`；安装目录没有 `renderdoc.pyd`；MCP venv 是 3.12.9。可能无法交付 headless。 |
| 2 | **Spike B：per-instance IPC + 双实例**（时间盒） | 验证每请求文件、原子 rename 领取、heartbeat、busy/unresponsive、停止一个实例不影响另一个；这是多实例的地基。 | 双实例竞态、心跳误判、Windows 文件锁/rename 语义；未实测。 |
| 3 | **单实例 v1：工具契约 + 15 工具 + annotations/outputSchema + 结构化错误 + 载荷策略** | 不依赖 headless/多实例；直接减少工具选择困难、base64 浪费和错误不可操作；先测 schema token/正确率再锁数量。 | breaking change；客户端 outputSchema/annotations 支持未知；legacy 兼容；schema 膨胀。 |
| 4 | **UI context/act + capture operation** | 最高用户价值：让“这个 drawcall/这张 texture”有指代；`rd_capture_open` 改 operation，避免 30s 超时；修正 View*/AddDockWindow、Has* 惰性构造、SetEventID 恢复问题。 | UI 线程/模态加载；面板未构造；可见性未知；EventBrowser 不滚动；PySide2 依赖；需实机 UI 测试。 |
| 5 | **通用 job/operation 持久化 + `rd_job`** | capture 加载之外的深扫描/导出需要可追踪、可取消、可恢复；server 重启后能取回结果。 | 状态机/取消/部分结果；持久化一致性；extension 批次调度。 |
| 6 | **多实例 v2（若 Spike B 通过）** | per-instance mailbox、显式 instance_id/capture_id、启动/切换/focus、未保存检查。 | 多实例路由/进程所有权；用户数据丢失；焦点不可靠。 |
| 7 | **`rd_index` + 浅索引（若 Spike A 的 SD 路径可用）** | 给 `all_captures` 一个 bootstrap；先覆盖 marker/resource/event 名，不承诺深 shader/usage。 | 仍需 renderdoc 模块；索引失效/覆盖度；不能静默漏 capture。 |
| 8 | **深索引 + `rd_search(all_captures)`（若 GPU/headless 通过）** | 真正的超广度搜索；与 GUI 隔离。 | GPU/VRAM/加载时间；与 GUI 同时 replay；索引版本/身份。 |
| 9 | **legacy 清理 + 文档/观测** | 降低维护成本；在兼容窗口后移除旧工具/共享 mailbox。 | 旧客户端断裂；文档/测试滞后。 |

**关键顺序判断：** 复核建议“先单实例 30→15 + UI，headless/IPC 作为独立 spike”是正确的。上一版把 headless/IPC 当普通排期步骤，低估了部署/竞态风险；本版把它们前置为 spike，并且不阻塞单实例 v1。

---

## 10. 明确不建议做的事

1. 不做逐面板 1:1 工具；不承诺面板 UI 复刻。
2. 不在 headless spike 通过前承诺 `all_captures`；不做“索引里有什么就说什么”的伪全覆盖。
3. 不用 MCP Tasks 作为主路径；不依赖 `resource_link`；不把 base64 作为默认载荷。
4. 不在 UI 线程跑长循环；不用 `SetEventID` 做内部 cursor 恢复；不用同 tag AsyncInvoke 当取消机制。
5. 不在多实例时自动回退到共享 `request.json`；不在启动/停止时删除根目录或其他实例文件。
6. 不在默认配置里启动 qrenderdoc 实例；只杀自己启动的进程。
7. 不在 v1 支持远程/Android replay；不把远程 capture 伪装成本地 path。
8. 不保留 30 个 legacy 工具为默认；legacy 必须显式 opt-in，并保留旧响应形状。
9. 不声称“15 个工具一定比 30 个省 token”；先测量。
10. 不把不同 capture 的同号 ResourceId 当同一资源；不跨 capture 复用裸 event_id/resource_id。

---

## 11. 对复核意见的回应（摘要）

> 详细逐条见 **附录 B**（反方评审/事实核查）和 **附录 C**（Codex 会诊）。这里只给处理结论，避免正文重复。

| 编号 | 意见 | 处理 |
|---|---|---|
| O1 | Headless 需要 Python 3.6 + 匹配 core，不是可选步骤 | 接受；升级为 gating prerequisite；v1 不承诺 all_captures；Spike A 先验证。 |
| O2 | `LoadCapture` 在 UI 线程模态加载，30s 超时；job 不覆盖加载 | 接受；改为 operation 模型；新实例优先；`rd_job` 轮询；`capture-load` 执行器。 |
| O3 | all_captures 没有 bootstrap 索引路径 | 接受；加 `rd_index`（post-v1）+ coverage；无 headless 时明确不可用。 |
| O4 | Statistics/PerformanceCounter 数据可重建，上一版过度排除 | 接受；`rd_overview` 增加 statistics/counters；只排除 viewer UI 状态。 |
| O5 | `Get*` 惰性构造会创建隐藏面板；ui_seq 覆盖不全 | 接受；`Has*` 保护；`constructed_panels` + `visible=unknown`；250ms 轮询。 |
| O6 | 用 `SetEventID` 恢复会触发 UI 回调/滚动 | 接受；内部恢复改 `BlockInvoke(SetFrameEvent(...))`；加 `ui_nav_seq`。 |
| O7 | `get_mesh_summary` 同时映射到 rd_event 和 rd_mesh | 接受；`rd_event` 删除 mesh；`rd_mesh` 唯一入口。 |
| O8 | 15 工具 schema 更大，token/选择优势未测量 | 接受；15 是候选；加测量门；必要时拆分。 |
| O9 | 给所有工具 `wait_ms` 会强制 job 轮询 | 接受；删除公共 `wait_ms`；只长能力工具用 operation/job。 |
| O10 | `GetUsage` sentinel/`include_unbound` 不存在 | 接受；`usage_status/completeness`；删除 `include_unbound`；不丢弃 sentinel。 |
| M1 | 远程/Android 未覆盖 | 接受；v1 明确 `UNSUPPORTED_REMOTE_REPLAY`。 |
| M2 | 导出文件客户端可能读不到 | 接受；`auto` 小图 image content/统计，大图文件；`inline` 显式且限大小；legacy base64。 |
| M3 | 30→15 兼容层未定义 | 接受；`RENDERDOC_MCP_LEGACY_TOOLS=1`，保留旧响应形状；默认关闭。 |
| M4 | job 持久化/恢复未闭环 | 接受；SQLite jobs + 结果文件；重启恢复终态；`rd_job(list/result)`。 |
| M5 | 基础层“同步 UI 刷新”未定义 | 接受；刷新矩阵（§7.6）；不创建未构造面板。 |
| M6 | GetUsage 完整性未进输出契约 | 接受；`usage_status/completeness`；修正 D3D11 覆盖范围。 |

**Fact-check 中我们拒绝/修正的两点：**

1. **“D3D11 GetUsage 只覆盖 draw/dispatch”错误**：事实核查只看了 `d3d11_context.cpp` 的 `AddUsage`，漏了 wrapper 直接写 `m_ResourceUses`。证据：`d3d11_context_wrap.cpp:5821-5826,6521-6526,6759-7003`；`d3d11_context1_wrap.cpp:473-478,570`。正确说法是“查询便宜、完整性按 API/路径不同，输出要报告覆盖类别”。
2. **“多实例 claim refuted”要区分现状与提案**：当前实现共享单槽，复核对现状的 refuted 成立；本文的 claim 是“提案要求 per-instance”，不是“现状已有”。已改写为“当前不支持，需新增并实测”。

**审读意见的处理：**

- **原始三层构想未复述**：已在 §1.1 补表，明确用户原话 vs 本文重定义；§1.2 补术语。
- **正文以回应复核组织/五维未落地**：§2.2 给五维矩阵，§4 给模块/工具映射；详细 P/O 表移到附录 A/B/C；正文只留摘要。
- **15/16 摇摆**：锁定为 **v1 15 个，`rd_index` post-v1 不注册**；§8/§9/§11 全部统一；legacy 数量单列（45/46）。
- **`rd_capture_open` 默认行为矛盾**：统一为 `launch_if_missing=false`、`new_instance=false`，不默认启动；§0 改为“推荐对大 capture 显式启动新实例”。
- **docket 断言错误**：已删除“`find_spec('docket') == None`”；本次实测 `.venv` 有 `docket`，不用 Tasks 的理由改为“扩展 opt-in/客户端矩阵未列/FastMCP sync 函数不能 task=True”（`fastmcp/utilities/tasks.py:78-79`）。
- **规范判断无可追溯页**：§6 增加 URL/章节/版本表，并注明“来自调研材料，未重新抓取”；SDK 2025-11-25 为本机直接核实。
- **版本基线写成 v1.x**：已改为 `feature/renderdic_customhook`、`v1.45-354-g5f3763615`，说明 UI 文件有 fork 改动；删除未证实的“master 两个回调”说法，要求固定官方 release tag 重核。
- **用 grep 推出设计意图**：已改为直接 `mcp.list_tools()` 证据：30 个工具、annotations=None、output_schema 是通用 object；结论改为“没有字段级 outputSchema/annotations”，不再说“没按这些维度设计”。

---

## 12. 局限与未验证事项

1. 没有在真实 RenderDoc/GPU 上跑：SetEventID 滚动、View*/AddDockWindow 可见性、AddCaptureViewer 顺序、LoadCapture 耗时/模态、UI 轮询、双实例、headless 导入、shader 编译、`FetchCounters` 可用性。
2. 没有构建/导入 headless `renderdoc.pyd`；只静态确认它链 `PYTHON36.dll`、安装目录没有该模块、MCP venv 不是 3.6。
3. 没有测 `tools/list` token、first-call 正确率、任务总 token；15 工具面是候选，不是已验证的最优。
4. 没有测 MCP 客户端（Codex/Claude Code）对 outputSchema/annotations/resource_link/Tasks 的支持；SDK 版本事实已核，协商版本未抓包。
5. 没有测远程/Android replay；v1 明确不支持。
6. 没有测 job 持久化/恢复、取消/部分结果、server 重启；设计上已闭环，但未实现/未实测。
7. 没有测 per-instance IPC 的 Windows rename/锁语义、busy/unresponsive 阈值、心跳误判。
8. 没有固定目标 RenderDoc 版本；本 checkout 是 fork 分支 `v1.45-354`，UI 文件有改动；v1.x/1.36/1.46 的行为矩阵需重核。
9. 没有验证 `Widget().isVisible()`/PySide2 在 bundled 环境下的可用性；`focused_panel` 仍为 unknown。
10. 没有验证 `GetUsage` 在 D3D12/Vulkan/GL 的精确覆盖；输出契约要求报告 completeness，但不声称逐 API 已实测。

---

## 13. 结论

- **现在做单实例 v1**：15 个工具的契约、annotations/outputSchema、结构化错误、文件化载荷、capture 代际、UI 快照/导航、capture operation。它不依赖 headless 和多实例，能直接改善用户最常用的“看帧/看 event/看资源/跳过去”。
- **headless 与多实例先做 spike**：headless 是 Python 3.6 + 匹配 core 的部署问题，不是 `find_spec` 一行；per-instance IPC 是当前共享单槽的改造，不是现状。两者通过前，不承诺 `all_captures` 和多实例切换。
- **读工具不改变 UI**：Has* 保护、直连 SetFrameEvent 恢复、导航代际、分批 AsyncInvoke；`SetEventID` 只用于用户可见导航。
- **不要把工具数量当目标**：15 是候选，先测 schema token 和正确率；必要时拆分。

---

## 附录 A：与第一版评估逐条分歧（P1-P15）

| # | 第一版论断 | 立场 | 依据 |
|---|---|---|---|
| P1 | 三层按难度切是错的，应按状态/副作用/作用域/载荷四维切 | **部分同意** | 同意按难度切不适合工具分类；四维是设计检查表，不是分层方案。实际切法是状态所有者+执行位置+作用域+副作用+载荷。直接 `mcp.list_tools()`：30 个工具、annotations=None、output_schema 为通用 object；这是“没有字段级契约”，不是“没按这些维度设计”的意图证明。 |
| P2 | “完全复刻面板”是陷阱，应做信息模型 | **部分同意** | 方向正确；但上一版低估了数据可重建范围：Statistics/PerformanceCounter 数据可由 `CurRootActions/GetTextures/GetBuffers/FrameInfo` 和 `FetchCounters` 重建（`StatisticsViewer.cpp:678-684`；`PerformanceCounterViewer.cpp:344`；`renderdoc_replay.h:803`）；读不到的是 viewer UI 状态。 |
| P3 | `ViewShader/ViewBuffer/...` 必须自己调 `RaiseDockWindow()` | **不同意（事实错误）** | 这些窗口没有 show/dock（`CaptureContext.cpp:2746-2812`）；`RaiseDockWindow` 对非 `ToolWindowManagerArea` 只 warning（`ToolWindowManager.cpp:549-569`）；必须 `AddDockWindow` 或 `Widget().show()`。 |
| P4 | `AddCaptureViewer` 在已有 capture 时同步触发 `OnCaptureLoaded` + `OnEventChanged` | **部分同意** | 还触发 `OnSelectedEventChanged`（`CaptureContext.h:135-145`）；`OnCaptureClosed` 在本 checkout 里于 `m_CaptureLoaded=false`/`CloseThread` 之前（`CaptureContext.cpp:1515-1526,1570-1574`）。其它版本未核对。 |
| P5 | 拖 timeline 会连续触发 `OnEventChanged`，必须防抖 | **部分同意** | TimelineBar 每次 mouseMove 调 `SetEventID`（`TimelineBar.cpp:385-420`），但 SetEventID 同步等 replay，tagged AsyncInvoke 会合并同 tag 待处理项（`ReplayManager.cpp:255-283`）；实际回调率被 replay 延迟限制。防抖仍要做，理由是写盘/快照成本；Hz 未实测。 |
| P6 | `GetUsage()` 是 O(1)，返回每个事件的访问方式，单 capture 搜索完全可行 | **部分同意，且上一版有一条错误** | 预计算、查询便宜（`resource_usage.rst:3-5,13,36`；`replay_controller.cpp:528-535`），但不是 O(1)，是 map lookup + O(k) 拷贝。**D3D11 并非只覆盖 draw/dispatch**：copy/clear/resolve/discard/genmips/CPUWrite 在 wrapper 里直接写 `m_ResourceUses`（`d3d11_context_wrap.cpp:5821-5826,6521-6526,6759-7003`；`d3d11_context1_wrap.cpp:473-478,570`）。完整性仍按 API/路径不同，输出必须带 `usage_status/completeness`。 |
| P7 | 跨 capture 索引优先，首次打开时索引 action/资源名，不需要 replay | **不同意** | `OpenFile` 只解码容器/元数据（`capture_access.rst:46`）；action/资源名来自已加载 ctx（`QRDInterface.h:2655,2670,2760`），对从未打开的 capture 需要 `OpenCapture` 或解析 SD；headless 模块默认不发布。 |
| P8 | `get_texture_data` 和 `save_texture` 内部都 base64 | **不同意** | `save_texture` 调用 `SaveTexture(..., output_path)` 写文件（`resource_service.py:204-213`），无 base64；base64 只在 `get_buffer_contents`（:256）和 `get_texture_data`（:399）。 |
| P9 | `ui_act` 导航是 destructive | **不同意** | `readOnlyHint=false` 对；但导航可逆，应 `destructiveHint=false, idempotentHint=true`。destructive 留给 `capture_open`、shader 替换。 |
| P10 | MCP 2025-11-25 有 experimental Tasks，自建 job 更稳 | **部分同意** | 结论成立；2026-07-28 已把 Tasks 移为扩展，客户端矩阵未列；本仓库 mcp 1.25.0 最高 2025-11-25（`mcp/types.py:27`）；FastMCP task=True 对 sync function 报错（`.venv/Lib/site-packages/fastmcp/utilities/tasks.py:78-79`），本仓库工具是 sync。 |
| P11 | 所有工具接受 `instance_id`；默认“显式 > 前台窗口 > 最近活跃 > 唯一 > 报错” | **部分同意** | instance_id 必须贯穿；但“前台窗口/最近活跃”不可靠且是隐式状态。默认只应“显式 > 唯一活实例 > 报错候选”；还需要 capture_id 代际，否则旧 event/resource ID 会误伤。 |
| P12 | FTS5 天然支持前缀/模糊/OR | **部分同意** | 本机 SQLite 3.50.2 实测：`bloom*`、`bloom OR tonemap`、trigram `Downs` 都可用；拼写错误 `Blom` 返回 `[]`。FTS5 没有内建编辑距离模糊；需要规范化 + Levenshtein/spellfix。 |
| P13 | 每次调用都附带完整 context | **部分同意** | 指代消解有价值，但完整 context 会放大 token、耦合 schema。建议只回显紧凑 `scope`，完整快照按需 `rd_ui_context`；ui_act/destructive 可附带前后快照。 |
| P14 | 读工具是纯只读的 | **需要补充** | 很多读工具在 replay 回调里 `SetFrameEvent` 且不恢复：`search_service.py:43`、`action_service.py:149`、`pipeline_service.py:149,478`、`mesh_service.py:255,389,539`、`analysis_service.py:553`。`ctx.CurEvent` 不变，但 replay controller 被留在最后扫描事件。恢复应直接 `SetFrameEvent`，不要用 `SetEventID`（复核 O6）。 |
| P15 | 扩展只暴露原语，搜索/过滤/跨实例编排全放服务器 | **部分同意** | 原则对，但“薄”不等于每个 event 一次 IPC；replay-bound 提取应在扩展里批量做，服务器做 job/索引/过滤。现有 `AnalysisService` 已在扩展内组合（`analysis_service.py:29-53,93-139`），不应拆成 N 次 IPC。 |

---

## 附录 B：反方评审/事实核查逐条回应

### B.1 反方评审 objections

| # | 意见 | 处理 | 说明 |
|---|---|---|---|
| O1 | Headless 被当成可选步骤，实际需要 Python 3.6 + 匹配 core | **接受，升级为 gating prerequisite** | 本次核实：`docs/python_api/python_module.rst:18` 明确默认不发布模块；`renderdoc.pyd` 链 `PYTHON36.dll`；MCP venv 3.12.9；安装目录无 `renderdoc.pyd`。v1 不承诺 all_captures；Spike A 先验证。复核写的 venv 3.13.9 是全局 Python，`.venv` 实际 3.12.9；两者都不是 3.6，结论不变。 |
| O2 | `LoadCapture` 在 UI 线程模态加载，30s 超时，job 执行器不覆盖 capture 加载 | **接受** | 改为 operation 模型：`rd_capture_open` 返回 `operation_id`；新实例优先（但默认不启动，需显式）；已有实例写 `operations/<id>.json` 后调 `LoadCapture`；`rd_job` 读文件/持久 registry；`idempotency_key` 映射 operation；补充 `capture-load` 执行器。 |
| O3 | all_captures 没有 bootstrap 路径 | **接受** | 加 `rd_index`（post-v1、浅/深、coverage）；`rd_search(all_captures)` 只返回已索引 capture 并报告 coverage；无 headless 时 deep 不可用，shallow 只覆盖 GUI 打开过的 capture；不静默跳过。 |
| O4 | Statistics/PerformanceCounter 数据可重建，上一版过度排除 | **接受** | `StatisticsViewer.cpp:678-684` 从 ctx 取数；`PerformanceCounterViewer.cpp:344` 调 `FetchCounters`；`rd_overview` 增加 statistics/counters sections；仍不承诺 viewer UI 状态。 |
| O5 | `Get*` 惰性构造会创建隐藏面板，ui_seq 覆盖不全 | **接受** | `rd_ui_context` 先 `Has*()`，为假返回 null；不直接调用惰性 getter；改 `constructed_panels` + `visible=unknown`；250ms 轮询补状态；`ui_seq` 只覆盖可观测字段。 |
| O6 | 用 `SetEventID` 恢复会触发 UI 回调和 EventBrowser 滚动 | **接受** | 内部恢复改为 replay 线程 `BlockInvoke(SetFrameEvent(saved, True))`；加 `ui_nav_seq`；异步任务不覆盖用户新导航；读工具不调 `SetEventID`。 |
| O7 | `get_mesh_summary` 同时映射到 rd_event 和 rd_mesh，双入口 | **接受** | `rd_event` 删除 mesh section；`rd_mesh` 是唯一 mesh 入口（summary/page/export）。 |
| O8 | 15 工具 schema 更大，token/选择优势未测量 | **接受** | 15 改为候选假设；加测量门（tools/list token、first-call 正确率、任务总 token）；必要时拆分 `rd_event`/`rd_resource_data`。 |
| O9 | 给所有工具 `wait_ms` 会强制 job 轮询 | **接受** | 删除公共 `wait_ms`；普通读同步；只有 `rd_capture_open/rd_search(all_captures)/rd_index/深 usage/shader compile` 使用 operation/job；不定义自动通知，轮询是显式的。 |
| O10 | `GetUsage` sentinel 与 `include_unbound` 不存在 | **接受** | 返回 `usage_status: tracked/untracked/never_used/not_found` 与 `completeness`；sentinel `EventUsage(0, Unused)` 不丢弃；删除 `include_unbound`。 |
| M1 | 远程 replay/Android 未覆盖 | **接受，v1 明确不支持** | 当前 `open_capture` 只接受本地 path、`local=True`（`capture_manager.py:97-116`）；v1 返回 `UNSUPPORTED_REMOTE_REPLAY`；未来加 `host/remote_path`。 |
| M2 | 导出文件客户端可能读不到 | **接受** | 默认 `auto`：小图 image content + 统计；大图文件路径；`mode=inline` 显式且 <=64KB；legacy 保留 base64；不依赖 `resource_link`。 |
| M3 | 30→15 兼容层未定义 | **接受** | `RENDERDOC_MCP_LEGACY_TOOLS=1` 注册 30 个 adapter，保留旧响应形状；默认关闭；两个 minor 弃用窗口。 |
| M4 | job 持久化/恢复未闭环 | **接受** | SQLite jobs 表 + 结果文件；server 重启加载终态，running 标 interrupted；`rd_job(list/result)` 可恢复；TTL。 |
| M5 | 基础层“同步 UI 刷新”未定义 | **接受** | 加刷新矩阵（§7.6）；说明 capture open/navigate/shader edit/读工具的差异；不创建未构造面板。 |
| M6 | GetUsage 完整性未进输出契约 | **接受** | `usage_status/completeness` per API；D3D11 修正为包含 wrapper 记录的 copy/clear/resolve 等；不再说“只覆盖 draw/dispatch”。 |

### B.2 事实核查 results

| 核查项 | 状态 | 处理 |
|---|---|---|
| `SetEventID` 驱动 EventBrowser 选中/滚动；`CurEvent` vs `CurSelectedEvent` | verified | 接受；§3.1 已按 force/elapsed/过滤器/EventBrowser 存在性写清。 |
| `View*` 不自动显示，`RaiseDockWindow` 无效 | verified | 接受；必须 `AddDockWindow`/`Widget().show()`。 |
| `AddCaptureViewer` 三回调；UI 线程；`OnCaptureClosed` 在清理前 | verified（本 checkout） | 接受；其它版本未核对，不再引用未证实的 master 行为。 |
| `LoadCapture` 无保存提示；旧 ID 是否复用 | inconclusive | 接受“无提示”（`CaptureContext.cpp:921-926`）；**当前代码没有 capture 代际**，旧 ID 复用无法静态排除；本方案新增 `capture_id` 代际与 `STALE_CAPTURE`，不声称现状已有。 |
| `GetUsage` 预计算/便宜，D3D11 只覆盖 draw/dispatch | **部分拒绝事实核查** | 预计算/便宜接受；**“D3D11 只覆盖 draw/dispatch”错误**：`d3d11_context_wrap.cpp:5821-5826,6521-6526,6759-7003` 和 `d3d11_context1_wrap.cpp:473-478,570` 直接记录 Copy/CopySrc/CopyDst/Clear/Resolve/ResolveSrc/ResolveDst/Discard/GenMips/CPUWrite。完整性按 API/路径不同，输出契约必须报告，不能简单说“缺失”。 |
| 跨 capture 索引不能只靠 `OpenFile` | verified | 接受；加 `rd_index`/coverage/headless prerequisite。 |
| 面板状态部分可读；Statistics/PerformanceCounter 无 getter | verified，但需区分数据/UI | 接受 UI 状态不可读；**数据可重建**（`StatisticsViewer.cpp:678-684`；`PerformanceCounterViewer.cpp:344`；`renderdoc_replay.h:803`），已改 `rd_overview`。 |
| MCP 客户端能力/SDK 版本 | inconclusive | 接受；SDK 1.25.0 最高 2025-11-25 已核实；客户端是否消费 outputSchema/annotations/Tasks 未实测。 |
| 长 AsyncInvoke 占用 replay、关闭 capture 失效 | inconclusive | 接受静态推理；改为分批 AsyncInvoke + 取消标志 + 导航代际；需实机验证延迟/关闭行为。 |
| 多实例可独立 mailbox/heartbeat | **refuted（当前代码）** | 接受：当前是共享单槽（`socket_server.py:16-19,36-72`；`client.py:16-20`）；多进程本身允许，但 per-instance mailbox 是**提案**，未实现/未实测。已改写 load-bearing claim。 |

### B.3 我们拒绝/修正的复核结论

1. **拒绝“D3D11 GetUsage 只覆盖 draw/dispatch”**：事实核查只看了 `AddUsage`，漏了 wrapper 直接写 `m_ResourceUses`。证据：`d3d11_context_wrap.cpp:5821-5826,6521-6526,6759-7003`；`d3d11_context1_wrap.cpp:473-478,570`。正确说法是“查询便宜、完整性按 API/路径不同，输出要报告覆盖类别”。
2. **修正“多实例 claim refuted”的表述**：当前实现共享单槽，复核对现状的 refuted 成立；但本文的 claim 是“提案要求 per-instance”，不是“现状已有”。已改写为“当前不支持，需新增并实测”。
3. **修正复核的 venv 版本**：`.venv/Scripts/python.exe -V` 是 3.12.9；全局 `python -V` 是 3.13.9；两者都不是 3.6。结论（headless 需要 3.6）不变。
4. **修正上一版 docket 断言**：`.venv` 里 `docket` 存在，不能再说“find_spec 为 None”；不用 Tasks 的理由改为扩展 opt-in/客户端矩阵未列/FastMCP sync 函数不能 task=True。

---

## 附录 C：Codex 会诊逐条回应

1. **“三层只应作为产品能力分组，不能直接作为代码分层；按状态所有者/执行位置切模块”**：同意。§2/§4/§7.1 已改为 state owner/execution location；工具数量不锁死，15 是候选 + 测量门。
2. **“D3D11 copy/resolve/clear 包装直接写 m_ResourceUses；草案整体排除错误”**：**Codex 正确**。本次 `rg` 直接验证 wrapper 行号；已修正 P6/§3.3/§7.9。事实核查只查了 `d3d11_context.cpp` 的 `AddUsage`，漏了 wrapper 文件。
3. **“SetEventID 恢复会覆盖用户在异步任务期间的新导航；单 AsyncInvoke 循环仍独占 replay；tag 去重不是取消”**：同意。改为分批 AsyncInvoke + `ui_nav_seq` + 直连 `SetFrameEvent` 恢复 + 取消标志。
4. **“CaptureViewer + dirty flag 不足以维持完整 UI 快照”**：同意。加 250ms 轮询；`ui_seq` 只覆盖 observed 字段；状态带 `observed_at/sources/fields_unknown`。
5. **“资源内容随 event 变化；跨 capture 身份不能只靠 ResourceId”**：同意。`rd_resource_data` 加 `event_id`/`source`/`session_modifications`；`resource_ref={capture_id,resource_id}`；跨 capture 用 `capture_file_id`/`index_version`。
6. **“IPC deadline 替换 pending 有竞态；busy=true 不能永久免死”**：同意。改每请求文件 + `requests→processing` 原子 rename 领取；busy 超时标 unresponsive；不再单槽替换。
7. **“搜索需要 typed predicates/AND-OR；terms+fields 不够”**：同意。`rd_search` 用谓词树 + `same_event`；返回实体类型/证明；FTS5 只做预筛。
8. **“没有显式 output_schema= 不等于没有 outputSchema；FastMCP 会推导”**：同意前半。当前 `-> dict` 的问题是**缺字段级契约**，不是完全没有 schema；本次 `mcp.list_tools()` 已直接抓到通用 object schema。
9. **“导航不应仅因改 UI 标 destructive；文件导出不能统一标 read-only”**：同意，已在 annotations 中区分。
10. **“建议工作区协调器、replay 执行适配、独立 worker、查询/导航分离、数据时间点、任务可追踪、覆盖度报告、跨 capture 匹配依据”**：同意，已映射到 §7.1/§7.5/§7.7/§7.8。

Codex 本次可用；其回答来自独立会诊（输入材料），本文没有逐行复核它引用的所有行号，但关键 D3D11/Statistics/FetchCounters 已由本次 `rg` 验证。

---

## 附录 D：输入材料与版本说明

- 第一版评估：`.zcode/workflow-drafts/first-evaluation.md`（仓库内）。
- 上一轮草案：`out/renderdoc-mcp-refactor-draft.md`（仓库内，**已被本文取代**；其中 D3D11 GetUsage/headless 可选性等结论有误，不要作为最终依据）。
- 四份调研材料与两轮复核意见：本次对话输入，**不在仓库中**，无法用 git 历史追溯；其中规范结论在本轮没有重新抓取，已在 §6 标注来源和状态。
- RenderDoc 源码：`D:/Projects/renderdoc`，分支 `feature/renderdic_customhook`，`v1.45-354-g5f3763615`，commit `5f3763615e57`；不是官方 clean tag。UI 行为矩阵若要用于其它版本，必须以目标 release tag 重核。
