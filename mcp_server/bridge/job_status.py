"""Read atomic job snapshots without waiting for RenderDoc's UI thread."""
import json
import os
import time
import uuid


def load_snapshot(path):
    """Retry only transient file sharing; never repeat a submitted operation."""
    for attempt in range(7):
        try:
            with open(path,encoding='utf-8') as handle:
                return json.load(handle)
        except OSError as exc:
            sharing=isinstance(exc,PermissionError) or getattr(exc,'winerror',None) in (5,32,33)
            if not sharing or attempt==6: raise
            time.sleep(.005*(2**attempt))


def item_summary(item, details_path):
    result = {k:item[k] for k in ('item_key','action_event_id','instance','view_index',
              'complete','ok','error','warnings','serialization_complete') if k in item}
    result['details_path'] = details_path
    mesh = item.get('mesh') or {}
    fields = ('success','output_path','index_path','vertex_count','index_count','stage','data_quality')
    result['mesh'] = {k:mesh[k] for k in fields if k in mesh}
    result['meshes'] = {stage:{k:value[k] for k in fields if k in value}
                        for stage,value in item.get('meshes',{}).items()}
    result['shader_exports'] = {stage:{k:value[k] for k in ('shader_id','original','manifest_path','hlsl') if k in value}
                                for stage,value in item.get('shader_exports',{}).items()}
    textures = item.get('textures') or []
    exports = [e for t in textures for e in (t.get('exports') or ([t['export']] if 'export' in t else []))]
    result['texture_exports'] = dict(total=len(exports),saved=sum('path' in e for e in exports),
        failed=sum('error' in e for e in exports),skipped=sum('skipped' in e for e in exports),
        pending=sum('export' not in t and 'exports' not in t for t in textures))
    def artifacts(value):
        found=[]
        if isinstance(value,dict):
            for key,v in value.items():
                if key in ('path','output_path','index_path','details_path','metadata_path','manifest_path','original') and isinstance(v,str):
                    found.append(v)
                else: found.extend(artifacts(v))
        elif isinstance(value,list):
            for v in value: found.extend(artifacts(v))
        return found
    result['artifact_paths']=list(dict.fromkeys(artifacts(item)))
    constants=item.get('constants',[])
    result['constant_exports']=dict(total=len(constants),saved=sum(r.get('status')=='exported' for r in constants),
                                    failed=sum(r.get('status')=='failed' for r in constants))
    return result


def _read_status(directory, job_id, offset=0, limit=100):
    if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 500:
        raise ValueError("INVALID_PAGINATION: offset >= 0, 1 <= limit <= 500")
    job_id = str(uuid.UUID(job_id))
    path = os.path.join(directory, job_id + ".json")
    try:
        record = load_snapshot(path)
    except FileNotFoundError:
        raise ValueError("JOB_NOT_FOUND: %s (submission may still be pending)" % job_id)
    if record.get("api_contract_version") != 4:
        raise ValueError("API_VERSION_MISMATCH: job snapshot requires API contract 4")
    result = {k: v for k, v in record.items() if k not in ("items", "item_files")}
    files = record.get("item_files")
    if files is None:
        count, items = len(record["items"]), record["items"][offset:offset + limit]
    else:
        count, items = len(files), []
        for item_path in files[offset:offset + limit]:
            if os.path.commonpath([os.path.abspath(directory), os.path.abspath(item_path)]) != os.path.abspath(directory):
                raise ValueError("INVALID_JOB_MANIFEST: item path outside job directory")
            items.append(load_snapshot(item_path))
    result.update(items=items, offset=offset, limit=limit, total_count=count,
                  has_more=offset + limit < count, manifest_path=path,
                  idle_seconds=max(0, time.time() - record["last_progress_at"]))
    if record["kind"] == "dump_draws":
        result["items"] = [item_summary(item, files[offset + i] if files else path)
                           for i,item in enumerate(items)]
    result["stalled"] = record["status"] == "running" and result["idle_seconds"] > 30
    result["status_source"] = "atomic_job_snapshot"
    result['phase_elapsed_seconds'] = (max(0,time.time()-record['phase_started_at'])
        if record['status'] == 'running' and 'phase_started_at' in record else record.get('phase_elapsed_seconds',0))
    result['can_request_cancel'] = record.get('cancel_supported',False) and record['status'] not in (
        'completed','completed_with_errors','failed','cancelled','interrupted')
    result['cancel_effect'] = 'between_steps' if record.get('step_kind') == 'replay' else 'cooperative'
    cancel_path = os.path.join(directory, "controls", job_id + ".cancel.json")
    if os.path.exists(cancel_path) and record["status"] in ("queued", "running", "paused", "cancelling"):
        result.update(cancel_requested=True, status="cancelling")
    return result


def read_status(directory, job_id, offset=0, limit=100, wait_seconds=0, after_revision=None, wait_for='change'):
    """Bounded file-only wait. Never holds the IPC lock or calls replay."""
    if isinstance(wait_seconds,bool) or not isinstance(wait_seconds,(int,float)) or not 0 <= wait_seconds <= 20:
        raise ValueError('INVALID_REQUEST: wait_seconds must be between 0 and 20')
    if after_revision is not None and (type(after_revision) is not int or after_revision < 0):
        raise ValueError('INVALID_REQUEST: after_revision must be a nonnegative integer')
    if wait_for not in ('change','terminal'):
        raise ValueError('INVALID_REQUEST: wait_for must be change or terminal')
    deadline=time.monotonic()+wait_seconds
    baseline=after_revision
    while True:
        result=_read_status(directory,job_id,offset,limit)
        revision=result.get('status_revision',0)
        if baseline is None: baseline=revision
        changed=revision != baseline
        if (changed and wait_for=='change') or result['status'] in ('completed','completed_with_errors','failed','cancelled','interrupted','paused') or time.monotonic() >= deadline:
            result['changed']=changed
            if after_revision is not None and not changed:
                result['items']=[]
            return result
        time.sleep(min(.1,max(0,deadline-time.monotonic())))


def request_cancel(directory, job_id):
    snapshot = read_status(directory, job_id, limit=1)
    if snapshot["status"] in ("completed", "completed_with_errors", "failed", "cancelled", "interrupted"):
        return snapshot
    if not snapshot["cancel_supported"]:
        raise ValueError("JOB_NOT_CANCELLABLE: native operation cannot be interrupted")
    controls = os.path.join(directory, "controls")
    os.makedirs(controls, exist_ok=True)
    path = os.path.join(controls, snapshot["job_id"] + ".cancel.json")
    temporary = path + "." + uuid.uuid4().hex + ".tmp"
    try:
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump({"job_id": snapshot["job_id"], "requested_at": time.time()}, handle)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    return read_status(directory, job_id, limit=1)
