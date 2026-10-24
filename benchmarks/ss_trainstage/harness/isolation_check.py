"""Run INSIDE the contestant sandbox; a check, not an OS sandbox installer."""
import argparse,json,os,pathlib,datetime
def check(forbidden):
    rows=[]
    for name in forbidden:
        p=pathlib.Path(name)
        try:
            if p.is_dir():
                with os.scandir(p) as entries: next(entries,None)
            else:
                with p.open('rb') as f:f.read(1)
            rows.append({'path':str(p),'accessible':True,'status':'isolation_failure'})
        except (PermissionError,FileNotFoundError,NotADirectoryError) as e:
            rows.append({'path':str(p),'accessible':False,'status':type(e).__name__})
        except OSError as e:
            rows.append({'path':str(p),'accessible':None,'status':str(e)})
    return {'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':bool(rows) and all(x['accessible'] is False for x in rows),'checks':rows,'limitation':'Only tests named paths in this execution namespace. Does not prove aliases, credentials, network shares, or other tools cannot access secrets. Requires independently enforced sandbox and separate reviewer session.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--forbid',action='append',required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();result=check(a.forbid);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if result['passed'] else 2)
