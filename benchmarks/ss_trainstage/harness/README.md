# RenderDoc 单捕获评测工具

本目录负责提交导入、文件校验、外部评分的计算、图片诊断和 Markdown 报告。它不运行被测模型、不连接设备、不修改捕获、不自动把参考答案打成 100 分，也不替代 Blender / Unity 的实际打开与渲染检查。

依赖：Python 3.10+、NumPy、Pillow、Matplotlib。宿主 Python 3.14 可运行基础指标；`harness/.venv` 的独立 Python 3.12 环境已安装 CPU Torch/Torchvision/LPIPS，锁文件为 `requirements-lock.txt`。官方权重校验见 `metric-environment.json`；同图 LPIPS=0 验证见 `oracle/evidence/lpips_identity_check.json`。普通缺依赖环境仍会明确返回 unavailable。可用 `python -m pip install -r harness/requirements.txt` 安装基础依赖。测试框架使用标准库 unittest。

## CLI

以下命令从评测根目录执行，路径可替换。每个报告输出目录必须不存在或为空，并且不能位于提交目录内部；已有文件不会覆盖。

```powershell
python harness/benchmark.py validate submissions/my-run
python harness/benchmark.py import submissions/my-run --runs-dir runs
python harness/benchmark.py assessment-template runs/my-run --out reviews/my-run/assessment.json
# 独立评审者填写 assessment.json，提供观察记录后才将 status 改为 final。
python harness/benchmark.py evaluate runs/my-run --assessment reviews/my-run/assessment.json --out reports/my-run
python harness/benchmark.py compare-images reference/render.png runs/my-run/render.png --lpips --out reports/image-metrics.json
python harness/benchmark.py aggregate reports/run-1/result.json reports/run-2/result.json reports/run-3/result.json --out reports/repeats
python -m unittest discover -s harness/tests -v
```

补充命令（从测评根目录运行）：

```powershell
python harness/create_submission.py --task blender --run-id RUN_ID --out submissions/RUN_ID
python harness/basic_report.py template submissions/basic-answers.md --run-id BASIC_RUN --out reviews/basic-assessment.json
python harness/basic_report.py evaluate submissions/basic-answers.md --assessment reviews/basic-assessment.json --out reports/basic
python harness/suite_report.py reports/run-1/result.json reports/run-2/result.json --out reports/comparison
python harness/telemetry_report.py path/to/events.jsonl --run-id RUN_ID --actor candidate --out reports/RUN_ID-tools
python harness/geometry_metrics.py reference-geometry.json submitted-geometry.json --out reports/geometry.json
python harness/pipeline_metrics.py compare oracle/source/pipeline_resource_graph.json submission/pipeline-graph.json --out reports/pipeline-metrics.json
$env:TORCH_HOME=(Join-Path (Get-Location) 'harness/cache/torch')
harness/.venv/Scripts/python.exe harness/visual_metrics.py reference.png submitted.png --regions regions.json --lpips --out reports/visual.json
```

基础题模板也包含 `submission_validity` 与 `independence` 两个独立证据门槛；不要求重开或资源完整。两项均 verified 才提供正式 `score_mean`，失败/未知时为 null，保留 `rubric_raw_mean` 诊断；无效提交标 disqualified。`template --role reference` 可标明合法裁判参考角色，访问有效性按该角色协议核验。

`suite_report` 仅在四任务齐全且所有供给尝试均已评审并具有合资格正式分数时计算等权案例均分，不以缺失任务为零，也不挑除无效尝试后平均剩余高分。`visual_metrics` 的区域清单是 `{名称: "相对于清单的二值PNG路径"}`，掩码必须与图像同尺寸、单通道、值为0/255；SSIM仅统计11×11完全位于区域内的窗口。轮廓传 `--reference-silhouette` / `--candidate-silhouette`；线性深度传无pickle的`.npy`与明确 `--depth-unit`。深度必须同相机、同定义、同单位，不能混用设备深度和世界距离。缺少参考时不生成该项。几何文件格式见 `geometry_metrics.py` 文档字符串，顶点最近距离不是表面Chamfer。

