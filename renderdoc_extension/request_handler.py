"""
Request Handler for RenderDoc MCP Bridge
Routes incoming requests to appropriate facade methods.
"""

import traceback


class RequestHandler:
    """Handles incoming MCP bridge requests"""

    def __init__(self, facade):
        self.facade = facade
        self._methods = {
            "ping": self._handle_ping,
            "get_capture_status": self._handle_get_capture_status,
            "get_draw_calls": self._handle_get_draw_calls,
            "get_frame_summary": self._handle_get_frame_summary,
            "search_draws": self._handle_search_draws,
            "get_draw_call_details": self._handle_get_draw_call_details,
            "get_action_timings": self._handle_get_action_timings,
            "get_shader_info": self._handle_get_shader_info,
            "get_buffer_contents": self._handle_get_buffer_contents,
            "get_texture_info": self._handle_get_texture_info,
            "list_resources": self._handle_list_resources,
            "get_texture_data": self._handle_get_texture_data,
            "save_texture": self._handle_save_texture,
            "get_pipeline_state": self._handle_get_pipeline_state,
            "list_captures": self._handle_list_captures,
            "open_capture": self._handle_open_capture,
            "get_mesh_summary": self._handle_get_mesh_summary,
            "get_mesh_data": self._handle_get_mesh_data,
            "export_mesh_csv": self._handle_export_mesh_csv,
        }

    def handle(self, request):
        """Handle a request and return response"""
        request_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})

        try:
            if method not in self._methods:
                return self._error_response(
                    request_id, -32601, "Method not found: %s" % method
                )

            result = self._methods[method](params)
            return {"id": request_id, "result": result}

        except ValueError as e:
            code, message = self._classify_error(str(e))
            return self._error_response(request_id, code, message)
        except Exception as e:
            traceback.print_exc()
            code, message = self._classify_error(str(e))
            return self._error_response(request_id, code, message)

    def _error_response(self, request_id, code, message):
        """Create an error response"""
        return {"id": request_id, "error": {"code": code, "message": message}}

    def _classify_error(self, message):
        """Classify exception messages into stable JSON-RPC error responses."""
        if ": " in message:
            prefix = message.split(": ", 1)[0]
        else:
            prefix = ""

        invalid_prefixes = {
            "INVALID_STAGE",
            "INVALID_EVENT_ID",
            "INVALID_RESOURCE_ID",
            "INVALID_RESOURCE_TYPE",
            "INVALID_SEARCH_TYPE",
            "INVALID_MIP_LEVEL",
            "INVALID_SLICE",
            "INVALID_SAMPLE",
            "INVALID_DEPTH_SLICE",
        }
        runtime_prefixes = {
            "CAPTURE_NOT_LOADED",
            "RESOURCE_NOT_FOUND",
            "TEXTURE_NOT_FOUND",
            "BUFFER_NOT_FOUND",
            "RESOURCE_QUERY_FAILED",
            "UNSUPPORTED_CAPTURE_FEATURE",
        }

        if prefix in invalid_prefixes:
            return -32602, message
        if prefix in runtime_prefixes:
            return -32000, message
        if " is required" in message:
            return -32602, "INVALID_REQUEST: %s" % message
        return -32000, message

    @staticmethod
    def _require_param(params, name):
        """Require a parameter in the request."""
        value = params.get(name)
        if value is None:
            raise ValueError("%s is required" % name)
        return value

    def _handle_ping(self, params):
        """Handle ping request"""
        return {"status": "ok", "message": "pong"}

    def _handle_get_capture_status(self, params):
        """Handle get_capture_status request"""
        return self.facade.get_capture_status()

    def _handle_get_draw_calls(self, params):
        """Handle get_draw_calls request"""
        include_children = params.get("include_children", True)
        marker_filter = params.get("marker_filter")
        exclude_markers = params.get("exclude_markers")
        event_id_range = params.get("event_id_range")
        if event_id_range is not None:
            event_id_min = event_id_range.get("min")
            event_id_max = event_id_range.get("max")
        else:
            event_id_min = params.get("event_id_min")
            event_id_max = params.get("event_id_max")
        only_actions = params.get("only_actions", False)
        flags_filter = params.get("flags_filter")
        return self.facade.get_draw_calls(
            include_children=include_children,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            event_id_min=event_id_min,
            event_id_max=event_id_max,
            only_actions=only_actions,
            flags_filter=flags_filter,
        )

    def _handle_get_frame_summary(self, params):
        """Handle get_frame_summary request"""
        return self.facade.get_frame_summary()

    def _handle_search_draws(self, params):
        """Handle search_draws request."""
        search_type = self._require_param(params, "by")
        query = self._require_param(params, "query")
        stage = params.get("stage")
        return self.facade.search_draws(search_type, query, stage)

    def _handle_get_draw_call_details(self, params):
        """Handle get_draw_call_details request"""
        event_id = self._require_param(params, "event_id")
        return self.facade.get_draw_call_details(int(event_id))

    def _handle_get_action_timings(self, params):
        """Handle get_action_timings request"""
        event_ids = params.get("event_ids")
        marker_filter = params.get("marker_filter")
        exclude_markers = params.get("exclude_markers")
        return self.facade.get_action_timings(
            event_ids=event_ids,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
        )

    def _handle_get_shader_info(self, params):
        """Handle get_shader_info request"""
        event_id = self._require_param(params, "event_id")
        stage = self._require_param(params, "stage")
        return self.facade.get_shader_info(int(event_id), stage)

    def _handle_get_buffer_contents(self, params):
        """Handle get_buffer_contents request"""
        resource_id = self._require_param(params, "resource_id")
        offset = params.get("offset", 0)
        length = params.get("length", 0)
        return self.facade.get_buffer_contents(resource_id, offset, length)

    def _handle_get_texture_info(self, params):
        """Handle get_texture_info request"""
        resource_id = self._require_param(params, "resource_id")
        return self.facade.get_texture_info(resource_id)

    def _handle_list_resources(self, params):
        """Handle list_resources request."""
        resource_type = self._require_param(params, "resource_type")
        name_filter = params.get("name_filter")
        offset = int(params.get("offset", 0))
        limit = int(params.get("limit", 50))
        return self.facade.list_resources(resource_type, name_filter, offset, limit)

    def _handle_get_texture_data(self, params):
        """Handle get_texture_data request"""
        resource_id = self._require_param(params, "resource_id")
        mip = params.get("mip", 0)
        slice_idx = params.get("slice", 0)
        sample = params.get("sample", 0)
        depth_slice = params.get("depth_slice")  # None = full volume
        return self.facade.get_texture_data(resource_id, mip, slice_idx, sample, depth_slice)

    def _handle_save_texture(self, params):
        """Handle save_texture request"""
        resource_id = self._require_param(params, "resource_id")
        output_path = self._require_param(params, "output_path")
        format_type = params.get("format_type", "PNG")
        mip = params.get("mip", 0)
        slice_index = params.get("slice_index", 0)
        alpha_mode = params.get("alpha_mode", "preserve")
        return self.facade.save_texture(
            resource_id=resource_id,
            output_path=output_path,
            format_type=format_type,
            mip=mip,
            slice_index=slice_index,
            alpha_mode=alpha_mode,
        )

    def _handle_get_pipeline_state(self, params):
        """Handle get_pipeline_state request"""
        event_id = self._require_param(params, "event_id")
        return self.facade.get_pipeline_state(int(event_id))

    def _handle_list_captures(self, params):
        """Handle list_captures request"""
        directory = self._require_param(params, "directory")
        return self.facade.list_captures(directory)

    def _handle_open_capture(self, params):
        """Handle open_capture request"""
        capture_path = self._require_param(params, "capture_path")
        return self.facade.open_capture(capture_path)

    def _handle_get_mesh_summary(self, params):
        """Handle get_mesh_summary request"""
        event_id = self._require_param(params, "event_id")
        return self.facade.get_mesh_summary(int(event_id))

    def _handle_get_mesh_data(self, params):
        """Handle get_mesh_data request"""
        event_id = self._require_param(params, "event_id")
        stage = params.get("stage", "VSIn")
        offset = params.get("offset", params.get("start_offset", 0))
        limit = params.get("limit", params.get("max_vertices", 100))
        attributes = params.get("attributes")
        return self.facade.get_mesh_data(
            event_id=int(event_id),
            stage=stage,
            offset=int(offset),
            limit=int(limit),
            start_offset=int(offset),
            max_vertices=int(limit),
            attributes=attributes,
        )

    def _handle_export_mesh_csv(self, params):
        """Handle export_mesh_csv request"""
        event_id = self._require_param(params, "event_id")
        output_path = self._require_param(params, "output_path")
        stage = params.get("stage", "VSIn")
        include_attributes = params.get("include_attributes")
        return self.facade.export_mesh_csv(
            event_id=int(event_id),
            output_path=output_path,
            stage=stage,
            include_attributes=include_attributes,
        )
