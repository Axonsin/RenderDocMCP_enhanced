"""Run inside RenderDoc's Python UI with the validation RDC already loaded.

Independent native evidence only: no MCP imports, no shader edits. Change EIDS
for another capture. Output lives in the temporary IPC evidence directory.
"""
import json
import os
import struct
import tempfile

import renderdoc as rd

EIDS = (169, 633, 949, 961, 1942)
OUTPUT = os.path.join(tempfile.gettempdir(), "renderdoc_mcp", "postvs_native_repro.json")


def collect(ctx):
    if not ctx.IsCaptureLoaded():
        raise RuntimeError("Load the validation RDC before running this script")
    original = ctx.CurEvent()
    result = {"renderdoc_version": rd.GetVersionString(), "capture": ctx.GetCaptureFilename(),
              "original_event": original, "source": "independent_native_replay_callback", "draws": []}

    def read(controller):
        try:
            for eid in EIDS:
                row = {"action_event_id": eid}
                try:
                    action = ctx.GetAction(eid)
                    if action is None or not action.flags & rd.ActionFlags.Drawcall:
                        raise ValueError("not a draw in this capture")
                    controller.SetFrameEvent(eid, True)
                    mesh = controller.GetPostVSData(0, 0, rd.MeshDataStage.VSOut)
                    row["format"] = {key: str(getattr(mesh, key)) for key in (
                        "vertexResourceId", "vertexByteOffset", "vertexByteStride", "indexResourceId",
                        "indexByteOffset", "indexByteStride", "baseVertex", "numIndices", "status")}
                    count = min(12, mesh.numIndices)
                    if mesh.indexResourceId != rd.ResourceId.Null():
                        code = {1: "B", 2: "H", 4: "I"}[mesh.indexByteStride]
                        raw = bytes(controller.GetBufferData(mesh.indexResourceId, mesh.indexByteOffset,
                                                             count * mesh.indexByteStride))
                        indices = [i + mesh.baseVertex for i in struct.unpack("<%d%s" % (count, code), raw)]
                    else:
                        indices = list(range(count))
                    positions = []
                    for index in indices:
                        raw = bytes(controller.GetBufferData(mesh.vertexResourceId,
                            mesh.vertexByteOffset + index * mesh.vertexByteStride, 16))
                        positions.append(list(struct.unpack("<4f", raw)))
                    row.update(indices=indices, position_xyzw=positions,
                               distinct_positions=len(set(tuple(p) for p in positions)))
                except Exception as exc:
                    row["error"] = str(exc)
                result["draws"].append(row)
        finally:
            controller.SetFrameEvent(original, True)

    ctx.Replay().BlockInvoke(read)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
    print("Native post-VS evidence: " + OUTPUT)


if "pyrenderdoc" in globals():
    collect(pyrenderdoc)
