"""2.0 correctness and lifecycle tests using documented native data shapes."""
import enum
import importlib.util
import json
import math
from pathlib import Path
import struct
import tempfile
from types import SimpleNamespace as NS
import uuid
import sys
import types
import time
from unittest.mock import patch

import pytest

import test_mesh as mesh_tests
import test_pipeline as pipeline_tests


ROOT = Path(__file__).resolve().parents[1]


def standalone(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "renderdoc_extension/services" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


JOBS = standalone("job_service")
VALUES = standalone("texture_values")
NATIVE = pipeline_tests.MODULES["native_serialization"]
VARIABLES = pipeline_tests.MODULES["shader_variables"]
with patch.dict(sys.modules, {"renderdoc_extension.services.job_service": JOBS,
    "renderdoc_extension.services.shader_variables": VARIABLES,
    "renderdoc_extension.services.native_serialization": NATIVE,
    "renderdoc_extension.services.resource_catalog": pipeline_tests.MODULES['resource_catalog']}):
    spec = importlib.util.spec_from_file_location('renderdoc_extension.services.constant_export',
        ROOT/'renderdoc_extension/services/constant_export.py')
    CONSTANT_EXPORT = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(CONSTANT_EXPORT)



class Session:
    def __init__(self):
        self.generation, self.revision = "capture", 0

    def token(self):
        return self.generation, self.revision

    def observe_replacements(self, controller):
        pass

    def describe(self):
        return dict(capture_session=self.generation, replay_revision=self.revision)


@pytest.fixture
def jobs(tmp_path):
    callbacks = []
    session = Session()
    manager = JOBS.JobService(NS(Replay=lambda: NS(AsyncInvoke=callbacks.append)), session, str(tmp_path))
    return manager, callbacks, session


def tick(manager, callbacks):
    manager.pump()
    if callbacks:
        callbacks.pop(0)(NS())


def test_idempotent_submission_conflicts_and_persistence(jobs):
    manager, callbacks, session = jobs
    key = str(uuid.uuid4())
    def steps(key):
        yield "replay", "native_call", lambda c: {"result": {"value": 7}}
    first = manager.submit("test", {"a": 1}, steps, key)
    assert first["status"] == "queued"
    assert manager.submit("test", {"a": 1}, steps, key)["job_id"] == key
    with pytest.raises(ValueError, match="JOB_CONFLICT"):
        manager.submit("test", {"a": 2}, steps, key)
    tick(manager, callbacks)
    tick(manager, callbacks)
    assert manager.status(key)["result"] == {"value": 7}
    assert manager.status(key)["status"] == "completed"
    assert json.loads(Path(first["manifest_path"]).read_text())["status"] == "completed"


def test_cancel_inflight_then_resume_does_not_repeat_completed_step(jobs):
    manager, callbacks, session = jobs
    calls = []
    def steps(key):
        for i in range(3):
            yield "replay", str(i), lambda c, i=i: calls.append(i)
    key = manager.submit("test", {}, steps)["job_id"]
    manager.pump()
    assert len(callbacks) == 1
    manager.cancel(key)
    callbacks.pop()(NS())
    manager.pump()
    assert manager.status(key)["status"] == "cancelled"
    manager.resume(key)
    for _ in range(4):
        tick(manager, callbacks)
    assert calls == [0, 1, 2]
    assert manager.status(key)["status"] == "completed"


def test_budget_pause_retries_only_pending_step(jobs):
    manager, callbacks, session = jobs
    calls = []
    def steps(key):
        def write(c):
            if manager.records[key]["texture_budget"] == 0:
                raise JOBS.PauseJob("TEXTURE_BUDGET")
            calls.append("saved")
            return {"texture_budget": 0}
        yield "replay", "first", write
        yield "replay", "second", write
    key = manager.submit("test", {}, steps)["job_id"]
    tick(manager, callbacks)
    tick(manager, callbacks)
    assert manager.status(key)["status"] == "paused"
    manager.pump()
    manager.resume(key, 1)
    tick(manager, callbacks)
    tick(manager, callbacks)
    assert calls == ["saved", "saved"]
    assert manager.status(key)["status"] == "completed"


def test_session_revision_and_restart_invalidate_jobs(jobs):
    manager, callbacks, session = jobs
    def steps(key):
        yield "replay", "one", lambda c: pytest.fail("stale callback ran")
    key = manager.submit("test", {}, steps)["job_id"]
    session.revision += 1
    manager.pump()
    assert manager.status(key)["status"] == "interrupted"
    with pytest.raises(ValueError, match="STALE_JOB"):
        manager.resume(key)
    session.revision = 0
    second = manager.submit("another", {}, steps)["job_id"]
    restarted = JOBS.JobService(manager.ctx, session, manager.directory)
    assert restarted.status(second)["status"] == "interrupted"


@pytest.mark.parametrize('state',['paused','cancelled'])
def test_capture_change_invalidates_and_releases_suspended_work(jobs,state):
    manager,callbacks,session=jobs
    def steps(key):
        def pause(c):raise JOBS.PauseJob('budget')
        yield 'replay','pause',pause
    key=manager.submit('test',{},steps)['job_id']
    tick(manager,callbacks)
    if state=='cancelled':
        manager.cancel(key);manager.pump()
    assert manager.status(key)['status']==state
    session.generation='new_capture'
    manager.pump()
    assert manager.status(key)['status']=='interrupted'
    assert key not in manager.runners and manager.records[key]['items'] is None


def test_ui_native_step_does_not_probe_controller(jobs):
    manager, callbacks, session = jobs
    def steps(key):
        yield "ui_native", "load", lambda c: {"result": {"controller_is_none": c is None}}
    key = manager.submit("open_capture", {}, steps, capture_bound=False)["job_id"]
    manager.pump()
    manager.pump()
    assert manager.status(key)["result"]["controller_is_none"]
    assert not callbacks


def test_native_sequence_and_slot_descriptors():
    Viewport = type("Viewport", (), {"__slots__": ("x", "y", "width", "height", "minDepth", "maxDepth")})
    view = Viewport()
    for k, v in dict(x=1, y=2, width=2280, height=1428, minDepth=0, maxDepth=1).items():
        setattr(view, k, v)
    class NativeSequence:
        def __len__(self):
            return 1
        def __getitem__(self, i):
            if i:
                raise IndexError()
            return view
    assert NATIVE.plain(NativeSequence())[0]["width"] == 2280
    assert NATIVE.plain([]) == []
    with pytest.raises(ValueError, match="SERIALIZATION_UNAVAILABLE"):
        NATIVE.plain(Viewport())
    with pytest.raises(ValueError, match="unsupported native type"):
        NATIVE.plain(object())


def test_real_sint_and_decoded_matrix_order():
    RealType = enum.IntEnum("VarType", "SInt Float")
    value = NS(name="signed", type=RealType.SInt, rows=1, columns=1,
               value=NS(s32v=[-7]), members=[])
    result = VARIABLES.read_variables([value], [], [], 0, 50)
    assert result["children"]["items"][0]["value"] == [-7]
    value = NS(name="matrix", type=RealType.Float, rows=2, columns=2,
               value=NS(f32v=[1, 2, 3, 4]), members=[])
    declaration = NS(byteOffset=32, type=NS(name="mat2", elements=1, arrayByteStride=0,
                                           matrixByteStride=16, RowMajor=lambda: False))
    row = VARIABLES.read_variables([value], [declaration], [], 0, 50)["children"]["items"][0]
    assert row["value_order"] == "row_major"
    assert row["layout"]["storage_order"] == "column_major"
    assert row["value"] == [1, 2, 3, 4]


@pytest.mark.parametrize("width,code", [(1, "B"), (2, "H"), (4, "I")])
def test_compacted_postvs_indices_and_csv(width, code, tmp_path):
    t = mesh_tests
    controller = t.Controller()
    ctx = t.Context(controller)
    ctx.action.numIndices = 6
    post = t.postvs_mesh(stride=16)
    post.numIndices, post.indexResourceId, post.indexByteStride = 6, t.ResourceId(8), width
    post.indexByteOffset = 4
    controller.postvs = post
    controller.buffers[7] = struct.pack("<12f", 10, 11, 12, 1, 20, 21, 22, 1, 30, 31, 32, 1)
    controller.buffers[8] = bytes(4) + struct.pack("<6" + code, 2, 0, 1, 2, 1, 0)
    controller.reflections[t.ShaderStage.Vertex] = NS(outputSignature=[t.sig("POSITION", 0, 4)])
    service = t.MESH.MeshService(ctx, ctx.invoke)
    result = service.get_mesh_data(343, "VSOut")
    assert result["indices"] == [2, 0, 1, 2, 1, 0]
    assert [v["POSITION"][0] for v in result["items"]] == [30, 10, 20, 30, 20, 10]
    export = service.export_mesh_csv(343, str(tmp_path / "mesh.csv"), "VSOut")
    assert export["vertex_count"] == 3
    assert Path(export["index_path"]).read_text().split() == ["0", "1", "2", "0", "2", "1"]


def test_mesh_short_read_and_negative_vertex_are_errors():
    t = mesh_tests
    service = t.MESH.MeshService(NS(), lambda fn: None)
    fmt = t.ResourceFormat()
    with pytest.raises(ValueError, match="OUT_OF_BOUNDS"):
        service._unpack_vertex_data(fmt, b"", 0)
    with pytest.raises(ValueError, match="OUT_OF_BOUNDS"):
        service._unpack_vertex_data(fmt, bytes(16), -1)
    mesh = t.MeshFormat()
    mesh.indexResourceId, mesh.indexByteStride, mesh.numIndices = t.ResourceId(8), 2, 3
    with pytest.raises(ValueError, match="SHORT_READ"):
        service._get_indices(NS(GetBufferData=lambda *args: b"\0\0"), mesh)


def fmt(kind="Regular", comp="Float", width=4, count=4, bgra=False):
    return NS(type=NS(name=kind), compType=NS(name=comp), compByteWidth=width,
              compCount=count, BGRAOrder=lambda: bgra)


@pytest.mark.parametrize("width,code", [(2, "e"), (4, "f"), (8, "d")])
def test_float_texture_decoding_preserves_hdr_negative_nan(width, code):
    size, count, read = VALUES.decoder(fmt(width=width))
    data = struct.pack("<4" + code, -1, 16, float("nan"), float("inf"))
    result = read(data, 0, "storage")
    assert result[:2] == [-1, 16]
    assert math.isnan(result[2]) and math.isinf(result[3])


def test_integer_srgb_bgra_and_alpha_domains():
    _, _, read = VALUES.decoder(fmt(comp="UNormSRGB", width=1, bgra=True))
    raw = bytes([255, 128, 0, 128])
    encoded = read(raw, 0, "storage")
    linear = read(raw, 0, "linear")
    assert encoded == [0, 128 / 255, 1, 128 / 255]
    assert linear[1] < encoded[1]
    assert linear[3] == encoded[3]
    _, _, read = VALUES.decoder(fmt(comp="SInt", width=4, count=1))
    assert read(struct.pack("<i", -123), 0, "storage") == [-123]


def test_packed_r11g11b10_and_r10g10b10a2():
    _, _, read = VALUES.decoder(fmt("R11G11B10", count=3))
    bits = (15 << 6) | ((15 << 6) << 11) | ((15 << 5) << 22)
    assert read(struct.pack("<I", bits), 0, "linear") == [1, 1, 1]
    _, _, read = VALUES.decoder(fmt("R10G10B10A2", comp="UNorm"))
    assert read(bytes([255] * 4), 0, "storage") == [1, 1, 1, 1]
    _, _, read = VALUES.decoder(fmt("R10G10B10A2", comp="SInt"))
    assert read(bytes([255] * 4), 0, "storage") == [-1, -1, -1, -1]
    _, _, read = VALUES.decoder(fmt("R10G10B10A2", comp="SNorm"))
    bits = 512 | (511 << 10) | (0 << 20) | (2 << 30)
    assert read(struct.pack('<I',bits),0,'storage') == [-1,1,0,-1]


def test_roi_limits_and_unsupported_formats():
    with pytest.raises(ValueError, match="UNSUPPORTED_FORMAT"):
        VALUES.decoder(fmt("ASTC"))
    with pytest.raises(ValueError, match="outside"):
        VALUES.validate_region(dict(x=1, y=0, width=10, height=1), 10, 10)
    with pytest.raises(ValueError, match="RESOURCE_LIMIT"):
        VALUES.validate_region(dict(x=0, y=0, width=1024, height=1024), 1024, 1024)


def test_job_status_is_available_during_stalled_native_callback(jobs, monkeypatch):
    manager, callbacks, session = jobs
    def steps(key):
        yield "replay", "native", lambda c: None
    key = manager.submit("test", {}, steps)["job_id"]
    assert manager.busy()  # Includes queued jobs before the first timer tick.
    manager.pump()
    now = JOBS.time.time()
    monkeypatch.setattr(JOBS.time, "time", lambda: now + 45)
    status = manager.status(key)
    assert status["status"] == "running" and status["stalled"]
    assert status["idle_seconds"] >= 45
    manager.cancel(key)
    callbacks.pop()(NS())
    manager.pump()
    assert not manager.busy()


def test_pause_is_immediately_resumable_without_extra_timer_tick(jobs):
    manager, callbacks, _ = jobs
    def steps(key):
        def pause(c):
            raise JOBS.PauseJob("budget")
        yield "replay", "pause", pause
    key = manager.submit("test", {}, steps)["job_id"]
    tick(manager, callbacks)
    assert not manager.busy()
    assert manager.resume(key)["status"] == "queued"


@pytest.fixture
def capture_environment(tmp_path, monkeypatch):
    monkeypatch.setitem(sys.modules, "renderdoc", mesh_tests.MESH.rd)
    module = standalone("capture_manager")
    rd = module.rd
    calls = []
    outcome = NS(OK=lambda: True, Message=lambda: "Success")
    class Host:
        def __init__(self, name):
            self.name, self.connected, self.running, self.mismatch = name, False, True, False
        def Hostname(self): return self.name
        def IsConnected(self): return self.connected
        def IsServerRunning(self): return self.running
        def IsBusy(self): return False
        def IsVersionMismatch(self): return self.mismatch
        def VersionMismatchError(self): return "1.45 != 1.46"
        def CheckStatus(self): calls.append("check")
        def Launch(self):
            calls.append("launch")
            self.running = True
            return outcome
    local, remote, local_choice = Host(""), Host("adb://DEVICE"), Host("localhost")
    current = [local]
    def connect(host):
        if host.Hostname()=='localhost':
            current[0]=local
            calls.append('connect_local')
            return outcome
        current[0] = host
        host.connected = True
        calls.append("connect")
        return outcome
    connection = NS(ListFolder=lambda path: [NS(filename="#DefaultActivity")],
                    CopyCaptureFromRemote=lambda source,dest,progress:Path(dest).write_bytes(b'capture'),
                    ShutdownConnection=lambda: calls.append("preflight_close"))
    monkeypatch.setattr(rd, "CreateRemoteServerConnection", lambda h: (outcome, connection), raising=False)
    monkeypatch.setattr(rd, "ReplayOptions", lambda: NS(), raising=False)
    monkeypatch.setattr(rd, "OpenCaptureFile", lambda:NS(OpenFile=lambda *args:outcome,
                        DriverName=lambda:'Vulkan',Shutdown=lambda:None),raising=False)
    monkeypatch.setitem(sys.modules, "qrenderdoc", NS(RemoteHost=lambda name: local_choice if name=='localhost' else remote))
    replay = NS(CurrentRemote=lambda: current[0], ConnectToRemoteServer=connect,
                DisconnectFromRemoteServer=lambda: calls.append("disconnect"),
                GetRemoteSupport=lambda:['Vulkan'],
                ListFolder=lambda path, wait, cb: cb(path, [NS(filename="frame.rdc")]),
                CopyCaptureFromRemote=lambda source,dest,widget:Path(dest).write_bytes(b'capture'),
                CopyCaptureToRemote=lambda path, widget: calls.append("upload") or "/remote/frame.rdc")
    ctx = NS(Replay=lambda: replay, Config=lambda: NS(GetRemoteHosts=lambda: [local_choice,remote]),
             IsCaptureLoaded=lambda: True, GetCaptureFilename=lambda: ctx.filename,
             GetMainWindow=lambda: NS(Widget=lambda: None), filename="old.rdc")
    ctx.CloseCapture = lambda: calls.append("close_capture")
    ctx.ConnectToRemoteServer = lambda host: calls.append('context_connect') or connect(host)
    def load(path, options, original, temporary, local):
        calls.append(("load", path, local))
        ctx.filename = original
    ctx.LoadCapture = load
    session = Session()
    manager = JOBS.JobService(ctx, session, str(tmp_path/'jobs'))
    controller = NS(GetAPIProperties=lambda: NS(pipelineType="Vulkan", remoteReplay=bool(current[0].Hostname())),
                    GetFatalErrorStatus=lambda: outcome)
    service = module.CaptureManager(ctx, lambda fn: fn(controller), session=session, jobs=manager)
    service._guard_android_start = lambda hostname:calls.append('start_guard')
    return service, manager, remote, calls, tmp_path, current


@pytest.mark.parametrize("location,target,connected", [("local","local",False), ("local","remote",False),
                                                       ("remote","remote",False), ("remote","remote",True)])
def test_capture_preflight_upload_and_remote_file_location(capture_environment, monkeypatch, location, target, connected):
    service, jobs, host, calls, directory, current = capture_environment
    path = directory/'frame.rdc'
    path.write_bytes(b"capture")
    if connected:
        host.connected = True
        current[0] = host
    capture_path = str(path) if location == "local" else "/remote/frame.rdc"
    if location == "remote":
        original_isfile = sys.modules['os'].path.isfile
        def forbidden_local_stat(path):
            if path == capture_path:
                pytest.fail("remote capture was checked with local isfile")
            return original_isfile(path)
        monkeypatch.setattr(sys.modules['os'].path, "isfile", forbidden_local_stat)
    key = service.open_capture(capture_path, location, target, host.Hostname() if target == "remote" else None)["job_id"]
    jobs.pump()
    jobs.pump()
    result = jobs.status(key)
    assert result["status"] == "completed", result["error"]
    assert ("upload" in calls) == (location == "local" and target == "remote")
    load = next(c for c in calls if isinstance(c, tuple))
    assert load[2] == (target == "local")
    if location == "remote":
        assert not path.parent.joinpath("remote").exists()
    if target=='remote' and not connected:
        assert 'context_connect' in calls


@pytest.mark.parametrize("failure", ["version", "start", "connect", "file"])
def test_remote_preflight_failure_keeps_existing_capture(capture_environment, monkeypatch, failure):
    service, jobs, host, calls, directory, current = capture_environment
    if failure == "version":
        host.mismatch = True
    if failure == "start":
        host.running = False
        host.Launch = lambda: NS(OK=lambda: False, Message=lambda: "launch denied")
    if failure == "connect":
        monkeypatch.setattr(service.__class__.__init__.__globals__["rd"], "CreateRemoteServerConnection",
                            lambda h: (NS(OK=lambda: False, Message=lambda: "unreachable"), None))
    if failure == "file":
        current[0] = host
        host.connected = True
        service.ctx.Replay().CopyCaptureFromRemote = lambda *args:None
    key = service.open_capture("/remote/frame.rdc", "remote", "remote", host.Hostname())["job_id"]
    jobs.pump()
    assert jobs.status(key)["status"] == "failed"
    assert "close_capture" not in calls
    assert service.ctx.filename == "old.rdc"


@pytest.fixture
def investigation(tmp_path, monkeypatch):
    rd = pipeline_tests.RD
    monkeypatch.setattr(rd, "Subresource", lambda: NS(), raising=False)
    dependencies = {"renderdoc": rd, "renderdoc_extension.services.job_service": JOBS,
                    "renderdoc_extension.services.texture_values": VALUES,
                    "renderdoc_extension.services.constant_export": CONSTANT_EXPORT,
                    "renderdoc_extension.services.pipeline_snapshot": pipeline_tests.MODULES["pipeline_snapshot"],
                    "renderdoc_extension.utils": NS(Parsers=pipeline_tests.MODULES['pipeline_snapshot'].Parsers)}
    for name in ('native_serialization', 'replay_query', 'resource_catalog'):
        dependencies['renderdoc_extension.services.'+name] = pipeline_tests.MODULES[name]
    with patch.dict(sys.modules, dependencies):
        spec = importlib.util.spec_from_file_location('renderdoc_extension.services.investigation_service',
                                                      ROOT/'renderdoc_extension/services/investigation_service.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    callbacks, calls = [], []
    ctx = NS(IsCaptureLoaded=lambda: True, CurEvent=lambda: 99, GetAction=lambda e: NS(eventId=e),
             Replay=lambda: NS(AsyncInvoke=callbacks.append))
    session = Session()
    jobs = JOBS.JobService(ctx, session, str(tmp_path/'jobs'))
    texture_format = fmt(comp='SInt', width=4, count=1)
    texture_format.Name = lambda: 'R32_SINT'
    texture_format.compType = rd.CompType.SInt
    texture = NS(resourceId=rd.ResourceId(1), width=2, height=1, depth=1,
                 mips=1, arraysize=1, msSamp=1, format=texture_format)
    controller = NS(event=99, GetAPIProperties=lambda: NS(pipelineType='Vulkan', pixelHistory=True),
                    GetTextures=lambda: [texture])
    controller.SetFrameEvent = lambda event, force: setattr(controller, 'event', event)
    def data(rid, sub):
        calls.append(controller.event)
        return struct.pack('<2i', *([-9, 50] if controller.event == 10 else [-6, 45]))
    controller.GetTextureData = data
    def run(key):
        for _ in range(200):
            jobs.pump()
            if callbacks:
                callbacks.pop(0)(controller)
            if jobs.status(key)['status'] in JOBS.TERMINAL:
                break
            time.sleep(.005)
        return jobs.status(key)
    return module.InvestigationService(ctx, session, jobs), controller, calls, run, tmp_path


def test_texture_comparison_reads_each_event_once_and_restores(investigation):
    service, controller, calls, run, tmp = investigation
    key = service.compare_texture_events('ResourceId::1',10,20,dict(x=0,y=0,width=2,height=1),str(tmp))['job_id']
    status = run(key)
    assert status['status'] == 'completed', status['error']
    result = status['result']
    assert calls == [10,20] and controller.event == 99
    assert struct.unpack('<2d',Path(result['difference_file']).read_bytes()) == (3,-5)
    assert result['changed_pixels'] == 2 and result['mean_absolute_error'] == [4]


def test_all_nonfinite_roi_has_no_fabricated_zero_error(investigation):
    service,controller,calls,run,tmp=investigation
    texture=controller.GetTextures()[0]
    texture.format.compType=pipeline_tests.RD.CompType.Float
    controller.GetTextureData=lambda *args:struct.pack('<2f',float('nan'),float('inf'))
    key=service.compare_texture_events('1',10,20,dict(x=0,y=0,width=2,height=1),str(tmp))['job_id']
    status=run(key)
    assert status['status']=='completed',status['error']
    result=status['result']
    assert result['finite_samples']==[0]
    assert result['max_absolute_error']==result['mean_absolute_error']==[None]
    assert result['nonfinite'][0]['nonfinite_delta']==2
    assert result['nonfinite'][0]['nan_a']==1 and result['nonfinite'][0]['inf_a']==1


@pytest.mark.parametrize('mode', ['unsupported', 'size', 'roi', 'short'])
def test_texture_comparison_failures_restore_replay(investigation, mode):
    service, controller, calls, run, tmp = investigation
    texture = controller.GetTextures()[0]
    region = dict(x=0,y=0,width=1,height=1)
    if mode == 'unsupported': texture.format.type = NS(name='ASTC')
    if mode == 'size': texture.width, texture.height = 8192,8192
    if mode == 'roi': region['width'] = 3
    if mode == 'short': controller.GetTextureData = lambda *args: b''
    key = service.compare_texture_events('1',10,20,region,str(tmp))['job_id']
    status = run(key)
    assert status['status'] == 'failed'
    assert controller.event == 99
    assert not list(tmp.glob('*/manifest.json'))


def test_pixel_history_capability_and_paginated_native_fragments(investigation):
    service, controller, calls, run, tmp = investigation
    controller.GetAPIProperties = lambda: NS(pixelHistory=False)
    key = service.get_pixel_history('1',0,0,20,str(tmp))['job_id']
    assert run(key)['result']['available'] is False
    controller.GetAPIProperties = lambda: NS(pixelHistory=True)
    value = NS(col=NS(intValue=[-7,0,0,0]), depth=0.5, stencil=0)
    controller.PixelHistory = lambda *args: [NS(eventId=10,fragIndex=i,directShaderWrite=False,unboundPS=False,
                                               preMod=value,shaderOut=value,postMod=value,shaderDiscarded=False)
                                            for i in range(3)]
    key = service.get_pixel_history('1',0,0,20,str(tmp))['job_id']
    status = run(key)
    assert status['status'] == 'completed' and controller.event == 99
    page = service.jobs.status(key, offset=1,limit=1)
    assert page['total_count'] == 3 and page['has_more']
    assert page['items'][0]['postMod']['color'][0] == -7
    assert not page['items'][0]['preMod_valid']


def test_reflected_layout_keeps_nested_strides_without_inferred_semantics():
    typ = NS(rows=4,columns=4,baseType=NS(name='Float'),elements=3,
             arrayByteStride=64,matrixByteStride=16,RowMajor=lambda:False,members=[])
    rows = VARIABLES.reflected_layout([NS(name='m',byteOffset=32,type=typ)])
    assert rows[0]['matrix'] and rows[0]['array_byte_stride'] == 64
    assert rows[0]['storage_order'] == 'column_major'
    assert 'value' not in rows[0] and 'object_matrix' not in rows[0]


@pytest.mark.parametrize('name,field,number', [('Float','f32v',1.5),('Double','f64v',2.5),('Half','f16v',.5),
    ('SInt','s32v',-9),('UInt','u32v',9),('Bool','u32v',1),('Enum','s32v',-2),
    ('SLong','s64v',-4294967297),('ULong','u64v',4294967297),('SShort','s16v',-9),
    ('UShort','u16v',9),('SByte','s8v',-9),('UByte','u8v',9)])
def test_all_documented_scalar_constant_fields(name, field, number):
    value = NS(name='v',type=NS(name=name),rows=1,columns=1,members=[],value=NS(**{field:[number]}))
    assert VARIABLES.read_variables([value],[],[],0,50)['children']['items'][0]['value'] == [number]


def test_array_element_offsets_are_relative_to_array_parent():
    typ = NS(name='float[2]',elements=2,arrayByteStride=16,matrixByteStride=0,members=[])
    declaration = NS(name='array',byteOffset=32,type=typ)
    elem = lambda n: NS(name='[%d]'%n,type=NS(name='Float'),rows=1,columns=1,members=[],value=NS(f32v=[n]))
    array = NS(name='array',type=NS(name='Float'),rows=0,columns=0,members=[elem(0),elem(1)])
    result = VARIABLES.read_variables([array],[declaration],[0],0,50)
    assert result['node']['layout']['byte_offset'] == 32
    assert [r['layout']['byte_offset'] for r in result['children']['items']] == [0,16]
    assert all(r['layout']['offset_basis']=='parent' for r in result['children']['items'])


def test_postvs_restart_base_vertex_and_multiview_validation(tmp_path):
    t = mesh_tests
    controller = t.Controller()
    ctx = t.Context(controller)
    pipe = controller.GetPipelineState()
    pipe.IsRestartEnabled, pipe.GetRestartIndex = lambda:True, lambda:65535
    pipe.MultiviewBroadcastCount = lambda:2
    controller.GetPipelineState = lambda:pipe
    post = t.postvs_mesh(stride=16)
    post.numIndices, post.indexResourceId, post.indexByteStride = 4,t.ResourceId(8),2
    post.indexByteOffset, post.baseVertex = 4,1
    controller.postvs = post
    controller.buffers[8] = bytes(4)+struct.pack('<4H',1,0,65535,1)
    controller.buffers[7] = struct.pack('<12f',0,0,0,1,10,11,12,1,20,21,22,1)
    controller.reflections[t.ShaderStage.Vertex] = NS(outputSignature=[t.sig('POSITION',0,4)])
    service = t.MESH.MeshService(ctx,ctx.invoke)
    result = service.get_mesh_data(343,'VSOut',view_index=1)
    assert result['indices'] == [2,1,-1,2]
    assert result['items'][2] == {'primitive_restart':True}
    assert controller.postvs_calls[-1][1] == 1
    export = service.export_mesh_csv(343,str(tmp_path/'mesh.csv'),'VSOut',view_index=1)
    assert Path(export['index_path']).read_text().split() == ['0','1','-1','0']
    with pytest.raises(ValueError,match='VIEW_INDEX'):
        service.get_mesh_data(343,'VSOut',view_index=2)
    with pytest.raises(ValueError,match='VIEW_INDEX'):
        service.export_mesh_csv(343,str(tmp_path/'bad.csv'),'VSIn',view_index=1)


def test_atomic_job_snapshot_reads_only_requested_page_without_ui(jobs, monkeypatch):
    from mcp_server.bridge.job_status import read_status
    manager, callbacks, _ = jobs
    def steps(key):
        for index in range(4):
            yield 'replay','item',lambda c,index=index:{'item':{'item_key':str(index),'value':index}}
    key=manager.submit('test',{},steps)['job_id']
    for _ in range(5): tick(manager,callbacks)
    metadata=json.loads(Path(manager.directory,key+'.json').read_text())
    assert 'items' not in metadata and len(metadata['item_files'])==4
    original=json.load
    reads=[]
    def counted(handle,*args,**kwargs):
        reads.append(handle.name)
        return original(handle,*args,**kwargs)
    monkeypatch.setattr(json,'load',counted)
    result=read_status(manager.directory,key,offset=2,limit=1)
    assert len(reads)==2 and result['items'][0]['value']==2
    assert result['total_count']==4 and result['has_more']
    reads.clear()
    restarted=JOBS.JobService(manager.ctx,manager.session,manager.directory)
    assert not any(Path(path).parent.name=='items' for path in reads)
    assert restarted.status(key)['items']==manager.status(key)['items']


def test_batch_status_is_compact_and_full_binding_evidence_stays_on_disk(jobs):
    from mcp_server.bridge.job_status import read_status
    manager,callbacks,_=jobs
    item=dict(item_key='343:0:0',action_event_id=343,complete=True,ok=True,warnings=[],
              bindings=[dict(raw_evidence='x'*(2*1024*1024))],textures=[])
    def steps(key):
        yield 'replay','facts',lambda c:{'item':item}
    key=manager.submit('dump_draws',{},steps)['job_id']
    tick(manager,callbacks);tick(manager,callbacks)
    private=manager.status(key)
    public=read_status(manager.directory,key)
    assert private['items']==public['items']
    assert len(json.dumps(public))<4096
    assert 'bindings' not in public['items'][0]
    details=json.loads(Path(public['items'][0]['details_path']).read_text())
    assert details['bindings']==item['bindings']
    assert manager.records[key]['items'] is None


def test_loaded_capture_defers_protocol_discovery(capture_environment, monkeypatch):
    service,jobs,host,calls,directory,current=capture_environment
    monkeypatch.setattr(service.__class__.__init__.__globals__['rd'],'GetSupportedDeviceProtocols',
                        lambda:pytest.fail('enumerating ADB during loaded capture can disrupt replay'),raising=False)
    assert service.get_replay_context()['discovery_deferred']


def test_disk_cancellation_works_without_ui_and_is_consumed_cooperatively(jobs):
    from mcp_server.bridge.job_status import request_cancel,read_status
    manager,callbacks,_=jobs
    def steps(key):
        yield 'replay','native',lambda c:None
    key=manager.submit('test',{},steps)['job_id']
    manager.pump()
    assert request_cancel(manager.directory,key)['status']=='cancelling'
    assert manager.records[key]['cancel_requested'] is False  # UI has not polled.
    manager.pump()
    assert manager.records[key]['cancel_requested']
    callbacks.pop()(NS())
    manager.pump()
    assert read_status(manager.directory,key)['status']=='cancelled'
    manager.resume(key)
    assert not Path(manager.directory,'controls',key+'.cancel.json').exists()


def test_worker_step_leaves_ui_scheduler_available(jobs):
    import threading
    manager,callbacks,_=jobs
    release=threading.Event()
    def steps(key):
        yield 'worker','manifest',lambda c:release.wait(2) and {'result':{'saved':True}}
    key=manager.submit('test',{},steps)['job_id']
    manager.pump()
    assert manager.inflight and not callbacks
    assert manager.status(key)['phase']=='manifest'
    manager.cancel(key)
    release.set()
    for _ in range(100):
        if not manager.inflight: break
        time.sleep(.005)
    manager.pump()
    assert manager.status(key)['status']=='cancelled'


def test_external_replacement_and_capture_changes_invalidate_shared_tokens(monkeypatch):
    monkeypatch.setitem(sys.modules,'qrenderdoc',NS(CaptureViewer=object))
    module=standalone('session_state')
    target=[1]
    ctx=NS(AddCaptureViewer=lambda v:None,RemoveCaptureViewer=lambda v:None,
           GetResources=lambda:[NS(type='Shader',resourceId=1)],GetResourceReplacement=lambda rid:target[0])
    session=module.SessionState(ctx)
    session.observe_replacements()
    original=session.token()
    target[0]=9
    session.observe_replacements()
    assert session.token()==(original[0],original[1]+1)
    session.OnCaptureClosed()
    assert session.token()[0]!=original[0] and session.token()[1]==0


def test_duplicate_draw_and_instance_requests_have_consistent_progress(tmp_path):
    dependencies={'renderdoc':mesh_tests.MESH.rd,
        'renderdoc_extension.services.job_service':JOBS,
        'renderdoc_extension.services.mesh_service':mesh_tests.MESH,
        'renderdoc_extension.services.pipeline_snapshot':pipeline_tests.MODULES['pipeline_snapshot'],
        'renderdoc_extension.services.replay_query':pipeline_tests.MODULES['replay_query'],
        'renderdoc_extension.services.shader_variables':VARIABLES,
        'renderdoc_extension.services.constant_export':CONSTANT_EXPORT}
    with patch.dict(sys.modules,dependencies):
        spec=importlib.util.spec_from_file_location('renderdoc_extension.services.batch_service',
                                                   ROOT/'renderdoc_extension/services/batch_service.py')
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    callbacks=[]
    action=NS(eventId=343,flags=mesh_tests.ActionFlags.Drawcall,numInstances=1)
    ctx=NS(IsCaptureLoaded=lambda:True,GetAction=lambda eid:action,
           Replay=lambda:NS(AsyncInvoke=callbacks.append))
    manager=JOBS.JobService(ctx,Session(),str(tmp_path/'jobs'))
    service=module.BatchService(ctx,None,None,manager.session,manager)
    key=service.dump_draws(str(tmp_path),action_event_ids=[343,343],instances=[0,0],
                          export_meshes=False,export_textures=False)['job_id']
    manager.pump()
    status=manager.status(key)
    assert status['parameters']['instances']==[0]
    assert status['expected_items']==1
    assert status['counts']==dict(requested=2,valid_draws=1,successful=0,failed=0,skipped=1,pending=1)


@pytest.mark.parametrize('case',['valid','missing','mismatch','orphan32','old_sdk','other_user','future_version'])
def test_android_official_start_never_reaches_install_branch(capture_environment,monkeypatch,case):
    service,jobs,host,calls,directory,current=capture_environment
    rd=service.__class__.__init__.__globals__['rd']
    monkeypatch.setattr(rd,'GetVersionString',lambda:'1.47' if case=='future_version' else '1.46',raising=False)
    monkeypatch.setattr(rd,'GetCommitHash',lambda:'hosthash',raising=False)
    host.running=False
    service._guard_android_start=lambda h:service.__class__._guard_android_start(service,h)
    def query(serial,args):
        assert serial=='DEVICE'
        if args==['getprop','ro.product.cpu.abi']:return 'arm64-v8a'
        if args==['am','get-current-user']:return '10' if case=='other_user' else '0'
        if args==['getprop','ro.build.version.sdk']:return '30' if case=='old_sdk' else '34'
        if args[:3]==['pm','list','packages']:
            assert args[3:5]==['--user','10' if case=='other_user' else '0']
            return '' if case in ('missing','other_user') else 'package:org.renderdoc.renderdoccmd.arm64'
        if args[:2]==['pm','dump']:
            if args[2].endswith('arm32'):return 'versionCode=145 versionName=oldhash' if case=='orphan32' else ''
            return 'versionCode=146 versionName='+('oldhash' if case=='mismatch' else 'hosthash')
        raise AssertionError(args)
    service._android_query=query
    key=service.open_capture('/remote/frame.rdc','remote','remote',host.Hostname())['job_id']
    jobs.pump();jobs.pump()
    status=jobs.status(key)
    assert ('launch' in calls)==(case=='valid')
    assert status['status']==('completed' if case=='valid' else 'failed')
    if case!='valid':assert 'close_capture' not in calls


def test_local_selection_updates_capture_context_not_just_replay_manager(capture_environment):
    service,jobs,host,calls,directory,current=capture_environment
    current[0]=host
    host.connected=True
    path=directory/'frame.rdc';path.write_bytes(b'capture')
    key=service.open_capture(str(path),'local','local')['job_id']
    jobs.pump();jobs.pump()
    status=jobs.status(key)
    assert status['status']=='completed',status['error']
    assert 'context_connect' in calls and 'connect_local' in calls
    assert current[0].Hostname()=='' and status['result']['remote_replay'] is False


def test_successful_launch_without_ready_server_does_not_close_old_capture(capture_environment):
    service,jobs,host,calls,directory,current=capture_environment
    host.running=False
    host.Launch=lambda:NS(OK=lambda:True)
    key=service.open_capture('/remote/frame.rdc','remote','remote',host.Hostname())['job_id']
    jobs.pump()
    assert jobs.status(key)['error'].startswith('REMOTE_START_FAILED:')
    assert 'close_capture' not in calls and 'context_connect' not in calls
