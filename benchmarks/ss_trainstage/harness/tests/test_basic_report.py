import sys,pathlib,unittest,tempfile,json
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from basic_report import template,evaluate

def final_fixture(p):
    a=p/'answers.md';a.write_text('Synthetic answers, not official results',encoding='utf8')
    (p/'observations.md').write_text('Synthetic independent review assertion only',encoding='utf8')
    r=template(a,'synthetic');r.update(status='final',reviewer={'kind':'human','id':'synthetic-reviewer'},reviewed_at='2026-10-23T10:00:00Z')
    for k in r['questions']:r['questions'][k]={'level':100,'rationale':'Synthetic rubric fixture','evidence':['review:observations.md']}
    for k in r['verification']:r['verification'][k]={'status':'verified','note':'Synthetic external gate observation','evidence':['review:observations.md']}
    return a,r,p/'review.json'
class BasicTests(unittest.TestCase):
    def test_draft_unscored_and_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d);a=p/'answers.md';a.write_text('synthetic fixture');r=template(a,'synthetic');rp=p/'review.json';rp.write_text(json.dumps(r))
            self.assertIsNone(evaluate(a,rp,p/'out')['score_mean'])
            a.write_text('changed')
            with self.assertRaises(ValueError):evaluate(a,rp,p/'out2')
    def test_incomplete_final_not_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d);a=p/'a';a.write_text('fixture');r=template(a,'synthetic');r['status']='final';rp=p/'r.json';rp.write_text(json.dumps(r))
            with self.assertRaises(ValueError):evaluate(a,rp,p/'out')
    def test_invalid_all_100_has_no_official_basic_mean(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d);a,r,rp=final_fixture(p)
            r['verification']['submission_validity']['status']='failed'
            r['verification']['submission_validity']['note']='Synthetic unauthorized access to oracle answers'
            rp.write_text(json.dumps(r),encoding='utf8');result=evaluate(a,rp,p/'out')
            self.assertEqual(result['rubric_raw_mean'],100)
            self.assertIsNone(result['score_mean']);self.assertEqual(result['eligibility_status'],'disqualified')
            self.assertIn('Official mean: **N/A',(p/'out/report.md').read_text(encoding='utf8'))
    def test_unknown_independence_and_nonindependent_gate_evidence_do_not_qualify(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d);a,r,rp=final_fixture(p)
            r['verification']['independence']={'status':'not_checked'}
            rp.write_text(json.dumps(r),encoding='utf8');result=evaluate(a,rp,p/'out')
            self.assertIsNone(result['score_mean']);self.assertEqual(result['rubric_raw_mean'],100)
            r['verification']['independence']={'status':'verified','note':'Synthetic assertion','evidence':['submission:answers.md']}
            rp.write_text(json.dumps(r),encoding='utf8')
            with self.assertRaisesRegex(ValueError,'independently collected'):evaluate(a,rp,p/'bad-evidence')
            r['verification']['independence']['evidence']=['review:observations.md']
            r['role']='reference';r['verification']['submission_validity']['note']='Synthetic reference protocol permits oracle/source access'
            rp.write_text(json.dumps(r),encoding='utf8')
            self.assertEqual(evaluate(a,rp,p/'valid-reference')['score_mean'],100)
