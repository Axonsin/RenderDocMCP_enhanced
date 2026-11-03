"""Bounded status waits read files without acquiring IPC or replay access."""
import json
import threading
import time
import uuid

import pytest
from mcp_server.bridge.job_status import read_status
import mcp_server.bridge.job_status as reader
from test_v2 import JOBS


def test_wait_wakes_on_revision_change(tmp_path):
    key=str(uuid.uuid4());path=str(tmp_path/(key+'.json'))
    row=dict(job_id=key,api_contract_version=4,kind='test',status='running',status_revision=1,
             last_progress_at=time.time(),items=[],cancel_supported=True,phase_started_at=time.time(),step_kind='replay')
    JOBS.atomic_json(path,row)
    def update():
        time.sleep(.08)
        JOBS.atomic_json(path,dict(row,status_revision=2,status='completed'))
    worker=threading.Thread(target=update);worker.start()
    result=read_status(str(tmp_path),key,wait_seconds=2,after_revision=1)
    worker.join()
    assert result['changed'] and result['status']=='completed' and result['status_revision']==2


def test_unchanged_wait_is_bounded_and_does_not_return_duplicate_items(tmp_path):
    key=str(uuid.uuid4())
    row=dict(job_id=key,api_contract_version=4,kind='test',status='running',status_revision=1,
             last_progress_at=time.time()-100,items=[{'large':'payload'}],cancel_supported=True,
             waiting_for_native=True,phase_started_at=time.time()-100,step_kind='replay')
    JOBS.atomic_json(str(tmp_path/(key+'.json')),row)
    start=time.monotonic()
    result=read_status(str(tmp_path),key,wait_seconds=.1,after_revision=1)
    assert time.monotonic()-start < 1
    assert not result['changed'] and not result['items']
    assert result['status']=='running' and result['waiting_for_native'] and result['stalled']
    assert result['phase_elapsed_seconds']>=100 and result['cancel_effect']=='between_steps'


def test_terminal_wait_ignores_intermediate_revision(tmp_path):
    key=str(uuid.uuid4());path=str(tmp_path/(key+'.json'))
    row=dict(job_id=key,api_contract_version=4,kind='test',status='running',status_revision=1,
             last_progress_at=time.time(),items=[],cancel_supported=True)
    JOBS.atomic_json(path,row)
    def update():
        time.sleep(.05);JOBS.atomic_json(path,dict(row,status_revision=2))
        time.sleep(.15);JOBS.atomic_json(path,dict(row,status_revision=3,status='paused'))
    worker=threading.Thread(target=update);worker.start()
    result=read_status(str(tmp_path),key,wait_seconds=2,after_revision=1,wait_for='terminal')
    worker.join()
    assert result['status']=='paused' and result['status_revision']==3


@pytest.mark.parametrize('wait,revision',[(21,None),(-1,None),(float('nan'),None),(0,-1),(0,True)])
def test_invalid_wait_rejected_before_file_access(tmp_path,wait,revision):
    with pytest.raises(ValueError):read_status(str(tmp_path),str(uuid.uuid4()),wait_seconds=wait,after_revision=revision)


def test_reader_retries_same_snapshot_on_windows_sharing(tmp_path,monkeypatch):
    path=tmp_path/'snapshot.json';path.write_text('{"revision":2}')
    calls=[];original=open
    def sharing(name,*args,**kwargs):
        calls.append(str(name))
        if len(calls)<3:raise PermissionError('snapshot replacement in progress')
        return original(name,*args,**kwargs)
    monkeypatch.setattr(reader,'open',sharing,raising=False)
    assert reader.load_snapshot(str(path))=={'revision':2}
    assert calls==[str(path)]*3
