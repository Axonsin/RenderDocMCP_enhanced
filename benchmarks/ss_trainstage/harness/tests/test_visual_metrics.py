import sys,unittest,pathlib,tempfile,subprocess
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from visual_metrics import region_metrics,silhouette,depth
class VisualTests(unittest.TestCase):
    def test_excluded_error_and_boundary(self):
        x=np.zeros((30,30,3));y=x.copy();y[:5]=1;m=np.ones((30,30),bool);m[:5]=False
        r=region_metrics(x,y,m);self.assertEqual(r['mae'],0);self.assertEqual(r['ssim']['value'],1);self.assertEqual(r['ssim']['valid_windows'],300)
    def test_thin_roi_no_fake_ssim(self):
        x=np.zeros((20,20,3));m=np.zeros((20,20),bool);m[10]=True;r=region_metrics(x,x,m)
        self.assertIsNone(r['ssim']['value']);self.assertEqual(r['pixel_count'],20)
    def test_empty_silhouette_not_perfect(self):
        a=np.zeros((2,2),bool);self.assertIsNone(silhouette(a,a)['iou'])
        b=a.copy();b[0,0]=True;self.assertEqual(silhouette(a,b)['iou'],0)
    def test_depth_missing_and_unit(self):
        a=np.array([[1.,2.],[3.,4.]]);b=np.array([[2.,0.],[3.,np.nan]]);m=np.ones((2,2),bool)
        r=depth(a,b,m,'metre');self.assertEqual(r['candidate_missing_pixels'],2);self.assertAlmostEqual(r['mae'],.5)
        with self.assertRaises(ValueError):depth(a,b,m,'')
    def test_cli_refuses_to_overwrite_input_png(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)/'input.png';Image.new('RGB',(12,12)).save(path);before=path.read_bytes()
            result=subprocess.run([sys.executable,str(pathlib.Path(__file__).resolve().parents[1]/'visual_metrics.py'),str(path),str(path),'--out',str(path)],capture_output=True)
            self.assertNotEqual(result.returncode,0);self.assertEqual(path.read_bytes(),before)
if __name__=='__main__':unittest.main()
