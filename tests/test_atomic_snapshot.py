"""Windows atomic publication retries never repeat native export work."""
import json

import pytest
from test_v2 import JOBS


def test_sharing_violation_retries_same_temporary_file(tmp_path,monkeypatch):
    path=str(tmp_path/'job.json');JOBS.atomic_json(path,{'revision':1})
    replace=JOBS.os.replace;attempts=[]
    def sharing(source,dest):
        attempts.append(source)
        if len(attempts)<3:
            error=OSError('reader holds destination');error.winerror=5;raise error
        replace(source,dest)
    monkeypatch.setattr(JOBS.os,'replace',sharing)
    JOBS.atomic_json(path,{'revision':2})
    assert len(set(attempts))==1 and len(attempts)==3
    assert json.loads((tmp_path/'job.json').read_text())=={'revision':2}
    assert not list(tmp_path.glob('*.tmp'))


def test_permanent_io_error_preserves_previous_snapshot(tmp_path,monkeypatch):
    path=str(tmp_path/'job.json');JOBS.atomic_json(path,{'revision':1})
    def fail(*args):raise OSError('disk full')
    monkeypatch.setattr(JOBS.os,'replace',fail)
    with pytest.raises(OSError,match='disk full'):JOBS.atomic_json(path,{'revision':2})
    assert json.loads((tmp_path/'job.json').read_text())=={'revision':1}
    assert not list(tmp_path.glob('*.tmp'))


def test_persistent_sharing_violation_has_bounded_retries(tmp_path,monkeypatch):
    path=str(tmp_path/'job.json');JOBS.atomic_json(path,{'revision':1})
    attempts=[];delays=[]
    def fail(source,dest):
        attempts.append(source)
        error=OSError('sharing violation');error.winerror=32;raise error
    monkeypatch.setattr(JOBS.os,'replace',fail)
    monkeypatch.setattr(JOBS.time,'sleep',delays.append)
    with pytest.raises(OSError):JOBS.atomic_json(path,{'revision':2})
    assert len(attempts)==7 and len(set(attempts))==1 and sum(delays)<.4
    assert json.loads((tmp_path/'job.json').read_text())=={'revision':1}
