"""Analytic synthetic geometry only; no model submission or acceptance scores."""
import copy,json,sys,unittest,tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import geometry_metrics as g

def obj(rid='mesh',positions=None,matrix=None):
    return dict(reference_id=rid,positions=positions if positions is not None else [[0,0,0],[1,0,0],[0,1,0]],matrix_world=(np.eye(4) if matrix is None else matrix).tolist())
def world(*objects,**kwargs):return dict(objects=list(objects),**kwargs)
class GeometryMetricsTests(unittest.TestCase):
    def test_identical_and_unordered_vertices_have_zero_distance(self):
        r=obj();c=obj(positions=list(reversed(r['positions'])));out=g.compare(world(r),world(c))
        self.assertEqual(out['objects'][0]['geometry']['normalized_bidirectional']['rms'],0)
        self.assertEqual(out['objects'][0]['transform']['rotation_error_degrees'],0)
        self.assertEqual(out['objects'][0]['reprojection']['status'],'unavailable')
    def test_same_world_geometry_with_different_local_coordinates(self):
        m=np.eye(4);m[0,3]=2;r=obj();c=obj(positions=[[-2,0,0],[-1,0,0],[-2,1,0]],matrix=m)
        out=g.compare(world(r),world(c))['objects'][0]
        self.assertEqual(out['geometry']['bidirectional']['maximum'],0)
        self.assertEqual(out['transform']['translation_error'],2)
    def test_rotation_scale_translation_are_analytic(self):
        m=np.array([[0,-3,0,4],[2,0,0,0],[0,0,4,0],[0,0,0,1]],float)
        out=g.compare(world(obj()),world(obj(matrix=m)))['objects'][0]['transform']
        self.assertAlmostEqual(out['rotation_error_degrees'],90)
        self.assertEqual(out['translation_error'],4)
        self.assertEqual(out['axis_length_absolute_error'],[1,2,3])
    def test_coverage_extras_and_duplicates_never_choose_arbitrary_match(self):
        out=g.compare(world(obj('a'),obj('b')),world(obj('a'),obj('a'),obj('extra')))
        self.assertEqual(out['coverage']['missing_reference_ids'],['b'])
        self.assertEqual(out['coverage']['extra_candidate_ids'],['extra'])
        self.assertEqual(out['coverage']['duplicate_candidate_ids'],{'a':2})
        self.assertEqual(out['coverage']['matched_id_fraction'],0)
        self.assertEqual(out['objects'],[])
    def test_shear_reflection_and_degenerate_scale_do_not_invent_rotation(self):
        for kind in ['shear','reflection','zero']:
            m=np.eye(4)
            if kind=='shear':m[0,1]=.5
            else:m[0,0]=-1 if kind=='reflection' else 0
            result=g.compare(world(obj()),world(obj(matrix=m)))['objects'][0]['transform']
            self.assertTrue(result['candidate_flags'])
            self.assertIsNone(result['rotation_error_degrees'])
    def test_explicit_reprojection_and_positive_w_filter(self):
        r=obj(positions=[[0,0,1],[0,1,1]]);c=obj(positions=[[1,0,1],[1,1,1]])
        c['vertex_correspondences']=[[0,0],[1,1]]
        out=g.compare(world(r,camera_view_projection=np.eye(4).tolist(),viewport=[100,200]),world(c))['objects'][0]['reprojection']
        self.assertEqual(out['ndc_error']['rms'],1)
        self.assertEqual(out['pixel_error']['rms'],50)
        self.assertEqual(out['camera_mode'],'reference_VP_used_for_both')
        vp=np.eye(4);vp[3,3]=-1
        out=g.compare(world(r,camera_view_projection=vp.tolist()),world(c))['objects'][0]['reprojection']
        self.assertEqual(out['status'],'unavailable')
        self.assertEqual(out['invalid_or_behind_camera_count'],2)
    def test_sampling_is_bounded_deterministic_and_reported(self):
        points=np.column_stack([np.arange(3000),np.zeros(3000),np.zeros(3000)]).tolist();r=world(obj(positions=points))
        a=g.compare(r,r,max_points=17);b=g.compare(r,r,max_points=17)
        self.assertEqual(a,b);x=a['objects'][0]['geometry']
        self.assertEqual(x['reference_sample_count'],17)
        self.assertEqual(x['reference_sample_indices'][0],0);self.assertEqual(x['reference_sample_indices'][-1],2999)
        with self.assertRaises(g.GeometryError):g.compare(r,r,max_points=2049)
    def test_empty_and_nonfinite_input_are_not_zero_success(self):
        out=g.compare(world(obj()),world(obj(positions=[])))['objects'][0]
        self.assertEqual(out['geometry']['status'],'unavailable')
        r=obj(positions=[[float('nan'),0,0]])
        with self.assertRaises(g.GeometryError):g.compare(world(r),world(obj()))
        r=obj();r['matrix_world'][3][0]=1
        with self.assertRaises(g.GeometryError):g.compare(world(r),world(obj()))
    def test_correspondence_indices_are_validated(self):
        c=obj();c['vertex_correspondences']=[[0,100]]
        with self.assertRaises(g.GeometryError):g.compare(world(obj(),camera_view_projection=np.eye(4).tolist()),world(c))
    def test_json_serializable_no_scores(self):
        out=g.compare(world(obj(positions=[[0,0,0]])),world(obj(positions=[[1,0,0]])))
        self.assertIsNone(out['objects'][0]['geometry']['normalized_bidirectional'])
        json.dumps(out,allow_nan=False)
        self.assertNotIn('score',out);self.assertNotIn('passed',out)
    def test_duplicate_correspondences_report_partial_coverage(self):
        r=obj();c=obj(positions=[[0,0,0],[50,0,0],[0,50,0]])
        c['vertex_correspondences']=[[0,0]]*100
        result=g.compare(world(r,camera_view_projection=np.eye(4).tolist()),world(c))['objects'][0]
        self.assertGreater(result['geometry']['bidirectional']['rms'],0)
        projection=result['reprojection']
        self.assertEqual(projection['ndc_error']['rms'],0)
        self.assertEqual(projection['correspondence_count'],100)
        self.assertEqual(projection['unique_correspondence_count'],1)
        self.assertEqual(projection['duplicate_pair_count'],99)
        self.assertAlmostEqual(projection['reference_vertex_coverage'],1/3)
    def test_cli_refuses_to_overwrite_input_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'reference.json';path.write_text(json.dumps(world(obj())),encoding='utf8');before=path.read_bytes()
            self.assertEqual(g.main([str(path),str(path),'--out',str(path)]),2)
            self.assertEqual(path.read_bytes(),before)
if __name__=='__main__':unittest.main()
