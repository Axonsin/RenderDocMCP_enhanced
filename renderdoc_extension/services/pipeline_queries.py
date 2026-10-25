"""Public views of the request-local pipeline model."""

import uuid

import qrenderdoc as qrd

from .pipeline_snapshot import Snapshot, stage_name, visible
from .replay_query import at_event, require_action
from .resource_catalog import paginate, validate_page
from .shader_variables import read_variables


class PipelineQueries(qrd.CaptureViewer):
    def __init__(self, ctx, invoke_fn, session=None):
        super(PipelineQueries, self).__init__()
        self.ctx, self._invoke = ctx, invoke_fn
        self.session = session
        self._generation = uuid.uuid4().hex
        ctx.AddCaptureViewer(self)

    def OnCaptureLoaded(self):
        self._generation = uuid.uuid4().hex

    def OnCaptureClosed(self):
        self._generation = uuid.uuid4().hex

    def OnSelectedEventChanged(self, event_id):
        pass

    def OnEventChanged(self, event_id):
        pass

    def dispose(self):
        self.ctx.RemoveCaptureViewer(self)

    def _snapshot_query(self, action_event_id, operation):
        action = require_action(self.ctx, action_event_id)
        if self.session:
            self.session.observe_replacements()
        def read(controller, event):
            return operation(Snapshot(self.ctx, controller, action,
                                      self.session.token() if self.session else self._generation))
        return at_event(self.ctx, self._invoke, action_event_id, read)

    def get_pipeline_state(self, action_event_id):
        return self._snapshot_query(action_event_id, lambda snapshot: snapshot.overview())

    @staticmethod
    def _options(show_unused, show_empty, offset, limit):
        validate_page(offset, limit)
        if type(show_unused) is not bool or type(show_empty) is not bool:
            raise ValueError("INVALID_FILTER: show_unused and show_empty must be booleans")

    def get_pipeline_stage(self, action_event_id, stage, section="overview",
                           show_unused=False, show_empty=False, offset=0, limit=50):
        name = stage_name(stage)
        self._options(show_unused, show_empty, offset, limit)

        def query(snapshot):
            item = snapshot.stages[name]
            result = {"action_event_id": action_event_id, "api": snapshot.api, "stage": name,
                      "label": item["label"], "status": item["status"], "section": section}
            if section == "overview":
                result.update(next(s for s in snapshot.overview()["stages"] if s["stage"] == name))
                return result
            if item["status"] != "enabled":
                result.update(available=False, reason=item.get("reason", item["status"]))
                return result
            if section not in item["sections"]:
                raise ValueError("INVALID_SECTION: section is not available for this stage")
            result.update(item["sections"][section])
            data = result.pop("data", None)
            if section == "descriptors" and isinstance(data, dict) and "sets" in data:
                result["data"] = {k: v for k, v in data.items() if k != "sets"}
                result.update(paginate(data["sets"], offset, limit))
                return result
            if isinstance(data, list):
                if data and isinstance(data[0], dict) and "binding_key" in data[0]:
                    data = [r for r in data if visible(r, show_unused, show_empty)]
                result.update(paginate(data, offset, limit))
            elif data is not None:
                result["data"] = data
            return result
        return self._snapshot_query(action_event_id, query)

    def inspect_pipeline_binding(self, action_event_id, binding_id, section="details",
                                 child_path=None, offset=0, limit=50):
        validate_page(offset, limit)
        if section not in ("details", "variables"):
            raise ValueError("INVALID_SECTION: expected details or variables")
        if section == "details" and child_path is not None:
            raise ValueError("INVALID_CHILD_PATH: only variables supports child_path")

        def query(snapshot):
            row = next((r for r in snapshot.bindings if r["binding_id"] == binding_id), None)
            if row is None:
                raise ValueError("INVALID_BINDING_ID: binding is stale or belongs to another action/capture")
            result = {"action_event_id": action_event_id, "api": snapshot.api, "binding": row}
            if section == "details":
                return result
            source = snapshot.variable_sources.get(row["binding_key"])
            if source is None:
                raise ValueError("INVALID_SECTION: variables requires a constant binding")
            stage, index, array_element, reflection, declaration = source
            if reflection is None or declaration is None:
                result.update(available=False, reason="shader_reflection_unavailable")
                return result
            if not row["bound"]:
                result.update(available=False, reason="constant_binding_not_bound")
                return result
            pipe = snapshot.pipe
            # This accessor already includes Vulkan dynamic offsets.
            binding = pipe.GetConstantBlock(stage, index, array_element).descriptor
            pipeline = (pipe.GetComputePipelineObject() if row["stage"] == "compute"
                        else pipe.GetGraphicsPipelineObject())
            values = snapshot.controller.GetCBufferVariableContents(
                pipeline, pipe.GetShader(stage), stage, pipe.GetShaderEntryPoint(stage), index,
                binding.resource, binding.byteOffset,
                row.get("provided_bytes") if row.get("provided_bytes") is not None else binding.byteSize)
            result.update(read_variables(values, declaration.variables,
                                         [] if child_path is None else child_path, offset, limit))
            result["available"] = True
            return result
        return self._snapshot_query(action_event_id, query)

    def get_action_textures(self, action_event_id, direction="all", stage=None,
                            show_unused=False, show_empty=False, offset=0, limit=50):
        self._options(show_unused, show_empty, offset, limit)
        if direction not in ("all", "input", "output"):
            raise ValueError("INVALID_DIRECTION: expected all, input or output")
        name = stage_name(stage) if stage is not None else None

        def query(snapshot):
            rows = [r for r in snapshot.texture_rows()
                    if visible(r, show_unused, show_empty)
                    and (direction == "all" or direction in r["roles"])
                    and (name is None or name == r["stage"])]
            result = {"action_event_id": action_event_id, "api": snapshot.api, "direction": direction}
            result.update(snapshot.transfer_status)
            errors = []
            for item in snapshot.stages.values():
                if name is not None and item["stage"] != name:
                    continue
                if item["status"] == "unavailable":
                    errors.append({"stage": item["stage"], "reason": item.get("reason")})
                for section in ("resources", "attachments"):
                    data = item["sections"].get(section)
                    if data and not data["available"]:
                        errors.append({"stage": item["stage"], "section": section,
                                       "reason": data.get("reason", data.get("errors"))})
            if errors:
                result.update(available=False, errors=errors)
            result.update(paginate(rows, offset, limit))
            return result
        return self._snapshot_query(action_event_id, query)

    def analysis_snapshot(self, action_event_id):
        """Unpaged internal projection; callers must not compose paged public views."""
        def query(snapshot):
            return {"overview": snapshot.overview(), "bindings": snapshot.bindings,
                    "textures": snapshot.texture_rows(),
                    "fixed_function": {name: snapshot.stages[name] for name in
                                       ("vertex_input", "rasterizer", "framebuffer")}}
        return self._snapshot_query(action_event_id, query)
