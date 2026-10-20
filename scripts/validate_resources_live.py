"""Read-only Resource Inspector smoke check against an already-loaded capture.

Install/reload the updated extension first. No capture is opened, no event is
selected and no resource is modified. Prints a JSON report for UI comparison.
"""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mcp_server.bridge.client import RenderDocBridge


def validate(resource_id=None):
    bridge = RenderDocBridge()
    report = {"capture": bridge.call("get_capture_status")}
    if not report["capture"].get("loaded"):
        raise RuntimeError("Open a capture in RenderDoc before running this check")
    report["directory"] = bridge.call("list_resources", {"limit": 10})
    if resource_id is None:
        buffers = bridge.call("list_resources", {"resource_type": "buffer", "limit": 1})
        candidates = buffers["items"] or report["directory"]["items"]
        if not candidates:
            raise RuntimeError("The loaded capture contains no resources")
        resource_id = candidates[0]["resource_id"]
    args = {"resource_id": resource_id}
    report["inspection"] = bridge.call("inspect_resource", args)
    report["usage"] = bridge.call("trace_resource_usage", dict(args, limit=10))
    directory = bridge.call("get_resource_initialization", dict(args, limit=5))
    report["initialization"] = directory
    first = next((item for item in directory["items"] if "error" not in item), None)
    if first is not None:
        report["parameters"] = bridge.call(
            "get_resource_initialization", dict(args, chunk_index=first["chunk_index"], limit=10))
    related = report["inspection"]["related_resources"]["items"]
    first = next((item for item in related if not item.get("missing")), None)
    if first is not None:
        report["related_inspection"] = bridge.call(
            "inspect_resource", {"resource_id": first["resource_id"]})
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resource-id", help="Use the resource selected in the Resource Inspector")
    args = parser.parse_args()
    print(json.dumps(validate(args.resource_id), indent=2, ensure_ascii=False, allow_nan=False))
