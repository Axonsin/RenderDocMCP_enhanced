"""
Pipeline state service for RenderDoc.
"""

import renderdoc as rd

from ..utils import Parsers, Serializers, Helpers


class PipelineService:
    """Pipeline state service"""

    _TEXT_SHADER_ENCODINGS = {
        "GLSL",
        "HLSL",
        "Slang",
        "SPIRVAsm",
        "OpenGLSPIRVAsm",
    }

    def __init__(self, ctx, invoke_fn):
        self.ctx = ctx
        self._invoke = invoke_fn

    def get_shader_info(self, event_id, stage):
        """Get shader information for a specific stage"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"shader": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            pipe = shader_ctx["pipe"]
            stage_enum = shader_ctx["stage_enum"]
            reflection = shader_ctx["reflection"]

            shader_info = {
                "resource_id": shader_ctx["resource_id"],
                "entry_point": shader_ctx["entry_point"],
                "stage": shader_ctx["stage_name"],
            }

            # Get disassembly
            try:
                targets = controller.GetDisassemblyTargets(True)
                if targets:
                    pipeline_obj = (
                        pipe.GetComputePipelineObject()
                        if stage_enum == rd.ShaderStage.Compute
                        else pipe.GetGraphicsPipelineObject()
                    )
                    disasm = controller.DisassembleShader(
                        pipeline_obj, reflection, targets[0]
                    )
                    shader_info["disassembly"] = disasm
            except Exception as e:
                shader_info["disassembly_error"] = str(e)

            # Get constant buffer info
            if reflection:
                shader_info["constant_buffers"] = self._get_cbuffer_info(
                    controller, pipe, reflection, stage_enum
                )
                shader_info["resources"] = self._get_resource_bindings(reflection)

            result["shader"] = shader_info

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["shader"]

    def get_shader_source(self, event_id, stage):
        """Get original shader source text when the capture preserves it."""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"shader_source": None, "error": None}

        def callback(controller):
            shader_ctx = self._resolve_shader_context(controller, event_id, stage)
            if shader_ctx["error"]:
                result["error"] = shader_ctx["error"]
                return

            reflection = shader_ctx["reflection"]
            shader_source = {
                "resource_id": shader_ctx["resource_id"],
                "entry_point": shader_ctx["entry_point"],
                "stage": shader_ctx["stage_name"],
                "encoding": "Unknown",
                "source_available": False,
            }

            if not reflection:
                shader_source["reason"] = "Shader reflection/source bytes unavailable"
                result["shader_source"] = shader_source
                return

            encoding_name = self._get_shader_encoding_name(reflection.encoding)
            shader_source["encoding"] = encoding_name

            raw_bytes = reflection.rawBytes
            shader_source["byte_length"] = len(raw_bytes) if raw_bytes is not None else 0

            if not raw_bytes:
                shader_source["reason"] = "Shader source payload is empty"
                result["shader_source"] = shader_source
                return

            if encoding_name in self._TEXT_SHADER_ENCODINGS:
                try:
                    shader_source["source_text"] = raw_bytes.decode("utf-8-sig")
                    shader_source["source_available"] = True
                except UnicodeDecodeError as exc:
                    shader_source["reason"] = (
                        "Failed to decode %s shader source as UTF-8: %s"
                        % (encoding_name, exc)
                    )
                result["shader_source"] = shader_source
                return

            shader_source["reason"] = (
                "Original source text is not available for %s shaders"
                % encoding_name
            )
            result["shader_source"] = shader_source

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["shader_source"]

    def get_pipeline_state(self, event_id):
        """Get full pipeline state at an event"""
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

        result = {"pipeline": None, "error": None}

        def callback(controller):
            controller.SetFrameEvent(event_id, True)

            pipe = controller.GetPipelineState()
            api = controller.GetAPIProperties().pipelineType

            pipeline_info = {
                "event_id": event_id,
                "api": str(api),
            }

            # Shader stages with detailed bindings
            stages = {}
            stage_list = Helpers.get_all_shader_stages()
            for stage in stage_list:
                shader = pipe.GetShader(stage)
                if shader != rd.ResourceId.Null():
                    stage_info = {
                        "resource_id": Parsers.canonical_resource_id(shader),
                        "entry_point": pipe.GetShaderEntryPoint(stage),
                        "stage": Parsers.stage_name(stage),
                    }

                    reflection = pipe.GetShaderReflection(stage)

                    stage_info["resources"] = self._get_stage_resources(
                        controller, pipe, stage, reflection
                    )
                    stage_info["uavs"] = self._get_stage_uavs(
                        controller, pipe, stage, reflection
                    )
                    stage_info["samplers"] = self._get_stage_samplers(
                        pipe, stage, reflection
                    )
                    stage_info["constant_buffers"] = self._get_stage_cbuffers(
                        controller, pipe, stage, reflection
                    )

                    stages[Parsers.stage_name(stage)] = stage_info

            pipeline_info["shaders"] = stages

            # Viewport and scissor — GetViewport(index) returns one Viewport at a time
            try:
                viewports = []
                for idx in range(8):  # D3D11 supports up to 8 viewports
                    v = pipe.GetViewport(idx)
                    if not v.enabled:
                        break
                    viewports.append({
                        "x": v.x,
                        "y": v.y,
                        "width": v.width,
                        "height": v.height,
                        "min_depth": v.minDepth,
                        "max_depth": v.maxDepth,
                    })
                if viewports:
                    pipeline_info["viewports"] = viewports
            except Exception:
                pass

            # Render targets — GetOutputTargets() returns List[Descriptor], resource via .resource
            try:
                rts = []
                for i, rt in enumerate(pipe.GetOutputTargets()):
                    if rt.resource != rd.ResourceId.Null():
                        rts.append({"index": i, "resource_id": Parsers.canonical_resource_id(rt.resource)})
                pipeline_info["render_targets"] = rts
            except Exception:
                pass

            try:
                depth = pipe.GetDepthTarget()
                if depth.resource != rd.ResourceId.Null():
                    pipeline_info["depth_target"] = Parsers.canonical_resource_id(depth.resource)
            except Exception:
                pass

            # Input assembly — GetPrimitiveTopology() returns Topology directly
            try:
                pipeline_info["input_assembly"] = {
                    "topology": str(pipe.GetPrimitiveTopology())
                }
            except Exception:
                pass

            texture_summary = self._collect_event_textures(controller, pipe)
            pipeline_info.update(texture_summary)

            result["pipeline"] = pipeline_info

        self._invoke(callback)

        if result["error"]:
            raise ValueError(result["error"])
        return result["pipeline"]

    def _get_stage_resources(self, controller, pipe, stage, reflection):
        """Get shader resource views (SRVs) for a stage"""
        resources = []
        try:
            srvs = pipe.GetReadOnlyResources(stage, False)

            name_map = {}
            if reflection:
                for res in reflection.readOnlyResources:
                    name_map[res.fixedBindNumber] = res.name

            for srv in srvs:
                if srv.descriptor.resource == rd.ResourceId.Null():
                    continue

                slot = srv.access.index
                res_info = {
                    "slot": slot,
                    "name": name_map.get(slot, ""),
                    "resource_id": Parsers.canonical_resource_id(srv.descriptor.resource),
                }

                res_info.update(
                    self._get_resource_details(controller, srv.descriptor.resource)
                )

                res_info["first_mip"] = srv.descriptor.firstMip
                res_info["num_mips"] = srv.descriptor.numMips
                res_info["first_slice"] = srv.descriptor.firstSlice
                res_info["num_slices"] = srv.descriptor.numSlices

                resources.append(res_info)
        except Exception as e:
            resources.append({"error": str(e)})

        return resources

    def _get_stage_uavs(self, controller, pipe, stage, reflection):
        """Get unordered access views (UAVs) for a stage"""
        uavs = []
        try:
            uav_list = pipe.GetReadWriteResources(stage, False)

            name_map = {}
            if reflection:
                for res in reflection.readWriteResources:
                    name_map[res.fixedBindNumber] = res.name

            for uav in uav_list:
                if uav.descriptor.resource == rd.ResourceId.Null():
                    continue

                slot = uav.access.index
                uav_info = {
                    "slot": slot,
                    "name": name_map.get(slot, ""),
                    "resource_id": Parsers.canonical_resource_id(uav.descriptor.resource),
                }

                uav_info.update(
                    self._get_resource_details(controller, uav.descriptor.resource)
                )

                uav_info["first_element"] = uav.descriptor.firstMip
                uav_info["num_elements"] = uav.descriptor.numMips

                uavs.append(uav_info)
        except Exception as e:
            uavs.append({"error": str(e)})

        return uavs

    def _get_stage_samplers(self, pipe, stage, reflection):
        """Get samplers for a stage"""
        samplers = []
        try:
            sampler_list = pipe.GetSamplers(stage, False)

            name_map = {}
            if reflection:
                for samp in reflection.samplers:
                    name_map[samp.fixedBindNumber] = samp.name

            for samp in sampler_list:
                slot = samp.access.index
                samp_info = {
                    "slot": slot,
                    "name": name_map.get(slot, ""),
                }

                desc = samp.sampler
                try:
                    samp_info["address_u"] = str(desc.addressU)
                    samp_info["address_v"] = str(desc.addressV)
                    samp_info["address_w"] = str(desc.addressW)
                except AttributeError:
                    pass

                try:
                    tf = desc.filter
                    samp_info["filter"] = {
                        "minify": str(tf.minify),
                        "magnify": str(tf.magnify),
                        "mip": str(tf.mip),
                        "function": str(tf.filter),
                    }
                except AttributeError:
                    pass

                try:
                    samp_info["max_anisotropy"] = desc.maxAnisotropy
                except AttributeError:
                    pass

                try:
                    samp_info["min_lod"] = desc.minLOD
                    samp_info["max_lod"] = desc.maxLOD
                    samp_info["mip_lod_bias"] = desc.mipBias
                except AttributeError:
                    pass

                try:
                    fv = desc.borderColorValue.floatValue
                    samp_info["border_color"] = [fv[0], fv[1], fv[2], fv[3]]
                except (AttributeError, TypeError):
                    pass

                try:
                    samp_info["compare_function"] = str(desc.compareFunction)
                except AttributeError:
                    pass

                samplers.append(samp_info)
        except Exception as e:
            samplers.append({"error": str(e)})

        return samplers

    def _get_stage_cbuffers(self, controller, pipe, stage, reflection):
        """Get constant buffers for a stage from shader reflection"""
        cbuffers = []
        try:
            if not reflection:
                return cbuffers

            for cb in reflection.constantBlocks:
                slot = cb.fixedBindNumber
                cb_info = {
                    "slot": slot,
                    "name": cb.name,
                    "byte_size": cb.byteSize,
                    "variable_count": len(cb.variables) if cb.variables else 0,
                    "variables": [],
                }
                if cb.variables:
                    for var in cb.variables:
                        cb_info["variables"].append({
                            "name": var.name,
                            "byte_offset": var.byteOffset,
                            "type": str(var.type.name) if var.type else "",
                        })
                cbuffers.append(cb_info)

        except Exception as e:
            cbuffers.append({"error": str(e)})

        return cbuffers

    def _collect_event_textures(self, controller, pipe):
        """Collect concise input/output texture summaries for an event."""
        tex_ids = {tex.resourceId for tex in controller.GetTextures()}

        input_textures = []
        seen_inputs = set()
        for stage in Helpers.get_all_shader_stages():
            try:
                srvs = pipe.GetReadOnlyResources(stage, False)
            except Exception:
                continue
            for srv in srvs:
                rid = srv.descriptor.resource
                if rid == rd.ResourceId.Null() or rid not in tex_ids or rid in seen_inputs:
                    continue
                seen_inputs.add(rid)
                input_textures.append({
                    "resource_id": Parsers.canonical_resource_id(rid),
                    "name": self._get_resource_name(rid),
                    "stage": Parsers.stage_name(stage),
                    "slot": srv.access.index,
                })

        output_textures = []
        try:
            for i, rt in enumerate(pipe.GetOutputTargets()):
                if rt.resource == rd.ResourceId.Null():
                    continue
                output_textures.append({
                    "resource_id": Parsers.canonical_resource_id(rt.resource),
                    "name": self._get_resource_name(rt.resource),
                    "type": "render_target",
                    "index": i,
                })
        except Exception:
            pass

        try:
            depth = pipe.GetDepthTarget()
            if depth.resource != rd.ResourceId.Null():
                output_textures.append({
                    "resource_id": Parsers.canonical_resource_id(depth.resource),
                    "name": self._get_resource_name(depth.resource),
                    "type": "depth_target",
                })
        except Exception:
            pass

        return {
            "input_textures": input_textures,
            "output_textures": output_textures,
            "input_count": len(input_textures),
            "output_count": len(output_textures),
        }

    def _get_resource_name(self, resource_id):
        """Get resource name with safe fallback."""
        try:
            return self.ctx.GetResourceName(resource_id) or ""
        except Exception:
            return ""

    def _resolve_shader_context(self, controller, event_id, stage):
        """Resolve the currently bound shader and reflection for one event/stage."""
        controller.SetFrameEvent(event_id, True)

        pipe = controller.GetPipelineState()
        stage_enum = Parsers.parse_stage(stage)
        shader = pipe.GetShader(stage_enum)

        if shader == rd.ResourceId.Null():
            return {
                "error": "RESOURCE_NOT_FOUND: no %s shader bound" % stage,
            }

        return {
            "error": None,
            "pipe": pipe,
            "stage_enum": stage_enum,
            "stage_name": Parsers.parse_stage_name(stage),
            "shader": shader,
            "resource_id": Parsers.canonical_resource_id(shader),
            "entry_point": pipe.GetShaderEntryPoint(stage_enum),
            "reflection": pipe.GetShaderReflection(stage_enum),
        }

    @staticmethod
    def _get_shader_encoding_name(encoding):
        """Convert RenderDoc shader encoding enums to stable response strings."""
        if encoding is None:
            return "Unknown"
        return getattr(encoding, "name", str(encoding))

    def _get_resource_details(self, controller, resource_id):
        """Get details about a resource (texture or buffer)"""
        details = {}

        try:
            resource_name = self.ctx.GetResourceName(resource_id)
            if resource_name:
                details["name"] = resource_name
        except Exception:
            pass

        for tex in controller.GetTextures():
            if tex.resourceId == resource_id:
                details["type"] = "texture"
                details["width"] = tex.width
                details["height"] = tex.height
                details["depth"] = tex.depth
                details["array_size"] = tex.arraysize
                details["mip_levels"] = tex.mips
                details["format"] = str(tex.format.Name())
                details["dimension"] = str(tex.type)
                details["msaa_samples"] = tex.msSamp
                return details

        for buf in controller.GetBuffers():
            if buf.resourceId == resource_id:
                details["type"] = "buffer"
                details["length"] = buf.length
                return details

        return details

    def _get_cbuffer_info(self, controller, pipe, reflection, stage):
        """Get constant buffer information and values"""
        cbuffers = []

        for i, cb in enumerate(reflection.constantBlocks):
            cb_info = {
                "name": cb.name,
                "slot": i,
                "size": cb.byteSize,
                "variables": [],
            }

            try:
                pipeline_obj = (
                    pipe.GetComputePipelineObject()
                    if stage == rd.ShaderStage.Compute
                    else pipe.GetGraphicsPipelineObject()
                )
                bind = pipe.GetConstantBlock(stage, i, 0)

                # 检测 $Globals (OpenGL 内联 uniform block)
                is_globals = (cb.name == "$Globals")

                if is_globals:
                    # $Globals 没有底层 buffer 资源，使用空 ResourceId
                    variables = controller.GetCBufferVariableContents(
                        pipeline_obj,
                        reflection.resourceId,
                        stage,
                        reflection.entryPoint,
                        i,
                        rd.ResourceId.Null(),  # 空 ResourceId
                        0,
                        0
                    )
                    cb_info["variables"] = Serializers.serialize_variables(variables)
                elif bind.descriptor.resource != rd.ResourceId.Null():
                    # 普通 buffer-backed constant block
                    variables = controller.GetCBufferVariableContents(
                        pipeline_obj,
                        reflection.resourceId,
                        stage,
                        reflection.entryPoint,
                        i,
                        bind.descriptor.resource,
                        bind.descriptor.byteOffset,
                        bind.descriptor.byteSize,
                    )
                    cb_info["variables"] = Serializers.serialize_variables(variables)
            except Exception as e:
                cb_info["error"] = str(e)

            cbuffers.append(cb_info)

        return cbuffers

    def _get_resource_bindings(self, reflection):
        """Get shader resource bindings"""
        resources = []

        try:
            for res in reflection.readOnlyResources:
                resources.append(
                    {
                        "name": res.name,
                        "type": str(res.resType),
                        "binding": res.fixedBindNumber,
                        "access": "ReadOnly",
                    }
                )
        except Exception:
            pass

        try:
            for res in reflection.readWriteResources:
                resources.append(
                    {
                        "name": res.name,
                        "type": str(res.resType),
                        "binding": res.fixedBindNumber,
                        "access": "ReadWrite",
                    }
                )
        except Exception:
            pass

        return resources
