"""Template/evaluate the 12 diagnostics using an external evidence-backed review."""
import argparse,json,pathlib
from benchmark import require,sha256_file,evidence,prepare_report_directory,timestamp,nonempty,md,LEVELS,required_verification,validate_verification
IDS=[f'B{i:02}' for i in range(1,13)]
def template(answers,run_id,role='candidate'):
    require(pathlib.Path(answers).is_file(),'Answers file missing')
    require(role in ('candidate','reference'),'Invalid role')
    return {'schema_version':1,'kind':'basic_assessment','run_id':run_id,'answers_sha256':sha256_file(answers),'status':'draft',
       'role':role,'reviewer':{'id':None,'kind':None,'model':None,'session_id':None},'candidate_session_id':None,'reviewed_at':None,'rubric_version':'rdoc-ss-frame2925-v2',
       'verification':{k:{'status':'not_checked','note':None,'evidence':[]} for k in required_verification('basic')},
       'questions':{i:{'level':None,'rationale':'','evidence':[]} for i in IDS}}
def evaluate(answers,review_path,out):
    p=pathlib.Path(review_path);r=json.loads(p.read_text(encoding='utf-8'))
    require(r.get('schema_version')==1 and r.get('kind')=='basic_assessment','Invalid basic assessment')
    require(r.get('answers_sha256')==sha256_file(answers),'Answer digest differs from reviewed artifact')
    require(r.get('status') in ('draft','final'),'Unknown review status');nonempty(r.get('run_id'),'run_id');values=[]
    require(r.get('role') in ('candidate','reference'),'Invalid role')
    if r['status']=='final':
        reviewer=r.get('reviewer',{});require(reviewer.get('kind') in ('human','independent_model'),'External reviewer required');nonempty(reviewer.get('id'),'reviewer.id')
        if reviewer['kind']=='independent_model':
            nonempty(reviewer.get('model'),'reviewer.model');nonempty(reviewer.get('session_id'),'reviewer.session_id')
            require(reviewer['session_id']!=r.get('candidate_session_id'),'Cannot self-review candidate session')
        timestamp(r.get('reviewed_at'),'reviewed_at');nonempty(r.get('rubric_version'),'rubric_version')
        r['verification']=validate_verification(r.get('verification',{}),'basic',pathlib.Path(answers).resolve().parent,p.resolve().parent)
        require(set(r.get('questions',{}))==set(IDS),'Exactly B01..B12 required')
        for q,item in r['questions'].items():
            require(type(item.get('level')) is int and item['level'] in LEVELS,'Invalid five-level score '+q);nonempty(item.get('rationale'),q+'.rationale')
            item['evidence']=evidence(item.get('evidence',[]),pathlib.Path(answers).resolve().parent,p.resolve().parent,review_required=True);values.append(item['level'])
    r['rubric_raw_mean']=sum(values)/12 if len(values)==12 else None
    gates=r.get('verification',{})
    states=[gates.get(k,{}).get('status','not_checked') for k in required_verification('basic')]
    if r['status']!='final':eligibility='unreviewed'
    elif gates.get('submission_validity',{}).get('status')=='failed':eligibility='disqualified'
    elif 'failed' in states:eligibility='verification_failed'
    elif any(s!='verified' for s in states):eligibility='unverified'
    else:eligibility='eligible'
    r['eligibility_status']=eligibility
    r['score_mean']=r['rubric_raw_mean'] if eligibility=='eligible' else None
    r['scoring']='12 equal diagnostics, separate from composite case mean and UI bonus. Official mean requires independently evidenced submission validity and independence; failed/unknown gates suppress it. Raw mean is diagnostic only. Validity follows the actual role/protocol allowed access scope. Review identity and evidence meaning require trusted auditing.'
    target=prepare_report_directory(out);(target/'basic-results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=[f'# Basic diagnostics: {md(r["run_id"])}','',f'Review: **{r["status"]}**. Eligibility: **{eligibility}**. Official mean: **{r["score_mean"] if r["score_mean"] is not None else "N/A"} / 100**. Raw rubric mean: **{r["rubric_raw_mean"] if r["rubric_raw_mean"] is not None else "N/A"}**. '+r['scoring'],'','| Question | Raw rubric level | Rationale |','|---|---:|---|']
    for q in IDS:
        item=r['questions'][q];lines.append(f'| {q} | {item.get("level") if r["status"]=="final" else "N/A"} | {md(item.get("rationale", ""))} |')
    lines+=['','Verification:']+[f'- {k}: **{gates.get(k,{}).get("status","not_checked")}** — {md(gates.get(k,{}).get("note") or "No observation")}' for k in required_verification('basic')]
    lines+=['','[Evidence and raw data](basic-results.json)'];(target/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');return r
def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    t=sub.add_parser('template');t.add_argument('answers');t.add_argument('--run-id',required=True);t.add_argument('--role',choices=['candidate','reference'],default='candidate');t.add_argument('--out',required=True)
    e=sub.add_parser('evaluate');e.add_argument('answers');e.add_argument('--assessment',required=True);e.add_argument('--out',required=True);a=p.parse_args()
    if a.cmd=='template':
        out=pathlib.Path(a.out);require(not out.exists(),'Output exists');out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(template(a.answers,a.run_id,a.role),ensure_ascii=False,indent=2),encoding='utf-8')
    else:evaluate(a.answers,a.assessment,a.out)
if __name__=='__main__':main()
