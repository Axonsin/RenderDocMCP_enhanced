---
name: rdoc-reconstruct-unity
description: >
  用 RenderDoc MCP 取证并还原进 Unity URP：把捕获中的场景、物体或特效重建为可编译、
  可运行、可渲染对照的 Unity 工程/场景，覆盖几何导入、材质 Principled 拟合、观测
  Shader 分支整理、Renderer Feature 与自定义 Pass 的按需使用。Use this whenever the
  user wants to recreate a captured scene/object/effect inside Unity (URP) from an
  RDC capture — "把这个特效在 URP 里复刻一下", "把这一帧的场景还原成 Unity 工程" —
  including cases where they only name a single effect or object. 不适用于：与捕获
  无关的普通 Unity 功能开发、目标是 Blender 的重建（用 Blender 重建 Skill）、只想要
  管线解释（用管线分析 Skill）、性能优化建议（用性能诊断 Skill）。
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

## 工作步骤

1. **健康核对（固定第一步）**：按 `references/tool-usage.md` §2 执行。
2. **锁定范围与契约**：目标工程、Unity/URP 版本、还原对象清单、验收标准（编译通过/
   场景可开/渲染对照）、坐标系与颜色空间（Linear/Gamma）写入 `context.json`。
3. **取证**：几何、纹理（含数值域标注）、常量与绑定（材质参数推导）、观测 Shader
   反汇编（识别分支与关键字/缓冲布局）。可疑数据先按证据契约判定再使用。
4. **设计还原结构**：按 `references/reconstruction.md` §2 规划——哪些走标准 URP
   功能（粒子、Decal、Volumetric），哪些需要 Renderer Feature/自定义 Pass，哪些只能
   近似拟合（列为差异）。共享逻辑按功能组织，不做一次性硬编码。
5. **工程实现**：几何导入（网格、LOD、实例化）、材质与贴图导入（域处理正确）、
   Shader/RenderFeature 编写、场景组装（层级、相机、光照、后处理设置）。
6. **编译与运行验证**：进编辑器编译无错 → 打开场景无缺失资源 → 按捕获视角渲染对照。
   每一步的失败先排障（可用故障诊断方法），不跳过报错继续堆功能。
7. **收尾**：差异说明（逐项：捕获行为 vs 还原行为 vs 已知差异原因）、证据清单、
   checkpoint；改动型交付给出可回滚的改动清单。

## 硬性约束

- 还原以"观测行为等价"为目标：外部表现对齐，不要求内部实现与原引擎一致。
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