评估本身不下载模型权重。新机器需要显式运行 `harness/prepare_metric_weights.py`，从torchvision声明的官方URL预取并校验AlexNet；之后设置TORCH_HOME。虚拟环境路径迁移后需按锁文件重建。

命令成功返回 0；无效文件、路径或评分返回 2，并将结构化错误写入 stderr。一次有效评测即使未通过门槛也返回 0，是否通过读取 `decision.passed`。未评审时该字段为 null。

## 提交清单 run.json

提交目录中的 `run.json` 示例如下，内容是非官方演示值，不是实际模型结果：

```json
{
  "schema_version": 1,
  "run_id": "example-pipeline-1",
  "task": "pipeline",
  "role": "candidate",
  "outcome": "completed",
  "experiment_id": "ss-onecapture",
  "condition_id": "tools-and-prompt-v1",
  "protocol_id": "rdoc-ss-frame2925-v2",
  "repetition": 1,
  "capture_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "model": {"name": "REPLACE_WITH_ACTUAL_MODEL", "version": null},
  "started_at": "2026-10-23T10:00:00+08:00",
  "artifacts": {"report": "answer.md", "evidence": "evidence.json"},
  "log": "events.jsonl",
  "telemetry": {"wall_time_s": null, "input_tokens": null, "output_tokens": null, "tool_calls": null, "cost_usd": null}
}
```

`task` 只能是 `blender` / `unity` / `pipeline` / `optimization`。`role` 是 `candidate` 或 `reference`。同一重复实验需要相同 experiment / condition / protocol / capture hash / task / model 及版本；重复编号必须不同。未知模型版本使用 null。捕获哈希应由编排方核对，工具只能检查格式和分组一致性，无法凭哈希文本证明实际输入正确。

`outcome` 可为 completed（省略时默认）、failed、aborted、incomplete。后面三种允许缺少必需交付文件，`artifacts` 可以为空，便于真实保存失败/超时尝试；声明的文件仍必须存在且有效。非 completed 的运行无论评分多高都不会通过。评审者可以只引用独立的 `review:` 观察记录给出失败等级；它们仍必须进入重复统计分母，不能为了满足文件清单伪造工程。

必需产物：

| 任务 | artifacts 必需键 | 文件要求 |
|---|---|---|
| blender | project、render、report | `.blend`、`.png`、`.md` |
| unity | project、render、report | 项目目录（Assets 与 ProjectSettings/ProjectVersion.txt）、`.png`、`.md` |
| pipeline | report、evidence | `.md`、证据文件或目录 |
| optimization | report、evidence | `.md`、证据文件或目录 |

其他 artifact 键允许作为附加文件。路径必须是提交根目录下的 `/` 分隔相对路径；禁止绝对路径、`..`、符号链接/junction、Windows ADS。导入仅复制声明产物与日志；快照记录清单和每个文件的 SHA-256，之后内容变化会拒绝评分。`.blend` 头检查与 Unity 目录结构检查不能证明工程可用，仍需独立应用验证。

日志是可选 JSONL：首行为 `{"event":"start","timestamp":"...Z"}`，中间可记录 `tool_call`，末行为 `{"event":"finish","timestamp":"...Z","status":"completed"}`。结束状态允许 completed / failed / aborted，时间必须单调且含时区。截断、畸形或缺结束事件的日志标为 incomplete；缺失日志标为 missing，派生时间与工具次数为 null。完整日志的观察值与清单自报遥测分开显示；完整并不证明捕获了所有调用。不要把真实失败的重复从样本中移除。

## 外部评审

`assessment-template` 生成绑定提交摘要的 draft；不填分、不批准。评审者填写以下结构后改为 final：

