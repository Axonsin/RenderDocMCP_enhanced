"""Durable batch integration tests, including process/session loss and corruption."""
import importlib.util
import json
from pathlib import Path
import sys
import time
import types

import pytest
import test_pipeline as pipeline
import test_v2 as v2

NS=types.SimpleNamespace
ROOT=Path(__file__).resolve().parents[1]


@pytest.fixture
def batch(tmp_path,monkeypatch):
    rd=pipeline.RD
    for name in ('renderdoc_extension','renderdoc_extension.services','renderdoc_extension.utils'):
        package=types.ModuleType(name)
        package.__path__=[str(ROOT/name.replace('.','/'))]
        monkeypatch.setitem(sys.modules,name,package)
    sys.modules['renderdoc_extension.utils'].Parsers=pipeline.MODULES['pipeline_snapshot'].Parsers
    monkeypatch.setitem(sys.modules,'renderdoc',rd)
    for name,module in dict(job_service=v2.JOBS,constant_export=v2.CONSTANT_EXPORT,
                            texture_values=v2.VALUES,**pipeline.MODULES).items():
        monkeypatch.setitem(sys.modules,'renderdoc_extension.services.'+name,module)
    def load(name):
        spec=importlib.util.spec_from_file_location('renderdoc_extension.services.'+name,
                            ROOT/'renderdoc_extension/services'/ (name+'.py'))
        module=importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules,spec.name,module)
        spec.loader.exec_module(module)
        return module
    checkpoint=load('export_checkpoint')
    load('texture_export')
    investigation=load('investigation_service')
    export=load('batch_export')
    service_module=load('batch_service')
    capture=tmp_path/'frame.rdc';capture.write_bytes(b'original capture')
    callbacks=[];calls=[]
    ctx=NS(IsCaptureLoaded=lambda:True,GetCaptureFilename=lambda:str(capture),
        APIProps=lambda:NS(pipelineType='Vulkan'),CurEvent=lambda:99,
        GetAction=lambda eid:NS(eventId=eid,flags=rd.ActionFlags.Drawcall,numInstances=2),
        Replay=lambda:NS(AsyncInvoke=callbacks.append))
    session=v2.Session();session.build_hash='testbuild';session.replacements=[]
    session.observe_replacements=lambda *args:None
    manager=v2.JOBS.JobService(ctx,session,str(tmp_path/'jobs'))
    mesh=NS()
    def capture_mesh(c,eid,stage,attrs,instance,view):
        calls.append(('mesh',eid,stage,instance))
        return (eid,stage,instance)
    def write_mesh(data,eid,path,stage,instance,view):
        Path(path).write_text(str(data));Path(path).with_suffix('.idx').write_text('0')
        return dict(success=True,output_path=path,index_path=str(Path(path).with_suffix('.idx')),stage=stage)
    mesh._capture_csv=capture_mesh;mesh.write_mesh_csv=write_mesh
    service=service_module.BatchService(ctx,None,mesh,session,manager)
    controller=NS(event=99)
    controller.SetFrameEvent=lambda e,force:setattr(controller,'event',e)
    controller.GetFatalErrorStatus=lambda:NS(OK=lambda:True)
    controller.GetAPIProperties=lambda:NS(pipelineType='Vulkan')
    def reflection(stage):
        return NS(encoding='SPIRV',rawBytes=b'spirv',resourceId=55,entryPoint='main',debugInfo=NS(files=[]),
            inputSignature=[],outputSignature=[],readOnlyResources=[],readWriteResources=[],samplers=[],constantBlocks=[])
    controller.GetPipelineState=lambda:NS(GetShaderReflection=reflection,GetGraphicsPipelineObject=lambda:66)
    controller.GetDisassemblyTargets=lambda all_targets:['SPIR-V (RenderDoc)','AMDIL']
    def disassemble(pipe,ref,target):calls.append(('shader',target));return target+' text'
    controller.DisassembleShader=disassemble
    fmt=NS(Name=lambda:'R8_UNORM',type='Regular',compType='UNorm',compByteWidth=1,compCount=1)
    tex=NS(resourceId=1,width=2,height=1,depth=1,mips=1,arraysize=6,msSamp=1,format=fmt)
    controller.GetTextures=lambda:[tex]
    def raw(rid,sub):
        calls.append(('raw',controller.event,sub.slice))
        return bytes([controller.event,sub.slice])
    controller.GetTextureData=raw
    monkeypatch.setattr(rd,'Subresource',lambda:NS(),raising=False)
    class Snapshot:
        def __init__(self,ctx,c,action,token):
            self.bindings=[]
            self.pipe=NS(GetVertexInputs=lambda:[])
            self.stages=dict(vertex={'shader':dict(resource={'resource_id':'ResourceId::55'},pipeline={'resource_id':'ResourceId::66'})},
                rasterizer={'sections':{}},framebuffer={'sections':{}})
        def texture_rows(self):
            return [dict(resource={'resource_id':'ResourceId::1'},bound=True,resource_kind='texture',roles=['input'],
                        subresources={'first_mip':0,'mip_count':1,'first_slice':2,'slice_count':2})]
    monkeypatch.setattr(export,'Snapshot',Snapshot)
    def run(key,limit=3000):
        for _ in range(limit):
            service.jobs.pump()
            if callbacks:callbacks.pop(0)(controller)
            if service.jobs.status(key)['status'] in v2.JOBS.TERMINAL|{'paused'}:break
            time.sleep(.002)
        return service.jobs.status(key)
    return NS(service=service,manager=manager,ctx=ctx,session=session,controller=controller,calls=calls,run=run,
              tmp=tmp_path,capture=capture,export=export,checkpoint=checkpoint,service_module=service_module,mesh=mesh)


