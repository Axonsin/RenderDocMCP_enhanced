"""
Reverse lookup search service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Parsers, Helpers
from .replay_query import record_restore_failure


class SearchService:
    """Reverse lookup search service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    def _search_actions(self, matcher_fn):
        """
        Common template for searching draw and dispatch actions.

        Args:
            matcher_fn: Function(pipe, controller, action, ctx) -> match_reason or None
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"matches": [], "scanned_count": 0, "scan_failures": 0,
                  "scan_error": None, "error": None}
        restore_event = self.ctx.CurEvent()
        failures = [0, None]  # count, first message

        def callback(controller):
            try:
                root_actions = controller.GetRootActions()
                structured_file = controller.GetStructuredFile()
                all_actions = Helpers.flatten_actions(root_actions)

                # Filter to only draw calls and dispatches
                draw_actions = [
                    a for a in all_actions
                    if a.flags & (rd.ActionFlags.Drawcall | rd.ActionFlags.Dispatch)
                ]
                result["scanned_count"] = len(draw_actions)

                for action in draw_actions:
                    # Fetch fresh pipeline snapshots for each event, including remote replay.
                    try:
                        controller.SetFrameEvent(action.eventId, True)
                        pipe = controller.GetPipelineState()
                    except Exception as exc:
                        # One unreadable action must not abort the whole scan,
                        # but partial failures stay visible in the response.
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

                if draw_actions and failures[0] == len(draw_actions):
                    raise RuntimeError(
                        "RESOURCE_QUERY_FAILED: all %d actions failed to scan: %s"
                        % (len(draw_actions), failures[1])
                    )
            except Exception as exc:
                # Exceptions must survive the SWIG BlockInvoke callback boundary.
                result["error"] = exc
            finally:
                try:
                    controller.SetFrameEvent(restore_event, True)
                except Exception as exc:
                    record_restore_failure(result, exc)

        self._invoke(callback)
        if result["error"] is not None:
            raise result["error"]
        result["total_matches"] = len(result["matches"])
        return result

    def search_actions(self, by, query, stage=None):
        """Search draw and dispatch actions by shader, texture, or resource usage."""
        if by == "shader":
            return self.find_actions_by_shader(query, stage)
        if by == "texture":
            return self.find_actions_by_texture(query)
        if by == "resource":
            return self.find_actions_by_resource(query)
        raise ValueError("INVALID_SEARCH_TYPE: by must be one of shader, texture, resource")

    def find_actions_by_shader(self, shader_name, stage=None):
        """Find draw and dispatch actions using a shader with the given name (partial match)."""
        # Determine which stages to check
        if stage:
            stages_to_check = [Parsers.parse_stage(stage)]
        else:
            stages_to_check = Helpers.get_all_shader_stages()

        def matcher(pipe, controller, action, ctx):
            for s in stages_to_check:
                shader = pipe.GetShader(s)
                if shader == rd.ResourceId.Null():
                    continue

                reflection = pipe.GetShaderReflection(s)
                if reflection:
                    entry_point = pipe.GetShaderEntryPoint(s)
                    shader_debug_name = ""
                    try:
                        shader_debug_name = ctx.GetResourceName(shader)
                    except Exception:
                        pass

                    if shader_name.lower() in entry_point.lower():
                        return "%s entry_point: '%s'" % (Parsers.stage_name(s), entry_point)
                    elif shader_debug_name and shader_name.lower() in shader_debug_name.lower():
                        return "%s name: '%s'" % (Parsers.stage_name(s), shader_debug_name)
            return None

        return self._search_actions(matcher)

    def find_actions_by_texture(self, texture_name):
        """Find draw and dispatch actions using a texture with the given name (partial match)."""
        stages_to_check = Helpers.get_all_shader_stages()

        def matcher(pipe, controller, action, ctx):
            # Check SRVs (read-only resources)
            for stage in stages_to_check:
                try:
                    srvs = pipe.GetReadOnlyResources(stage, False)
                    for srv in srvs:
                        if srv.descriptor.resource == rd.ResourceId.Null():
                            continue
                        res_name = ""
                        try:
                            res_name = ctx.GetResourceName(srv.descriptor.resource)
                        except Exception:
                            pass
                        if res_name and texture_name.lower() in res_name.lower():
                            return "%s srv: '%s'" % (Parsers.stage_name(stage), res_name)
                except Exception:
                    pass

                # Check UAVs (read-write resources)
                try:
                    uavs = pipe.GetReadWriteResources(stage, False)
                    for uav in uavs:
                        if uav.descriptor.resource == rd.ResourceId.Null():
                            continue
                        res_name = ""
                        try:
                            res_name = ctx.GetResourceName(uav.descriptor.resource)
                        except Exception:
                            pass
                        if res_name and texture_name.lower() in res_name.lower():
                            return "%s uav: '%s'" % (Parsers.stage_name(stage), res_name)
                except Exception:
                    pass

            # Check render targets
            try:
                for i, rt in enumerate(pipe.GetOutputTargets()):
                    if rt.resource == rd.ResourceId.Null():
                        continue
                    res_name = ""
                    try:
                        res_name = ctx.GetResourceName(rt.resource)
                    except Exception:
                        pass
                    if res_name and texture_name.lower() in res_name.lower():
                        return "render_target[%d]: '%s'" % (i, res_name)
            except Exception:
                pass

            return None

        return self._search_actions(matcher)

    def find_actions_by_resource(self, resource_id):
        """Find draw and dispatch actions using a specific resource ID (exact match)."""
        target_rid = Parsers.parse_resource_id(resource_id)
        stages_to_check = Helpers.get_all_shader_stages()

        def matcher(pipe, controller, action, ctx):
            # Check shaders
            for stage in stages_to_check:
                shader = pipe.GetShader(stage)
                if shader == target_rid:
                    return "%s shader" % Parsers.stage_name(stage)

            # Check SRVs and UAVs
            for stage in stages_to_check:
                try:
                    srvs = pipe.GetReadOnlyResources(stage, False)
                    for srv in srvs:
                        if srv.descriptor.resource == target_rid:
                            return "%s srv slot %d" % (Parsers.stage_name(stage), srv.access.index)
                except Exception:
                    pass

                try:
                    uavs = pipe.GetReadWriteResources(stage, False)
                    for uav in uavs:
                        if uav.descriptor.resource == target_rid:
                            return "%s uav slot %d" % (Parsers.stage_name(stage), uav.access.index)
                except Exception:
                    pass

            # Check render targets
            try:
                for i, rt in enumerate(pipe.GetOutputTargets()):
                    if rt.resource == target_rid:
                        return "render_target[%d]" % i
            except Exception:
                pass

            try:
                if pipe.GetDepthTarget().resource == target_rid:
                    return "depth_target"
            except Exception:
                pass

            return None

        return self._search_actions(matcher)
