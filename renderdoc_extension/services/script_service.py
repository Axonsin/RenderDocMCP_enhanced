"""User-supplied batch scripts executed as one cooperative replay job step (Python 3.6).

The runner contract is deliberately frozen: scripts receive a `pyrenderdoc`/`controller`
pair and a small `mcp` helper namespace, and everything that changes between tasks lives
in the script text. No ctx/Qt access is exposed; scripts run on the replay thread.
"""
import hashlib
import json
import math
import os
import sys
import time
import traceback

MAX_SCRIPT_BYTES = 512 * 1024
MAX_RESULT_BYTES = 256 * 1024
LOG_TAIL_LINES = 64
PROGRESS_INTERVAL = 0.5


class Cancelled(Exception):
    """Raised by mcp.check_cancel() after a cooperative cancel was requested."""


def _guard_for(ctx):
    module = sys.modules.get(__package__ + ".replay_guard")
    return module.GUARDS.get(id(ctx)) if module else None


def _number(value):
    """Return a JSON-safe finite number; NaN/Infinity would poison the manifest."""
    if type(value) not in (int, float):
        return None
    try:
        return value if math.isfinite(value) else None
    except OverflowError:
        return None


def _normalize_result(value):
    """Validate a script result and normalize it to plain JSON types."""
    try:
        encoded = json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ValueError("SCRIPT_RESULT_NOT_SERIALIZABLE: %s" % exc)
    if len(encoded.encode("utf-8")) > MAX_RESULT_BYTES:
        raise ValueError("SCRIPT_RESULT_TOO_LARGE: serialized result exceeds %d KiB"
                         % (MAX_RESULT_BYTES // 1024))
    return json.loads(encoded)


class _Tee(object):
    """Mirror script output to RenderDoc's console and the job's output.log."""

    def __init__(self, original, handle):
        self._original, self._handle, self._error = original, handle, None

    def write(self, text):
        try:
            self._original.write(text)
        except Exception as exc:
            self._error = self._error or str(exc)
        try:
            self._handle.write(text)
        except Exception as exc:
            self._error = self._error or str(exc)
        return len(text)

    def flush(self):
        for stream in (self._original, self._handle):
            try:
                stream.flush()
            except Exception as exc:
                self._error = self._error or str(exc)

    def isatty(self):
        return False

    def __getattr__(self, name):
        return getattr(self._original, name)


class _Runtime(object):
    """The frozen `mcp` helper namespace exposed to scripts."""

    def __init__(self, jobs, key, directory):
        self.jobs, self.key, self.directory = jobs, key, directory
        self.job_id = key
        self.cancel_path = os.path.join(jobs.directory, "controls", key + ".cancel.json")
        self.artifacts_dir = os.path.join(directory, "artifacts")
        self.output_path = os.path.join(directory, "output.log")
        self.artifacts = []
        self.log_lines = []
        self.result = None
        self.has_result = False
        self.keep_event_flag = False
        self.cancel_observed = False
        self.log_error = None
        self._last_progress = 0.0

    # ---- cancellation (works even when the UI timer is modal-starved) ----
    def cancelled(self):
        record = self.jobs.records.get(self.key) or {}
        return bool(record.get("cancel_requested")) or os.path.exists(self.cancel_path)

    def check_cancel(self):
        if self.cancelled():
            raise Cancelled("cancellation requested")
        return False

    # ---- progress and logging ----
    def progress(self, stage, current=None, total=None, note=None):
        fields = {"phase": str(stage)[:256]}
        if _number(current) is not None:
            fields["progress_current"] = _number(current)
        if _number(total) is not None:
            fields["progress_total"] = _number(total)
        if note is not None:
            fields["progress_note"] = str(note)[:512]
        fields["log_tail"] = list(self.log_lines)
        now = time.time()
        # Keep last_progress_at fresh so `stalled` stays meaningful, but do not
        # rewrite the manifest from a tight loop more than twice a second.
        if now - self._last_progress >= PROGRESS_INTERVAL:
            self._last_progress = now
            self.jobs.update(self.key, last_progress_at=now, **fields)
        return fields

    def log(self, message):
        line = "%s %s" % (time.strftime("%H:%M:%S"), str(message)[:2048])
        if len(self.log_lines) >= LOG_TAIL_LINES:
            self.log_lines.pop(0)
        self.log_lines.append(line)
        try:
            with open(os.path.join(self.directory, "script.log"), "a", encoding="utf-8") as handle:
                handle.write(line + "\n")
        except OSError as exc:
            self.log_error = str(exc)
        return line

    # ---- artifacts ----
    def artifact_path(self, name):
        if (not isinstance(name, str) or not name or name in (".", "..") or "/" in name
                or "\\" in name or ":" in name):
            raise ValueError("INVALID_REQUEST: artifact name must be a plain file name")
        os.makedirs(self.artifacts_dir, exist_ok=True)
        return os.path.join(self.artifacts_dir, name)

    def artifact(self, name, data):
        path = self.artifact_path(name)
        if isinstance(data, str):
            payload = data.encode("utf-8")
        elif isinstance(data, bytes):
            payload = data
        else:
            raise ValueError("INVALID_REQUEST: artifact data must be str or bytes")
        with open(path, "wb") as handle:
            handle.write(payload)
        entry = {"name": name, "path": path, "bytes": len(payload),
                 "sha256": hashlib.sha256(payload).hexdigest()}
        # A rewritten artifact leaves one entry describing the final file on disk.
        # normcase collapses Windows case aliases that write the same file.
        self.artifacts = [item for item in self.artifacts
                          if os.path.normcase(item["name"]) != os.path.normcase(name)]
        self.artifacts.append(entry)
        return entry

    # ---- result and event policy ----
    def set_result(self, value):
        self.result = _normalize_result(value)
        self.has_result = True
        return self.result

    def keep_event(self):
        self.keep_event_flag = True

    def summary(self):
        return {"value": self.result, "has_result": self.has_result,
                "cancelled": self.cancel_observed or self.cancelled(),
                "artifacts": list(self.artifacts), "log_tail": list(self.log_lines),
                "output_log": self.output_path if os.path.exists(self.output_path) else None,
                "log_error": self.log_error}


class ScriptService(object):
    def __init__(self, ctx, session, jobs):
        self.ctx, self.session, self.jobs = ctx, session, jobs

    def run_script(self, code, label=None, job_id=None):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("INVALID_REQUEST: code must be a non-empty string")
        try:
            encoded = code.encode("utf-8")
        except UnicodeError as exc:
            raise ValueError("INVALID_REQUEST: code must be valid UTF-8 text: %s" % exc)
        if len(encoded) > MAX_SCRIPT_BYTES:
            raise ValueError("INVALID_REQUEST: script exceeds %d KiB" % (MAX_SCRIPT_BYTES // 1024))
        if label is not None and not isinstance(label, str):
            raise ValueError("INVALID_REQUEST: label must be a string")
        try:
            compiled = compile(code, "<mcp_script>", "exec")
        except SyntaxError as exc:
            raise ValueError("SCRIPT_SYNTAX_ERROR: line %s: %s" % (exc.lineno, exc.msg))
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        digest = hashlib.sha256(encoded).hexdigest()
        # The full text stays on disk; the record keeps identity and size only.
        params = {"code_sha256": digest, "label": label, "line_count": code.count("\n") + 1,
                  "code_bytes": len(encoded)}

        def steps(key):
            directory = os.path.join(self.jobs.directory, key)
            os.makedirs(directory, exist_ok=True)
            script_path = os.path.join(directory, "script.py")
            # Byte-for-byte snapshot: text mode would translate newlines on Windows
            # and break the recorded code_sha256.
            with open(script_path, "wb") as handle:
                handle.write(encoded)
            self.jobs.update(key, script_path=script_path, script_sha256=digest)

            def execute(controller):
                return self._execute(controller, compiled, key, directory, digest)

            yield ("replay", "script", execute)

        return self.jobs.submit("run_script", params, steps, job_id, resumable=False)

    def _restore_point(self):
        guard = _guard_for(self.ctx)
        if guard is not None:
            try:
                if guard.thread_state.active:
                    return guard.thread_state.event
            except AttributeError:
                pass
        try:
            return self.ctx.CurEvent()
        except Exception:
            return 0

    def _environment(self, controller, runtime, directory):
        environment = {
            "__name__": "<mcp_script>",
            "__file__": os.path.join(directory, "script.py"),
            "pyrenderdoc": controller,
            "controller": controller,
            "mcp": runtime,
        }
        module = sys.modules.get("renderdoc")
        if module is not None:
            environment["renderdoc"] = module
            environment["rd"] = module
        return environment

    @staticmethod
    def _write_traceback(directory):
        try:
            with open(os.path.join(directory, "traceback.txt"), "w", encoding="utf-8") as handle:
                handle.write(traceback.format_exc())
        except OSError:
            pass

    def _execute(self, controller, compiled, key, directory, digest):
        runtime = _Runtime(self.jobs, key, directory)
        restore = self._restore_point()
        environment = self._environment(controller, runtime, directory)
        runtime.log("script %s started" % digest[:12])
        error = None
        with open(runtime.output_path, "a", encoding="utf-8", errors="replace") as log_handle:
            tee = _Tee(sys.stdout, log_handle)
            original = (sys.stdout, sys.stderr)
            try:
                sys.stdout, sys.stderr = tee, tee
                try:
                    exec(compiled, environment)
                    if not runtime.has_result and "RESULT" in environment:
                        runtime.set_result(environment["RESULT"])
                except Cancelled:
                    runtime.cancel_observed = True
                    runtime.log("cancellation acknowledged")
                except BaseException as exc:
                    # SystemExit/KeyboardInterrupt must not escape the native callback:
                    # job_service would keep the pending step and dispatch it again.
                    self._write_traceback(directory)
                    message = str(exc) or exc.__class__.__name__
                    if not message.startswith("SCRIPT_"):
                        label = "" if isinstance(exc, Exception) else exc.__class__.__name__ + ": "
                        message = "SCRIPT_ERROR: %s%s" % (label, message)
                    error = message
            finally:
                sys.stdout, sys.stderr = original
                tee.flush()
                if tee._error and not runtime.log_error:
                    runtime.log_error = "OUTPUT_LOG_FAILED: %s" % tee._error
                if not runtime.keep_event_flag:
                    try:
                        controller.SetFrameEvent(restore, True)
                    except Exception as exc:
                        if error is None:
                            error = "REPLAY_RESTORE_FAILED: %s" % exc
                        else:
                            runtime.log("event restore failed: %s" % exc)
        if error is not None:
            raise RuntimeError(error)
        runtime.log("script finished")
        try:
            self.jobs.update(key, log_tail=list(runtime.log_lines), last_progress_at=time.time())
        except KeyError:
            pass  # The record is gone; the step result still reaches the caller.
        return {"result": runtime.summary()}
