"""Combine evaluated runs into four-task case reports without inventing missing results."""
import argparse,csv,json,pathlib,collections,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from benchmark import TASKS,decision,require,read_json,prepare_report_directory,md,validate_stored_assessment

def combine(results):
    groups=collections.defaultdict(list);ids=set()
    for r in results:
        require(r.get('schema_version')==1 and r.get('kind')=='evaluation_result','Expected benchmark evaluate result.json')
        run=r['run'];require(run['run_id'] not in ids,'Duplicate run_id');ids.add(run['run_id'])
        require(run['task'] in TASKS,'Unknown task')
        validate_stored_assessment(run,r['assessment'])
        require(run.get('outcome','completed') in ('completed','failed','aborted','incomplete'),'Invalid stored attempt outcome')
        r['decision']=decision(run['task'],r['assessment'],run.get('outcome','completed'))
        key=(run['capture_sha256'],run['protocol_id'],run['experiment_id'],run['condition_id'],run['model']['name'],run['model'].get('version'),run['role'])
        groups[key].append(r)
    output=[]
    for key,rs in groups.items():
        scores={};counts={};complete=True
        for task in TASKS:
            rows=[r for r in rs if r['run']['task']==task];values=[r['decision']['score'] for r in rows if r['decision']['score'] is not None]
            counts[task]={'attempts':len(rows),'reviewed':sum(r['assessment']['status']=='final' for r in rows),'officially_scored':len(values),'disqualified':sum(r['decision']['status']=='disqualified' for r in rows)}
            scores[task]=sum(values)/len(values) if values and len(values)==len(rows) else None
            complete &= scores[task] is not None
        output.append({'capture_sha256':key[0],'protocol_id':key[1],'experiment_id':key[2],'condition_id':key[3],'model':key[4],'model_version':key[5],'role':key[6],
          'task_scores':scores,'counts':counts,'case_score':sum(scores.values())/4 if complete else None,'run_ids':[r['run']['run_id'] for r in rs],
          'status':'complete' if complete else 'missing_unreviewed_or_ineligible_tasks','runs':rs})
    return output

def report(paths,out):
    groups=combine([read_json(p) for p in paths]);out=prepare_report_directory(out);assets=out/'assets';assets.mkdir(exist_ok=True)
    labels=[f"{g['model']}\n{g['condition_id']} ({g['role']})" for g in groups];charts=[]
    fig,ax=plt.subplots(figsize=(max(9,3*len(groups)),5));width=.18
    for i,task in enumerate(TASKS):
        xs=[j+(i-1.5)*width for j,g in enumerate(groups) if g['task_scores'][task] is not None];ys=[g['task_scores'][task] for g in groups if g['task_scores'][task] is not None]
        ax.bar(xs,ys,width,label=task)
    ax.set_xticks(range(len(groups)),labels);ax.set(ylim=(0,105),ylabel='Eligible official task score / 100',title='Four-task comparison | missing/ineligible omitted; raw scores excluded');ax.legend();fig.tight_layout();fig.savefig(assets/'task-scores.png',dpi=160);plt.close(fig);charts.append(('Task scores','task-scores.png'))
    for field,unit,name in [('cost_usd','USD','quality-cost'),('wall_time_s','seconds','quality-time')]:
        points=[]
        for g in groups:
            for r in g['runs']:
                v=r.get('telemetry',{}).get(field);score=r['decision']['score']
                if isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v>=0 and score is not None:points.append((v,score,r['run']['run_id'],r['run']['task']))
        if points:
            fig,ax=plt.subplots(figsize=(9,5))
            for v,s,rid,task in points:ax.scatter(v,s);ax.annotate(rid+' / '+task,(v,s),fontsize=7)
            ax.set(xlabel=f'{field} ({unit}; manifest reported)',ylabel='Eligible official task score / 100',ylim=(0,105),title=f'Quality versus {field} | n={len(points)} eligible only; raw scores excluded');fig.tight_layout();fig.savefig(assets/(name+'.png'),dpi=160);plt.close(fig);charts.append((name,name+'.png'))
    public=[{k:v for k,v in g.items() if k!='runs'} for g in groups];(out/'suite.json').write_text(json.dumps(public,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'suite.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['model','condition','role','status',*TASKS,'case_score']);w.writerows([[g['model'],g['condition_id'],g['role'],g['status'],*g['task_scores'].values(),g['case_score']] for g in groups])
    lines=['# Case comparison','', 'The case score is the equal mean of four task means. Every supplied attempt must have an eligible official score before its task mean is available. Failed/unknown validity, independence or reconstruction gates suppress that score; disqualified/raw rubric scores never enter quality means or cost/time plots. Missing tasks never count as zero. UI remains separate. Different protocols/captures are separate groups; no cross-case ranking is inferred.','', '[JSON](suite.json) · [CSV](suite.csv)','', '| Model | Condition | Role | Blender | Unity | Pipeline | Optimization | Case mean |','|---|---|---|---:|---:|---:|---:|---:|']
    for g in groups:lines.append('| '+' | '.join(md('N/A' if v is None else str(v)) for v in [g['model'],g['condition_id'],g['role'],*g['task_scores'].values(),g['case_score']])+' |')
    for title,name in charts:lines+=['',f'![{title}](assets/{name})']
    lines+=['','Sample counts per task:','']
    for g in groups:lines.append(f"- {md(g['model'])} / {md(g['condition_id'])}: "+'; '.join(f'{t} n={c["attempts"]}, reviewed={c["reviewed"]}, official={c["officially_scored"]}, disqualified={c["disqualified"]}' for t,c in g['counts'].items()))
    lines+=['','No error bars or success estimates are produced here. Use benchmark.py aggregate for at least three independently reviewed repetitions. Input JSON is trusted evaluator output; identity/authenticity still requires the review audit.']
    (out/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');return public
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('results',nargs='+');p.add_argument('--out',required=True);a=p.parse_args();report(a.results,a.out)
