# RenderDoc MCP Server 重构：ArchitectureDraft

> 版本：2026-10-20  
> 范围：MCP Server + RenderDoc UI 扩展的整体重构，不含实现代码。  
> 证据边界：本草案只做静态审查，**没有启动/调用 qrenderdoc、renderdoccmd、renderdoc、wscript/cscript、Start-Process、--ui-python 或 LoadCapture**；没有做实机回放、UI 操作、双实例或频率测量。所有涉及真实 UI、双实例、headless replay、编译耗时的结论都标为“未实测”。  
> 本次实际执行的只读检查：`rg -c "^@mcp.tool" mcp_server/server.py` → 30；`rg -n "annotations=|output_schema=|timeout=" mcp_server/server.py` → 无输出；`python - <<PY` 的 SQLite FTS5 测试（见 §3 P12）；`python -c "importlib.util.find_spec(...)"` → `renderdoc`/`qrenderdoc` 均为 None；`python -V` → 3.13.9；`rg` 读取 `mcp/types.py` → `LATEST_PROTOCOL_VERSION = "2025-11-25"`。  
> 四份调研材料记为：【MCP 规范】【RenderDoc 能力】【仓库现状】【同类实践】。RenderDoc 源码引用基于本地 checkout `D:/Projects/renderdoc`，commit `5f3763615e57`（2026-10-03）。  
> 本机没有把 RenderDoc 的 standalone Python 模块装进 MCP server 的解释器（`find_spec('renderdoc') == None`），这不等于用户的 RenderDoc 安装没有该模块；headless 的部署条件因此列为待验证。

---

## 0. 结论摘要

1. **三层划分作为“路线图”基本成立，作为“工具分类轴”不成立。** “交互层”是横切输入，不是一层工具；“进阶层”混合了跨 capture、长任务和副作用，三者并不正交。真正该切的是：每次调用需要哪个显式 handle（instance/capture/event/resource）、同步还是 job、副作用是什么、载荷是内联还是文件。
2. **“完全复刻 RenderDoc 面板”按字面做不到。** qrenderdoc 只暴露了部分面板的数据模型；`StatisticsViewer`、`PerformanceCounterViewer` 只有 `Widget()`，没有数据 getter；没有全局 `CurSelectedResource`；`Has*()` 只表示对象被构造过，不表示可见。可交付的是“主分析面板的语义对等 + 导航同步”，不是像素/布局复刻。
3. **“跳到对应 drawcall”可行，但依赖面板已存在。** `SetEventID` 会驱动 EventBrowser 选中并 `scrollTo`；如果 EventBrowser 尚未实例化（或调用时被 exclude），逻辑导航仍会移动 replay，但不会滚动。第一版评估把 `ViewShader/ViewBuffer/...` 的显示方式写成 `RaiseDockWindow()`，这是事实错误：这些窗口既没有 show 也没有 dock，必须 `AddDockWindow()` 或 `Widget().show()`。
4. **“读取用户当前候选状态”只能做到“已提交状态的有限快照”。** 可以读 `CurEvent`/`CurSelectedEvent`/`CurSelectedAction`、TextureViewer 的当前资源/子资源/overlay/zoom/picked location、EventBrowser 的 filter text、ResourceInspector 的当前资源；读不到 hover/未确认候选，也没有所有面板的统一状态，PipelineStateViewer 只有 setter 没有 selected-stage getter，BufferViewer 只有 setter。
5. **进阶层不是“再写几个工具”，而是协议和进程模型的升级。** 单 capture 的 `GetUsage` 查询便宜，但 D3D11 只覆盖 draw/dispatch 的绑定使用，不覆盖 copy/clear/resolve；跨 capture 搜索不能占用 GUI 实例，必须走索引 + headless replay 或扩展内分段 AsyncInvoke；多实例必须先做 per-instance mailbox + 显式 handle。
6. **收敛后的工具面是 15 个**：`rd_captures`、`rd_capture_open`、`rd_overview`、`rd_events`、`rd_event`、`rd_resources`、`rd_resource_data`、`rd_resource_usage`、`rd_shader`、`rd_shader_edit`、`rd_search`、`rd_mesh`、`rd_ui_context`、`rd_ui_act`、`rd_job`。30 个旧工具全部有映射，但有明确牺牲（见 §4.4）。

---

## 1. overallVerdict

三层捕捉的是真实需求，但它是**能力成熟度/路线图的切分**，不是工具面的分类轴：“交互层”是横切输入，“进阶层”混合了跨 capture、长任务和副作用，三者并不正交。作为路线图，“先数据、再上下文、再跨实例/跨捕获”基本正确；作为架构，应按每次调用需要的显式 handle（instance/capture/event/resource）、执行模型（同步/job）、副作用（读/改 UI/改 replay 状态/写文件）和载荷形态（内联/文件）来切。  
“完全复刻面板”按字面做不到：qrenderdoc 只暴露部分面板的数据模型，`StatisticsViewer`、`PerformanceCounterViewer` 只有 `Widget()`，没有数据 getter（`qrenderdoc/Code/Interface/QRDInterface.h:1452-1550`）；可交付的是主分析面板的**语义对等 + 导航同步**，不是像素/布局复刻。  
进阶层不是“更高级的工具”，而是同一批工具在显式作用域和 job 协议上的延伸；没有 per-instance IPC、capture 代际和长任务协议，跨 capture 搜索与多实例切换按当前描述不可落地。

---

## 2. layerVerdicts

### 2.1 基础层：**按当前描述不可行（字面）；重定义为“能力对等 + 导航”后有条件可行**

**为什么字面复刻做不到（静态已核）：**

1. **部分面板没有数据模型。** `IStatisticsViewer` 只有 `Widget()`；`IPerformanceCounterViewer` 只有 `Widget()` 和 `UpdateDurationColumn()`（`QRDInterface.h:1452-1550`）。MCP 无法“读出”这两个面板的内容。
2. **没有全局“选中资源”。** `ICaptureContext` 有 `CurEvent()`、`CurSelectedEvent()`、`CurAction()`、`CurSelectedAction()`，但没有 `CurSelectedResource()`；资源选择分散在 `ITextureViewer::GetCurrentResource()` 和 `IResourceInspector::CurrentResource()`（`QRDInterface.h:826,1043`；`rg` 未发现 `CurSelectedResource`）。
3. **`Has*()` 不代表可见。** `HasEventBrowser()` 等只判断单例指针非空（`CaptureContext.h:237-265`）；`Get*()` 首次调用创建窗口后立刻 `hide()`（`CaptureContext.cpp:2347-2417` 的 `setupDockWindow(..., true)`），`Show*()` 才负责“显示/抬起”（`QRDInterface.h:3222-3255`）。
4. **`View*` 窗口不是 dock 窗口。** `ViewShader`、`ViewBuffer`、`ViewTextureAsBuffer`、`ViewPixelHistory` 只 `new` 出窗口，既不 `show()` 也不 `AddDockWindow()`（`CaptureContext.cpp:2746-2812`）；文档明确写 “opened, but not shown”（`QRDInterface.h:3298-3395`）。`RaiseDockWindow()` 只在父级是 `ToolWindowManagerArea` 时切换 tab，否则只打印 warning（`ToolWindowManager.cpp:549-569`）。**第一版评估在这里写错了**；正确做法是 `AddDockWindow(window, DockReference.TransientPopupArea/MainToolArea, ...)`（`QRDInterface.h:3437`；`CaptureContext.cpp:2972-3000`）或 `Widget().show()`。
5. **面板可见性没有可靠 getter。** `Has*()` 只表示构造过；如果 PySide2 可用，可以用 `Widget().isVisible()` 补，但这依赖 PySide2 且未实测。

**可行的那部分（用户真正要的）：**

- Event Browser 的信息模型 → `rd_events`（action 树、marker、分页）；
- Pipeline State Viewer → `rd_event(sections=pipeline)`；
- Texture Viewer → `rd_resources` + `rd_resource_data` + `rd_ui_act(show_panel=texture_viewer)`；
- Mesh Viewer → `rd_mesh`；
- Shader Viewer → `rd_shader` / `rd_shader_edit`；
- Resource Inspector 的使用链 → `rd_resource_usage`；
- Timeline 的时间信息 → `rd_overview(include_timings=true)` / `rd_event(sections=timing)`；
- “跳到对应 drawcall” → `rd_ui_act(action=navigate)` + `SetEventID`。

