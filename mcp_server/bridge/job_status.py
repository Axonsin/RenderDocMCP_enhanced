"""Read atomic job snapshots without waiting for RenderDoc's UI thread."""
import json
import os
import time
import uuid


def item_summary(item, details_path):
    result = {k: item[k] for k in ("item_key", "action_event_id", "instance", "view_index",
              "complete", "ok", "error", "warnings", "serialization_complete") if k in item}
    result["details_path"] = details_path
    mesh = item.get("mesh") or {}
    result["mesh"] = {k: mesh[k] for k in ("success", "output_path", "index_path", "vertex_count",
                      "index_count", "stage", "data_quality") if k in mesh}
    textures = item.get("textures") or []
    exports = [t["export"] for t in textures if "export" in t]
    result["texture_exports"] = {"total": len(textures), "saved": sum("path" in e for e in exports),
        "failed": sum("error" in e for e in exports), "skipped": sum("skipped" in e for e in exports),
        "pending": len(textures) - len(exports)}
    result["artifact_paths"] = list(dict.fromkeys([mesh[k] for k in ("output_path", "index_path") if k in mesh] +
                                                [e["path"] for e in exports if "path" in e]))
    constants = item.get("constants", [])
    result["constant_exports"] = {"total": len(constants), "saved": sum(r.get("status") == "exported" for r in constants),
                                  "failed": sum(r.get("status") == "failed" for r in constants)}
    result["artifact_paths"].extend(p for r in constants for p in [r.get("details_path"), r.get("raw", {}).get("path")] if p)
    return result


def read_status(directory, job_id, offset=0, limit=100):
    if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 500:
        raise ValueError("INVALID_PAGINATION: offset >= 0, 1 <= limit <= 500")
    job_id = str(uuid.UUID(job_id))
    path = os.path.join(directory, job_id + ".json")
    try:
        with open(path, encoding="utf-8") as handle:
            record = json.load(handle)
    except FileNotFoundError:
        raise ValueError("JOB_NOT_FOUND: %s (submission may still be pending)" % job_id)
    if record.get("api_contract_version") != 3:
        raise ValueError("API_VERSION_MISMATCH: job snapshot requires API contract 3")
    result = {k: v for k, v in record.items() if k not in ("items", "item_files")}
    files = record.get("item_files")
    if files is None:
        count, items = len(record["items"]), record["items"][offset:offset + limit]
    else:
        count, items = len(files), []
        for item_path in files[offset:offset + limit]:
            if os.path.commonpath([os.path.abspath(directory), os.path.abspath(item_path)]) != os.path.abspath(directory):
                raise ValueError("INVALID_JOB_MANIFEST: item path outside job directory")
            with open(item_path, encoding="utf-8") as handle:
                items.append(json.load(handle))
    result.update(items=items, offset=offset, limit=limit, total_count=count,
                  has_more=offset + limit < count, manifest_path=path,
                  idle_seconds=max(0, time.time() - record["last_progress_at"]))
    if record["kind"] == "dump_draws":
        result["items"] = [item_summary(item, files[offset + i] if files else path)
                           for i,item in enumerate(items)]
    result["stalled"] = record["status"] == "running" and result["idle_seconds"] > 30
    result["status_source"] = "atomic_job_snapshot"
    cancel_path = os.path.join(directory, "controls", job_id + ".cancel.json")
    if os.path.exists(cancel_path) and record["status"] in ("queued", "running", "paused", "cancelling"):
        result.update(cancel_requested=True, status="cancelling")
    return result


def request_cancel(directory, job_id):
    snapshot = read_status(directory, job_id, limit=1)
    if snapshot["status"] in ("completed", "completed_with_errors", "failed", "cancelled", "interrupted"):
        return snapshot
    if not snapshot["cancel_supported"]:
        raise ValueError("JOB_NOT_CANCELLABLE: native operation cannot be interrupted")
    controls = os.path.join(directory, "controls")
    os.makedirs(controls, exist_ok=True)
    path = os.path.join(controls, snapshot["job_id"] + ".cancel.json")
    temporary = path + "." + uuid.uuid4().hex + ".tmp"
    try:
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump({"job_id": snapshot["job_id"], "requested_at": time.time()}, handle)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    return read_status(directory, job_id, limit=1)
