"""Report observed call log distributions; missing retry/cost/token data stays unknown."""
import argparse,collections,csv,json,pathlib,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from benchmark import prepare_report_directory,md

def summarize(path):
    calls=[];malformed=[]
    for n,line in enumerate(pathlib.Path(path).read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():continue
        try:r=json.loads(line)
        except json.JSONDecodeError:malformed.append(n);continue
        if not isinstance(r,dict):malformed.append(n);continue
        if r.get('event')=='tool_call' or 'method' in r:
            duration=r.get('duration_s',r.get('elapsed_seconds'))
            duration=duration if isinstance(duration,(int,float)) and not isinstance(duration,bool) and math.isfinite(duration) and duration>=0 else None
            status=r.get('success') if type(r.get('success')) is bool else (r.get('status')=='success' if r.get('status') in ('success','error') else None)
            calls.append({'tool':r.get('tool',r.get('method','unknown')),'duration_s':duration,'success':status,'retry':r.get('retry') if type(r.get('retry')) is bool else None})
    return {'observed_calls':len(calls),'explicit_errors':sum(x['success'] is False for x in calls),'unknown_outcomes':sum(x['success'] is None for x in calls),
       'explicit_retries':sum(x['retry'] is True for x in calls) if calls and all(x['retry'] is not None for x in calls) else None,
       'observed_retry_events':sum(x['retry'] is True for x in calls),'unknown_retry_outcomes':sum(x['retry'] is None for x in calls),
       'retry_observations':sum(x['retry'] is not None for x in calls),'malformed_lines':malformed,'calls':calls,
       'scope':'Observed log entries only; transport success does not prove semantic/tool success. Retries are never inferred from repeating the same method. No total model time/cost/token counts inferred.'}

def report(path,out,run_id,actor):
    data=summarize(path);data.update(run_id=run_id,actor=actor);out=prepare_report_directory(out);assets=out/'assets';assets.mkdir(exist_ok=True);charts=[]
    counts=collections.Counter(x['tool'] for x in data['calls'])
    if counts:
        rows=counts.most_common();fig,ax=plt.subplots(figsize=(10,max(4,.35*len(rows))));ax.barh([x[0] for x in rows][::-1],[x[1] for x in rows][::-1]);ax.set(xlabel='Observed calls (count)',title=f'{run_id} / {actor} | n={data["observed_calls"]}');fig.tight_layout();fig.savefig(assets/'tool-calls.png',dpi=150);plt.close(fig);charts.append('tool-calls.png')
    durations=[x['duration_s'] for x in data['calls'] if x['duration_s'] is not None]
    if durations:
        fig,ax=plt.subplots(figsize=(8,4));ax.hist(durations,bins=min(20,len(durations)));ax.set(xlabel='Recorded call duration (seconds)',ylabel='Calls',title=f'{run_id} / {actor} | duration n={len(durations)}');fig.tight_layout();fig.savefig(assets/'tool-durations.png',dpi=150);plt.close(fig);charts.append('tool-durations.png')
    (out/'telemetry.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'calls.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['tool','duration_s','success','retry']);w.writeheader();w.writerows(data['calls'])
    lines=[f'# Observed tool activity: {md(run_id)}','',f'Actor: **{actor}**. '+data['scope'],'',f'Observed calls: {data["observed_calls"]}; explicit errors: {data["explicit_errors"]}; unknown outcomes: {data["unknown_outcomes"]}; retries: {data["explicit_retries"] if data["explicit_retries"] is not None else "N/A"}; malformed lines: {data["malformed_lines"]}.','', '[JSON](telemetry.json) · [CSV](calls.csv)']
    lines += ['',f'Explicit retry=true events observed: {data["observed_retry_events"]}; calls with unknown retry field: {data["unknown_retry_outcomes"]}. The observed count is a lower bound when fields are missing, not a fabricated total.']
    for c in charts:lines+=['',f'![{c}](assets/{c})']
    (out/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');return data
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('log');p.add_argument('--run-id',required=True);p.add_argument('--actor',choices=['candidate','referee'],required=True);p.add_argument('--out',required=True);a=p.parse_args();report(a.log,a.out,a.run_id,a.actor)