**条件：** 只承诺“主分析面板的信息对等 + 导航”，明确排除 Pixel History 的 UI 状态、API Inspector 的当前行、Statistics/PerformanceCounter 的内容、Texture Viewer 的完整 viewport/range 状态、Mesh Preview 的相机/overlay。v1 给覆盖矩阵，不给“完全复刻”。

**导航细节（静态已核）：** `SetEventID(exclude, selectedEventId, eventId, force=False)` 更新 selected/effective 两个 EID，经 tagged `AsyncInvoke` 在 replay 线程执行 `SetFrameEvent`，并同步等待完成；capture 未加载或 `eventId > m_LastAction->eventId` 时直接 no-op（`CaptureContext.cpp:1695-1748`；`QRDInterface.h:2424-2436`）。EventBrowser 的 `OnEventChanged` 调用 `SelectEvent(CurSelectedEvent())`，`SelectEvent` 再 `ExpandNode` → `scrollTo`（`EventBrowser.cpp:4115-4124,5815-5853`）。因此要滚动，EventBrowser 必须已经存在，且 `force=True` 才能在“同一 event”时也触发回调。

### 2.2 交互层：**有条件可行**

**可读的（静态已核）：**

| 状态 | API | 备注 |
|---|---|---|
| 当前 capture / 是否加载 | `IsCaptureLoaded()`、`GetCaptureFilename()` | 无 capture 代际，需要新加 |
| effective event | `CurEvent()` | replay 实际到达的事件 |
| selected event | `CurSelectedEvent()` | 用户选中的行/marker；与 effective 可不同 |
| selected/current action | `CurSelectedAction()`、`CurAction()` | |
| Texture Viewer 当前资源 | `GetTextureViewer().GetCurrentResource()` | 只在该面板存在时有意义 |
| Texture Viewer 子资源 | `GetSelectedSubresource()` / `SetSelectedSubresource()` | |
| Texture display/zoom/overlay/picked | `GetTextureDisplay()`、`GetZoomLevel()`、`IsZoomAutoFit()`、`GetTextureOverlay()`、`GetPickedLocation()` | |
| Event Browser filter | `GetCurrentFilterText()` / `SetCurrentFilterText()` | `QRDInterface.h:480-487` |
| Resource Inspector 当前资源 | `GetResourceInspector().CurrentResource()` | |
| 面板是否构造过 | `Has*()` | **不代表可见** |

**读不到的（因此不能承诺）：**

- hover/未确认候选、拖拽中的临时状态；
- 全局 selected resource；
- PipelineStateViewer 的当前 stage（只有 `SelectPipelineStage()`，没有 getter）；
- BufferViewer 的当前 instance/view/stage（只有 setter：`SetCurrentInstance`、`SetCurrentView`、`SetPreviewStage`）；
- ShaderViewer 的滚动位置/当前行；
- StatisticsViewer、PerformanceCounterViewer 的内容；
- 面板可见性（`Has*` 只表示构造过；`Widget().isVisible()` 依赖 PySide2，未实测）。

**三个必须处理的坑：**

1. **注册时机。** `AddCaptureViewer()` 在 capture 已加载时会同步触发 `OnCaptureLoaded()`、`OnSelectedEventChanged(CurSelectedEvent())`、`OnEventChanged(CurEvent())`（`CaptureContext.h:135-145`）。viewer 必须完全构造完再注册，否则会在半初始化状态被回调。
2. **事件风暴。** TimelineBar 在左键 `mouseMoveEvent` 里直接调用 `SetEventID`，没有 timer/debounce（`TimelineBar.cpp:385-420`）；`SetEventID` 又会同步等待 replay（`CaptureContext.cpp:1716-1747`）。实际回调频率被 replay 延迟和 tagged `AsyncInvoke` 的队列合并限制，不是“每个鼠标移动都触发一次”，但写 status.json 仍然必须合并（建议 150–250ms dirty flag + QTimer）。
3. **线程。** 扩展 Python 在 UI 线程；回调里不要做 `BlockInvoke` 或大文件 I/O。快照回调只更新内存 + dirty flag；写盘由定时器做。

**MCP 侧的限制：** 如果协商到 2026-07-28，协议级 session 已移除，跨请求状态必须用显式 handle；本仓库安装的 MCP SDK 实际最高是 2025-11-25（`mcp/types.py:27`），仍可能有 session，但不应把业务状态寄托在 session 上。无论哪个版本，`instance_id`/`capture_id` 都应显式传递；服务端不能靠“上一次调用打开了哪个 capture”来决定这次的行为。

### 2.3 进阶层：**有条件可行；在现有 IPC 上按当前描述不可行**

**现有 IPC 的硬约束（静态已核）：**

- 固定目录 `%TEMP%/renderdoc_mcp/`，固定 `request.json` 单槽；`host/port` 是死参数（`client.py:16-20,35-38`；`socket_server.py:16-19,25-34`）。
- 请求体只有 `{id, method, params, ipc_version}`，没有 instance/capture 标识（`client.py:91-96`）。
- 两个实例都 100ms 轮询同一个 `request.json`；先 `os.remove` 的实例赢，另一个在 `handle` 之前就失败（`socket_server.py:43-46,74-99`）。这不是概率问题，是语义错误。
- 启动/停止任一实例都会 `_cleanup_files()` 删共享的 `request.json/response.json/lock`（`socket_server.py:36-41,52-58,65-72`），会吞掉另一个实例的请求。
- 普通工具 30s、5 个 shader 编辑方法 120s（`client.py:22-23,39-40,97`）；超时后扩展仍可能执行并写 `response_<id>.json`，但客户端已不读；未提交的 pending 请求会永久挡住后续调用（`client.py:103-108`；`socket_server.py:107-114`；`tests/test_bridge.py:107-129`）。
- 每个请求在 UI 线程的 QTimer 槽里同步执行，replay 访问经 `BlockInvoke`（`socket_server.py:43-46,74-99`；`renderdoc_facade.py:58-60`）。长扫描会冻结 UI。

**进阶层里哪些其实便宜、哪些不便宜：**

| 能力 | 可行性 | 代价/条件 |
|---|---|---|
| 单 capture 内“这个 texture 在哪些 event 被用” | 可行，`GetUsage()` 是加载期预计算的 per-resource 表 | D3D11 只覆盖 draw/dispatch/CmdList 的绑定；copy/clear/resolve 可能不出现；D3D12 有 per-event resourceUsage；不是 O(1)，是 map lookup + O(k) 拷贝 |
| 单 capture 内“按名字/模糊/OR 搜 marker/resource/event” | 可行 | action/resource 名可从已加载的 `ctx.CurRootActions()`/`GetTextures()`/`GetBuffers()` 取，无需 replay；shader 名需要逐 event pipeline，需 replay |
| 跨多个 .rdc 搜索 | 可行但不应在 GUI 实例做 | 需要 headless replay 或索引；`OpenFile` 只解码容器/元数据，不做 graphics API 调用；枚举 action/resource 通常要 `OpenCapture`（replay）或自行解析 SD |
| 多实例切换 | 技术可行 | 需要 per-instance mailbox、heartbeat、显式 handle；没有标准 MCP 路由原语 |
| 自由打开/切换 RenderDoc | 技术可行 | MCP server 侧启动 qrenderdoc（位置参数传 capture，`qrenderdoc.cpp:475-486`），等待 heartbeat；涉及进程所有权和数据丢失风险 |
| “整个 rdc 搜一个 texture 的像素内容” | 不在本方案 v1 | 需要逐 draw 回读/扫描，代价高；先明确搜索的是 usage/绑定/元数据，不是像素值 |

**结论：** 进阶层不是“加一个 search 工具”能解决的；它要求先把 IPC 从“单槽广播”改成“按实例寻址”，再把长任务从“同步阻塞”改成“job handle + 结果落盘”，最后把跨 capture 的深扫描移到 headless。现有 30s/120s 同步模型下，按当前描述不可行。

