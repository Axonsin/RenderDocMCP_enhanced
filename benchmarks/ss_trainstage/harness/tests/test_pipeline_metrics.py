"""Controlled synthetic errors only; these are not model benchmark results."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pipeline_metrics as p


def binding(eid=30, rid="ResourceId::7", slot=0):
    return {"consumer_action_event_id": eid, "resource_id": rid, "stage": "fragment",
            "binding_slot": slot, "binding_range": {"first_mip": 0, "num_mips": 1, "first_slice": 0, "num_slices": 1},
            "verification": "verified", "evidence": ["synthetic-fixture:binding"]}


def graph():
    return {"kind": "pipeline_graph", "schema_version": 1, "pass_granularity": "semantic",
            "scope": {"description": "NONOFFICIAL synthetic graph", "complete": True},
            "passes": [{"pass_id": pid, "action_event_ids": [eid], "verification": "verified", "evidence": ["synthetic-fixture:passes"]}
                       for pid, eid in [("shadow", 10), ("opaque", 20), ("composite", 30)]],
            "pass_sequence": ["shadow", "opaque", "composite"],
            "sequence_verification": "verified", "sequence_evidence": ["synthetic-fixture:order"],
            "bindings": [binding(), binding(20, "ResourceId::8")], "producer_links": None}


def producer(producer_eid=20):
    return {"binding": binding(), "producer_action_event_id": producer_eid, "coverage": "full_binding_range",
            "semantics": "single_complete_overwrite", "verification": "verified", "evidence": ["synthetic-fixture:full-write"]}


class PipelineMetricsTests(unittest.TestCase):
    def test_identical_graph_is_deterministic_but_producers_unavailable(self):
        a = p.compare(graph(), graph())
        self.assertEqual(a, p.compare(graph(), graph()))
        for key in ["passes", "pass_membership", "order", "bindings", "binding_ranges"]:
            self.assertEqual(a["metrics"][key]["f1"], 1)
        self.assertIsNone(a["metrics"]["restricted_producers"]["f1"])
        self.assertNotIn("score", a)
        self.assertNotIn("passed", a)

    def test_wrong_dependency_creates_one_false_positive_and_one_false_negative(self):
        candidate = graph()
        candidate["bindings"][0]["resource_id"] = "ResourceId::999"
        metric = p.compare(graph(), candidate)["metrics"]["bindings"]
        self.assertEqual((metric["true_positive"], metric["false_positive"], metric["false_negative"]), (1, 1, 1))
        self.assertEqual(metric["f1"], .5)
        self.assertEqual(metric["unmatched_candidate"][0]["resource_id"], "ResourceId::999")

    def test_missing_pass_and_reversed_order_are_distinct_diagnostics(self):
        candidate = graph()
        candidate["passes"].pop(1)
        candidate["pass_sequence"] = ["composite", "shadow"]
        metrics = p.compare(graph(), candidate)["metrics"]
        self.assertAlmostEqual(metrics["passes"]["recall"], 2/3)
        self.assertEqual(metrics["passes"]["missing_reference"], [{"pass_id": "opaque"}])
        self.assertEqual(metrics["order"]["inversion_count"], 1)
        self.assertEqual(metrics["order"]["f1"], 0)

    def test_missing_middle_pass_does_not_invent_adjacent_dependency(self):
        candidate = graph()
        candidate["passes"].pop(1)
        candidate["pass_sequence"].pop(1)
        metric = p.compare(graph(), candidate)["metrics"]["order"]
        self.assertEqual(metric["true_positive"], 1)
        self.assertEqual(metric["false_positive"], 0)
        self.assertEqual(metric["false_negative"], 2)

    def test_range_error_does_not_change_binding_identity(self):
        candidate = graph()
        candidate["bindings"][0]["binding_range"]["first_slice"] = 1
        metrics = p.compare(graph(), candidate)["metrics"]
        self.assertEqual(metrics["bindings"]["f1"], 1)
        self.assertEqual(metrics["binding_ranges"]["f1"], .5)

    def test_unknown_candidate_range_is_not_wildcard(self):
        candidate = graph()
        candidate["bindings"][0]["binding_range"] = None
        metric = p.compare(graph(), candidate)["metrics"]["binding_ranges"]
        self.assertEqual(metric["f1"], .5)
        self.assertEqual(metric["candidate_unknown_range_count"], 1)

    def test_unknown_reference_range_is_explicitly_outside_strict_scope(self):
        reference = graph()
        reference["bindings"][0]["binding_range"] = None
        metric = p.compare(reference, graph())["metrics"]["binding_ranges"]
        self.assertEqual(metric["reference_count"], 1)
        self.assertEqual(metric["reference_unknown_range_count"], 1)
        self.assertEqual(metric["candidate_outside_known_reference_identity_count"], 1)

    def test_repeated_bindings_cannot_inflate_scores(self):
        candidate = graph()
        candidate["bindings"] += [copy.deepcopy(candidate["bindings"][0]) for _ in range(100)]
        result = p.compare(graph(), candidate)
        self.assertEqual(result["metrics"]["bindings"]["candidate_count"], 2)
        self.assertEqual(result["duplicate_records"]["candidate_bindings"], 100)

    def test_duplicate_resource_different_stage_or_slot_stays_distinct(self):
        reference = graph()
        reference["bindings"].append(binding(slot=2))
        self.assertEqual(p.compare(reference, graph())["metrics"]["bindings"]["false_negative"], 1)
        candidate = graph()
        candidate["bindings"][0]["stage"] = "vertex"
        self.assertEqual(p.compare(graph(), candidate)["metrics"]["bindings"]["false_negative"], 1)

    def test_stage_alias_normalization(self):
        candidate = graph()
        candidate["bindings"][0]["stage"] = "PS"
        self.assertEqual(p.compare(graph(), candidate)["metrics"]["bindings"]["f1"], 1)

    def test_missing_collections_are_unavailable_empty_claims_are_measurable(self):
        candidate = graph()
        candidate.pop("bindings")
        metric = p.compare(graph(), candidate)["metrics"]["bindings"]
        self.assertEqual(metric["status"], "unavailable")
        self.assertIsNone(metric["f1"])
        candidate["bindings"] = []
        metric = p.compare(graph(), candidate)["metrics"]["bindings"]
        self.assertEqual(metric["f1"], 0)
        self.assertEqual(metric["recall"], 0)
        self.assertIsNone(metric["precision"])
        reference = graph(); reference["bindings"] = []
        metric = p.compare(reference, candidate)["metrics"]["bindings"]
        self.assertIsNone(metric["f1"])

    def test_candidate_cannot_hide_wrong_claims_by_setting_unknown(self):
        candidate = graph()
        candidate["bindings"][0].update(resource_id="wrong", verification="unknown", evidence=[])
        self.assertEqual(p.compare(graph(), candidate)["metrics"]["bindings"]["false_positive"], 1)

    def test_reference_unverified_claims_are_excluded(self):
        reference = graph()
        reference["bindings"][0]["verification"] = "inferred"
        result = p.compare(reference, graph())
        self.assertEqual(result["metrics"]["bindings"]["reference_count"], 1)
        self.assertEqual(result["reference_excluded"]["unverified_reference_bindings"], 1)

    def test_restricted_producer_mismatch_and_unknown_values(self):
        reference = graph(); candidate = graph()
        reference["producer_links"] = [producer()]
        candidate["producer_links"] = [producer(10)]
        metric = p.compare(reference, candidate)["metrics"]["restricted_producers"]
        self.assertEqual(metric["f1"], 0)
        self.assertEqual(metric["false_positive"], 1)
        candidate["producer_links"][0]["producer_action_event_id"] = None
        metric = p.compare(reference, candidate)["metrics"]["restricted_producers"]
        self.assertEqual(metric["candidate_unknown_producer_count"], 1)
        self.assertEqual(metric["false_negative"], 1)

    def test_partial_cumulative_and_unknown_producers_never_become_truth(self):
        for changes, reason in [({"coverage": "partial"}, "unknown_or_partial_write_coverage"),
                                ({"semantics": "cumulative"}, "nonexclusive_or_unknown_semantics"),
                                ({"producer_action_event_id": None}, "unknown_producer"),
                                ({"producer_action_event_id": 31}, "noncausal_reference_link")]:
            reference = graph(); link = producer(); link.update(changes)
            reference["producer_links"] = [link]
            candidate = graph(); candidate["producer_links"] = [producer(10)]
            metric = p.compare(reference, candidate)["metrics"]["restricted_producers"]
            self.assertIsNone(metric["f1"])
            self.assertEqual(metric["reference_excluded_reasons"][reason], 1)
            self.assertEqual(metric["candidate_links_outside_verified_scope"], 1)

    def test_ambiguous_verified_producers_are_not_arbitrarily_selected(self):
        reference = graph(); reference["producer_links"] = [producer(10), producer(20)]
        metric = p.compare(reference, reference)["metrics"]["restricted_producers"]
        self.assertIsNone(metric["f1"])
        self.assertEqual(metric["reference_excluded_reasons"]["ambiguous_reference_binding_scopes"], 1)

    def test_resource_adapter_ignores_versions_and_attachment_writes(self):
        raw = {"schema_version": 2, "draws": [{"action_event_id": 30, "evidence": "capture:30.json"}],
               "versions": [{"version_id": "ResourceId::7@20", "write_enabled_action_event_id": 20}],
               "edges": [{**{key: binding()[key] for key in p.IDENTITY}, "access": "shader_read", "source_version": "ResourceId::7@20", "subresource": {"binding_reported": binding()["binding_range"]}},
                         {"access": "read_modify_write", "source_action_event_id": 20, "actual_pixel_writes_verified": False},
                         {"access": "attachment_binding_write_disabled", "source_action_event_id": 30}]}
        normalized = p.normalize(raw)
        self.assertEqual(normalized["pass_granularity"], "action")
        self.assertEqual(len(normalized["bindings"]), 1)
        self.assertIsNone(normalized["producer_links"])
        self.assertIsNone(p.compare(raw, raw)["metrics"]["restricted_producers"]["f1"])
        self.assertEqual(normalized["adapter"]["ignored_edge_counts"]["read_modify_write"], 1)

    def test_invalid_types_and_incomplete_identity_are_rejected(self):
        for changes in [{"consumer_action_event_id": True}, {"binding_slot": -1}, {"resource_id": None}, {"stage": "unknown"}]:
            candidate = graph(); candidate["bindings"][0].update(changes)
            with self.assertRaises(p.PipelineError): p.compare(graph(), candidate)
        candidate = graph(); candidate["bindings"][0]["binding_range"]["num_mips"] = 0
        with self.assertRaises(p.PipelineError): p.compare(graph(), candidate)
        candidate = graph(); del candidate["bindings"][0]["consumer_action_event_id"]
        with self.assertRaises(p.PipelineError): p.compare(graph(), candidate)

    def test_bad_pass_sequences_and_duplicate_ids_rejected(self):
        for sequence in [["shadow", "shadow"], ["not-declared"]]:
            candidate = graph(); candidate["pass_sequence"] = sequence
            with self.assertRaises(p.PipelineError): p.compare(graph(), candidate)
        candidate = graph(); candidate["passes"].append(copy.deepcopy(candidate["passes"][0]))
        with self.assertRaises(p.PipelineError): p.compare(graph(), candidate)

    def test_atomic_actions_do_not_claim_semantic_pass_accuracy(self):
        candidate = graph(); candidate["pass_granularity"] = "action"
        result = p.compare(graph(), candidate)
        self.assertIsNone(result["metrics"]["passes"]["f1"])
        self.assertEqual(result["metrics"]["bindings"]["f1"], 1)

    def test_cli_no_overwrite_and_json_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); source = root / "input.json"; output = root / "output.json"
            source.write_text(json.dumps(graph()), encoding="utf-8")
            self.assertEqual(p.main(["compare", str(source), str(source), "--out", str(output)]), 0)
            original = source.read_bytes(); saved = output.read_bytes()
            self.assertEqual(p.main(["normalize", str(source), "--out", str(source)]), 2)
            self.assertEqual(p.main(["normalize", str(source), "--out", str(output)]), 2)
            self.assertEqual(source.read_bytes(), original); self.assertEqual(output.read_bytes(), saved)
            for bad in ['{"key":1,"key":2}', '{"x":NaN}', '{"incomplete":']:
                source.write_text(bad, encoding="utf-8")
                with self.assertRaises(p.PipelineError): p.read_json(source)


if __name__ == "__main__":
    unittest.main()
