"""
Reverse lookup search service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Parsers, Helpers


class SearchService:
    """Reverse lookup search service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    def _search_draws(self, matcher_fn):
        """
        Common template for searching draw calls.

        Args:
            matcher_fn: Function(pipe, controller, action, ctx) -> match_reason or None
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"matches": [], "scanned_count": 0}

        def callback(controller):
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
                controller.SetFrameEvent(action.eventId, False)
                pipe = controller.GetPipelineState()

                match_reason = matcher_fn(pipe, controller, action, self.ctx)
                if match_reason:
                    result["matches"].append({
                        "event_id": action.eventId,
                        "name": action.GetName(structured_file),
                        "match_reason": match_reason,
                    })

        self._invoke(callback)
        result["total_matches"] = len(result["matches"])
        return result

    def search_draws(self, by, query, stage=None):
        """Search draw calls by shader, texture, or resource usage."""
        if by == "shader":
            return self.find_draws_by_shader(query, stage)
        if by == "texture":
            return self.find_draws_by_texture(query)
        if by == "resource":
            return self.find_draws_by_resource(query)
        raise ValueError("INVALID_SEARCH_TYPE: by must be one of shader, texture, resource")

    def find_draws_by_shader(self, shader_name, stage=None):
        """Find all draw calls using a shader with the given name (partial match)."""
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

        return self._search_draws(matcher)

    def find_draws_by_texture(self, texture_name):
        """Find all draw calls using a texture with the given name (partial match)."""
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

        return self._search_draws(matcher)

    def find_draws_by_resource(self, resource_id):
        """Find all draw calls using a specific resource ID (exact match)."""
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

        return self._search_draws(matcher)
