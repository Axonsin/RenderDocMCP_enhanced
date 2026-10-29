"""run_script job runner: cooperative execution, cancellation, evidence on disk."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import threading
from types import SimpleNamespace as NS

import pytest


ROOT = Path(__file__).resolve().parents[1]
# pytest does not add the repository root to sys.path for rootdir-relative collection.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def standalone(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


JOBS = standalone("job_service_script", "renderdoc_extension/services/job_service.py")
SCRIPTS = standalone("script_service_t", "renderdoc_extension/services/script_service.py")
HANDLER = standalone("request_handler_script", "renderdoc_extension/request_handler.py")


class Session:
    def __init__(self):
        self.generation, self.revision = "capture", 0

    def token(self):
        return self.generation, self.revision

    def observe_replacements(self, controller):
        pass

    def describe(self):
        return dict(capture_session=self.generation, replay_revision=self.revision)


class Control(object):
    """Fake ReplayController recording SetFrameEvent calls."""

    def __init__(self, events=None):
        self.events = events if events is not None else []

    def SetFrameEvent(self, event, force):
        self.events.append((event, force))


@pytest.fixture
def env(tmp_path):
    callbacks = []
    session = Session()
    # One context for both services, as in the extension: guard lookups key on id(ctx).
    ctx = NS(IsCaptureLoaded=lambda: True, CurEvent=lambda: 77,
             Replay=lambda: NS(AsyncInvoke=callbacks.append))
    jobs = JOBS.JobService(ctx, session, str(tmp_path))
    return SCRIPTS.ScriptService(ctx, session, jobs), jobs, callbacks, session


def tick(jobs, callbacks, controller=None):
    jobs.pump()
    if callbacks:
        callbacks.pop(0)(controller or Control())


def finish(jobs, callbacks, controller=None):
    tick(jobs, callbacks, controller)
    tick(jobs, callbacks, controller)


def test_result_record_metadata_and_script_snapshot(env):
    service, jobs, callbacks, _ = env
    code = "mcp.set_result({'draws': 3})\n"
    status = service.run_script(code, label="smoke")
    key = status["job_id"]
    assert status["status"] == "queued"
    finish(jobs, callbacks)
    final = jobs.status(key)
    assert final["status"] == "completed"
    assert final["result"]["value"] == {"draws": 3}
    assert final["result"]["has_result"] is True
    assert final["parameters"]["code_sha256"] == hashlib.sha256(code.encode("utf-8")).hexdigest()
    assert final["parameters"]["label"] == "smoke"
    assert final["parameters"]["line_count"] == 2
    # The script body is evidence on disk; the job record keeps identity only.
    assert "mcp.set_result" not in json.dumps(final["parameters"])
    assert Path(final["script_path"]).read_bytes() == code.encode("utf-8")
    assert hashlib.sha256(Path(final["script_path"]).read_bytes()).hexdigest() == \
        final["parameters"]["code_sha256"]


def test_result_variable_fallback_and_stdout_capture(env, capsys):
    service, jobs, callbacks, _ = env
    status = service.run_script("print('hello from script')\nRESULT = {'value': 1}\n")
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert final["status"] == "completed"
    assert final["result"]["value"] == {"value": 1}
    log = Path(final["result"]["output_log"]).read_text(encoding="utf-8")
    assert "hello from script" in log
    assert any("script" in line for line in final["result"]["log_tail"])
    assert "hello from script" in capsys.readouterr().out


def test_script_exception_reports_script_error_and_traceback(env):
    service, jobs, callbacks, _ = env
    status = service.run_script("raise RuntimeError('boom')\n")
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert final["status"] == "failed"
    assert final["error"].startswith("SCRIPT_ERROR:") and "boom" in final["error"]
    traceback_path = Path(final["script_path"]).parent / "traceback.txt"
    assert "RuntimeError: boom" in traceback_path.read_text(encoding="utf-8")


def test_cancel_observed_from_disk_control_without_ui_pump(env):
    service, jobs, callbacks, _ = env
    code = ("mcp.set_result({'before': mcp.cancelled()})\n"
            "mcp.check_cancel()\n"
            "mcp.set_result({'after': True})\n")
    status = service.run_script(code)
    key = status["job_id"]
    jobs.pump()
    assert len(callbacks) == 1
    controls = Path(jobs.directory) / "controls"
    controls.mkdir(exist_ok=True)
    (controls / (key + ".cancel.json")).write_text("{}", encoding="utf-8")
    callbacks.pop(0)(Control())
    final = jobs.status(key)
    assert final["result"]["cancelled"] is True
    assert final["result"]["value"] == {"before": True}
    jobs.pump()
    assert jobs.status(key)["status"] == "cancelled"


def test_cancel_before_dispatch_never_runs_the_script(env):
    service, jobs, callbacks, _ = env
    status = service.run_script("mcp.set_result({'ran': True})\n")
    key = status["job_id"]
    assert jobs.cancel(key)["status"] == "cancelling"
    jobs.pump()
    final = jobs.status(key)
    assert final["status"] == "cancelled"
    assert final["result"] is None
    assert callbacks == []
    # A cancelled single-step script has nothing left to continue; it must not be
    # resumable into a misleading "completed" state.
    with pytest.raises(ValueError, match="JOB_NOT_RESUMABLE"):
        jobs.resume(key)


def test_system_exit_is_contained_and_never_redispatched(env):
    service, jobs, callbacks, _ = env
    status = service.run_script("import sys\nsys.exit(3)\n")
    key = status["job_id"]
    finish(jobs, callbacks)
    final = jobs.status(key)
    assert final["status"] == "failed"
    assert "SystemExit" in final["error"]
    assert Path(final["script_path"]).parent.joinpath("traceback.txt").exists()
    jobs.pump()
    jobs.pump()
    assert callbacks == []  # the step was consumed exactly once


def test_non_finite_progress_values_are_dropped(env):
    service, jobs, callbacks, _ = env
    code = ("mcp.progress('stage', float('nan'), float('inf'), note='x')\n"
            "mcp.set_result({'ok': True})\n")
    status = service.run_script(code)
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert final["status"] == "completed"
    assert final["progress_note"] == "x"
    assert "progress_current" not in final and "progress_total" not in final


def test_restore_point_prefers_guard_thread_event(env, monkeypatch):
    service, _, _, _ = env
    guard = NS(thread_state=threading.local())
    guard.thread_state.active = True
    guard.thread_state.event = 55
    monkeypatch.setitem(sys.modules, SCRIPTS.__package__ + ".replay_guard",
                        NS(GUARDS={id(service.ctx): guard}))
    assert service._restore_point() == 55
    guard.thread_state.active = False
    assert service._restore_point() == 77


def test_rewritten_artifact_keeps_one_entry(env):
    service, jobs, callbacks, _ = env
    code = ("mcp.artifact('x.bin', 'first')\n"
            "info = mcp.artifact('x.bin', 'second')\n"
            "mcp.set_result({'sha': info['sha256']})\n")
    status = service.run_script(code)
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert len(final["result"]["artifacts"]) == 1
    entry = final["result"]["artifacts"][0]
    assert Path(entry["path"]).read_text(encoding="utf-8") == "second"
    assert entry["sha256"] == hashlib.sha256(b"second").hexdigest()


def test_cancelled_script_releases_its_runner(env):
    service, jobs, callbacks, _ = env
    status = service.run_script("mcp.set_result(1)\n")
    key = status["job_id"]
    jobs.cancel(key)
    jobs.pump()
    assert jobs.status(key)["status"] == "cancelled"
    # Nothing can resume it, so the generator (and the script text it closes over)
    # must not stay alive for the rest of the session.
    assert key not in jobs.runners and key not in jobs.pending


def test_replay_step_restores_with_guard_thread_event(tmp_path, monkeypatch):
    session = Session()
    callbacks, events, preflight = [], [], []
    ctx = NS(IsCaptureLoaded=lambda: True, CurEvent=lambda: 77,
             Replay=lambda: NS(AsyncInvoke=callbacks.append))
    jobs = JOBS.JobService(ctx, session, str(tmp_path))
    guard = NS(state={"event_id": 42}, thread_state=threading.local(),
               preflight=lambda: preflight.append(True),
               phase=lambda *args, **kwargs: None,
               check=lambda controller: None)
    monkeypatch.setitem(sys.modules, SCRIPTS.__package__ + ".replay_guard",
                        NS(GUARDS={id(ctx): guard}))
    service = SCRIPTS.ScriptService(ctx, session, jobs)
    code = ("import threading\n"
            "pyrenderdoc.SetFrameEvent(900, True)\n"
            "mcp.set_result({'thread': threading.current_thread().name})\n")
    status = service.run_script(code)
    jobs.pump()
    assert preflight  # the UI-side dispatch probes replay health first
    worker = threading.Thread(target=lambda: callbacks.pop(0)(Control(events)),
                              name="replay-sim")
    worker.start()
    worker.join()
    jobs.pump()
    final = jobs.status(status["job_id"])
    assert final["status"] == "completed"
    assert final["result"]["value"]["thread"] == "replay-sim"
    # Restore uses the guard's thread-local event (42), not ctx.CurEvent() (77).
    assert events == [(900, True), (42, True)]


def test_artifact_case_aliases_share_one_entry(env):
    service, jobs, callbacks, _ = env
    code = ("mcp.artifact('x.bin', 'first')\n"
            "info = mcp.artifact('X.BIN', 'second')\n"
            "mcp.set_result({'sha': info['sha256']})\n")
    status = service.run_script(code)
    finish(jobs, callbacks)
    artifacts = jobs.status(status["job_id"])["result"]["artifacts"]
    same_file = os.path.normcase("x.bin") == os.path.normcase("X.BIN")
    assert len(artifacts) == (1 if same_file else 2)


def test_tee_reports_failed_output_writes(tmp_path):
    handle = open(tmp_path / "output.log", "w", encoding="utf-8")
    handle.close()
    tee = SCRIPTS._Tee(io.StringIO(), handle)
    assert tee.write("x") == 1
    assert tee._error


def test_result_size_and_serialization_limits(env):
    service, jobs, callbacks, _ = env
    status = service.run_script("mcp.set_result({'payload': 'x' * (300 * 1024)})\n")
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert final["status"] == "failed"
    assert final["error"].startswith("SCRIPT_RESULT_TOO_LARGE")
    status = service.run_script("mcp.set_result({'x': object()})\n")
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    assert final["status"] == "failed"
    assert final["error"].startswith("SCRIPT_RESULT_NOT_SERIALIZABLE")


def test_artifacts_are_written_with_hashes(env):
    service, jobs, callbacks, _ = env
    code = ("info = mcp.artifact('values.csv', '1,2,3')\n"
            "mcp.set_result({'artifact': info['name'], 'path': mcp.artifact_path('next.txt')})\n")
    status = service.run_script(code)
    finish(jobs, callbacks)
    final = jobs.status(status["job_id"])
    entry = final["result"]["artifacts"][0]
    assert Path(entry["path"]).read_text(encoding="utf-8") == "1,2,3"
    assert entry["sha256"] == hashlib.sha256(b"1,2,3").hexdigest()
    assert final["result"]["value"]["artifact"] == "values.csv"
    assert Path(final["result"]["value"]["path"]).parent.name == "artifacts"


def test_event_restored_unless_keep_event(env):
    service, jobs, callbacks, _ = env
    events = []
    status = service.run_script("pyrenderdoc.SetFrameEvent(900, True)\n")
    finish(jobs, callbacks, Control(events))
    assert jobs.status(status["job_id"])["status"] == "completed"
    assert events == [(900, True), (77, True)]
    events = []
    status = service.run_script("mcp.keep_event()\npyrenderdoc.SetFrameEvent(901, True)\n")
    finish(jobs, callbacks, Control(events))
    assert events == [(901, True)]


def test_resubmission_is_idempotent_and_conflicts_on_new_code(env):
    service, jobs, callbacks, _ = env
    key = "11111111-1111-4111-8111-111111111111"
    assert service.run_script("mcp.set_result(1)\n", job_id=key)["status"] == "queued"
    assert service.run_script("mcp.set_result(1)\n", job_id=key)["status"] == "queued"
    with pytest.raises(ValueError, match="JOB_CONFLICT"):
        service.run_script("mcp.set_result(2)\n", job_id=key)


def test_submission_validation(env):
    service, jobs, callbacks, _ = env
    with pytest.raises(ValueError, match="INVALID_REQUEST: code must be a non-empty string"):
        service.run_script("   ")
    with pytest.raises(ValueError, match="INVALID_REQUEST: code must be a non-empty string"):
        service.run_script(None)
    with pytest.raises(ValueError, match="INVALID_REQUEST: label must be a string"):
        service.run_script("pass\n", label=7)
    with pytest.raises(ValueError, match="SCRIPT_SYNTAX_ERROR"):
        service.run_script("if True:\npass\n")
    with pytest.raises(ValueError, match="INVALID_REQUEST: script exceeds"):
        service.run_script("#" * (513 * 1024))
    assert jobs.records == {}


def test_capture_is_required(tmp_path):
    session = Session()
    jobs = JOBS.JobService(NS(Replay=lambda: NS(AsyncInvoke=lambda run: None)), session, str(tmp_path))
    service = SCRIPTS.ScriptService(NS(IsCaptureLoaded=lambda: False, CurEvent=lambda: 0), session, jobs)
    with pytest.raises(ValueError, match="CAPTURE_NOT_LOADED"):
        service.run_script("pass\n")


class Facade(object):
    _guard = None
    _jobs = None
    runtime_info = {"api_contract_version": 3, "extension_version": "3.1.0"}

    def __init__(self):
        self.calls = []

    def run_script(self, code, label=None, job_id=None):
        self.calls.append((code, label, job_id))
        return {"job_id": "job", "status": "queued"}


def request(method, params):
    return {"id": "request", "method": method, "params": params,
            "api_contract_version": 3, "server_version": "3.1.0"}


def test_request_handler_dispatches_run_script_and_whitelists_params():
    facade = Facade()
    handler = HANDLER.RequestHandler(facade)
    result = handler.handle(request("run_script", {"code": "pass\n", "label": "batch"}))
    assert result["result"]["status"] == "queued"
    assert facade.calls == [("pass\n", "batch", None)]
    rejected = handler.handle(request("run_script", {"code": "pass\n", "code_sha256": "spoof"}))
    assert "INVALID_REQUEST: unexpected parameter(s): code_sha256" in rejected["error"]["message"]
    assert len(facade.calls) == 1


def test_server_gate_and_python36_precheck(monkeypatch):
    server = pytest.importorskip("mcp_server.server")
    calls = []
    monkeypatch.setattr(server.bridge, "call",
                        lambda method, params=None: calls.append((method, params)) or {"job_id": "job"})
    monkeypatch.delenv(server.SCRIPT_EXECUTION_ENV, raising=False)
    with pytest.raises(server.RenderDocBridgeError, match="SCRIPT_EXECUTION_DISABLED"):
        server.run_script(code="print(1)\n")
    assert calls == []
    monkeypatch.setenv(server.SCRIPT_EXECUTION_ENV, "1")
    with pytest.raises(server.RenderDocBridgeError, match="provide exactly one of code or script_path"):
        server.run_script()
    with pytest.raises(server.RenderDocBridgeError, match="provide exactly one of code or script_path"):
        server.run_script(code="pass\n", script_path=str(ROOT / "no.py"))
    with pytest.raises(server.RenderDocBridgeError, match="SCRIPT_SYNTAX_ERROR"):
        server.run_script(code="if (n := 1):\n    pass\n")
    assert calls == []
    assert server.run_script(code="mcp.set_result(1)\n", label="x") == {"job_id": "job"}
    assert calls[-1] == ("run_script", {"code": "mcp.set_result(1)\n", "label": "x", "job_id": None})


def test_server_reads_script_path_and_rejects_relative(tmp_path, monkeypatch):
    server = pytest.importorskip("mcp_server.server")
    calls = []
    monkeypatch.setattr(server.bridge, "call",
                        lambda method, params=None: calls.append((method, params)) or {"job_id": "job"})
    monkeypatch.setenv(server.SCRIPT_EXECUTION_ENV, "true")
    script = tmp_path / "batch.py"
    # Bytes, not text: the server reads bytes so newlines are not translated.
    script.write_bytes(b"mcp.set_result(2)\n")
    server.run_script(script_path=str(script))
    assert calls[-1][1]["code"] == "mcp.set_result(2)\n"
    with pytest.raises(server.RenderDocBridgeError, match="script_path must be absolute"):
        server.run_script(script_path="batch.py")
    with pytest.raises(server.RenderDocBridgeError, match="cannot read"):
        server.run_script(script_path=str(tmp_path / "missing.py"))


def test_server_rejects_oversized_script_files(tmp_path, monkeypatch):
    server = pytest.importorskip("mcp_server.server")
    calls = []
    monkeypatch.setattr(server.bridge, "call",
                        lambda method, params=None: calls.append((method, params)) or {"job_id": "job"})
    monkeypatch.setenv(server.SCRIPT_EXECUTION_ENV, "1")
    big = tmp_path / "big.py"
    big.write_bytes(b"#" * (server.MAX_SCRIPT_BYTES + 1))
    with pytest.raises(server.RenderDocBridgeError, match="script exceeds"):
        server.run_script(script_path=str(big))
    not_utf8 = tmp_path / "binary.py"
    not_utf8.write_bytes(b"\xff\xfe\x00")
    with pytest.raises(server.RenderDocBridgeError, match="must be UTF-8"):
        server.run_script(script_path=str(not_utf8))
    assert calls == []
