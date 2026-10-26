---
name: rdoc-analyze-pipeline
description: >
  通过 RenderDoc MCP 检查捕获帧的渲染管线：讲清一帧如何从几何走到最终输出、追踪任意
  资源在整帧中的读写与依赖、解释某个 Pass/Draw 的阶段与绑定，并产出可核验的管线说明与
  管线图。Use this whenever the user wants to understand how a captured frame renders,
  trace a resource's usage across the frame, explain passes/draws/bindings/shader
  stages, or produce a pipeline diagram from an RDC capture — even if they just say
  "帮我看看这一帧是怎么画的" or "这个纹理被谁用了". 不适用于：把捕获内容重建进
  Blender/Unity（用对应的重建 Skill）、性能归因与优化建议（用性能诊断 Skill）、捕获
  打不开或数据可疑的排障（用故障诊断 Skill）。
---

# RenderDoc 管线分析

从 RenderDoc 捕获（RDC）出发，产出一帧渲染过程的**可核验解释**：每个阶段做了什么、
资源在哪里被读写、最终画面由哪些 Pass 组合而成。

## 触发边界

适用：理解帧结构、追踪资源使用、解释绑定与阶段、多 Pass 组成、生成管线图。
不适用（转交给对应 Skill 或直接说明）：

- 要把内容搬进 Blender / Unity → 重建类 Skill。
- 问"哪里慢、怎么优化" → 性能诊断 Skill。
- 打不开捕获、查询报错、数据可疑 → 先走故障诊断 Skill，健康后再回来。

范围由用户的请求决定："看一下这个 Pass" 不是"分析整帧"。不要自行扩大范围。

## 工作步骤

1. **健康核对（固定第一步）**：按共用契约 `references/tool-usage.md` §2 核对捕获
   加载状态、回放健康与版本。不健康先排障（回放失效时先 `get_replay_diagnostics`
   取本机诊断，禁止用占位数据继续；设备日志需显式授权）；版本与既往分析不一致
   时，旧结论作废。
2. **确定范围**：向用户确认或从请求推断分析范围（整帧 / 某 marker 子树 / 某资源 /
   某个 Pass），写入 job 的 `context.json`（跨阶段任务时，见 `references/job-layout.md`）。
3. **帧概览**：读帧统计与 action 树（按 marker 过滤、排除纯 UI 噪声），识别真实的
   功能 Pass 边界。区分三类节点：
   - 引擎/游戏代码发起的真实 Draw/Dispatch；
   - 中间件自动插入的 marker（UI、后处理链、调试层）；
   - 功能 Pass（名称相似但语义不同，如多个同名的相机渲染）。
4. **管线细读**：对范围内关键 action 依次读管线总览 → 阶段状态 → 绑定详情 →
   输入/输出纹理。绑定接口返回的 `binding_id` 是临时令牌，只在同一 action 的响应内有效。
   常量与纹理证据优先消费文件产物（事件常量导出、纹理 auto/file 落盘结果）。
5. **资源追踪**：对用户关心的资源做整帧使用追踪与 action 级依赖追溯，注意：
   - 资源有版本/子资源概念，读写的是哪个 mip/slice 要记录；
   - 部分写入与混合依赖常见——**最近绑定该资源的 action 不一定是像素的最终生产者**；
   - 只读/读写/写后写要分开陈述。
6. **综合产出**：把发现组织成时间线与数据流说明，交叉核对反例（同一资源是否有第二
   个写入者、marker 是否掩盖了真实调用）。
7. **恢复与收尾**：长程分析按 `references/evidence-contract.md` 记录证据与 checkpoint；
   结束时确认回放位置与替换状态已恢复。

## 验收标准

- 每个结论能回溯到具体 action/绑定/追踪证据（见证据契约）。
- 管线说明覆盖：帧 → Pass → 关键 Draw 的层级，以及范围内资源的读写时间线。
- 产出的管线图（结构化数据或 PNG）节点与报告文字一一对应，不画没有证据的边。
- 明确列出推断与未解决项；"最近绑定者 = 生产者"这类常见误判不得出现。

## 参考资料读取时机

| 文件 | 何时读 |
|---|---|
| `references/tool-usage.md` | 首次调用任何工具前（健康核对、术语、读取策略） |
| `references/pipeline-analysis.md` | 开始步骤 3 前（层级分析方法、工具组合次序、图模板） |
| `references/evidence-contract.md` | 需要记录证据、遇到可疑空结果、或长程任务需要 checkpoint 时 |
| `references/job-layout.md` | 任务跨多阶段、用户要求产出目录与报告时 |

