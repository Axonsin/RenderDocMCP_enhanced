"""
High-level analysis service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Helpers, Parsers, Serializers


class AnalysisService:
    """High-level analysis-oriented operations built on top of canonical primitives."""

    def __init__(
        self,
        ctx,
        invoke_fn,
        action_service,
        pipeline_service,
        resource_service,
        mesh_service,
    ):
        self.ctx = ctx
        self._invoke = invoke_fn
        self._action = action_service
        self._pipeline = pipeline_service
        self._resource = resource_service
        self._mesh = mesh_service

    def inspect_event(self, event_id):
        """Build a compact analysis-oriented inspection bundle for an event."""
        details = self._action.get_draw_call_details(event_id)
        pipeline = self._pipeline.get_pipeline_state(event_id)
        timings = self._action.get_action_timings(event_ids=[event_id])

        timing_summary = {
            "available": bool(timings.get("available")),
        }
        if timings.get("available"):
            timing_entry = None
            for entry in timings.get("timings", []):
                if entry.get("event_id") == event_id:
                    timing_entry = entry
                    break
            timing_summary["event"] = timing_entry
        else:
            timing_summary["reason"] = timings.get("error", "")

        mesh_summary = None
        if "Drawcall" in details.get("flags", []):
            try:
                mesh_summary = self._mesh.get_mesh_summary(event_id)
            except ValueError:
                mesh_summary = None

        shader_summary = []
        shader_map = pipeline.get("shaders", {})
        for stage_name in sorted(shader_map.keys()):
            stage_info = shader_map[stage_name]
            shader_summary.append({
                "stage": stage_name,
                "resource_id": stage_info.get("resource_id"),
                "entry_point": stage_info.get("entry_point", ""),
                "read_only_resource_count": len(stage_info.get("resources", [])),
                "read_write_resource_count": len(stage_info.get("uavs", [])),
                "sampler_count": len(stage_info.get("samplers", [])),
                "constant_buffer_count": len(stage_info.get("constant_buffers", [])),
            })

        pipeline_summary = {
            "api": pipeline.get("api"),
            "input_assembly": pipeline.get("input_assembly", {}),
            "viewports": pipeline.get("viewports", []),
            "render_targets": pipeline.get("render_targets", []),
            "depth_target": pipeline.get("depth_target"),
            "input_textures": pipeline.get("input_textures", []),
            "output_textures": pipeline.get("output_textures", []),
            "input_count": pipeline.get("input_count", 0),
            "output_count": pipeline.get("output_count", 0),
        }

        return {
            "event_id": event_id,
            "name": details.get("name", ""),
            "action_id": details.get("action_id"),
            "flags": details.get("flags", []),
            "details": details,
            "timing": timing_summary,
            "shaders": shader_summary,
            "pipeline": pipeline_summary,
            "mesh": mesh_summary,
        }

    def summarize_capture(self):
        """Summarize the loaded capture with likely next investigation entry points."""
        summary = self._action.get_frame_summary()
        timings = self._action.get_action_timings()

        hot_actions = []
        if timings.get("available"):
            hot_actions = sorted(
                timings.get("timings", []),
                key=lambda item: item.get("duration_ms", 0.0),
                reverse=True,
            )[:10]

        entry_points = []
        seen_event_ids = set()

        for marker in summary.get("top_level_markers", [])[:5]:
            entry_points.append({
                "type": "marker",
                "name": marker.get("name", ""),
                "event_id": marker.get("event_id"),
                "reason": "top_level_marker",
            })
            if marker.get("event_id") is not None:
                seen_event_ids.add(marker.get("event_id"))

        for action in hot_actions[:5]:
            if action.get("event_id") in seen_event_ids:
                continue
            entry_points.append({
                "type": "hot_action",
                "name": action.get("name", ""),
                "event_id": action.get("event_id"),
                "reason": "high_gpu_duration",
                "duration_ms": action.get("duration_ms"),
            })
            seen_event_ids.add(action.get("event_id"))

        return {
            "api": summary.get("api"),
            "total_actions": summary.get("total_actions", 0),
            "statistics": summary.get("statistics", {}),
            "top_level_markers": summary.get("top_level_markers", []),
            "resource_counts": summary.get("resource_counts", {}),
            "hot_actions": hot_actions,
            "suggested_entry_points": entry_points,
        }

    def trace_resource_usage(
        self,
        resource_id,
        marker_filter=None,
        exclude_markers=None,
        event_id_min=None,
        event_id_max=None,
        before_event_id=None,
    ):
        """Trace how a resource is used across matching events in the capture."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"data": None, "error": None}

        def callback(controller):
            structured_file = controller.GetStructuredFile()
            action_index = self._build_action_index(
                controller.GetRootActions(), structured_file
            )
            catalog = self._build_resource_catalog(controller)
            resource_info = self._get_resource_info(resource_id, catalog)

            # Use the original raw ResourceId from the catalog for GetUsage,
            # because re-constructed ResourceId objects don't work in OpenGL.
            numeric_id = Parsers.extract_numeric_id(resource_id)
            rid = None
            tex = catalog["textures"].get(numeric_id)
            buf = catalog["buffers"].get(numeric_id)
            if tex is not None:
                rid = tex.resourceId
            elif buf is not None:
                rid = buf.resourceId

            if rid is None:
                result["error"] = "INVALID_RESOURCE_ID: %s" % resource_id
                return

            usage_entries = []
            usage_histogram = {}
            roles = set()

            try:
                usages = controller.GetUsage(rid)
            except Exception as exc:
                result["error"] = "RESOURCE_QUERY_FAILED: %s" % str(exc)
                return

            for usage in usages:
                action_info = action_index.get(usage.eventId)
                if not self._matches_filters(
                    action_info,
                    marker_filter=marker_filter,
                    exclude_markers=exclude_markers,
                    event_id_min=event_id_min,
                    event_id_max=event_id_max,
                ):
                    continue

                usage_name = self._enum_name(usage.usage)
                access = self._classify_usage_access(usage_name)
                usage_histogram[usage_name] = usage_histogram.get(usage_name, 0) + 1
                roles.update(self._usage_roles(usage_name))

                entry = {
                    "event_id": usage.eventId,
                    "name": action_info.get("name", ""),
                    "marker_path": action_info.get("marker_path", ""),
                    "flags": action_info.get("flags", []),
                    "usage": usage_name,
                    "access": access,
                }
                if getattr(usage, "view", rd.ResourceId.Null()) != rd.ResourceId.Null():
                    entry["view_resource_id"] = Parsers.canonical_resource_id(usage.view)
                usage_entries.append(entry)

            usage_entries.sort(key=lambda item: item["event_id"])

            reads = [
                item for item in usage_entries
                if item["access"] in ("read", "read_write")
            ]
            writes = [
                item for item in usage_entries
                if item["access"] in ("write", "read_write")
            ]

            latest_writer_before_event = None
            if before_event_id is not None:
                for item in writes:
                    if item["event_id"] < before_event_id:
                        latest_writer_before_event = item
                    else:
                        break

            result["data"] = {
                "resource": resource_info,
                "roles": sorted(roles),
                "usage_counts": usage_histogram,
                "event_count": len(usage_entries),
                "read_count": len(reads),
                "write_count": len(writes),
                "first_writer": writes[0] if writes else None,
                "latest_writer": writes[-1] if writes else None,
                "latest_writer_before_event": latest_writer_before_event,
                "reads": reads,
                "writes": writes,
                "events": usage_entries,
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]

    def trace_event_dependencies(self, event_id):
        """Trace immediate resource dependencies for an event."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"data": None, "error": None}

        def callback(controller):
            controller.SetFrameEvent(event_id, True)

            action = self.ctx.GetAction(event_id)
            if not action:
                result["error"] = "INVALID_EVENT_ID: no action at event %d" % event_id
                return

            structured_file = controller.GetStructuredFile()
            action_index = self._build_action_index(
                controller.GetRootActions(), structured_file
            )
            catalog = self._build_resource_catalog(controller)
            pipe = controller.GetPipelineState()

            inputs_by_stage = {}
            input_resources = []
            output_resources = []
            seen_outputs = set()

            for stage in Helpers.get_all_shader_stages():
                stage_name = Parsers.stage_name(stage)
                stage_inputs = []

                try:
                    for srv in pipe.GetReadOnlyResources(stage, False):
                        rid = srv.descriptor.resource
                        if rid == rd.ResourceId.Null():
                            continue
                        stage_inputs.append(
                            self._make_binding_entry(
                                rid,
                                catalog,
                                binding_type="srv",
                                stage=stage_name,
                                slot=srv.access.index,
                            )
                        )
                except Exception:
                    pass

                try:
                    for cb in pipe.GetConstantBlocks(stage, False):
                        rid = cb.descriptor.resource
                        if rid == rd.ResourceId.Null():
                            continue
                        stage_inputs.append(
                            self._make_binding_entry(
                                rid,
                                catalog,
                                binding_type="constant_buffer",
                                stage=stage_name,
                                slot=cb.access.index,
                            )
                        )
                except Exception:
                    pass

                try:
                    for uav in pipe.GetReadWriteResources(stage, False):
                        rid = uav.descriptor.resource
                        if rid == rd.ResourceId.Null():
                            continue
                        uav_entry = self._make_binding_entry(
                            rid,
                            catalog,
                            binding_type="uav",
                            stage=stage_name,
                            slot=uav.access.index,
                        )
                        stage_inputs.append(uav_entry)
                        output_key = (Parsers.extract_numeric_id(rid), stage_name, uav.access.index)
                        if output_key not in seen_outputs:
                            seen_outputs.add(output_key)
                            output_resources.append(dict(uav_entry))
                except Exception:
                    pass

                for entry in stage_inputs:
                    producer = self._find_latest_writer_before_event(
                        controller,
                        action_index,
                        entry["resource_id"],
                        event_id,
                        catalog,
                    )
                    entry["producer_event"] = producer
                    input_resources.append(entry)

                if stage_inputs:
                    inputs_by_stage[stage_name] = stage_inputs

            input_assembly = self._collect_input_assembly_dependencies(
                pipe,
                controller,
                action_index,
                catalog,
                event_id,
            )

            for entry in input_assembly:
                input_resources.append(entry)

            try:
                for index, rt in enumerate(pipe.GetOutputTargets()):
                    if rt.resource == rd.ResourceId.Null():
                        continue
                    output_resources.append(
                        self._make_binding_entry(
                            rt.resource,
                            catalog,
                            binding_type="render_target",
                            slot=index,
                        )
                    )
            except Exception:
                pass

            try:
                depth = pipe.GetDepthTarget()
                if depth.resource != rd.ResourceId.Null():
                    output_resources.append(
                        self._make_binding_entry(
                            depth.resource,
                            catalog,
                            binding_type="depth_target",
                        )
                    )
            except Exception:
                pass

            result["data"] = {
                "event_id": event_id,
                "name": action.GetName(structured_file),
                "flags": Serializers.serialize_flags(action.flags),
                "inputs_by_stage": inputs_by_stage,
                "input_assembly": input_assembly,
                "output_resources": output_resources,
                "input_resource_count": len(input_resources),
                "output_resource_count": len(output_resources),
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]

    def diff_events(self, event_id_a, event_id_b):
        """Compare two events using normalized compact inspection snapshots."""
        event_a = self.inspect_event(event_id_a)
        event_b = self.inspect_event(event_id_b)

        shader_differences = []
        shader_map_a = self._index_by_key(event_a.get("shaders", []), "stage")
        shader_map_b = self._index_by_key(event_b.get("shaders", []), "stage")
        for stage in sorted(set(shader_map_a.keys()) | set(shader_map_b.keys())):
            left = shader_map_a.get(stage)
            right = shader_map_b.get(stage)
            if left != right:
                shader_differences.append({
                    "stage": stage,
                    "event_a": left,
                    "event_b": right,
                })

        texture_inputs_a = self._index_bindings(
            event_a.get("pipeline", {}).get("input_textures", []),
            ("stage", "slot"),
        )
        texture_inputs_b = self._index_bindings(
            event_b.get("pipeline", {}).get("input_textures", []),
            ("stage", "slot"),
        )

        output_textures_a = self._index_bindings(
            event_a.get("pipeline", {}).get("output_textures", []),
            ("type", "index"),
        )
        output_textures_b = self._index_bindings(
            event_b.get("pipeline", {}).get("output_textures", []),
            ("type", "index"),
        )

        draw_parameter_differences = {}
        for key in (
            "num_indices",
            "num_instances",
            "base_vertex",
            "vertex_offset",
            "instance_offset",
            "index_offset",
        ):
            if event_a.get("details", {}).get(key) != event_b.get("details", {}).get(key):
                draw_parameter_differences[key] = {
                    "event_a": event_a.get("details", {}).get(key),
                    "event_b": event_b.get("details", {}).get(key),
                }

        mesh_differences = {}
        for key in ("topology", "num_vertices", "num_indices", "indexed"):
            left_mesh = (event_a.get("mesh") or {}).get(key)
            right_mesh = (event_b.get("mesh") or {}).get(key)
            if left_mesh != right_mesh:
                mesh_differences[key] = {
                    "event_a": left_mesh,
                    "event_b": right_mesh,
                }

        timing_delta_ms = None
        timing_a = ((event_a.get("timing") or {}).get("event") or {}).get("duration_ms")
        timing_b = ((event_b.get("timing") or {}).get("event") or {}).get("duration_ms")
        if timing_a is not None and timing_b is not None:
            timing_delta_ms = timing_b - timing_a

        return {
            "event_a": {
                "event_id": event_a.get("event_id"),
                "name": event_a.get("name", ""),
                "flags": event_a.get("flags", []),
            },
            "event_b": {
                "event_id": event_b.get("event_id"),
                "name": event_b.get("name", ""),
                "flags": event_b.get("flags", []),
            },
            "differences": {
                "shader_changes": shader_differences,
                "input_texture_changes": self._diff_indexed_bindings(
                    texture_inputs_a, texture_inputs_b
                ),
                "output_texture_changes": self._diff_indexed_bindings(
                    output_textures_a, output_textures_b
                ),
                "draw_parameter_changes": draw_parameter_differences,
                "mesh_changes": mesh_differences,
                "timing_delta_ms": timing_delta_ms,
            },
        }

    def analyze_pass(self, marker_filter, exclude_markers=None):
        """Aggregate action, shader, resource, and timing information under a marker subtree."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"data": None, "error": None, "event_ids": []}

        def callback(controller):
            root_actions = controller.GetRootActions()
            structured_file = controller.GetStructuredFile()
            action_index = self._build_action_index(root_actions, structured_file)
            catalog = self._build_resource_catalog(controller)

            selected = [
                info for info in action_index.values()
                if self._matches_filters(
                    info,
                    marker_filter=marker_filter,
                    exclude_markers=exclude_markers,
                )
                and not info.get("is_marker")
            ]
            selected.sort(key=lambda item: item["event_id"])

            if not selected:
                result["error"] = "INVALID_MARKER_FILTER: no actions matched marker_filter %s" % marker_filter
                return

            result["event_ids"] = [info["event_id"] for info in selected]

            shader_counts = {}
            render_target_counts = {}
            input_resource_counts = {}
            marker_paths = set()
            stats = {
                "action_count": len(selected),
                "draw_count": 0,
                "dispatch_count": 0,
            }

            for info in selected:
                action = info["action"]
                marker_paths.add(info.get("marker_path", ""))

                if action.flags & rd.ActionFlags.Drawcall:
                    stats["draw_count"] += 1
                if action.flags & rd.ActionFlags.Dispatch:
                    stats["dispatch_count"] += 1

                controller.SetFrameEvent(action.eventId, False)
                pipe = controller.GetPipelineState()

                for stage in Helpers.get_all_shader_stages():
                    shader = pipe.GetShader(stage)
                    if shader == rd.ResourceId.Null():
                        continue
                    key = Parsers.stage_name(stage)
                    entry_point = ""
                    try:
                        entry_point = pipe.GetShaderEntryPoint(stage)
                    except Exception:
                        pass
                    shader_key = "%s|%s|%s" % (
                        key,
                        Parsers.canonical_resource_id(shader),
                        entry_point,
                    )
                    if shader_key not in shader_counts:
                        shader_counts[shader_key] = {
                            "stage": key,
                            "resource_id": Parsers.canonical_resource_id(shader),
                            "entry_point": entry_point,
                            "count": 0,
                        }
                    shader_counts[shader_key]["count"] += 1

                    try:
                        for srv in pipe.GetReadOnlyResources(stage, False):
                            rid = srv.descriptor.resource
                            if rid == rd.ResourceId.Null():
                                continue
                            res_key = Parsers.canonical_resource_id(rid)
                            if res_key not in input_resource_counts:
                                input_resource_counts[res_key] = self._make_binding_entry(
                                    rid,
                                    catalog,
                                    binding_type="input_resource",
                                    stage=key,
                                    slot=srv.access.index,
                                )
                                input_resource_counts[res_key]["count"] = 0
                            input_resource_counts[res_key]["count"] += 1
                    except Exception:
                        pass

                try:
                    for index, rt in enumerate(pipe.GetOutputTargets()):
                        if rt.resource == rd.ResourceId.Null():
                            continue
                        res_key = "%s:%d" % (Parsers.canonical_resource_id(rt.resource), index)
                        if res_key not in render_target_counts:
                            render_target_counts[res_key] = self._make_binding_entry(
                                rt.resource,
                                catalog,
                                binding_type="render_target",
                                slot=index,
                            )
                            render_target_counts[res_key]["write_count"] = 0
                        render_target_counts[res_key]["write_count"] += 1
                except Exception:
                    pass

                try:
                    depth = pipe.GetDepthTarget()
                    if depth.resource != rd.ResourceId.Null():
                        res_key = "%s:depth" % Parsers.canonical_resource_id(depth.resource)
                        if res_key not in render_target_counts:
                            render_target_counts[res_key] = self._make_binding_entry(
                                depth.resource,
                                catalog,
                                binding_type="depth_target",
                            )
                            render_target_counts[res_key]["write_count"] = 0
                        render_target_counts[res_key]["write_count"] += 1
                except Exception:
                    pass

            warnings = []
            repeated_targets = [
                target for target in render_target_counts.values()
                if target.get("write_count", 0) >= 5
            ]
            if repeated_targets:
                warnings.append({
                    "type": "repeated_target_writes",
                    "message": "One or more output targets are written repeatedly within the pass.",
                    "targets": repeated_targets[:5],
                })

            if len(render_target_counts) >= 4:
                warnings.append({
                    "type": "target_churn",
                    "message": "Multiple output targets are touched within the selected pass subtree.",
                    "target_count": len(render_target_counts),
                })

            result["data"] = {
                "marker_filter": marker_filter,
                "matched_marker_paths": sorted(
                    [path for path in marker_paths if path]
                )[:20],
                "statistics": stats,
                "event_range": {
                    "min": selected[0]["event_id"],
                    "max": selected[-1]["event_id"],
                },
                "main_shaders": sorted(
                    shader_counts.values(),
                    key=lambda item: item["count"],
                    reverse=True,
                )[:10],
                "render_targets_written": sorted(
                    render_target_counts.values(),
                    key=lambda item: item.get("write_count", 0),
                    reverse=True,
                )[:10],
                "representative_input_resources": sorted(
                    input_resource_counts.values(),
                    key=lambda item: item.get("count", 0),
                    reverse=True,
                )[:10],
                "top_timed_actions": [],
                "warnings": warnings,
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])

        timings = self._action.get_action_timings(event_ids=result.get("event_ids") or None)
        if timings.get("available"):
            result["data"]["top_timed_actions"] = sorted(
                timings.get("timings", []),
                key=lambda item: item.get("duration_ms", 0.0),
                reverse=True,
            )[:10]
        return result["data"]

    def _build_action_index(self, actions, structured_file, parent_markers=None, index=None):
        """Build an event_id keyed action index with marker path context."""
        if parent_markers is None:
            parent_markers = []
        if index is None:
            index = {}

        for action in actions:
            name = action.GetName(structured_file)
            is_marker = self._is_marker(action.flags)
            is_push_like = bool(action.flags & (rd.ActionFlags.PushMarker | rd.ActionFlags.SetMarker))

            marker_path = "/".join(parent_markers)
            action_marker_path = marker_path
            if is_push_like:
                action_marker_path = "/".join(parent_markers + [name]) if parent_markers else name

            index[action.eventId] = {
                "event_id": action.eventId,
                "name": name,
                "flags": Serializers.serialize_flags(action.flags),
                "marker_path": action_marker_path,
                "is_marker": is_marker,
                "action": action,
            }

            child_markers = parent_markers
            if is_push_like:
                child_markers = parent_markers + [name]

            if action.children:
                self._build_action_index(action.children, structured_file, child_markers, index)

        return index

    @staticmethod
    def _is_marker(flags):
        """Return True if action flags identify a marker event."""
        return bool(flags & (rd.ActionFlags.PushMarker | rd.ActionFlags.SetMarker | rd.ActionFlags.PopMarker))

    @staticmethod
    def _matches_filters(
        action_info,
        marker_filter=None,
        exclude_markers=None,
        event_id_min=None,
        event_id_max=None,
    ):
        """Match action metadata against optional marker/range filters."""
        if action_info is None:
            return False

        marker_path = action_info.get("marker_path", "")
        if marker_filter and marker_filter.lower() not in marker_path.lower():
            return False

        if exclude_markers:
            marker_path_lower = marker_path.lower()
            for exclude in exclude_markers:
                if exclude.lower() in marker_path_lower:
                    return False

        event_id = action_info.get("event_id")
        if event_id_min is not None and event_id < event_id_min:
            return False
        if event_id_max is not None and event_id > event_id_max:
            return False
        return True

    def _build_resource_catalog(self, controller):
        """Build a lightweight lookup catalog for resources in the capture."""
        catalog = {
            "textures": {},
            "buffers": {},
            "resources": {},
            "cache": {},
        }

        try:
            for tex in controller.GetTextures():
                catalog["textures"][int(tex.resourceId)] = tex
        except Exception:
            pass

        try:
            for buf in controller.GetBuffers():
                catalog["buffers"][int(buf.resourceId)] = buf
        except Exception:
            pass

        try:
            for res in controller.GetResources():
                catalog["resources"][int(res.resourceId)] = res
        except Exception:
            pass

        return catalog

    def _get_resource_info(self, resource_id, catalog):
        """Get cached resource metadata."""
        numeric_id = Parsers.extract_numeric_id(resource_id)
        if numeric_id in catalog["cache"]:
            return catalog["cache"][numeric_id]

        info = {
            "resource_id": "ResourceId::%d" % numeric_id,
            "name": "",
        }

        tex = catalog["textures"].get(numeric_id)
        buf = catalog["buffers"].get(numeric_id)
        res = catalog["resources"].get(numeric_id)

        # Use the original raw ResourceId from the catalog for name lookup,
        # because re-constructed ResourceId objects may not work with
        # GetResourceName in OpenGL.
        name_source = None
        if tex is not None:
            name_source = tex.resourceId
        elif buf is not None:
            name_source = buf.resourceId
        if name_source is not None:
            info["name"] = self._safe_resource_name(name_source)
        else:
            info["name"] = self._safe_resource_name(resource_id)

        if tex is not None:
            info.update({
                "resource_type": "texture",
                "width": tex.width,
                "height": tex.height,
                "depth": tex.depth,
                "array_size": tex.arraysize,
                "mip_levels": tex.mips,
                "format": str(tex.format.Name()),
                "dimension": str(tex.type),
                "byte_size": tex.byteSize,
                "msaa_samples": tex.msSamp,
            })
        elif buf is not None:
            info.update({
                "resource_type": "buffer",
                "byte_size": buf.length,
                "creation_flags": self._resource._parse_buffer_flags(buf.creationFlags),
            })

        if res is not None:
            info["resource_kind"] = self._enum_name(res.type)
            info["parent_resources"] = [
                Parsers.canonical_resource_id(parent)
                for parent in getattr(res, "parentResources", [])
            ]
            info["derived_resources"] = [
                Parsers.canonical_resource_id(child)
                for child in getattr(res, "derivedResources", [])
            ]

        catalog["cache"][numeric_id] = info
        return info

    def _make_binding_entry(
        self,
        resource_id,
        catalog,
        binding_type,
        stage=None,
        slot=None,
    ):
        """Build a normalized resource binding entry."""
        entry = dict(self._get_resource_info(resource_id, catalog))
        entry["binding_type"] = binding_type
        if stage is not None:
            entry["stage"] = stage
        if slot is not None:
            entry["slot"] = slot
        return entry

    def _collect_input_assembly_dependencies(
        self,
        pipe,
        controller,
        action_index,
        catalog,
        event_id,
    ):
        """Collect vertex/index buffer dependencies."""
        dependencies = []

        try:
            for slot, vb in enumerate(pipe.GetVBuffers()):
                if vb.resourceId == rd.ResourceId.Null():
                    continue
                entry = self._make_binding_entry(
                    vb.resourceId,
                    catalog,
                    binding_type="vertex_buffer",
                    slot=slot,
                )
                entry["producer_event"] = self._find_latest_writer_before_event(
                    controller, action_index, entry["resource_id"], event_id, catalog
                )
                dependencies.append(entry)
        except Exception:
            pass

        try:
            ib = pipe.GetIBuffer()
            if ib.resourceId != rd.ResourceId.Null():
                entry = self._make_binding_entry(
                    ib.resourceId,
                    catalog,
                    binding_type="index_buffer",
                )
                entry["producer_event"] = self._find_latest_writer_before_event(
                    controller, action_index, entry["resource_id"], event_id, catalog
                )
                dependencies.append(entry)
        except Exception:
            pass

        return dependencies

    def _find_latest_writer_before_event(self, controller, action_index, resource_id, event_id, catalog=None):
        """Find the latest write-like usage before a given event."""
        try:
            if catalog is not None:
                numeric_id = Parsers.extract_numeric_id(resource_id)
                tex = catalog["textures"].get(numeric_id)
                buf = catalog["buffers"].get(numeric_id)
                if tex is not None:
                    rid = tex.resourceId
                elif buf is not None:
                    rid = buf.resourceId
                else:
                    return None
            else:
                rid = Parsers.parse_resource_id(resource_id)
            usages = controller.GetUsage(rid)
        except Exception:
            return None

        latest = None
        for usage in usages:
            usage_name = self._enum_name(usage.usage)
            access = self._classify_usage_access(usage_name)
            if access not in ("write", "read_write"):
                continue
            if usage.eventId >= event_id:
                continue

            action_info = action_index.get(usage.eventId)
            latest = {
                "event_id": usage.eventId,
                "name": action_info.get("name", "") if action_info else "",
                "marker_path": action_info.get("marker_path", "") if action_info else "",
                "usage": usage_name,
            }

        return latest

    @staticmethod
    def _enum_name(value):
        """Convert an enum-like object into a stable simple name."""
        if hasattr(value, "name"):
            return value.name
        text = str(value)
        if "." in text:
            return text.split(".")[-1]
        return text

    @staticmethod
    def _classify_usage_access(usage_name):
        """Classify a RenderDoc ResourceUsage into read/write semantics."""
        if usage_name.endswith("_Resource") or usage_name.endswith("_Constants"):
            return "read"
        if usage_name in ("VertexBuffer", "IndexBuffer", "InputTarget", "Indirect", "CopySrc", "ResolveSrc"):
            return "read"
        if usage_name.endswith("_RWResource"):
            return "read_write"
        if usage_name in ("Copy", "Resolve"):
            return "read_write"
        if usage_name in (
            "ColorTarget",
            "DepthStencilTarget",
            "Clear",
            "Discard",
            "GenMips",
            "CopyDst",
            "ResolveDst",
            "CPUWrite",
            "StreamOut",
        ):
            return "write"
        return "other"

    @staticmethod
    def _usage_roles(usage_name):
        """Map RenderDoc ResourceUsage names to higher-level usage roles."""
        roles = set()
        if usage_name.endswith("_Resource") or usage_name == "All_Resource":
            roles.add("srv")
        if usage_name.endswith("_RWResource") or usage_name == "All_RWResource":
            roles.add("uav")
        if usage_name.endswith("_Constants") or usage_name == "All_Constants":
            roles.add("constant_buffer")
        if usage_name == "VertexBuffer":
            roles.add("vertex_buffer")
        if usage_name == "IndexBuffer":
            roles.add("index_buffer")
        if usage_name == "ColorTarget":
            roles.add("render_target")
        if usage_name == "DepthStencilTarget":
            roles.add("depth_target")
        if usage_name in ("Copy", "CopySrc", "CopyDst"):
            roles.add("copy")
        if usage_name in ("Resolve", "ResolveSrc", "ResolveDst"):
            roles.add("resolve")
        if usage_name == "Indirect":
            roles.add("indirect")
        if usage_name == "InputTarget":
            roles.add("input_attachment")
        return roles

    def _safe_resource_name(self, resource_id):
        """Safely retrieve a resource name from the capture context."""
        try:
            return self.ctx.GetResourceName(resource_id) or ""
        except Exception:
            return ""

    @staticmethod
    def _index_by_key(items, key):
        """Index a list of dictionaries by a single key."""
        indexed = {}
        for item in items:
            indexed[item.get(key)] = item
        return indexed

    @staticmethod
    def _index_bindings(items, keys):
        """Index a list of bindings by a tuple of keys."""
        indexed = {}
        for item in items:
            indexed[tuple(item.get(key) for key in keys)] = item
        return indexed

    @staticmethod
    def _diff_indexed_bindings(left_map, right_map):
        """Diff two indexed binding maps."""
        added = []
        removed = []
        changed = []

        all_keys = sorted(set(left_map.keys()) | set(right_map.keys()))
        for key in all_keys:
            left = left_map.get(key)
            right = right_map.get(key)
            if left is None:
                added.append({"binding": key, "value": right})
            elif right is None:
                removed.append({"binding": key, "value": left})
            elif left != right:
                changed.append({
                    "binding": key,
                    "event_a": left,
                    "event_b": right,
                })

        return {
            "added": added,
            "removed": removed,
            "changed": changed,
        }
