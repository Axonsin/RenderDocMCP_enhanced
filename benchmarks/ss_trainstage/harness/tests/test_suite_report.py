import sys,pathlib,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from suite_report import combine
from benchmark import TASKS,required_verification
def fixture(task,level=100):
    return {'schema_version':1,'kind':'evaluation_result','run':{'run_id':task,'task':task,'capture_sha256':'a'*64,'protocol_id':'x','experiment_id':'x','condition_id':'x','model':{'name':'synthetic'},'role':'reference'},
      'assessment':{'status':'final','reviewer':{'id':'synthetic','kind':'human'},'provenance':{'method':'test fixture','reviewed_at':'2026-10-23T10:00:00Z','rubric_version':'synthetic-only'},'verification':{k:{'status':'verified','note':'Synthetic independent observation, not actual model evidence','evidence':[{'reference':'review:observation.txt','sha256':'a'*64}]} for k in required_verification(task)},'components':{k:{'level':level,'weight':w} for k,w in TASKS[task].items()}}}
class SuiteTests(unittest.TestCase):
    def test_missing_not_zero(self):self.assertIsNone(combine([fixture('blender')])[0]['case_score'])
    def test_equal_four_mean(self):self.assertEqual(combine([fixture(t,25*(i+1)) for i,t in enumerate(TASKS)])[0]['case_score'],62.5)
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):combine([fixture('blender'),fixture('blender')])
    def test_truthy_but_invalid_review_provenance_rejected(self):
        x=fixture('pipeline');x['assessment']['reviewer']={'id':'self'}
        with self.assertRaises(ValueError):combine([x])
        x=fixture('pipeline');x['assessment']['provenance']={'method':'test fixture'}
        with self.assertRaises(ValueError):combine([x])
    def test_invalid_all_100_is_disqualified_and_cannot_raise_suite_mean(self):
        rows=[fixture(t) for t in TASKS]
        rows[0]['assessment']['verification']['submission_validity']['status']='failed'
        group=combine(rows)[0]
        self.assertIsNone(group['case_score']);self.assertIsNone(group['task_scores']['blender'])
        self.assertEqual(group['counts']['blender']['disqualified'],1)
        self.assertEqual(group['counts']['blender']['officially_scored'],0)
        self.assertEqual(rows[0]['decision']['rubric_raw_score'],100)
        self.assertEqual(rows[0]['decision']['status'],'disqualified')
    def test_unknown_validity_and_missing_resource_gate_never_become_scores(self):
        x=fixture('pipeline');x['assessment']['verification']['submission_validity']={'status':'not_checked'}
        self.assertIsNone(combine([x])[0]['task_scores']['pipeline'])
        x=fixture('unity');del x['assessment']['verification']['resource_completeness']
        with self.assertRaises(ValueError):combine([x])
    def test_same_session_judge_and_unhashed_gate_rejected(self):
        x=fixture('pipeline');x['run']['session_id']='same'
        x['assessment']['reviewer']={'id':'judge','kind':'independent_model','model':'same-model-is-allowed','session_id':'same'}
        with self.assertRaises(ValueError):combine([x])
        x=fixture('blender');x['assessment']['verification']['reopened']['evidence']=[{'reference':'submission:report.md','sha256':'a'*64}]
        with self.assertRaises(ValueError):combine([x])
if __name__=='__main__':unittest.main()