def submit(b,**kw):
    args=dict(output_dir=str(b.tmp/'output'),action_event_ids=[10,20],export_constants=False,
              export_options={'texture_modes':['raw']})
    args.update(kw)
    return b.service.dump_draws(**args)['job_id']


def test_complete_batch_links_stages_shared_shaders_and_temporal_textures(batch):
    b=batch;key=submit(b);status=b.run(key)
    assert status['status']=='completed',status
    assert b.controller.event==99
    assert len([x for x in b.calls if x[0]=='shader'])==1
    assert len([x for x in b.calls if x[0]=='mesh'])==4
    assert [x for x in b.calls if x[0]=='raw']==[('raw',10,2),('raw',10,3),('raw',20,2),('raw',20,3)]
    result=json.loads(Path(status['result']['summary_path']).read_text())
    assert set(result['items'][0]['meshes'])=={'VSIn','VSOut'}
    assert result['items'][0]['shader_exports']['vertex']['shader_id']=='ResourceId::55'
    data=[r['textures'][0]['exports'][0]['path'] for r in result['items']]
    assert Path(data[0]).read_bytes()!=Path(data[1]).read_bytes()


def test_restart_reuses_hash_verified_artifacts_and_refreshes_bindings(batch):
    b=batch;key=submit(b);assert b.run(key)['status']=='completed'
    original=list(b.calls)
    b.session.generation='reopened'
    b.service.jobs=v2.JOBS.JobService(b.ctx,b.session,str(b.tmp/'jobs'))
    b.service=b.service_module.BatchService(b.ctx,None,b.mesh,b.session,b.service.jobs)
    b.service.jobs.resume(key)
    result=b.run(key)
    assert result['status']=='completed',result
    assert result['reused_artifacts']>=9
    assert b.calls==original
    assert json.loads(Path(result['result']['summary_path']).read_text())['items'][0]['provenance']['capture_session']=='reopened'


def test_corrupt_one_mesh_repairs_only_that_mesh(batch):
    b=batch;key=submit(b);status=b.run(key)
    manifest=json.loads(Path(status['result']['summary_path']).read_text())
    Path(manifest['items'][0]['meshes']['VSOut']['output_path']).write_text('corrupted')
    b.calls.clear();b.service.jobs.resume(key);result=b.run(key)
    assert result['status']=='completed',result
    assert b.calls==[('mesh',10,'VSOut',0)]


