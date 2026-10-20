"""Exercise real file IPC, OS transaction locks and late responses."""

import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import time
import types
import unittest
import uuid
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CLIENT = load("bridge_under_test", "mcp_server/bridge/client.py")


class QObject:
    def __init__(self, parent=None):
        pass


qt = types.ModuleType("PySide2.QtCore")
qt.QObject, qt.QTimer = QObject, object
with patch.dict(sys.modules, {"PySide2": types.ModuleType("PySide2"), "PySide2.QtCore": qt}):
    SERVER = load("server_under_test", "renderdoc_extension/socket_server.py")


class Handler:
    def __init__(self):
        self.calls = []

    def handle(self, request):
        self.calls.append(request)
        time.sleep(request["params"].get("delay", 0))
        return {"id": request["id"], "result": request["params"]}


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        directory = self.directory.name
        self.patches = []
        for module in (CLIENT, SERVER):
            paths = {"IPC_DIR": directory, "REQUEST_FILE": os.path.join(directory, "request.json"),
                     "RESPONSE_FILE": os.path.join(directory, "response.json"),
                     "LOCK_FILE": os.path.join(directory, "lock")}
            if module is CLIENT:
                paths["CALL_LOCK_FILE"] = os.path.join(directory, "call.lock")
            current = patch.multiple(module, **paths)
            current.start()
            self.patches.append(current)
        self.handler = Handler()
        self.server = SERVER.MCPBridgeServer("", 0, self.handler)
        self.server._running = True
        self.stop = threading.Event()
        self.thread = None

    def tearDown(self):
        self.stop.set()
        if self.thread:
            self.thread.join(3)
        for current in self.patches:
            current.stop()
        self.directory.cleanup()

    def start_server(self):
        def poll():
            while not self.stop.is_set():
                self.server._poll_request()
                self.stop.wait(0.002)
        self.thread = threading.Thread(target=poll, daemon=True)
        self.thread.start()

    def test_concurrent_clients_are_serialized(self):
        self.start_server()
        responses = {}
        failures = []

        def call(marker):
            try:
                responses[marker] = CLIENT.RenderDocBridge().call("ping", {"marker": marker, "delay": 0.06})
            except Exception as exc:
                failures.append(exc)

        clients = [threading.Thread(target=call, args=(i,)) for i in range(3)]
        for thread in clients:
            thread.start()
        for thread in clients:
            thread.join(3)
        self.assertEqual(failures, [])
        self.assertEqual(len(self.handler.calls), 3)
        self.assertEqual({key: value["marker"] for key, value in responses.items()}, {0: 0, 1: 1, 2: 2})

    def test_empty_lock_file_excludes_second_client_without_initialization_write(self):
        failures = []
        acquired = []

        def contender():
            try:
                with CLIENT.RenderDocBridge()._transaction(time.monotonic() + 0.05):
                    acquired.append(True)
            except CLIENT.RenderDocBridgeError as exc:
                failures.append(str(exc))

        with CLIENT.RenderDocBridge()._transaction(time.monotonic() + 1):
            self.assertEqual(os.path.getsize(CLIENT.CALL_LOCK_FILE), 0)
            thread = threading.Thread(target=contender)
            thread.start()
            thread.join(2)
            self.assertFalse(thread.is_alive())
            self.assertFalse(acquired)
            self.assertEqual(len(failures), 1)
            self.assertIn("IPC_BUSY", failures[0])
        with CLIENT.RenderDocBridge()._transaction(time.monotonic() + 1):
            self.assertEqual(os.path.getsize(CLIENT.CALL_LOCK_FILE), 0)

    def test_timeout_late_reply_cannot_satisfy_following_call(self):
        self.start_server()
        client = CLIENT.RenderDocBridge()
        client.edit_timeout = 0.02
        with self.assertRaisesRegex(CLIENT.RenderDocBridgeError, "RESULT_PENDING.*Do not automatically retry"):
            client.call("replace_shader", {"marker": "first", "delay": 0.15})
        self.assertEqual(client.call("ping", {"marker": "second"}), {"marker": "second"})
        self.assertEqual(len(self.handler.calls), 2)
        self.assertTrue(list(Path(self.directory.name).glob("response_*.json")))

    def test_response_id_is_checked(self):
        Path(CLIENT.RESPONSE_FILE).write_text(json.dumps({"id": "stale", "result": "wrong"}), encoding="utf-8")
        self.start_server()
        self.assertEqual(CLIENT.RenderDocBridge().call("ping", {"marker": "right"}), {"marker": "right"})

    def test_pending_request_is_not_overwritten_after_timeout(self):
        pending = {"id": "pending", "method": "slow"}
        Path(CLIENT.REQUEST_FILE).write_text(json.dumps(pending), encoding="utf-8")
        client = CLIENT.RenderDocBridge()
        client.timeout = 0.01
        with self.assertRaisesRegex(CLIENT.RenderDocBridgeError, "request was not submitted"):
            client.call("ping")
        self.assertEqual(json.loads(Path(CLIENT.REQUEST_FILE).read_text(encoding="utf-8")), pending)

    def test_nested_poll_does_not_execute_another_request(self):
        request = {"id": str(uuid.uuid4()), "ipc_version": 2, "params": {}}
        nested = {"id": str(uuid.uuid4()), "ipc_version": 2, "params": {"nested": True}}

        def handle(value):
            self.handler.calls.append(value)
            Path(CLIENT.REQUEST_FILE).write_text(json.dumps(nested), encoding="utf-8")
            self.server._poll_request()
            return {"id": value["id"], "result": "first"}

        self.server.handler = types.SimpleNamespace(handle=handle)
        Path(CLIENT.REQUEST_FILE).write_text(json.dumps(request), encoding="utf-8")
        self.server._poll_request()
        self.assertEqual(len(self.handler.calls), 1)
        self.assertTrue(Path(CLIENT.REQUEST_FILE).exists())
        response = Path(self.directory.name) / ("response_%s.json" % request["id"])
        self.assertEqual(json.loads(response.read_text(encoding="utf-8"))["result"], "first")
        self.assertFalse(Path(str(response) + ".tmp").exists())

    def test_server_supports_legacy_client(self):
        request = {"id": "legacy-id", "method": "ping", "params": {}}
        Path(CLIENT.REQUEST_FILE).write_text(json.dumps(request), encoding="utf-8")
        self.server._poll_request()
        self.assertEqual(json.loads(Path(CLIENT.RESPONSE_FILE).read_text(encoding="utf-8"))["id"], "legacy-id")

    def test_error_reply_is_not_a_success(self):
        self.server.handler = types.SimpleNamespace(handle=lambda request: {
            "id": request["id"], "error": {"code": -32000, "message": "SHADER_TOOL_MISSING: compiler"}})
        self.start_server()
        with self.assertRaisesRegex(CLIENT.RenderDocBridgeError, "SHADER_TOOL_MISSING"):
            CLIENT.RenderDocBridge().call("get_shader_edit_context")


if __name__ == "__main__":
    unittest.main()
