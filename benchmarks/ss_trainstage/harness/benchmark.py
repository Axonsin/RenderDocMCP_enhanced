"""RenderDoc benchmark: artifact validation, evidence-based scoring, and Markdown reports.

No model execution, remote access, capture modification, or automatic judging occurs here.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import math
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath

TASKS = {
    "blender": {"geometry": 30, "trs": 25, "visual": 35, "usability": 10},
    "unity": {"geometry": 20, "visual": 50, "shader": 20, "usability": 10},
    "pipeline": {"pass_structure": 25, "dependency": 35, "meaning": 25, "evidence": 15},
    "optimization": {"diagnosis": 35, "cause": 30, "proposal": 25, "priority": 10},
}
LEVELS = (0, 25, 50, 75, 100)
TELEMETRY_FIELDS = ("wall_time_s", "input_tokens", "output_tokens", "tool_calls", "cost_usd")
REQUIRED = {
    "blender": ("project", "render", "report"),
    "unity": ("project", "render", "report"),
    "pipeline": ("report", "evidence"),
    "optimization": ("report", "evidence"),
}
SNAPSHOT_NAME = ".benchmark_snapshot.json"


def required_verification(task):
    """Acceptance gates, separate from rubric levels and optional UI diagnostics."""
    return ("submission_validity", "independence") + (("resource_completeness", "reopened", "rendered") if task in ("blender", "unity") else ())


class ValidationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def read_json(path):
    try:
        with Path(path).open("r", encoding="utf-8-sig") as stream:
            result = json.load(stream)
        require(isinstance(result, dict), f"Expected JSON object: {path}")
        return result
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read JSON {path}: {exc}") from exc


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def digest_object(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def safe_path(root, relative, *, must_exist=True):
    require(isinstance(relative, str) and relative and "\x00" not in relative, "Path must be a nonempty string")
    require("\\" not in relative and ":" not in relative, f"Use portable relative paths with '/': {relative}")
    pure = PurePosixPath(relative)
    require(not pure.is_absolute() and not PureWindowsPath(relative).is_absolute() and ".." not in pure.parts, f"Unsafe path: {relative}")
    require(pure.parts and pure.as_posix() not in (".", ""), f"Unsafe path: {relative}")
    root = Path(root).resolve()
    path = root.joinpath(*pure.parts)
    current = root
    for part in pure.parts:
        current = current / part
        require(not current.is_symlink() and not (hasattr(current, "is_junction") and current.is_junction()), f"Symlink/junction forbidden: {relative}")
    try:
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise ValidationError(f"Path escapes root: {relative}") from exc
    if must_exist:
        require(path.exists(), f"Missing path: {relative}")
    return path


def timestamp(value, field):
    require(isinstance(value, str), f"{field} must be an ISO timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"Invalid {field}: {value}") from exc
    require(parsed.tzinfo is not None, f"{field} must include timezone")
    return parsed


def nonempty(value, field):
    require(isinstance(value, str) and bool(value.strip()), f"{field} must be nonempty text")
    return value


def number(value, field, *, integer=False):
    require(not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value) and value >= 0, f"{field} must be a finite nonnegative number")
    if integer:
        require(isinstance(value, int), f"{field} must be an integer")
    return value


def inspect_file(path):
    require(path.is_file(), f"Not a regular file: {path}")
    require(path.stat().st_size > 0, f"Empty artifact: {path}")
    if path.suffix.lower() == ".png":
        try:
            from PIL import Image
            with Image.open(path) as image:
                require(image.format == "PNG", f"Expected PNG content: {path}")
                image.verify()
        except ImportError as exc:
            raise ValidationError("Pillow required to validate PNG files") from exc
        except (OSError, SyntaxError) as exc:
            raise ValidationError(f"Invalid PNG {path}: {exc}") from exc
    return {"sha256": sha256_file(path), "size_bytes": path.stat().st_size}


def artifact_files(root, relative):
    path = safe_path(root, relative)
    files = {}
    if path.is_file():
        files[relative] = inspect_file(path)
    else:
        require(path.is_dir(), f"Invalid artifact: {relative}")
        for child in sorted(path.rglob("*")):
            rel = child.relative_to(root).as_posix()
            safe_path(root, rel)
            if child.is_file():
                files[rel] = inspect_file(child)
        require(files, f"Empty artifact directory: {relative}")
    return files


def inspect_log(root, relative):
    """Only complete, ordered start..finish logs produce derived telemetry."""
    result = {"status": "missing", "reason": "No log supplied", "wall_time_s": None, "tool_calls": None, "events": None}
    if relative is None:
        return result
    path = safe_path(root, relative)
    require(path.is_file(), "log must be a file")
    try:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        require(rows and all(isinstance(row, dict) for row in rows), "Empty/non-object event log")
        times = [timestamp(row.get("timestamp"), "log.timestamp") for row in rows]
        require(times == sorted(times), "Log timestamps are not monotonic")
        require(rows[0].get("event") == "start", "First log event must be start")
        require(rows[-1].get("event") == "finish", "Missing finish event")
        require(sum(row.get("event") == "start" for row in rows) == 1 and sum(row.get("event") == "finish" for row in rows) == 1, "Log contains multiple attempts")
        require(rows[-1].get("status") in ("completed", "failed", "aborted"), "finish.status must be completed/failed/aborted")
        result.update(status="complete", reason=None, events=len(rows), completion=rows[-1]["status"], wall_time_s=(times[-1] - times[0]).total_seconds(), tool_calls=sum(row.get("event") == "tool_call" for row in rows))
    except (ValueError, TypeError, OSError, UnicodeError) as exc:
        result.update(status="incomplete", reason=str(exc))
    return result


def validate_run(root):
    root = Path(root).resolve()
    manifest_path = safe_path(root, "run.json")
    run = read_json(manifest_path)
    require(run.get("schema_version") == 1, "run.schema_version must be 1")
    require(isinstance(run.get("run_id"), str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,95}", run["run_id"]), "Invalid run_id")
    require(run.get("task") in TASKS, f"task must be one of {list(TASKS)}")
    require(run.get("role") in ("candidate", "reference"), "role must be candidate/reference")
    require(run.get("outcome", "completed") in ("completed", "failed", "aborted", "incomplete"), "outcome must be completed/failed/aborted/incomplete")
    for field in ("experiment_id", "condition_id", "protocol_id"):
        nonempty(run.get(field), field)
    number(run.get("repetition"), "repetition", integer=True)
    require(run["repetition"] >= 1, "repetition must be >= 1")
    require(isinstance(run.get("capture_sha256"), str) and re.fullmatch(r"[a-fA-F0-9]{64}", run["capture_sha256"]), "capture_sha256 must contain 64 hex characters")
    require(isinstance(run.get("model"), dict), "model must be an object")
    nonempty(run["model"].get("name"), "model.name")
    # Null is appropriate for an unrecorded model version; do not invent one.
    if run["model"].get("version") is not None:
        nonempty(run["model"]["version"], "model.version")
    timestamp(run.get("started_at"), "started_at")
    require(isinstance(run.get("artifacts"), dict), "artifacts must be a mapping")
    if run.get("outcome", "completed") == "completed":
        for key in REQUIRED[run["task"]]:
            require(key in run["artifacts"], f"Missing required artifact kind: {key}")
    files = {}
    for kind, relative in run["artifacts"].items():
        nonempty(kind, "artifact kind")
        require(relative not in ("run.json", SNAPSHOT_NAME), "Reserved artifact path")
        files.update(artifact_files(root, relative))
    require("run.json" not in files and SNAPSHOT_NAME not in files, "Artifact directory includes reserved metadata")
    if "report" in run["artifacts"]:
        report = safe_path(root, run["artifacts"]["report"])
        require(report.is_file() and report.suffix.lower() == ".md", "report artifact must be a Markdown file")
    if run["task"] in ("blender", "unity"):
        if "render" in run["artifacts"]:
            render = safe_path(root, run["artifacts"]["render"])
            require(render.is_file() and render.suffix.lower() == ".png", "render artifact must be a PNG file")
        project = safe_path(root, run["artifacts"]["project"]) if "project" in run["artifacts"] else None
        if project is not None and run["task"] == "blender":
            require(project.is_file() and project.suffix.lower() == ".blend", "Blender project must be .blend")
            with project.open("rb") as stream:
                header = stream.read(7)
            # Blender also permits compressed project files. Reopenability is verified externally.
            require(header == b"BLENDER" or header.startswith(b"\x1f\x8b") or header.startswith(b"\x28\xb5\x2f\xfd"), "Unrecognized Blender file header")
        elif project is not None:
            require(project.is_dir(), "Unity project artifact must be a directory")
            require((project / "Assets").is_dir() and (project / "ProjectSettings" / "ProjectVersion.txt").is_file(), "Unity project requires Assets and ProjectSettings/ProjectVersion.txt")
    telemetry = run.get("telemetry") or {}
    require(isinstance(telemetry, dict), "telemetry must be an object or null")
    normalized_telemetry = {}
    for key in TELEMETRY_FIELDS:
        value = telemetry.get(key)
        if value is not None:
            number(value, f"telemetry.{key}", integer=key in ("input_tokens", "output_tokens", "tool_calls"))
        normalized_telemetry[key] = value
    log = inspect_log(root, run.get("log"))
    if run.get("log"):
        files.update(artifact_files(root, run["log"]))
    snapshot = {"schema_version": 1, "manifest_sha256": sha256_file(manifest_path), "files": files}
    snapshot["run_digest"] = digest_object(snapshot)
    existing = root / SNAPSHOT_NAME
    if existing.exists():
        require(read_json(existing) == snapshot, "Imported submission changed after snapshot; reimport as a new run")
    return {"run": run, "snapshot": snapshot, "telemetry": normalized_telemetry, "log": log}


def import_run(source, runs_dir):
    source, runs_dir = Path(source).resolve(), Path(runs_dir).resolve()
    checked = validate_run(source)
    destination = safe_path(runs_dir, checked["run"]["run_id"], must_exist=False)
    require(not destination.exists(), f"Run already exists: {destination}")
    require(destination != source and source not in destination.parents, "Import destination cannot be inside source")
    destination.mkdir(parents=True)
    try:
        shutil.copy2(source / "run.json", destination / "run.json")
        for relative in checked["snapshot"]["files"]:
            target = safe_path(destination, relative, must_exist=False)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(safe_path(source, relative), target)
        # Preserve empty Unity subdirectories without importing unrelated source files.
        for relative in checked["run"]["artifacts"].values():
            artifact = safe_path(source, relative)
            if artifact.is_dir():
                for directory in artifact.rglob("*"):
                    if directory.is_dir():
                        rel = directory.relative_to(source).as_posix()
                        safe_path(source, rel)
                        safe_path(destination, rel, must_exist=False).mkdir(parents=True, exist_ok=True)
        write_json(destination / SNAPSHOT_NAME, checked["snapshot"])
        validate_run(destination)
    except Exception:
        # Retain incomplete import for inspection; never erase a path on failure.
        raise
    return {"imported_to": str(destination), "run_digest": checked["snapshot"]["run_digest"]}


def evidence(refs, run_root, review_root, *, review_required=False):
    require(isinstance(refs, list) and refs, "Evidence must be a nonempty list")
    records = []
    for ref in refs:
        require(isinstance(ref, str) and ":" in ref, "Evidence must use submission:path or review:path")
        namespace, relative = ref.split(":", 1)
        require(namespace in ("submission", "review"), f"Unknown evidence namespace: {namespace}")
        path = safe_path(run_root if namespace == "submission" else review_root, relative)
        records.append({"reference": ref, **inspect_file(path)})
    if review_required:
        require(any(item["reference"].startswith("review:") for item in records), "Verified gate needs independently collected review: evidence")
    return records


def validate_verification(provided, task, run_root, review_root):
    require(isinstance(provided, dict), "verification must be an object")
    require(set(provided) <= set(required_verification(task)), "Unknown verification gate; use the task's explicit acceptance gates")
    verification = {}
    for key in required_verification(task):
        item = provided.get(key, {"status": "not_checked"})
        require(isinstance(item, dict) and item.get("status") in ("verified", "failed", "not_checked"), f"Invalid verification status: {key}")
        verification[key] = {"status": item["status"], "note": item.get("note"), "evidence": []}
        if item["status"] in ("verified", "failed"):
            verification[key]["note"] = nonempty(item.get("note"), f"verification.{key}.note")
            verification[key]["evidence"] = evidence(item.get("evidence"), run_root, review_root, review_required=True)
    return verification


def validate_assessment(value, checked, run_root, review_root):
    run = checked["run"]
    require(value.get("schema_version") == 1, "assessment.schema_version must be 1")
    require(value.get("run_id") == run["run_id"] and value.get("task") == run["task"], "Assessment run_id/task mismatch")
    require(value.get("run_digest") == checked["snapshot"]["run_digest"], "Assessment does not match this submission snapshot")
    require(value.get("status") in ("draft", "final", "unavailable"), "assessment.status must be draft/final/unavailable")
    if value["status"] != "final":
        return {"status": value["status"], "reason": value.get("reason", "External review not final"), "components": {}, "ui": None, "verification": {}}
    reviewer = value.get("reviewer", {})
    require(isinstance(reviewer, dict) and reviewer.get("kind") in ("human", "independent_model"), "Final review needs external human/independent_model reviewer")
    nonempty(reviewer.get("id"), "reviewer.id")
    if reviewer["kind"] == "independent_model":
        nonempty(reviewer.get("model"), "reviewer.model")
        # Independence concerns sessions and evidence, not model-family identity.
        # The same model may be evaluated and serve as a separately initialized judge.
        nonempty(reviewer.get("session_id"), "reviewer.session_id")
        require(reviewer["session_id"] != run.get("session_id"), "Candidate session cannot judge itself as independent")
    provenance = value.get("provenance", {})
    require(isinstance(provenance, dict), "provenance must be an object")
    timestamp(provenance.get("reviewed_at"), "provenance.reviewed_at")
    nonempty(provenance.get("method"), "provenance.method")
    nonempty(provenance.get("rubric_version"), "provenance.rubric_version")
    scores = value.get("scores")
    require(isinstance(scores, dict) and set(scores) == set(TASKS[run["task"]]), "Scores must contain exactly the task's rubric components")
    components = {}
    for key, weight in TASKS[run["task"]].items():
        item = scores[key]
        require(isinstance(item, dict), f"Invalid score entry: {key}")
        level = item.get("level")
        require(type(level) is int and level in LEVELS, f"{key}.level must be one of {LEVELS}")
        components[key] = {"level": level, "weight": weight, "rationale": nonempty(item.get("rationale"), f"{key}.rationale"), "evidence": evidence(item.get("evidence"), run_root, review_root)}
    verification = validate_verification(value.get("verification", {}), run["task"], run_root, review_root)
    ui = value.get("ui")
    if ui is not None:
        require(isinstance(ui, dict), "ui must be an object or null")
        score = ui.get("score")
        require(type(score) is int and 0 <= score <= 10, "ui.score must be integer 0..10")
        ui = {"score": score, "rationale": nonempty(ui.get("rationale"), "ui.rationale"), "evidence": evidence(ui.get("evidence"), run_root, review_root)}
    return {"status": "final", "reviewer": reviewer, "provenance": provenance, "components": components, "verification": verification, "ui": ui}


def decision(task, assessment, outcome="completed"):
    if assessment["status"] != "final":
        return {"score": None, "rubric_raw_score": None, "passed": None, "status": "unreviewed", "reasons": ["External review is not final"]}
    scores = assessment["components"]
    total = sum(scores[key]["level"] * weight / 100 for key, weight in TASKS[task].items())
    reasons = []
    if outcome != "completed":
        reasons.append(f"Attempt outcome is {outcome}")
    if total < 80:
        reasons.append("Weighted score below 80")
    if any(item["level"] < 75 for item in scores.values()):
        reasons.append("At least one component below 75")
    verification = assessment.get("verification", {})
    gates = {gate: verification.get(gate, {}).get("status", "not_checked") for gate in required_verification(task)}
    for gate, state in gates.items():
        if state != "verified":
            reasons.append(f"Independent {gate} verification {state}")
    eligible = all(state == "verified" for state in gates.values()) and outcome == "completed"
    if gates["submission_validity"] == "failed":
        status = "disqualified"
    elif any(state == "failed" for state in gates.values()):
        status = "verification_failed"
    elif any(state != "verified" for state in gates.values()):
        status = "unverified"
    elif outcome != "completed":
        status = "attempt_failed"
    else:
        status = "passed" if not reasons else "below_threshold"
    return {"score": round(total, 4) if eligible else None, "rubric_raw_score": round(total, 4), "passed": not reasons, "status": status, "reasons": reasons}


def validate_stored_assessment(run, review):
    """Shared aggregate/suite validation of trusted evaluator output structure.

    Hash shape and provenance are checked here; identity and observation truth
    still require an external review audit, as with freshly evaluated results.
    """
    require(review.get("status") in ("draft", "final", "unavailable"), "Invalid stored review status")
    if review["status"] != "final":
        return
    reviewer = review.get("reviewer", {})
    require(isinstance(reviewer, dict) and reviewer.get("kind") in ("human", "independent_model"), "Stored result needs external human/independent_model reviewer")
    nonempty(reviewer.get("id"), "stored reviewer.id")
    if reviewer["kind"] == "independent_model":
        nonempty(reviewer.get("model"), "stored reviewer.model")
        nonempty(reviewer.get("session_id"), "stored reviewer.session_id")
        require(reviewer["session_id"] != run.get("session_id"), "Candidate session cannot judge itself as independent")
    provenance = review.get("provenance", {})
    require(isinstance(provenance, dict), "Missing stored review provenance")
    timestamp(provenance.get("reviewed_at"), "stored reviewed_at")
    nonempty(provenance.get("method"), "stored review method")
    nonempty(provenance.get("rubric_version"), "stored rubric_version")
    components = review.get("components", {})
    require(isinstance(components, dict) and set(components) == set(TASKS[run["task"]]), "Invalid stored components")
    for key, item in components.items():
        require(isinstance(item, dict) and type(item.get("level")) is int and item["level"] in LEVELS and item.get("weight") == TASKS[run["task"]][key], "Invalid stored score/weight")
    verification = review.get("verification")
    require(isinstance(verification, dict) and set(verification) == set(required_verification(run["task"])), "Stored verification must contain exactly the task's acceptance gates")
    for key, gate in verification.items():
        require(isinstance(gate, dict) and gate.get("status") in ("verified", "failed", "not_checked"), "Invalid stored verification status")
        if gate["status"] in ("verified", "failed"):
            nonempty(gate.get("note"), f"stored verification.{key}.note")
            refs = gate.get("evidence")
            require(isinstance(refs, list) and any(isinstance(item, dict) and isinstance(item.get("reference"), str) and item["reference"].startswith("review:") and isinstance(item.get("sha256"), str) and re.fullmatch(r"[a-f0-9]{64}", item["sha256"]) for item in refs), "Stored verified/failed gate lacks hashed independent evidence")


def assessment_template(root):
    checked = validate_run(root)
    run = checked["run"]
    return {"schema_version": 1, "run_id": run["run_id"], "task": run["task"], "run_digest": checked["snapshot"]["run_digest"], "status": "draft", "reason": "Awaiting external review", "reviewer": {"id": "", "kind": "human"}, "provenance": {"reviewed_at": "", "method": "", "rubric_version": "rdoc-ss-frame2925-v2"}, "scores": {key: {"level": None, "rationale": "", "evidence": []} for key in TASKS[run["task"]]}, "verification": {key: {"status": "not_checked", "note": (f"Review this {run['role']} run against its allowed source/tool/context scope; unauthorized oracle access or screenshot-plane substitution invalidates candidate reconstruction" if key == "submission_validity" else None), "evidence": []} for key in required_verification(run["task"])}, "ui": None}


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def display(value):
    return "N/A" if value is None else str(value)


def prepare_report_directory(output):
    raw_output = Path(output).absolute()
    for ancestor in (raw_output, *raw_output.parents):
        require(not ancestor.is_symlink() and not (hasattr(ancestor, "is_junction") and ancestor.is_junction()), "Report output cannot traverse a symlink/junction")
    output = raw_output.resolve()
    if output.exists():
        require(output.is_dir() and not any(output.iterdir()), f"Report directory must be empty: {output}")
    else:
        output.mkdir(parents=True)
    return output


def plot_scores(result, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return {"status": "unavailable", "reason": "matplotlib is not installed"}
    components = result["assessment"]["components"]
    if not components:
        return {"status": "unavailable", "reason": "No final scores; no chart fabricated"}
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    keys = list(components)
    ax.bar(keys, [components[key]["level"] for key in keys], color="#4477aa")
    ax.axhline(75, color="#cc6677", linestyle="--", label="Component threshold: 75")
    verdict=result['decision']
    ax.set(ylim=(0, 105), ylabel="Raw reviewed rubric level (not eligibility)", title=f"{result['run']['run_id']} | {verdict['status']} | official {display(verdict['score'])} | raw {display(verdict['rubric_raw_score'])}")
    ax.set_yticks(LEVELS)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(path, dpi=160, metadata={"Software": "RenderDocBenchmark harness"})
    plt.close(fig)
    return {"status": "available", "path": "assets/scores.png"}


def write_run_report(result, output, run_root=None, review_root=None):
    requested_output = output
    output = Path(output).resolve()
    if run_root is not None:
        source = Path(run_root).resolve()
        require(output != source and source not in output.parents, "Report output cannot be inside the submission")
    output = prepare_report_directory(requested_output)
    result["chart"] = plot_scores(result, output / "assets" / "scores.png")
    # Copy PNG evidence into report assets so Markdown remains portable.
    evidence_images = []
    if run_root is not None and review_root is not None:
        seen = set()
        entries = list(result["assessment"].get("components", {}).values()) + list(result["assessment"].get("verification", {}).values())
        if result["assessment"].get("ui"):
            entries.append(result["assessment"]["ui"])
        for entry in entries:
            for item in entry.get("evidence", []):
                ref = item["reference"]
                if ref in seen:
                    continue
                seen.add(ref)
                namespace, relative = ref.split(":", 1)
                source = safe_path(run_root if namespace == "submission" else review_root, relative)
                if source.suffix.lower() == ".png":
                    name = f"evidence-{len(evidence_images)+1:02d}-{item['sha256'][:12]}.png"
                    target = output / "assets" / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
                    evidence_images.append({"reference": ref, "path": f"assets/{name}"})
    result["evidence_images"] = evidence_images
    write_json(output / "result.json", result)
    with (output / "scores.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("run_id", "task", "decision_status", "official_score", "rubric_raw_score", "component", "weight", "raw_level", "raw_weighted_contribution"))
        for key, item in result["assessment"]["components"].items():
            writer.writerow((result["run"]["run_id"], result["run"]["task"], result["decision"]["status"], result["decision"]["score"], result["decision"]["rubric_raw_score"], key, item["weight"], item["level"], item["weight"] * item["level"] / 100))
    with (output / "telemetry.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("run_id", "field", "value", "source", "status"))
        for key, value in result["telemetry"].items():
            writer.writerow((result["run"]["run_id"], key, value, "manifest", "self_reported" if value is not None else "missing"))
        for key in ("wall_time_s", "tool_calls"):
            writer.writerow((result["run"]["run_id"], key, result["log"][key], "event_log", result["log"]["status"]))
    run, assessment, verdict = result["run"], result["assessment"], result["decision"]
    lines = [f"# Run {md(run['run_id'])}", "", f"Task: **{md(run['task'])}** · Role: **{md(run['role'])}** · Model: **{md(run['model']['name'])}**", "", f"Attempt outcome: **{md(run.get('outcome', 'completed'))}**. Review status: **{assessment['status']}**. Decision: **{verdict['status']}**. Official score: **{display(verdict['score'])}**. Raw rubric diagnostic: **{display(verdict['rubric_raw_score'])}**. Pass: **{display(verdict['passed'])}**.", "", "Pass requires total >=80, every component >=75, verified submission validity and independence; reconstruction also requires verified resource completeness, reopen and render. Failed/unknown gates or an incomplete attempt suppress the official score. Raw rubric levels are diagnostic only and never enter suite quality means when ineligible. UI is separate (0–10).", "", f"Submission digest: `{result['run_digest']}`", "", "[Raw JSON](result.json) · [Scores CSV](scores.csv) · [Telemetry CSV](telemetry.csv)", ""]
    if verdict["reasons"]:
        lines += ["Reasons: " + "; ".join(md(reason) for reason in verdict["reasons"]), ""]
    if result["chart"]["status"] == "available":
        lines += ["![Component scores](assets/scores.png)", ""]
    else:
        lines += ["Chart unavailable: " + md(result["chart"]["reason"]), ""]
    lines += ["| Component | Weight | Level | Rationale |", "|---|---:|---:|---|"]
    for key, item in assessment["components"].items():
        lines.append(f"| {key} | {item['weight']}% | {item['level']} | {md(item['rationale'])} |")
    lines += ["", f"UI score: **{display(assessment.get('ui', {}).get('score') if assessment.get('ui') else None)} / 10**", "", "## Verification and provenance", ""]
    if assessment["status"] == "final":
        lines += [f"Reviewer: {md(assessment['reviewer']['id'])} ({assessment['reviewer']['kind']}). Method: {md(assessment['provenance']['method'])}. Reviewed: {md(assessment['provenance']['reviewed_at'])}.", ""]
    for key, item in assessment.get("verification", {}).items():
        lines.append(f"- {key}: **{item['status']}** — {md(item.get('note') or 'No review observation recorded')}")
    lines += ["", "The harness checks evidence paths and hashes; it cannot establish reviewer identity or the truth of an observation. External reviewers remain responsible for semantic correctness. Reference runs follow the same scoring rules and never receive an automatic 100.", "", "## Telemetry", "", "All manifest telemetry is self-reported unless independently audited. Complete-log observations are separate; log completeness does not prove exhaustive capture.", "", "| Field | Manifest value |", "|---|---:|"]
    for key, value in result["telemetry"].items():
        lines.append(f"| {key} | {display(value)} |")
    log = result["log"]
    lines += ["", f"Log status: **{log['status']}**. Log-observed wall time: {display(log['wall_time_s'])} s; tool calls: {display(log['tool_calls'])}.", "", f"Log detail: {md(log.get('reason') or log.get('completion', 'N/A'))}", "", "## PNG evidence", ""]
    for item in evidence_images:
        lines += [f"{md(item['reference'])}", "", f"![Evidence]({item['path']})", ""]
    if not evidence_images:
        lines += ["No PNG evidence supplied. This report does not imply visual or runtime verification.", ""]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")
    return result


def evaluate(root, assessment_path, output):
    checked = validate_run(root)
    assessment_path = Path(assessment_path).resolve()
    assessment = validate_assessment(read_json(assessment_path), checked, Path(root).resolve(), assessment_path.parent)
    result = {"schema_version": 1, "kind": "evaluation_result", "run": checked["run"], "run_digest": checked["snapshot"]["run_digest"], "assessment_file_sha256": sha256_file(assessment_path), "assessment": assessment, "decision": decision(checked["run"]["task"], assessment, checked["run"].get("outcome", "completed")), "telemetry": checked["telemetry"], "log": checked["log"]}
    return write_run_report(result, output, Path(root).resolve(), assessment_path.parent)


def _blur_valid(array, kernel):
    # Separable Gaussian convolution, fixed float64 accumulation, no resize/padding.
    width = len(kernel)
    horizontal = sum(kernel[i] * array[:, i:array.shape[1]-width+1+i, :] for i in range(width))
    return sum(kernel[i] * horizontal[i:array.shape[0]-width+1+i, :, :] for i in range(width))


def image_metrics(reference, candidate, *, lpips=False):
    try:
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise ValidationError("Image metrics require numpy and Pillow") from exc
    loaded = []
    metadata = []
    for path in (Path(reference), Path(candidate)):
        inspect_file(path)
        try:
            with Image.open(path) as image:
                require(image.format == "PNG", "Metrics require lossless PNG inputs")
                require(image.mode in ("RGB", "RGBA"), "Metrics require explicit 8-bit RGB/RGBA images; convert with documented settings first")
                pixels = np.asarray(image.convert("RGBA"), dtype=np.float64)
                require(np.all(pixels[:, :, 3] == 255), "Transparent pixels require a documented common background before comparison")
                loaded.append(pixels[:, :, :3] / 255.0)
                metadata.append({"path": str(path), "sha256": sha256_file(path), "dimensions": list(image.size), "mode": image.mode})
        except OSError as exc:
            raise ValidationError(f"Cannot load image {path}: {exc}") from exc
    x, y = loaded
    require(x.shape == y.shape, f"Image dimension mismatch: {x.shape} versus {y.shape}; no implicit resize")
    require(min(x.shape[:2]) >= 11, "SSIM requires each image dimension >= 11 pixels")
    coords = np.arange(-5, 6, dtype=np.float64)
    kernel = np.exp(-(coords * coords) / (2 * 1.5 ** 2))
    kernel /= kernel.sum()
    mx, my = _blur_valid(x, kernel), _blur_valid(y, kernel)
    vx = np.maximum(_blur_valid(x*x, kernel) - mx*mx, 0)
    vy = np.maximum(_blur_valid(y*y, kernel) - my*my, 0)
    covariance = _blur_valid(x*y, kernel) - mx*my
    ssim_map = ((2*mx*my + .01**2) * (2*covariance + .03**2)) / ((mx*mx + my*my + .01**2) * (vx + vy + .03**2))
    mse = float(np.mean((x-y)**2))
    result = {"schema_version": 1, "reference": metadata[0], "candidate": metadata[1], "method": "RGB stored file values / 255; Gaussian SSIM 11x11 sigma=1.5; population covariance; valid crop; channel/pixel mean; K1=.01 K2=.03; float64", "registration": "none; identical camera, crop, resolution, color management and scene state must be established externally", "ssim": {"status": "available", "value": float(np.mean(ssim_map))}, "mae": float(np.mean(np.abs(x-y))), "mse": mse, "psnr_db": None if mse == 0 else float(-10 * np.log10(mse)), "psnr_note": "identical images: infinite PSNR represented as null" if mse == 0 else None, "lpips": {"status": "not_requested", "value": None}, "scoring": "Diagnostic only; image metrics never become rubric scores automatically"}
    if lpips:
        result["lpips"] = optional_lpips(x, y)
    return result


def optional_lpips(x, y):
    # Refuse implicit network downloads. Both pretrained backbones and calibration
    # weights must already exist locally; no random-network substitute is accepted.
    absent = [name for name in ("torch", "torchvision", "lpips") if importlib.util.find_spec(name) is None]
    if absent:
        return {"status": "unavailable", "value": None, "reason": "Missing dependencies: " + ", ".join(absent)}
    try:
        import torch
        import lpips as lpips_module
        from unittest.mock import patch
        backbone = Path(torch.hub.get_dir()) / "checkpoints" / "alexnet-owt-7be5be79.pth"
        calibration = Path(lpips_module.__file__).parent / "weights" / "v0.1" / "alex.pth"
        if not backbone.is_file() or not calibration.is_file():
            return {"status": "unavailable", "value": None, "reason": "Pretrained AlexNet and LPIPS v0.1 weights are not both cached; no download attempted"}
        require(min(x.shape[:2]) >= 64, "LPIPS/AlexNet requires images >=64 pixels in each dimension")
        with patch("torch.hub.download_url_to_file", side_effect=RuntimeError("Network weight download forbidden")):
            metric = lpips_module.LPIPS(net="alex", version="0.1", model_path=str(calibration), verbose=False).cpu().eval()
            with torch.no_grad():
                tensors = [torch.from_numpy(a.transpose(2, 0, 1).copy()).float().unsqueeze(0) * 2 - 1 for a in (x, y)]
                value = float(metric(*tensors).item())
        require(math.isfinite(value), "LPIPS produced a nonfinite result")
        return {"status": "available", "value": value, "network": "alex", "version": "0.1", "device": "cpu", "backbone_sha256": sha256_file(backbone), "calibration_sha256": sha256_file(calibration)}
    except Exception as exc:
        return {"status": "unavailable", "value": None, "reason": str(exc)}


def wilson(successes, total):
    z = 1.959963984540054
    p = successes / total
    divisor = 1 + z*z/total
    center = (p + z*z/(2*total)) / divisor
    half = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total)) / divisor
    return [max(0.0, center-half), min(1.0, center+half)]


def aggregate(paths, output):
    groups = defaultdict(list)
    seen_ids = set()
    for path in paths:
        result = read_json(path)
        require(result.get("schema_version") == 1 and result.get("kind") == "evaluation_result", f"Invalid evaluation result: {path}")
        run, review = result.get("run", {}), result.get("assessment", {})
        require(run.get("task") in TASKS, f"Invalid result task: {path}")
        require(run.get("run_id") not in seen_ids, f"Duplicate run_id: {run.get('run_id')}")
        seen_ids.add(run["run_id"])
        validate_stored_assessment(run, review)
        require(run.get("outcome", "completed") in ("completed", "failed", "aborted", "incomplete"), "Invalid stored attempt outcome")
        result["decision"] = decision(run["task"], review, run.get("outcome", "completed"))  # Ignore any supplied accepted/passed field.
        key = tuple([run.get(field) for field in ("experiment_id", "condition_id", "protocol_id", "capture_sha256", "task", "role")] + [run.get("model", {}).get("name"), run.get("model", {}).get("version")])
        groups[key].append(result)
    summaries = []
    for key, results in sorted(groups.items(), key=lambda item: str(item[0])):
        ordered = sorted(results, key=lambda result: (timestamp(result["run"]["started_at"], "started_at"), result["run"]["repetition"]))
        repetitions = [result["run"]["repetition"] for result in ordered]
        require(len(set(repetitions)) == len(repetitions), "Duplicate repetition within a condition")
        digests = [result["run_digest"] for result in ordered]
        require(len(set(digests)) == len(digests), "Duplicate submission digest in repetition group")
        session_ids = [result["run"].get("session_id") for result in ordered]
        require(all(value is None or isinstance(value, str) for value in session_ids), "Candidate session_id must be text or null")
        known_session_ids = [value.strip() for value in session_ids if value and value.strip()]
        if key[5] == "candidate":
            require(len(set(known_session_ids)) == len(known_session_ids), "Duplicate candidate session_id contradicts independent repetitions")
        missing_session_ids = len(ordered) - len(known_session_ids)
        reviewed = [result for result in ordered if result["decision"]["passed"] is not None]
        independent = [result for result in reviewed if result["assessment"].get("verification", {}).get("independence", {}).get("status") == "verified"]
        complete = len(independent) == len(ordered) and len(independent) >= 3 and key[5] == "candidate"
        successes = sum(result["decision"]["passed"] for result in independent)
        p = successes / len(independent) if complete else None
        bounds = wilson(successes, len(independent)) if complete else None
        triplets = [independent[i:i+3] for i in range(0, len(independent)-2, 3)] if complete else []
        summary = {"experiment_id": key[0], "condition_id": key[1], "protocol_id": key[2], "capture_sha256": key[3], "task": key[4], "role": key[5], "model": key[6], "model_version": key[7], "submitted_runs": len(ordered), "reviewed_runs": len(reviewed), "verified_independent_runs": len(independent), "passes": successes if complete else None, "pass_probability_estimate": p, "pass_cubed_estimate": p**3 if p is not None else None, "pass_probability_wilson_95": bounds, "pass_cubed_transformed_wilson_95": [b**3 for b in bounds] if bounds else None, "nonoverlapping_triplets": len(triplets) if complete else None, "observed_triplet_success_rate": sum(all(item["decision"]["passed"] for item in block) for block in triplets) / len(triplets) if triplets else None, "unused_tail_runs": len(independent) % 3 if complete else None, "status": "estimated" if complete else "insufficient_or_unverified", "run_ids": [result["run"]["run_id"] for result in ordered]}
        summary["missing_session_id_runs"] = missing_session_ids
        summary["disqualified_runs"] = sum(result["decision"]["status"] == "disqualified" for result in ordered)
        summary["officially_scored_runs"] = sum(result["decision"]["score"] is not None for result in ordered)
        summary["independence_limitation"] = ("Missing candidate session IDs: independence depends solely on independently collected review evidence for those runs; session isolation is not established by identifiers." if missing_session_ids else "Distinct session IDs exclude known session reuse but do not establish context isolation; independent review evidence is still required.")
        summaries.append(summary)
    output = prepare_report_directory(output)
    data = {"schema_version": 1, "groups": summaries, "method": "p_hat^3 estimates three consecutive passes under independent identically distributed attempts; it is not pass@3. Requires >=3 reviewed, independently verified candidate attempts and no unreviewed/unverified member in the supplied group. Wilson interval is transformed, not an exact joint confidence guarantee. Observed triplets are chronological, nonoverlapping; leftover attempts are not counted as triplets. Selection/exhaustiveness cannot be verified by this harness."}
    write_json(output / "aggregate.json", data)
    fields = [key for key in summaries[0] if key not in ("run_ids", "pass_probability_wilson_95", "pass_cubed_transformed_wilson_95")] if summaries else ["status"]
    with (output / "aggregate.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(summaries)
    chart = None
    eligible = [item for item in summaries if item["pass_cubed_estimate"] is not None]
    if eligible:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(max(8, len(eligible)*1.8), 4.5))
            labels = [f"{item['model']}\n{item['task']}\n{item['condition_id']}" for item in eligible]
            ax.bar(labels, [item["pass_cubed_estimate"] for item in eligible], color="#4477aa")
            ax.set(ylim=(0, 1), ylabel="Estimated p³", title="Three consecutive passes (IID assumption; not a ranking)")
            fig.tight_layout()
            (output / "assets").mkdir(exist_ok=True)
            fig.savefig(output / "assets" / "pass-cubed.png", dpi=160)
            plt.close(fig)
            chart = "assets/pass-cubed.png"
        except ImportError:
            pass
    lines = ["# Repeated-run report", "", data["method"], "", "No ranking is inferred. Reference runs are not candidate performance measurements. Missing statistics remain null/N/A.", "", "[Raw JSON](aggregate.json) · [Raw CSV](aggregate.csv)", "", "| Model | Task | Condition | Submitted | Reviewed | Independent | p estimate | p³ estimate | Observed triplets | Status |", "|---|---|---|---:|---:|---:|---:|---:|---:|---|"]
    for item in summaries:
        lines.append("| " + " | ".join(md(display(item[key])) for key in ("model", "task", "condition_id", "submitted_runs", "reviewed_runs", "verified_independent_runs", "pass_probability_estimate", "pass_cubed_estimate", "observed_triplet_success_rate", "status")) + " |")
    for item in summaries:
        lines += ["", f"Session provenance ({md(item['model'])} / {md(item['task'])} / {md(item['condition_id'])}): {item['missing_session_id_runs']} missing session IDs. {item['independence_limitation']}"]
    if chart:
        lines += ["", f"![Repeated pass estimates]({chart})"]
    else:
        lines += ["", "No probability chart: no eligible groups, or matplotlib unavailable. No placeholder model data generated."]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="Validate submission and inspect telemetry")
    validate.add_argument("submission")
    importer = sub.add_parser("import", help="Copy only declared artifacts into an immutable run snapshot")
    importer.add_argument("submission")
    importer.add_argument("--runs-dir", required=True)
    template = sub.add_parser("assessment-template", help="Create an unscored draft for an external reviewer")
    template.add_argument("submission")
    template.add_argument("--out", required=True)
    score = sub.add_parser("evaluate", help="Score external review and generate Markdown/PNG/JSON/CSV")
    score.add_argument("submission")
    score.add_argument("--assessment", required=True)
    score.add_argument("--out", required=True)
    metrics = sub.add_parser("compare-images", help="Deterministic same-resolution PNG diagnostics")
    metrics.add_argument("reference")
    metrics.add_argument("candidate")
    metrics.add_argument("--lpips", action="store_true")
    metrics.add_argument("--out", required=True)
    summary = sub.add_parser("aggregate", help="Report repeated independent runs without invented rankings")
    summary.add_argument("results", nargs="+")
    summary.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_run(args.submission)
        elif args.command == "import":
            result = import_run(args.submission, args.runs_dir)
        elif args.command == "assessment-template":
            require(not Path(args.out).exists(), "Refusing to overwrite assessment")
            result = assessment_template(args.submission)
            write_json(args.out, result)
        elif args.command == "evaluate":
            result = evaluate(args.submission, args.assessment, args.out)
        elif args.command == "compare-images":
            require(not Path(args.out).exists(), "Refusing to overwrite image metrics")
            result = image_metrics(args.reference, args.candidate, lpips=args.lpips)
            write_json(args.out, result)
        else:
            result = aggregate(args.results, args.out)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ValidationError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
