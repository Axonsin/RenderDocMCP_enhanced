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


def test_verified_batch_can_repair_a_corrupt_content_addressed_constant(tmp_path):
    records=[dict(binding_key='binding',stage='fragment',status='exported',values_status='exported',_raw=b'captured bytes')]
    result=v2.CONSTANT_EXPORT.write_constants(str(tmp_path),records,{},'e1')[0]
    path=Path(result['raw']['path']);path.write_bytes(b'corrupt')
    with pytest.raises(RuntimeError,match='ARTIFACT_HASH_MISMATCH'):
        v2.CONSTANT_EXPORT.write_constants(str(tmp_path),records,{},'e1')
    repaired=v2.CONSTANT_EXPORT.write_constants(str(tmp_path),records,{},'e1',repair_corrupt=True)[0]
    assert path.read_bytes()==b'captured bytes' and repaired['raw']['sha256']==result['raw']['sha256']
