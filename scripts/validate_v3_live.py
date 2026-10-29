"""Standard MCP stdio smoke scenario for the Snqx frame3369 Vulkan capture.

Reopens only the explicitly supplied capture/host. No shader edits or device faults.
Large evidence stays on disk; all RenderDoc reads go through published MCP tools.
"""
import argparse
import asyncio
import base64
import hashlib
import json
from pathlib import Path
import struct
import time
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

SHA = '63fc25ea89e49706a452469bae970b1063526f1f4b93ecf67f4049d2d42eccbb'

async def validate(args):
    root = Path(args.output_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    report = {'capture': args.capture, 'host': args.host, 'checks': {}}
    async with Client(StdioTransport(command='renderdoc-mcp', args=[],
                      env={'FASTMCP_SHOW_SERVER_BANNER':'false'}), timeout=180) as client:
        async def call(tool, params=None, key=None):
            started = time.monotonic()
            try:
                result = (await client.call_tool(tool, params or {})).data
            except Exception as exc:
                record = {'tool':tool, 'parameters':params, 'error':str(exc), 'elapsed_seconds':time.monotonic()-started}
                (root/(key or tool+'.error')).with_suffix('.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
                raise
            record = {'tool':tool, 'parameters':params, 'data':result, 'elapsed_seconds':time.monotonic()-started}
            (root/((key or tool)+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
            print(key or tool, 'ok', flush=True)
            return result

        async def job(tool, params, key):
            result = await call(tool, params, key+'_submitted')
            job_id = result['job_id']
            for _ in range(240):
                status = await call('get_job_status', {'job_id':job_id,'limit':1}, key+'_status')
                if status['status'] in ('completed','completed_with_errors','failed','interrupted','cancelled','paused'):
                    assert status['status']=='completed', status
                    return status
                await asyncio.sleep(.5)
            raise RuntimeError('live job still pending: '+job_id)

        tools = await client.list_tools()
        report['checks']['tool_count'] = len(tools)
        initial = await call('get_capture_status',key='initial_status')
        assert initial['extension_version']=='3.1.0' and initial['api_contract_version']==3
        assert initial['ipc_version']==2
        opened = await job('open_capture',{'capture_path':args.capture,'replay_target':'remote','remote_host':args.host},'open')
        assert opened['result']['capture_sha256']==SHA, 'this scenario requires the exact Snqx frame3369 capture'
        before = await call('get_capture_status',key='before')
        assert before['replay_healthy'] and before['remote_replay'] and 'Vulkan' in before['api']
        replacements = await call('list_shader_replacements',key='replacements_before')
        assert replacements['capture_session']==before['capture_session']
        report['checks']['shared_session'] = True

        batch = await job('dump_draws',{'output_dir':str(root/'draws'),'action_event_ids':[1922,1930],
                           'export_textures':False},'draws')
        details = json.loads(Path(batch['items'][0]['details_path']).read_text(encoding='utf-8'))
        assert details['constants'] and all(r['status']!='failed' for r in details['constants'])
        constant = next(r for r in details['constants'] if r['status']=='exported' and 'raw' in r)
        meta = json.loads(Path(constant['details_path']).read_text(encoding='utf-8'))
        raw = await call('get_buffer_contents',{'resource_id':meta['resource']['resource_id'],
              'action_event_id':meta['action_event_id'],'offset':meta['byte_offset'],'length':meta['byte_size']},'constant_independent_range')
        assert base64.b64decode(raw['content_base64'])==Path(meta['raw']['path']).read_bytes()
        report['checks']['constant_exact_range'] = True

        shader = await job('export_shader_bundle',{'action_event_id':1930,'stage':'fragment',
                    'output_dir':str(root/'shader')},'shader')
        manifest = json.loads(Path(shader['result']['manifest_path']).read_text(encoding='utf-8'))
        assert any(f['path'].endswith('event_context.json') for f in manifest['files'])
        assert manifest['constants'] and all(r['status']!='failed' for r in manifest['constants'])
        report['checks']['shader_event_context'] = True

        d16 = await call('get_texture_data',{'resource_id':'ResourceId::17571','action_event_id':218,
                      'output_dir':str(root/'textures')},'d16_auto')
        assert d16['output_mode']=='file' and 'content_base64' not in d16
        raw16 = Path(d16['path']).read_bytes()
        assert hashlib.sha256(raw16).hexdigest()==d16['sha256']
        roi = {'x':850,'y':600,'width':16,'height':16}
        depth16 = await call('get_texture_data',{'resource_id':'ResourceId::17571','action_event_id':218,
                           'aspect':'depth','region':roi},'d16_depth_roi')
        values = struct.unpack('<256f',base64.b64decode(depth16['content_base64']))
        for i,value in enumerate(values):
            offset=((roi['y']+i//16)*2048+roi['x']+i%16)*2
            assert abs(value-struct.unpack_from('<H',raw16,offset)[0]/65535)<1e-7
        report['checks']['d16_depth_roi'] = True

        raw24 = await call('get_texture_data',{'resource_id':'ResourceId::27187','action_event_id':2006,
                       'sample':0,'output_dir':str(root/'textures')},'d24_auto')
        packed = Path(raw24['path']).read_bytes()
        assert raw24['output_mode']=='file' and raw24['layout_available']
        for sample in [0,1]:
            selected = await call('get_texture_data',{'resource_id':'ResourceId::27187','action_event_id':2006,
                              'sample':sample,'aspect':'stencil','region':roi},'stencil_sample'+str(sample))
            stencil = base64.b64decode(selected['content_base64'])
            assert len(stencil)==256 and selected['sample']==sample
            if sample==0:
                for i,value in enumerate(stencil):
                    offset=((roi['y']+i//16)*1632+roi['x']+i%16)*4
                    assert value==struct.unpack_from('<I',packed,offset)[0]>>24
        report['checks']['d24_stencil_samples'] = True
        comparison = await job('compare_texture_events',{'resource_id':'ResourceId::27187',
                    'action_event_id_a':1976,'action_event_id_b':2006,'region':roi,'sample':0,
                    'aspect':'stencil','output_dir':str(root/'comparison')},'stencil_comparison')
        report['checks']['stencil_comparison'] = bool(comparison['result'])
        await call('get_replay_diagnostics',{'output_dir':str(root/'diagnostics')},'local_diagnostics')
        await call('get_replay_diagnostics',{'output_dir':str(root/'diagnostics'),'include_device_logs':True,
                   'remote_host':args.host},'device_diagnostics')
        after = await call('get_capture_status',key='after')
        after_replacements = await call('list_shader_replacements',key='replacements_after')
        assert after['replay_healthy'] and after['event_id']==before['event_id']
        assert after['capture_session']==before['capture_session']
        assert after_replacements['items']==replacements['items']
        report['checks']['event_and_replacements_restored'] = True
        report['runtime'] = after
    (root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture',required=True)
    parser.add_argument('--host',required=True)
    parser.add_argument('--output-dir',required=True)
    asyncio.run(validate(parser.parse_args()))
