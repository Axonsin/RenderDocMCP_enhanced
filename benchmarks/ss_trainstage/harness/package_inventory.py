"""Freeze deliverable hashes; local dependency caches are excluded, built reference players are retained."""
import argparse,os,pathlib,json,hashlib,datetime
EXCLUDED={'Library','Temp','Obj','Logs','UserSettings','.venv','cache','__pycache__','.git'}
VALIDATION_PROJECTS={'reference/unity/Evidence/PortableProject','oracle/source/independent_review/unity_project'}
def inventory(root):
    root=pathlib.Path(root).resolve();rows=[]
    for current,dirs,files in os.walk(root):
        dirs[:]=sorted(d for d in dirs if d not in EXCLUDED)
        current_rel=pathlib.Path(current).relative_to(root).as_posix()
        if current_rel in VALIDATION_PROJECTS:
            # The authoritative project is already included. Keep only the
            # independent cold-import output, not a second copy of its assets.
            dirs[:]=[d for d in dirs if d=='Evidence'];files=[]
        for name in sorted(files):
            p=pathlib.Path(current)/name;rel=p.relative_to(root).as_posix()
            if name.endswith(('.blend1','.pid')) or rel in ('package-manifest.json','acceptance.json') or name.endswith('-public.zip'):continue
            if p.is_symlink():raise ValueError('Symlink in deliverables: '+rel)
            h=hashlib.sha256()
            with p.open('rb') as f:
                for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
            rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':h.hexdigest()})
    return {'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':rows,'file_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),'excluded_directories':sorted(EXCLUDED),'validation_projects_evidence_only':sorted(VALIDATION_PROJECTS),'note':'Private artifact inventory, not a public input bundle; source inputs and external app installations are not embedded. This hash snapshot does not claim visual equivalence or candidate isolation.'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();r=inventory(a.root);a.out.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in r.items() if k!='files'},indent=2))