```json
{
  "schema_version": 1,
  "run_id": "example-pipeline-1",
  "task": "pipeline",
  "run_digest": "USE_GENERATED_DIGEST",
  "status": "final",
  "reviewer": {"id": "reviewer-identity", "kind": "human"},
  "provenance": {"reviewed_at": "2026-10-23T11:00:00+08:00", "method": "逐项对照独立采集证据", "rubric_version": "rdoc-ss-frame2925-v2"},
  "scores": {
    "pass_structure": {"level": 75, "rationale": "逐项写明证据与不足", "evidence": ["submission:answer.md", "review:observations.md"]},
    "dependency": {"level": 100, "rationale": "逐项写明证据与不足", "evidence": ["review:observations.md"]},
    "meaning": {"level": 75, "rationale": "逐项写明证据与不足", "evidence": ["review:observations.md"]},
    "evidence": {"level": 75, "rationale": "逐项写明证据与不足", "evidence": ["review:observations.md"]}
  },
  "verification": {
    "submission_validity": {"status": "verified", "note": "按candidate角色和公开协议核验访问范围、提交方法及证据，无违规访问或截图平面替代", "evidence": ["review:observations.md"]},
    "independence": {"status": "verified", "note": "由编排记录确认独立初始化与隔离上下文", "evidence": ["review:observations.md"]}
  },
  "ui": null
}
```

`submission:` 相对于提交根目录；`review:` 相对于 assessment 所在目录。证据必须是存在且非空的文件；PNG 需要实际可解码。每个 `verified` / `failed` 验证项都必须提供独立 `review:` 证据与说明。四类任务都要求 `submission_validity` 和 `independence` 为 verified；Blender / Unity 还要求 `resource_completeness`、`reopened`、`rendered` 为 verified。模板按任务生成准确字段，未知字段报错，未填门槛归为 not_checked，不能通过。已归一化 result 的门槛字段必须完整，aggregate 和 suite 使用同一校验函数。

`submission_validity` 核验该运行角色和协议允许的源码、工具、上下文范围，以及是否用最终截图平面冒充三维。candidate 非授权读取裁判答案应判 failed；允许读取源码的 reference 按其授权范围判断，不因合法裁判资产使用而自动无效。`resource_completeness` 核验交付工程实际需要的纹理、材质、脚本、依赖文件可用；几何覆盖和画面质量仍由各评分维度评审。被测代理自行提供的 `accepted: true` 不参与判定。

评审身份为 `human` 或 `independent_model`；后一种还要提供 reviewer.model 与 reviewer.session_id；裁判可使用同一模型，但必须在独立会话中评审，不能复用被测会话。工具不能认证身份、判断证据语义或证明上下文隔离，必须由可信编排者/人工审计。截图/日志路径存在不等于画面正确或软件确实重新打开。reference 也使用同样流程；没有最终外部评分时没有分数。

## 评分协议

每个维度只能取整数 `0 / 25 / 50 / 75 / 100`：0 无有效完成；25 仅少量有效片段；50 部分完成且仍有主要缺陷；75 核心要求基本满足但有明确不足；100 按任务专用检查清单完整满足且证据充分。具体几何、TRS、画面对齐与性能判断由冻结的任务 rubric 定义；此工具不把主观描述自动转换成分数。

| 任务 | 维度权重 |
|---|---|
| blender | geometry 30、trs 25、visual 35、usability 10 |
| unity | geometry 20、visual 50、shader 20、usability 10 |
| pipeline | pass_structure 25、dependency 35、meaning 25、evidence 15 |
| optimization | diagnosis 35、cause 30、proposal 25、priority 10 |

原始加权分 `rubric_raw_score` = Σ(维度等级 × 权重 / 100)。只有运行完成且所有必需门槛 verified，才提供正式 `score`。通过还要求正式分 ≥80 且每个维度 ≥75。有效性 failed 标为 `disqualified`，正式 score=null；有效性/独立性/资源/重开/渲染门槛未知或失败同样没有正式分，final 结果的 passed=false，原始分只保留作诊断。报告图表、CSV 明确区分正式分与原始分；无资格的原始100不会进入 suite 的任务均值或质量/费用图。`ui` 独立 0–10，不加进总分、不改变通过条件。若评审 UI，使用 `{"score": 7, "rationale": "...", "evidence": ["review:..."]}`；未评审为 null。UI 的方向和含义应由实验协议固定，切勿把工具次数当成 UI 分数。

