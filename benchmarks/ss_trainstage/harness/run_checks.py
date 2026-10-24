"""Run the actual unit suite and retain machine-readable counts and failure logs."""
import pathlib,unittest,json,datetime,io,sys
root=pathlib.Path(__file__).resolve().parents[1]
stream=io.StringIO();suite=unittest.defaultTestLoader.discover(str(root/'harness/tests'))
result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
log=root/'harness/test-results.txt';log.write_text(stream.getvalue(),encoding='utf-8')
record={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tests_run':result.testsRun,'passed':result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped)-len(result.expectedFailures)-len(result.unexpectedSuccesses),'skipped':len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),'expected_failures':len(result.expectedFailures),'unexpected_successes':len(result.unexpectedSuccesses),'successful':result.wasSuccessful(),'skipped_tests':[(str(test),reason) for test,reason in result.skipped],'scope':'Synthetic fixtures and evaluator mechanics; not model performance or rendering acceptance','log':'harness/test-results.txt'}
(root/'harness/test-results.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2));raise SystemExit(0 if result.wasSuccessful() else 1)
