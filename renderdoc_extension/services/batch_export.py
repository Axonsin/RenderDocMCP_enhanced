"""Complete evidence export with durable artifact checkpoints. Python 3.6."""
import copy
import json
import os
import time
import uuid

import renderdoc as rd

from ..utils import Parsers
from .constant_export import read_constants, write_constants
from .export_checkpoint import ExportCheckpoint, digest
from .investigation_service import InvestigationService
from .job_service import atomic_json, PauseJob
from .pipeline_snapshot import Snapshot, plain
from .replay_query import at_event, require_action
from .texture_export import select, transport
from .texture_values import snapshot_format, MAX_SUBRESOURCE_BYTES, decoder


def paths(value):
    result = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ('path', 'output_path', 'index_path', 'details_path', 'metadata_path',
                       'manifest_path', 'original') and isinstance(item, str):
                result.append(item)
            else:
                result.extend(paths(item))
    elif isinstance(value, list):
        for item in value:
            result.extend(paths(item))
    return list(dict.fromkeys(result))


def options(value):
    if not isinstance(value, dict):
        raise ValueError('INVALID_REQUEST: export_options must be an object')
    defaults = dict(mesh_stages=['VSIn', 'VSOut'], shader_stages=['vertex', 'fragment'],
                    disassembly_targets=['default'], texture_modes=['preview', 'raw'],
                    preview_format='PNG', mips='bound', slices='bound', samples=[0],
                    aspects=['all'], hlsl_converter=None)
    if set(value) - set(defaults):
        raise ValueError('INVALID_REQUEST: unknown export_options fields')
    defaults.update(value)
    for key, allowed in (('mesh_stages', ('VSIn','VSOut','GSOut')),
                         ('texture_modes', ('preview','raw')), ('aspects', ('all','depth','stencil'))):
        if not isinstance(defaults[key], list) or any(x not in allowed for x in defaults[key]):
            raise ValueError('INVALID_REQUEST: invalid '+key)
        defaults[key] = list(dict.fromkeys(defaults[key]))
    if not isinstance(defaults['shader_stages'], list):
        raise ValueError('INVALID_REQUEST: shader_stages must be a list')
    defaults['shader_stages'] = list(dict.fromkeys(Parsers.parse_stage_name(s) for s in defaults['shader_stages']))
    targets = defaults['disassembly_targets']
    if targets is not None and (not isinstance(targets, list) or any(not isinstance(t,str) or not t for t in targets)):
        raise ValueError('INVALID_REQUEST: invalid disassembly_targets')
    for key in ('mips','slices','samples'):
        v = defaults[key]
        valid = v in ('bound','all') if isinstance(v,str) else (
                isinstance(v,list) and v and all(type(i) is int and i >= 0 for i in v))
        if not valid:
            raise ValueError('INVALID_REQUEST: '+key+' must be bound, all, or nonnegative indices')
    if defaults['preview_format'] not in ('PNG','EXR','DDS'):
        raise ValueError('INVALID_REQUEST: preview_format must be PNG, EXR or DDS')
    converter = defaults['hlsl_converter']
    if converter is not None and (not isinstance(converter,str) or not os.path.isabs(converter) or not os.path.isfile(converter)):
        raise ValueError('INVALID_REQUEST: hlsl_converter must name an installed SPIRV-Cross executable')
    return defaults


