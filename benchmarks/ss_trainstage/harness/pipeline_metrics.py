"""Deterministic set diagnostics for pipeline structure; never assigns rubric scores.

Canonical JSON (kind=pipeline_graph, schema_version=1):
  scope: {description: str, complete: bool}; pass_granularity: semantic | action
  passes: [{pass_id: str, action_event_ids: [positive int],
            verification: verified | inferred | unknown, evidence: [str]}] | null
  pass_sequence: [pass_id, ...] | null
  sequence_verification: verified | inferred | unknown; sequence_evidence: [str]
  bindings: [{consumer_action_event_id: int, resource_id: str, stage: str,
              binding_slot: int, binding_range: {first_mip, num_mips,
              first_slice, num_slices}, verification: ..., evidence: [str]}] | null
  producer_links: [{binding: <binding record>, producer_action_event_id: int|null,
                    coverage: full_binding_range | partial | unknown,
                    semantics: single_complete_overwrite | cumulative | unknown,
                    verification: ..., evidence: [str]}] | null

Omitted collections mean unavailable; [] is an explicit empty claim. Range fields
may be null/missing, but unknown never matches a known range. Reference records
need verification=verified and nonempty evidence. Candidate confidence does not
hide its claims. Pass IDs must come from an agreed ontology: no name guessing.
The adapter for oracle resource graphs v1/v2 uses only observed shader_read
bindings and draw order (atomic actions, NOT semantic pass classification).
Versions and write-enabled transitions NEVER establish exclusive producers.
Evidence strings are provenance references, not evidence authenticity checks.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Any


class PipelineError(ValueError):
    """Invalid or ambiguous input; no results are silently invented."""


IDENTITY = ("consumer_action_event_id", "resource_id", "stage", "binding_slot")
RANGE = ("first_mip", "num_mips", "first_slice", "num_slices")
VERIFY = {"verified", "inferred", "unknown"}
STAGES = {
    "vs": "vertex", "vertex": "vertex", "ps": "fragment", "fs": "fragment",
    "pixel": "fragment", "fragment": "fragment", "cs": "compute", "compute": "compute",
    "gs": "geometry", "geometry": "geometry", "hs": "tess_control", "hull": "tess_control",
    "tess_control": "tess_control", "ds": "tess_eval", "domain": "tess_eval",
    "tess_eval": "tess_eval", "task": "task", "mesh": "mesh",
}
MAX_PASSES = 512  # all ordered pairs are explicit and inspectable in the output


def _object(value, where):
    if not isinstance(value, dict):
        raise PipelineError(f"{where} must be an object")
    return value


def _text(value, where):
    if not isinstance(value, str) or not value.strip():
        raise PipelineError(f"{where} must be a nonempty string")
    return value


def _int(value, where, minimum=0):
    if type(value) is not int or value < minimum:
        raise PipelineError(f"{where} must be an integer >= {minimum}")
    return value


def _list(value, where):
    if not isinstance(value, list):
        raise PipelineError(f"{where} must be an array")
    return value


def _evidence(value, where):
    return sorted(set(_text(x, where) for x in _list(value, where)))


def _verification(value, where):
    if not isinstance(value, str) or value not in VERIFY:
        raise PipelineError(f"{where} must be verified, inferred or unknown")
    return value


def _verified(row):
    return row["verification"] == "verified" and bool(row["evidence"])


def _binding(value, where):
    row = _object(value, where)
    stage = _text(row.get("stage"), f"{where}.stage").lower()
    if stage not in STAGES:
        raise PipelineError(f"{where}.stage is unsupported: {stage}")
    ranges = row.get("binding_range")
    if ranges is None:
        ranges = {}
    _object(ranges, f"{where}.binding_range")
    result = {
        "consumer_action_event_id": _int(row.get("consumer_action_event_id"), f"{where}.consumer_action_event_id", 1),
        "resource_id": _text(row.get("resource_id"), f"{where}.resource_id"),
        "stage": STAGES[stage],
        "binding_slot": _int(row.get("binding_slot"), f"{where}.binding_slot"),
        "binding_range": {k: None if ranges.get(k) is None else _int(ranges[k], f"{where}.binding_range.{k}", 1 if k.startswith("num_") else 0) for k in RANGE},
        "verification": _verification(row.get("verification", "unknown"), f"{where}.verification"),
        "evidence": _evidence(row.get("evidence", []), f"{where}.evidence"),
    }
    return result


def adapt_resource_graph(raw):
    """Capture adapter; deliberately ignores source_version and all write edges."""
    _object(raw, "graph")
    if type(raw.get("schema_version")) is not int or raw["schema_version"] not in (1, 2):
        raise PipelineError("resource graph schema_version must be 1 or 2")
    draws = _list(raw.get("draws"), "draws")
    edges = _list(raw.get("edges"), "edges")
    passes = []
    draw_evidence = {}
    for i, row in enumerate(draws):
        _object(row, f"draws[{i}]")
        eid = _int(row.get("action_event_id"), f"draws[{i}].action_event_id", 1)
        evidence = row.get("evidence")
        evidence = [_text(evidence, f"draws[{i}].evidence")] if evidence else []
        draw_evidence[eid] = evidence
        passes.append({"pass_id": f"action:{eid}", "action_event_ids": [eid], "verification": "verified", "evidence": evidence})
    bindings = []
    ignored = Counter()
    for i, edge in enumerate(edges):
        _object(edge, f"edges[{i}]")
        if edge.get("access") != "shader_read":
            ignored[str(edge.get("access", "missing_access"))] += 1
            continue
        subresource = edge.get("subresource")
        if subresource is None:
            subresource = {}
        _object(subresource, f"edges[{i}].subresource")
        bindings.append({**{k: edge.get(k) for k in IDENTITY},
                         "binding_range": subresource.get("binding_reported"),
                         "verification": "verified",
                         "evidence": draw_evidence.get(edge.get("consumer_action_event_id"), [])})
    return {
        "kind": "pipeline_graph", "schema_version": 1,
        "scope": {"description": str(raw.get("scope", "Observed capture bindings")), "complete": False},
        "pass_granularity": "action", "passes": passes,
        "pass_sequence": [p["pass_id"] for p in passes],
        "sequence_verification": "verified",
        "sequence_evidence": sorted({e for p in passes for e in p["evidence"]}),
        "bindings": bindings, "producer_links": None,
        "adapter": {"source_schema_version": raw["schema_version"],
                    "ignored_edge_counts": dict(sorted(ignored.items())),
                    "version_records_not_promoted_to_producers": len(_list(raw.get("versions", []), "versions")),
                    "note": "Atomic draw coverage/order only. Cumulative versions, partial writes, disabled attachments, clears and unknown writers are not exclusive producer truth."},
    }


def normalize(data):
    _object(data, "graph")
    if data.get("kind") != "pipeline_graph":
        data = adapt_resource_graph(data)
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise PipelineError("canonical schema_version must be 1")
    scope = _object(data.get("scope", {}), "scope")
    complete = scope.get("complete", False)
    if type(complete) is not bool:
        raise PipelineError("scope.complete must be boolean")
    granularity = data.get("pass_granularity", "semantic")
    if granularity not in ("semantic", "action"):
        raise PipelineError("pass_granularity must be semantic or action")
    out = {"kind": "pipeline_graph", "schema_version": 1,
           "scope": {"description": str(scope.get("description", "Unspecified scope")), "complete": complete},
           "pass_granularity": granularity}
    if "adapter" in data:
        out["adapter"] = data["adapter"]
    passes = data.get("passes")
    out["passes"] = None
    if passes is not None:
        _list(passes, "passes")
        if len(passes) > MAX_PASSES:
            raise PipelineError(f"passes exceeds explicit ordered-pair limit {MAX_PASSES}")
        out["passes"] = []
        seen = set()
        for i, row in enumerate(passes):
            _object(row, f"passes[{i}]")
            pid = _text(row.get("pass_id"), f"passes[{i}].pass_id")
            if pid in seen:
                raise PipelineError(f"duplicate pass_id: {pid}")
            seen.add(pid)
            eids = row.get("action_event_ids")
            out["passes"].append({"pass_id": pid,
                "action_event_ids": None if eids is None else sorted(set(_int(x, f"passes[{i}].action_event_ids", 1) for x in _list(eids, f"passes[{i}].action_event_ids"))),
                "verification": _verification(row.get("verification", "unknown"), f"passes[{i}].verification"),
                "evidence": _evidence(row.get("evidence", []), f"passes[{i}].evidence")})
    sequence = data.get("pass_sequence")
    out["pass_sequence"] = None
    if sequence is not None:
        sequence = [_text(p, "pass_sequence item") for p in _list(sequence, "pass_sequence")]
        if passes is None or len(set(sequence)) != len(sequence) or not set(sequence) <= {p["pass_id"] for p in out["passes"]}:
            raise PipelineError("pass_sequence must contain unique declared pass IDs")
        out["pass_sequence"] = sequence
    out["sequence_verification"] = _verification(data.get("sequence_verification", "unknown"), "sequence_verification")
    out["sequence_evidence"] = _evidence(data.get("sequence_evidence", []), "sequence_evidence")
    bindings = data.get("bindings")
    out["bindings"] = None if bindings is None else [_binding(b, f"bindings[{i}]") for i, b in enumerate(_list(bindings, "bindings"))]
    links = data.get("producer_links")
    out["producer_links"] = None
    if links is not None:
        out["producer_links"] = []
        for i, row in enumerate(_list(links, "producer_links")):
            _object(row, f"producer_links[{i}]")
            producer = row.get("producer_action_event_id")
            coverage = row.get("coverage", "unknown")
            semantics = row.get("semantics", "unknown")
            if coverage not in ("full_binding_range", "partial", "unknown") or semantics not in ("single_complete_overwrite", "cumulative", "unknown"):
                raise PipelineError(f"producer_links[{i}] has invalid coverage or semantics")
            out["producer_links"].append({"binding": _binding(row.get("binding"), f"producer_links[{i}].binding"),
                "producer_action_event_id": None if producer is None else _int(producer, f"producer_links[{i}].producer_action_event_id", 1),
                "coverage": coverage, "semantics": semantics,
                "verification": _verification(row.get("verification", "unknown"), f"producer_links[{i}].verification"),
                "evidence": _evidence(row.get("evidence", []), f"producer_links[{i}].evidence")})
    return out


def _key(row, with_range=False):
    key = tuple(row[k] for k in IDENTITY)
    return key + tuple(row["binding_range"][k] for k in RANGE) if with_range else key


def _range_known(row):
    return all(row["binding_range"][k] is not None for k in RANGE)


def _sort_key(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def set_metric(reference, candidate, fields):
    """Precision is null for no claims, recall null for no reference facts."""
    if reference is None or candidate is None:
        return {"status": "unavailable", "reason": "Reference or candidate collection was not supplied/verified",
                "precision": None, "recall": None, "f1": None,
                "reference_count": None if reference is None else len(set(reference)),
                "candidate_count": None if candidate is None else len(set(candidate))}
    r, c = set(reference), set(candidate)
    tp, fp, fn = len(r & c), len(c - r), len(r - c)
    def rows(keys):
        return [dict(zip(fields, key)) for key in sorted(keys, key=_sort_key)]
    return {"status": "available" if r or c else "empty", "reference_count": len(r), "candidate_count": len(c),
            "true_positive": tp, "false_positive": fp, "false_negative": fn,
            "precision": tp / len(c) if c else None, "recall": tp / len(r) if r else None,
            "f1": 2 * tp / (2 * tp + fp + fn) if r or c else None,
            "missing_reference": rows(r - c), "unmatched_candidate": rows(c - r)}


def _ordered_pairs(sequence):
    return [(a, b) for i, a in enumerate(sequence) for b in sequence[i+1:]]


def compare(reference, candidate):
    r, c = normalize(reference), normalize(candidate)
    excluded = {}
    rp = None if r["passes"] is None else [p for p in r["passes"] if _verified(p)]
    cp = c["passes"]
    excluded["unverified_reference_passes"] = 0 if r["passes"] is None else len(r["passes"]) - len(rp)
    same_granularity = r["pass_granularity"] == c["pass_granularity"]
    pass_ids = set_metric(None if rp is None or not same_granularity else [(p["pass_id"],) for p in rp],
                          None if cp is None else [(p["pass_id"],) for p in cp], ("pass_id",))
    if not same_granularity:
        pass_ids["reason"] = "Different pass_granularity; semantic passes cannot be compared to atomic draw IDs"
    membership = set_metric(None if rp is None or not same_granularity else [(p["pass_id"], eid) for p in rp if p["action_event_ids"] is not None for eid in p["action_event_ids"]],
                            None if cp is None else [(p["pass_id"], eid) for p in cp if p["action_event_ids"] is not None for eid in p["action_event_ids"]], ("pass_id", "action_event_id"))
    membership["reference_passes_with_unknown_membership"] = None if rp is None else sum(p["action_event_ids"] is None for p in rp)
    membership["candidate_passes_with_unknown_membership"] = None if cp is None else sum(p["action_event_ids"] is None for p in cp)
    sequence_verified = r["sequence_verification"] == "verified" and bool(r["sequence_evidence"])
    rs = None if r["pass_sequence"] is None or rp is None or not sequence_verified or not same_granularity else [p for p in r["pass_sequence"] if p in {v["pass_id"] for v in rp}]
    cs = c["pass_sequence"]
    r_pairs = None if rs is None else _ordered_pairs(rs)
    c_pairs = None if cs is None else _ordered_pairs(cs)
    order = set_metric(r_pairs, c_pairs, ("before_pass_id", "after_pass_id"))
    inversions = [] if r_pairs is None or c_pairs is None else sorted(set(r_pairs) & {(b, a) for a, b in c_pairs}, key=_sort_key)
    order["reversed_reference_pairs"] = [{"before_pass_id": a, "after_pass_id": b} for a, b in inversions]
    order["inversion_count"] = None if r_pairs is None or c_pairs is None else len(inversions)
    order["reference_sequence_count"] = None if rs is None else len(rs)
    order["candidate_sequence_count"] = None if cs is None else len(cs)
    rb = None if r["bindings"] is None else [b for b in r["bindings"] if _verified(b)]
    cb = c["bindings"]
    excluded["unverified_reference_bindings"] = 0 if r["bindings"] is None else len(r["bindings"]) - len(rb)
    bindings = set_metric(None if rb is None else [_key(b) for b in rb], None if cb is None else [_key(b) for b in cb], IDENTITY)
    known_ids = set() if rb is None else {_key(b) for b in rb if _range_known(b)}
    ranged = set_metric(None if rb is None else [_key(b, True) for b in rb if _range_known(b)],
                        None if cb is None else [_key(b, True) for b in cb if _key(b) in known_ids], IDENTITY + RANGE)
    ranged["scope"] = "Only identities whose reference binding range is fully known; extra identities remain in bindings"
    ranged["reference_unknown_range_count"] = None if rb is None else sum(not _range_known(b) for b in rb)
    ranged["candidate_unknown_range_count"] = None if cb is None else sum(not _range_known(b) for b in cb)
    ranged["candidate_outside_known_reference_identity_count"] = None if cb is None else sum(_key(b) not in known_ids for b in cb)
    duplicate_counts = {"reference_bindings": None if rb is None else len(rb)-len({_key(b, True) for b in rb}),
                        "candidate_bindings": None if cb is None else len(cb)-len({_key(b, True) for b in cb})}
    producer_exclusions = Counter()
    eligible = []
    for link in r["producer_links"] or []:
        reason = None
        if not _verified(link) or not _verified(link["binding"]): reason = "unverified_or_missing_evidence"
        elif link["producer_action_event_id"] is None: reason = "unknown_producer"
        elif link["coverage"] != "full_binding_range": reason = "unknown_or_partial_write_coverage"
        elif link["semantics"] != "single_complete_overwrite": reason = "nonexclusive_or_unknown_semantics"
        elif not _range_known(link["binding"]): reason = "unknown_binding_range"
        elif link["producer_action_event_id"] >= link["binding"]["consumer_action_event_id"]: reason = "noncausal_reference_link"
        if reason: producer_exclusions[reason] += 1
        else: eligible.append(link)
    scopes = {}
    for link in eligible:
        scopes.setdefault(_key(link["binding"], True), set()).add(link["producer_action_event_id"])
    ambiguous = {key for key, producers in scopes.items() if len(producers) != 1}
    producer_exclusions["ambiguous_reference_binding_scopes"] = len(ambiguous)
    scopes = {key: next(iter(producers)) for key, producers in scopes.items() if key not in ambiguous}
    c_links = c["producer_links"]
    c_scoped = [] if c_links is None else [link for link in c_links if _key(link["binding"], True) in scopes]
    producers = set_metric([key+(producer,) for key, producer in scopes.items()] if scopes else None,
                           None if c_links is None else [_key(link["binding"], True)+(link["producer_action_event_id"],) for link in c_scoped], IDENTITY+RANGE+("producer_action_event_id",))
    producers.update({"scope": "Restricted to evidenced single complete overwrite of the entire known binding range; never inferred from cumulative versions",
                      "eligible_reference_binding_scopes": len(scopes), "reference_excluded_reasons": dict(sorted(producer_exclusions.items())),
                      "candidate_links_outside_verified_scope": None if c_links is None else len(c_links)-len(c_scoped),
                      "candidate_unknown_producer_count": None if c_links is None else sum(link["producer_action_event_id"] is None for link in c_links),
                      "candidate_noncausal_link_count": None if c_links is None else sum(link["producer_action_event_id"] is not None and link["producer_action_event_id"] >= link["binding"]["consumer_action_event_id"] for link in c_links)})
    return {"schema_version": 1, "kind": "pipeline_diagnostics", "reference_scope": r["scope"],
            "candidate_scope": c["scope"], "reference_adapter": r.get("adapter"), "candidate_adapter": c.get("adapter"),
            "metrics": {"passes": pass_ids, "pass_membership": membership, "order": order,
                        "bindings": bindings, "binding_ranges": ranged, "restricted_producers": producers},
            "reference_excluded": excluded, "duplicate_records": duplicate_counts,
            "limitations": ["Set agreement is diagnostic only; no rubric score or acceptance decision is produced.",
                "FP means unmatched candidate claims within this comparison, not proven false statements when reference coverage is incomplete.",
                "Verified is supplied provenance; this tool validates its structure, not authenticity or independent review.",
                "Binding ranges are recorded API descriptor ranges, not sampled mip/slice traces. Different API representations need reviewer reconciliation; a cube binding with num_slices=1 does not prove sampling only face 0. Range disagreement is not an automatic error penalty.",
                "Missing collections and zero denominators produce null; unknown values are never wildcard matches.",
                "Pass semantics and optimization quality require independent review; atomic draw coverage does not assess those dimensions."]}


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PipelineError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=_unique_keys,
                          parse_constant=lambda s: (_ for _ in ()).throw(PipelineError(f"nonfinite JSON value: {s}")))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PipelineError(f"Cannot read JSON {path}: {exc}") from exc


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
    except OSError as exc:
        raise PipelineError(f"Cannot create output (existing files are never replaced): {path}: {exc}") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    normal = sub.add_parser("normalize", help="Normalize canonical or capture graph into explicit comparison input")
    normal.add_argument("graph", type=Path)
    normal.add_argument("--out", type=Path, required=True)
    comparing = sub.add_parser("compare", help="Compute sets; does not score or accept submissions")
    comparing.add_argument("reference", type=Path)
    comparing.add_argument("candidate", type=Path)
    comparing.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        inputs = [args.graph] if args.command == "normalize" else [args.reference, args.candidate]
        if args.out.resolve() in {path.resolve() for path in inputs}:
            raise PipelineError("Output must not replace an input")
        if args.out.exists():
            raise PipelineError("Output already exists; refusing overwrite")
        result = normalize(read_json(args.graph)) if args.command == "normalize" else compare(read_json(args.reference), read_json(args.candidate))
        result["input_provenance"] = [{"path": str(path.resolve()), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in inputs]
        write_json(args.out, result)
        print(json.dumps({"status": "written", "output": str(args.out.resolve())}, ensure_ascii=False))
        return 0
    except (PipelineError, OSError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