冻结标准为 `rdoc-ss-frame2925-v2`；v2补全上述验收门槛，未改变五档维度与权重。未发布v1存于私有oracle历史目录；尚无official model runs，不产生旧成绩兼容或重算。

## 图像与重复实验

`compare-images` 要求相同尺寸的 8 位 RGB / 不透明 RGBA PNG，不会自动裁切、配准、缩放、应用传递函数或改变背景。SSIM 用 11×11 Gaussian σ=1.5、总体协方差、valid 区域、RGB 通道均值、float64；同时输出 MAE / MSE / PSNR。完全相同图像的无限 PSNR 用 null 加说明表示。颜色空间、相机、分辨率、裁切与状态必须在外部先对齐。这些指标只是诊断，不能自动替代视觉评分。此案例的比较基线是RenderDoc导出的post-tone/LUT数值；不得对某一边额外施加显示sRGB编码。Blender显示图与Raw数值比较图须分开，实际设置见参考工程render_contract。LPIPS同样直接使用所记录的共同文件数值域，不把未验证的显示色彩校准当事实。

LPIPS 默认不请求；`--lpips` 仅在 Torch/Torchvision/LPIPS 和预训练 AlexNet、LPIPS v0.1 权重已在本地时运行 CPU 推理。依赖、权重或运行能力缺失会返回 unavailable/value:null，且不会下载权重或用随机网络冒充 LPIPS。

aggregate 要求每个条件至少 3 次独立、最终评审的 candidate 运行。同一提供组中只要有未评审或独立性未验证的运行就不出概率估计。所有已评审失败都进入分母。`p³=(成功次数/次数)³` 是 IID 假设下连续三次均成功的代入估计，**不是至少一次成功的 pass@3**。同时报告 Wilson 95% 区间及其三次方、按时间顺序非重叠三次分组的实际成功率；不足三次的尾部不充当完整三次试验。n=3 的 p³ 很不稳定，不能描述为性能保证。工具不能证明提供的运行列表没有被挑选。

报告只有 Markdown，图表与证据 PNG 使用 `assets/...` 相对引用；原始数据另存 JSON / CSV。缺数据不造图、不造排名；没有足够独立重复时显示 N/A。`tests/test_benchmark.py` 中所有材料都是明确标注的非官方合成 fixture，不能混入 runs 或正式报告。

## 结构化管线诊断

`pipeline_metrics.py` 是标准库工具，只计算集合 precision / recall / F1 和顺序倒置，不输出 rubric 分数或通过结论。输入可以是捕获的 `pipeline_resource_graph.json` v1/v2，也可以是下面的显式规范；它不从自然语言猜 Pass 名称或绑定。Pass ID 必须预先约定一致。完整字段说明也见模块文档字符串。

```json
{
  "kind": "pipeline_graph",
  "schema_version": 1,
  "scope": {"description": "NONOFFICIAL schema example", "complete": false},
  "pass_granularity": "semantic",
  "passes": [
    {"pass_id": "opaque", "action_event_ids": [20], "verification": "verified", "evidence": ["capture:20.json"]},
    {"pass_id": "composite", "action_event_ids": [30], "verification": "verified", "evidence": ["capture:30.json"]}
  ],
  "pass_sequence": ["opaque", "composite"],
  "sequence_verification": "verified",
  "sequence_evidence": ["capture:actions.json"],
  "bindings": [{
    "consumer_action_event_id": 30,
    "resource_id": "ResourceId::7",
    "stage": "fragment",
    "binding_slot": 0,
    "binding_range": {"first_mip": 0, "num_mips": 1, "first_slice": 0, "num_slices": 1},
    "verification": "verified",
    "evidence": ["capture:30.json"]
  }],
  "producer_links": null
}
```