---

## 3. positions：与第一版评估的分歧

> 结论：第一版的大方向（不要逐面板、交互层先行、per-instance、自建 job、收敛工具）大体正确；但有 4 个事实错误/遗漏：`RaiseDockWindow`、`save_texture` base64、`GetUsage` 的完整性、以及“索引不需要 replay”。此外它没有讨论 MCP 无状态化、capture 代际、读工具的 replay cursor 副作用。

| # | 第一版论断 | 立场 | 依据 |
|---|---|---|---|
| P1 | 三层按“难度”切是错的，应按状态归属/副作用/作用域/载荷四个正交维度切 | **部分同意** | 同意“按难度切”不适合做工具分类；但四维是设计检查表，不是分层方案。副作用落在 annotations，载荷落在返回形态，二者不是“层”。实际切法是“handle + 执行模型 + 效果 + 载荷”；层只是聚合。当前 30 个工具的 `rg -c "^@mcp.tool"` 结果是 30，`annotations/output_schema/timeout` 一个都没有，说明旧工具面确实没有按这些维度设计。 |
| P2 | “完全复刻面板”是陷阱，应做信息模型 | **同意方向，但第一版仍低估了不可行范围** | `IStatisticsViewer`/`IPerformanceCounterViewer` 只有 `Widget()`/`UpdateDurationColumn()`（`QRDInterface.h:1452-1550`）；没有全局 `CurSelectedResource`；`IBufferViewer` 只有 setter；`IPipelineStateViewer` 只有 `SelectPipelineStage` 没有 getter。不是“不要做 20 个工具”，而是有些面板根本读不出来。另外第一版说 `CurPipelineState()` “恒有效”：它在无 capture 时被设为 `&m_DummyPipelineState`（`CaptureContext.cpp:1570-1572`），不是可用状态；工具必须先检查 `IsCaptureLoaded()`。 |
| P3 | `ViewShader`/`ViewBuffer`/`ViewTextureAsBuffer`/`ViewPixelHistory` 返回“已打开但未显示”，必须自己调 `RaiseDockWindow()` | **不同意（事实错误）** | 这些窗口没有 show 也没有 dock（`CaptureContext.cpp:2746-2812`）；`RaiseDockWindow` 对非 `ToolWindowManagerArea` 只 `qWarning`（`ToolWindowManager.cpp:549-569`）。必须 `AddDockWindow()`（`CaptureContext.cpp:2972-3000`）或 `Widget().show()`。按第一版实现，`show_panel` 会静默失败。 |
| P4 | `AddCaptureViewer()` 在已有 capture 时会同步触发 `OnCaptureLoaded()` 和 `OnEventChanged()` | **部分同意（漏了一个）** | `CaptureContext.h:135-145` 还会触发 `OnSelectedEventChanged(CurSelectedEvent())`；三个回调都要能处理。`OnCaptureClosed()` 在本 checkout 里于 `m_CaptureLoaded=false` 和 `CloseThread()` **之前**调用（`CaptureContext.cpp:1515-1526,1570-1574`），回调内对象还在，但返回后不得再持有。 |
| P5 | 拖动 timeline 会连续触发 `OnEventChanged`，快照必须 150–250ms 防抖 | **部分同意** | TimelineBar 确实每次 `mouseMoveEvent` 调 `SetEventID`（`TimelineBar.cpp:385-420`），但 `SetEventID` 同步等待 replay，且 tagged `AsyncInvoke` 会删除队列中同 tag 的待处理项（【RenderDoc 能力】finding 6；`ReplayManager.cpp:255-283`），实际回调率被 replay 延迟限制。防抖仍然要做，但理由是“写盘/快照成本”，不是“每个鼠标事件都会回调”。具体 Hz 未实测。 |
| P6 | `GetUsage()` 是 O(1)，返回“每个事件对资源的访问方式”，单 capture 搜索完全可行 | **部分同意（两处不准确）** | 用法表在加载期预计算（`resource_usage.rst:3-5,13,36`），查询是 map lookup + vector copy，不是 O(1)。D3D11 的 `AddUsage` 只对 `Drawcall/Dispatch/CmdList` 记录绑定（`d3d11_context.cpp:1077-1092,1228`）；copy/clear/resolve 不保证出现。D3D12 有 per-event `resourceUsage`（`d3d12_commands.cpp:2357`），完整性按 API 不同。要“整个 rdc 的所有使用”，需要知道完整性边界或补扫描。 |
| P7 | 跨 capture “索引优先”：首次打开 capture 时后台索引 action 树/资源名/shader 名，不需要 replay | **不同意/需要补充** | `CaptureFile.OpenFile` 只解码容器和元数据，不做 graphics API 调用（`capture_access.rst:46`）；action 树/资源名来自已加载的 `ctx.CurRootActions()`/`GetTextures()`/`GetBuffers()`（`QRDInterface.h:2655,2670,2760`），对从未在 GUI 打开过的 capture 需要 `OpenCapture`（replay）或自行解析 SD。所以“不需要 replay”只对“已经在 GUI 打开的 capture 的浅元数据”成立；跨 capture 首次索引仍要 headless replay，成本不低。 |
| P8 | `get_texture_data` 和 `save_texture` 内部都 base64 | **不同意（部分事实错误）** | `save_texture` 调用 `controller.SaveTexture(tex_save, output_path)` 写文件（`resource_service.py:204-213`），没有 base64。base64 只在 `get_buffer_contents`（`:256`）和 `get_texture_data`（`:399`）。要改的是这两个读接口，不是 save_texture。 |
| P9 | `ui_act` 导航是 destructive（改变用户 UI 状态） | **不同意** | `readOnlyHint=false` 是对的；但 `destructiveHint` 表示“可能做破坏性更新”，导航是可逆的 UI 状态变化，应为 `destructiveHint=false`、`idempotentHint=true`。把导航标成 destructive 会让客户端每次跳转都弹确认，违背“用户说跳过去就跳过去”。destructive 留给 `capture_open` 和 shader 替换。 |
| P10 | MCP 2025-11-25 有 experimental Tasks，自己实现 job 更稳 | **同意结论，需要更新版本与理由** | 按【MCP 规范】，2026-07-28 已把 Tasks 移出核心，成为 `io.modelcontextprotocol/tasks` 扩展，客户端矩阵未列它；本仓库安装的 `mcp` 1.25.0 最高协议是 2025-11-25（`mcp/types.py:27`），FastMCP 的 tasks 路径需要 `fastmcp[tasks]`/docket，而本机 `find_spec('docket') == None`。自建 job 仍然更稳，且不依赖客户端 opt-in。 |
| P11 | 所有工具都应接受可选 `instance_id`；默认解析“显式 > 前台窗口 > 最近活跃 > 唯一 > 报错” | **同意前半，不同意默认解析** | `instance_id` 必须贯穿（`client.py:91-96` 现在完全没有）。但“前台窗口”没有可靠 API，“最近活跃”是隐式时间状态，违反“显式 handle”原则。默认只应“显式 > 唯一活实例 > 报错列出候选”；多实例时不要猜。还需要 `capture_id`（代际），否则事件/资源 ID 在 capture 切换后会误伤。`shader_edit_service.py:29,48-62` 的 generation 机制可以推广。 |
| P12 | FTS5 天然支持前缀/模糊/OR 查询 | **部分不同意（“模糊”被夸大）** | 本机 SQLite 3.50.2 实测：`bloom*` 匹配 `BloomDownsample/BloomUpsample`；`bloom OR tonemap` 正常；trigram tokenizer 的 `Downs` 能匹配 `BloomDownsample`；但拼写错误 `Blom` 返回 `[]`。FTS5 没有内建编辑距离模糊；要做 typo 容忍，需额外规范化 + Levenshtein/spellfix。 |
| P13 | 每次工具调用都附带完整 `context` 字段 | **部分不同意** | “指代消解”是对的，但把完整 context 塞进每个响应会放大 token、耦合所有 outputSchema，并让缓存/分页更复杂（Anthropic 建议 25k token 上限，【MCP 规范】/【同类实践】）。建议：每个响应只回显紧凑 `scope`（instance_id/capture_id/event_id/ui_seq），完整快照用 `rd_ui_context`；只在 `rd_ui_act`/destructive 工具的结果里附带完整 context。 |
| P14 | 读工具是纯只读的 | **需要补充** | 很多“读”工具在 replay 回调里调用 `SetFrameEvent` 且不恢复：`search_service.py:43`、`action_service.py:149`、`pipeline_service.py:149,478`、`mesh_service.py:255,389,539`、`analysis_service.py:553`。`ctx.CurEvent` 不变，但 replay controller 被留在最后一个扫描事件，属于隐藏副作用。设计上要么用 scoped save/restore（`shader_edit_service.py:106-109` 的做法），要么把扫描移到 headless。 |
| P15 | 扩展只暴露原语，搜索规划/过滤/跨实例编排全部放服务器端 | **部分同意** | 原则正确，但“薄”不等于“每个 event 一次 IPC”。replay-bound 的提取（pipeline、usage、mesh、shader）必须在扩展里批量做，否则 N 个 event 会产生 N 次 UI-thread/BlockInvoke 往返，比现在的 `AnalysisService` 编排更卡。服务器应负责 job 生命周期、跨 capture 规划、过滤/分页/索引；扩展负责“一次调用内批量提取 + 进度/取消”。现有 `AnalysisService` 已经在扩展内组合（`analysis_service.py:29-53,93-139`），不应该为了“薄”把它拆成 N 次 IPC。 |

