"""Exercise the live Bridge against an already-open MOBILE remote capture.

Run from the repository root with --event-id and a NEW --output-dir. The Bridge
must be enabled. This never opens/closes a capture or switches replay devices.
Every replacement made by this validation is reverted in finally.
"""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import sys
import traceback

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mcp_server.bridge.client import RenderDocBridge, RenderDocBridgeError


def validate(event_id, output, shared_candidates=()):
    bridge = RenderDocBridge()
    bridge.timeout = 120.0
    report = {"event_id": event_id, "completed": False}
    edit_id = None

    def save_report():
        (output / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    def pixels(event, label=None):
        pipeline = bridge.call("get_pipeline_state", {"event_id": event})
        target = next(t["resource_id"] for t in pipeline["output_textures"] if t["type"] == "render_target")
        data = bridge.call("get_texture_data", {"resource_id": target})
        digest = hashlib.sha256(base64.b64decode(data["content_base64"])).hexdigest()
        if label:
            bridge.call("save_texture", {"resource_id": target, "output_path": str(output / (label + ".png"))})
        return digest

    def apply(source, name):
        result = bridge.call("replace_shader", {"edit_id": edit_id, "source_text": source})
        report[name] = result
        save_report()
        if result["last_attempt_status"] != "applied":
            raise RuntimeError(name + " failed to apply; see compiler log")
        return result

    try:
        status = bridge.call("get_capture_status")
        report["capture"] = status
        if not status.get("loaded") or status.get("remote_replay") is not True:
            raise RuntimeError("A loaded mobile remote replay capture is required")
        existing = bridge.call("list_shader_replacements")
        if existing["total_count"] or any(e["conflict"] for e in existing["sessions"]):
            raise RuntimeError("Restore existing shader edits before running validation")
        edit = bridge.call("get_shader_edit_context", {"event_id": event_id, "stage": "pixel", "mode": "glsl"})
        edit_id = edit["edit_id"]
        if edit["remote_replay"] is not True:
            raise RuntimeError("Edit is not attached to remote replay")
        report["context"] = {k: v for k, v in edit.items() if k not in ("source_text", "applied_source_text")}
        source = edit["source_text"]
        save_report()
        bridge.call("export_shader_source", {"edit_id": edit_id, "output_path": str(output / "initial.glsl")})
        # Keep validation bounded; a full-frame resource search can be expensive on a phone.
        candidates = [candidate for candidate in shared_candidates if candidate != event_id]
        other_events = []
        for candidate in sorted(candidates, key=lambda e: abs(e - event_id))[:24]:
            state = bridge.call("get_pipeline_state", {"event_id": candidate})
            if (state.get("shaders", {}).get("pixel", {}).get("resource_id") == edit["resource_id"]
                    and any(t["type"] == "render_target" for t in state.get("output_textures", []))):
                other_events.append(candidate)
                if len(other_events) == 2:
                    break
        report["shared_shader_event_ids"] = [event_id] + other_events
        other_before = {e: pixels(e) for e in other_events}
        before = pixels(event_id, "before")
        report["before_sha256"] = before
        save_report()
        apply(source, "roundtrip")
        roundtrip = pixels(event_id)
        report["roundtrip_equal"] = roundtrip == before
        failed = bridge.call("replace_shader", {"edit_id": edit_id, "source_text": "INVALID SHADER SOURCE"})
        report["compile_failure"] = failed
        report["failure_preserves_replacement"] = (failed["last_attempt_status"] == "compile_failed"
                                                     and failed["applied"] and pixels(event_id) == roundtrip)
        apply(source, "repeat")
        outputs = re.findall(r"\bout\s+(?:(?:highp|mediump|lowp)\s+)?vec4\s+(\w+)\s*(?:;|$)",
                             source, re.MULTILINE)
        variable = outputs[0] if outputs else ("gl_FragColor" if "gl_FragColor" in source else None)
        if not variable:
            raise RuntimeError("Validation requires a pixel shader with a vec4 output")
        modified, count = re.subn(r"\bvoid\s+main\s*\(", "void mcp_original_main(", source, count=1)
        if count != 1:
            raise RuntimeError("Could not find GLSL main entry")
        modified += "\nvoid main() { mcp_original_main(); %s = vec4(1,0,1,1); }\n" % variable
        apply(modified, "color_edit")
        report["modified_sha256"] = pixels(event_id, "modified")
        report["color_pixels_changed"] = report["modified_sha256"] != before
        report["shared_shader_changed_events"] = [e for e in other_events if pixels(e) != other_before[e]]
        bridge.call("export_shader_source", {"edit_id": edit_id, "output_path": str(output / "modified.glsl")})
        try:
            bridge.call("export_shader_source", {"edit_id": edit_id, "output_path": str(output / "modified.glsl")})
        except RenderDocBridgeError as exc:
            report["export_refuses_overwrite"] = "OUTPUT_FILE_EXISTS" in str(exc)
        else:
            report["export_refuses_overwrite"] = False
        bridge.call("revert_shader", {"edit_id": edit_id})
        bridge.call("revert_shader", {"edit_id": edit_id})
        report["restored_sha256"] = pixels(event_id, "restored")
        report["restored_equal"] = report["restored_sha256"] == before
        if edit["original_encoding"] in ("SPIRV", "OpenGLSPIRV"):
            assembly = bridge.call("get_shader_edit_context", {"event_id": event_id, "stage": "pixel", "mode": "spirv_asm"})
            edit_id = assembly["edit_id"]
            bridge.call("export_shader_source", {"edit_id": edit_id, "output_path": str(output / "initial.spvasm")})
            apply(assembly["source_text"], "assembly")
            report["assembly_equal"] = pixels(event_id) == before
            bridge.call("revert_shader", {"edit_id": edit_id})
        report["completed"] = True
    except Exception:
        report["error"] = traceback.format_exc()
    finally:
        if edit_id:
            try:
                report["final_revert"] = bridge.call("revert_shader", {"edit_id": edit_id})
                report["final_state"] = bridge.call("list_shader_replacements")
            except Exception:
                report["cleanup_error"] = traceback.format_exc()
        save_report()
    required = ["roundtrip_equal", "failure_preserves_replacement", "color_pixels_changed",
                "export_refuses_overwrite", "restored_equal"]
    if report.get("context", {}).get("original_encoding") in ("SPIRV", "OpenGLSPIRV"):
        required.append("assembly_equal")
    report["passed"] = (report["completed"] and all(report.get(key) is True for key in required)
                        and "cleanup_error" not in report
                        and report.get("final_state", {}).get("total_count") == 0)
    save_report()
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event-id", type=int, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--shared-event-ids", type=int, nargs="*", default=[],
                        help="Optional draws to verify as users of the same pixel shader")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = validate(args.event_id, output, args.shared_event_ids)
    print(json.dumps({k: v for k, v in result.items() if isinstance(v, (bool, str, int))}, ensure_ascii=False, indent=2))
    sys.exit(0 if result["passed"] else 1)
