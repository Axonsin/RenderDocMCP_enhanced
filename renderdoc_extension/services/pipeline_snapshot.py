"""Request-local Pipeline State model shared by pipeline, texture and analysis tools."""

import hashlib
import json
import math

import renderdoc as rd

from ..utils import Parsers
from .resource_catalog import build_catalog, enum_name, identity
from .native_serialization import plain


STAGES = (
    ("vertex_input", None), ("vertex", "Vertex"), ("tess_control", "Hull"),
    ("tess_eval", "Domain"), ("geometry", "Geometry"), ("task", "Task"),
    ("mesh", "Mesh"), ("rasterizer", None), ("fragment", "Pixel"),
    ("framebuffer", None), ("compute", "Compute"),
)
ALIASES = {
    "vi": "vertex_input", "vs": "vertex", "hs": "tess_control",
    "tcs": "tess_control", "hull": "tess_control", "ds": "tess_eval",
    "tes": "tess_eval", "domain": "tess_eval", "gs": "geometry",
    "as": "task", "ts": "task", "ms": "mesh", "fs": "fragment",
    "ps": "fragment", "pixel": "fragment", "fb": "framebuffer",
    "om": "framebuffer", "cs": "compute",
}
SHADER_SECTIONS = ("shader", "descriptors", "resources", "samplers",
                   "constant_buffers", "push_constants")


def stage_name(value):
    name = str(value).lower()
    name = ALIASES.get(name, name)
    if name not in dict(STAGES):
        raise ValueError("INVALID_STAGE: %s" % value)
    if dict(STAGES)[name] is not None:
        return Parsers.parse_stage_name(name)
    return name


def flag(value, name, enum_type=None):
    member = getattr(enum_type or rd.ActionFlags, name, None)
    return member is not None and bool(value & member)



def unavailable(reason):
    return {"available": False, "reason": str(reason)}


def section_read(operation):
    try:
        return {"available": True, "data": operation()}
    except Exception as exc:
        return unavailable(exc)


def visible(row, show_unused=False, show_empty=False):
    if row["issues"]:
        return True
    if row.get("usage") == "statically_unused" and not show_unused:
        return False
    return show_empty or row.get("bound", False)


