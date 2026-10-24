"""Deterministic Unity-world geometry/TRS diagnostics; never converts to scores.

JSON: {objects:[{reference_id, positions:[[x,y,z]], matrix_world:[[4x4]],
                vertex_correspondences:[[reference_index,candidate_index]]?}],
       camera_view_projection:[[4x4]]?, viewport:[width,height]?}

Positions are local. Matrices are row-major JSON, multiply column vectors, and
use the same Unity-world coordinates in both files. Indices may be supplied but
are deliberately not used: these are vertex-set distances, not surface Chamfer.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, math
from pathlib import Path
import numpy as np

MAX_POINTS = 2048
SHEAR_TOLERANCE = 1e-5

class GeometryError(ValueError): pass
def require(condition, message):
    if not condition: raise GeometryError(message)
def matrix(value, label, *, affine=True):
    try: result=np.asarray(value,dtype=np.float64)
    except (TypeError,ValueError) as e: raise GeometryError(label+' must be a numeric 4x4 matrix') from e
    require(result.shape==(4,4) and np.isfinite(result).all(), label+' must be a finite row-major 4x4 matrix')
    if affine: require(np.allclose(result[3],[0,0,0,1],atol=1e-8,rtol=0), label+' must be affine with final row [0,0,0,1]')
    return result
def scene(value, label):
    require(isinstance(value,dict) and isinstance(value.get('objects'),list),label+' needs objects array')
    parsed=[]
    for i,item in enumerate(value['objects']):
        require(isinstance(item,dict),f'{label}.objects[{i}] must be an object')
        rid=item.get('reference_id');require(isinstance(rid,str) and bool(rid.strip()),'reference_id must be nonempty text')
        try:p=np.asarray(item.get('positions'),dtype=np.float64)
        except (TypeError,ValueError) as e:raise GeometryError(rid+' positions must be numeric Nx3') from e
        if p.size==0:p=np.empty((0,3),dtype=np.float64)
        require(p.ndim==2 and p.shape[1]==3 and np.isfinite(p).all(),rid+' positions must be finite Nx3')
        m=matrix(item.get('matrix_world'),rid+'.matrix_world');world=p@m[:3,:3].T+m[:3,3]
        require(np.isfinite(world).all(),rid+' world positions overflowed')
        parsed.append(dict(reference_id=rid,positions=p,world=world,matrix=m,correspondences=item.get('vertex_correspondences')))
    vp=matrix(value['camera_view_projection'],label+'.camera_view_projection',affine=False) if value.get('camera_view_projection') is not None else None
    viewport=value.get('viewport')
    if viewport is not None:require(isinstance(viewport,list) and len(viewport)==2 and all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v>0 for v in viewport),'viewport must be [positive width,positive height]')
    return parsed,vp,viewport
def sample(points,limit):
    indices=np.linspace(0,len(points)-1,min(len(points),limit),dtype=np.int64) if len(points) else np.empty(0,dtype=np.int64)
    return points[indices],indices
def nearest(points,targets):
    # Bound each temporary to 256 x max_points x 3 (<= 12 MiB at 2048).
    distances=[]
    for start in range(0,len(points),256):
        diff=points[start:start+256,None,:]-targets[None,:,:]
        distances.extend(np.sqrt(np.min(np.einsum('ijk,ijk->ij',diff,diff),axis=1)).tolist())
    return np.asarray(distances)
def stats(values):
    return dict(count=len(values),rms=float(np.sqrt(np.mean(values**2))),p95=float(np.percentile(values,95)),maximum=float(np.max(values))) if len(values) else dict(count=0,rms=None,p95=None,maximum=None)
def decomposition(m):
    a=m[:3,:3];scale=np.linalg.norm(a,axis=0);degenerate=bool(np.any(scale<=1e-12));det=float(np.linalg.det(a));unit=a/np.where(scale>1e-12,scale,1)
    shear=float(np.max(abs(unit.T@unit-np.eye(3)))) if not degenerate else None
    reflected=det<0;flags=[]
    if degenerate:flags.append('degenerate_scale')
    if shear is not None and shear>SHEAR_TOLERANCE:flags.append('shear_not_exact_TRS')
    if reflected:flags.append('negative_determinant_signed_scale_rotation_ambiguous')
    r=None
    if not flags:
        u,_,vt=np.linalg.svd(unit);r=u@vt
    return dict(translation=m[:3,3],axis_lengths=scale,determinant=det,shear_residual=shear,flags=flags,rotation=r)
def transform_metrics(r,c,diagonal):
    rd,cd=decomposition(r),decomposition(c);translation=float(np.linalg.norm(rd['translation']-cd['translation']));angle=None
    if rd['rotation'] is not None and cd['rotation'] is not None:
        cosine=(np.trace(rd['rotation'].T@cd['rotation'])-1)/2;angle=float(np.degrees(np.arccos(np.clip(cosine,-1,1))))
    relative=np.divide(abs(cd['axis_lengths']-rd['axis_lengths']),rd['axis_lengths'],out=np.full(3,np.nan),where=rd['axis_lengths']>1e-12)
    return dict(translation_error=translation,translation_error_normalized=translation/diagonal if diagonal>1e-12 else None,rotation_error_degrees=angle,
        reference_axis_lengths=rd['axis_lengths'].tolist(),candidate_axis_lengths=cd['axis_lengths'].tolist(),axis_length_absolute_error=abs(cd['axis_lengths']-rd['axis_lengths']).tolist(),axis_length_relative_error=[float(v) if np.isfinite(v) else None for v in relative],
        reference_flags=rd['flags'],candidate_flags=cd['flags'],reference_determinant=rd['determinant'],candidate_determinant=cd['determinant'],reference_shear_residual=rd['shear_residual'],candidate_shear_residual=cd['shear_residual'],
        note='Axis lengths are unsigned. Rotation error is omitted for shear, degenerate scale or reflection; no unique signed TRS is invented.')
def project(points,vp):
    clip=np.column_stack([points,np.ones(len(points))])@vp.T
    valid=np.isfinite(clip).all(axis=1)&(clip[:,3]>1e-8)
    xy=np.full((len(points),2),np.nan);xy[valid]=clip[valid,:2]/clip[valid,3:4]
    return xy,valid
def reprojection(r,c,rvp,cvp,viewport,limit):
    pairs=c['correspondences']
    if pairs is None:return dict(status='unavailable',reason='No explicit vertex_correspondences; ordering is not assumed')
    require(isinstance(pairs,list),'vertex_correspondences must be a list of integer index pairs')
    require(all(isinstance(p,list) and len(p)==2 and all(isinstance(i,int) and not isinstance(i,bool) for i in p) for p in pairs),'vertex_correspondences must contain [reference_index,candidate_index] integer pairs')
    require(all(0<=p[0]<len(r['world']) and 0<=p[1]<len(c['world']) for p in pairs),'vertex correspondence index out of range')
    if rvp is None:return dict(status='unavailable',reason='Reference camera_view_projection missing',correspondence_count=len(pairs))
    raw_count=len(pairs)
    pairs=list(dict.fromkeys(tuple(p) for p in pairs))
    count=len(pairs);selected=np.linspace(0,count-1,min(count,limit),dtype=int) if count else np.empty(0,dtype=int);a=np.array(pairs,dtype=int).reshape(-1,2)[selected]
    x,xok=project(r['world'][a[:,0]],rvp);y,yok=project(c['world'][a[:,1]],rvp if cvp is None else cvp);ok=xok&yok
    delta=y[ok]-x[ok];ndc=np.linalg.norm(delta,axis=1);pixels=np.linalg.norm(delta*np.array(viewport)/2,axis=1) if viewport is not None else np.empty(0)
    return dict(status='available' if ok.any() else 'unavailable',reason=None if ok.any() else 'No valid positive-W corresponding points',camera_mode='separate_reference_and_candidate_VP' if cvp is not None else 'reference_VP_used_for_both',correspondence_count=raw_count,unique_correspondence_count=count,duplicate_pair_count=raw_count-count,reference_vertex_coverage=len({p[0] for p in pairs})/len(r['world']) if len(r['world']) else None,candidate_vertex_coverage=len({p[1] for p in pairs})/len(c['world']) if len(c['world']) else None,sampled_correspondence_count=len(a),invalid_or_behind_camera_count=int((~ok).sum()),ndc_error=stats(ndc),pixel_error=stats(pixels) if viewport is not None else None,reference_viewport=viewport,clipping='Only positive finite clip W checked; offscreen positive-W points retained; no rasterization or visibility test',coverage_note='Repeated identical pairs are deduplicated before sampling/statistics. Error describes supplied correspondences only, never unpaired vertices.')
def compare(reference,candidate,*,max_points=MAX_POINTS):
    require(type(max_points) is int and 1<=max_points<=MAX_POINTS,'max_points must be integer 1..2048')
    rs,rvp,rv=scene(reference,'reference');cs,cvp,cv=scene(candidate,'candidate')
    rb=collections.defaultdict(list);cb=collections.defaultdict(list)
    for o in rs:rb[o['reference_id']].append(o)
    for o in cs:cb[o['reference_id']].append(o)
    duplicate_r={k:len(v) for k,v in rb.items() if len(v)>1};duplicate_c={k:len(v) for k,v in cb.items() if len(v)>1}
    matched=sorted(k for k in rb.keys()&cb.keys() if len(rb[k])==len(cb[k])==1);missing=sorted(rb.keys()-cb.keys());extra=sorted(cb.keys()-rb.keys());ambiguous=sorted(set(duplicate_r)|set(duplicate_c));results=[]
    for rid in matched:
        r,c=rb[rid][0],cb[rid][0];rp,ri=sample(r['world'],max_points);cp,ci=sample(c['world'],max_points);diag=float(np.linalg.norm(np.ptp(r['world'],axis=0))) if len(r['world']) else 0
        geo=dict(reference_vertex_count=len(r['world']),candidate_vertex_count=len(c['world']),reference_sample_count=len(rp),candidate_sample_count=len(cp),sampling='deterministic linspace indices, endpoints included',reference_sample_indices=ri.tolist(),candidate_sample_indices=ci.tolist(),normalization_reference_world_aabb_diagonal=diag)
        if len(rp) and len(cp):
            rc,cr=nearest(rp,cp),nearest(cp,rp);both=np.concatenate([rc,cr]);geo.update(status='available',reference_to_candidate=stats(rc),candidate_to_reference=stats(cr),bidirectional=stats(both),normalized_bidirectional=stats(both/diag) if diag>1e-12 else None,normalization_note=None if diag>1e-12 else 'Degenerate reference extent; normalized distances unavailable')
        else:geo.update(status='unavailable',reason='Empty vertex set; no fabricated zero distance',normalized_bidirectional=None)
        results.append(dict(reference_id=rid,geometry=geo,transform=transform_metrics(r['matrix'],c['matrix'],diag),reprojection=reprojection(r,c,rvp,cvp,rv,max_points)))
    return dict(schema_version=1,kind='geometry_diagnostics',coordinate_convention='Unity world; local positions; row-major 4x4 matrices multiplying column vectors',coverage=dict(reference_object_count=len(rs),candidate_object_count=len(cs),reference_unique_ids=len(rb),candidate_unique_ids=len(cb),matched_unambiguous_ids=matched,matched_id_fraction=len(matched)/len(rb) if rb else None,missing_reference_ids=missing,extra_candidate_ids=extra,duplicate_reference_ids=duplicate_r,duplicate_candidate_ids=duplicate_c,ambiguous_ids_excluded=ambiguous),objects=results,
        method=dict(max_points_per_object=max_points,nearest_vertex_distance='Bidirectional nearest distances on sampled world-space vertex sets, RMS/p95/max; NOT full surface Chamfer or Hausdorff',sampling_limitation='When sampled, vertex order/tessellation can change distance even for the same surface; triangle interiors, UVs and shading are not compared',transform='Translation distance, orthonormal rotation delta, unsigned axis-length errors; shear/reflection/degenerate axes flagged',reprojection='Requires explicit per-object correspondences; no nearest-point pairs are treated as semantic correspondence',candidate_viewport=cv,viewport_note='Pixel errors use reference viewport only; unequal candidate viewport requires external registration',scoring='Diagnostics only. No pass/fail thresholds, score conversion or object-level semantic matching inferred.'))
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('reference');p.add_argument('candidate');p.add_argument('--out',required=True);p.add_argument('--max-points',type=int,default=MAX_POINTS);args=p.parse_args(argv)
    try:
        ref=Path(args.reference);cand=Path(args.candidate);out=Path(args.out);require(not out.exists(),'Refusing to overwrite diagnostic output')
        result=compare(json.loads(ref.read_text(encoding='utf-8-sig')),json.loads(cand.read_text(encoding='utf-8-sig')),max_points=args.max_points)
        result['inputs']={k:dict(path=str(x.resolve()),sha256=hashlib.sha256(x.read_bytes()).hexdigest()) for k,x in [('reference',ref),('candidate',cand)]}
        out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf8');print(json.dumps(dict(output=str(out),coverage=result['coverage']),ensure_ascii=False));return 0
    except (GeometryError,OSError,ValueError,TypeError) as e:print(json.dumps(dict(status='error',error=str(e))));return 2
if __name__=='__main__':raise SystemExit(main())
