"""Shared replay validity gate and bounded metadata journal (Python 3.6)."""
import json
import logging
from logging.handlers import RotatingFileHandler
import os
import tempfile
import time
import uuid
import threading

GUARDS = {}

def atomic(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    temporary = path + '.' + uuid.uuid4().hex + '.tmp'
    try:
        with open(temporary, 'w', encoding='utf-8') as handle:
            json.dump(value, handle, ensure_ascii=False, allow_nan=False)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)

class ReplayGuard:
    def __init__(self, ctx, session, runtime=None):
        self.ctx, self.session = ctx, session
        self.directory = os.path.join(tempfile.gettempdir(), 'renderdoc_mcp', 'diagnostics')
        os.makedirs(self.directory, exist_ok=True)
        self.logger = logging.getLogger('renderdoc_mcp_requests_' + uuid.uuid4().hex)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(RotatingFileHandler(os.path.join(self.directory, 'requests.jsonl'),
                              maxBytes=10 * 1024 * 1024, backupCount=2, encoding='utf-8'))
        self.state = {'runtime': runtime or {}, 'last_success': None}
        self.failure_session = None
        self.thread_state = threading.local()
        self.cached_token = None
        self.actions = {}
        self.resource_names = {}
        self.action_names = {}
        GUARDS[id(ctx)] = self

    def publish(self):
        try:
            atomic(os.path.join(self.directory, 'current.json'), self.state)
        except OSError as exc:
            self.state['diagnostic_write_error'] = str(exc)

    def begin(self, request):
        self.started = time.monotonic()
        self.phase_started = self.started
        safe = ('action_event_id', 'action_event_id_a', 'action_event_id_b', 'resource_id',
                'mip', 'slice_index', 'sample', 'depth_slice', 'aspect', 'offset', 'length', 'job_id')
        self.state.update(self.session.describe())
        self.state['request'] = {'request_id': request.get('id'), 'method': request.get('method'),
            'parameters': {k: v for k, v in request.get('params', {}).items() if k in safe},
            'started_at': time.time(), 'phase': 'submitted', 'status': 'running'}
        self.publish()
        self.logger.info(json.dumps(self.state['request'], ensure_ascii=False))

    def phase(self, name, **fields):
        row = self.state.setdefault('request', {})
        now = time.monotonic()
        previous = row.get('phase')
        if previous and hasattr(self, 'phase_started'):
            timings = row.setdefault('phase_seconds', {})
            timings[previous] = timings.get(previous, 0)+now-self.phase_started
        self.phase_started = now
        row.update(phase=name, **fields)
        self.logger.info(json.dumps(dict(row, observed_at=time.time()), ensure_ascii=False))
        self.publish()

    def finish(self, error=None):
        row = self.state.setdefault('request', {})
        row.update(ended_at=time.time(), elapsed_seconds=time.monotonic()-getattr(self, 'started', time.monotonic()),
                   status='failed' if error else 'completed')
        if error:
            row['error'] = str(error)[:2048]
        else:
            self.state['last_success'] = dict(row)
        self.logger.info(json.dumps(row, ensure_ascii=False))
        self.publish()

    def observe_failure(self, message):
        self.state['health'] = {'healthy': False, 'error': str(message), 'observed_at': time.time()}
        token = self.session.token()
        if self.failure_session != token:
            self.failure_session = token
            path = os.path.join(self.directory, 'failure_' + uuid.uuid4().hex + '.json')
            self.state['failure_snapshot'] = path
            try:
                atomic(path, self.state)
            except OSError:
                pass
        self.publish()

    def failure(self, message):
        self.observe_failure(message)
        raise RuntimeError(message)

    def preflight(self):
        # UI-only. Never called from inside a replay callback.
        if not self.ctx.IsCaptureLoaded():
            return
        self.state['event_id'] = self.ctx.CurEvent()
        remote = self.ctx.Replay().CurrentRemote()
        self.state['remote_host'] = remote.Hostname() if remote else None
        if remote and not remote.IsConnected():
            self.failure('REMOTE_CONNECTION_LOST: remote context is disconnected')
        props = self.ctx.APIProps()
        api = str(props.pipelineType).split('.')[-1]
        if self.session.expected_api is None:
            self.session.expected_api = api
        self.state['capture_api'] = self.session.expected_api
        if self.cached_token != self.session.token():
            self.actions = {}
            self.action_names = {}
            def visit(rows):
                for action in rows:
                    self.actions[action.eventId] = action
                    try:
                        self.action_names[action.eventId] = self.ctx.GetEventName(action.eventId)
                    except Exception:
                        self.action_names[action.eventId] = ""
                    visit(action.children)
            visit(self.ctx.CurRootActions())
            self.resource_names = {int(r.resourceId): self.ctx.GetResourceName(r.resourceId) for r in self.ctx.GetResources()}
            self.cached_token = self.session.token()

    def check(self, controller):
        fatal = controller.GetFatalErrorStatus()
        if not fatal.OK():
            self.failure('REPLAY_UNHEALTHY: ' + str(fatal.Message()))
        api = str(controller.GetAPIProperties().pipelineType).split('.')[-1]
        if self.session.expected_api and api != self.session.expected_api:
            self.failure('REPLAY_API_MISMATCH: expected %s, received %s' % (self.session.expected_api, api))
        self.state['health'] = {'healthy': True, 'api': api, 'observed_at': time.time()}

    def dispose(self):
        GUARDS.pop(id(self.ctx), None)
        for handler in list(self.logger.handlers):
            handler.close()
            self.logger.removeHandler(handler)