**第一版没有覆盖、但会改变设计的三点：**

1. **MCP 无状态化/session 问题。** 如果协商到 2026-07-28，跨调用状态必须用显式 handle；本仓库 SDK 仍支持 2025-11-25，但不能把“当前 capture/当前 event”存在服务端。所有工具签名从第一天就要带 `instance_id`/`capture_id`。
2. **capture 代际。** 同一路径重新打开必须是新 `capture_id`；旧 job、旧 shader edit、旧资源 ID 必须失败并可恢复。现有 `ShaderEditService._generation` 只覆盖 shader 编辑，应提升为全局 session 状态。
3. **读工具的 replay cursor 副作用。** 见 P14；这与“只读”注解不矛盾（不修改用户数据），但会影响后续调用的确定性，必须在架构里解决。

---

## 4. proposedTools

### 4.1 设计规则

1. **按工作流合并，不按 API/面板 1:1。** 每个工具只回答一个唯一问题；名字用 `rd_` 前缀（避免和其它 server 聚合时冲突）。
2. **15 个 = 12 个领域工具 + 3 个基础设施（`rd_captures`、`rd_ui_context`、`rd_job`）。** 比第一版的 12 个多，是因为多实例发现、上下文和长任务必须有显式入口；比现在的 30 个少 15 个。
3. **四个注解全部显式。** 规范默认是 `readOnlyHint=false, destructiveHint=true, idempotentHint=false, openWorldHint=true`；不写等于把所有工具都当危险操作。所有工具都是本地 closed-world，`openWorldHint=false`。
4. **所有工具声明 outputSchema（根是 object）**，返回 `structuredContent`，并回填序列化 JSON 的 `TextContent` 以兼容旧客户端。错误走 `isError:true`，不承诺 `structuredContent` 符合 outputSchema（规范未明确，见 §8）。
5. **大载荷 reference-over-value。** 不在 JSON 里 inline base64；二进制/大文本写文件，返回路径 + 摘要 + 可选的小预览（image content 只在明确要求且尺寸受限时用）。
6. **作用域显式。** 所有工具接受 `instance_id?` 和 `capture_id?`；内部 replay 读必须 scoped，不留下 cursor 副作用。
7. **写操作有幂等/并发保护。** `rd_capture_open` 用 `idempotency_key`；`rd_shader_edit(apply)` 用 `edit_id + expected_revision`；`rd_job(cancel)` 二次调用 no-op；导出默认拒绝覆盖。
8. **工具列表静态。** 能力缺失（headless 不可用、shader 编辑不支持）返回 `TOOL_UNAVAILABLE`/`UNSUPPORTED_*`，不动态增删工具（`tools/list` 不得随连接变化）。

### 4.2 工具表

