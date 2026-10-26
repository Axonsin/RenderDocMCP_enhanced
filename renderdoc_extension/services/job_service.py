"""Cooperative jobs driven by the extension's UI timer (Python 3.6)."""
import copy
import hashlib
import json
import os
import tempfile
import threading
import time
import uuid


TERMINAL = {"completed", "completed_with_errors", "failed", "cancelled", "interrupted"}


def atomic_json(path, value):
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    temporary = path + "." + uuid.uuid4().hex + ".tmp"
    try:
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, allow_nan=False, indent=2)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)


class PauseJob(Exception):
    pass


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


class JobService:
    def __init__(self, ctx, session, directory=None):
        self.ctx, self.session = ctx, session
        self.directory = directory or os.path.join(tempfile.gettempdir(), "renderdoc_mcp", "jobs")
        os.makedirs(self.directory, exist_ok=True)
        self.lock = threading.RLock()
        self.records, self.runners, self.pending = {}, {}, {}
        self.active = None
        self.inflight = False
        for name in os.listdir(self.directory):
            if not name.endswith(".json"):
                continue
            try:
                with open(os.path.join(self.directory, name), encoding="utf-8") as handle:
                    record = json.load(handle)
                if "items" not in record:
                    record["items"] = None  # Historical detail files are read only on demand.
                if record["status"] not in TERMINAL:
                    record.update(status="interrupted", error="EXTENSION_RESTARTED")
                    atomic_json(os.path.join(self.directory, name), record)
                self.records[record["job_id"]] = record
            except (ValueError, KeyError, OSError):
                continue

    def _save(self, record):
        record["api_contract_version"] = 3
        if record["kind"] == "dump_draws" and record["items"] is not None:
            complete = sum(bool(i.get("complete")) for i in record["items"])
            record["counts"] = {
                "requested": record.get("requested_count"), "valid_draws": record.get("draw_count"),
                "successful": sum(bool(i.get("complete")) and i.get("ok") is True for i in record["items"]),
                "failed": sum(bool(i.get("complete")) and i.get("ok") is False for i in record["items"]),
                "skipped": record.get("skipped_count", 0),
                "pending": max(0, record.get("expected_items", 0) - complete)}
        if "item_files" not in record:
            record["item_files"] = []
            for index, item in enumerate(record["items"] or []):
                self._save_item(record, index, item)
        metadata = {k: v for k, v in record.items() if k != "items"}
        atomic_json(os.path.join(self.directory, record["job_id"] + ".json"), metadata)

    def _save_item(self, record, index, item):
        path = os.path.join(self.directory, record["job_id"], "items", "%08d.json" % index)
        atomic_json(path, item)
        files = record.setdefault("item_files", [])
        if index == len(files):
            files.append(path)
        else:
            files[index] = path

    def submit(self, kind, params, factory, job_id=None, capture_bound=True):
        job_id = str(uuid.UUID(job_id)) if job_id else str(uuid.uuid4())
        signature = hashlib.sha256(json.dumps([kind, params], sort_keys=True).encode()).hexdigest()
        with self.lock:
            if job_id in self.records:
                if self.records[job_id]["request_hash"] != signature:
                    raise ValueError("JOB_CONFLICT: job_id already has different parameters")
                return self.status(job_id, limit=1)
            record = dict(job_id=job_id, kind=kind, request_hash=signature, parameters=params,
                          status="queued", phase="queued", created_at=time.time(),
                          last_progress_at=time.time(), steps_completed=0, items=[],
                          cancel_requested=False, cancel_supported=True, texture_budget=48,
                          capture_bound=capture_bound, session=list(self.session.token()),
                          result=None, error=None, provenance=self.session.describe())
            self.records[job_id] = record
            self.runners[job_id] = iter(factory(job_id))
            self._save(record)
            return self.status(job_id, limit=1)

    def update(self, job_id, **values):
        with self.lock:
            self.records[job_id].update(values)
            if "items" in values:
                self.records[job_id]["item_files"] = []
                for index, item in enumerate(values["items"]):
                    self._save_item(self.records[job_id], index, item)
            self._save(self.records[job_id])

    def status(self, job_id, offset=0, limit=100):
        if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 500:
            raise ValueError("INVALID_PAGINATION: offset >= 0, 1 <= limit <= 500")
        with self.lock:
            if job_id not in self.records:
                raise ValueError("JOB_NOT_FOUND: %s" % job_id)
            record = self.records[job_id]
            result = copy.deepcopy({k: v for k, v in record.items() if k not in ("items", "item_files")})
            items = record["items"]
            files = record.get("item_files", [])
            if items is None:
                count, page = len(files), []
                for path in files[offset:offset + limit]:
                    with open(path, encoding="utf-8") as handle:
                        page.append(json.load(handle))
            else:
                count, page = len(items), copy.deepcopy(items[offset:offset + limit])
            if record["kind"] == "dump_draws":
                page = [item_summary(item, files[offset + i] if offset + i < len(files) else None)
                        for i, item in enumerate(page)]
            result.update(items=page, offset=offset, limit=limit,
                          total_count=count, has_more=offset + limit < count,
                          manifest_path=os.path.join(self.directory, job_id + ".json"),
                          idle_seconds=max(0, time.time() - result["last_progress_at"]))
            result["stalled"] = result["status"] == "running" and result["idle_seconds"] > 30
            return result

    def cancel(self, job_id):
        with self.lock:
            record = self.records.get(job_id)
            if record is None:
                raise ValueError("JOB_NOT_FOUND: %s" % job_id)
            if not record["cancel_supported"]:
                raise ValueError("JOB_NOT_CANCELLABLE: native operation cannot be interrupted")
            if record["status"] not in TERMINAL:
                record.update(cancel_requested=True, status="cancelling")
                self._save(record)
            return self.status(job_id, limit=1)

    def resume(self, job_id, texture_budget=48):
        if type(texture_budget) is not int or texture_budget < 1:
            raise ValueError("INVALID_REQUEST: texture_budget must be positive")
        with self.lock:
            record = self.records.get(job_id)
            if record is None:
                raise ValueError("JOB_NOT_FOUND: %s" % job_id)
            if (job_id not in self.runners or record["session"] != list(self.session.token())):
                raise ValueError("STALE_JOB: cannot resume across capture/revision or extension restart")
            if record["status"] not in ("paused", "cancelled"):
                raise ValueError("INVALID_REQUEST: only paused/cancelled jobs can resume")
            cancel_path = os.path.join(self.directory, "controls", record["job_id"] + ".cancel.json")
            if os.path.exists(cancel_path):
                os.remove(cancel_path)
            record.update(status="queued", cancel_requested=False, error=None,
                          texture_budget=texture_budget, last_progress_at=time.time())
            self._save(record)
            return self.status(job_id, limit=1)

    def busy(self):
        return self.inflight or any(r["status"] in ("queued", "running", "cancelling")
                                    for r in self.records.values())

    def _retire(self, record):
        record["items"] = None
        self.runners.pop(record["job_id"], None)
        self.pending.pop(record["job_id"], None)

    def pump(self):
        """Called on the UI thread only, after publishing the IPC response."""
        with self.lock:
            token = list(self.session.token())
            for key, record in self.records.items():
                if (record["capture_bound"] and record["session"] != token and
                        record["status"] in ("queued", "running", "paused", "cancelling", "cancelled") and
                        not (self.inflight and key == self.active)):
                    record.update(status="interrupted", error="STALE_JOB: capture or revision changed")
                    self._save(record)
                    self._retire(record)
            # Control requests are atomically published by the stdio process;
            # accepting cancellation does not depend on a responsive UI loop.
            for record in self.records.values():
                if not record["cancel_requested"] and record["status"] not in TERMINAL:
                    cancel_path = os.path.join(self.directory, "controls", record["job_id"] + ".cancel.json")
                    if os.path.exists(cancel_path):
                        record.update(cancel_requested=True, status="cancelling")
                        self._save(record)
            if self.inflight:
                return
            if self.active is None:
                self.active = next((k for k, r in self.records.items()
                                    if r["status"] in ("queued", "cancelling") and k in self.runners), None)
            if self.active is None:
                return
            key = self.active
            record = self.records[key]
            if record["capture_bound"]:
                self.session.observe_replacements(None)
            if record["capture_bound"] and record["session"] != list(self.session.token()):
                record.update(status="interrupted", error="STALE_JOB: capture or revision changed")
            elif record["cancel_requested"]:
                record["status"] = "cancelled"
            if record["status"] in TERMINAL or record["status"] == "paused":
                self._save(record)
                if record["status"] in TERMINAL and record["status"] != "cancelled":
                    self._retire(record)
                self.active = None
                return
            try:
                if key not in self.pending:
                    self.pending[key] = next(self.runners[key])
            except StopIteration:
                record["status"] = ("completed_with_errors" if any(
                    i.get("ok") is False for i in record["items"]) else "completed")
                record.update(phase="finished", cancel_supported=False, last_progress_at=time.time())
                self._save(record)
                self._retire(record)
                self.active = None
                return
            except Exception as exc:
                record.update(status="failed", error=str(exc))
                self._save(record)
                self.active = None
                return
            kind, phase, function = self.pending[key]
            record.update(status="running", phase=phase,
                          cancel_supported=kind != "ui_native", last_progress_at=time.time())
            self.inflight = True
            self._save(record)

        def run(controller=None):
            try:
                if record["capture_bound"]:
                    if record["session"] != list(self.session.token()):
                        raise RuntimeError("STALE_JOB: external shader replacement changed")
                import sys
                module = sys.modules.get(__package__ + ".replay_guard")
                guard = module.GUARDS.get(id(self.ctx)) if module else None
                if guard and controller is not None:
                    guard.thread_state.active = True
                    guard.thread_state.event = guard.state.get("event_id")
                    guard.check(controller)
                output = function(controller) or {}
                if guard and controller is not None:
                    guard.check(controller)
                if record["capture_bound"] and record["session"] != list(self.session.token()):
                    raise RuntimeError("STALE_JOB: capture or revision changed during operation")
                with self.lock:
                    if "item" in output:
                        item = output.pop("item")
                        existing = next((i for i, x in enumerate(record["items"])
                                         if x.get("item_key") == item.get("item_key")), None)
                        if existing is None:
                            record["items"].append(copy.deepcopy(item))
                            existing = len(record["items"]) - 1
                        else:
                            record["items"][existing] = copy.deepcopy(item)
                        self._save_item(record, existing, record["items"][existing])
                    record.update(output)
                    record["steps_completed"] += 1
                    record["last_progress_at"] = time.time()
                    self.pending.pop(key, None)
            except PauseJob as exc:
                with self.lock:
                    record.update(status="paused", error=str(exc))
            except Exception as exc:
                with self.lock:
                    record.update(status="interrupted" if "STALE_JOB" in str(exc) else "failed", error=str(exc))
            finally:
                if "guard" in locals() and guard and controller is not None:
                    guard.thread_state.active = False
                with self.lock:
                    self.inflight = False
                    self._save(record)

        if kind == "replay":
            try:
                import sys
                module = sys.modules.get(__package__ + ".replay_guard")
                guard = module.GUARDS.get(id(self.ctx)) if module else None
                if guard:
                    guard.preflight()
                    guard.phase("job_replay", job_id=key, job_phase=phase)
                self.ctx.Replay().AsyncInvoke(run)
            except Exception as exc:
                with self.lock:
                    self.inflight = False
                    record.update(status="failed", error=str(exc))
                    self._save(record)
        elif kind == "worker":
            worker = threading.Thread(target=run, name="RenderDocMCP-job-" + key, daemon=True)
            worker.start()
        else:
            run()

    def dispose(self):
        with self.lock:
            for record in self.records.values():
                if record["status"] not in TERMINAL:
                    record.update(status="interrupted", error="EXTENSION_UNLOADED")
                    self._save(record)
