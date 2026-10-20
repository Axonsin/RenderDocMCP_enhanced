"""Read-only comparison report for an already-loaded capture and updated extension.

No installation, capture opening, image export or UI event selection is performed.
Pipeline queries temporarily replay the action and restore the UI's replay event.
"""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mcp_server.bridge.client import RenderDocBridge


def validate(action_event_id, stage):
    bridge = RenderDocBridge()
    report = {"capture": bridge.call("get_capture_status")}
    if not report["capture"].get("loaded"):
        raise RuntimeError("Open a capture and reload the updated extension first")
    args = {"action_event_id": action_event_id}
    report["overview"] = bridge.call("get_pipeline_state", args)
    report["stage"] = bridge.call("get_pipeline_stage", dict(args, stage=stage))
    report["sections"] = {}
    for name in report["stage"].get("sections", {}):
        report["sections"][name] = bridge.call(
            "get_pipeline_stage", dict(args, stage=stage, section=name, limit=10))
    report["textures"] = bridge.call("get_action_textures", dict(args, limit=20))
    constants = report["sections"].get("constant_buffers", {}).get("items", [])
    if constants:
        binding = constants[0]
        report["binding"] = bridge.call(
            "inspect_pipeline_binding", dict(args, binding_id=binding["binding_id"]))
        report["variables"] = bridge.call(
            "inspect_pipeline_binding",
            dict(args, binding_id=binding["binding_id"], section="variables", limit=10))
    rows = report["textures"]["items"]
    resource = next((row["resource"] for row in rows if row.get("resource")), None)
    if resource:
        reference = {"resource_id": resource["resource_id"]}
        report["resource"] = bridge.call("inspect_resource", reference)
        report["usage"] = bridge.call("trace_resource_usage", dict(reference, limit=10))
        report["initialization"] = bridge.call("get_resource_initialization", dict(reference, limit=5))
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--action-event-id", type=int, required=True)
    parser.add_argument("--stage", default="FS")
    options = parser.parse_args()
    print(json.dumps(validate(options.action_event_id, options.stage),
                     ensure_ascii=False, indent=2, allow_nan=False))
