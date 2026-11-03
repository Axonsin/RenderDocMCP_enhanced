"""Detached, verifiable export checkpoints (no replay/Qt access)."""
import hashlib
import json
import os

from .job_service import atomic_json


def digest(path):
    value = hashlib.sha256()
    with open(path, 'rb') as handle:
        for block in iter(lambda: handle.read(1024*1024), b''):
            value.update(block)
    return value.hexdigest()


class ExportCheckpoint:
    VERSION = 1

    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.path = os.path.join(directory, 'checkpoint.json')
        self.tasks = {}
        if os.path.isfile(self.path):
            with open(self.path, encoding='utf-8') as handle:
                data = json.load(handle)
            if data.get('version') != self.VERSION:
                raise ValueError('CHECKPOINT_VERSION_MISMATCH: unsupported export checkpoint')
            self.tasks = data['tasks']

    def _inside(self, path):
        return os.path.commonpath([self.directory, os.path.realpath(path)]) == os.path.realpath(self.directory)

    def restore(self, key):
        row = self.tasks.get(key)
        if not row or row.get('status') != 'completed':
            return None
        for artifact in row['artifacts']:
            path = artifact['path']
            if not self._inside(path) or not os.path.isfile(path) or digest(path) != artifact['sha256']:
                return None
        return row['result']

    def complete(self, key, result, paths):
        artifacts = []
        for path in dict.fromkeys(paths):
            if not self._inside(path):
                raise ValueError('INVALID_ARTIFACT_PATH: outside export directory')
            artifacts.append(dict(path=path, sha256=digest(path), size_bytes=os.path.getsize(path)))
        self.tasks[key] = dict(status='completed', result=result, artifacts=artifacts)
        atomic_json(self.path, dict(version=self.VERSION, tasks=self.tasks))
        return result
