"""Region RGB, silhouette and same-unit depth diagnostics; no inferred scores."""
import argparse,json,pathlib
import numpy as np
from PIL import Image
from benchmark import _blur_valid, optional_lpips, ValidationError, require, sha256_file

def rgb(path):
    with Image.open(path) as im:
        require(im.format=='PNG' and im.mode in ('RGB','RGBA'),'Use explicit 8-bit RGB/RGBA PNG')
        a=np.asarray(im.convert('RGBA'))
        require(np.all(a[:,:,3]==255),'Composite transparency with documented settings first')
        return a[:,:,:3].astype(np.float64)/255

def mask(path,shape):
    with Image.open(path) as im:
        a=np.asarray(im)
    require(a.ndim==2 and a.shape==shape,'Mask must be one channel at the exact image resolution')
    require(np.all((a==0)|(a==255)),'Mask values must be 0 or 255')
    return a>0

def region_metrics(x,y,m):
    require(x.shape==y.shape and x.shape[:2]==m.shape,'Image/mask shape mismatch')
    require(min(m.shape)>=11,'SSIM needs dimensions >=11')
    count=int(m.sum())
    if not count:return {'status':'unavailable','reason':'Empty region','pixel_count':0}
    k=np.exp(-(np.arange(-5,6,dtype=np.float64)**2)/(2*1.5**2));k/=k.sum()
    mx,my=_blur_valid(x,k),_blur_valid(y,k)
    vx=np.maximum(_blur_valid(x*x,k)-mx*mx,0);vy=np.maximum(_blur_valid(y*y,k)-my*my,0)
    cov=_blur_valid(x*y,k)-mx*my
    sm=((2*mx*my+.01**2)*(2*cov+.03**2))/((mx*mx+my*my+.01**2)*(vx+vy+.03**2))
    # A window qualifies only if every one of its 121 pixels is in the ROI.
    inner=np.ones((m.shape[0]-10,m.shape[1]-10),dtype=bool)
    for dy in range(11):
        for dx in range(11):inner &= m[dy:dy+inner.shape[0],dx:dx+inner.shape[1]]
    error=x[m]-y[m];mse=float(np.mean(error**2))
    return {'status':'available','pixel_count':count,'mae':float(np.mean(abs(error))),'mse':mse,'psnr_db':None if mse==0 else float(-10*np.log10(mse)),
      'ssim':{'status':'available' if inner.any() else 'unavailable','value':float(sm[inner].mean()) if inner.any() else None,'valid_windows':int(inner.sum())},
      'method':'RGB stored file values; Gaussian 11x11 sigma1.5; SSIM only fully contained windows; empty/too-thin ROI never becomes zero'}

def silhouette(a,b):
    require(a.shape==b.shape,'Silhouette dimensions differ')
    union=int((a|b).sum());intersection=int((a&b).sum())
    return {'iou':intersection/union if union else None,'reference_pixels':int(a.sum()),'candidate_pixels':int(b.sum()),'intersection':intersection,'union':union,'both_empty':union==0}

def depth(a,b,m,unit):
    require(a.shape==b.shape==m.shape,'Depth/mask shape mismatch')
    require(bool(unit),'Explicit common depth unit required; no implicit device-depth conversion')
    av=np.isfinite(a)&(a>0);bv=np.isfinite(b)&(b>0);valid=m&av&bv
    error=abs(a[valid]-b[valid]);rel=error/a[valid]
    return {'unit':unit,'valid_pixels':int(valid.sum()),'reference_valid_pixels':int((av&m).sum()),'candidate_missing_pixels':int((av&~bv&m).sum()),
      'mae':float(error.mean()) if len(error) else None,'rmse':float(np.sqrt(np.mean(error**2))) if len(error) else None,'absolute_relative':float(rel.mean()) if len(error) else None,
      'method':'Aligned positive finite linear depth in the same camera convention and unit; missing pixels reported separately'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('reference');p.add_argument('candidate');p.add_argument('--regions',help='JSON object mapping region names to relative binary PNG paths');p.add_argument('--reference-silhouette');p.add_argument('--candidate-silhouette');p.add_argument('--reference-depth');p.add_argument('--candidate-depth');p.add_argument('--depth-unit');p.add_argument('--lpips',action='store_true');p.add_argument('--out',required=True);a=p.parse_args()
    out=pathlib.Path(a.out);require(not out.exists(),'Refusing to overwrite diagnostic output')
    x,y=rgb(a.reference),rgb(a.candidate);require(x.shape==y.shape,'Image sizes differ; no auto registration');shape=x.shape[:2]
    masks={'full':np.ones(shape,dtype=bool)};sources={}
    if a.regions:
        rp=pathlib.Path(a.regions);defs=json.loads(rp.read_text(encoding='utf-8'))
        for name,path in defs.items():
            require(name!='full','full is reserved');mp=rp.parent/path;masks[name]=mask(mp,shape);sources[name]={'path':str(mp),'sha256':sha256_file(mp)}
    result={'schema_version':1,'reference_sha256':sha256_file(a.reference),'candidate_sha256':sha256_file(a.candidate),'regions':{n:region_metrics(x,y,m) for n,m in masks.items()},'mask_sources':sources,'lpips':optional_lpips(x,y) if a.lpips else {'status':'not_requested','value':None},'silhouette':None,'depth':None,'scoring':'Diagnostic values only; no automatic percent reconstruction or rubric score'}
    require(bool(a.reference_silhouette)==bool(a.candidate_silhouette),'Both silhouette paths required')
    if a.reference_silhouette:result['silhouette']=silhouette(mask(a.reference_silhouette,shape),mask(a.candidate_silhouette,shape))
    require(bool(a.reference_depth)==bool(a.candidate_depth),'Both depth paths required')
    if a.reference_depth:
        require(a.depth_unit is not None,'--depth-unit required')
        da,db=np.load(a.reference_depth,allow_pickle=False),np.load(a.candidate_depth,allow_pickle=False)
        result['depth']={n:depth(da,db,m,a.depth_unit) for n,m in masks.items()}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8');print(out)
if __name__=='__main__':
    try:main()
    except (ValidationError,ValueError,OSError) as e:raise SystemExit(str(e))