- `passes` 检查集合与 `(pass_id, action_event_id)` 成员关系；`pass_sequence` 检查所有有序对，另列真正倒置的对。漏掉中间 Pass 不会凭空制造一条错误的相邻关系。最多 512 个 Pass；缺少序列则顺序不可用。
- 绑定默认比较 `(consumer_action_event_id, resource_id, stage, binding_slot)`；pixel/PS/FS 统一为 fragment，但不同绑定槽不能合并。另一个指标严格比较四个 range 字段；参考范围未知的条目不纳入该项，候选未知值不能作通配符。未知范围数量、排除数量、未匹配/缺失事实均保留。
- Range 仅表示所记录 API 的绑定契约，**不是实际逐片元读取的 mip / slice**。不同 API 的范围表达须由裁判核验；例如旧 API 的 cubemap `num_slices=1` 不证明只采 face 0。范围不一致是诊断，不直接处罚或转分。
- 参考只纳入 `verification=verified` 且 evidence 非空的事实；验证标记与路径是来源声明，本工具不能证明证据真实性。候选的所有结构完整声明都参加比较，不能把错误声明改成 unknown 来隐藏。参考不完整时，FP 仅意味着未匹配声明，不足以证明该声明错误。
- 缺少整个集合或设为 null 表示不可用；`[]` 表示明确声明为空。precision 的候选分母为零或 recall 的参考分母为零时分别为 null；双方都空时 F1 为 null，不给完美值。重复绑定去重并记录重复数量；缺必需 identity、负索引、bool 冒充整数、畸形 JSON 会报错。

捕获图适配器仅将 `access=shader_read` 转为绑定事实，使用原 draw 顺序形成 `action:<eid>`。此时 `pass_granularity=action`，覆盖 132 个 draw **不等于**已正确识别语义 Pass；action 与 semantic 输入之间不会计算 Pass 得分。`read_modify_write`、禁写附件和 depth-test read 不混入 shader-read 集合。当前 287 个累计版本并未提升为唯一 producer 真值。

`restricted_producers` 单独显示。显式 producer link 格式为 `{"binding": <完整绑定记录>, "producer_action_event_id": 20, "coverage": "full_binding_range", "semantics": "single_complete_overwrite", "verification": "verified", "evidence": ["独立完整覆盖证据"]}`。只有参考中范围完整、证据齐全、唯一完整覆盖且时间因果有效的条目才进入该受限诊断；partial / unknown / cumulative / 相互冲突来源均排除。候选在未验证范围之外的 producer 声明计为 unscorable，不自动当错误。捕获图 `source_version` 只表示累计状态的最新已知写入推进，因此默认 producer 诊断 unavailable。

```powershell
python harness/pipeline_metrics.py normalize oracle/source/pipeline_resource_graph.json --out reports/pipeline-reference-input.json
python harness/pipeline_metrics.py compare reports/pipeline-reference-input.json submissions/my-run/pipeline-graph.json --out reports/pipeline-diagnostic.json
python harness/pipeline_calibration.py oracle/source/pipeline_resource_graph.json --out reports/new-pipeline-calibration
python -m unittest discover -s harness/tests -p 'test_pipeline_metrics.py' -v
```

输出 JSON 包含输入文件 SHA-256，不覆盖已有文件；受控校准输出目录必须不存在。校准器生成同图控制、错误资源、漏 Pass、顺序倒置、错误范围及缺失绑定六种可追溯副本，保存 Markdown、PNG、原始 CSV / JSON，**不创建模型运行**。已实际执行并检查 PNG 的校准见 [管线校准报告](calibration/pipeline_verified/report.md)。在当前 465 个绑定中只换错一项，集合 F1 仍接近 1；因此必须同时查看具体 FP / FN，不能以总体数值掩盖关键错误。
