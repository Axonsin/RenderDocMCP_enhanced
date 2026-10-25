# skill-support

RenderDoc 实战 Skills 的支撑目录：共用契约的单一编辑源、同步工具与触发用例集。
Skill 本体在仓库的 `.agents/skills/`（规范版本）。设计方案见
`docs/renderdoc-skills-design.md`。

## 目录

```text
shared-references/   共用契约编辑源（同步到每个 skill 的 references/）
sync_references.py   同步脚本（stdlib，无第三方依赖）
references-manifest.json  最近一次同步的哈希清单
evals/               每个 skill 的触发用例集（<name>.evals.json）
```

## 同步共用契约

`shared-references/` 下的文件会同时同步进 `.agents/skills/`（Codex）和
`.claude/skills/`（Claude Code）下每个 skill 的 `references/`，并统一记录在 manifest，
保证每个发布目录可独立安装。`--check` 同时检查两边，任意一边漂移都会失败。
**修改共用契约只改编辑源，然后运行同步**：

```bash
python skill-support/sync_references.py           # 同步并更新 manifest
python skill-support/sync_references.py --check   # 只检查漂移（有差异退出码 1）
python skill-support/sync_references.py --force   # 覆盖本地改动的目标
```

判定规则（依据上次同步的 manifest 哈希）：

- 只更新了共享源 → 目标自动刷新，**不需要** `--force`；
- 目标与源、与上次同步哈希都不一致 → 视为本地修改，报冲突跳过，`--force` 才覆盖；
- 目标缺失 → `--check` 判为漂移，同步时直接补齐；
- 源文件被删除 → 其旧目标经哈希校验后自动清理。

回归测试见 `tests/test_skill_sync.py`（`python -m unittest discover -s tests`）。

## 安装到目标工程

当前没有自动安装器（设计方案第 4 阶段内容）。手动方式：

1. 复制所需的 skill 目录（含同步后的 `references/`）到目标工程的 `.agents/skills/`
   （Codex）或 `.claude/skills/`（Claude Code）。
2. 不同客户端的加载行为与权限不假定完全相同；`agents/openai.yaml` 是 Codex 展示
   元数据，Claude Code 只读 `SKILL.md` frontmatter。

在本仓库重新生成 `.claude/skills/`（从 `.agents/skills/` 规范源，排除 Codex 元数据）：

```bash
rm -rf .claude/skills && for s in .agents/skills/*/; do \
  n=$(basename "$s"); mkdir -p ".claude/skills/$n/references"; \
  cp "$s/SKILL.md" ".claude/skills/$n/"; cp "$s"/references/*.md ".claude/skills/$n/references/"; done
```

## 当前状态

- 2026-10-24：五个 Skill 首版成稿，**静态验证通过**（结构、红线、触发用例集）。
- 尚未经实机（真实 RenderDoc 捕获 + Blender/Unity MCP）行为验证；描述未跑触发
  优化循环（依赖 claude CLI 的 run_loop，可在 Claude Code 中补跑）。
- scripts/ 按设计要求留空：只在实机验证过的确定性辅助才发布。
