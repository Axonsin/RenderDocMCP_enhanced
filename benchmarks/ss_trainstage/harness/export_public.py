"""Export only allowlisted contestant inputs, never oracle/reference/harness state."""
import argparse,pathlib,zipfile,json,hashlib
def export(root,output):
    root=pathlib.Path(root).resolve();output=pathlib.Path(output)
    d=root/'dataset';case=json.loads((d/'case.json').read_text(encoding='utf-8'))
    capture=d/case['capture']
    if capture.resolve().parent!=d.resolve():raise ValueError('Capture outside dataset')
    if hashlib.sha256(capture.read_bytes()).hexdigest()!=case['sha256']:raise ValueError('Capture hash mismatch')
    files=[capture,d/'case.json',d/'basic_tasks.json',d/'README.md',d/'scoring.md']+[d/'tasks'/(x+'.md') for x in ['blender','unity','pipeline','optimization']]
    with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_STORED) as z:
        for f in files:
            if f.is_symlink() or not f.is_file():raise ValueError('Invalid public file: '+str(f))
            z.write(f,f.relative_to(d).as_posix())
    return {'bundle':str(output),'files':len(files),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'private_directories_included':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();print(json.dumps(export(a.root,a.out),indent=2))