| # | name | purpose（回答什么问题） | sideEffect | annotations |
|---|---|---|---|---|
| 1 | `rd_captures` | 现在有哪些 RenderDoc 实例、各自加载了哪个 capture，某个目录里有哪些 `.rdc`？这次调用该用哪个 `instance_id`/`capture_id`？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 2 | `rd_capture_open` | 把指定 capture 打开/切换到一个实例（没有实例时可启动一个）后，新的 `capture_id` 是什么？ | destructive / cross-capture | `{"readOnlyHint":false,"destructiveHint":true,"idempotentHint":false,"openWorldHint":false}` |
| 3 | `rd_overview` | 这一帧/pass 的整体工作负载是什么，时间花在哪，先看哪些 event？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 4 | `rd_events` | 在这个 marker/事件区间/标志过滤下，有哪些 action，层级和分页是什么？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 5 | `rd_event` | 这个 event 的详情、管线、资源依赖、时间、网格摘要是什么；与另一个 event 相比哪里变了？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 6 | `rd_resources` | 当前 capture 里有哪些 texture/buffer，按名称/格式过滤后是什么？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 7 | `rd_resource_data` | 这个资源的内容长什么样、统计特征是什么、如何导出成文件/小预览？ | file-write（不改 capture） | `{"readOnlyHint":false,"destructiveHint":false,"idempotentHint":false,"openWorldHint":false}` |
| 8 | `rd_resource_usage` | 这个资源在整帧/整个 capture 的哪些 event 被读/写/消费，完整性如何？ | read-only（可返回 job） | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 9 | `rd_shader` | 这个 event/资源绑定的 shader 是什么，源码/反汇编/反射/常量缓冲/绑定是什么？ | read-only | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 10 | `rd_shader_edit` | 如何准备、应用、还原、列出或导出当前 capture 会话里的 shader 替换？ | destructive（改 replay 资源 + UI replacement 映射；不改 .rdc） | `{"readOnlyHint":false,"destructiveHint":true,"idempotentHint":false,"openWorldHint":false}` |
| 11 | `rd_search` | 在这帧或所有已索引 capture 里，哪些 marker/资源/shader/event 匹配这组词（all/any/模糊）？ | read-only（可返回 job） | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 12 | `rd_mesh` | 这个 draw 的网格拓扑、顶点/索引数据是什么，如何分页或导出？ | file-write for export；其余 read-only | `{"readOnlyHint":false,"destructiveHint":false,"idempotentHint":false,"openWorldHint":false}` |
| 13 | `rd_ui_context` | 用户现在在 RenderDoc 里看的是哪个 capture/event/资源/面板/过滤条件？ | read-only（UI 状态） | `{"readOnlyHint":true,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 14 | `rd_ui_act` | 把用户的 RenderDoc UI 导航到正在讨论的 event/资源/面板/视图。 | ui-state | `{"readOnlyHint":false,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |
| 15 | `rd_job` | 之前那个长任务现在什么状态、结果在哪、能不能取消？ | job-control（status/result 只读；cancel 改 job 状态） | `{"readOnlyHint":false,"destructiveHint":false,"idempotentHint":true,"openWorldHint":false}` |

**关键参数（不是全部 schema）：**

- 公共：`instance_id?`、`capture_id?`、`wait_ms?`（默认 3000–5000；超时返回 job）。
- `rd_captures`：`directory?`、`include_stale?`。
- `rd_capture_open`：`capture_path`、`instance_id?`、`launch_if_missing?`（默认 false）、`discard_unsaved?`（默认 false）、`idempotency_key?`。
- `rd_overview`：`marker?`、`include_timings?`、`detail?`。
- `rd_events`：`marker?`、`exclude_markers?`、`event_range?`、`flags?`、`only_actions?`、`cursor?`、`limit?`。
- `rd_event`：`event_id`、`sections?`（summary/pipeline/resources/shader/timing/mesh/dependencies/all）、`compare_to?`。
- `rd_resources`：`kind?`（texture/buffer/all）、`resource_id?`、`name_query?`、`format?`、`cursor?`、`limit?`。
- `rd_resource_data`：`resource_id`、`subresource?`（mip/slice/sample/depth_slice）、`mode?`（preview/stats/file/hex）、`output_path?`、`max_dimension?`。
- `rd_resource_usage`：`resource_id` 或 `name_query?`、`usage_kinds?`、`marker?`、`event_range?`、`group_by?`、`include_unbound?`。
- `rd_shader`：`event_id?`、`stage?`、`resource_id?`、`parts?`。
- `rd_shader_edit`：`action`（prepare/apply/revert/list/export）、`edit_id?`、`event_id?`、`stage?`、`mode?`、`source_text?`、`output_path?`、`expected_revision?`。
- `rd_search`：`terms[]`、`mode?`（all/any）、`fuzzy?`、`fields?`、`scope?`（current_capture/all_captures）、`limit?`、`cursor?`。
- `rd_mesh`：`event_id`、`stage?`、`mode?`（summary/page/export）、`offset?`、`limit?`、`attributes?`、`output_path?`。
- `rd_ui_context`：`include?`（events/texture/panels/all）。
- `rd_ui_act`：`action`（navigate/show_panel/select_resource/set_texture_view/set_event_filter/focus）、`event_id?`、`selected_event_id?`、`panel?`、`resource_id?`、`subresource?`、`overlay?`、`zoom?`、`filter_text?`。
- `rd_job`：`action`（status/result/cancel/list）、`job_id?`、`instance_id?`。

### 4.3 合并映射（30 → 15）

| 新工具 | 合并的旧工具 | 说明 |
|---|---|---|
| `rd_captures` | `get_capture_status` + `list_captures` | 实例/捕获/目录列表合一；`capture_id` 在这里返回 |
| `rd_capture_open` | `open_capture` | 增加 instance 路由、可选 launch、未保存修改检查、幂等键 |
| `rd_overview` | `get_frame_summary` + `summarize_capture` + `analyze_pass` + `get_action_timings`（汇总） | 一份“这一帧/这个 pass 大致如何”的答案 |
| `rd_events` | `get_draw_calls` | 统一 marker/range/flags，树/平铺 + 分页 |
| `rd_event` | `inspect_event` + `get_draw_call_details` + `get_pipeline_state` + `trace_event_dependencies` + `diff_events` + `get_action_timings`（单事件） + `get_mesh_summary` | `sections` 选段；`compare_to` 取代独立 diff |
| `rd_resources` | `list_resources` + `get_texture_info` | 统一 texture/buffer 枚举；单资源详情用 `resource_id` |
| `rd_resource_data` | `get_texture_data` + `get_buffer_contents` + `save_texture` | 内容读取/统计/落盘；不再 inline base64 |
| `rd_resource_usage` | `trace_resource_usage` + `search_draws(by=resource/texture)` | 使用链 + 反向查找；完整性显式标注 |
| `rd_shader` | `get_shader_info` + `get_shader_source` | `parts` 选段；不创建编辑状态 |
| `rd_shader_edit` | `get_shader_edit_context` + `replace_shader` + `revert_shader` + `list_shader_replacements` + `export_shader_source` | 一个 action 枚举；apply 带 revision |
| `rd_search` | `search_draws`（全部模式）+ 新的跨 capture | 结构化 terms/mode/fields/fuzzy；scope 决定同步还是 job |
| `rd_mesh` | `get_mesh_summary` + `get_mesh_data` + `export_mesh_csv` | summary/page/export 三模式 |
| `rd_ui_context` | 新能力 | 读 status + 有限 getter |
| `rd_ui_act` | 新能力 | navigate/show/select/view/filter/focus |
| `rd_job` | 新能力；替代 `RESULT_PENDING` 的“无处可查” | 自建 job handle，不依赖 MCP Tasks |

### 4.4 牺牲了什么

1. **逐面板一一对应没有了。** Pixel History、API Inspector 的当前行、Statistics/PerformanceCounter 的内容、Texture Viewer 的完整 viewport/range、Mesh Preview 的相机/overlay 都不承诺；代价是“完全复刻”降级为“主分析面板信息对等”。
2. **`get_draw_call_details` / `inspect_event` / `diff_events` 的独立入口没有了。** 它们变成 `rd_event` 的 `sections`/`compare_to`；schema 变大，必须用 sections + 分页控制载荷。
3. **`analyze_pass` 不再是顶层工具。** 变成 `rd_overview(marker=...)`；可发现性下降，需要在描述里写清“问 pass 整体工作负载时用 rd_overview”。
4. **`get_frame_summary` 与 `summarize_capture` 的区分消失。** 两者本来语义就不稳定（一个偏统计，一个偏建议）；合并后用 `detail` 表达。老用户可能不习惯。
5. **`rd_shader_edit(action=prepare)` 被归入 destructive 工具。** prepare 只创建编辑记录，不改 capture；但同一工具的 apply/revert 是 destructive，注解只能按最危险动作标。客户端会对 prepare 也弹确认，属于过度警告。
6. **`rd_resource_data` 不再返回 inline base64。** 这是有意的破坏性变更：脚本化调用必须改成“读文件路径”。好处是 token/内存可控；代价是调用方多一步 I/O。
7. **`list_shader_replacements` 不再独立。** 并入 `rd_shader_edit(action=list)` 或 `rd_ui_context` 的编辑摘要；可发现性下降，但超时后有明确查询入口。
8. **旧工具名全部消失。** 30 → 15 是 breaking change；需要一版 `RENDERDOC_MCP_LEGACY_TOOLS=1` 兼容别名，并更新 AGENTS/README/docs。代价是维护两套名字一个版本。
9. **`event_id_min/max` 与 `start_offset/max_vertices` 别名砍掉。** 只保留 canonical 的 `event_range` 和 `offset/limit`；现有调用方必须迁移。
10. **不提供 MCP Tasks 入口。** 先自建 `rd_job`；未来可把 `job_id` 映射到 Tasks，但不承诺。

### 4.5 关键契约

#### 4.5.1 句柄

- `instance_id`：`rd-<pid>-<8hex>`，扩展进程启动时生成，进程内稳定；不是路径哈希。
- `capture_id`：不透明字符串，包含 `instance_id` + 加载代际（UUID）+ 路径哈希；同一路径重新打开必须是新 id；capture 关闭/重载后旧 id 返回 `STALE_CAPTURE`。
- `edit_id`：shader 编辑记录 id；只在当前 `capture_id` 内有效；跨 capture 复用返回 `INVALID_EDIT_ID`。
- `job_id`：MCP server 生成的不透明 UUID；TTL 和生命周期在 `rd_job` 描述里写清；server 重启后 `JOB_NOT_FOUND`。
- `ui_seq`：扩展每次 UI 变化递增；响应携带，用来判断上下文是否已过期。

#### 4.5.2 统一 marker 语义

当前四套语义不一致（【仓库现状】）：
- `get_draw_calls` 只对 PushMarker 建匹配、exclude 命中整棵子树跳过（`serializers.py:120-129`）；
- `get_action_timings` 把 SetMarker 也追加进路径、不弹出（`action_service.py:263-278`）；
- `AnalysisService` 用全路径 lower-case 匹配（`analysis_service.py:745-753`）；
- 同一输入可能选到不同子树。

统一为：
- `PushMarker` 进入作用域，`PopMarker` 离开；
- `SetMarker` 是当前 action/region 的标签，不成为后续兄弟的祖先；
- `marker_filter` 对“由 PushMarker 组成的路径”做子串匹配；
- `exclude_markers` 命中任一祖先路径即跳过整棵子树；
- 所有工具共用同一个 builder；
- 只保留 `event_range` 一种写法；只保留 `offset/limit` 一种写法。

#### 4.5.3 输出与错误

成功：

```json
{
  "ok": true,
  "data": { "...": "..." },
  "scope": {
    "instance_id": "rd-1234-ab12cd34",
    "capture_id": "cap-...",
    "event_id": 4812,
    "ui_seq": 128,
    "capture_loaded": true
  },
  "warnings": [],
  "job": null
}
```

错误（`isError: true`，文本 JSON；不承诺 structuredContent 符合 outputSchema）：

```json
{
  "ok": false,
  "error": {
    "code": "CAPTURE_CHANGED",
    "message": "capture generation no longer matches",
    "hint": "Call rd_captures and retry with the new capture_id.",
    "retryable": false,
    "outcome_unknown": false,
    "candidates": []
  },
  "scope": { "...": "..." }
}
```

稳定错误码至少包括：`INSTANCE_NOT_FOUND`、`INSTANCE_AMBIGUOUS`、`CAPTURE_NOT_LOADED`、`CAPTURE_CHANGED`、`CAPTURE_MODIFIED`、`EVENT_NOT_FOUND`、`RESOURCE_NOT_FOUND`、`UNSUPPORTED_CAPTURE_FEATURE`、`INVALID_ARGUMENT`、`BUSY`、`TIMEOUT_OUTCOME_UNKNOWN`、`JOB_NOT_FOUND`、`JOB_CANCELLED`、`TOOL_UNAVAILABLE`、`FILE_EXISTS`。

超时语义：只有可能有副作用的工具在超时后返回 `outcome_unknown=true`；读工具返回 job 或 `retryable=true`，但也不要在原请求未完成时盲目重试。

#### 4.5.4 载荷策略

- Texture：默认返回元数据 + 统计摘要（min/max/mean/histogram 采样）+ 小 PNG 预览路径；需要原图时 `mode=file` 写 PNG/EXR/DDS，返回路径；不 inline base64。
- Buffer：默认返回长度、hash、前 256B hex；需要全量时 `mode=file` 写 `.bin`；不 inline base64。
- Shader：源码 < 50KB 直接返回文本；否则写文件 + 预览。
- Action 树：默认只返回根层 + 子节点计数；`cursor`/`limit` 展开；单次上限（例如 2000 节点）后截断并给 `next_cursor`。
- Mesh：单页最多 500 顶点；`total_count` 必须是顶点数而不是索引数（现有 `get_mesh_summary` 用 `action.numIndices` 当 `num_vertices`，`mesh_service.py:337-338`；`get_mesh_data` 用 `len(all_indices)` 当 `total_count`，`:430-441`，这是要修的 bug）。

---

## 5. architecture

### 5.1 进程与职责

```
AI Client (stdio)
   │
   ▼
MCP Server (Python 3.10+, FastMCP 3)
   ├─ 15 个静态工具 + schema/annotations
   ├─ 实例发现/路由（instances/ heartbeat）
   ├─ job registry + 结果落盘
   ├─ SQLite FTS5 索引（可选，Phase 6）
   └─ headless worker 管理（可选，独立进程）
   │  per-instance file IPC
   ▼
RenderDoc Extension (Py3.6, UI 进程)
   ├─ UI 线程：SetEventID / Show* / AddDockWindow / 有限状态读取
   ├─ replay 线程：短 BlockInvoke；长任务 AsyncInvoke 分段
   ├─ CaptureViewer：un-debounced 内存快照 → 150–250ms 合并写 status.json
   └─ session-scoped shader edit（generation + edit_id + revision）
   │  可选
   ▼
Headless Worker (独立 Python + renderdoc 模块)
   ├─ OpenCaptureFile → OpenCapture → 扫描 action/resource/shader/usage
   ├─ 跨 capture 深度索引/搜索
   └─ 需要 GPU/驱动；D3D11/12 可用 WARP fallback
```

**职责边界：**
- **MCP Server**：唯一工具面；路由；job；索引；结果裁剪；`rd_captures` 的目录列举（纯 `os.listdir`/`stat`）也在 server 侧做，不占 UI 线程；不做 RenderDoc import；不持有隐式“当前实例/capture”。
- **Extension**：只做“必须在 RenderDoc 进程内才能做”的事；UI 原语 + replay 提取；不做跨 capture 编排；不在 UI 线程做长循环。
- **Headless**：跨 capture、深扫描、索引构建；与 GUI 隔离，失败可降级。

### 5.2 线程模型

- 扩展 Python 在 UI 线程（`threading.rst:9`）；`CaptureViewer` 回调也在 UI 线程。
- UI 线程只做短操作（目标 < 1s）；`BlockInvoke` 可以用于短查询，但长扫描必须走 `AsyncInvoke` 分段或 headless。
- 所有 replay-bound 读必须 **scoped**：保存 `ctx.CurEvent()`/`ctx.CurSelectedEvent()`，结束后在 UI 线程用 `SetEventID(..., force=True)` 恢复；capture 代际变化则不恢复。当前 `search_draws` 等会遗留 `SetFrameEvent` 状态（P14）。
- 回调里不做 replay、不做大文件 I/O；只更新内存快照 + dirty flag。
- MCP server 的 sync 工具在线程池执行（FastMCP 默认），不阻塞事件循环；stdout 只给 MCP 协议，日志走 stderr/文件。
- Headless worker 是独立进程，不与 GUI replay 线程共享 GPU 上下文；同一 capture 的并发 replay 需要考虑 VRAM/驱动限制。

### 5.3 IPC v3（per-instance mailbox）

```
%TEMP%/renderdoc_mcp/
  instances/
    rd-1234-ab12cd34/
      heartbeat.json          # pid, started_at, capture_path, capture_id,
                              # api, ext_version, capabilities, busy, last_event, updated_at
      lock                    # 每实例 OS lock（串行化多个 MCP server 客户端）
      request.json            # 单槽、原子写；带 id/deadline/idempotency_key
      response_<id>.json      # 每请求文件、原子写
      status.json             # 防抖后的 UI 快照 + busy + job 进度
      jobs/<job_id>.json      # 扩展侧 job 进度（可选）
  index/                      # server 侧 SQLite（持久目录，不放 %TEMP% 更稳）
  jobs/<job_id>/              # server/headless 结果文件
```

- **原子写**：temp + `os.replace`；request/response 都是。
- **超时**：请求带 `created_at`/`deadline`；扩展看到已过期且未开始的请求，丢弃并写 `expired` 响应；已开始的请求完成后写响应，server 只保留 TTL 供诊断。
- **不再永久 IPC_BUSY**：pending 请求超过 deadline 后可被替换；替换前写一条 `expired` 响应，避免“一个超时请求挡住后续所有调用”（现状见 `client.py:103-108`）。
- **清理**：扩展启动/停止只清理自己的目录；绝不删除根目录或其他实例文件。server 在确认心跳过期后清理，保留 24h 供诊断。
- **心跳与忙碌**：心跳 1s；`busy=true` 时即使心跳旧也不判死，标记 `unresponsive`；pid 存活检测作为辅助（Windows 上用 ctypes `OpenProcess`，不依赖 psutil）。
- **能力协商**：heartbeat 里带 `capabilities`（shader_edit、panel_show、headless_available 等）；工具列表不随能力变化，能力缺失返回结构化错误。

### 5.4 多实例与路由

- 每个 qrenderdoc 进程一个扩展、一个 `instance_id`、一个 mailbox；`os.getpid()` + 随机后缀 + 启动时间。
- `rd_captures` 扫描 `instances/`，返回 `instance_id`、pid、capture path、`capture_id`、api、last_event、busy、capabilities。
- 解析规则：**显式 `instance_id` > 唯一活实例 > 报错列出候选**。不做“前台窗口/最近活跃”默认；这两者不可靠，且是隐式状态。
- `rd_capture_open`：
  - 目标实例已有 capture 时，先 `GetCaptureModifications()`（`QRDInterface.h:2559`）；有未保存修改且 `discard_unsaved=false` → `CAPTURE_MODIFIED`；
  - `ctx.LoadCapture()` 会无条件 `CloseCapture()`（`CaptureContext.cpp:921-926`），所以这是 destructive；
  - 没有活实例且 `launch_if_missing=true`：用配置的 qrenderdoc 路径 + capture 位置参数启动（`qrenderdoc.cpp:475-486`），等待 heartbeat 匹配；只管理自己启动的子进程，不杀用户启动的实例。
- `rd_ui_act(action=focus)` 用 `BringToFront()`（尽力而为，`QRDInterface.h:283-288`），返回 `focused` 的实际结果（可能失败）。
- 多个实例同时打开同一个 .rdc 是允许的；`rd_captures` 会列出多个，必须显式选。

### 5.5 长任务

- 读工具默认 `wait_ms=3000–5000`；超过则返回 `job_id`（不阻塞连接）。
- Job 状态机：`queued → running → cancel_requested → cancelled | succeeded | failed | invalidated`。
- 执行器：
  - **extension-async**：单个 `AsyncInvoke` 回调，分段处理、每 N 项写 `jobs/<id>.json` 进度、检查取消标志；适合必须在 GUI capture 里做的单 capture 扫描。代价：占用 replay 线程，`SetEventID`/导航会排队；不适合长时间交互。
  - **headless**：独立进程打开同一个 .rdc；适合跨 capture、深索引、批量 usage；不占 GUI replay；代价：GPU/VRAM、加载时间、模块部署。
- 取消是协作式：只保证不再继续，不回滚已写结果；`cancel` 后可能得到 partial result。
- capture 关闭/重载：扩展取消该 generation 的所有 job，server 标记 `invalidated`；结果已落盘的仍可读，但要带 `capture_id` 警告。
- server 重启：job registry 丢失；`rd_job` 返回 `JOB_NOT_FOUND`，提示重提；磁盘结果保留 TTL。
- 不使用 MCP Tasks 作为主路径；`job_id` 未来可映射到 Tasks 扩展。

### 5.6 搜索与索引

**浅索引（便宜，不需要 replay）：**
- 在 capture 加载时，从 UI 线程 cached 数据取：`ctx.CurRootActions()`（action/marker 树）、`ctx.GetTextures()`、`ctx.GetBuffers()`、`GetCaptureFilename()`、API。
- 写入 server 的 SQLite：captures、events、resources；FTS5 索引 name/marker_path。
- 适合“按 marker/resource/event 名模糊/OR 搜索”。

**深索引（需要 replay）：**
- headless `OpenCapture` 后逐 event 取 shader/entry point、pipeline bindings、usage；写入 shaders/usage 表。
- 首次扫描慢；按 path+size+mtime(+hash) 失效；可增量。
- 适合“按 shader 名/绑定/使用关系跨 capture 搜索”。

**FTS5 的真实能力（本机实测，SQLite 3.50.2）：**
- `bloom*` 前缀匹配 `BloomDownsample/BloomUpsample`；
- `bloom OR tonemap` 正常；
- trigram tokenizer 的 `Downs` 能匹配 `BloomDownsample`；
- 拼写错误 `Blom` 返回 `[]`——**没有内建编辑距离模糊**。需要 CamelCase/snake_case 规范化 + 前缀/trigram + 可选的 Levenshtein 重排或 spellfix1。
- 不要做成字符串 DSL；用结构化 `terms[] + mode(all/any) + fuzzy + fields + scope`。

**搜索范围：**
- `scope=current_capture`：优先浅索引；需要 shader/usage 时走深索引或 extension-async job。
- `scope=all_captures`：headless/index only；不打开 GUI capture；结果按 capture 分组，限制条数。
- “像素值搜索”不在 v1；如果未来要做，单独列为 headless 的逐 draw 回读任务，并明确成本。

### 5.7 迁移路径

1. **双写/双读期**：新 per-instance 目录与旧共享 `request.json` 并存，feature flag 选择；旧 30 工具继续可用，新增可选 `instance_id`/`capture_id`。
2. **工具面切换**：新 15 工具上线，旧工具作为 `legacy` 别名保留一个版本；annotations/outputSchema 全量补。
3. **长任务切换**：`search/resource_usage/export` 先接 job；旧的同步路径保留 fallback。
4. **headless 上线**：先只做索引构建，不接用户查询；稳定后接 `scope=all_captures`。
5. **移除 legacy**：删除共享 mailbox、旧工具名、旧别名；更新 AGENTS/README/docs/tests。

### 5.8 安全/可靠性/可观测性

- **本地边界**：文件 IPC 不是安全边界；使用 per-user `%TEMP%`，文档明确“本机同用户进程可读写”。不要把它当沙箱。
- **路径校验**：`capture_path` 必须是存在的 `.rdc`；导出路径必须绝对、拒绝覆盖；qrenderdoc 可执行路径只从配置读，不从工具参数读。
- **数据丢失**：`rd_capture_open` 检查 `GetCaptureModifications()`；默认拒绝覆盖未保存修改；`discard_unsaved=true` 才继续。
- **进程所有权**：只杀自己启动的 qrenderdoc；记录 child pid + start time；server 退出不杀用户实例。
- **可观测性**：每请求 timing、队列深度、heartbeat 年龄、job 进度、错误码；日志写 `%LOCALAPPDATA%/renderdoc_mcp/logs`，stdout 只给 MCP。
- **降级**：headless 不可用 → `rd_search(all_captures)` 返回 `TOOL_UNAVAILABLE` + 提示“先打开 capture 建浅索引”；shader 编辑不支持 → `UNSUPPORTED_CAPTURE_FEATURE`；不静默降级成错误结果。

---

## 6. roadmap

| step | title | why | risk |
|---|---|---|---|
| 1 | 验证性 spike（不改产品代码） | 本方案有 10 个 load-bearing 事实未实测：双实例、SetEventID 滚动、View* 显示、GetUsage 完整性、headless 可用性、MCP 客户端能力。先用真实 RenderDoc/GPU/测试 capture 做只读验证，成本低，能避免按错误假设重构。 | 需要真实渲染环境和测试 capture；可能发现某层目标要缩小（尤其是面板复刻、跨 capture 搜索、headless 部署）。 |
| 2 | IPC v3：per-instance mailbox + heartbeat + 显式 handle | 这是所有后续工作的地基；没有它，任何工具都可能打到错误实例，启动/停止还会删别人的请求。用 feature flag + 旧共享目录 fallback，低风险迁移。 | 双路径期竞态；心跳误判（busy vs dead）；旧客户端兼容；需要双实例实测。 |
| 3 | 工具面收敛 30→15 + annotations + outputSchema + 结构化错误 + 载荷上限 | 纯 server 侧，不碰 RenderDoc，风险最低；立即减少工具选择困难和 token 浪费，并为后续 job/搜索定好签名。 | breaking change；客户端是否消费 outputSchema/annotations 未知；schema 膨胀；需要一版 legacy 别名。 |
| 4 | UI context/act：快照 + 导航 + 面板显示 + `AddDockWindow` 修正 | 用户价值最高，改动局限在扩展；让“这个 drawcall/这张 texture”有指代，并修正第一版 `RaiseDockWindow` 的错误。 | UI 线程阻塞；面板未实例化导致不滚动；`Has*` 不等于可见；`SetEventID` no-op；需要真实 UI 测试。 |
| 5 | Job 原语 + `rd_job` + 长读工具 job 化 + scoped replay 恢复 | 没有 job，30s 超时后结果无处可查；没有 scoped restore，读工具会留下 replay cursor 副作用。先接 `search/resource_usage/export`。 | capture 切换使 job 失效；取消/部分结果语义；server 重启丢 job；extension-async 仍会占用 replay 线程。 |
| 6 | Headless worker + 浅/深索引 + `rd_search(scope=all_captures)` | 真正的“超广度搜索”必须在 GUI 外做；浅索引先解决 marker/resource 名搜索，深索引再做 shader/usage。 | `renderdoc` 模块/GPU/Python ABI 部署；加载时间和 VRAM；索引失效；与 GUI 同时 replay 的兼容性；本机 `find_spec` 为 None，必须先验证。 |
| 7 | 实例启动/切换/focus + 生命周期所有权 | 完成“自由打开/切换 RenderDoc”；依赖 2 的发现/路由和 4 的 focus。默认关闭，显式 opt-in。 | 进程管理/路径安全；用户数据丢失；多窗口焦点不可靠；server 退出时的清理策略。 |
| 8 | 移除 legacy、更新文档/测试、补观测 | 降低长期维护成本；在别名/双路径稳定一个版本后做。 | 旧客户端断裂；文档/测试滞后；需要明确的弃用窗口。 |

**不建议先做的：** 逐面板 1:1 工具（投入产出最低，且会污染工具面）；跨 capture 像素值搜索（成本高、语义不清）；MCP Tasks 作为主路径（客户端支持未知）。

---

## 7. loadBearingClaims

| # | claim | checkHow（如何独立核实） |
|---|---|---|
| 1 | `SetEventID` 能驱动 EventBrowser 选中并滚动；`CurEvent` 是 effective，`CurSelectedEvent` 是 selected；EventBrowser 不存在时不滚动 | 静态已核 `CaptureContext.cpp:1695-1748`、`EventBrowser.cpp:4115-4124,5815-5853`；实机：加载 capture，打开 EventBrowser，分别对 draw 和 marker 调 `SetEventID([], selected, event, True)`，检查 `CurEvent/CurSelectedEvent`、`QTreeView.currentIndex()`、滚动位置；再在 EventBrowser 未实例化时重复，确认 `scrolled=false`。 |
| 2 | `ViewShader/ViewBuffer/ViewTextureAsBuffer/ViewPixelHistory` 不会自动显示，`RaiseDockWindow` 对它们无效，必须 `AddDockWindow` 或 `Widget().show()` | 静态已核 `CaptureContext.cpp:2746-2812`、`QRDInterface.h:3298-3395`、`ToolWindowManager.cpp:549-569`；实机：调用 `ViewShader` 后检查 `Widget().isVisible()`，再分别调用 `RaiseDockWindow`/`AddDockWindow`，观察是否可见。 |
| 3 | `AddCaptureViewer` 在已有 capture 时同步触发三个回调；扩展 Python 在 UI 线程；`OnCaptureClosed` 在数据清理前 | 静态已核 `CaptureContext.h:135-145`、`CaptureContext.cpp:1515-1526,1570-1574`；实机：先加载 capture，再注册 viewer，记录回调顺序/线程 ID；关闭 capture 时在回调里访问 ctx，确认对象仍可用、返回后不得再用。 |
| 4 | `LoadCapture` 无条件关闭当前 capture（无保存提示），并使旧 capture 代际/资源 ID 失效 | 静态已核 `CaptureContext.cpp:921-926`；实机：打开 A 再打开 B，观察是否弹保存提示、`OnCaptureClosed` 顺序；用旧 `capture_id`/ResourceId 调工具，确认 `STALE_CAPTURE`/失败而不是误伤。 |
| 5 | `GetUsage` 是加载期预计算的 per-resource 表，查询便宜但完整性按 API 不同；D3D11 只覆盖 draw/dispatch/CmdList 绑定 | 静态已核 `resource_usage.rst:3-5,13,36`、`replay_controller.cpp:528-535`、`d3d11_context.cpp:1077-1092,1228`、`d3d12_commands.cpp:2357`；实机：用含 copy/clear/resolve 的 D3D11 capture，比较 `GetUsage` 与逐 event pipeline 扫描；再在 D3D12 上重复。 |
| 6 | 跨 capture 索引不能只靠 `OpenFile`；枚举 action/resource 需要 `OpenCapture`（replay）或解析 SD；headless 需要可用模块/GPU | 静态已核 `capture_access.rst:46`、`QRDInterface.h:2655,2670,2760`；本机 `find_spec('renderdoc') == None`；实机：对一个从未在 GUI 打开的 .rdc 做 `OpenFile`，尝试枚举 action/resource；再 `OpenCapture`，比较耗时和结果；确认 RenderDoc 安装里的 standalone 模块与 Python ABI。 |
| 7 | qrenderdoc 只暴露部分面板状态：没有全局 selected resource；Statistics/PerformanceCounter 无数据 getter；BufferViewer 只有 setter；PipelineStateViewer 无 selected-stage getter；`Has*` 不代表可见 | 静态已核 `QRDInterface.h:826,1043,1452-1550,956-1030,718-745`、`CaptureContext.h:237-265`；实机：逐项调用 getter，确认可读字段；尝试读取 BufferViewer 当前 instance/stage、PipelineStateViewer 当前 stage，确认无 API。 |
| 8 | 目标 MCP 客户端对 outputSchema/annotations/resource_link/Tasks 的支持未知；本仓库 SDK 最高协商 2025-11-25，2026-07-28 的 session 移除不一定是当前生效协议 | 静态已核 `mcp/types.py:27`、`mcp/shared/version.py:3`（本机 mcp 1.25.0）；实机：抓 Codex/Claude Code 的 `initialize` 结果和 `tools/list`/`tools/call`，确认协商版本、是否消费 structuredContent、是否显示 annotations、是否支持 Tasks/resource_link。 |
| 9 | 长 `AsyncInvoke` 扫描会占用 replay 线程，使 `SetEventID`/导航排队或卡顿；capture 关闭会使扫描失效 | 实机：在大 capture 上启动一个逐 event 扫描，同时从 UI 导航，测 `SetEventID` 延迟/进度对话框；在扫描中关闭 capture，观察异常/取消；再在 headless 进程做同样扫描比较。 |
| 10 | 多实例可以同时运行，每个扩展可独立写自己的 mailbox/heartbeat；启动/停止一个实例不应影响另一个 | 实机：启动两个 qrenderdoc，各打开不同 capture；检查两个 `instances/<id>/heartbeat.json`；向一个发长请求，同时停止另一个，确认第一个请求不受影响；杀掉一个进程，确认 server 在 TTL 后清理且不误删另一个。 |

---

## 8. 未验证/待实机确认清单

1. 仅调用 `AddDockWindow` 是否足以让从未 `show()` 的 `View*` QWidget 立即可见，还是还需 `Widget().show()`；未做实机 UI 验证。
2. EventBrowser 在新建后是否会自动选中当前 event/滚动；未验证。
3. `Has*()` 的对象是否可能“构造但未显示”；`Widget().isVisible()` 在 bundled PySide2 下是否可用；未验证。
4. 双实例的 heartbeat/请求隔离、busy vs dead 判定；未实测。
5. `GetUsage` 在 D3D11/D3D12/Vulkan/GL 上对 copy/clear/resolve/barrier 的覆盖差异；未逐 API 实测。
6. headless `renderdoc` 模块在目标 RenderDoc 安装中的 Python ABI、GPU/WARP 可用性、与 GUI 同时 replay 的限制；本机 server 环境 `find_spec` 为 None。
7. `SetEventID` 在慢 replay 下的实际延迟、进度对话框行为、取消能力；未实测。
8. shader `CompileShader` 是否能在非 UI 线程/异步 job 中运行，还是必须 UI 线程 + 嵌套事件循环；未验证。现有代码在 UI 线程调用（`shader_edit_service.py:387-389`），decompile 用 QProcess 等待 10s/60s（`:227-236`）。
9. `open_capture` 期间 `GetCaptureModifications()` 的可靠性（是否覆盖所有未保存修改）；未验证。
10. MCP 客户端对 2026-07-28 去 session 化的实际支持；本仓库 SDK 仍是 2025-11-25，不能假定最新规范已生效。
11. `isError:true` 的错误结果是否必须符合 outputSchema；规范未明确（【MCP 规范】openQuestions）。
12. 多实例“自由切换”时 `BringToFront()` 的实际成功率；官方明确不保证。
13. SQLite FTS5 在目标 Python（可能 3.6/3.13）和打包环境中的可用性；本机 3.50.2 已验证 FTS5/trigram，但未在 RenderDoc 嵌入式 Python 中验证（扩展不跑 SQLite；索引在 server/headless 侧）。

---

## 9. 一句话总结

把“三层”当路线图，不当工具分类；把“面板复刻”降级为“主分析面板语义对等 + 导航”；把“交互层”做成显式快照而不是隐式会话；把“进阶层”拆成 per-instance IPC、capture 代际、job 协议和 headless 索引四件事，按风险从低到高落地。