def test_capture_mismatch_refuses_resume_before_replay(batch):
    b=batch;key=submit(b);assert b.run(key)['status']=='completed'
    b.capture.write_bytes(b'different capture');b.calls.clear()
    b.service.jobs.resume(key);status=b.run(key)
    assert status['status']=='failed' and 'CHECKPOINT_CAPTURE_MISMATCH' in status['error']
    assert not b.calls


def test_texture_budget_pause_rebuild_and_resume(batch):
    b=batch;key=submit(b,max_textures=1)
    status=b.run(key);assert status['status']=='paused',status
    b.service.jobs.resume(key,texture_budget=10)
    status=b.run(key);assert status['status']=='completed',status
    assert len([x for x in b.calls if x[0]=='raw'])==4


def test_mesh_failure_does_not_discard_other_artifacts(batch):
    b=batch;capture=b.mesh._capture_csv
    def fail(c,eid,stage,*args):
        if stage=='VSOut':raise ValueError('MESH_SIGNATURE_UNAVAILABLE: no post-VS')
        return capture(c,eid,stage,*args)
    b.mesh._capture_csv=fail
    key=submit(b);status=b.run(key)
    assert status['status']=='completed_with_errors',status
    manifest=json.loads(Path(status['result']['summary_path']).read_text())
    assert all(i['shader_exports'] and i['textures'][0]['exports'] for i in manifest['items'])
    assert all(i['errors'][0]['task'].endswith(':mesh:VSOut') for i in manifest['items'])
    assert status['failures']


def test_duplicate_draws_instances_have_consistent_counts(batch):
    b=batch;key=submit(b,action_event_ids=[10,10],instances=[0,0])
    status=b.run(key)
    assert status['status']=='completed',status
    assert status['expected_items']==1
    assert status['counts']==dict(requested=2,valid_draws=1,successful=1,failed=0,skipped=1,pending=0)


def test_failed_constant_still_exports_textures(batch,monkeypatch):
    b=batch;original=b.export.Snapshot
    class Snapshot(original):
        def __init__(self,*args):
            super().__init__(*args)
            self.bindings=[dict(category='constant',binding_key='uniforms')]
    monkeypatch.setattr(b.export,'Snapshot',Snapshot)
    def fail(*args):raise RuntimeError('CONSTANT_EXPORT_FAILED: unavailable layout')
    monkeypatch.setattr(b.export,'read_constants',fail)
    key=submit(b,export_constants=True);status=b.run(key)
    assert status['status']=='completed_with_errors',status
    manifest=json.loads(Path(status['result']['summary_path']).read_text())
    assert all(i['textures'][0]['exports'] for i in manifest['items'])


def test_replay_disconnect_stops_without_recording_artifact_success(batch):
    b=batch
    def fail(*args):raise RuntimeError('REPLAY_UNHEALTHY: connection lost')
    b.mesh._capture_csv=fail
    key=submit(b);status=b.run(key)
    assert status['status']=='failed' and 'REPLAY_UNHEALTHY' in status['error']
    assert not [x for x in b.calls if x[0] in ('raw','shader')]


def test_cancel_then_reopen_resumes_from_disk(batch):
    b=batch;key=submit(b)
    # Stop at a committed mesh boundary, without leaving an in-flight native call.
    for _ in range(1000):
        b.service.jobs.pump()
        callbacks=b.ctx.Replay().AsyncInvoke.__self__
        if callbacks:callbacks.pop(0)(b.controller)
        if b.service.jobs.pending.get(key) is None and ('mesh',10,'VSIn',0) in b.calls and not b.service.jobs.inflight:
            break
        time.sleep(.002)
    b.service.jobs.cancel(key);assert b.run(key)['status']=='cancelled'
    b.session.generation='reopened'
    b.service.jobs=v2.JOBS.JobService(b.ctx,b.session,str(b.tmp/'jobs'))
    b.service=b.service_module.BatchService(b.ctx,None,b.mesh,b.session,b.service.jobs)
    b.service.jobs.resume(key);status=b.run(key)
    assert status['status']=='completed',status


@pytest.mark.parametrize('value',[{'mips':[]},{'samples':[-1]},{'shader_stages':['bogus']},{'unknown':True}])
def test_invalid_options_rejected_before_submission(batch,value):
    with pytest.raises(ValueError):submit(batch,export_options=value)


