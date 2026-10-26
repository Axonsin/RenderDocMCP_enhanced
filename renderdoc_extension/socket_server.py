"""
File-based IPC Server for RenderDoc MCP Bridge
Uses file polling since RenderDoc's Python doesn't have socket/QtNetwork modules.
"""

import json
import os
import traceback
import tempfile
import uuid
import time

from PySide2.QtCore import QObject, QTimer


# IPC directory
IPC_DIR = os.path.join(tempfile.gettempdir(), "renderdoc_mcp")
REQUEST_FILE = os.path.join(IPC_DIR, "request.json")
IPC_VERSION = 2


class MCPBridgeServer(QObject):
    """File-based IPC server for MCP bridge communication"""

    def __init__(self, handler, parent=None):
        super(MCPBridgeServer, self).__init__(parent)
        self.handler = handler
        self._timer = None
        self._running = False
        self._busy = False

        # Create IPC directory
        if not os.path.exists(IPC_DIR):
            os.makedirs(IPC_DIR)

    def start(self):
        """Start the server with polling"""
        self._running = True

        # Clean up old files
        self._cleanup_files()

        # Start polling timer (check every 100ms)
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._poll_request)
        self._timer.start(100)

        print("[MCP Bridge] File-based IPC server started")
        print("[MCP Bridge] IPC directory: %s" % IPC_DIR)
        return True

    def stop(self):
        """Stop the server"""
        self._running = False
        if self._timer:
            self._timer.stop()
            self._timer = None
        self._cleanup_files()
        print("[MCP Bridge] Server stopped")

    def is_running(self):
        """Check if server is running"""
        return self._running

    def _cleanup_files(self):
        """Remove IPC files"""
        for f in [REQUEST_FILE]:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except Exception:
                pass

    def _poll_request(self):
        """Check for incoming request"""
        if not self._running or self._busy:
            return

        # Check if request file exists
        if not os.path.exists(REQUEST_FILE):
            self._pump_jobs()
            return

        self._busy = True  # ShaderProcessingTool progress dialogs run a nested Qt event loop.
        temporary = None
        try:
            # Read request
            with open(REQUEST_FILE, "r", encoding="utf-8") as f:
                request = json.load(f)

            # Remove request file
            os.remove(REQUEST_FILE)

            request_id = str(uuid.UUID(request["id"]))
            if request["ipc_version"] != IPC_VERSION:
                raise ValueError("Invalid IPC protocol version")

            # Process request
            try:
                response = self.handler.handle(request)
            except Exception as e:
                traceback.print_exc()
                response = {
                    "id": request.get("id"),
                    "error": {"code": -32603, "message": str(e)}
                }

            response_path = os.path.join(IPC_DIR, "response_%s.json" % request_id)
            temporary = response_path + ".tmp"
            serialization_start = time.monotonic()
            with open(temporary, "w", encoding="utf-8") as f:
                json.dump(response, f)
            response_bytes = os.path.getsize(temporary)
            os.replace(temporary, response_path)
            guard = getattr(self.handler.facade, "_guard", None) if hasattr(self.handler, "facade") else None
            if guard:
                guard.phase("response_published", serialization_seconds=time.monotonic()-serialization_start, response_bytes=response_bytes)

        except Exception as e:
            print("[MCP Bridge] Error processing request: %s" % str(e))
            traceback.print_exc()
        finally:
            self._busy = False
            if temporary and os.path.exists(temporary):
                os.remove(temporary)
        # Publish the reply before starting any native/UI operation. Continuous
        # status polling must not starve the cooperative job scheduler.
        self._pump_jobs()

    def _pump_jobs(self):
        facade = getattr(self.handler, "facade", None)
        jobs = getattr(facade, "_jobs", None)
        if jobs:
            jobs.pump()
