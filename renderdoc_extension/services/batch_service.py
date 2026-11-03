"""Event-scoped batch exports, executed as resumable replay-thread steps."""
import os

import renderdoc as rd

from .replay_query import require_action


class BatchService:
    def __init__(self, ctx, invoke_fn, mesh_service, session=None, jobs=None):
        self.ctx, self._invoke, self._mesh = ctx, invoke_fn, mesh_service
        self.session, self.jobs = session, jobs
        if jobs is not None:
            jobs.recovery_handlers['dump_draws'] = self._recover

    def _recover(self, record):
        from .batch_export import BatchExport
        return BatchExport(self).recover(record)

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
                   action_event_id_range=None, instances=None, view_index=0,
                   export_constants=True, max_textures=48, max_texture_edge=None,
                   skip_depth=False, job_id=None, export_options=None):
        from .batch_export import BatchExport
        params = dict(output_dir=output_dir, action_event_ids=action_event_ids, marker_filter=marker_filter,
            action_event_id_range=action_event_id_range, instances=instances, view_index=view_index,
            export_constants=export_constants, max_textures=max_textures, max_texture_edge=max_texture_edge,
            skip_depth=skip_depth, job_id=job_id, export_options={} if export_options is None else export_options)
        return BatchExport(self).submit(params)
