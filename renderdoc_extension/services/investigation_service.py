"""File-backed shader evidence and native numeric investigations."""
import hashlib
import json
import math
import os
import struct

import renderdoc as rd

from ..utils import Parsers
from .job_service import atomic_json
from .native_serialization import plain
from .replay_query import at_event, require_action
from .resource_catalog import enum_name
from .texture_values import decoder, validate_region, MAX_SUBRESOURCE_BYTES


def _digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _reflect(value, fields):
    return {k: plain(getattr(value, k)) for k in fields if hasattr(value, k)}


def _constant(value):
    typ = value.type
    result = _reflect(value, ("name", "byteOffset", "bitFieldOffset", "bitFieldSize", "defaultValue"))
    result["type"] = _reflect(typ, ("name", "rows", "columns", "elements", "arrayByteStride",
                                    "matrixByteStride", "baseType", "flags", "pointerTypeID"))
    result["type"]["members"] = [_constant(v) for v in typ.members]
    return result


class InvestigationService:
    def __init__(self, ctx, session, jobs):
        self.ctx, self.session, self.jobs = ctx, session, jobs

    def _directory(self, output_dir, key):
        if not isinstance(output_dir, str) or not os.path.isabs(output_dir):
            raise ValueError("INVALID_OUTPUT_PATH: output_dir must be absolute")
        path = os.path.join(output_dir, key)
        os.makedirs(path, exist_ok=True)
        return path

    def export_shader_bundle(self, action_event_id, stage, output_dir, job_id=None):
        require_action(self.ctx, action_event_id)
        stage_enum = Parsers.parse_stage(stage)
        def steps(key):
            directory = self._directory(output_dir, key)
            def export(controller):
                def read(c, event):
                    pipe = c.GetPipelineState()
                    ref = pipe.GetShaderReflection(stage_enum)
                    if ref is None:
                        raise ValueError("RESOURCE_NOT_FOUND: shader reflection unavailable")
                    encoding = enum_name(ref.encoding)
                    suffix = {"SPIRV": ".spv", "GLSL": ".glsl", "HLSL": ".hlsl",
                              "SPIRVAsm": ".spvasm", "Slang": ".slang"}.get(encoding, ".bin")
                    raw_path = os.path.join(directory, "original" + suffix)
                    with open(raw_path, "wb") as handle:
                        handle.write(bytes(ref.rawBytes))
                    files = [raw_path]
                    pipeline = pipe.GetComputePipelineObject() if enum_name(stage_enum) == "Compute" else pipe.GetGraphicsPipelineObject()
                    disassembly = {}
                    for index, target in enumerate(c.GetDisassemblyTargets(True)):
                        path = os.path.join(directory, "disassembly_%d.txt" % index)
                        try:
                            with open(path, "w", encoding="utf-8") as handle:
                                handle.write(c.DisassembleShader(pipeline, ref, target))
                            files.append(path)
                            disassembly[target] = path
                        except Exception as exc:
                            disassembly[target] = {"unavailable": str(exc)}
                    sources = []
                    for index, source in enumerate(getattr(ref.debugInfo, "files", [])):
                        path = os.path.join(directory, "source_%d_%s" % (index, os.path.basename(source.filename)))
                        with open(path, "w", encoding="utf-8") as handle:
                            handle.write(source.contents)
                        files.append(path)
                        sources.append({"original_filename": source.filename, "path": path})
                    signature_fields = ("varName", "semanticName", "semanticIndex", "regIndex", "systemValue",
                                        "varType", "compCount", "regChannelMask", "channelUsedMask", "stream")
                    reflection = {"input_signature": [_reflect(s, signature_fields) for s in ref.inputSignature],
                                  "output_signature": [_reflect(s, signature_fields) for s in ref.outputSignature]}
                    for name in ("readOnlyResources", "readWriteResources", "samplers"):
                        reflection[name] = [_reflect(r, ("name", "fixedBindNumber", "fixedBindSetOrSpace",
                                                        "bindArraySize", "isTexture", "textureType", "isReadOnly"))
                                            for r in getattr(ref, name)]
                    reflection["constant_blocks"] = [dict(
                        _reflect(b, ("name", "byteSize", "bufferBacked", "fixedBindNumber", "fixedBindSetOrSpace")),
                        variables=[_constant(v) for v in b.variables]) for b in ref.constantBlocks]
                    path = os.path.join(directory, "reflection.json")
                    atomic_json(path, reflection)
                    files.append(path)
                    result = dict(provenance=self.session.describe(), action_event_id=event, event_phase="after",
                                  shader_id="ResourceId::%d" % int(ref.resourceId), stage=Parsers.parse_stage_name(stage),
                                  entry_point=ref.entryPoint, encoding=encoding, source="capture_shader",
                                  original=raw_path, embedded_sources=sources, disassembly=disassembly,
                                  files=[{"path": p, "sha256": _digest(p)} for p in files])
                    manifest = os.path.join(directory, "manifest.json")
                    atomic_json(manifest, result)
                    return {"result": dict(result, manifest_path=manifest)}
                return at_event(self.ctx, lambda fn: fn(controller), action_event_id, read)
            yield ("replay", "export_shader", export)
        return self.jobs.submit("export_shader_bundle", dict(action_event_id=action_event_id, stage=stage,
                                                             output_dir=output_dir), steps, job_id)

    def compare_texture_events(self, resource_id, action_event_id_a, action_event_id_b,
                               region, output_dir, mip=0, slice_index=0, sample=0,
                               depth_slice=0, value_domain="storage", job_id=None):
        for eid in (action_event_id_a, action_event_id_b):
            require_action(self.ctx, eid)
        if value_domain not in ("storage", "linear"):
            raise ValueError("INVALID_REQUEST: value_domain must be storage or linear")
        if any(type(v) is not int or v < 0 for v in (mip, slice_index, sample, depth_slice)):
            raise ValueError("INVALID_REQUEST: invalid subresource")
        params = dict(resource_id=resource_id, action_event_id_a=action_event_id_a,
                      action_event_id_b=action_event_id_b, region=region, output_dir=output_dir,
                      mip=mip, slice_index=slice_index, sample=sample, depth_slice=depth_slice, value_domain=value_domain)
        def steps(key):
            directory = self._directory(output_dir, key)
            values = []
            metadata = {}
            for eid in (action_event_id_a, action_event_id_b):
                def fetch(controller, eid=eid):
                    def read(c, event):
                        api = enum_name(c.GetAPIProperties().pipelineType)
                        if api not in ("Vulkan", "D3D11", "D3D12"):
                            raise ValueError("UNSUPPORTED_FORMAT: raw coordinate layout is unverified on %s" % api)
                        rid = Parsers.extract_numeric_id(resource_id)
                        td = next((t for t in c.GetTextures() if int(t.resourceId) == rid), None)
                        if td is None:
                            raise ValueError("TEXTURE_NOT_FOUND: %s" % resource_id)
                        if mip >= td.mips or slice_index >= td.arraysize or sample >= max(1, td.msSamp):
                            raise ValueError("INVALID_REQUEST: subresource outside texture")
                        width, height, depth = max(1, td.width >> mip), max(1, td.height >> mip), max(1, td.depth >> mip)
                        if depth_slice >= depth:
                            raise ValueError("INVALID_DEPTH_SLICE: outside mip")
                        size, count, read_pixel = decoder(td.format)
                        expected = width * height * depth * size
                        if expected > MAX_SUBRESOURCE_BYTES:
                            raise ValueError("RESOURCE_LIMIT: subresource exceeds 64 MiB")
                        x, y, w, h = validate_region(region, width, height)
                        sub = rd.Subresource()
                        sub.mip, sub.slice, sub.sample = mip, slice_index, sample
                        data = bytes(c.GetTextureData(td.resourceId, sub))
                        if len(data) != expected:
                            raise ValueError("RESOURCE_QUERY_FAILED: unexpected raw layout/short read %d != %d" % (len(data), expected))
                        rows = [read_pixel(data, ((depth_slice * height + yy) * width + xx) * size, value_domain)
                                for yy in range(y, y + h) for xx in range(x, x + w)]
                        metadata.update(format=td.format.Name(), channels=count, coordinate_origin="top_left",
                                        api=api, mip=mip, slice_index=slice_index, sample=sample,
                                        depth_slice=depth_slice, value_domain=value_domain, region=region)
                        values.append(rows)
                    at_event(self.ctx, lambda fn: fn(controller), eid, read)
                yield ("replay", "read_texture_event_%d" % eid, fetch)
            def compare(_):
                channels = metadata["channels"]
                absolute, signed, maximum, finite = [0.0] * channels, [0.0] * channels, [0.0] * channels, [0] * channels
                nonfinite = [{"nan_a": 0, "nan_b": 0, "inf_a": 0, "inf_b": 0, "nonfinite_delta": 0} for _ in range(channels)]
                changed = 0
                path = os.path.join(directory, "difference.f64le")
                with open(path, "wb") as handle:
                    for a, b in zip(*values):
                        delta = []
                        pixel_changed = False
                        for i, (av, bv) in enumerate(zip(a, b)):
                            d = bv - av
                            delta.append(d)
                            for label, v in (("a", av), ("b", bv)):
                                if math.isnan(v):
                                    nonfinite[i]["nan_" + label] += 1
                                if math.isinf(v):
                                    nonfinite[i]["inf_" + label] += 1
                            if math.isfinite(d):
                                n = finite[i] + 1
                                absolute[i] += (abs(d) - absolute[i]) / n
                                signed[i] = signed[i] * (1.0 - 1.0 / n) + d / n
                                maximum[i] = max(maximum[i], abs(d))
                                finite[i] += 1
                            else:
                                nonfinite[i]["nonfinite_delta"] += 1
                            pixel_changed = pixel_changed or av != bv
                        changed += int(pixel_changed)
                        handle.write(struct.pack("<%dd" % channels, *delta))
                result = dict(metadata, provenance=self.session.describe(), source="observed_texture_difference",
                              action_event_id_a=action_event_id_a, action_event_id_b=action_event_id_b,
                              event_phase="after", resource_id=resource_id, difference_direction="b_minus_a",
                              pixel_count=len(values[0]), changed_pixels=changed, finite_samples=finite,
                              nonfinite=nonfinite,
                              max_absolute_error=[a if n else None for a,n in zip(maximum,finite)],
                              comparison_rule="component_inequality_nan_is_unequal",
                              mean_absolute_error=[a if n else None for a, n in zip(absolute, finite)],
                              mean_signed_difference=[a if n else None for a, n in zip(signed, finite)],
                              difference_file=path, difference_encoding="little_endian_float64_pixel_interleaved",
                              sha256=_digest(path))
                manifest = os.path.join(directory, "manifest.json")
                atomic_json(manifest, result)
                values[:] = []
                return {"result": dict(result, manifest_path=manifest)}
            yield ("worker", "calculate_difference", compare)
        return self.jobs.submit("compare_texture_events", params, steps, job_id)

    def get_pixel_history(self, resource_id, x, y, action_event_id, output_dir,
                          mip=0, slice_index=0, sample=0, job_id=None):
        require_action(self.ctx, action_event_id)
        if any(type(v) is not int or v < 0 for v in (x, y, mip, slice_index, sample)):
            raise ValueError("INVALID_REQUEST: invalid pixel/subresource")
        params = dict(resource_id=resource_id, x=x, y=y, action_event_id=action_event_id,
                      output_dir=output_dir, mip=mip, slice_index=slice_index, sample=sample)
        def steps(key):
            directory = self._directory(output_dir, key)
            def fetch(controller):
                def read(c, event):
                    if not c.GetAPIProperties().pixelHistory:
                        return {"result": {"available": False, "reason": "pixel_history_not_supported"}}
                    rid = Parsers.extract_numeric_id(resource_id)
                    td = next((t for t in c.GetTextures() if int(t.resourceId) == rid), None)
                    if td is None:
                        raise ValueError("TEXTURE_NOT_FOUND: %s" % resource_id)
                    if mip >= td.mips or x >= max(1, td.width >> mip) or y >= max(1, td.height >> mip):
                        raise ValueError("INVALID_REQUEST: pixel outside texture mip")
                    if slice_index >= (max(1, td.depth >> mip) if td.depth > 1 else td.arraysize) or sample >= max(1, td.msSamp):
                        raise ValueError("INVALID_REQUEST: subresource outside texture")
                    sub = rd.Subresource()
                    sub.mip, sub.slice, sub.sample = mip, slice_index, sample
                    history = c.PixelHistory(td.resourceId, x, y, sub, rd.CompType.Typeless)
                    rows = []
                    def modification(value):
                        color = value.col
                        field = "uintValue" if td.format.compType == rd.CompType.UInt else (
                            "intValue" if td.format.compType == rd.CompType.SInt else "floatValue")
                        return {"color": plain(list(getattr(color, field))),
                                "depth": plain(value.depth), "stencil": value.stencil}
                    for index, item in enumerate(history):
                        row = _reflect(item, ("eventId", "directShaderWrite", "unboundPS", "fragIndex", "primitiveID",
                                              "sampleMasked", "backfaceCulled", "depthClipped", "depthBoundsFailed",
                                              "viewClipped", "scissorClipped", "shaderDiscarded", "depthTestFailed",
                                              "stencilTestFailed", "predicationSkipped"))
                        passed = bool(item.Passed()) if hasattr(item, "Passed") else None
                        row.update(item_key=str(index), preMod=modification(item.preMod),
                                   shaderOut=modification(item.shaderOut), postMod=modification(item.postMod),
                                   preMod_valid=item.fragIndex == 0,
                                   passed=passed,
                                   shaderOut_valid=(False if item.directShaderWrite or item.unboundPS else
                                                    True if passed is True else None),
                                   shaderOut_validity="not_guaranteed_for_failed_or_discarded_fragments")
                        rows.append(row)
                    result = dict(provenance=self.session.describe(), available=True, parameters=params,
                                  coordinate_origin="top_left", source="native_pixel_history", events=rows,
                                  validity_note="Native API limitations apply; failed/discarded fragments may lack valid values.")
                    path = os.path.join(directory, "manifest.json")
                    atomic_json(path, result)
                    self.jobs.update(key, items=rows)
                    return {"result": {"available": True, "manifest_path": path, "event_count": len(rows)}}
                return at_event(self.ctx, lambda fn: fn(controller), action_event_id, read)
            yield ("replay", "pixel_history", fetch)
        return self.jobs.submit("get_pixel_history", params, steps, job_id)
