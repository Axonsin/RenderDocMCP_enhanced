"""
Action operations service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Serializers, Helpers
from .resource_catalog import build_catalog, paginate, validate_page
from .structured_data import read_node
from .replay_query import require_action


class ActionService:
    """Action operations service"""

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    def get_actions(
        self,
        include_children=True,
        marker_filter=None,
        exclude_markers=None,
        action_event_id_range=None,
        exclude_marker_actions=False,
        flags_filter=None,
    ):
        """
        Get the action tree in the capture with optional filtering.
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"items": []}

        def callback(controller):
            root_actions = controller.GetRootActions()
            structured_file = controller.GetStructuredFile()
            result["items"] = Serializers.serialize_actions(
                root_actions,
                structured_file,
                include_children,
                marker_filter=marker_filter,
                exclude_markers=exclude_markers,
                action_event_id_range=action_event_id_range,
                exclude_marker_actions=exclude_marker_actions,
                flags_filter=flags_filter,
            )

        def count_items(items):
            total = 0
            for item in items:
                total += 1
                total += count_items(item.get("children", []))
            return total

        self._invoke(callback)
        return {
            "items": result["items"],
            "total_count": count_items(result["items"]),
        }

    def get_frame_summary(self):
        """
        Get a summary of the current capture frame.
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"summary": None}

        def callback(controller):
            root_actions = controller.GetRootActions()
            structured_file = controller.GetStructuredFile()
            api = controller.GetAPIProperties().pipelineType

            # Statistics counters
            stats = {
                "draw_calls": 0,
                "dispatches": 0,
                "clears": 0,
                "copies": 0,
                "presents": 0,
                "markers": 0,
            }
            total_actions = [0]

            def count_actions(actions):
                for action in actions:
                    total_actions[0] += 1
                    flags = action.flags

                    if flags & rd.ActionFlags.Drawcall:
                        stats["draw_calls"] += 1
                    if flags & rd.ActionFlags.Dispatch:
                        stats["dispatches"] += 1
                    if flags & rd.ActionFlags.Clear:
                        stats["clears"] += 1
                    if flags & rd.ActionFlags.Copy:
                        stats["copies"] += 1
                    if flags & rd.ActionFlags.Present:
                        stats["presents"] += 1
                    if flags & (rd.ActionFlags.PushMarker | rd.ActionFlags.SetMarker):
                        stats["markers"] += 1

                    if action.children:
                        count_actions(action.children)

            count_actions(root_actions)

            # Top-level markers
            top_markers = []
            for action in root_actions:
                if action.flags & rd.ActionFlags.PushMarker:
                    child_count = Helpers.count_children(action)
                    top_markers.append({
                        "name": action.GetName(structured_file),
                        "action_event_id": action.eventId,
                        "child_count": child_count,
                    })

            # Resource counts
            textures = controller.GetTextures()
            buffers = controller.GetBuffers()

            result["summary"] = {
                "api": str(api),
                "total_actions": total_actions[0],
                "statistics": stats,
                "top_level_markers": top_markers,
                "resource_counts": {
                    "textures": len(textures),
                    "buffers": len(buffers),
                },
            }

        self._invoke(callback)
        return result["summary"]

    def get_action_details(self, action_event_id):
        """Get metadata, draw counts, offsets and output resources for an action."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        require_action(self.ctx, action_event_id)

        result = {"details": None, "error": None}

        def callback(controller):
            # Move to the event
            controller.SetFrameEvent(action_event_id, True)

            action = self.ctx.GetAction(action_event_id)
            if not action:
                result["error"] = "INVALID_ACTION_EVENT_ID: no action at event %d" % action_event_id
                return

            structured_file = controller.GetStructuredFile()

            details = {
                "action_event_id": action.eventId,
                "action_id": action.actionId,
                "name": action.GetName(structured_file),
                "flags": Serializers.serialize_flags(action.flags),
                "num_indices": action.numIndices,
                "num_instances": action.numInstances,
                "base_vertex": action.baseVertex,
                "vertex_offset": action.vertexOffset,
                "instance_offset": action.instanceOffset,
                "index_offset": action.indexOffset,
            }

            # Output resources
            outputs = []
            for i, output in enumerate(action.outputs):
                if output != rd.ResourceId.Null():
                    outputs.append({"index": i, "resource_id": str(output)})
            details["outputs"] = outputs

            if action.depthOut != rd.ResourceId.Null():
                details["depth_output"] = str(action.depthOut)

            result["details"] = details

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["details"]

    def get_action_api_calls(self, action_event_id, api_event_id=None, child_path=None,
                             offset=0, limit=50):
        """Read the selected action's API events or expand one call's parameters."""
        validate_page(offset, limit)
        if type(action_event_id) is not int or action_event_id <= 0:
            raise ValueError("INVALID_ACTION_EVENT_ID: expected a positive action EID")
        if api_event_id is not None and (type(api_event_id) is not int or api_event_id <= 0):
            raise ValueError("INVALID_API_EVENT_ID: expected a positive API EID")
        if child_path is not None and (
                not isinstance(child_path, list) or
                any(type(i) is not int or i < 0 for i in child_path)):
            raise ValueError("INVALID_CHILD_PATH: expected non-negative child indices")
        if api_event_id is None and child_path:
            raise ValueError("INVALID_CHILD_PATH: api_event_id is required")
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
        result = {}

        def callback(controller):
            try:
                action = self.ctx.GetAction(action_event_id)
                if action is None or action.eventId != action_event_id:
                    raise ValueError("INVALID_ACTION_EVENT_ID: no action at event %d" % action_event_id)
                structured = controller.GetStructuredFile()
                events = list(action.events)
                context = {"action_event_id": int(action.eventId),
                           "name": str(action.GetName(structured))}

                def describe(event):
                    index = int(event.chunkIndex)
                    entry = {"api_event_id": int(event.eventId), "chunk_index": index}
                    if index == getattr(event, "NoChunk", 0xFFFFFFFF):
                        entry.update({"available": False, "reason": "no_chunk", "name": None})
                    elif index < 0 or index >= len(structured.chunks):
                        entry.update({"available": False, "reason": "invalid_chunk_index",
                                      "name": None})
                    else:
                        chunk = structured.chunks[index]
                        entry.update({"available": True, "name": str(chunk.name),
                                      "child_count": chunk.NumChildren()})
                    return entry

                if api_event_id is None:
                    page = paginate(events, offset, limit)
                    page["items"] = [describe(event) for event in page["items"]]
                    context.update(page)
                else:
                    event = next((e for e in events if e.eventId == api_event_id), None)
                    if event is None:
                        raise ValueError("INVALID_API_EVENT_ID: event %d does not belong to action %d"
                                         % (api_event_id, action_event_id))
                    entry = describe(event)
                    context["api_call"] = entry
                    if entry["available"]:
                        context.update(read_node(
                            structured.chunks[entry["chunk_index"]],
                            [] if child_path is None else child_path, self.ctx,
                            build_catalog(controller, descriptors=False), offset, limit))
                result["data"] = context
            except Exception as exc:
                # Exceptions must survive the SWIG BlockInvoke callback boundary.
                result["error"] = exc

        self._invoke(callback)
        if "error" in result:
            raise result["error"]
        return result["data"]

    def get_action_timings(
        self,
        action_event_ids=None,
        marker_filter=None,
        exclude_markers=None,
    ):
        """
        Get GPU timing information for actions.

        Args:
            action_event_ids: Optional list of specific event IDs to get timings for.
                      If None, returns timings for all actions.
            marker_filter: Only include actions under markers containing this string.
            exclude_markers: Exclude actions under markers containing these strings.

        Returns:
            Dictionary with:
            - available: Whether GPU timing counters are supported
            - unit: Time unit (typically "seconds")
            - timings: List of {action_event_id, name, duration_seconds, duration_ms}
            - total_duration_ms: Sum of all durations
        """
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"data": None, "error": None}

        def callback(controller):
            # Check if EventGPUDuration counter is available
            counters = controller.EnumerateCounters()
            if rd.GPUCounter.EventGPUDuration not in counters:
                result["data"] = {
                    "available": False,
                    "error": "GPU timing counters not supported on this capture",
                }
                return

            # Get counter description
            counter_desc = controller.DescribeCounter(rd.GPUCounter.EventGPUDuration)

            # Fetch timing data
            counter_results = controller.FetchCounters([rd.GPUCounter.EventGPUDuration])

            # Build action_event_id to timing map
            timing_map = {}
            target_counter = int(rd.GPUCounter.EventGPUDuration)
            for r in counter_results:
                if r.counter == target_counter:
                    # EventGPUDuration typically returns double
                    # Try to get the value in the most appropriate way
                    val = r.value.d  # double is the standard for duration
                    timing_map[r.eventId] = val

            # Get structured file for action names
            structured_file = controller.GetStructuredFile()
            root_actions = controller.GetRootActions()

            # Collect actions to report timings for
            timings = []
            total_duration = [0.0]

            def collect_timings(actions, parent_markers=None):
                if parent_markers is None:
                    parent_markers = []

                for action in actions:
                    action_name = action.GetName(structured_file)
                    current_markers = parent_markers[:]

                    # Track marker hierarchy
                    is_marker = bool(action.flags & (rd.ActionFlags.PushMarker | rd.ActionFlags.SetMarker))
                    if is_marker:
                        current_markers.append(action_name)

                    # Apply marker filter
                    if marker_filter:
                        marker_path = "/".join(current_markers)
                        if marker_filter.lower() not in marker_path.lower():
                            # Still recurse into children
                            if action.children:
                                collect_timings(action.children, current_markers)
                            continue

                    # Apply exclude filter
                    if exclude_markers:
                        skip = False
                        for exclude in exclude_markers:
                            for m in current_markers:
                                if exclude.lower() in m.lower():
                                    skip = True
                                    break
                            if skip:
                                break
                        if skip:
                            if action.children:
                                collect_timings(action.children, current_markers)
                            continue

                    # Check if we should include this event
                    action_event_id = action.eventId
                    include = True
                    if action_event_ids is not None:
                        include = action_event_id in action_event_ids

                    if include and action_event_id in timing_map:
                        duration_sec = timing_map[action_event_id]
                        duration_ms = duration_sec * 1000.0
                        timings.append({
                            "action_event_id": action_event_id,
                            "name": action_name,
                            "duration_seconds": duration_sec,
                            "duration_ms": duration_ms,
                        })
                        total_duration[0] += duration_ms

                    # Recurse into children
                    if action.children:
                        collect_timings(action.children, current_markers)

            collect_timings(root_actions)

            # Sort by action_event_id
            timings.sort(key=lambda x: x["action_event_id"])

            result["data"] = {
                "available": True,
                "unit": str(counter_desc.unit),
                "timings": timings,
                "total_duration_ms": total_duration[0],
                "count": len(timings),
            }

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["data"]
