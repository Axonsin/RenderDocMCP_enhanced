"""Session-scoped shader editing. All public methods run on the UI thread.

TODO: Add HLSL / DXBC / DXIL editing and compiler selection after DirectX validation.
"""

import os
import shutil
import shlex
import tempfile
from types import SimpleNamespace
import uuid

import qrenderdoc as qrd
import renderdoc as rd

from ..utils import Parsers


class ShaderEditService(qrd.CaptureViewer):
    """Own replacement resources, but never the capture's original shaders."""

    MODES = ("auto", "original", "glsl", "spirv_asm")
    SCOPE = "All draws referencing the original shader resource are affected."

    def __init__(self, ctx, invoke_fn, session=None):
        super(ShaderEditService, self).__init__()
        self.ctx = ctx
        self.session = session
        self._invoke = invoke_fn
        self._generation = uuid.uuid4().hex
        self._edits = {}
        self._resources = {}
        self._busy = False
        ctx.AddCaptureViewer(self)

    def OnCaptureLoaded(self):
        self._reset()

    def OnCaptureClosed(self):
        # ReplayController shutdown frees its target resources. Do not call a closing replay.
        self._reset()

    def OnSelectedEventChanged(self, event_id):
        pass

    def OnEventChanged(self, event_id):
        pass

    def _reset(self):
        self._generation = uuid.uuid4().hex
        self._edits.clear()
        self._resources.clear()

    def _require_capture(self):
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")

    def _record(self, edit_id):
        self._require_capture()
        record = self._edits.get(edit_id)
        if record is None or record["generation"] != self._generation:
            raise ValueError("INVALID_EDIT_ID: shader edit does not belong to this capture session")
        return record

    def _replay(self, callback):
        # SWIG callbacks cannot reliably propagate exceptions across BlockInvoke.
        result = {}

        def invoke(controller):
            try:
                result["value"] = callback(controller)
            except Exception as exc:
                # Never retain a traceback holding replay-owned SWIG objects on the UI thread.
                result["error"] = (isinstance(exc, ValueError), str(exc))

        self._invoke(invoke)
        if "error" in result:
            invalid, message = result["error"]
            raise (ValueError if invalid else RuntimeError)(message)
        return result.get("value")

    @staticmethod
    def _encoding_name(encoding):
        return getattr(encoding, "name", str(encoding))

    @staticmethod
    def _flags(values):
        flags = rd.ShaderCompileFlags()
        for name, value in values:
            flag = rd.ShaderCompileFlag()
            flag.name, flag.value = name, value
            flags.flags.append(flag)
        return flags

    @staticmethod
    def _tool_exists(tool):
        executable = tool.executable
        return bool(executable and (os.path.isfile(executable) or shutil.which(executable)))

    def _assert_owner(self, record):
        current = self.ctx.GetResourceReplacement(record["original"])
        expected = record["replacement"] or rd.ResourceId.Null()
        if current != expected:
            raise ValueError("SHADER_EDIT_CONFLICT: shader replacement changed outside this edit; "
                             "restore it in its owning editor before continuing")

    def _restore_event(self, generation):
        if generation == self._generation and self.ctx.IsCaptureLoaded():
            self.ctx.SetEventID([], self.ctx.CurSelectedEvent(), self.ctx.CurEvent(), True)

    def _snapshot(self, event_id, stage):
        stage_enum = Parsers.parse_stage(stage)
        if not isinstance(event_id, int) or isinstance(event_id, bool) or event_id < 1:
            raise ValueError("INVALID_EVENT_ID: event_id must be a positive integer")

        def read(controller):
            props = controller.GetAPIProperties()
            if not getattr(props, "shadersMutable", True):
                raise ValueError("UNSUPPORTED_CAPTURE_FEATURE: replay device cannot replace shaders")
            controller.SetFrameEvent(event_id, True)
            pipe = controller.GetPipelineState()
            original = pipe.GetShader(stage_enum)
            if original == rd.ResourceId.Null():
                raise ValueError("RESOURCE_NOT_FOUND: no %s shader bound" % stage)
            key = Parsers.canonical_resource_id(original)
            if key in self._resources:
                cached = self._resources[key]
                if cached["reflection"].stage != stage_enum or (
                        pipe.GetShaderEntryPoint(stage_enum) or "main") != cached["reflection"].entryPoint:
                    raise ValueError("UNSUPPORTED_CAPTURE_FEATURE: editing multiple entry points "
                                     "of one shader resource is not supported")
                return cached
            reflection = pipe.GetShaderReflection(stage_enum)
            if reflection is None:
                raise ValueError("UNSUPPORTED_CAPTURE_FEATURE: shader reflection is unavailable")
            allowed = (rd.ShaderEncoding.GLSL, rd.ShaderEncoding.SPIRV,
                       rd.ShaderEncoding.OpenGLSPIRV)
            if reflection.encoding not in allowed:
                raise ValueError("UNSUPPORTED_SHADER_ENCODING: %s; HLSL/DXBC/DXIL editing is TODO"
                                 % self._encoding_name(reflection.encoding))
            if reflection.encoding != rd.ShaderEncoding.GLSL and len(controller.GetShaderEntryPoints(original)) > 1:
                raise ValueError("UNSUPPORTED_CAPTURE_FEATURE: shader module has multiple entry points")
            # Detach data before returning to the UI or running a tool's nested event loop.
            # ShaderReflection has no public Python constructor. Store only owned plain data.
            snapshot = SimpleNamespace(encoding=reflection.encoding, stage=stage_enum,
                                       entryPoint=pipe.GetShaderEntryPoint(stage_enum) or "main",
                                       rawBytes=bytes(reflection.rawBytes))
            flags = [(f.name, f.value) for f in reflection.debugInfo.compileFlags.flags]
            return {"original": original, "resource_id": key, "reflection": snapshot,
                    "original_flags": flags, "accepted": list(controller.GetTargetShaderEncodings()),
                    "api": str(props.pipelineType), "remote_replay": bool(props.remoteReplay)}

        snapshot = self._replay(read)
        if snapshot["resource_id"] not in self._resources and self.ctx.IsResourceReplaced(snapshot["original"]):
            raise ValueError("SHADER_EDIT_CONFLICT: shader is already replaced outside MCP")
        return snapshot

    def _path(self, snapshot, mode):
        native = snapshot["reflection"].encoding
        accepted = snapshot["accepted"]
        if native == rd.ShaderEncoding.GLSL:
            if mode not in ("auto", "original", "glsl"):
                raise ValueError("UNSUPPORTED_SHADER_ENCODING: GLSL has no SPIR-V assembly")
            source_encoding = rd.ShaderEncoding.GLSL
            resolved = "original"
        else:
            if mode == "original":
                raise ValueError("UNSUPPORTED_SHADER_ENCODING: binary SPIR-V is not original text")
            resolved = "glsl" if mode in ("auto", "glsl") else "spirv_asm"
            source_encoding = (rd.ShaderEncoding.GLSL if resolved == "glsl" else
                               rd.ShaderEncoding.OpenGLSPIRVAsm
                               if native == rd.ShaderEncoding.OpenGLSPIRV else rd.ShaderEncoding.SPIRVAsm)
        tools = list(self.ctx.Config().ShaderProcessors)
        decompiler = None
        if native != rd.ShaderEncoding.GLSL:
            decompiler = next((t for t in tools if t.input == native and t.output == source_encoding
                               and self._tool_exists(t)), None)
            if decompiler is None:
                raise ValueError("SHADER_TOOL_MISSING: no available %s -> %s decompiler in ShaderProcessors"
                                 % (self._encoding_name(native), self._encoding_name(source_encoding)))
        # Keep Vulkan and OpenGL SPIR-V distinct, even when both encodings are accepted.
        output_encoding = native
        compiler = None
        if source_encoding != native or source_encoding not in accepted:
            targets = (rd.ShaderEncoding.OpenGLSPIRV,) if native == rd.ShaderEncoding.GLSL else (native,)
            compiler = next((t for t in tools if t.input == source_encoding and t.output in targets
                             and t.output in accepted and self._tool_exists(t)), None)
            if compiler is None:
                raise ValueError("SHADER_TOOL_MISSING: no available %s -> %s compiler in ShaderProcessors"
                                 % (self._encoding_name(source_encoding), self._encoding_name(native)))
            output_encoding = compiler.output
        return resolved, source_encoding, output_encoding, decompiler, compiler

    def _decompile(self, tool, snapshot):
        """Run a configured decompiler without borrowing a ShaderReflection pointer.

        Qt's QProcess is available in RenderDoc's embedded Python even on builds
        where subprocess is unavailable. Keep input/output unique to this call.
        """
        from PySide2.QtCore import QProcess

        with tempfile.TemporaryDirectory(prefix="renderdoc_mcp_shader_") as directory:
            input_path = os.path.join(directory, "input.spv")
            output_path = os.path.join(directory, "output.txt")
            log_path = os.path.join(directory, "stderr.txt")
            stdout_path = os.path.join(directory, "stdout.txt")
            with open(input_path, "wb") as handle:
                handle.write(snapshot.rawBytes)
            args = shlex.split(tool.DefaultArguments())
            cross_tools = (rd.KnownShaderTool.SPIRV_Cross, rd.KnownShaderTool.SPIRV_Cross_OpenGL)
            dis_tools = (rd.KnownShaderTool.spirv_dis, rd.KnownShaderTool.spirv_dis_OpenGL)
            if tool.tool in cross_tools:
                args.extend(["--output", "{output_file}", "{input_file}"])
            elif tool.tool in dis_tools:
                args.extend(["-o", "{output_file}", "{input_file}"])
            elif "{input_file}" not in args or "{output_file}" not in args:
                raise ValueError("SHADER_TOOL_MISSING: custom decompiler must configure input/output placeholders")
            replacements = {"{input_file}": input_path, "{output_file}": output_path,
                            "{entry_point}": snapshot.entryPoint,
                            "{glsl_stage4}": {"vertex": "vert", "hull": "tesc", "domain": "tese",
                                              "geometry": "geom", "pixel": "frag", "compute": "comp"}[
                                                  Parsers.stage_name(snapshot.stage)],
                            "{spirv_ver}": self._spirv_version(snapshot.rawBytes)}
            for index, arg in enumerate(args):
                for key, value in replacements.items():
                    arg = arg.replace(key, value)
                args[index] = arg
            process = QProcess()
            process.setStandardOutputFile(stdout_path)
            process.setStandardErrorFile(log_path)
            process.start(tool.executable, args)
            if not process.waitForStarted(10000):
                raise ValueError("SHADER_DECOMPILE_FAILED: " + process.errorString())
            finished = process.waitForFinished(60000)
            if not finished:
                process.kill()
                process.waitForFinished(5000)
            log = "Running %s %s\n" % (tool.executable, repr(args))
            for path in (stdout_path, log_path):
                if os.path.isfile(path):
                    with open(path, "rb") as handle:
                        log += handle.read().decode("utf-8", "replace")
            success = finished and process.exitStatus() == QProcess.NormalExit and process.exitCode() == 0
            data = b""
            if success and os.path.isfile(output_path):
                with open(output_path, "rb") as handle:
                    data = handle.read()
            log += "\nExit code: %s%s" % (process.exitCode(), " (timed out)" if not finished else "")
            return SimpleNamespace(result=data, log=log)

    def get_shader_edit_context(self, event_id, stage, mode="auto"):
        self._require_capture()
        if mode not in self.MODES:
            raise ValueError("INVALID_EDIT_MODE: expected auto, original, glsl, or spirv_asm")
        if self._busy:
            raise ValueError("SHADER_EDIT_BUSY: another shader operation is running")
        generation = self._generation
        self._busy = True
        try:
            snapshot = self._snapshot(event_id, stage)
            existing = next((e for e in self._edits.values()
                             if e["resource_id"] == snapshot["resource_id"]), None)
            if existing:
                self._assert_owner(existing)
                if mode == "auto" or mode == existing["mode"] or (
                        mode == "glsl" and existing["mode"] == "original"):
                    return self._describe(existing, True)
                if existing["replacement"]:
                    raise ValueError("SHADER_EDIT_CONFLICT: revert before changing editing representation")
            candidates = ("glsl", "spirv_asm") if (
                mode == "auto" and snapshot["reflection"].encoding != rd.ShaderEncoding.GLSL
            ) else (mode,)
            failures = []
            for candidate in candidates:
                try:
                    path = self._path(snapshot, candidate)
                    break
                except ValueError as exc:
                    if len(candidates) == 1:
                        raise
                    failures.append(str(exc))
            else:
                raise ValueError("SHADER_TOOL_MISSING: " + "; ".join(failures))
            resolved, source_encoding, output_encoding, decompiler, compiler = path
            log = ""
            if decompiler:
                output = self._decompile(decompiler, snapshot["reflection"])
                log = output.log
                if not output.result:
                    raise ValueError("SHADER_DECOMPILE_FAILED: " + log)
                source = bytes(output.result).decode("utf-8-sig")
            else:
                source = snapshot["reflection"].rawBytes.decode("utf-8-sig")
            if not source.strip():
                raise ValueError("SHADER_DECOMPILE_FAILED: shader source is empty")
            if generation != self._generation:
                raise ValueError("INVALID_EDIT_ID: capture changed while preparing shader")
            original_entry = snapshot["reflection"].entryPoint
            flags = snapshot["original_flags"]
            if decompiler:
                flags = [(k, v) for k, v in flags if k == "@spirver"]
            record = dict(snapshot)
            record.update({"edit_id": uuid.uuid4().hex, "generation": generation,
                           "event_id": event_id, "stage": Parsers.parse_stage_name(stage),
                           "stage_enum": Parsers.parse_stage(stage), "mode": resolved,
                           "source_encoding": source_encoding, "output_encoding": output_encoding,
                           "decompiler": decompiler, "compiler": compiler,
                           "entry_point": original_entry,
                           "source_entry_point": "main" if source_encoding == rd.ShaderEncoding.GLSL
                           else original_entry, "compile_flags": flags,
                           "spirv_version": next((v for k, v in flags if k == "@spirver"),
                                                 self._spirv_version(snapshot["reflection"].rawBytes)),
                           "source_text": source, "applied_source_text": None,
                           "replacement": None, "revision": 0,
                           "last_attempt_status": "prepared", "log": log})
            if existing:
                del self._edits[existing["edit_id"]]
            self._edits[record["edit_id"]] = record
            self._resources[record["resource_id"]] = snapshot
            return self._describe(record, True)
        finally:
            self._busy = False
            self._restore_event(generation)

    @staticmethod
    def _spirv_version(raw):
        if len(raw) >= 8 and raw[:4] == b"\x03\x02\x23\x07":
            return "spirv%d.%d" % (raw[6], raw[5])
        return "spirv1.0"

    def _describe(self, record, include_source=False):
        current = self.ctx.GetResourceReplacement(record["original"])
        applied = record["replacement"] is not None and current == record["replacement"]
        compiler = record["compiler"]
        result = {"edit_id": record["edit_id"], "edit_session": record["generation"],
                  "capture_session": self.session.capture_session if self.session else record["generation"],
                  "event_id": record["event_id"], "stage": record["stage"], "api": record["api"],
                  "remote_replay": record["remote_replay"],
                  "resource_id": record["resource_id"], "mode": record["mode"],
                  "original_encoding": self._encoding_name(record["reflection"].encoding),
                  "encoding": self._encoding_name(record["source_encoding"]),
                  "target_encoding": self._encoding_name(record["output_encoding"]),
                  "entry_point": record["entry_point"],
                  "source_entry_point": record["source_entry_point"],
                  "spirv_version": record["spirv_version"],
                  "compile_flags": [{"name": k, "value": v} for k, v in record["compile_flags"]],
                  "compiler": compiler.name if compiler else "Builtin",
                  "decompiler": record["decompiler"].name if record["decompiler"] else None,
                  "applied": applied,
                  "replacement_resource_id": Parsers.canonical_resource_id(record["replacement"])
                  if record["replacement"] is not None else None,
                  "conflict": current != (record["replacement"] or rd.ResourceId.Null()),
                  "revision": record["revision"], "last_attempt_status": record["last_attempt_status"],
                  "log": record["log"], "scope": self.SCOPE}
        if include_source:
            result["source_text"] = record["source_text"]
            result["applied_source_text"] = record["applied_source_text"]
        return result

    @staticmethod
    def _compiler_arguments(record):
        args = record["compiler"].DefaultArguments()
        if record["source_encoding"] in (rd.ShaderEncoding.SPIRVAsm, rd.ShaderEncoding.OpenGLSPIRVAsm):
            # glslang calls this spirv1.x; SPIRV-Tools calls the same version spv1.x.
            args += " --target-env " + record["spirv_version"].replace("spirv", "spv", 1)
        elif record["source_entry_point"] != record["entry_point"]:
            args += " --source-entrypoint main -e {entry_point}"
        return args

    def replace_shader(self, edit_id, source_text):
        record = self._record(edit_id)
        if not isinstance(source_text, str) or not source_text.strip() or "\x00" in source_text:
            raise ValueError("INVALID_SHADER_SOURCE: expected nonempty text without NUL bytes")
        if self._busy:
            raise ValueError("SHADER_EDIT_BUSY: another shader operation is running")
        self._assert_owner(record)
        self._busy = True
        generation = self._generation
        record["source_text"] = source_text
        record["last_attempt_status"] = "compiling"
        record["log"] = ""
        try:
            shader_bytes = source_text.encode("utf-8")
            compiler = record["compiler"]
            if compiler:
                if not self._tool_exists(compiler):
                    raise ValueError("SHADER_TOOL_MISSING: compiler executable is unavailable")
                args = self._compiler_arguments(record)
                output = compiler.CompileShader(self.ctx.GetMainWindow().Widget(), source_text,
                                                record["entry_point"], record["stage_enum"],
                                                record["spirv_version"], args)
                self._record(edit_id)
                record["log"] = output.log
                shader_bytes = bytes(output.result)
                if not shader_bytes:
                    record["last_attempt_status"] = "compile_failed"
                    return self._describe(record)
            self._record(edit_id)  # Tool progress dialogs can pump capture-close events.
            self._assert_owner(record)

            def build(controller):
                replacement, log = controller.BuildTargetShader(
                    record["entry_point"], record["output_encoding"], shader_bytes,
                    self._flags(record["compile_flags"]), record["stage_enum"])
                record["log"] += ("\n" if record["log"] and log else "") + log
                if replacement == rd.ResourceId.Null():
                    return None
                try:
                    controller.ReplaceResource(record["original"], replacement)
                except Exception:
                    controller.FreeTargetResource(replacement)
                    raise
                return replacement

            replacement = self._replay(build)
            if replacement is None:
                record["last_attempt_status"] = "compile_failed"
                return self._describe(record)
            previous = record["replacement"]
            try:
                # Remove the old reverse UI mapping before registering a newer replacement.
                if previous is not None:
                    self.ctx.UnregisterReplacement(record["original"])
                self.ctx.RegisterReplacement(record["original"], replacement)
            except Exception:
                # UI bookkeeping and replay replacement must commit together.
                if previous is not None:
                    self._replay(lambda c: c.ReplaceResource(record["original"], previous))
                    self.ctx.RegisterReplacement(record["original"], previous)
                else:
                    self._replay(lambda c: c.RemoveReplacement(record["original"]))
                    self.ctx.UnregisterReplacement(record["original"])
                self._replay(lambda c: c.FreeTargetResource(replacement))
                raise
            record["replacement"] = replacement
            record["applied_source_text"] = source_text
            record["revision"] += 1
            record["last_attempt_status"] = "applied"
            if previous is not None:
                self._replay(lambda c: c.FreeTargetResource(previous))
            return self._describe(record)
        except Exception as exc:
            record["last_attempt_status"] = "operation_failed"
            record["log"] += "\n" + str(exc)
            raise
        finally:
            self._busy = False
            self._restore_event(generation)

    def revert_shader(self, edit_id):
        record = self._record(edit_id)
        if self._busy:
            raise ValueError("SHADER_EDIT_BUSY: another shader operation is running")
        self._assert_owner(record)
        previous = record["replacement"]
        if previous is not None:
            self._replay(lambda c: c.RemoveReplacement(record["original"]))
            try:
                self.ctx.UnregisterReplacement(record["original"])
                self._restore_event(record["generation"])
            except Exception:
                self._replay(lambda c: c.ReplaceResource(record["original"], previous))
                self.ctx.RegisterReplacement(record["original"], previous)
                raise
            record["replacement"] = None
            record["applied_source_text"] = None
            self._replay(lambda c: c.FreeTargetResource(previous))
        record["last_attempt_status"] = "reverted"
        return self._describe(record)

    def list_shader_replacements(self):
        sessions = [self._describe(e) for e in self._edits.values()] if self.ctx.IsCaptureLoaded() else []
        items = [e for e in sessions if e["applied"]]
        return {"items": items, "total_count": len(items), "sessions": sessions,
                "edit_session": self._generation,
                "capture_session": self.session.capture_session if self.session else self._generation}

    def export_shader_source(self, edit_id, output_path):
        record = self._record(edit_id)
        if not isinstance(output_path, str) or not os.path.isabs(output_path):
            raise ValueError("INVALID_OUTPUT_PATH: output_path must be absolute")
        try:
            with open(output_path, "x", encoding="utf-8", newline="") as handle:
                handle.write(record["source_text"])
        except FileExistsError:
            raise ValueError("OUTPUT_FILE_EXISTS: refusing to overwrite " + output_path)
        return {"edit_id": edit_id, "output_path": os.path.abspath(output_path),
                "encoding": self._encoding_name(record["source_encoding"]), "file_encoding": "UTF-8",
                "last_attempt_status": record["last_attempt_status"],
                "matches_applied_source": record["source_text"] == record["applied_source_text"]}

    def dispose(self):
        try:
            if self.ctx.IsCaptureLoaded():
                for record in list(self._edits.values()):
                    if record["replacement"] is None:
                        continue
                    try:
                        self.revert_shader(record["edit_id"])
                    except ValueError as exc:
                        if not str(exc).startswith("SHADER_EDIT_CONFLICT:"):
                            raise
                        self._replay(lambda c: c.FreeTargetResource(record["replacement"]))
        finally:
            self.ctx.RemoveCaptureViewer(self)
            self._reset()
