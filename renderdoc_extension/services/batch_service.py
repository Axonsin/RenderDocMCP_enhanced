"""Event-scoped batch exports, executed as resumable replay-thread steps."""
import copy
import hashlib
import json
import os

import renderdoc as rd

from .job_service import atomic_json, PauseJob
from .mesh_service import MeshService
from .pipeline_snapshot import Snapshot, plain
from .replay_query import at_event, require_action
from .shader_variables import reflected_layout
from .constant_export import read_constants, write_constants


class BatchService:
    def __init__(self, ctx, invoke_fn, mesh_service, session=None, jobs=None):
        self.ctx, self._invoke, self._mesh = ctx, invoke_fn, mesh_service
        self.session, self.jobs = session, jobs

    def _select(self, action_event_ids, marker_filter, action_event_id_range):
        if sum(x is not None for x in (action_event_ids, marker_filter, action_event_id_range)) != 1:
            raise ValueError("INVALID_REQUEST: choose exactly one draw list, marker or EID range")
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        if action_event_ids is not None:
            if not isinstance(action_event_ids, list) or not 1 <= len(action_event_ids) <= 256:
                raise ValueError("INVALID_REQUEST: action_event_ids must contain 1..256 IDs")
            actions = [require_action(self.ctx, e) for e in action_event_ids]
            if any(not a.flags & rd.ActionFlags.Drawcall for a in actions):
                raise ValueError("INVALID_ACTION_EVENT_ID: explicit selections must be draws")
            selected = sorted(set(a.eventId for a in actions))
            return selected, len(actions) - len(selected)
        low, high = 1, 0xffffffff
        if action_event_id_range is not None:
            if not isinstance(action_event_id_range, dict) or set(action_event_id_range) != {"min", "max"}:
                raise ValueError("INVALID_REQUEST: range needs min and max")
            low, high = action_event_id_range["min"], action_event_id_range["max"]
            if type(low) is not int or type(high) is not int or not 1 <= low <= high:
                raise ValueError("INVALID_REQUEST: invalid action EID range")
        if marker_filter is not None and (not isinstance(marker_filter, str) or not marker_filter):
            raise ValueError("INVALID_MARKER_FILTER: non-empty marker required")
        selected, skipped = [], [0]
        def visit(rows, inherited=False):
            for a in rows:
                try:
                    name = self.ctx.GetEventName(a.eventId)
                except Exception:
                    try:
                        name = a.GetName(self.ctx.GetStructuredFile())
                    except Exception:
                        name = getattr(a, "name", "")
                matched = inherited or marker_filter is None or marker_filter in str(name)
                if matched and low <= a.eventId <= high:
                    if a.flags & rd.ActionFlags.Drawcall:
                        selected.append(a.eventId)
                    else:
                        skipped[0] += 1
                visit(a.children, matched)
        visit(self.ctx.CurRootActions())
        if not selected:
            raise ValueError("INVALID_REQUEST: selector matches no draws")
        return sorted(set(selected)), skipped[0]

    def dump_draws(self, output_dir, action_event_ids=None, marker_filter=None,
                   action_event_id_range=None, mesh_stage="VSIn", instances=None, view_index=0,
                   export_meshes=True, export_textures=True, max_textures=48,
                   max_texture_edge=None, skip_depth=False, job_id=None, export_constants=True):
        selected, skipped = self._select(action_event_ids, marker_filter, action_event_id_range)
        if mesh_stage not in ("VSIn", "VSOut", "GSOut"):
            raise ValueError("INVALID_STAGE: invalid mesh_stage")
        instances = [0] if instances is None else instances
        if not isinstance(instances, list) or not instances or any(type(i) is not int or i < 0 for i in instances):
            raise ValueError("INVALID_INSTANCE: instances must be non-negative integer list")
        instances = sorted(set(instances))
        if type(view_index) is not int or view_index < 0 or (mesh_stage == "VSIn" and view_index):
            raise ValueError("INVALID_VIEW_INDEX: invalid view selection")
        if type(max_textures) is not int or max_textures < 1:
            raise ValueError("INVALID_REQUEST: max_textures must be positive")
        if max_texture_edge is not None and (type(max_texture_edge) is not int or max_texture_edge < 1):
            raise ValueError("INVALID_REQUEST: max_texture_edge must be positive or null")
        if any(type(v) is not bool for v in (export_meshes, export_textures, skip_depth, export_constants)):
            raise ValueError("INVALID_REQUEST: export options must be booleans")
        if not isinstance(output_dir, str) or not os.path.isabs(output_dir):
            raise ValueError("INVALID_OUTPUT_PATH: output_dir must be absolute")
        for eid in selected:
            a = require_action(self.ctx, eid)
            if any(i >= max(1, a.numInstances) for i in instances):
                raise ValueError("INVALID_INSTANCE: selected instance exceeds draw %d" % eid)
        params = dict(output_dir=output_dir, action_event_ids=action_event_ids,
                      marker_filter=marker_filter, action_event_id_range=action_event_id_range,
                      mesh_stage=mesh_stage, instances=instances, view_index=view_index,
                      export_meshes=export_meshes, export_textures=export_textures,
                      max_textures=max_textures, max_texture_edge=max_texture_edge, skip_depth=skip_depth, export_constants=export_constants)

        def steps(key):
            directory = os.path.join(output_dir, key)
            os.makedirs(directory, exist_ok=True)
            self.jobs.update(key, texture_budget=max_textures, requested_count=len(action_event_ids or selected),
                             draw_count=len(selected), skipped_count=skipped,
                             expected_items=len(selected) * len(instances), output_dir=directory)
            saved, contents = {}, {}
            for eid in selected:
                for instance in sorted(set(instances)):
                    entry = {"item_key": "%d:%d:%d" % (eid, instance, view_index),
                             "action_event_id": eid, "instance": instance, "view_index": view_index,
                             "complete": False}
                    constant_payload = {}
                    def facts(controller, eid=eid, instance=instance, entry=entry, payload=constant_payload):
                        try:
                            fatal = controller.GetFatalErrorStatus()
                        except Exception:
                            fatal = None
                        if fatal is not None and not fatal.OK():
                            raise RuntimeError("REPLAY_UNHEALTHY: %s" % fatal.Message())
                        try:
                            def read(c, event):
                                action = require_action(self.ctx, eid)
                                snapshot = Snapshot(self.ctx, c, action, self.session.token())
                                entry.update(source="tool_output", provenance=self.session.describe(),
                                             vertex_inputs=plain(snapshot.pipe.GetVertexInputs()),
                                             shaders={k: s.get("shader") for k, s in snapshot.stages.items() if s.get("shader")},
                                             bindings=copy.deepcopy(snapshot.bindings),
                                             fixed_state={k: copy.deepcopy(snapshot.stages[k]) for k in ("rasterizer", "framebuffer")})
                                entry["textures"] = [copy.deepcopy(r) for r in snapshot.texture_rows()
                                                     if r.get("bound") and r.get("resource_kind") == "texture"
                                                     and "input" in r.get("roles", [])]
                                if not export_textures:
                                    for texture_row in entry["textures"]:
                                        texture_row["export"] = {"skipped": "export_disabled"}
                                entry["constant_layouts"] = []
                                for binding in entry["bindings"]:
                                    source = snapshot.variable_sources.get(binding["binding_key"])
                                    if source is None or source[4] is None:
                                        continue
                                    declaration = source[4]
                                    entry["constant_layouts"].append({
                                        "binding_id": binding["binding_id"],
                                        "binding_key": binding["binding_key"],
                                        "reflection_index": source[1], "array_element": source[2],
                                        "name": declaration.name, "byte_size": declaration.byteSize,
                                        "source": "reflected_constant_layout", "semantic": "unknown",
                                        "variables": reflected_layout(declaration.variables)})
                                if export_constants:
                                    payload["records"] = read_constants(snapshot)
                                if export_meshes:
                                    local = MeshService(self.ctx, lambda fn: fn(c))
                                    path = os.path.join(directory, "mesh_%d_i%d_v%d.csv" % (eid, instance, view_index))
                                    entry["mesh"] = local.export_mesh_csv(eid, path, mesh_stage,
                                                                         instance=instance, view_index=view_index)
                                issues = [section.get("reason") for st in entry["fixed_state"].values()
                                          for section in st.get("sections", {}).values() if section.get("available") is False]
                                entry["warnings"] = issues
                                entry["serialization_complete"] = not issues
                                entry["ok"] = True
                            at_event(self.ctx, lambda fn: fn(controller), eid, read)
                        except Exception as exc:
                            entry.update(ok=False, error=str(exc))
                        entry["complete"] = not entry.get("ok") or (not export_textures and not export_constants)
                        return {"item": entry}
                    yield ("replay", "draw_%d_instance_%d" % (eid, instance), facts)
                    if entry.get("ok") and export_constants:
                        def constants(_, entry=entry, payload=constant_payload, eid=eid, instance=instance):
                            entry["constants"] = write_constants(directory, payload.pop("records", []), entry["provenance"], "e%d_i%d" % (eid, instance))
                            if any(r["status"] == "failed" for r in entry["constants"]):
                                entry.update(ok=False, error="CONSTANT_EXPORT_FAILED: see constant details")
                            entry["complete"] = not export_textures or not entry.get("ok")
                            return {"item": entry}
                        yield ("worker", "constants_%d" % eid, constants)
                    if not entry.get("ok") or not export_textures:
                        continue
                    for row in entry["textures"]:
                        def texture(controller, row=row, eid=eid, entry=entry):
                            rid = int(row["resource"]["resource_id"].split("::")[-1])
                            sub = row.get("subresources") or {}
                            mip, layer = sub.get("first_mip") or 0, sub.get("first_slice") or 0
                            cache_key = (self.session.token(), eid, rid, mip, layer, 0, "PNG", "preserve")
                            if cache_key not in saved:
                                record = self.jobs.records[key]
                                if record["texture_budget"] <= 0:
                                    raise PauseJob("TEXTURE_BUDGET: resume_job adds a fresh texture allowance")
                                def save(c, event):
                                    td = next(t for t in c.GetTextures() if int(t.resourceId) == rid)
                                    if max_texture_edge and max(td.width, td.height) > max_texture_edge:
                                        return {"skipped": "max_texture_edge"}
                                    if skip_depth and str(td.format.compType).split(".")[-1] == "Depth":
                                        return {"skipped": "depth_filter"}
                                    config = rd.TextureSave()
                                    config.resourceId = td.resourceId
                                    config.mip, config.slice.sliceIndex = mip, layer
                                    config.sample.sampleIndex = 0
                                    config.destType, config.alpha = rd.FileType.PNG, rd.AlphaMapping.Preserve
                                    path = os.path.join(directory, "tex_%d_e%d_m%d_s%d.png" % (rid, eid, mip, layer))
                                    outcome = c.SaveTexture(config, path)
                                    if not outcome.OK():
                                        raise RuntimeError("TEXTURE_SAVE_FAILED: %s" % outcome.Message())
                                    with open(path, "rb") as handle:
                                        digest = hashlib.sha256(handle.read()).hexdigest()
                                    if digest in contents:
                                        os.remove(path)
                                        path = contents[digest]
                                    else:
                                        contents[digest] = path
                                    return dict(path=path, sha256=digest, source="capture_texture",
                                                format=td.format.Name(), export_format="PNG", mip=mip,
                                                slice_index=layer, sample=0, event_phase="after",
                                                source_color_space="srgb" if td.format.compType == rd.CompType.UNormSRGB else "linear",
                                                output_value_domain="RenderDoc_SaveTexture_conversion")
                                try:
                                    saved[cache_key] = at_event(self.ctx, lambda fn: fn(controller), eid, save)
                                    if "path" in saved[cache_key]:
                                        self.jobs.update(key, texture_budget=record["texture_budget"] - 1)
                                except Exception as exc:
                                    saved[cache_key] = {"error": str(exc)}
                                    entry["ok"] = False
                            row["export"] = saved[cache_key]
                            return {"item": entry}
                        yield ("replay", "texture_%d" % eid, texture)
                    def complete(_, entry=entry):
                        entry["complete"] = True
                        return {"item": entry}
                    yield ("ui", "completed_draw_%d_instance_%d" % (eid, instance), complete)
            def finish(_):
                record = self.jobs.records[key]
                result = dict(provenance=record["provenance"], draw_count=len(selected),
                              item_count=len(record["items"]),
                              ok_count=sum(i.get("ok") is True for i in record["items"]),
                              failed_count=sum(i.get("ok") is False for i in record["items"]),
                              pending_count=sum(not i.get("complete") for i in record["items"]),
                              textures_saved=len(contents), skipped_count=skipped,
                              items=record["items"])
                path = os.path.join(directory, "manifest.json")
                atomic_json(path, result)
                return {"result": {k: v for k, v in dict(result, summary_path=path).items() if k != "items"}}
            yield ("worker", "writing_manifest", finish)
        return self.jobs.submit("dump_draws", params, steps, job_id)
