---
name: rdoc-reconstruct-unity
description: >
  用 RenderDoc MCP 取证并还原进 Unity URP：默认按**标准静态场景重建**（几何、贴图
  与 URP 材质、相机、光照、标准 Volume 后处理）到可编译、可运行、可渲染对照的工程；
  粒子/特效系统（Particle System/VFX Graph）与渲染管线改动（Renderer Feature、
  自定义 Pass）仅在调用参数 `--effects` / `--pipeline` 显式要求时进行。Use this
  whenever the
  user wants to recreate a captured scene/object/effect inside Unity (URP) from an
  RDC capture — "把这个特效在 URP 里复刻一下", "把这一帧的场景还原成 Unity 工程" —
  including cases where they only name a single effect or object. 不适用于：与捕获
  无关的普通 Unity 功能开发、目标是 Blender 的重建（用 Blender 重建 Skill）、只想要
  管线解释（用管线分析 Skill）、性能优化建议（用性能诊断 Skill）。
argument-hint: "[对象/场景范围] [--effects] [--pipeline]"
---

# RenderDoc → Unity URP 重建

交付一个**可编译、可打开、可渲染对照**的 Unity 工程/场景（或对既有工程的改动清单），
以及与捕获的差异说明。

## 触发边界

范围由用户请求决定：单物体、某个特效、某个 Pass 的还原，或整帧场景。"复刻这个特效"
不自动升级为重建全部场景。目标工程二选一并确认：

- 新建独立工程（干净、可整体交付）；或
- 在用户指定工程内改动（遵守其版本管理边界，改动清单进 job/project）。

不适用：无 RDC 来源的 Unity 开发、Blender 交付、只想理解渲染流程。

## 调用参数

读取用户传入的参数：`$ARGUMENTS`

- 包含 `--effects`：本次允许添加粒子与特效系统（Particle System / VFX Graph、
  Compute 模拟等）；
- 包含 `--pipeline`：本次允许修改渲染管线——Renderer Feature、自定义 Pass、
  渲染器与管线资产设置；
- 其余文本视为范围描述（对象/Pass/场景名等）。

两个标志都不包含（含未传参数）：只做**标准静态场景重建**——几何、贴图与 URP 材质
（含材质级自定义 Shader）、相机、光照、标准 Volume 后处理参数。用户口头提到特效
但未带 `--effects` 时：先完成静态部分，再明确告知带参数重新触发才能继续——不要
自行推断授权。

## 工作步骤

1. **健康核对（固定第一步）**：按 `references/tool-usage.md` §2 执行。
2. **锁定范围与契约**：目标工程、Unity/URP 版本、还原对象清单、验收标准（编译通过/
   场景可开/渲染对照）、坐标系与颜色空间（Linear/Gamma）写入 `context.json`。
3. **取证**：几何、纹理（含数值域标注）、常量与绑定（材质参数推导）、观测 Shader
   反汇编（识别分支与关键字/缓冲布局）。可疑数据先按证据契约判定再使用。
4. **设计还原结构**：按 `references/reconstruction.md` §2 规划——默认只用标准 URP
   内建能力（Lit/Complex 材质、内建光照/阴影、Volume 参数）；粒子/特效系统仅在带
   `--effects`、Renderer Feature/自定义 Pass 仅在带 `--pipeline` 时纳入计划，未带
   参数时对应机制记为"未还原——需参数"。共享逻辑按功能组织，不做一次性硬编码。
5. **工程实现**：几何导入（网格、LOD、实例化）、材质与贴图导入（域处理正确）、
   材质级 Shader 编写、场景组装（层级、相机、光照、后处理设置）；
   RenderFeature/渲染器改动仅在带 `--pipeline` 参数时进行。
6. **编译与运行验证**：进编辑器编译无错 → 打开场景无缺失资源 → 按捕获视角渲染对照。
   每一步的失败先排障（可用故障诊断方法），不跳过报错继续堆功能。
7. **收尾**：差异说明（逐项：捕获行为 vs 还原行为 vs 已知差异原因）、证据清单、
   checkpoint；改动型交付给出可回滚的改动清单。

## 硬性约束

- 未带 `--effects` 不添加任何粒子/特效系统；未带 `--pipeline` 不改动渲染管线
  （Renderer Feature、自定义 Pass、渲染器与管线资产）。对应内容以"未还原——需参数"
  记入差异说明，不由代理自行推断授权。
- 还原目标是与捕获的外部表现一致；实现精度分级：有可靠 shader 源码或可读反编译
  表达时优先逐段保留计算与分支语义，证据不足或用户明确允许近似时才按观测行为拟合。
- Shader 分支按观测到的活跃路径实现；未观测分支标注为推断/未验证。
- 不把捕获中的引擎私有资产格式直接塞进工程；一切导入走 Unity 可读路径。

## 验收标准

- 工程编译通过、场景可打开、无缺失引用（编译器与控制台零错误，或逐条解释）；
- 捕获视角下的渲染对照图 + 差异说明（哪些等价、哪些近似、为什么）；
- 每个资产/材质可回溯到捕获资源与参数来源；
- 若为既有工程改动：改动清单完整、可回滚。

## 参考资料读取时机

| 文件 | 何时读 |
|---|---|
| `references/tool-usage.md` | 首次调用任何工具前 |
| `references/reconstruction.md` | 开始步骤 4 前（结构规划、材质拟合、Pass 移植方法） |
| `references/evidence-contract.md` | 记录证据、判定可疑数据、长程 checkpoint 时 |
| `references/job-layout.md` | 建工作目录、组织工程产出与报告时 |

## RenderDoc MCP 3.0

按 references/tool-usage.md 的 3.0 契约调用；优先消费完整事件常量/事件 shader 包与纹理文件产物。失效回放先取本机诊断，禁止使用占位数据；设备日志需显式授权。