class Snapshot:
    """Created and consumed entirely on the replay thread."""

    def __init__(self, ctx, controller, action, generation):
        self.ctx, self.controller, self.action = ctx, controller, action
        self.event_id, self.generation = action.eventId, generation
        self.catalog = build_catalog(controller)
        self.pipe = controller.GetPipelineState()
        self.api = enum_name(controller.GetAPIProperties().pipelineType)
        self.native = None
        self.native_error = None
        getter = {"Vulkan": "GetVulkanPipelineState", "D3D11": "GetD3D11PipelineState",
                  "D3D12": "GetD3D12PipelineState", "OpenGL": "GetGLPipelineState"}.get(self.api)
        if getter:
            try:
                self.native = getattr(controller, getter)()
            except Exception as exc:
                self.native_error = str(exc)
        self.graphics = flag(action.flags, "Drawcall") or flag(action.flags, "MeshDispatch")
        self.compute = flag(action.flags, "Dispatch") and not self.graphics
        self.stages, self.bindings, self.variable_sources = {}, [], {}
        for name, enum in STAGES:
            self._stage(name, enum)
        self.transfer = []
        self.transfer_status = {"available": True}
        if not self.graphics and not self.compute:
            self._transfer()
        # Tokens identify the capture, action, location and current binding contents.
        for row in self.bindings:
            payload = json.dumps([generation, self.event_id, row], sort_keys=True)
            row["binding_id"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def resource(self, rid):
        if rid is None or rid == rd.ResourceId.Null():
            return None
        return identity(self.ctx, rid, self.catalog)

    def _section(self, stage, name, operation):
        stage["sections"][name] = section_read(operation)

    def _stage(self, name, enum):
        stage = {"stage": name, "label": name.replace("_", " ").title(),
                 "status": "not_applicable", "sections": {}}
        self.stages[name] = stage
        applicable = self.compute if name == "compute" else self.graphics
        if not applicable:
            return
        stage["status"] = "enabled"
        if enum:
            stage_enum = getattr(rd.ShaderStage, enum, None)
            if stage_enum is None:
                stage["status"] = "unavailable"
                stage["reason"] = "shader_stage_not_supported"
                return
            try:
                stage["label"] = self.pipe.Abbrev(stage_enum)
                shader = self.pipe.GetShader(stage_enum)
                if shader == rd.ResourceId.Null():
                    stage["status"] = "disabled"
                    return
                reflection = self.pipe.GetShaderReflection(stage_enum)
                pipeline = (self.pipe.GetComputePipelineObject() if name == "compute"
                            else self.pipe.GetGraphicsPipelineObject())
                shader_info = {"resource": self.resource(shader), "pipeline": self.resource(pipeline),
                               "entry_point": self.pipe.GetShaderEntryPoint(stage_enum),
                               "reflection_available": reflection is not None}
                stage["shader"] = shader_info
                self._section(stage, "shader", lambda: shader_info)
                self._section(stage, "descriptors", lambda: self._descriptors(name))
                categories = (
                    ("resources", "GetReadOnlyResources", "readOnlyResources", "read_only"),
                    ("resources", "GetReadWriteResources", "readWriteResources", "read_write"),
                    ("samplers", "GetSamplers", "samplers", "sampler"),
                    ("constant_buffers", "GetConstantBlocks", "constantBlocks", "constant"),
                )
                for section, method, reflect_field, category in categories:
                    result = section_read(lambda: self._shader_bindings(
                        name, stage_enum, reflection, method, reflect_field, category))
                    previous = stage["sections"].get(section)
                    if previous:
                        data = previous.get("data", []) + result.get("data", [])
                        errors = previous.get("errors", [])
                        if not result["available"]:
                            errors = errors + [result["reason"]]
                        if not previous["available"] and "reason" in previous:
                            errors = errors + [previous["reason"]]
                        result = {"available": not errors, "data": data}
                        if errors:
                            result["errors"] = errors
                    stage["sections"][section] = result
                constants = stage["sections"]["constant_buffers"]
                direct = [r for r in constants.get("data", []) if not r["buffer_backed"]]
                constants["data"] = [r for r in constants.get("data", []) if r["buffer_backed"]]
                stage["sections"]["push_constants"] = dict(constants, data=direct)
                if name == "compute":
                    self._section(stage, "dispatch", lambda: {
                        "groups": plain(self.action.dispatchDimension),
                        "threads_per_group": plain(self.action.dispatchThreadsDimension)})
            except Exception as exc:
                stage["status"] = "unavailable"
                stage["reason"] = str(exc)
            return
        if name == "vertex_input":
            if flag(self.action.flags, "MeshDispatch"):
                stage["status"] = "not_applicable"
                return
            self._section(stage, "assembly", lambda: {
                "topology": enum_name(self.pipe.GetPrimitiveTopology()),
                "restart_enabled": self.pipe.IsRestartEnabled(),
                "restart_index": self.pipe.GetRestartIndex()})
            self._section(stage, "attributes", lambda: plain(self.pipe.GetVertexInputs()))
            self._section(stage, "buffers", self._vertex_buffers)
        elif name == "rasterizer":
            self._section(stage, "rasterizer", lambda: {
                "common": plain(self.pipe.GetRasterState()),
                "native": plain(self.native.rasterizer) if self.api == "Vulkan" and self.native
                else unavailable("native_rasterizer_details_not_exposed")})
            self._section(stage, "viewports", lambda: self._viewports(False))
            self._section(stage, "scissors", lambda: self._viewports(True))
            self._section(stage, "multisample", lambda: self._native_field("multisample"))
        elif name == "framebuffer":
            try:
                stage["label"] = self.pipe.OutputAbbrev()
            except Exception:
                pass
            self._section(stage, "attachments", self._attachments)
            if self.api == "Vulkan":
                stage["sections"]["attachments"]["native_renderpass"] = section_read(
                    lambda: self._native_field("currentPass"))
            self._section(stage, "blend", lambda: {
                "targets": plain(self.pipe.GetColorBlends()),
                "factor": plain(self.pipe.GetBlendFactor()),
                "independent": self.pipe.IsIndependentBlendingEnabled()})
            self._section(stage, "depth_stencil", lambda: {
                "depth": plain(self.pipe.GetDepthTestState()),
                "stencil_enabled": self.pipe.IsStencilTestEnabled(),
                "stencil_faces": plain(self.pipe.GetStencilFaces()),
                "native": plain(self.native.depthStencil) if self.api == "Vulkan" and self.native
                else unavailable("native_depth_stencil_details_not_exposed")})

    def _native_field(self, field):
        if self.api != "Vulkan" or self.native is None:
            raise ValueError(self.native_error or "native_%s_not_supported" % field)
        return plain(getattr(self.native, field))

    def _viewports(self, scissors):
        if self.native is None:
            raise ValueError(self.native_error or "native_viewport_count_unavailable")
        if self.api == "Vulkan":
            return [plain(v.scissor if scissors else v.vp) for v in self.native.viewportScissor.viewportScissors]
        return plain(getattr(self.native.rasterizer, "scissors" if scissors else "viewports"))

    def _descriptors(self, stage):
        if self.api != "Vulkan" or self.native is None:
            return {"native": unavailable(self.native_error or "native_descriptor_details_not_supported")}
        pipeline = self.native.compute if stage == "compute" else self.native.graphics
        sets = []
        for index, item in enumerate(pipeline.descriptorSets):
            sets.append({
                "set": index, "resource": self.resource(item.descriptorSetResourceId),
                "layout": self.resource(item.layoutResourceId), "push_descriptor": item.pushDescriptor,
                "dynamic_offsets": plain(item.dynamicOffsets),
                "descriptor_buffer_index": getattr(item, "descriptorBufferIndex", None),
                "descriptor_buffer_byte_offset": getattr(item, "descriptorBufferByteOffset", None),
                "embedded_samplers": getattr(item, "descriptorBufferEmbeddedSamplers", None),
            })
        return {"pipeline": self.resource(pipeline.pipelineResourceId),
                "compute_layout": self.resource(pipeline.pipelineComputeLayoutResourceId),
                "pre_raster_layout": self.resource(pipeline.pipelinePreRastLayoutResourceId),
                "fragment_layout": self.resource(pipeline.pipelineFragmentLayoutResourceId),
                "sets": sets, "descriptor_buffers": plain(pipeline.descriptorBuffers)}

    def _base(self, stage, category, location, label, binding_name=""):
        comparison_location = dict(location)
        if "binding" in comparison_location:
            # Reflection order may change between shaders at the same API binding.
            comparison_location.pop("reflection_index", None)
        store = comparison_location.get("descriptor_store")
        if isinstance(store, dict):
            comparison_location["descriptor_store"] = store["resource_id"]
        key = json.dumps([stage, category, comparison_location],
                         sort_keys=True, separators=(",", ":"))
        return {"stage": stage, "category": category, "location": location, "binding_key": key,
                "label": label, "binding_name": binding_name, "resource": None,
                "bound": False, "usage": "unknown", "roles": [], "issues": []}

    def _describe(self, row, descriptor):
        rid = descriptor.resource
        row["resource"] = self.resource(rid)
        row["bound"] = row["resource"] is not None
        row["view"] = self.resource(getattr(descriptor, "view", None))
        row["secondary"] = self.resource(getattr(descriptor, "secondary", None))
        row["descriptor_type"] = enum_name(getattr(descriptor, "type", "Unknown"))
        row["descriptor_flags"] = enum_name(getattr(descriptor, "flags", "Unknown"))
        row["format"] = plain(getattr(descriptor, "format", None))
        row["view_type"] = enum_name(getattr(descriptor, "textureType", "Unknown"))
        row["descriptor_details"] = plain(descriptor)
        numeric = int(rid) if rid is not None else 0
        texture = self.catalog["textures"].get(numeric)
        buffer = self.catalog["buffers"].get(numeric)
        if texture is not None:
            row["resource_kind"] = "texture"
            row["texture"] = {
                "width": texture.width, "height": texture.height, "depth": texture.depth,
                "array_size": texture.arraysize, "mip_levels": texture.mips,
                "samples": texture.msSamp, "format": plain(texture.format),
            }
            row["subresources"] = {k: getattr(descriptor, prop, None) for k, prop in (
                ("first_mip", "firstMip"), ("mip_count", "numMips"),
                ("first_slice", "firstSlice"), ("slice_count", "numSlices"))}
        elif buffer is not None:
            row["resource_kind"] = "buffer"
            offset, size = descriptor.byteOffset, descriptor.byteSize
            # UINT64_MAX means the remainder of the buffer, not an enormous allocation.
            if size == (1 << 64) - 1:
                size = max(0, buffer.length - offset)
            row["buffer_range"] = {"byte_offset": offset, "byte_size": size,
                                   "end_exclusive": offset + size, "resource_byte_size": buffer.length,
                                   "element_byte_size": getattr(descriptor, "elementByteSize", None)}
            if offset < 0 or size < 0 or offset + size > buffer.length:
                row["issues"].append({"code": "buffer_range_out_of_bounds",
                                      "range_end": offset + size, "resource_bytes": buffer.length})
        else:
            row["resource_kind"] = "unknown"

    def _shader_bindings(self, name, stage, reflection, method, reflect_field, category):
        rows = []
        declarations = getattr(reflection, reflect_field, []) if reflection is not None else []
        for used in getattr(self.pipe, method)(stage, False):
            access, descriptor = used.access, used.descriptor
            index = access.index
            declaration = declarations[index] if 0 <= index < len(declarations) else None
            if category == "constant" and declaration is not None:
                # Unlike raw descriptor-store contents, this includes dynamic offsets.
                descriptor = self.pipe.GetConstantBlock(stage, index, access.arrayElement).descriptor
            location = {"reflection_index": index, "array_element": access.arrayElement}
            if declaration is not None:
                location["binding"] = declaration.fixedBindNumber
                location["set_or_space"] = declaration.fixedBindSetOrSpace
            else:
                location["descriptor_store"] = self.resource(access.descriptorStore)
                location["descriptor_byte_offset"] = access.byteOffset
            prefix = self.stages[name]["label"]
            label = "%s%s %s[%s]" % (prefix, " RW" if category == "read_write" else "",
                                     index, access.arrayElement)
            row = self._base(name, category, location, label,
                             getattr(declaration, "name", ""))
            row["descriptor_store"] = self.resource(access.descriptorStore)
            row["descriptor_byte_offset"] = access.byteOffset
            if self.api == "Vulkan" and self.native is not None and declaration is not None:
                pipeline = self.native.compute if name == "compute" else self.native.graphics
                set_index = declaration.fixedBindSetOrSpace
                if 0 <= set_index < len(pipeline.descriptorSets):
                    native_set = pipeline.descriptorSets[set_index]
                    row["descriptor_set"] = self.resource(native_set.descriptorSetResourceId)
                    row["descriptor_set_layout"] = self.resource(native_set.layoutResourceId)
                    row["dynamic_offsets"] = [
                        plain(d) for d in native_set.dynamicOffsets
                        if d.descriptorByteOffset == access.byteOffset]
            row["usage"] = "statically_unused" if access.staticallyUnused else (
                "possibly_used" if declaration is not None else "unknown")
            row["shader"] = self.resource(self.pipe.GetShader(stage))
            if category == "sampler":
                row["resource"] = self.resource(used.sampler.object)
                row["bound"] = row["resource"] is not None or bool(
                    getattr(used.sampler, "creationTimeConstant", False)) or (
                    enum_name(getattr(used.sampler, "type", "Unknown")) in ("Sampler", "ImageSampler"))
                row["sampler"] = plain(used.sampler)
                row["resource_kind"] = "sampler"
            else:
                self._describe(row, descriptor)
                row["roles"] = ["input", "output"] if category == "read_write" else ["input"]
                if category == "read_only" and (
                        used.sampler.object != rd.ResourceId.Null() or
                        enum_name(getattr(used.sampler, "type", "Unknown")) in ("Sampler", "ImageSampler")):
                    row["combined_sampler"] = {"resource": self.resource(used.sampler.object),
                                               "state": plain(used.sampler)}
            if category == "constant":
                backed = getattr(declaration, "bufferBacked", True)
                row["buffer_backed"] = backed
                if not backed:
                    row["bound"] = declaration is not None
                    row["constant_storage"] = "direct"
                else:
                    row["constant_storage"] = "buffer"
                row["required_bytes"] = getattr(declaration, "byteSize", None)
                row["provided_bytes"] = row.get("buffer_range", {}).get("byte_size")
                row["variable_count"] = len(getattr(declaration, "variables", []))
                required, provided = row["required_bytes"], row["provided_bytes"]
                if backed and required is not None and provided is not None and provided < required:
                    row["issues"].append({"code": "constant_buffer_range_too_small",
                                          "required_bytes": required, "provided_bytes": provided})
                self.variable_sources[row["binding_key"]] = (stage, index, access.arrayElement,
                                                              reflection, declaration)
            if not row["bound"] and declaration is not None and not access.staticallyUnused:
                row["issues"].append({"code": "required_binding_missing",
                                      "evidence": "declared_binding_not_statically_unused"})
            if (row.get("resource_kind") == "unknown" and declaration is not None
                    and getattr(declaration, "isTexture", False)):
                row["resource_kind"] = "texture"
            rows.append(row)
            self.bindings.append(row)
        return rows

    def _vertex_buffers(self):
        rows = []
        buffers = [("vertex", i, b) for i, b in enumerate(self.pipe.GetVBuffers())]
        buffers.append(("index", 0, self.pipe.GetIBuffer()))
        attributes = self.pipe.GetVertexInputs()
        for category, slot, buf in buffers:
            row = self._base("vertex_input", category, {"slot": slot}, "%s %s" % (category, slot))
            row["resource"] = self.resource(buf.resourceId)
            row["resource_kind"], row["bound"], row["roles"] = "buffer", bool(row["resource"]), ["input"]
            row["buffer_range"] = {"byte_offset": buf.byteOffset, "byte_size": buf.byteSize,
                                   "byte_stride": buf.byteStride}
            resource = self.catalog["buffers"].get(int(buf.resourceId))
            if resource is not None:
                size = (max(0, resource.length - buf.byteOffset)
                        if buf.byteSize == (1 << 64) - 1 else buf.byteSize)
                row["buffer_range"].update(byte_size=size, end_exclusive=buf.byteOffset + size,
                                           resource_byte_size=resource.length)
                if buf.byteOffset < 0 or size < 0 or buf.byteOffset + size > resource.length:
                    row["issues"].append({"code": "buffer_range_out_of_bounds",
                                          "range_end": buf.byteOffset + size,
                                          "resource_bytes": resource.length})
            needed = (flag(self.action.flags, "Indexed") if category == "index" else
                      any(a.used and a.vertexBuffer == slot and not a.genericEnabled for a in attributes))
            row["usage"] = "possibly_used" if needed else "statically_unused"
            if needed and not row["bound"]:
                row["issues"].append({"code": "required_binding_missing"})
            rows.append(row)
            self.bindings.append(row)
        return rows

    def _attachments(self):
        rows = []
        targets = [("color", i, d) for i, d in enumerate(self.pipe.GetOutputTargets())]
        targets.append(("depth_stencil", 0, self.pipe.GetDepthTarget()))
        if hasattr(self.pipe, "GetDepthResolveTarget"):
            targets.append(("depth_resolve", 0, self.pipe.GetDepthResolveTarget()))
        for category, index, descriptor in targets:
            row = self._base("framebuffer", category, {"index": index},
                             "%s %s" % (self.stages["framebuffer"]["label"],
                                        index if category == "color" else category))
            self._describe(row, descriptor)
            row["resource_kind"], row["roles"] = "texture", ["output"]
            row["usage"] = "bound" if row["bound"] else "unknown"
            if category == "depth_stencil":
                row["read_only"] = self._depth_read_only()
            rows.append(row)
            self.bindings.append(row)
        return rows

    def _depth_read_only(self):
        # Write state is distinct from attachment/view read-only flags.
        return section_read(lambda: {
            "depth_writes_enabled": self.pipe.GetDepthTestState().depthWrites,
            "stencil_test_enabled": self.pipe.IsStencilTestEnabled(),
            "stencil_faces": plain(self.pipe.GetStencilFaces()),
            "attachment_access": self._attachment_access(),
        })

    def _attachment_access(self):
        if self.api == "Vulkan" and self.native:
            rp, fb = self.native.currentPass.renderpass, self.native.currentPass.framebuffer
            index = rp.depthstencilAttachment
            if 0 <= index < len(fb.attachments):
                attachment = fb.attachments[index]
                layouts = []
                for image in getattr(self.native, "images", []):
                    if image.resourceId == attachment.resource:
                        layouts = [plain(layout) for layout in image.layouts
                                   if layout.baseMip < attachment.firstMip + attachment.numMips
                                   and layout.baseMip + layout.numMip > attachment.firstMip
                                   and layout.baseLayer < attachment.firstSlice + attachment.numSlices
                                   and layout.baseLayer + layout.numLayer > attachment.firstSlice]
                        break
                return {"view": plain(attachment), "image_layouts": layouts,
                        "read_only_flags": unavailable("Vulkan uses per-aspect image layouts and write state")}
        if self.api in ("D3D11", "D3D12") and self.native:
            om = self.native.outputMerger
            return {"depth_read_only": getattr(om, "depthReadOnly", None),
                    "stencil_read_only": getattr(om, "stencilReadOnly", None)}
        return unavailable("attachment_read_only_flags_unavailable")

    def _transfer(self):
        copying = flag(self.action.flags, "Copy") or flag(self.action.flags, "Resolve")
        clearing = flag(self.action.flags, "Clear")
        if not copying and not clearing:
            self.transfer_status = unavailable("action_has_no_supported_texture_operation")
            return
        targets = []
        if copying:
            targets.append(("source", self.action.copySource, self.action.copySourceSubresource, "input"))
        targets.append(("destination", self.action.copyDestination,
                        getattr(self.action, "copyDestinationSubresource", None), "output"))
        for label, rid, sub, role in targets:
            tex = self.catalog["textures"].get(int(rid))
            if tex is None:
                if clearing or rid == rd.ResourceId.Null():
                    self.transfer_status = unavailable("texture_target_not_available")
                continue
            row = self._base("transfer", label, {"role": role}, "SRC" if role == "input" else "DST")
            row.update(resource=self.resource(rid), resource_kind="texture", bound=True,
                       usage="action_target", roles=[role],
                       texture={"width": tex.width, "height": tex.height, "depth": tex.depth,
                                "format": plain(tex.format), "mip_levels": tex.mips,
                                "array_size": tex.arraysize, "samples": tex.msSamp},
                       subresources=plain(sub) if copying else unavailable("clear_subresource_range_unavailable"))
            self.bindings.append(row)
            self.transfer.append(row)

    def overview(self):
        stages = []
        for name, unused in STAGES:
            stage = self.stages[name]
            rows = [r for r in self.bindings if r["stage"] == name]
            stages.append({k: v for k, v in stage.items() if k != "sections"})
            stages[-1].update(
                sections={k: {f: v[f] for f in ("available", "reason", "errors") if f in v}
                          for k, v in stage["sections"].items()},
                binding_count=len(rows),
                issues=[dict(issue, binding_id=r["binding_id"]) for r in rows for issue in r["issues"]])
        pipelines = []
        for stage in stages:
            pipeline = stage.get("shader", {}).get("pipeline")
            if pipeline and pipeline not in pipelines:
                pipelines.append(pipeline)
        action = {"action_event_id": self.event_id, "flags": enum_name(self.action.flags)}
        try:
            action["name"] = self.action.GetName(self.ctx.GetStructuredFile())
        except Exception as exc:
            action["name_unavailable"] = str(exc)
        return {"action_event_id": self.event_id, "action": action,
                "api": self.api, "pipelines": pipelines,
                "pipeline_kind": "graphics" if self.graphics else "compute" if self.compute else "none",
                "stages": stages}

    def texture_rows(self):
        return [r for r in self.bindings if r.get("resource_kind") == "texture"]
