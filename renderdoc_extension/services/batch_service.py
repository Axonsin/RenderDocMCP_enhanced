"""Batch dump of draw geometry and material facts in as few IPC round trips as possible.

The extension is the only place that can walk many draws cheaply: each draw still
costs one BlockInvoke, but the MCP client pays a single request. Everything here is
Python 3.6 + stdlib plus the renderdoc module.
"""

import os
import struct

import renderdoc as rd

from .pipeline_snapshot import Snapshot
from .replay_query import at_event, require_action

# Textures larger than this are almost always scene render targets rather than
# material inputs; skipping them keeps the dump small and fast.
MAX_TEXTURE_EDGE = 4096
_SKIP_FORMAT_MARKERS = ("D16", "D24", "D32", "D32S8", "S8", "DEPTH")


class BatchService(object):
    def __init__(self, ctx, invoke_fn, mesh_service):
        self.ctx = ctx
        self._invoke = invoke_fn
        self._mesh = mesh_service

    # ------------------------------------------------------------------ public

    def dump_draws(self, action_event_ids, mesh_dir=None, texture_dir=None,
                   export_meshes=True, export_textures=True, max_textures=48,
                   summary_path=None):
        """Dump meshes + material facts for a list of draw EIDs.

        Returns one entry per requested event, including failures, so the caller
        can tell "nothing to export" apart from "the draw was skipped".
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        if not isinstance(action_event_ids, (list, tuple)) or not action_event_ids:
            raise ValueError("INVALID_REQUEST: action_event_ids must be a non-empty list")
        if len(action_event_ids) > 256:
            raise ValueError("INVALID_REQUEST: at most 256 events per call")
        if export_meshes and not mesh_dir:
            raise ValueError("INVALID_REQUEST: mesh_dir is required when export_meshes")
        if export_textures and not texture_dir:
            raise ValueError("INVALID_REQUEST: texture_dir is required when export_textures")

        if export_meshes:
            _ensure_dir(mesh_dir)
        if export_textures:
            _ensure_dir(texture_dir)

        if summary_path is None and mesh_dir:
            # The MCP reply must stay small; always spill the full facts.
            summary_path = os.path.join(mesh_dir, "_batch_summary.json")

        budget = {"textures": max_textures}
        saved = {}
        draws = []
        for raw_eid in action_event_ids:
            eid = int(raw_eid)
            entry = {"action_event_id": eid}
            try:
                action = require_action(self.ctx, eid)
                entry["flags"] = _flag_names(action.flags)
                entry["index_count"] = int(action.numIndices)
                entry["instance_count"] = int(action.numInstances)
                if not (action.flags & rd.ActionFlags.Drawcall):
                    entry["skipped"] = "not_a_draw"
                    draws.append(entry)
                    continue
                if export_meshes:
                    entry["mesh"] = self._dump_mesh(eid, mesh_dir)
                entry.update(self._material_facts(eid, texture_dir if export_textures else None,
                                                  budget, saved))
                entry["ok"] = True
            except Exception as exc:  # keep the batch going; report per draw
                entry["ok"] = False
                entry["error"] = str(exc)
            draws.append(entry)

        result = {
            "draw_count": len(draws),
            "ok_count": sum(1 for d in draws if d.get("ok")),
            "failed_count": sum(1 for d in draws if d.get("ok") is False),
            "draws": draws,
            "textures": sorted(saved.values(), key=lambda t: t["resource_id"]),
            "textures_deferred": budget["textures"] <= 0,
        }
        if summary_path:
            # Full per-draw material facts are large; write them next to the
            # meshes and keep the IPC reply small.
            _ensure_dir(os.path.dirname(summary_path) or ".")
            import json as _json
            with open(summary_path, "w", encoding="utf-8") as fh:
                _json.dump(result, fh, ensure_ascii=False)
            return {
                "summary_path": summary_path,
                "draw_count": result["draw_count"],
                "ok_count": result["ok_count"],
                "failed_count": result["failed_count"],
                "textures_saved": len(result["textures"]),
                "failed": [d for d in draws if d.get("ok") is False][:5],
            }
        return result

    # ----------------------------------------------------------------- helpers

    def _dump_mesh(self, eid, mesh_dir):
        output_path = os.path.join(mesh_dir, "vsIn_%d.csv" % eid)
        info = self._mesh.export_mesh_csv(eid, output_path, "VSIn")
        return {
            "path": output_path,
            "vertex_count": info.get("vertex_count"),
            "index_count": info.get("index_count"),
            "attributes": info.get("exported_attributes"),
        }

    def _material_facts(self, eid, texture_dir, budget, saved):
        eid_box = {"value": None, "error": None}

        def operation(controller, event):
            snapshot = Snapshot(self.ctx, controller, require_action(self.ctx, eid),
                                "batch")
            eid_box["value"] = self._summarise(snapshot, controller, eid, texture_dir,
                                               budget, saved)

        at_event(self.ctx, self._invoke, eid,
                 lambda controller, event: operation(controller, event))
        if eid_box["error"]:
            raise RuntimeError(eid_box["error"])
        return eid_box["value"]

    def _summarise(self, snapshot, controller, eid, texture_dir, budget, saved):
        result = {"vertex_shader": None, "pixel_shader": None, "constants": [],
                  "textures": [], "blend": None, "depth": None}
        stages = snapshot.stages
        for key, slot in (("vertex", "vertex_shader"), ("fragment", "pixel_shader")):
            item = stages.get(key) or {}
            shader = item.get("shader") or {}
            resource = shader.get("resource") or {}
            result[slot] = resource.get("resource_id")

        for row in snapshot.bindings:
            if row.get("category") != "constant" or not row.get("bound"):
                continue
            if row.get("stage") not in ("vertex", "fragment"):
                continue
            rng = row.get("buffer_range") or {}
            result["constants"].append({
                "stage": row.get("stage"),
                "binding_name": row.get("binding_name"),
                "location": row.get("location"),
                "byte_offset": rng.get("byte_offset"),
                "byte_size": rng.get("byte_size"),
                "resource_id": (row.get("resource") or {}).get("resource_id"),
            })

        result["object_matrix"] = self._object_matrix(snapshot, controller, result["constants"])

        framebuffer = stages.get("framebuffer") or {}
        sections = framebuffer.get("sections") or {}
        if sections.get("blend", {}).get("available"):
            result["blend"] = sections["blend"].get("data")
        if sections.get("depth_stencil", {}).get("available"):
            result["depth"] = sections["depth_stencil"].get("data")

        for row in snapshot.texture_rows():
            # Texture SRVs use the read_only/read_write categories, not "resource".
            if row.get("resource_kind") != "texture" or not row.get("bound"):
                continue
            if "input" not in (row.get("roles") or []):
                continue
            if row.get("stage") not in ("vertex", "fragment"):
                continue
            resource = row.get("resource") or {}
            rid = resource.get("resource_id")
            if not rid:
                continue
            numeric = _numeric_id(rid)
            record = {"resource_id": rid, "stage": row.get("stage"),
                      "location": row.get("location")}
            path = None
            if numeric is not None and numeric in saved:
                path = saved[numeric]["file"]
                record.update({k: saved[numeric][k] for k in ("width", "height", "format")})
            elif texture_dir and budget["textures"] > 0 and numeric is not None:
                path, meta = self._save_texture(controller, snapshot, numeric, texture_dir)
                record.update(meta)
                if path:
                    budget["textures"] -= 1
                    saved[numeric] = {"resource_id": numeric, "file": path,
                                      "width": meta.get("width"),
                                      "height": meta.get("height"),
                                      "format": meta.get("format")}
            if path:
                record["file"] = path
            else:
                record["skipped"] = True
            result["textures"].append(record)
        return result

    def _object_matrix(self, snapshot, controller, constants):
        """Read the 720-byte per-object block's leading 4x4 affine, if present.

        Passes that place geometry per draw bind this struct on the vertex
        stage; its Offset(0) is the object->world affine in column-major order.
        """
        for row in constants:
            if row.get("stage") != "vertex" or row.get("byte_size") != 720:
                continue
            numeric = _numeric_id(row.get("resource_id"))
            if numeric is None:
                continue
            buf = (snapshot.catalog.get("buffers") or {}).get(numeric)
            if buf is None:
                continue
            try:
                data = controller.GetBufferData(buf.resourceId, int(row["byte_offset"]), 64)
                values = struct.unpack("<16f", bytes(data[:64]))
            except Exception:
                continue
            return [round(v, 9) for v in values]
        return None

    def _save_texture(self, controller, snapshot, numeric, texture_dir):
        # Resolve from the snapshot catalog: a nested BlockInvoke here would run
        # on the replay thread and never return.
        tex = (snapshot.catalog.get("textures") or {}).get(numeric)
        if tex is None:
            return None, {"skipped": "texture_descriptor_missing"}
        name_attr = getattr(tex.format, "Name", None)
        try:
            format_name = name_attr() if callable(name_attr) else str(tex.format)
        except Exception:
            format_name = str(tex.format)
        meta = {"width": int(tex.width), "height": int(tex.height),
                "format": format_name}
        if int(tex.width) > MAX_TEXTURE_EDGE or int(tex.height) > MAX_TEXTURE_EDGE:
            return None, {"skipped": "too_large"}
        if any(marker in meta["format"].upper() for marker in _SKIP_FORMAT_MARKERS):
            return None, {"skipped": "depth_format"}
        output_path = os.path.join(texture_dir, "tex_%d.png" % numeric)
        if not os.path.exists(output_path):
            tex_save = rd.TextureSave()
            tex_save.resourceId = tex.resourceId
            tex_save.mip = 0
            tex_save.slice.sliceIndex = 0
            tex_save.alpha = rd.AlphaMapping.Preserve
            tex_save.destType = rd.FileType.PNG
            try:
                # Already on the replay thread; call SaveTexture directly.
                outcome = controller.SaveTexture(tex_save, output_path)
                ok = bool(outcome.OK())
            except Exception as exc:
                return None, {"save_failed": "%s: %s" % (meta["format"], exc)}
            if not ok:
                return None, {"save_failed": meta["format"]}
        return output_path, meta


def _ensure_dir(path):
    if path and not os.path.exists(path):
        os.makedirs(path)


def _numeric_id(text):
    try:
        return int(str(text).split("::")[-1])
    except (TypeError, ValueError):
        return None


def _flag_names(flags):
    names = []
    for name in ("Drawcall", "Dispatch", "Indexed", "Instanced", "Clear", "Copy"):
        value = getattr(rd.ActionFlags, name, None)
        if value is not None and (flags & value):
            names.append(name)
    return names


def _blend_summary(data):
    if not isinstance(data, dict):
        return None
    summary = {"enabled": data.get("blendEnable")}
    for key in ("source", "destination", "operation", "sourceAlpha",
                "destinationAlpha", "alphaOperation", "colorWrite"):
        if key in data:
            summary[key] = data[key]
    return summary


def _depth_summary(data):
    if not isinstance(data, dict):
        return None
    summary = {}
    for key in ("depthEnable", "depthWrite", "depthFunction", "depthBounds"):
        if key in data:
            summary[key] = data[key]
    return summary
