"""Offline diagnostics: never wait for the RenderDoc UI/replay controller."""
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import tempfile
import time
import uuid

LIMIT = 2 * 1024 * 1024

def tail(path, limit=LIMIT):
    with open(path, 'rb') as handle:
        handle.seek(0, 2)
        size = handle.tell()
        handle.seek(max(0, size-limit))
        return handle.read(limit)

def collect(directory, output_dir=None, include_device_logs=False, remote_host=None):
    if type(include_device_logs) is not bool:
        raise ValueError('INVALID_REQUEST: include_device_logs must be boolean')
    if output_dir is not None and (not isinstance(output_dir, str) or not os.path.isabs(output_dir)):
        raise ValueError('INVALID_OUTPUT_PATH: output_dir must be absolute')
    directory = Path(directory)
    key = uuid.uuid4().hex
    target = Path(output_dir or directory/'bundles') / key
    target.mkdir(parents=True, exist_ok=False)
    result = {'diagnostic_id': key, 'observed_at': time.time(), 'source': 'persisted_snapshot',
              'files': [], 'warnings': [], 'device_logs_requested': include_device_logs}
    try:
        state = json.loads((directory/'current.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        state = {}
        result['warnings'].append('snapshot_unavailable: ' + str(exc))
    result['snapshot'] = state

    def artifact(name, data):
        data = data[-LIMIT:]
        path = target/name
        path.write_bytes(data)
        result['files'].append({'path': str(path), 'size_bytes': len(data),
                                'sha256': hashlib.sha256(data).hexdigest()})

    # One aggregate local-log allowance, independent of the device allowance.
    remaining = LIMIT
    sources = [('requests.jsonl', directory/'requests.jsonl'),
               ('ipc.jsonl', directory/'ipc.jsonl'),
               ('renderdoc.log', state.get('renderdoc_log'))]
    for name, path in sources:
        if not path or not remaining:
            continue
        try:
            data = tail(path, min(remaining, LIMIT//2 if name != 'renderdoc.log' else remaining))
            artifact(name, data)
            remaining -= len(data)
        except OSError as exc:
            result['warnings'].append(name + ': ' + str(exc))
    if include_device_logs:
        host = remote_host or state.get('remote_host')
        adb = state.get('adb_path')
        if not isinstance(host, str) or not re.fullmatch(r'adb://[A-Za-z0-9_.:-]+', host):
            result['warnings'].append('device_unavailable: specify a valid adb:// host')
        elif not adb or not os.path.isfile(adb):
            result['warnings'].append('device_unavailable: configured ADB not found')
        else:
            try:
                # Avoid starting an absent ADB daemon as a diagnostic side effect.
                with socket.create_connection(('127.0.0.1', 5037), timeout=.2):
                    pass
                serial = host[6:]
                deadline = time.monotonic()+20
                remaining = LIMIT
                commands = [('device-state.txt', ['get-state']), ('device-processes.txt', ['shell', 'ps', '-A']),
                            ('device-crash-log.txt', ['logcat', '-d', '-b', 'crash', '-t', '2000'])]
                for name, args in commands:
                    if remaining <= 0 or time.monotonic() >= deadline:
                        break
                    options = {'creationflags': 0x08000000} if os.name == 'nt' else {}
                    with tempfile.TemporaryFile() as output:
                        outcome = subprocess.run([adb, '-s', serial]+args, stdout=output,
                            stderr=subprocess.STDOUT, timeout=max(.01, deadline-time.monotonic()), **options)
                        output.seek(0, 2)
                        output.seek(max(0, output.tell()-remaining))
                        data = output.read(remaining)
                    artifact(name, data)
                    remaining -= len(data)
                    if outcome.returncode:
                        result['warnings'].append(name + ': ADB exit ' + str(outcome.returncode))
            except (OSError, subprocess.TimeoutExpired) as exc:
                result['warnings'].append('device_unavailable: ' + str(exc))
    manifest = target/'manifest.json'
    result['manifest_path'] = str(manifest)
    manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    # Keep the potentially large last-success journal on disk.
    return {k: v for k, v in result.items() if k != 'snapshot'}
