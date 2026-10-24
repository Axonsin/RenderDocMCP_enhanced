"""Synthetic fixtures only. These are not benchmark submissions or model results."""
import copy
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import benchmark as b


def fixture(root, task="pipeline", run_id="synthetic-1", repetition=1):
    root.mkdir(parents=True, exist_ok=True)
    (root / "report.md").write_text("# Synthetic fixture\nNot an official benchmark result.\n", encoding="utf-8")
    (root / "evidence.json").write_text('{"synthetic": true}\n', encoding="utf-8")
    artifacts = {"report": "report.md", "evidence": "evidence.json"}
    if task in ("blender", "unity"):
        from PIL import Image
        Image.new("RGB", (16, 16), (42, 71, 99)).save(root / "render.png")
        artifacts["render"] = "render.png"
        if task == "blender":
            (root / "fixture.blend").write_bytes(b"BLENDER-v000SYNTHETIC-NOT-REOPENABLE")
            artifacts["project"] = "fixture.blend"
        else:
            (root / "project" / "Assets").mkdir(parents=True)
            (root / "project" / "ProjectSettings").mkdir()
            (root / "project" / "ProjectSettings" / "ProjectVersion.txt").write_text("m_EditorVersion: synthetic\n", encoding="utf-8")
            artifacts["project"] = "project"
    run = {"schema_version": 1, "run_id": run_id, "task": task, "role": "candidate", "experiment_id": "synthetic-test-only", "condition_id": "fixture", "protocol_id": "fixture-v1", "repetition": repetition, "capture_sha256": "a" * 64, "model": {"name": "SYNTHETIC-NOT-A-MODEL", "version": None}, "started_at": f"2026-01-01T00:00:{repetition:02d}+00:00", "artifacts": artifacts, "telemetry": None}
    b.write_json(root / "run.json", run)
    return run


def review(root, review_root, levels=None, verified=True):
    review_root.mkdir(parents=True, exist_ok=True)
    (review_root / "observation.txt").write_text("Synthetic test assertion; not an actual reopen/render observation.\n", encoding="utf-8")
    value = b.assessment_template(root)
    value.update(status="final", reviewer={"id": "test-suite-fixture", "kind": "human"}, provenance={"reviewed_at": "2026-01-02T00:00:00Z", "method": "Synthetic unit test only", "rubric_version": "fixture-v1"})
    for key in value["scores"]:
        value["scores"][key] = {"level": (levels or {}).get(key, 100), "rationale": "Synthetic fixture level", "evidence": ["submission:report.md"]}
    for key in value["verification"]:
        value["verification"][key] = {"status": "verified" if verified else "not_checked", "note": "Synthetic test observation", "evidence": ["review:observation.txt"] if verified else []}
    return value


class RunValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "source"
        self.run = fixture(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_telemetry_is_null(self):
        result = b.validate_run(self.root)
        self.assertTrue(all(v is None for v in result["telemetry"].values()))
        self.assertEqual(result["log"]["status"], "missing")
        self.assertIsNone(result["log"]["wall_time_s"])

    def test_incomplete_log_is_not_zero(self):
        self.run["log"] = "events.jsonl"
        b.write_json(self.root / "run.json", self.run)
        (self.root / "events.jsonl").write_text('{"event":"start","timestamp":"2026-01-01T00:00:00Z"}\n', encoding="utf-8")
        result = b.validate_run(self.root)
        self.assertEqual(result["log"]["status"], "incomplete")
        self.assertIsNone(result["log"]["tool_calls"])
        self.assertIsNone(result["log"]["wall_time_s"])

    def test_malformed_log_degrades_explicitly(self):
        (self.root / "events.jsonl").write_text("{not json}\n", encoding="utf-8")
        result = b.inspect_log(self.root, "events.jsonl")
        self.assertEqual(result["status"], "incomplete")

    def test_complete_log_counts_observations(self):
        rows = [{"event": "start", "timestamp": "2026-01-01T00:00:00Z"}, {"event": "tool_call", "timestamp": "2026-01-01T00:00:03Z"}, {"event": "finish", "timestamp": "2026-01-01T00:00:09Z", "status": "failed"}]
        (self.root / "events.jsonl").write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
        result = b.inspect_log(self.root, "events.jsonl")
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["wall_time_s"], 9)
        self.assertEqual(result["tool_calls"], 1)
        self.assertEqual(result["completion"], "failed")

    def test_paths_cannot_escape_or_use_drives(self):
        for relative in ("../outside.txt", "C:/secret.txt", "/secret.txt", "folder/../../outside", "folder\\..\\outside", "foo:stream", "."):
            with self.subTest(relative=relative), self.assertRaises(b.ValidationError):
                b.safe_path(self.root, relative, must_exist=False)

    def test_symlink_rejected(self):
        outside = self.base / "outside.txt"
        outside.write_text("outside", encoding="utf-8")
        try:
            (self.root / "linked.txt").symlink_to(outside)
        except OSError:
            self.skipTest("Host does not allow creating symlinks")
        with self.assertRaises(b.ValidationError):
            b.safe_path(self.root, "linked.txt")

    def test_missing_artifact_and_nonfinite_telemetry(self):
        self.run["artifacts"]["evidence"] = "missing.json"
        b.write_json(self.root / "run.json", self.run)
        with self.assertRaises(b.ValidationError):
            b.validate_run(self.root)
        self.run["artifacts"]["evidence"] = "evidence.json"
        self.run["telemetry"] = {"cost_usd": True}
        b.write_json(self.root / "run.json", self.run)
        with self.assertRaises(b.ValidationError):
            b.validate_run(self.root)

    def test_import_snapshot_detects_tampering(self):
        imported = Path(b.import_run(self.root, self.base / "runs")["imported_to"])
        b.validate_run(imported)
        (imported / "report.md").write_text("Changed\n", encoding="utf-8")
        with self.assertRaisesRegex(b.ValidationError, "changed after snapshot"):
            b.validate_run(imported)

    def test_import_does_not_overwrite(self):
        b.import_run(self.root, self.base / "runs")
        with self.assertRaises(b.ValidationError):
            b.import_run(self.root, self.base / "runs")

    def test_unity_empty_assets_survive_import(self):
        fixture(self.base / "unity", task="unity", run_id="unity")
        destination = b.import_run(self.base / "unity", self.base / "runs")["imported_to"]
        self.assertTrue((Path(destination) / "project" / "Assets").is_dir())

    def test_failed_attempt_can_be_imported_without_invented_artifacts(self):
        self.run.update(task="blender", outcome="failed", artifacts={})
        b.write_json(self.root / "run.json", self.run)
        destination = b.import_run(self.root, self.base / "runs")["imported_to"]
        self.assertEqual(b.validate_run(destination)["snapshot"]["files"], {})


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "source"
        fixture(self.root, task="blender")
        self.checked = b.validate_run(self.root)
        self.review_root = self.base / "review"
        self.value = review(self.root, self.review_root)

    def tearDown(self):
        self.tmp.cleanup()

    def validated(self, value=None):
        return b.validate_assessment(value or self.value, self.checked, self.root, self.review_root)

    def test_no_auto_accept_bool_and_reopen_gates(self):
        self.value["accepted"] = True
        self.value["verification"]["reopened"] = {"status": "not_checked"}
        verdict = b.decision("blender", self.validated())
        self.assertIsNone(verdict["score"])
        self.assertEqual(verdict["rubric_raw_score"], 100)
        self.assertFalse(verdict["passed"])

    def test_verified_reopen_cannot_use_submission_only(self):
        self.value["verification"]["reopened"]["evidence"] = ["submission:report.md"]
        with self.assertRaisesRegex(b.ValidationError, "independently collected"):
            self.validated()

    def test_only_five_levels_and_not_booleans(self):
        for value in (80, -1, 101, True, 75.0, None):
            with self.subTest(value=value):
                self.value["scores"]["geometry"]["level"] = value
                with self.assertRaises(b.ValidationError):
                    self.validated()

    def test_weighted_threshold_and_component_floor(self):
        self.value = review(self.root, self.review_root, {key: 75 for key in b.TASKS["blender"]})
        self.assertFalse(b.decision("blender", self.validated())["passed"])
        self.value["scores"]["geometry"]["level"] = 100
        verdict = b.decision("blender", self.validated())
        self.assertEqual(verdict["score"], 82.5)
        self.assertTrue(verdict["passed"])
        self.value = review(self.root, self.review_root, {"usability": 50})
        verdict = b.decision("blender", self.validated())
        self.assertEqual(verdict["score"], 95)
        self.assertFalse(verdict["passed"])

    def test_wrong_digest_and_independent_judge_session(self):
        self.value["run_digest"] = "0" * 64
        with self.assertRaises(b.ValidationError):
            self.validated()
        self.value["run_digest"] = self.checked["snapshot"]["run_digest"]
        self.value["reviewer"] = {"kind": "independent_model", "id": "self", "model": "SYNTHETIC-NOT-A-MODEL"}
        with self.assertRaises(b.ValidationError):
            self.validated()
        self.value["reviewer"]["session_id"] = "independent-review-session"
        self.assertEqual(self.validated()["status"], "final")

    def test_draft_has_no_score_and_ui_is_separate(self):
        self.value["status"] = "draft"
        self.assertIsNone(b.decision("blender", self.validated())["passed"])
        self.value["status"] = "final"
        self.value["ui"] = {"score": 0, "rationale": "No UI needed", "evidence": ["review:observation.txt"]}
        verdict = b.decision("blender", self.validated())
        self.assertTrue(verdict["passed"])
        self.assertEqual(verdict["score"], 100)

    def test_reference_does_not_receive_auto100(self):
        self.checked["run"]["role"] = "reference"
        self.value = review(self.root, self.review_root, {key: 25 for key in b.TASKS["blender"]})
        self.assertEqual(b.decision("blender", self.validated())["score"], 25)

    def test_failed_outcome_never_passes_even_with_high_scores(self):
        verdict = b.decision("blender", self.validated(), "failed")
        self.assertFalse(verdict["passed"])
        self.assertIsNone(verdict["score"])
        self.assertIn("Attempt outcome is failed", verdict["reasons"])

    def test_every_required_gate_blocks_official_score_when_failed_or_unknown(self):
        for gate in b.required_verification('blender'):
            for status in ('failed','not_checked'):
                value=copy.deepcopy(self.value)
                value['verification'][gate]={'status':status,'note':'Synthetic negative gate','evidence':['review:observation.txt'] if status=='failed' else []}
                verdict=b.decision('blender',self.validated(value))
                self.assertFalse(verdict['passed'],(gate,status))
                self.assertIsNone(verdict['score'],(gate,status))
                self.assertEqual(verdict['rubric_raw_score'],100)

    def test_invalid_submission_never_scores_even_if_every_task_rubric_is_100(self):
        for task in b.TASKS:
            root=self.base/('invalid-'+task);fixture(root,task=task)
            checked=b.validate_run(root);rr=self.base/('review-'+task);value=review(root,rr)
            value['verification']['submission_validity']={'status':'failed','note':'Synthetic unauthorized oracle access or screenshot-plane substitution','evidence':['review:observation.txt']}
            verdict=b.decision(task,b.validate_assessment(value,checked,root,rr))
            self.assertEqual(verdict['status'],'disqualified')
            self.assertIsNone(verdict['score']);self.assertEqual(verdict['rubric_raw_score'],100);self.assertFalse(verdict['passed'])

    def test_new_gates_need_independent_evidence_and_unknown_keys_are_rejected(self):
        for key in ('submission_validity','resource_completeness','independence'):
            value=copy.deepcopy(self.value);value['verification'][key]['evidence']=['submission:report.md']
            with self.assertRaisesRegex(b.ValidationError,'independently collected'):self.validated(value)
        value=copy.deepcopy(self.value);value['verification']['validity_typo']={'status':'failed'}
        with self.assertRaisesRegex(b.ValidationError,'Unknown verification gate'):self.validated(value)

    def test_reference_validity_uses_allowed_role_scope(self):
        self.checked['run']['role']='reference'
        self.value['verification']['submission_validity']['note']='Synthetic referee protocol explicitly allows source assets and oracle data for this reference role'
        self.assertTrue(b.decision('blender',self.validated())['passed'])

    def test_disqualified_report_preserves_raw_only_as_diagnostic(self):
        self.value['verification']['submission_validity']['status']='failed'
        b.write_json(self.review_root/'assessment.json',self.value)
        out=self.base/'disqualified-report'
        result=b.evaluate(self.root,self.review_root/'assessment.json',out)
        self.assertIsNone(result['decision']['score'])
        self.assertIn('Official score: **N/A**',(out/'report.md').read_text(encoding='utf8'))
        self.assertIn('Raw rubric diagnostic: **100.0**',(out/'report.md').read_text(encoding='utf8'))
        import csv
        rows=list(csv.DictReader((out/'scores.csv').open(encoding='utf8')))
        self.assertTrue(all(r['decision_status']=='disqualified' and r['official_score']=='' and r['rubric_raw_score']=='100.0' for r in rows))

    def test_cli_evaluation_produces_portable_markdown_png(self):
        self.value["scores"]["visual"]["evidence"] = ["submission:render.png"]
        b.write_json(self.review_root / "assessment.json", self.value)
        output = self.base / "out"
        process = subprocess.run([sys.executable, str(Path(b.__file__)), "evaluate", str(self.root), "--assessment", str(self.review_root / "assessment.json"), "--out", str(output)], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue((output / "assets" / "scores.png").is_file())
        self.assertTrue((output / "scores.csv").is_file())
        text = (output / "report.md").read_text(encoding="utf-8")
        self.assertIn("![Component scores](assets/scores.png)", text)
        self.assertIn("![Evidence](assets/evidence-", text)
        self.assertNotIn("<html", text)

    def test_report_cannot_overwrite_submission_or_existing_files(self):
        b.write_json(self.review_root / "assessment.json", self.value)
        before = (self.root / "report.md").read_bytes()
        with self.assertRaises(b.ValidationError):
            b.evaluate(self.root, self.review_root / "assessment.json", self.root)
        with self.assertRaises(b.ValidationError):
            b.evaluate(self.root, self.review_root / "assessment.json", self.root / "child-report")
        self.assertEqual((self.root / "report.md").read_bytes(), before)
        output = self.base / "existing"
        output.mkdir()
        (output / "report.md").write_text("preserve me", encoding="utf-8")
        with self.assertRaises(b.ValidationError):
            b.evaluate(self.root, self.review_root / "assessment.json", output)
        self.assertEqual((output / "report.md").read_text(encoding="utf-8"), "preserve me")


class ImageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        from PIL import Image
        self.Image = Image
        Image.new("RGB", (16, 16), (0, 0, 0)).save(self.base / "black.png")
        Image.new("RGB", (16, 16), (255, 255, 255)).save(self.base / "white.png")

    def tearDown(self):
        self.tmp.cleanup()

    def test_known_constant_ssim_and_identical(self):
        result = b.image_metrics(self.base / "black.png", self.base / "black.png")
        self.assertAlmostEqual(result["ssim"]["value"], 1, places=12)
        self.assertIsNone(result["psnr_db"])
        result = b.image_metrics(self.base / "black.png", self.base / "white.png")
        self.assertAlmostEqual(result["ssim"]["value"], .0001 / 1.0001, places=10)
        self.assertEqual(result["mse"], 1)

    def test_dimension_mismatch_and_small_input_rejected(self):
        self.Image.new("RGB", (17, 16)).save(self.base / "different.png")
        with self.assertRaisesRegex(b.ValidationError, "dimension mismatch"):
            b.image_metrics(self.base / "black.png", self.base / "different.png")
        self.Image.new("RGB", (8, 8)).save(self.base / "small.png")
        with self.assertRaisesRegex(b.ValidationError, ">= 11"):
            b.image_metrics(self.base / "small.png", self.base / "small.png")

    def test_transparency_and_corruption_rejected(self):
        self.Image.new("RGBA", (16, 16), (0, 0, 0, 0)).save(self.base / "alpha.png")
        with self.assertRaisesRegex(b.ValidationError, "Transparent"):
            b.image_metrics(self.base / "alpha.png", self.base / "black.png")
        (self.base / "broken.png").write_bytes(b"not a png")
        with self.assertRaises(b.ValidationError):
            b.image_metrics(self.base / "broken.png", self.base / "black.png")

    def test_unavailable_lpips_explicit_and_no_download(self):
        with patch("benchmark.importlib.util.find_spec", return_value=None):
            result = b.image_metrics(self.base / "black.png", self.base / "white.png", lpips=True)
        self.assertEqual(result["lpips"]["status"], "unavailable")
        self.assertIsNone(result["lpips"]["value"])


class AggregateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def result(self, index, *, passed=True, independent=True, final=True, outcome="completed"):
        root = self.base / f"source-{index}"
        fixture(root, run_id=f"synthetic-{index}", repetition=index)
        checked = b.validate_run(root)
        checked["run"]["outcome"] = outcome
        value = review(root, self.base / f"review-{index}", levels=None if passed else {key: 75 for key in b.TASKS["pipeline"]})
        if not independent:
            value["verification"]["independence"] = {"status": "not_checked"}
        if not final:
            value["status"] = "draft"
        normalized = b.validate_assessment(value, checked, root, self.base / f"review-{index}")
        result = {"schema_version": 1, "kind": "evaluation_result", "run": checked["run"], "run_digest": checked["snapshot"]["run_digest"], "assessment": normalized, "decision": {"passed": True, "score": 100}}
        path = self.base / f"result-{index}.json"
        b.write_json(path, result)
        return path

    def test_pass_cubed_uses_failures_and_not_best_of_three(self):
        paths = [self.result(1), self.result(2), self.result(3, passed=False)]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertAlmostEqual(group["pass_cubed_estimate"], (2/3)**3)
        self.assertEqual(group["observed_triplet_success_rate"], 0)
        self.assertEqual(group["passes"], 2)

    def test_triplets_are_nonoverlapping_and_tail_not_a_trial(self):
        paths = [self.result(i, passed=i != 3) for i in range(1, 5)]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertEqual(group["nonoverlapping_triplets"], 1)
        self.assertEqual(group["unused_tail_runs"], 1)
        self.assertEqual(group["observed_triplet_success_rate"], 0)
        self.assertAlmostEqual(group["pass_cubed_estimate"], .75**3)

    def test_unreviewed_attempt_prevents_selection_of_successes(self):
        paths = [self.result(1), self.result(2), self.result(3), self.result(4, final=False)]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertIsNone(group["pass_cubed_estimate"])
        self.assertEqual(group["submitted_runs"], 4)

    def test_fewer_than_three_or_unverified_independence(self):
        paths = [self.result(1), self.result(2), self.result(3, independent=False)]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertIsNone(group["pass_cubed_estimate"])
        self.assertEqual(group["verified_independent_runs"], 2)

    def test_duplicate_run_rejected(self):
        path = self.result(1)
        with self.assertRaisesRegex(b.ValidationError, "Duplicate run_id"):
            b.aggregate([path, path], self.base / "out")

    def test_failed_attempt_stays_in_denominator(self):
        paths = [self.result(1), self.result(2), self.result(3, outcome="failed")]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertEqual(group["verified_independent_runs"], 3)
        self.assertEqual(group["passes"], 2)
        self.assertAlmostEqual(group["pass_cubed_estimate"], (2/3)**3)

    def test_same_candidate_session_cannot_be_independent_repetitions(self):
        paths = [self.result(i) for i in range(1, 4)]
        for path in paths:
            value = b.read_json(path)
            value["run"]["session_id"] = "same-candidate-session"
            b.write_json(path, value)
        with self.assertRaisesRegex(b.ValidationError, "Duplicate candidate session_id"):
            b.aggregate(paths, self.base / "out")

    def test_distinct_sessions_still_require_independence_review(self):
        paths = [self.result(1), self.result(2), self.result(3, independent=False)]
        for index, path in enumerate(paths):
            value = b.read_json(path)
            value["run"]["session_id"] = f"candidate-session-{index}"
            b.write_json(path, value)
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertIsNone(group["pass_cubed_estimate"])
        self.assertEqual(group["missing_session_id_runs"], 0)

    def test_missing_session_ids_are_disclosed_and_need_external_evidence(self):
        paths = [self.result(i) for i in range(1, 4)]
        group = b.aggregate(paths, self.base / "out")["groups"][0]
        self.assertEqual(group["missing_session_id_runs"], 3)
        self.assertIn("solely", group["independence_limitation"])
        self.assertEqual(group["pass_cubed_estimate"], 1)

    def test_disqualified_independent_attempt_remains_in_denominator(self):
        paths=[self.result(i) for i in range(1,4)]
        value=b.read_json(paths[-1]);value['assessment']['verification']['submission_validity']['status']='failed';b.write_json(paths[-1],value)
        group=b.aggregate(paths,self.base/'invalid-out')['groups'][0]
        self.assertEqual(group['verified_independent_runs'],3);self.assertEqual(group['passes'],2)
        self.assertEqual(group['disqualified_runs'],1);self.assertEqual(group['officially_scored_runs'],2)
        self.assertAlmostEqual(group['pass_cubed_estimate'],(2/3)**3)

    def test_stored_missing_gate_or_unhashed_failed_gate_rejected(self):
        path=self.result(1);original=b.read_json(path)
        value=copy.deepcopy(original);del value['assessment']['verification']['submission_validity'];b.write_json(path,value)
        with self.assertRaisesRegex(b.ValidationError,'acceptance gates'):b.aggregate([path],self.base/'missing-gate')
        value=copy.deepcopy(original);value['assessment']['verification']['submission_validity'].update(status='failed',evidence=[]);b.write_json(path,value)
        with self.assertRaisesRegex(b.ValidationError,'hashed independent'):b.aggregate([path],self.base/'failed-gate')


if __name__ == "__main__":
    unittest.main()
