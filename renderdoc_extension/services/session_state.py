"""Shared capture identity. Never retain replay-owned objects here."""
import hashlib
import os
import uuid

import qrenderdoc as qrd


API_CONTRACT_VERSION = 3


def build_fingerprint():
    root = os.path.dirname(os.path.dirname(__file__))
    digest = hashlib.sha256()
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for name in sorted(files):
            if name.endswith((".py", ".json")):
                path = os.path.join(directory, name)
                digest.update(os.path.relpath(path, root).replace("\\", "/").encode("utf-8"))
                with open(path, "rb") as handle:
                    digest.update(handle.read())
    return digest.hexdigest()


class SessionState(qrd.CaptureViewer):
    def __init__(self, ctx):
        super(SessionState, self).__init__()
        self.ctx = ctx
        self.capture_session = uuid.uuid4().hex
        self.replay_revision = 0
        self.replacements = None
        self.expected_api = None
        self.build_hash = build_fingerprint()
        ctx.AddCaptureViewer(self)

    def OnCaptureLoaded(self):
        self.capture_session = uuid.uuid4().hex
        self.replay_revision = 0
        self.replacements = None
        self.expected_api = None

    def OnCaptureClosed(self):
        self.OnCaptureLoaded()

    def OnSelectedEventChanged(self, event_id):
        pass

    def OnEventChanged(self, event_id):
        pass

    def observe_replacements(self, controller=None):
        # CaptureContext wrappers marshal to the UI thread. Never invoke them
        # from a callback while the UI thread is waiting in BlockInvoke.
        values = []
        for resource in self.ctx.GetResources():
            if str(resource.type).split(".")[-1] == "Shader":
                values.append((int(resource.resourceId),
                               int(self.ctx.GetResourceReplacement(resource.resourceId))))
        fingerprint = tuple(sorted(values))
        if self.replacements is not None and fingerprint != self.replacements:
            self.replay_revision += 1
        self.replacements = fingerprint

    def describe(self):
        return {"capture_session": self.capture_session,
                "replay_revision": self.replay_revision,
                "extension_build_hash": self.build_hash,
                "api_contract_version": API_CONTRACT_VERSION}

    def token(self):
        return (self.capture_session, self.replay_revision)

    def dispose(self):
        self.ctx.RemoveCaptureViewer(self)
