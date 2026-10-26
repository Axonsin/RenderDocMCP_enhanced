---
name: rdoc-reconstruct-blender
description: >
  用 RenderDoc MCP 取证、用 Blender MCP 重建：把捕获中的人物、场景或特效恢复成可打开、
  可渲染的 .blend 文件，覆盖网格导出与导入、坐标/轴向/单位对齐、实例化与跨 Pass 去重、
  相机恢复、纹理通道与材质拟合。Use this whenever the user wants to bring meshes,
  characters, scenes, or effects from an RDC capture into Blender — even if they only
  say "把这个角色导出来" or "把这个场景恢复到 Blender里"; also use it when they ask
  for a .blend deliverable or Blender-side verification renders. 不适用于：与捕获无关
  的纯 Blender 建模/动画、只想要管线解释或性能分析、目标是 Unity 工程（用 Unity 重建
  Skill）。
---

# RenderDoc → Blender 场景重建

交付一个**能重新打开、能渲染**的 .blend，以及支撑它可信度的资产/实例证据清单。
不是导出一堆没人验证过的 OBJ。

## 触发边界

范围由用户请求决定，先确认再动手：

- "只要 Mesh" → 几何 + 姿态，不强制移植材质；
- "恢复这个角色/这个特效" → 单对象或局部效果，不升级为全场景；
- "恢复整个场景" → 全帧，但按对象家族分批交付，每批可独立验证。

不适用：无 RDC 来源的建模需求（正常 Blender 工作流）、目标是 Unity（用 Unity 重建
Skill）、需要先分析管线才知道取舍的（可先用管线分析 Skill，拿到结论再回来）。

## 工作步骤

1. **健康核对（固定第一步）**：按 `references/tool-usage.md` §2 核对捕获与回放健康；
   回放失效时先 `get_replay_diagnostics` 取本机诊断，禁止用占位数据继续（设备日志
   需显式授权）。
2. **锁定范围与契约**：和用户确认对象/Draw 范围、是否含材质、坐标系与单位偏好、
   验收视角；写入 `context.json`（见 `references/job-layout.md`）。
3. **选择代表对象**：挑一个有代表性的对象（几何不退化、材质典型、有逐实例特征），
   先打通"导出 → 导入 → 渲染 → 与捕获对照"的完整小闭环，尽早暴露坐标、索引、
   颜色域、常量错误；闭环通过后再按材质/几何家族批量扩展。
4. **取证导出**：
   - 网格：先读摘要（拓扑、顶点/索引数、属性、包围盒、实例数），再分页读数据或导出
     CSV；逐实例属性与后处理数据按需选实例；
   - 纹理：记录导出格式与数值域标注；按用途（颜色/法线/遮罩）核对通道语义；
   - 常量与材质参数：优先消费事件常量导出产物；按绑定展开常量树，记录推导出的
     PBR 参数及其 `inferred` 状态。
5. **Blender 构建**：按 `references/reconstruction.md` 处理坐标系、单位、实例、去重、
   相机与材质拟合；用 Blender MCP 建场景，几何导入优先用可复现的脚本化路径。
6. **验证与对照**：重新打开 .blend 确认无缺失资源；按捕获视角与自由视角各渲染一次，
   与捕获导出图对照（构图、剪影、颜色域、朝向）；差异写进报告。
7. **收尾**：资产/实例证据清单（来源 action、资源、实例映射）、未解决项、checkpoint。

## 硬性约束

- 全零/可疑导出先按证据契约判定，不进 Blender（黑墙就是这么来的）。
- 逐 Draw 判断、去重、材质归类由模型完成；辅助脚本只做已导出数据的验证/转换。
- 不假装"还原了"：未恢复的部分（骨骼动画、自定义引擎材质细节）如实列为未解决项。

## 验收标准

- .blend 实际重开无缺失资源、无报错；
- 代表对象在捕获视角下的渲染与捕获导出图可对照（列出已知差异）；
- 每个资产可回溯到来源资源与 action；实例映射与去重规则有记录；
- 报告区分事实/推断/实测/建议/未解决。

## 参考资料读取时机

| 文件 | 何时读 |
|---|---|
| `references/tool-usage.md` | 首次调用任何工具前（健康核对、术语、导出语义） |
| `references/reconstruction.md` | 开始步骤 3 前（坐标/实例/相机/材质方法与 Blender MCP 交接） |
| `references/evidence-contract.md` | 记录证据、判定可疑数据、长程 checkpoint 时 |
| `references/job-layout.md` | 建工作目录与报告时 |

