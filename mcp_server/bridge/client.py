"""
RenderDoc Bridge Client
Communicates with the RenderDoc extension via file-based IPC.
"""

import json
import os
import tempfile
import time
import uuid
from contextlib import contextmanager
from typing import Any


# IPC directory (must match renderdoc_extension/socket_server.py)
IPC_DIR = os.path.join(tempfile.gettempdir(), "renderdoc_mcp")
REQUEST_FILE = os.path.join(IPC_DIR, "request.json")
CALL_LOCK_FILE = os.path.join(IPC_DIR, "call.lock")

EDIT_METHODS = {"get_shader_edit_context", "replace_shader", "revert_shader",
                "list_shader_replacements", "export_shader_source"}


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

    def call(self, method: str, params: dict[str, Any] | None = None) -> Any:
        """Call a method on the RenderDoc extension"""
        # Check if IPC directory exists
        if not os.path.exists(IPC_DIR):
            raise RenderDocBridgeError(
                f"Cannot connect to RenderDoc MCP Bridge in {IPC_DIR}. "
                "Make sure RenderDoc is running with the MCP Bridge extension loaded."
            )

        request = {
            "id": str(uuid.uuid4()),
            "method": method,
            "params": params or {},
            "ipc_version": 2,
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
                        with open(response_file, "r", encoding="utf-8") as handle:
                            response = json.load(handle)
                        os.remove(response_file)
                        if response.get("id") == request["id"]:
                            if "error" in response:
                                error = response["error"]
                                raise RenderDocBridgeError(f"[{error['code']}] {error['message']}")
                            return response.get("result")
                    if time.monotonic() >= deadline:
                        raise RenderDocBridgeError(
                            "RESULT_PENDING: request %s timed out after submission; result is unknown. "
                            "Do not automatically retry. Query list_shader_replacements or "
                            "get_shader_edit_context to confirm shader state." % request["id"])
                    time.sleep(0.05)
        except RenderDocBridgeError:
            raise
        except Exception as e:
            raise RenderDocBridgeError(f"Communication error: {e}")
        finally:
            if os.path.exists(temporary):
                os.remove(temporary)
