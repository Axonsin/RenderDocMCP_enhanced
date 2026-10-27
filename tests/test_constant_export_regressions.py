"""Constant block identity and independent raw/value export regressions."""
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace as NS
from unittest.mock import patch

import pytest
import test_pipeline as pipeline
import test_v2 as v2


def test_gl_constant_keys_preserve_sources_and_interactive_decode():
    controller = pipeline.Controller()
    controller.api = 'OpenGL'
    pipe = controller.pipe
    pipe.reflection.constantBlocks = [
        pipeline.declaration('UnityPerDraw', 0, size=688),
        pipeline.declaration('$Globals', 0, backed=False)]
    pipe.constants = [pipeline.used(index=0, rid=10, offset=0, size=688),
                      pipeline.used(index=1, rid=0, offset=0, size=0)]
    names = ['unity_ObjectToWorld', 'unity_MatrixVP']
    controller.GetCBufferVariableContents = lambda *args: [pipeline.variable(names[args[4]])]
    ctx = pipeline.Context(controller)
    snapshot = pipeline.MODULES['pipeline_snapshot'].Snapshot(ctx, controller, ctx.action, ('capture', 0))
    rows = [r for r in snapshot.bindings if r['stage'] == 'vertex' and r['category'] == 'constant']
    assert len(rows) == 2 and rows[0]['binding_key'] != rows[1]['binding_key']
    for index, row in enumerate(rows):
        source = snapshot.variable_sources[row['binding_key']]
        assert source[0:3] == (pipeline.Stage.Vertex, index, 0)
        assert source[4] is pipe.reflection.constantBlocks[index]
        assert json.loads(row['binding_key']) == ['vertex', 'constant',
            dict(array_element=0, binding=0, set_or_space=0, reflection_index=index)]
    service = pipeline.SERVICE(ctx, ctx.invoke)
    public_rows = service.get_pipeline_stage(343, 'vertex', 'constant_buffers')['items']
    for index, row in enumerate(public_rows):
        decoded = service.inspect_pipeline_binding(343, row['binding_id'], section='variables')
        assert decoded['available']
        assert decoded['children']['items'][0]['name'] == names[index]
    assert controller.event == 99


@pytest.mark.parametrize('case', ['short_read', 'read_error', 'default', 'default_zero', 'push_constants', 'decode_error'])
def test_raw_and_values_are_independent(tmp_path, case):
    backed = case not in ('default', 'default_zero', 'push_constants')
    size = 0 if case == 'default_zero' else 4
    calls = []
    def read(rid, offset, size):
        calls.append((rid, offset, size))
        assert backed, 'direct constants must not read a buffer'
        if case == 'read_error':
            raise RuntimeError('driver read failed')
        return b'x' if case == 'short_read' else b'abcd'
    def decode(*args):
        assert args[4:] == (0, 1 if backed else 0, 0, size)
        if case == 'decode_error':
            raise RuntimeError('decode failed')
        return [pipeline.variable('camera', 2.0)]
    decl = NS(name='UnityPerDraw' if backed else '$Globals', byteSize=size, variables=[])
    pipe = NS(GetConstantBlock=lambda *a: NS(descriptor=NS(resource=1 if backed else 0, byteOffset=0)),
              GetGraphicsPipelineObject=lambda: 2, GetShader=lambda s: 3, GetShaderEntryPoint=lambda s: 'main')
    row = dict(category='constant', stage='vertex', binding_key='key', location={}, bound=True,
               provided_bytes=size if backed else None, buffer_backed=backed, binding_name=decl.name)
    snapshot = NS(bindings=[row], event_id=4620, pipe=pipe,
                  controller=NS(GetBufferData=read, GetCBufferVariableContents=decode),
                  api='Vulkan' if case == 'push_constants' else 'OpenGL', native=NS(pushconsts=b'abcd'),
                  variable_sources={'key': ('vertex', 0, 0, object(), decl)})
    record = v2.CONSTANT_EXPORT.read_constants(snapshot)[0]
    assert record['status'] == ('failed' if case == 'decode_error' else 'exported')
    assert record['values_status'] == record['status']
    assert record['layout'] == []
    if case != 'decode_error':
        assert record['values'][0]['value'] == [2.0]
    if case in ('short_read', 'read_error', 'default', 'default_zero'):
        assert record['raw']['status'] == 'unavailable'
        assert record['raw']['binding_name'] == decl.name
        assert record['raw']['expected_bytes'] == size
        assert '_raw' not in record
        if case == 'short_read':
            assert record['raw']['actual_bytes'] == 1
            assert 'UnityPerDraw (expected 4 bytes, actual 1 bytes)' in record['raw']['reason']
        elif case == 'read_error':
            assert 'driver read failed' in record['raw']['reason']
        else:
            assert not calls
            assert 'CONSTANT_RAW_UNAVAILABLE' in record['raw']['reason']
    else:
        assert record['raw']['status'] == 'exported' and record['_raw'] == b'abcd'
    summary = v2.CONSTANT_EXPORT.write_constants(str(tmp_path), [record], {}, 'e4620')[0]
    details = json.loads(Path(summary['details_path']).read_text())
    assert details['raw'] == summary['raw']
    assert details['values_status'] == record['values_status']
    assert ('path' in summary['raw']) == ('_raw' in record)


