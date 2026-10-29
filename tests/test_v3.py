"""3.0 evidence/health contracts, independent of a GPU or Android device."""
import base64
import importlib.util
import json
from pathlib import Path
import struct
import sys
from types import SimpleNamespace as NS
from unittest.mock import patch
import pytest
import test_pipeline as pipeline
import test_v2 as v2

ROOT = Path(__file__).resolve().parents[1]
def standalone(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

GUARD = standalone('guard_v3', 'renderdoc_extension/services/replay_guard.py')
DIAG = standalone('diagnostics_v3', 'mcp_server/bridge/diagnostics.py')
TEXTURE = pipeline.MODULES['resource_service'].select_texture.__globals__
select = pipeline.MODULES['resource_service'].select_texture
transport = pipeline.MODULES['resource_service'].transport_texture
def fmt(name):
    return NS(Name=lambda: name, type=NS(name=name), compType=NS(name='Depth'), compByteWidth=2,
              compCount=1, BGRAOrder=lambda: False)

def test_aspect_numeric_layout_roi_and_samples():
    raw = struct.pack('<4I', 0, 0xC9FFFFFF, 0xC8000000, 0xCB800000)
    data, meta, w, h = select(raw, fmt('D24S8'), 2, 2, 1, 'stencil', {'x':1,'y':0,'width':1,'height':2})
    assert data == bytes([201,203]) and (w,h)==(1,2)
    assert meta['row_pitch']==1 and meta['slice_pitch']==2
    data, meta, _, _ = select(raw, fmt('D24S8'), 2, 2, 1, 'depth')
    assert struct.unpack('<4f',data)[:3] == (0,1,0)
    assert meta['output_format']=='R32_FLOAT'
    assert select(raw,fmt('D24S8'),2,2,1)[0] == raw
    with pytest.raises(ValueError,match='UNSUPPORTED_FORMAT'):
        select(b'\0'*8,fmt('D32S8'),1,1,1,'depth')
    with pytest.raises(ValueError,match='INVALID_ASPECT|UNSUPPORTED_FORMAT'):
        select(b'\0\0',fmt('D16'),1,1,1,'stencil')
    assert struct.unpack('<f',select(b'\xff\xff',fmt('D16'),1,1,1,'depth')[0]) == (1,)

def test_texture_transport_threshold_file_hash_and_no_base64(tmp_path):
    small=transport(b'x'*262144,{},output_dir=str(tmp_path),session='session')
    assert small['output_mode']=='inline' and len(base64.b64decode(small['content_base64']))==262144
    big=transport(b'x'*262145,{},output_dir=str(tmp_path),session='session')
    assert big['output_mode']=='file' and 'content_base64' not in big
    assert Path(big['path']).stat().st_size==262145
    assert json.loads(Path(big['metadata_path']).read_text())['sha256']==big['sha256']
    with pytest.raises(ValueError,match='RESOURCE_LIMIT'):
        transport(b'x'*262145,{},'inline')
    with pytest.raises(ValueError,match='INVALID_OUTPUT_PATH'):
        transport(b'',{},'file','relative')

def test_opaque_and_short_layout_are_not_fabricated():
    raw,meta,_,_=select(b'abc',fmt('ASTC'),4,4,1)
    assert not meta['layout_available'] and meta['row_pitch'] is None and raw==b'abc'
    with pytest.raises(ValueError,match='raw layout/length mismatch'):
        select(b'a',fmt('D16'),1,1,1)
    with pytest.raises(ValueError,match='INVALID_REQUEST|RESOURCE_LIMIT'):
        select(bytes(2*3),fmt('D16'),3,1,1,region={'x':2,'y':0,'width':2,'height':1})

def make_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(GUARD.tempfile,'gettempdir',lambda:str(tmp_path))
    session=NS(expected_api=None,token=lambda:('session',0),describe=lambda:{'capture_session':'session','replay_revision':0})
    ctx=NS(IsCaptureLoaded=lambda:True,CurEvent=lambda:77,Replay=lambda:NS(CurrentRemote=lambda:None),
        APIProps=lambda:NS(pipelineType='Vulkan'),CurRootActions=lambda:[],GetResources=lambda:[])
    guard=GUARD.ReplayGuard(ctx,session)
    return guard,ctx

def controller(api='Vulkan',fatal=False):
    return NS(GetFatalErrorStatus=lambda:NS(OK=lambda:not fatal,Message=lambda:'device lost'),
              GetAPIProperties=lambda:NS(pipelineType=api))

@pytest.mark.parametrize('api',['D3D11','D3D12','Vulkan'])
@pytest.mark.parametrize('empty_host',[False,True])
def test_local_remotehost_sentinel_allows_replay(tmp_path,monkeypatch,api,empty_host):
    g,ctx=make_guard(tmp_path,monkeypatch)
    remote=NS(Hostname=lambda:'',IsConnected=lambda:False) if empty_host else None
    ctx.Replay=lambda:NS(CurrentRemote=lambda:remote)
    ctx.APIProps=lambda:NS(pipelineType=api)
    try:
        g.preflight()
        g.check(controller(api))
        assert g.state['remote_host'] is None
        assert g.session.expected_api == api
    finally:g.dispose()


def test_remote_loss_and_api_mismatch_write_first_failure(tmp_path,monkeypatch):
    g,ctx=make_guard(tmp_path,monkeypatch)
    try:
        g.begin({'id':'request','method':'get_pipeline_stage','params':{'shader_source':'secret'}})
        g.preflight();g.check(controller())
        with pytest.raises(RuntimeError,match='REPLAY_API_MISMATCH'):
            g.check(controller('D3D11'))
        first=g.state['failure_snapshot']
        with pytest.raises(RuntimeError,match='REPLAY_UNHEALTHY'):
            g.check(controller(fatal=True))
        assert first==g.state['failure_snapshot'] and Path(first).is_file()
        assert 'secret' not in Path(first).read_text()
        ctx.Replay=lambda:NS(CurrentRemote=lambda:NS(Hostname=lambda:'adb://device',IsConnected=lambda:False))
        with pytest.raises(RuntimeError,match='REMOTE_CONNECTION_LOST'):
            g.preflight()
    finally:g.dispose()

@pytest.mark.parametrize('failure_stage',['operation','restore'])
def test_at_event_post_checks_reject_values_after_native_failure(tmp_path,monkeypatch,failure_stage):
    g,ctx=make_guard(tmp_path,monkeypatch);g.session.expected_api='Vulkan';ctx.GetAction=lambda e:NS(eventId=e)
    c=controller();c.SetFrameEvent=lambda e,force:None
    def operation(c,e):
        if failure_stage=='operation':c.GetFatalErrorStatus=lambda:NS(OK=lambda:False,Message=lambda:'lost')
        return {'value':'must not escape'}
    if failure_stage=='restore':
        def set_event(e,force):
            if e==77:c.GetFatalErrorStatus=lambda:NS(OK=lambda:False,Message=lambda:'restore lost')
        c.SetFrameEvent=set_event
    with patch.dict(sys.modules,{'renderdoc_extension.services.replay_guard':GUARD}):
        try:
            with pytest.raises(RuntimeError,match='REPLAY_UNHEALTHY|REPLAY_RESTORE_FAILED'):
                pipeline.MODULES['replay_query'].at_event(ctx,lambda fn:fn(c),1,operation)
        finally:g.dispose()

def test_diagnostics_offline_default_no_adb_and_partial_device(tmp_path,monkeypatch):
    directory=tmp_path/'diagnostics';directory.mkdir()
    (directory/'current.json').write_text(json.dumps({'remote_host':'adb://device'}))
    (directory/'requests.jsonl').write_text('journal\n')
    (directory/'ipc.jsonl').write_text('ipc\n')
    monkeypatch.setattr(DIAG.subprocess,'run',lambda *a,**k:pytest.fail('default must not run ADB'))
    r=DIAG.collect(str(directory));assert Path(r['manifest_path']).is_file()
    assert 'snapshot' not in r and not r['warnings']
    r=DIAG.collect(str(directory),include_device_logs=True)
    assert any('configured ADB' in x for x in r['warnings'])

def test_constant_full_tree_event_reads_dynamic_offset_and_blob_dedup(tmp_path):
    exports=v2.CONSTANT_EXPORT
    decl=NS(byteSize=4,variables=[])
    descriptor=NS(resource=1,byteOffset=128,byteSize=4)
    calls=[];value=NS(name='signed',type=NS(name='SInt'),rows=1,columns=1,members=[],value=NS(s32v=[-9]))
    pipe=NS(GetConstantBlock=lambda *a:NS(descriptor=descriptor),GetGraphicsPipelineObject=lambda:2,
        GetShader=lambda s:3,GetShaderEntryPoint=lambda s:'main')
    c=NS(GetBufferData=lambda rid,off,size:calls.append((off,size)) or struct.pack('<i',-9),
         GetCBufferVariableContents=lambda *a:[value])
    row={'category':'constant','stage':'fragment','binding_key':'key','location':{'binding':2},'bound':True,
         'provided_bytes':4,'buffer_backed':True,'resource':{'resource_id':'ResourceId::1'}}
    snapshot=NS(bindings=[row],event_id=10,pipe=pipe,controller=c,api='Vulkan',
                variable_sources={'key':('fragment',0,0,object(),decl)})
    records=exports.read_constants(snapshot);snapshot.event_id=20;second=exports.read_constants(snapshot)
    assert calls==[(128,4),(128,4)]
    a=exports.write_constants(str(tmp_path),records,{'capture_session':'session'},'e10')
    b=exports.write_constants(str(tmp_path),second,{'capture_session':'session'},'e20')
    assert a[0]['raw']['path']==b[0]['raw']['path']
    details=json.loads(Path(a[0]['details_path']).read_text())
    assert details['values'][0]['value']==[-9] and details['byte_offset']==128 and details['action_event_id']==10
    row['bound']=False
    assert exports.read_constants(snapshot)[0]['status']=='skipped'
    row['bound']=True;snapshot.variable_sources['key']=('fragment',0,0,None,None)
    failed=exports.read_constants(snapshot)[0]
    assert failed['status']=='failed' and failed['_raw']==struct.pack('<i',-9)

def test_constant_nested_arrays_matrix_orders_and_nonfinite():
    leaf=NS(name='matrix',type=NS(name='Float'),rows=2,columns=2,members=[],
            value=NS(f32v=[1,2,3,float('nan')]))
    array=NS(name='array',type=NS(name='Struct'),rows=0,columns=0,members=[leaf])
    tree=v2.CONSTANT_EXPORT.full_value(array)
    assert tree['members'][0]['value_order']=='row_major'
    assert tree['members'][0]['value']==[1,2,3,'nan']

def test_diagnostics_device_whitelist_and_rotation_limits(tmp_path,monkeypatch):
    directory=tmp_path/'diagnostics';directory.mkdir();adb=tmp_path/'adb.exe';adb.write_bytes(b'placeholder')
    (directory/'current.json').write_text(json.dumps({'remote_host':'adb://device','adb_path':str(adb)}))
    calls=[]
    class Socket:
        def __enter__(self):return self
        def __exit__(self,*a):pass
    monkeypatch.setattr(DIAG.socket,'create_connection',lambda *a,**k:Socket())
    def run(command,stdout,stderr,timeout,**kwargs):
        calls.append(command)
        assert 0<timeout<=20
        stdout.write(b'device evidence')
        return NS(returncode=0)
    monkeypatch.setattr(DIAG.subprocess,'run',run)
    result=DIAG.collect(str(directory),include_device_logs=True)
    assert [c[3:] for c in calls]==[['get-state'],['shell','ps','-A'],['logcat','-d','-b','crash','-t','2000']]
    assert all(f['size_bytes']<=DIAG.LIMIT for f in result['files'])
    guard,ctx=make_guard(tmp_path,monkeypatch)
    try:
        handler=guard.logger.handlers[0]
        assert handler.maxBytes==10*1024*1024 and handler.backupCount==2
    finally:guard.dispose()

def test_diagnostics_device_timeout_keeps_local_bundle(tmp_path,monkeypatch):
    directory=tmp_path/'diagnostics';directory.mkdir();adb=tmp_path/'adb.exe';adb.write_bytes(b'placeholder')
    (directory/'current.json').write_text(json.dumps({'remote_host':'adb://device','adb_path':str(adb)}))
    class Socket:
        def __enter__(self):return self
        def __exit__(self,*a):pass
    monkeypatch.setattr(DIAG.socket,'create_connection',lambda *a,**k:Socket())
    def timeout(*args,**kwargs):raise DIAG.subprocess.TimeoutExpired(args[0],20)
    monkeypatch.setattr(DIAG.subprocess,'run',timeout)
    result=DIAG.collect(str(directory),include_device_logs=True)
    assert Path(result['manifest_path']).exists() and any('device_unavailable' in w for w in result['warnings'])


def test_mismatched_contract_and_package_versions_are_rejected_before_queries():
    calls=[]
    facade=NS(runtime_info={'api_contract_version':3,'extension_version':'3.0.0'},
              get_capture_status=lambda probe_replay=True:calls.append('called') or {})
    # Supply method placeholders only for handler construction; queried method is real.
    class Facade:
        _guard = None
        _jobs = None
        runtime_info=facade.runtime_info
        def __getattr__(self,name):
            return facade.get_capture_status if name=='get_capture_status' else lambda **kwargs:None
    handler=pipeline.HANDLER.RequestHandler(Facade())
    for request in [{'api_contract_version':2,'server_version':'3.0.0'},
                    {'api_contract_version':3,'server_version':'2.0.0'}]:
        result=handler.handle(dict(request,id='request',method='get_capture_status',params={}))
        assert 'API_VERSION_MISMATCH' in result['error']['message']
    assert not calls


def test_unverified_api_preserves_opaque_bytes_but_refuses_selection():
    data,meta,_,_=select(b'\0\0',fmt('D16'),1,1,1,verified_api=False)
    assert data==b'\0\0' and not meta['layout_available'] and meta['coordinate_origin'] is None
    with pytest.raises(ValueError,match='UNSUPPORTED_FORMAT'):
        select(b'\0\0',fmt('D16'),1,1,1,'depth',verified_api=False)


def test_constant_dedup_checks_existing_content(tmp_path):
    exports=v2.CONSTANT_EXPORT
    row={'status':'exported','binding_key':'binding','stage':'fragment','_raw':b'original'}
    result=exports.write_constants(str(tmp_path),[row],{'capture_session':'old'},'event')
    Path(result[0]['raw']['path']).write_bytes(b'corrupt')
    with pytest.raises(RuntimeError,match='ARTIFACT_HASH_MISMATCH'):
        exports.write_constants(str(tmp_path),[row],{'capture_session':'old'},'event')
