# 用 skill-creator 方法论编写五个 RenderDoc 实战 Skills（静态验证版）

依据 `docs/renderdoc-skills-design.md`，按已确认的四个决策执行：五个一次写完、静态验证（不跑实机子代理）、中文正文+双语 description、首版零 scripts。全程遵守设计稿红线：正文不出现固定 EID/ResourceId/本帧答案，不固定模型品牌/推理级别/MCP 别名（写"先发现可用 MCP 工具及 schema"），不打包裁判模式，发布目录可独立安装。

## 一、目录与文件（全部新建，约 26 个文件）

```
.agents/skills/                        # 规范版本（Codex 入口）
  rdoc-analyze-pipeline/
    SKILL.md
    agents/openai.yaml
    references/pipeline-analysis.md          # 本 Skill 专属方法
  rdoc-troubleshoot-capture/  (同结构, troubleshooting.md)
  rdoc-reconstruct-blender/   (同结构, reconstruction.md)
  rdoc-reconstruct-unity/     (同结构, reconstruction.md)
  rdoc-diagnose-performance/  (同结构, performance-method.md)
  # 每个目录的 references/ 另含由 shared-references 同步进来的 4 份共用契约
skill-support/
  shared-references/                    # 单一编辑源（设计稿 §5）
    evidence-contract.md    # 证据记录（verified/inferred/unresolved、原始与推导分离）+ 异常策略 + checkpoint/缓存失效
    job-layout.md           # job/ 输出目录与报告规范（按需创建、事实/推断/实测/建议/未解决）
    tool-usage.md           # renderdoc MCP 使用契约：先健康核对、先概要后分页、大文件落盘、术语表（自包含，不依赖仓库 docs）
    benchmark-contract.md   # practice|benchmark 模式边界与公开测评约束骨架
  sync_references.py        # stdlib 极简同步：shared-references → 五个 skill 的 references/，含哈希冲突报告
  README.md                 # 目录说明、同步与安装方式（复制到目标工程 .agents/skills 或 .claude/skills）
  evals/
    rdoc-analyze-pipeline.evals.json     # 每 Skill 8-10 条触发用例（should-trigger + 近似反例，中英混合）
    ...（共 5 份，集中存放避免污染可独立安装的发布目录）
```

## 二、五个 SKILL.md 的统一骨架与差异化内容

统一骨架（中文，<500 行）：frontmatter（name + 双语 pushy description，含明确反触发）→ 触发边界与不适用场景 → 输入判断（范围由用户请求决定）→ 关键步骤（以 `get_capture_status` 健康核对为固定入口）→ 验收标准 → references 读取时机表 → mode 判断（默认 practice，仅显式锁定才 benchmark）。

| Skill | description 触发面 | 核心流程要点 |
|---|---|---|
| rdoc-analyze-pipeline | 讲清一帧流程/追踪资源/管线图 | 帧概览→action 树过滤→管线总览→阶段/绑定→纹理→资源追踪→pass 汇总；区分真实操作/自动 marker/功能 Pass；绑定者≠像素生产者；交付 Markdown+结构化图+PNG |
| rdoc-troubleshoot-capture | 打不开/全零/查询失败/版本不符 | 健康字段解读（replay_healthy/replay_error/版本协议）→最小失败请求→错误分类（环境 vs 工具）→恢复验证；通用化已知失败模式（空树≠合法空、全零深度、sRGB 域、状态污染），不含本案例 EID |
| rdoc-reconstruct-blender | 恢复进 Blender/导出模型场景 | 代表对象打通导出→导入→渲染→对照，再按家族批量；坐标/轴向/单位、实例、跨 Pass 去重、相机恢复；Blender MCP 交接与验收 |
| rdoc-reconstruct-unity | 还原进 URP/特效复刻 | 工程组织→几何→材质 Principled 拟合→观测 Shader 分支→Renderer Feature/自定义 Pass 按需→编译/重开/渲染验收与差异说明 |
| rdoc-diagnose-performance | 过绘制/带宽/贵 Pass/优化建议 | 计时可用性判断→可证伪假设树→绑定 vs 实际采样 vs 计时收益→反证检查→优先级报告；A/B 实施需授权，允许证据不足时明说 |

各 Skill 的专属 reference 展开对应方法学（工具调用次序按能力发现适配，不写死签名）。

## 三、实施步骤

1. 写 `skill-support/shared-references/` 四份共用契约（内容主要提炼自设计稿 §3/§6/§7 与本轮服务端修复确立的语义）。
2. 写 `sync_references.py`（stdlib，源→目标复制 + SHA256 清单 + 目标有本地改动时警告不覆盖）与 `skill-support/README.md`。
3. 按 pipeline → troubleshoot → blender → unity → performance 顺序写五个 SKILL.md + 专属 reference；每写完一个立即同步共用契约。
4. 补 5 份 `agents/openai.yaml`（Codex 展示元数据，字段保守通用）。
5. 静态验证（替代 skill-creator 实机子代理循环）：
   - 结构校验：frontmatter 合法、目录完整、SKILL.md <500 行、引用文件存在、同步后无漂移；
   - 红线 grep：无绝对路径/盘符/用户名、无固定 EID/ResourceId、无裁判素材字样；
   - 描述评审：按 skill-creator 的描述优化原则自查（触发+反触发覆盖、双语、pushy 程度），并产出每 Skill 的触发用例集 `evals/<name>.evals.json` 留档（供后续实机验证与 Claude Code 里的 run_loop 描述优化复用——该循环依赖 claude CLI，本轮跳过并注明）。
6. 汇总：文件清单 + 静态验证结果 + 已知限制（未经实机验证、描述未跑优化循环）。

## 四、明确不做（本轮）

- 不写 `install_project_skills.py` 安装器、不做 `.claude/skills` 生成（设计稿第 4 阶段内容，README 给出手动方式）；
- 不放 scripts/（等实机验证后按需从 harness 提炼）；
- 不跑真实 RenderDoc/Blender/Unity 行为测试、不开跑分；
- 不改 benchmarks/ 与现有服务端代码。