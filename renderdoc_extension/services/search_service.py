"""
Reverse lookup search service for RenderDoc.
"""

import time

import renderdoc as rd

from ..utils import Parsers, Helpers
from .replay_query import record_restore_failure

DEFAULT_TIME_BUDGET_MS = 8000
DEFAULT_MAX_MATCHES = 200


class SearchService:
    """Reverse lookup search service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    # ------------------------------------------------------------------ helpers

    @staticmethod
    def _numeric(resource_id):
        return Parsers.extract_numeric_id(resource_id)

    @staticmethod
    def _descriptor_id(descriptor):
        try:
            return int(descriptor)
        except Exception:
            return None

    def _usage_event_ids(self, controller, numeric_ids, descriptors=None):
        """Draw/dispatch event IDs touching these resources, via GetUsage.

        A single-resource usage scan is far cheaper than rebuilding pipeline
        state at every event, which is the dominant cost on remote replay.
        """
        events = set()
        if descriptors is None:
            descriptors = self._resource_descriptors(controller)
        for numeric_id in numeric_ids:
            descriptor = descriptors.get(numeric_id)
            if descriptor is None:
                return None
            try:
                for usage in controller.GetUsage(descriptor.resourceId):
                    events.add(int(usage.eventId))
            except Exception:
                return None
        return events or None

    @staticmethod
    def _resource_descriptors(controller):
        descriptors = {}
        for name in ("GetResources", "GetTextures", "GetBuffers"):
            try:
                for res in getattr(controller, name)():
                    descriptors.setdefault(int(res.resourceId), res)
            except AttributeError:
                continue
        return descriptors

    def _matching_resource_ids(self, controller, query, descriptors=None):
        """Numeric IDs whose debug name contains the query (case-insensitive)."""
        needle = query.lower()
        matches = set()
        if descriptors is None:
            descriptors = self._resource_descriptors(controller)
        for numeric, res in descriptors.items():
            try:
                name = self.ctx.GetResourceName(res.resourceId) or ""
            except Exception:
                name = getattr(res, "name", "")
            if name and needle in name.lower():
                matches.add(numeric)
        return matches

    def _search_actions(self, matcher_fn, action_filter=None, time_budget_ms=None,
                        max_matches=None, start_event_id=None, scan_mode="pipeline",
                        action_event_id_range=None, prepare=None):
        """
        Common template for searching draw and dispatch actions.

        Args:
            matcher_fn: Function(pipe, controller, action, ctx) -> match_reason or None
            action_filter: Optional set of event IDs to restrict the scan to
            time_budget_ms: Stop before the client-side tool timeout and report
                a resume cursor instead of failing
            max_matches: Stop once this many matches are collected
            start_event_id: Resume cursor from a previous truncated scan
            scan_mode: Reported provenance of the candidate set
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        low, high, _ = self._range_filter(action_event_id_range)
        budget_ms = DEFAULT_TIME_BUDGET_MS if time_budget_ms is None else time_budget_ms
        if type(budget_ms) is not int or budget_ms <= 0:
            raise ValueError("INVALID_PAGINATION: time_budget_ms must be > 0")
        match_cap = DEFAULT_MAX_MATCHES if max_matches is None else max_matches
        if type(match_cap) is not int or match_cap <= 0:
            raise ValueError("INVALID_PAGINATION: max_matches must be > 0")
        if start_event_id is not None and (type(start_event_id) is not int or start_event_id <= 0):
            raise ValueError("INVALID_PAGINATION: start_event_id must be a positive integer")

        result = {
            "matches": [], "scanned_count": 0, "scan_failures": 0,
            "scan_error": None, "error": None, "complete": True,
            "stopped_reason": None, "next_event_id": None,
            "scan_mode": scan_mode, "time_budget_ms": budget_ms,
            "max_matches": match_cap, "elapsed_ms": None,
        }
        restore_event = self.ctx.CurEvent()
        failures = [0, None]  # count, first message
        started = time.monotonic()

        def callback(controller):
            moved = False
            try:
                candidates = action_filter
                mode = scan_mode
                if prepare is not None:
                    candidates = prepare(controller)
                    mode = "usage" if candidates is not None else "pipeline"
                    result["scan_mode"] = mode
                root_actions = controller.GetRootActions()
                structured_file = controller.GetStructuredFile()
                all_actions = Helpers.flatten_actions(root_actions)

                draw_actions = [
                    a for a in all_actions
                    if a.flags & (rd.ActionFlags.Drawcall | rd.ActionFlags.Dispatch)
                ]
                if candidates is not None:
                    draw_actions = [a for a in draw_actions if int(a.eventId) in candidates
                                    or any(int(e.eventId) in candidates
                                           for e in getattr(a, "events", []))]
                if low is not None:
                    draw_actions = [a for a in draw_actions if low <= int(a.eventId) <= high]
                if start_event_id is not None:
                    draw_actions = [a for a in draw_actions if int(a.eventId) >= int(start_event_id)]
                draw_actions.sort(key=lambda a: int(a.eventId))

                deadline = started + budget_ms / 1000.0
                for action in draw_actions:
                    if len(result["matches"]) >= match_cap:
                        result["complete"] = False
                        result["stopped_reason"] = "max_matches"
                        result["next_event_id"] = int(action.eventId)
                        break
                    if time.monotonic() >= deadline:
                        result["complete"] = False
                        result["stopped_reason"] = "time_budget"
                        result["next_event_id"] = int(action.eventId)
                        break

                    result["scanned_count"] += 1
                    if mode == "usage":
                        result["matches"].append({
                            "action_event_id": action.eventId,
                            "name": action.GetName(structured_file),
                            "match_reason": "resource usage",
                        })
                        continue
                    try:
                        moved = True
                        controller.SetFrameEvent(action.eventId, True)
                        pipe = controller.GetPipelineState()
                    except Exception as exc:
                        failures[0] += 1
                        if failures[1] is None:
                            failures[1] = str(exc)
                        continue

                    match_reason = matcher_fn(pipe, controller, action, self.ctx)
                    if match_reason:
                        result["matches"].append({
                            "action_event_id": action.eventId,
                            "name": action.GetName(structured_file),
                            "match_reason": match_reason,
                        })

                result["scan_failures"] = failures[0]
                result["scan_error"] = failures[1]

                if result["scanned_count"] and failures[0] == result["scanned_count"]:
                    raise RuntimeError(
                        "RESOURCE_QUERY_FAILED: all %d actions failed to scan: %s"
                        % (result["scanned_count"], failures[1])
                    )
            except Exception as exc:
                # Exceptions must survive the SWIG BlockInvoke callback boundary.
                message = str(exc)
                result["error"] = (exc if message.startswith(("INVALID_", "RESOURCE_QUERY_FAILED:"))
                                   else RuntimeError("RESOURCE_QUERY_FAILED: %s" % message))
            finally:
                if moved:
                    try:
                        controller.SetFrameEvent(restore_event, True)
                    except Exception as exc:
                        record_restore_failure(result, exc)

        self._invoke(callback)
        if result["error"] is not None:
            raise result["error"]
        result["elapsed_ms"] = int((time.monotonic() - started) * 1000)
        result["total_matches"] = len(result["matches"])
        return result

    # ------------------------------------------------------------------ public

    def search_actions(self, by, query, stage=None, action_event_id_range=None,
                       time_budget_ms=None, max_matches=None, start_event_id=None):
        """Search draw and dispatch actions by shader, texture, or resource usage."""
        if by == "shader":
            return self.find_actions_by_shader(query, stage, action_event_id_range,
                                               time_budget_ms, max_matches, start_event_id)
        if by == "texture":
            return self.find_actions_by_texture(query, action_event_id_range,
                                                time_budget_ms, max_matches, start_event_id)
        if by == "resource":
            return self.find_actions_by_resource(query, action_event_id_range,
                                                 time_budget_ms, max_matches, start_event_id)
        raise ValueError("INVALID_SEARCH_TYPE: by must be one of shader, texture, resource")

    @staticmethod
    def _range_filter(action_event_id_range):
        if action_event_id_range is None:
            return None, None, None
        try:
            low = action_event_id_range.get("min")
            high = action_event_id_range.get("max")
            if type(low) is not int or type(high) is not int or low <= 0:
                raise ValueError()
        except (AttributeError, TypeError, ValueError):
            raise ValueError(
                "INVALID_ACTION_EVENT_ID_RANGE: expected {\"min\": int, \"max\": int}"
            )
        if low > high:
            raise ValueError("INVALID_ACTION_EVENT_ID_RANGE: min must be <= max")
        return low, high, None

    def find_actions_by_shader(self, shader_name, stage=None, action_event_id_range=None,
                               time_budget_ms=None, max_matches=None, start_event_id=None):
        """Find draw and dispatch actions using a shader with the given name (partial match)."""
        if stage:
            stages_to_check = [Parsers.parse_stage(stage)]
        else:
            stages_to_check = Helpers.get_all_shader_stages()

        state = {"ids": None}

        def matcher(pipe, controller, action, ctx):
            ids = state["ids"]
            for s in stages_to_check:
                try:
                    shader = pipe.GetShader(s)
                except Exception:
                    continue
                if shader == rd.ResourceId.Null():
                    continue

                if ids:
                    shader_id = self._descriptor_id(shader)
                    if shader_id is not None and shader_id in ids:
                        return "%s shader id %d" % (Parsers.stage_name(s), shader_id)
                reflection = pipe.GetShaderReflection(s)
                if reflection:
                    entry_point = pipe.GetShaderEntryPoint(s)
                    if shader_name.lower() in entry_point.lower():
                        return "%s entry_point: '%s'" % (Parsers.stage_name(s), entry_point)

            return None

        def prepare(controller):
            state["ids"] = self._matching_resource_ids(controller, shader_name)
            return None

        return self._search_actions(
            matcher, time_budget_ms=time_budget_ms, max_matches=max_matches,
            start_event_id=start_event_id, action_event_id_range=action_event_id_range,
            prepare=prepare,
        )

    def find_actions_by_texture(self, texture_name, action_event_id_range=None,
                                time_budget_ms=None, max_matches=None, start_event_id=None):
        """Find draw and dispatch actions using a texture with the given name (partial match)."""
        stages_to_check = Helpers.get_all_shader_stages()
        state = {"ids": set(), "candidates": None}

        def collect(controller):
            descriptors = self._resource_descriptors(controller)
            state["ids"] = self._matching_resource_ids(controller, texture_name, descriptors)
            if state["ids"]:
                state["candidates"] = self._usage_event_ids(controller, state["ids"], descriptors)

        def matcher(pipe, controller, action, ctx):
            def hit(descriptor):
                return self._descriptor_id(descriptor) in state["ids"]

            for stage in stages_to_check:
                try:
                    for srv in pipe.GetReadOnlyResources(stage, False):
                        if hit(srv.descriptor.resource):
                            return "%s srv" % Parsers.stage_name(stage)
                except Exception:
                    pass
                try:
                    for uav in pipe.GetReadWriteResources(stage, False):
                        if hit(uav.descriptor.resource):
                            return "%s uav" % Parsers.stage_name(stage)
                except Exception:
                    pass

            try:
                for i, rt in enumerate(pipe.GetOutputTargets()):
                    if hit(rt.resource):
                        return "render_target[%d]" % i
            except Exception:
                pass

            try:
                if hit(pipe.GetDepthTarget().resource):
                    return "depth_target"
            except Exception:
                pass

            return None

        def prepare(controller):
            collect(controller)
            return state["candidates"] if state["ids"] else set()

        return self._search_actions(
            matcher, time_budget_ms=time_budget_ms, max_matches=max_matches,
            start_event_id=start_event_id, action_event_id_range=action_event_id_range,
            prepare=prepare,
        )

    def find_actions_by_resource(self, resource_id, action_event_id_range=None,
                                 time_budget_ms=None, max_matches=None, start_event_id=None):
        """Find draw and dispatch actions using a specific resource ID (exact match)."""
        try:
            numeric = self._numeric(resource_id)
            if numeric <= 0:
                raise ValueError()
        except (TypeError, ValueError):
            raise ValueError("INVALID_RESOURCE_ID: %s" % resource_id)
        stages_to_check = Helpers.get_all_shader_stages()

        def matcher(pipe, controller, action, ctx):
            # Usage may be unavailable; include non-SRV buffer bindings too.
            try:
                if self._descriptor_id(pipe.GetIBuffer().resourceId) == numeric:
                    return "index_buffer"
                if any(self._descriptor_id(v.resourceId) == numeric for v in pipe.GetVBuffers()):
                    return "vertex_buffer"
            except AttributeError:
                pass
            for stage in stages_to_check:
                try:
                    if self._descriptor_id(pipe.GetShader(stage)) == numeric:
                        return "%s shader" % Parsers.stage_name(stage)
                except Exception:
                    pass

            for stage in stages_to_check:
                try:
                    for cb in pipe.GetConstantBlocks(stage, False):
                        if self._descriptor_id(cb.descriptor.resource) == numeric:
                            return "%s constant_buffer" % Parsers.stage_name(stage)
                except AttributeError:
                    pass
                try:
                    for srv in pipe.GetReadOnlyResources(stage, False):
                        if self._descriptor_id(srv.descriptor.resource) == numeric:
                            return "%s srv slot %d" % (Parsers.stage_name(stage), srv.access.index)
                except Exception:
                    pass
                try:
                    for uav in pipe.GetReadWriteResources(stage, False):
                        if self._descriptor_id(uav.descriptor.resource) == numeric:
                            return "%s uav slot %d" % (Parsers.stage_name(stage), uav.access.index)
                except Exception:
                    pass

            try:
                for i, rt in enumerate(pipe.GetOutputTargets()):
                    if self._descriptor_id(rt.resource) == numeric:
                        return "render_target[%d]" % i
            except Exception:
                pass

            try:
                if self._descriptor_id(pipe.GetDepthTarget().resource) == numeric:
                    return "depth_target"
            except Exception:
                pass

            return None

        def prepare(controller):
            return self._usage_event_ids(controller, {numeric})

        return self._search_actions(
            matcher, time_budget_ms=time_budget_ms, max_matches=max_matches,
            start_event_id=start_event_id, action_event_id_range=action_event_id_range,
            prepare=prepare,
        )
