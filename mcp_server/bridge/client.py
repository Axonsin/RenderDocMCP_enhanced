"""
RenderDoc Bridge Client
Communicates with the RenderDoc extension via file-based IPC.
"""

import json
import os
import tempfile
import time
import uuid
import logging
from logging.handlers import RotatingFileHandler
from contextlib import contextmanager
from typing import Any
from mcp_server.bridge.job_status import read_status, request_cancel


# IPC directory (must match renderdoc_extension/socket_server.py)
IPC_DIR = os.path.join(tempfile.gettempdir(), "renderdoc_mcp")
REQUEST_FILE = os.path.join(IPC_DIR, "request.json")
CALL_LOCK_FILE = os.path.join(IPC_DIR, "call.lock")

EDIT_METHODS = {"get_shader_edit_context", "replace_shader", "revert_shader",
                "list_shader_replacements", "export_shader_source"}
JOB_METHODS = {"open_capture", "dump_draws", "export_shader_bundle", "compare_texture_events",
               "get_pixel_history", "run_script"}


class RenderDocBridgeError(Exception):
    """Error communicating with RenderDoc bridge"""

    pass


class RenderDocBridge:
    """Client for communicating with RenderDoc extension via file-based IPC"""

    def __init__(self):
        self.timeout = 30.0  # seconds
        self.edit_timeout = 120.0

    @contextmanager
    def _transaction(self, deadline):
        """OS lock serializes clients, including separate MCP server processes.

        Unlike an exclusive-create sentinel, the lock is released if a client dies.
        `deadline` covers both lock acquisition and response wait so the whole
        call stays within the client-side tool timeout.
        """
        with open(CALL_LOCK_FILE, "a+b") as handle:
            # Windows permits locking a byte beyond EOF. Do not seed the file:
            # another client can lock byte zero between our size check and flush,
            # causing the initialization write to fail with PermissionError.
            locked = False
            while not locked:
                handle.seek(0)
                try:
                    if os.name == "nt":
                        import msvcrt
                        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    locked = True
                except OSError:
                    if time.monotonic() >= deadline:
                        raise RenderDocBridgeError("IPC_BUSY: timed out waiting for another client; "
                                                  "request was not submitted")
                    time.sleep(0.05)
            try:
                yield
            finally:
                handle.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _journal(self, row):
        handler = None
        try:
            directory = os.path.join(IPC_DIR, "diagnostics")
            os.makedirs(directory, exist_ok=True)
            handler = RotatingFileHandler(os.path.join(directory, "ipc.jsonl"), maxBytes=10*1024*1024,
                                          backupCount=2, encoding="utf-8", delay=True)
            record = logging.LogRecord("ipc", logging.INFO, "", 0, json.dumps(row), (), None)
            handler.emit(record)
        except OSError:
            pass
        finally:
            if handler:
                handler.close()

    def call(self, method: str, params: dict[str, Any] | None = None) -> Any:
        request_id = str(uuid.uuid4())
        started = time.monotonic()
        self._journal({"request_id": request_id, "method": method, "phase": "ipc_submit", "started_at": time.time()})
        try:
            result = self._call(method, params, request_id)
            self._journal({"request_id": request_id, "method": method, "phase": "ipc_complete", "ended_at": time.time(),
                           "elapsed_seconds": time.monotonic()-started})
            return result
        except Exception as exc:
            self._journal({"request_id": request_id, "method": method, "phase": "ipc_error", "ended_at": time.time(),
                           "elapsed_seconds": time.monotonic()-started, "error": str(exc)[:2048]})
            raise

    def _call(self, method: str, params: dict[str, Any] | None = None, request_id=None) -> Any:
        """Call a method on the RenderDoc extension"""
        if method == "get_replay_diagnostics":
            from .diagnostics import collect
            return collect(os.path.join(IPC_DIR, "diagnostics"), **(params or {}))
        # Check if IPC directory exists
        if not os.path.exists(IPC_DIR):
            raise RenderDocBridgeError(
                f"Cannot connect to RenderDoc MCP Bridge in {IPC_DIR}. "
                "Make sure RenderDoc is running with the MCP Bridge extension loaded."
            )

        params = dict(params or {})
        if method in ("get_job_status", "cancel_job"):
            try:
                function = read_status if method == "get_job_status" else request_cancel
                return function(os.path.join(IPC_DIR, "jobs"), **params)
            except (ValueError, OSError) as exc:
                raise RenderDocBridgeError(str(exc)) from exc
        if method in JOB_METHODS and not params.get("job_id"):
            params["job_id"] = str(uuid.uuid4())
        request = {
            "id": request_id or str(uuid.uuid4()),
            "method": method,
            "params": params or {},
            "ipc_version": 2,
            "server_version": "3.1.0",
            "api_contract_version": 3,
        }
        timeout = self.edit_timeout if method in EDIT_METHODS else self.timeout
        response_file = os.path.join(IPC_DIR, "response_%s.json" % request["id"])
        temporary = os.path.join(IPC_DIR, "request_%s.tmp" % request["id"])
        deadline = time.monotonic() + timeout
        try:
            with self._transaction(deadline):
                # Never overwrite a request left pending by a timed-out client.
                while os.path.exists(REQUEST_FILE):
                    if time.monotonic() >= deadline:
                        raise RenderDocBridgeError("IPC_BUSY: previous request is still pending; "
                                                  "request was not submitted")
                    time.sleep(0.05)
                with open(temporary, "x", encoding="utf-8") as handle:
                    json.dump(request, handle)
                os.replace(temporary, REQUEST_FILE)
                while True:
                    # Per-request replies prevent a late response overwriting the next reply.
                    if os.path.exists(response_file):
                        try:
                            with open(response_file, "r", encoding="utf-8") as handle:
                                response = json.load(handle)
                        except PermissionError:
                            if time.monotonic() >= deadline:
                                raise RenderDocBridgeError("RESULT_PENDING: response file is inaccessible; operation was submitted, do not resubmit")
                            time.sleep(min(0.1, max(0, deadline-time.monotonic())))
                            continue
                        if response.get("id") != request["id"]:
                            raise RenderDocBridgeError("IPC_RESPONSE_MISMATCH: response ID differs from submitted request")
                        try:
                            os.remove(response_file)
                        except OSError:
                            pass  # A validated result remains valid if cleanup fails.
                        if response.get("id") == request["id"]:
                            if response.get("api_contract_version") != 3:
                                raise RenderDocBridgeError("API_VERSION_MISMATCH: update both MCP server and RenderDoc extension to 3.x")
                            if "error" in response:
                                error = response["error"]
                                raise RenderDocBridgeError(f"[{error['code']}] {error['message']}")
                            return response.get("result")
                    if time.monotonic() >= deadline:
                        raise RenderDocBridgeError(
                            "RESULT_PENDING: request %s timed out after submission; result is unknown. "
                            "Do not automatically retry. %s" % (request["id"],
                            ("Query get_job_status(job_id=%s)." % params["job_id"]) if method in JOB_METHODS
                            else "Query current replay/shader state before retrying."))
                    time.sleep(0.05)
        except RenderDocBridgeError:
            raise
        except Exception as e:
            raise RenderDocBridgeError(f"Communication error: {e}")
        finally:
            if os.path.exists(temporary):
                os.remove(temporary)