def test_worker_tool_arguments_preserve_spaces_quotes_and_backslashes(batch):
    script=batch.tmp/'tool with spaces.py'
    output=batch.tmp/'output with spaces.json'
    script.write_text('import sys,json;open(sys.argv[1],"w").write(json.dumps(sys.argv[2:]))')
    arguments=['a b','a"b','tail slash \\','unicode 渲染']
    assert batch.export.spawn([sys.executable,str(script),str(output)]+arguments)==0
    assert json.loads(output.read_text())==arguments


def test_build_mismatch_refuses_reuse(batch):
    b=batch;key=submit(b);assert b.run(key)['status']=='completed'
    b.session.build_hash='changed build';b.calls.clear()
    b.service.jobs.resume(key);state=b.run(key)
    assert state['status']=='failed' and 'CHECKPOINT_CAPTURE_MISMATCH' in state['error']
    assert not b.calls


def test_changed_plan_options_are_rejected(batch):
    b=batch;key=submit(b);assert b.run(key)['status']=='completed'
    b.service.jobs.records[key]['parameters']['export_options']['mips']=[0]
    with pytest.raises(ValueError,match='CHECKPOINT_PLAN_MISMATCH'):b.service.jobs.resume(key)


def test_modified_replay_cannot_create_durable_export(batch):
    b=batch;b.session.replacements=[(1,99)]
    key=submit(b);state=b.run(key)
    assert state['status']=='failed' and 'CHECKPOINT_REPLAY_MODIFIED' in state['error']
    assert not b.calls


def test_raw_multi_mip_selection_retains_indices_and_sizes(batch):
    b=batch;b.controller.GetTextures()[0].mips=2
    b.controller.GetTextureData=lambda rid,sub:b'\x01\x02' if sub.mip==0 else b'\x03'
    key=submit(b,action_event_ids=[10],export_options=dict(shader_stages=[],mesh_stages=[],
                           texture_modes=['raw'],mips='all',slices=[0]))
    state=b.run(key);assert state['status']=='completed',state
    item=json.loads(Path(state['result']['summary_path']).read_text())['items'][0]
    rows=item['textures'][0]['exports']
    assert [r['mip'] for r in rows]==[0,1]
    assert [len(Path(r['path']).read_bytes()) for r in rows]==[2,1]


def test_preview_format_uses_native_save_without_numeric_claims(batch,monkeypatch):
    b=batch;rd=b.export.rd
    monkeypatch.setattr(rd,'TextureSave',lambda:NS(slice=NS(),sample=NS()),raising=False)
    monkeypatch.setattr(rd,'FileType',NS(EXR='EXR'),raising=False)
    monkeypatch.setattr(rd,'AlphaMapping',NS(Preserve='Preserve'),raising=False)
    def save(config,path):
        assert config.destType=='EXR' and config.slice.sliceIndex==0
        Path(path).write_bytes(b'preview conversion')
        return NS(OK=lambda:True)
    b.controller.SaveTexture=save
    key=submit(b,action_event_ids=[10],export_options=dict(shader_stages=[],mesh_stages=[],
                texture_modes=['preview'],preview_format='EXR',slices=[0],mips=[0]))
    state=b.run(key);assert state['status']=='completed',state
    item=json.loads(Path(state['result']['summary_path']).read_text())['items'][0]
    row=item['textures'][0]['exports'][0]
    assert row['export_format']=='EXR' and row['output_value_domain']=='RenderDoc_SaveTexture_conversion'


def test_shader_cache_respects_pipeline_specialization(batch,monkeypatch):
    b=batch;original=b.export.Snapshot
    class Snapshot(original):
        def __init__(self,ctx,c,action,token):
            super().__init__(ctx,c,action,token)
            self.stages['vertex']['shader']['pipeline']['resource_id']='ResourceId::'+str(action.eventId)
    monkeypatch.setattr(b.export,'Snapshot',Snapshot)
    key=submit(b,export_options=dict(mesh_stages=[],texture_modes=[]));state=b.run(key)
    assert state['status']=='completed',state
    assert len([c for c in b.calls if c[0]=='shader'])==2