def test_failed_constants_still_export_textures(tmp_path, monkeypatch):
    dependencies = {'renderdoc': pipeline.RD,
        'renderdoc_extension.services.job_service': v2.JOBS,
        'renderdoc_extension.services.mesh_service': v2.mesh_tests.MESH,
        'renderdoc_extension.services.pipeline_snapshot': pipeline.MODULES['pipeline_snapshot'],
        'renderdoc_extension.services.replay_query': pipeline.MODULES['replay_query'],
        'renderdoc_extension.services.shader_variables': v2.VARIABLES,
        'renderdoc_extension.services.constant_export': v2.CONSTANT_EXPORT}
    with patch.dict(sys.modules, dependencies):
        spec = importlib.util.spec_from_file_location('renderdoc_extension.services.batch_constant_regression',
            v2.ROOT / 'renderdoc_extension/services/batch_service.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    controller = pipeline.Controller()
    ctx = pipeline.Context(controller)
    ctx.action.numInstances = 1
    callbacks = []
    ctx.Replay = lambda: NS(AsyncInvoke=callbacks.append)
    texture = dict(bound=True, resource_kind='texture', roles=['input'],
                   resource={'resource_id': 'ResourceId::11'})
    snapshot = NS(pipe=controller.pipe, bindings=[], variable_sources={},
                  stages={'rasterizer': {}, 'framebuffer': {}}, texture_rows=lambda: [texture])
    monkeypatch.setattr(module, 'Snapshot', lambda *a: snapshot)
    monkeypatch.setattr(module, 'read_constants', lambda s: [
        dict(binding_key='bad', stage='vertex', status='failed', error='decode failed')])
    monkeypatch.setattr(pipeline.RD, 'TextureSave', lambda: NS(slice=NS(), sample=NS()), raising=False)
    monkeypatch.setattr(pipeline.RD, 'FileType', NS(PNG=1), raising=False)
    monkeypatch.setattr(pipeline.RD, 'AlphaMapping', NS(Preserve=1), raising=False)
    saved = []
    def save(config, path):
        saved.append(path)
        Path(path).write_bytes(b'png evidence')
        return NS(OK=lambda: True)
    controller.SaveTexture = save
    controller.GetTextures = lambda: [NS(resourceId=pipeline.ResourceId(11), format=pipeline.FMT)]
    manager = v2.JOBS.JobService(ctx, v2.Session(), str(tmp_path / 'jobs'))
    service = module.BatchService(ctx, ctx.invoke, None, manager.session, manager)
    key = service.dump_draws(str(tmp_path), action_event_ids=[343], export_meshes=False)['job_id']
    deadline = time.monotonic() + 5
    while manager.status(key)['status'] not in v2.JOBS.TERMINAL and time.monotonic() < deadline:
        manager.pump()
        if callbacks:
            callbacks.pop(0)(controller)
        time.sleep(.005)
    status = manager.status(key)
    assert status['status'] == 'completed_with_errors', status
    assert len(saved) == 1 and Path(saved[0]).is_file()
    manifest = json.loads(Path(status['result']['summary_path']).read_text())
    entry = manifest['items'][0]
    assert entry['complete'] and not entry['ok']
    assert entry['error'].startswith('CONSTANT_EXPORT_FAILED')
    assert entry['constants'][0]['error'] == 'decode failed'
    assert entry['textures'][0]['export']['path'] == saved[0]