class BatchExport:
    def __init__(self, batch):
        self.batch = batch
        self.ctx, self.session, self.jobs = batch.ctx, batch.session, batch.jobs

    def submit(self, params):
        selected, skipped = self.batch._select(params['action_event_ids'], params['marker_filter'], params['action_event_id_range'])
        opts = options(params['export_options'])
        instances = [0] if params['instances'] is None else params['instances']
        if not isinstance(instances,list) or not instances or any(type(i) is not int or i < 0 for i in instances):
            raise ValueError('INVALID_INSTANCE: expected nonnegative instance indices')
        instances = sorted(set(instances))
        if type(params['view_index']) is not int or params['view_index'] < 0:
            raise ValueError('INVALID_VIEW_INDEX: expected nonnegative view')
        for eid in selected:
            if any(i >= max(1,require_action(self.ctx,eid).numInstances) for i in instances):
                raise ValueError('INVALID_INSTANCE: instance exceeds draw '+str(eid))
        for field in ('export_constants','skip_depth'):
            if type(params[field]) is not bool:
                raise ValueError('INVALID_REQUEST: '+field+' must be boolean')
        if type(params['max_textures']) is not int or params['max_textures'] < 1:
            raise ValueError('INVALID_REQUEST: max_textures must be positive')
        if params['max_texture_edge'] is not None and (type(params['max_texture_edge']) is not int or params['max_texture_edge'] < 1):
            raise ValueError('INVALID_REQUEST: max_texture_edge must be positive')
        if not isinstance(params['output_dir'],str) or not os.path.isabs(params['output_dir']):
            raise ValueError('INVALID_OUTPUT_PATH: absolute output_dir required')
        params = dict(params, instances=instances, export_options=opts)
        plan = dict(version=1, parameters=params, selected=selected, skipped=skipped,
                    requested=len(params['action_event_ids'] or selected))
        return self.jobs.submit('dump_draws', params, lambda key:self.steps(key,plan), params.get('job_id'))

    def recover(self, record):
        with open(record['durable_plan'],encoding='utf-8') as handle:
            plan = json.load(handle)
        if plan.get('version') != 1 or plan['parameters'] != record['parameters']:
            raise ValueError('CHECKPOINT_PLAN_MISMATCH: export parameters changed')
        return self.steps(record['job_id'],plan,True)

    def steps(self, key, plan, recovering=False):
        p = plan['parameters']
        opts = p['export_options']
        directory = os.path.join(p['output_dir'], key)
        os.makedirs(directory,exist_ok=True)
        self.session.observe_replacements()
        # Replacement IDs cannot identify edited shader contents across sessions.
        # Durable exports currently require original replay, verified on UI.
        if any(target not in (0,source) for source,target in (self.session.replacements or [])):
            raise ValueError('CHECKPOINT_REPLAY_MODIFIED: revert shader replacements before exporting')
        filename = self.ctx.GetCaptureFilename()
        api = str(self.ctx.APIProps().pipelineType)
        state = {}
        def identity(_):
            if not os.path.isfile(filename):
                raise ValueError('CAPTURE_IDENTITY_UNAVAILABLE: retain a local RDC copy for durable export')
            current = dict(capture_sha256=digest(filename), api=api, replay='original',
                           extension_build=self.session.build_hash,
                           converter_sha256=digest(opts['hlsl_converter']) if opts['hlsl_converter'] else None)
            if recovering and current != plan['identity']:
                raise ValueError('CHECKPOINT_CAPTURE_MISMATCH: capture, replay, converter or extension differs')
            plan['identity'] = current
            plan_path = os.path.join(directory,'plan.json')
            atomic_json(plan_path,plan)
            state['checkpoint'] = ExportCheckpoint(directory)
            return dict(durable_plan=plan_path, output_dir=directory, checkpoint_path=state['checkpoint'].path,
                        requested_count=plan['requested'], draw_count=len(plan['selected']),
                        skipped_count=plan['skipped'], expected_items=len(plan['selected'])*len(p['instances']),
                        items=[], result=None, reused_artifacts=0,
                        artifact_progress=dict(visited=0,completed=0,reused=0,failed=0),
                        texture_budget=self.jobs.records[key]['texture_budget'] if recovering else p['max_textures'])
        yield ('worker','verify_export_identity',identity)
        checkpoint = state['checkpoint']
        timing_path = os.path.join(directory,'stages.jsonl')

        def task(task_key, factory, refresh=False):
            box = {}
            def verify(_):
                box['result'] = None if refresh else checkpoint.restore(task_key)
                progress = dict(self.jobs.records[key]['artifact_progress'])
                progress['visited'] += 1
                if box['result'] is not None:
                    progress['completed'] += 1
                    progress['reused'] += 1
                self.jobs.update(key,artifact_progress=progress,reused_artifacts=progress['reused'])
                return {'item':entry}
            yield ('worker','verify:'+task_key,verify)
            if box['result'] is not None:
                return box['result']
            for kind, phase, function in factory():
                def execute(controller, function=function, phase=phase):
                    start = time.time()
                    outcome = 'completed'
                    failure = None
                    try:
                        output = function(controller) or {}
                        if 'result' in output:
                            box['result'] = output['result']
                    except Exception as exc:
                        outcome = 'paused' if isinstance(exc,PauseJob) else 'failed'
                        failure = str(exc)[:2048]
                        if self._fatal(exc): raise
                        box['error'] = exc
                        entry.setdefault('errors',[]).append(dict(task=task_key,phase=phase,error=failure))
                        progress = dict(self.jobs.records[key]['artifact_progress'])
                        progress['failed'] += 1
                        self.jobs.update(key,artifact_progress=progress)
                    finally:
                        # The journal is small, flushed at every boundary.
                        with open(timing_path,'a',encoding='utf-8') as handle:
                            handle.write(json.dumps(dict(task=task_key,phase=phase,started_at=start,
                                                status=outcome,error=failure,elapsed_seconds=time.time()-start))+'\n')
                    return {}
                yield (kind,phase,execute)
                if 'error' in box: raise box['error']
            def commit(_):
                result = box.get('result')
                if result is None:
                    raise RuntimeError('EXPORT_INCOMPLETE: task produced no artifact result')
                checkpoint.complete(task_key,result,paths(result))
                progress = dict(self.jobs.records[key]['artifact_progress'])
                progress['completed'] += 1
                self.jobs.update(key,artifact_progress=progress)
            yield ('worker','checkpoint:'+task_key,commit)
            return box['result']

        def scoped(eid,operation):
            return lambda c: at_event(self.ctx,lambda fn:fn(c),eid,operation)

        shader_cache = {}
        texture_cache = {}
        for eid in plan['selected']:
            for instance in p['instances']:
                self.jobs.update(key,current_event_id=eid,current_instance=instance,current_resource_id=None)
                prefix = 'e%d:i%d' % (eid,instance)
                entry = dict(item_key=prefix,action_event_id=eid,instance=instance,view_index=p['view_index'],
                             complete=False,ok=True,meshes={},shader_exports={},textures=[],constants=[])
                def publish(_,entry=entry):
                    return {'item':entry}
                yield ('worker','begin:'+prefix,publish)
                # Binding IDs are always freshly acquired, including after restart.
                def facts(c,event):
                    snap = Snapshot(self.ctx,c,require_action(self.ctx,event),self.session.token())
                    result = dict(provenance=self.session.describe(),bindings=copy.deepcopy(snap.bindings),
                        vertex_inputs=plain(snap.pipe.GetVertexInputs()),
                        shaders={s:v['shader'] for s,v in snap.stages.items() if v.get('shader')},
                        fixed_state={s:copy.deepcopy(snap.stages[s]) for s in ('rasterizer','framebuffer')},
                        textures=[copy.deepcopy(r) for r in snap.texture_rows() if r.get('bound') and
                                  r.get('resource_kind')=='texture' and 'input' in r.get('roles',[])])
                    issues=[section.get('reason') for stage in result['fixed_state'].values()
                            for section in stage.get('sections',{}).values() if section.get('available') is False]
                    result.update(warnings=issues,serialization_complete=not issues)
                    return {'result':result}
                def fact_steps():
                    yield ('replay','bindings:'+prefix,scoped(eid,facts))
                try:
                    data = yield from task(prefix+':bindings',fact_steps,True)
                    entry.update(data)
                except Exception:
                    raise  # No continuation after replay loss or invalid bindings.

                # Each constant binding is read on replay separately, written off replay.
                if p['export_constants']:
                    for index,row in enumerate(r for r in entry['bindings'] if r['category']=='constant'):
                        payload = {}
                        def constant_steps(row=row,index=index):
                            def read(c,event):
                                snap = Snapshot(self.ctx,c,require_action(self.ctx,event),self.session.token())
                                snap.bindings = [r for r in snap.bindings if r['binding_key']==row['binding_key']]
                                payload['records'] = read_constants(snap)
                            yield ('replay','constant_read:'+prefix+':'+str(index),scoped(eid,read))
                            def write(_):
                                records = write_constants(directory,payload.pop('records'),entry['provenance'],
                                    prefix.replace(':','_')+'_c'+str(index),repair_corrupt=True)
                                if any(r['status']=='failed' for r in records):
                                    raise RuntimeError('CONSTANT_EXPORT_FAILED: '+str(records))
                                return {'result':{'constants':records}}
                            yield ('worker','constant_write:'+prefix+':'+str(index),write)
                        try:
                            result = yield from task(prefix+':constant:'+str(index),constant_steps)
                            entry['constants'].extend(result['constants'])
                        except Exception as exc:
                            if self._fatal(exc): raise
                            entry.update(ok=False,error=str(exc))

                if opts['mesh_stages']:
                    for stage in opts['mesh_stages']:
                        payload = {}
                        def mesh_steps(stage=stage):
                            def read(c,event):
                                payload['mesh'] = self.batch._mesh._capture_csv(c,event,stage,None,instance,
                                                            0 if stage=='VSIn' else p['view_index'])
                            yield ('replay','mesh_read:'+prefix+':'+stage,scoped(eid,read))
                            def write(_):
                                path = os.path.join(directory,prefix.replace(':','_')+'_'+stage+'.csv')
                                result = self.batch._mesh.write_mesh_csv(payload.pop('mesh'),eid,path,stage,instance,
                                                                       0 if stage=='VSIn' else p['view_index'])
                                return {'result':result}
                            yield ('worker','mesh_write:'+prefix+':'+stage,write)
                        try:
                            entry['meshes'][stage] = yield from task(prefix+':mesh:'+stage,mesh_steps)
                        except Exception as exc:
                            if self._fatal(exc): raise
                            entry.update(ok=False,error=str(exc))

                investigation = InvestigationService(self.ctx,self.session,self.jobs)
                for stage in opts['shader_stages']:
                    shader = entry['shaders'].get(stage)
                    if not shader: continue
                    shader_id = shader['resource']['resource_id']
                    # Include pipeline and stage: hardware disassembly may depend
                    # on the pipeline specialization even for shared shader bytes.
                    shader_key = stage+':'+shader_id+':'+shader.get('pipeline',{}).get('resource_id','none')
                    try:
                        if shader_key not in shader_cache:
                            name = 'shader_'+digest_text(shader_key)[:20]
                            factory = investigation.shader_steps(eid,stage,directory,False,False,opts['disassembly_targets'])
                            shader_cache[shader_key] = yield from task(shader_key,lambda:factory(name))
                        entry['shader_exports'][stage] = shader_cache[shader_key]
                        if opts['hlsl_converter']:
                            shader_result = shader_cache[shader_key]
                            def hlsl_steps():
                                def convert(_):
                                    if shader_result['encoding'] not in ('SPIRV','OpenGLSPIRV'):
                                        raise ValueError('HLSL_CONVERSION_UNAVAILABLE: shader is not SPIR-V')
                                    path = os.path.join(os.path.dirname(shader_result['original']),'converted.hlsl')
                                    temporary = path+'.'+uuid.uuid4().hex+'.tmp'
                                    args = [opts['hlsl_converter'],shader_result['original'],'--hlsl','--shader-model','50','--output',temporary]
                                    try:
                                        if spawn(args) != 0 or not os.path.isfile(temporary):
                                            raise RuntimeError('HLSL_CONVERSION_FAILED: SPIRV-Cross failed')
                                        os.replace(temporary,path)
                                    finally:
                                        if os.path.isfile(temporary): os.remove(temporary)
                                    args[-1] = path
                                    return {'result':dict(path=path,converter=opts['hlsl_converter'],
                                        converter_sha256=plan['identity']['converter_sha256'],arguments=args[2:])}
                                yield ('worker','hlsl:'+shader_key,convert)
                            entry['shader_exports'][stage] = dict(shader_result,hlsl=(yield from task(shader_key+':hlsl',hlsl_steps)))
                    except Exception as exc:
                        if self._fatal(exc): raise
                        entry.update(ok=False,error=str(exc))

                if opts['texture_modes']:
                    for row in entry['textures']:
                        rid = row['resource']['resource_id']
                        self.jobs.update(key,current_resource_id=rid)
                        meta = {}
                        def texture_meta(c,event):
                            td = next(t for t in c.GetTextures() if int(t.resourceId)==int(rid.split('::')[-1]))
                            meta.update(width=td.width,height=td.height,depth=td.depth,mips=td.mips,
                                slices=td.arraysize,samples=max(1,td.msSamp),format=str(td.format.Name()))
                        yield ('replay','texture_metadata:'+str(eid)+':'+rid,scoped(eid,texture_meta))
                        if p['max_texture_edge'] and max(meta['width'],meta['height']) > p['max_texture_edge']:
                            row['export'] = {'skipped':'max_texture_edge'}
                            continue
                        if p['skip_depth'] and ('D16' in meta['format'] or 'D24' in meta['format'] or 'D32' in meta['format']):
                            row['export'] = {'skipped':'depth_filter'}
                            continue
                        sub = row.get('subresources') or {}
                        row['exports'] = []
                        for mip in indices(opts['mips'],meta['mips'],sub.get('first_mip') or 0,sub.get('mip_count')):
                            for layer in indices(opts['slices'],meta['slices'],sub.get('first_slice') or 0,sub.get('slice_count')):
                                for sample in indices(opts['samples'],meta['samples'],0):
                                    for mode in opts['texture_modes']:
                                        for aspect in opts['aspects'] if mode=='raw' else ['all']:
                                            texture_key = 'e%d:%s:m%d:s%d:a%d:%s:%s' % (eid,rid,mip,layer,sample,mode,aspect)
                                            try:
                                                if texture_key not in texture_cache:
                                                    def texture_steps():
                                                        payload = {}
                                                        def read(c,event):
                                                            td = next(t for t in c.GetTextures() if int(t.resourceId)==int(rid.split('::')[-1]))
                                                            stem = os.path.join(directory,'tex_'+digest_text(texture_key)[:24])
                                                            common = dict(resource_id=rid,action_event_id=eid,event_phase='after',mip=mip,
                                                                slice_index=layer,sample=sample,depth=max(1,td.depth>>mip),
                                                                width=max(1,td.width>>mip),height=max(1,td.height>>mip),format=str(td.format.Name()),
                                                                source_color_space='srgb' if str(td.format.compType).split('.')[-1]=='UNormSRGB' else 'linear')
                                                            if mode=='preview':
                                                                if td.depth > 1:
                                                                    raise ValueError('PREVIEW_UNAVAILABLE: use raw for volume textures')
                                                                config = rd.TextureSave()
                                                                config.resourceId=td.resourceId
                                                                config.mip=mip
                                                                config.slice.sliceIndex=layer
                                                                config.sample.sampleIndex=sample
                                                                config.destType=getattr(rd.FileType,opts['preview_format'])
                                                                config.alpha=rd.AlphaMapping.Preserve
                                                                path=stem+'.'+opts['preview_format'].lower()
                                                                outcome=c.SaveTexture(config,path)
                                                                if not outcome.OK(): raise RuntimeError('TEXTURE_SAVE_FAILED: '+str(outcome.Message()))
                                                                payload['result']=dict(common,path=path,export_format=opts['preview_format'],
                                                                    output_value_domain='RenderDoc_SaveTexture_conversion')
                                                            else:
                                                                fmt=snapshot_format(td.format)
                                                                try:
                                                                    size=decoder(fmt)[0]
                                                                    if common['width']*common['height']*common['depth']*size > MAX_SUBRESOURCE_BYTES:
                                                                        raise ValueError('RESOURCE_LIMIT: raw subresource exceeds 64 MiB')
                                                                except ValueError as exc:
                                                                    if str(exc).startswith('RESOURCE_LIMIT:'): raise
                                                                subresource=rd.Subresource()
                                                                subresource.mip=mip; subresource.slice=layer; subresource.sample=sample
                                                                raw=bytes(c.GetTextureData(td.resourceId,subresource))
                                                                if not raw or len(raw)>MAX_SUBRESOURCE_BYTES: raise ValueError('RESOURCE_LIMIT: empty or oversized raw texture')
                                                                payload.update(raw=raw,fmt=fmt,common=common,
                                                                    api=str(c.GetAPIProperties().pipelineType).split('.')[-1])
                                                        def read_scoped(c):
                                                            if self.jobs.records[key]['texture_budget'] <= 0:
                                                                raise PauseJob('TEXTURE_BUDGET: resume_job supplies more texture allowance')
                                                            return scoped(eid,read)(c)
                                                        yield ('replay','texture_read:'+texture_key,read_scoped)
                                                        def write(_):
                                                            if 'raw' in payload:
                                                                common=payload['common']
                                                                raw,layout,w,h=select(payload.pop('raw'),payload['fmt'],common['width'],common['height'],
                                                                    common['depth'],aspect,None,payload['api'] in ('Vulkan','D3D11','D3D12'))
                                                                common.update(layout,width=w,height=h,api=payload['api'])
                                                                payload['result']=transport(raw,common,'file',directory,'textures')
                                                            record=self.jobs.records[key]
                                                            self.jobs.update(key,texture_budget=record['texture_budget']-1)
                                                            return {'result':payload['result']}
                                                        yield ('worker','texture_write:'+texture_key,write)
                                                    texture_cache[texture_key] = yield from task(texture_key,texture_steps)
                                                row['exports'].append(texture_cache[texture_key])
                                            except PauseJob: raise
                                            except Exception as exc:
                                                if self._fatal(exc): raise
                                                entry.update(ok=False,error=str(exc))
                                                row['exports'].append(dict(error=str(exc),mip=mip,slice_index=layer,sample=sample,mode=mode,aspect=aspect))
                        if row['exports']: row['export']=row['exports'][0]
                entry['complete']=True
                yield ('worker','complete:'+prefix,publish)
        def finish(_):
            items=self.jobs.records[key]['items']
            manifest=os.path.join(directory,'manifest.json')
            result=dict(plan_path=os.path.join(directory,'plan.json'),checkpoint_path=checkpoint.path,
                        timings_path=timing_path,provenance=self.session.describe(),identity=plan['identity'],
                        draw_count=len(plan['selected']),item_count=len(items),
                        ok_count=sum(i['ok'] for i in items),failed_count=sum(not i['ok'] for i in items))
            atomic_json(manifest,dict(result,items=items))
            return {'result':dict(result,summary_path=manifest)}
        yield ('worker','writing_manifest',finish)

    @staticmethod
    def _fatal(exc):
        return isinstance(exc,PauseJob) or any(s in str(exc) for s in
            ('REPLAY_UNHEALTHY','REPLAY_RESTORE_FAILED','REMOTE_CONNECTION_LOST','STALE_JOB'))


def digest_text(value):
    import hashlib
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def windows_argument(value):
    """MS CRT argv quoting; os.spawnv does not escape whitespace on Windows."""
    output='"'
    backslashes=0
    for char in value:
        if char=='\\':
            backslashes+=1
            continue
        output+='\\'*(2*backslashes+1)+'"' if char=='"' else '\\'*backslashes+char
        backslashes=0
    return output+'\\'*(2*backslashes)+'"'


def spawn(arguments):
    args=[windows_argument(a) for a in arguments] if os.name=='nt' else arguments
    return os.spawnv(os.P_WAIT,arguments[0],args)


def indices(selection,total,first,count=None):
    result = (list(range(total)) if selection=='all' else
              list(range(first,min(total,first+(count or 1)))) if selection=='bound' else selection)
    if not result or any(type(i) is not int or i < 0 or i >= total for i in result):
        raise ValueError('INVALID_SUBRESOURCE: selected mip, slice or sample is out of range')
    return list(dict.fromkeys(result))
