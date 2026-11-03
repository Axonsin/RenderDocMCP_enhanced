"""Public MCP integration: cancel, restart/reopen, resume and verify a batch.

Run --phase prepare, reload the extension in RenderDoc, then --phase resume.
The original capture is only read; no shader edits or device fault injection.
"""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import sys
import time

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


def sha(path):
    value=hashlib.sha256()
    with open(path,'rb') as handle:
        for block in iter(lambda:handle.read(1024*1024),b''):value.update(block)
    return value.hexdigest()


async def main(args):
    output=Path(args.output_dir).resolve();output.mkdir(parents=True,exist_ok=True)
    report_path=output/'live_validation.json'
    report=json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {}
    transport=StdioTransport(command=sys.executable,args=['-m','mcp_server.server'],
        cwd=str(Path(__file__).resolve().parents[1]),env={'FASTMCP_SHOW_SERVER_BANNER':'false'})
    async with Client(transport,timeout=180) as client:
        async def call(name,**params):
            return (await client.call_tool(name,params)).data
        async def wait(job):
            deadline=time.monotonic()+600
            revision=None;last=None
            while time.monotonic()<deadline:
                state=await call('get_job_status',job_id=job['job_id'],limit=10,wait_seconds=2,after_revision=revision,wait_for='terminal')
                revision=state['status_revision']
                current=(state['status'],state['phase'])
                if current!=last:
                    print(json.dumps(dict(job_id=state['job_id'],status=current[0],phase=current[1],
                                          progress=state.get('artifact_progress'))),flush=True)
                    last=current
                if state['status'] in ('completed','completed_with_errors','paused','failed','interrupted','cancelled'):
                    return state
            raise RuntimeError('Validation deadline reached; inspect existing job before further action')
        if args.phase=='observe':
            before=report['before']
        else:
            open_params=dict(capture_path=args.capture,file_location='local',replay_target='current')
            if args.host:open_params.update(replay_target='remote',remote_host=args.host)
            opened=await wait(await call('open_capture',**open_params))
            assert opened['status']=='completed',opened
            before=await call('get_capture_status',probe_replay=True)
            assert before['api_contract_version']==4 and before['replay_healthy'],before
        if args.phase=='prepare':
            options={'hlsl_converter':args.converter}
            if args.mip_zero: options['mips']=[0]
            job=await call('dump_draws',output_dir=str(output/'export'),action_event_ids=args.events,
                max_textures=2,export_options=options)
            state=await wait(job)
            report.update(job_id=job['job_id'],prepare=state,before=before)
            report_path.write_text(json.dumps(report,indent=2),encoding='utf-8')
            assert state['status']=='paused',state
            state=await wait(await call('cancel_job',job_id=job['job_id']))
            assert state['status']=='cancelled',state
            report['cancelled']=state
        else:
            job=({'job_id':report['job_id']} if args.phase=='observe' else
                 await call('resume_job',job_id=report['job_id'],texture_budget=512))
            state=await wait(job);report['resumed']=state
            report_path.write_text(json.dumps(report,indent=2),encoding='utf-8')
            assert state['status']=='completed',state
            checkpoint=json.loads(Path(state['checkpoint_path']).read_text(encoding='utf-8'))
            verified=0
            for task in checkpoint['tasks'].values():
                for artifact in task['artifacts']:
                    assert sha(artifact['path'])==artifact['sha256'],artifact
                    verified+=1
            report['verified_artifacts']=verified
            assert state['reused_artifacts']>0,state
        health=await call('get_capture_status',probe_replay=True)
        assert health['replay_healthy'] and health['event_id']==before['event_id'],health
        report['health']=health
        report_path.write_text(json.dumps(report,indent=2),encoding='utf-8')
        print(json.dumps(dict(phase=args.phase,job_id=report['job_id'],healthy=True,
                              report=str(report_path))),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture',required=True)
    parser.add_argument('--host',default=None,help='Omit to use the current local replay context')
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--phase',choices=['prepare','resume','observe'],required=True)
    parser.add_argument('--events',nargs='+',type=int,default=[681,739])
    parser.add_argument('--converter',default=None)
    parser.add_argument('--mip-zero',action='store_true',help='Limit the live smoke test to mip 0, retaining every bound layer')
    asyncio.run(main(parser.parse_args()))
