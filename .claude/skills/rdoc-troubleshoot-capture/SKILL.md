---
name: rdoc-troubleshoot-capture
description: >
  诊断 RenderDoc MCP 工作流的故障：捕获打不开或加载失败、查询返回空数据或占位结果、
  纹理/网格导出全零、版本或 IPC 协议不一致、回放断连或驱动失效、Shader 替换不生效、
  查询后状态污染。Use this whenever an RDC capture fails to load, MCP queries return
  empty or suspicious results (all-zero textures, empty constant trees, missing mesh
  attributes), replay health looks broken, version/protocol mismatches appear, or the
  same request keeps failing — run this BEFORE retrying the same call again. 不适用于：
  正常的分析/重建/性能任务内部步骤（仅当其数据可信度存疑或用户显式要求排障时接入）；
  与 RenderDoc 无关的通用 MCP 连接问题（先检查客户端配置）。
---

# RenderDoc 捕获与工具故障诊断

目标是把"工具行为异常"变成**有证据的分类结论**：环境问题、数据问题、还是工具缺陷，
以及哪些工作可以在不依赖可疑数据的情况下继续。

## 触发边界

适用：加载失败、查询持续失败、结果为空/全零/缺属性、健康状态异常、版本不符、
替换不生效、状态疑似污染。
不适用：

- 正常任务中的例行查询（不要每次查询都跑完整诊断——只在异常或用户要求时接入）；
- 明知是用户工程代码的问题（可以顺手指出，但不在本 Skill 内展开）。

## 工作步骤

1. **建立基线**：调用状态/健康类工具，读全响应——捕获是否加载、图形 API、回放健康
   （`replay_healthy`/`replay_error`）、扩展与 RenderDoc 版本、IPC 协议版本。
   `replay_healthy` 为 false 或字段缺失本身就是重要结论，继续第 4 步。
2. **核对版本链**：客户端 → MCP 服务器进程 → RenderDoc 扩展三方版本是否匹配；
   协议版本不一致时先升级/对齐，不要在错配版本上调参重试。
3. **构造最小失败请求**：把失败操作缩减到最小（单个工具、最小参数、无过滤器），与
   失败的原请求对比，定位是参数问题、数据问题还是传输问题。每次尝试记录请求与响应。
4. **分类**：按 `references/troubleshooting.md` 的故障树归类——环境问题（进程、
   驱动、设备、版本）、数据问题（该资源/子资源本身）、工具缺陷（疑似实现 bug）。
   每类给出证据，不凭感觉定责。
5. **恢复验证**：修复动作（重开捕获、重启进程、对齐版本）之后，**重新做健康核对 +
   一个已知应成功的最小查询**来验证恢复，而不是直接跳回复杂任务。
6. **收尾**：按证据契约记录失败与恢复过程；明确告诉用户哪些工作可以继续、哪些必须
   等待修复，以及当前回放/替换状态的恢复情况。

## 硬性约束

- **停止重试**：失败原因没有变化时不重复发同一请求；记录后转做不依赖该数据的工作。
- **不洗数据**：不把 UI 或原生脚本补取的结果记成纯 MCP 成功；不把可疑空值当真值
  传给下游任务。
- **报告状态真相**：无法恢复到起始状态时，如实报告当前回放位置与替换清单。

## 验收标准

- 给出分类结论（环境/数据/工具缺陷）与证据链，而不是"再试一次好了"。
- 保留最小复现（请求 + 响应 + 健康快照），可供工具维护者直接使用。
- 明确回答三个问题：数据还能不能用、怎么恢复的、哪些结论需要作废。

## 参考资料读取时机

| 文件 | 何时读 |
|---|---|
| `references/tool-usage.md` | 需要 schema/术语/健康字段语义时（§2、§5） |
| `references/troubleshooting.md` | 开始第 4 步分类前（故障树、已知失败模式、恢复手段） |
| `references/evidence-contract.md` | 记录失败证据与状态恢复时 |
| `references/job-layout.md` | 排障过程需要交付复现包/报告时 |

## RenderDoc MCP 3.0

按 references/tool-usage.md 的 3.0 契约调用；优先消费完整事件常量/事件 shader 包与纹理文件产物。失效回放先取本机诊断，禁止使用占位数据；设备日志需显式授权。
