"""Controlled pipeline mutations. Output is calibration, never a model ranking."""
import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path
import sys

import pipeline_metrics as pm


def scenarios(reference):
    """Stable mutations selected from input order, with exact change provenance."""
    reference = pm.normalize(reference)
    if not reference["bindings"] or not reference["passes"] or len(reference["pass_sequence"] or []) < 2:
        raise pm.PipelineError("Calibration requires bindings, passes and at least two ordered passes")
    result = []
    def add(name, candidate, change):
        candidate["scope"]["description"] = "NONOFFICIAL controlled calibration: " + name
        result.append((name, candidate, change))
    add("identity_control", copy.deepcopy(reference), {"mutation": "none; agreement is a control, not model quality"})
    candidate = copy.deepcopy(reference)
    before = candidate["bindings"][0]["resource_id"]
    replacement = "calibration:nonexistent-resource"
    while replacement in {b["resource_id"] for b in reference["bindings"]}:
        replacement += "-extra"
    candidate["bindings"][0].update(resource_id=replacement, verification="unknown", evidence=[])
    add("wrong_resource", candidate, {"binding_index": 0, "resource_before": before, "resource_after": replacement})
    candidate = copy.deepcopy(reference)
    removed = candidate["passes"].pop(len(candidate["passes"]) // 2)
    candidate["pass_sequence"] = [pid for pid in candidate["pass_sequence"] if pid != removed["pass_id"]]
    add("missing_pass", candidate, {"removed_pass_id": removed["pass_id"], "note": "Bindings preserved to isolate pass structure"})
    candidate = copy.deepcopy(reference)
    before = candidate["pass_sequence"][:2]
    candidate["pass_sequence"][:2] = list(reversed(before))
    candidate.update(sequence_verification="unknown", sequence_evidence=[])
    add("reversed_order", candidate, {"before": before, "after": list(reversed(before))})
    known = next((i for i, b in enumerate(reference["bindings"]) if pm._range_known(b)), None)
    if known is not None:
        candidate = copy.deepcopy(reference)
        before = candidate["bindings"][known]["binding_range"]["first_slice"]
        candidate["bindings"][known]["binding_range"]["first_slice"] += 1
        candidate["bindings"][known].update(verification="unknown", evidence=[])
        add("wrong_range", candidate, {"binding_index": known, "first_slice_before": before, "first_slice_after": before+1})
    candidate = copy.deepcopy(reference); candidate["bindings"] = None
    add("missing_bindings", candidate, {"mutation": "bindings omitted; must be unavailable, not zero"})
    return reference, result


def run(input_path, out):
    input_path, out = Path(input_path), Path(out)
    if out.exists():
        raise pm.PipelineError("Calibration output directory must not exist")
    source_bytes = input_path.read_bytes()
    reference, variants = scenarios(pm.read_json(input_path))
    # Plotting is only for saved PNG diagnostics. The metric module is stdlib only.
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    outputs = []
    for name, candidate, change in variants:
        result = pm.compare(reference, candidate)
        outputs.append((name, candidate, change, result))
    out.mkdir(parents=True)
    pm.write_json(out / "reference.json", reference)
    rows = []
    for name, candidate, change, result in outputs:
        pm.write_json(out / f"{name}.candidate.json", candidate)
        pm.write_json(out / f"{name}.result.json", result)
        for metric, values in result["metrics"].items():
            rows.append({"scenario": name, "metric": metric, "status": values["status"],
                         **{key: values.get(key) for key in ("reference_count", "candidate_count", "true_positive", "false_positive", "false_negative", "precision", "recall", "f1")}})
    with (out / "raw.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    pm.write_json(out / "provenance.json", {"kind": "controlled_calibration_not_model_results", "source": str(input_path.resolve()),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(), "metric_script_sha256": hashlib.sha256(Path(pm.__file__).read_bytes()).hexdigest(),
        "calibration_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "scenarios": [{"name": name, "change": change} for name, _, change, _ in outputs],
        "reference_granularity": reference["pass_granularity"], "no_model_attempts": True})
    metrics = ["passes", "order", "bindings", "binding_ranges"]
    fig, axes = plt.subplots(2, 2, figsize=(12, 7), constrained_layout=True)
    names = [item[0] for item in outputs]
    for ax, metric in zip(axes.flat, metrics):
        for index, (_, _, _, result) in enumerate(outputs):
            value = result["metrics"][metric]["f1"]
            if value is None:
                ax.text(index, .045, "N/A", ha="center", fontsize=8)
            else:
                ax.bar(index, value, color="#4d6f91" if index == 0 else "#b86b47")
                ax.text(index, min(value + .025, 1.07), f"{value:.6f}", ha="center", fontsize=8)
        ax.set_title(metric); ax.set_ylabel("Set F1 (diagnostic only)")
        ax.set_ylim(0, 1.14); ax.set_xlim(-.6, len(names)-.4)
        ax.set_xticks(range(len(names)), names, rotation=30, ha="right", fontsize=8)
        ax.grid(axis="y", alpha=.2); ax.set_axisbelow(True)
    fig.suptitle("Controlled graph mutations — no model scores or rankings")
    fig.savefig(out / "calibration.png", dpi=150); plt.close(fig)
    lines = ["# 管线集合诊断的受控校准", "", "这不是模型运行、评分或排名。基于指定参考图产生可追溯的人工错误副本，检查诊断能否暴露错误；identity control 的 1 仅表示同一输入集合的一致性。", "",
             f"输入 SHA-256：`{hashlib.sha256(source_bytes).hexdigest()}`。Pass 粒度：`{reference['pass_granularity']}`；action 粒度只代表绘制覆盖和顺序，不代表语义 Pass 识别正确。", "",
             "![受控错误诊断](calibration.png)", "", "| 变体 | Pass F1 | 顺序 F1 | 绑定 F1 | 范围 F1 | 逆序对 |", "|---|---:|---:|---:|---:|---:|"]
    for name, _, _, result in outputs:
        values = result["metrics"]
        cells = ["unavailable" if values[metric]["f1"] is None else f"{values[metric]['f1']:.9f}" for metric in metrics]
        lines.append(f"| [{name}]({name}.result.json) | " + " | ".join(cells) + f" | {values['order']['inversion_count']} |")
    lines += ["", "完整 TP / FP / FN、未匹配事实和缺失事实见各结果 JSON；CSV 中空单元格表示 null。缺失 bindings 不生成零分。当前捕获图的累计写入版本不提供唯一 producer 真值，因此 restricted_producers 保持 unavailable。", "",
              "范围比较仅检查记录的 API 绑定契约是否一致，不直接处罚。不同 API 的表达、未知动态 slice 和 cubemap 须由裁判核验；例如旧 API 的 cube num_slices=1 不证明只采 face 0。本工具不把范围集合 F1 转成分数。", "",
              "[CSV 原始指标](raw.csv) · [变更及输入溯源](provenance.json) · [规范化参考输入](reference.json)", ""]
    (out / "report.md").write_text("\n".join(lines), encoding="utf-8")
    return {"output": str(out.resolve()), "scenarios": len(outputs)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run(args.reference, args.out), ensure_ascii=False))
        return 0
    except (pm.PipelineError, OSError, ImportError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
