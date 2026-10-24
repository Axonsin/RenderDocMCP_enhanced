import json,pathlib,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from telemetry_report import summarize
class TelemetryTests(unittest.TestCase):
    def test_partial_retry_fields_preserve_known_events_without_total(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)/'log.jsonl';rows=[{'method':'x','retry':True,'success':False},{'method':'x','retry':False},{'method':'x'}]
            path.write_text('\n'.join(json.dumps(r) for r in rows),encoding='utf8');r=summarize(path)
            self.assertEqual(r['observed_retry_events'],1);self.assertEqual(r['unknown_retry_outcomes'],1);self.assertIsNone(r['explicit_retries']);self.assertEqual(r['explicit_errors'],1)
    def test_no_log_calls_do_not_invent_retry_total(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)/'log.jsonl';path.write_text('',encoding='utf8');r=summarize(path)
            self.assertEqual(r['observed_calls'],0);self.assertIsNone(r['explicit_retries'])
if __name__=='__main__':unittest.main()
