"""
Request Handler for RenderDoc MCP Bridge
Routes incoming requests to appropriate facade methods.
"""

import inspect
import traceback


class RequestHandler:
    """Handles incoming MCP bridge requests"""

    def __init__(self, facade):
        self.facade = facade
        self._methods = {
            "ping": self._handle_ping,
            "get_capture_status": self._handle_get_capture_status,
            "get_actions": self._handle_get_actions,
            "get_frame_summary": self._handle_get_frame_summary,
            "inspect_action": self._handle_inspect_action,
            "summarize_capture": self._handle_summarize_capture,
            "search_actions": self._handle_search_actions,
            "get_action_details": self._handle_get_action_details,
            "get_action_api_calls": self._handle_get_action_api_calls,
            "get_action_timings": self._handle_get_action_timings,
            "get_shader_info": self._handle_get_shader_info,
            "get_shader_source": self._handle_get_shader_source,
            "get_shader_edit_context": self._handle_get_shader_edit_context,
            "replace_shader": self._handle_replace_shader,
            "revert_shader": self._handle_revert_shader,
            "list_shader_replacements": self._handle_list_shader_replacements,
            "export_shader_source": self._handle_export_shader_source,
            "get_buffer_contents": self._handle_get_buffer_contents,
            "get_texture_info": self._handle_get_texture_info,
            "list_resources": self._handle_list_resources,
            "inspect_resource": self._handle_inspect_resource,
            "get_resource_initialization": self._handle_get_resource_initialization,
            "get_texture_data": self._handle_get_texture_data,
            "save_texture": self._handle_save_texture,
            "get_pipeline_state": self._handle_get_pipeline_state,
            "get_pipeline_stage": self._handle_get_pipeline_stage,
            "inspect_pipeline_binding": self._handle_inspect_pipeline_binding,
            "get_action_textures": self._handle_get_action_textures,
            "trace_resource_usage": self._handle_trace_resource_usage,
            "trace_action_dependencies": self._handle_trace_action_dependencies,
            "diff_actions": self._handle_diff_actions,
            "analyze_pass": self._handle_analyze_pass,
            "list_captures": self._handle_list_captures,
            "open_capture": self._handle_open_capture,
            "get_mesh_summary": self._handle_get_mesh_summary,
            "get_mesh_data": self._handle_get_mesh_data,
            "export_mesh_csv": self._handle_export_mesh_csv,
            "dump_draws": self._handle_dump_draws,
            **{name: (lambda params, name=name: getattr(self.facade, name)(**params)) for name in (
                "get_replay_context", "get_job_status", "cancel_job", "resume_job",
                "export_shader_bundle", "compare_texture_events", "get_pixel_history",
                "run_script")},
        }

    def handle(self, request):
        guard = getattr(self.facade, "_guard", None)
        if guard:
            guard.begin(request)
        response = self._handle(request)
        if guard:
            data = response.get("result")
            if isinstance(data, dict):
                guard.phase("result_ready", readback_bytes=data.get("source_data_length", data.get("data_length", data.get("returned_bytes"))))
            if isinstance(data, dict) and data.get("replay_healthy") is False:
                guard.observe_failure(data.get("replay_error"))
            guard.finish(response.get("error", {}).get("message"))
        return response

    def _handle(self, request):
        """Handle a request and return response"""
        request_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})

        try:
            if method not in self._methods:
                return self._error_response(
                    request_id, -32601, "Method not found: %s" % method
                )

            runtime = getattr(self.facade, "runtime_info", {}) or {}
            if runtime.get("api_contract_version") == 3 and request.get("api_contract_version") != 3:
                raise ValueError("API_VERSION_MISMATCH: MCP server and extension must both use API contract 3")
            jobs = getattr(self.facade, "_jobs", None)
            controls = {"ping", "get_capture_status", "get_replay_context", "get_job_status", "cancel_job"}
            resubmission = (jobs and params.get("job_id") in jobs.records and
                            jobs.records[params["job_id"]]["kind"] == method)
            if jobs and jobs.busy() and method not in controls and not resubmission:
                raise ValueError("REPLAY_BUSY: query or cancel the active job before submitting replay work")
            target = getattr(self.facade, method) if method != "ping" else None
            allowed = set(inspect.signature(target).parameters) if target else set()
            unexpected = sorted(set(params) - allowed)
            if unexpected:
                raise ValueError("INVALID_REQUEST: unexpected parameter(s): %s" %
                                 ", ".join(unexpected))

            guard = getattr(self.facade, "_guard", None)
            if guard and method not in controls | {"open_capture", "list_captures", "list_shader_replacements"}:
                guard.preflight()
            if runtime.get("extension_version") and request.get("server_version") != runtime["extension_version"]:
                raise ValueError("API_VERSION_MISMATCH: deploy matching MCP server and extension versions")
            result = self._methods[method](params)
            return {"id": request_id, "result": result, "api_contract_version": 3}

        except ValueError as e:
            code, message = self._classify_error(str(e))
            return self._error_response(request_id, code, message)
        except Exception as e:
            traceback.print_exc()
            code, message = self._classify_error(str(e))
            return self._error_response(request_id, code, message)

    def _error_response(self, request_id, code, message):
        """Create an error response"""
        return {"id": request_id, "error": {"code": code, "message": message}, "api_contract_version": 3}

    def _classify_error(self, message):
        """Classify exception messages into stable JSON-RPC error responses."""
        if ": " in message:
            prefix = message.split(": ", 1)[0]
        else:
            prefix = ""

        invalid_prefixes = {
            "INVALID_REQUEST",
            "INVALID_USAGE_CATEGORIES",
            "INVALID_STAGE",
            "INVALID_ACTION_EVENT_ID",
            "INVALID_INSTANCE",
            "INVALID_BINDING_ID",
            "INVALID_SECTION",
            "INVALID_DIRECTION",
            "INVALID_FILTER",
            "INVALID_EVENT_ID",
            "INVALID_API_EVENT_ID",
            "INVALID_RESOURCE_ID",
            "INVALID_RESOURCE_TYPE",
            "INVALID_PAGINATION",
            "INVALID_SORT",
            "INVALID_CHUNK_INDEX",
            "INVALID_CHILD_PATH",
            "INVALID_SEARCH_TYPE",
            "INVALID_MARKER_FILTER",
            "INVALID_MIP_LEVEL",
            "INVALID_SLICE",
            "INVALID_SAMPLE",
            "INVALID_ASPECT",
            "INVALID_DEPTH_SLICE",
            "INVALID_EDIT_ID",
            "INVALID_EDIT_MODE",
            "INVALID_SHADER_SOURCE",
            "INVALID_OUTPUT_PATH",
            "INVALID_FORMAT_TYPE",
            "INVALID_ALPHA_MODE",
            "INVALID_VIEW_INDEX",
            "SCRIPT_SYNTAX_ERROR",
        }
        runtime_prefixes = {
            "CAPTURE_NOT_LOADED",
            "RESOURCE_NOT_FOUND",
            "TEXTURE_NOT_FOUND",
            "BUFFER_NOT_FOUND",
            "RESOURCE_QUERY_FAILED",
            "MESH_SIGNATURE_UNAVAILABLE",
            "TEXTURE_SAVE_FAILED",
            "REPLAY_RESTORE_FAILED",
            "UNSUPPORTED_CAPTURE_FEATURE",
            "SCRIPT_ERROR",
            "SCRIPT_RESULT_TOO_LARGE",
            "SCRIPT_RESULT_NOT_SERIALIZABLE",
            "SCRIPT_EXECUTION_DISABLED",
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
        """Handle ping request with version info (no replay probe)."""
        runtime = getattr(self.facade, "runtime_info", None) or {}
        capture_loaded = False
        try:
            capture_loaded = bool(self.facade.ctx.IsCaptureLoaded())
        except Exception:
            pass
        return {
            "status": "ok",
            "message": "pong",
            "extension_version": runtime.get("extension_version"),
            "renderdoc_version": runtime.get("renderdoc_version"),
            "ipc_version": runtime.get("ipc_version"),
            "capture_loaded": capture_loaded,
            "api_contract_version": 3,
            "extension_build_hash": runtime.get("extension_build_hash"),
        }

    def _handle_get_capture_status(self, params):
        """Handle get_capture_status request"""
        return self.facade.get_capture_status(**params)

    def _handle_get_actions(self, params):
        """Handle get_actions request"""
        include_children = params.get("include_children", True)
        marker_filter = params.get("marker_filter")
        exclude_markers = params.get("exclude_markers")
        action_event_id_range = params.get("action_event_id_range")
        exclude_marker_actions = params.get("exclude_marker_actions", False)
        flags_filter = params.get("flags_filter")
        return self.facade.get_actions(
            include_children=include_children,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            action_event_id_range=action_event_id_range,
            exclude_marker_actions=exclude_marker_actions,
            flags_filter=flags_filter,
        )

    def _handle_get_frame_summary(self, params):
        """Handle get_frame_summary request"""
        return self.facade.get_frame_summary()

    def _handle_inspect_action(self, params):
        """Handle inspect_action request."""
        action_event_id = self._require_param(params, "action_event_id")
        return self.facade.inspect_action(int(action_event_id))

    def _handle_summarize_capture(self, params):
        """Handle summarize_capture request."""
        return self.facade.summarize_capture()

    def _handle_search_actions(self, params):
        """Handle search_actions request."""
        search_type = self._require_param(params, "by")
        query = self._require_param(params, "query")
        stage = params.get("stage")
        return self.facade.search_actions(
            search_type,
            query,
            stage,
            action_event_id_range=params.get("action_event_id_range"),
            time_budget_ms=params.get("time_budget_ms"),
            max_matches=params.get("max_matches"),
            start_event_id=params.get("start_event_id"),
        )

    def _handle_get_action_details(self, params):
        """Handle get_action_details request"""
        action_event_id = self._require_param(params, "action_event_id")
        return self.facade.get_action_details(action_event_id=int(action_event_id))

    def _handle_get_action_timings(self, params):
        """Handle get_action_timings request"""
        action_event_ids = params.get("action_event_ids")
        marker_filter = params.get("marker_filter")
        exclude_markers = params.get("exclude_markers")
        return self.facade.get_action_timings(
            action_event_ids=action_event_ids,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
        )

    def _handle_get_shader_info(self, params):
        """Handle get_shader_info request"""
        event_id = self._require_param(params, "event_id")
        stage = self._require_param(params, "stage")
        return self.facade.get_shader_info(int(event_id), stage)

    def _handle_get_shader_source(self, params):
        """Handle get_shader_source request"""
        event_id = self._require_param(params, "event_id")
        stage = self._require_param(params, "stage")
        return self.facade.get_shader_source(int(event_id), stage)

    def _handle_get_shader_edit_context(self, params):
        return self.facade.get_shader_edit_context(
            self._require_param(params, "event_id"), self._require_param(params, "stage"),
            params.get("mode", "auto"))

    def _handle_replace_shader(self, params):
        return self.facade.replace_shader(self._require_param(params, "edit_id"),
                                          self._require_param(params, "source_text"))

    def _handle_revert_shader(self, params):
        return self.facade.revert_shader(self._require_param(params, "edit_id"))

    def _handle_list_shader_replacements(self, params):
        return self.facade.list_shader_replacements()

    def _handle_export_shader_source(self, params):
        return self.facade.export_shader_source(self._require_param(params, "edit_id"),
                                                self._require_param(params, "output_path"))

    def _handle_get_buffer_contents(self, params):
        """Handle get_buffer_contents request"""
        resource_id = self._require_param(params, "resource_id")
        offset = params.get("offset", 0)
        length = params.get("length", 0)
        return self.facade.get_buffer_contents(resource_id, offset, length, params.get("action_event_id"))

    def _handle_get_texture_info(self, params):
        """Handle get_texture_info request"""
        resource_id = self._require_param(params, "resource_id")
        return self.facade.get_texture_info(resource_id)

    def _handle_list_resources(self, params):
        """Handle list_resources request."""
        resource_type = params.get("resource_type", "all")
        name_filter = params.get("name_filter")
        offset = params.get("offset", 0)
        limit = params.get("limit", 50)
        return self.facade.list_resources(resource_type, name_filter, offset, limit,
                                          params.get("sort_by", "name"))

    def _handle_get_action_api_calls(self, params):
        return self.facade.get_action_api_calls(
            self._require_param(params, "action_event_id"), params.get("api_event_id"),
            params.get("child_path"), params.get("offset", 0), params.get("limit", 50))

    def _handle_inspect_resource(self, params):
        return self.facade.inspect_resource(
            self._require_param(params, "resource_id"),
            params.get("related_offset", 0), params.get("related_limit", 50))

    def _handle_get_resource_initialization(self, params):
        return self.facade.get_resource_initialization(
            self._require_param(params, "resource_id"), params.get("chunk_index"),
            params.get("child_path"), params.get("offset", 0), params.get("limit", 50))

    def _handle_get_texture_data(self, params):
        """Handle get_texture_data request"""
        resource_id = self._require_param(params, "resource_id")
        mip = params.get("mip", 0)
        slice_index = params.get("slice_index", 0)
        sample = params.get("sample", 0)
        depth_slice = params.get("depth_slice")  # None = full volume
        return self.facade.get_texture_data(**params)

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
            action_event_id=params.get("action_event_id"),
        )

    def _handle_get_pipeline_state(self, params):
        return self.facade.get_pipeline_state(self._require_param(params, "action_event_id"))

    def _handle_get_pipeline_stage(self, params):
        return self.facade.get_pipeline_stage(
            self._require_param(params, "action_event_id"), self._require_param(params, "stage"),
            params.get("section", "overview"), params.get("show_unused", False),
            params.get("show_empty", False), params.get("offset", 0), params.get("limit", 50))

    def _handle_inspect_pipeline_binding(self, params):
        return self.facade.inspect_pipeline_binding(
            self._require_param(params, "action_event_id"), self._require_param(params, "binding_id"),
            params.get("section", "details"), params.get("child_path"),
            params.get("offset", 0), params.get("limit", 50))

    def _handle_get_action_textures(self, params):
        return self.facade.get_action_textures(
            self._require_param(params, "action_event_id"), params.get("direction", "all"),
            params.get("stage"), params.get("show_unused", False), params.get("show_empty", False),
            params.get("offset", 0), params.get("limit", 50))

    def _handle_trace_resource_usage(self, params):
        """Handle trace_resource_usage request."""
        resource_id = self._require_param(params, "resource_id")
        marker_filter = params.get("marker_filter")
        exclude_markers = params.get("exclude_markers")
        event_id_range = params.get("event_id_range")
        before_event_id = params.get("before_event_id")
        return self.facade.trace_resource_usage(
            resource_id=resource_id,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            event_id_range=event_id_range,
            before_event_id=int(before_event_id) if before_event_id is not None else None,
            offset=params.get("offset", 0),
            limit=params.get("limit", 100),
            categories=params.get("categories"),
        )

    def _handle_trace_action_dependencies(self, params):
        """Handle trace_action_dependencies request."""
        action_event_id = self._require_param(params, "action_event_id")
        return self.facade.trace_action_dependencies(int(action_event_id))

    def _handle_diff_actions(self, params):
        """Handle diff_actions request."""
        action_event_id_a = self._require_param(params, "action_event_id_a")
        action_event_id_b = self._require_param(params, "action_event_id_b")
        return self.facade.diff_actions(int(action_event_id_a), int(action_event_id_b))

    def _handle_analyze_pass(self, params):
        """Handle analyze_pass request."""
        marker_filter = self._require_param(params, "marker_filter")
        exclude_markers = params.get("exclude_markers")
        return self.facade.analyze_pass(marker_filter, exclude_markers)

    def _handle_list_captures(self, params):
        """Handle list_captures request"""
        directory = self._require_param(params, "directory")
        return self.facade.list_captures(directory)

    def _handle_open_capture(self, params):
        """Handle open_capture request"""
        capture_path = self._require_param(params, "capture_path")
        return self.facade.open_capture(**params)

    def _handle_get_mesh_summary(self, params):
        """Handle get_mesh_summary request"""
        action_event_id = self._require_param(params, "action_event_id")
        # instance is passed through unconverted so the service's strict
        # non-negative-integer validation applies (no silent float truncation).
        return self.facade.get_mesh_summary(
            int(action_event_id), instance=params.get("instance", 0), view_index=params.get("view_index", 0)
        )

    def _handle_get_mesh_data(self, params):
        """Handle get_mesh_data request"""
        action_event_id = self._require_param(params, "action_event_id")
        stage = params.get("stage", "VSIn")
        offset = params.get("offset", 0)
        limit = params.get("limit", 100)
        attributes = params.get("attributes")
        return self.facade.get_mesh_data(
            action_event_id=int(action_event_id),
            stage=stage,
            offset=int(offset),
            limit=int(limit),
            attributes=attributes,
            instance=params.get("instance", 0),
            view_index=params.get("view_index", 0),
        )

    def _handle_dump_draws(self, params):
        return self.facade.dump_draws(**params)

    def _handle_export_mesh_csv(self, params):
        """Handle export_mesh_csv request"""
        action_event_id = self._require_param(params, "action_event_id")
        output_path = self._require_param(params, "output_path")
        stage = params.get("stage", "VSIn")
        attributes = params.get("attributes")
        return self.facade.export_mesh_csv(
            action_event_id=int(action_event_id),
            output_path=output_path,
            stage=stage,
            attributes=attributes,
            instance=params.get("instance", 0),
            view_index=params.get("view_index", 0),
        )
