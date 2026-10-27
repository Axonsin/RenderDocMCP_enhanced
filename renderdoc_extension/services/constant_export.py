"""Event-bound constant evidence shared by draw and shader exports."""
import hashlib
import os
from .job_service import atomic_json
from .shader_variables import VALUE_FIELDS, reflected_layout
from .native_serialization import plain
from .resource_catalog import enum_name

MAX_BYTES = 64 * 1024 * 1024

def full_value(value):
    result = {'name': str(value.name), 'type': enum_name(value.type), 'rows': value.rows,
              'columns': value.columns, 'value_order': 'row_major' if value.rows > 1 and value.columns > 1 else 'component_order'}
    if value.members:
        result['members'] = [full_value(v) for v in value.members]
    else:
        field = VALUE_FIELDS.get(enum_name(value.type))
        if not field or not hasattr(value.value, field):
            raise ValueError('CONSTANT_DECODE_UNAVAILABLE: unsupported scalar type ' + result['type'])
        result['value'] = plain(list(getattr(value.value, field))[:value.rows*value.columns])
    return result

def read_constants(snapshot, stage_filter=None):
    records = []
    for row in snapshot.bindings:
        if row['category'] != 'constant' or (stage_filter and row['stage'] != stage_filter):
            continue
        record = {'binding_key': row['binding_key'], 'stage': row['stage'], 'location': row['location'],
                  'resource': row.get('resource'), 'action_event_id': snapshot.event_id,
                  'event_phase': 'after', 'source': 'event_bound_constant', 'status': 'pending'}
        records.append(record)
        if not row['bound']:
            record.update(status='skipped', reason='unbound')
            continue
        try:
            stage, index, array_element, reflection, declaration = snapshot.variable_sources[row['binding_key']]
            descriptor = snapshot.pipe.GetConstantBlock(stage, index, array_element).descriptor
            size = row.get('provided_bytes')
            if size is None:
                size = getattr(declaration, 'byteSize', 0)
            offset = int(descriptor.byteOffset)
            size = int(size)
            if size < 0 or size > MAX_BYTES:
                raise ValueError('RESOURCE_LIMIT: constant binding exceeds 64 MiB')
            record.update(byte_offset=offset, byte_size=size, buffer_backed=row.get('buffer_backed', True))
            name = row.get('binding_name', '') or getattr(declaration, 'name', '')
            record['raw'] = {'status': 'unavailable', 'binding_name': name,
                             'expected_bytes': size, 'actual_bytes': None}
            try:
                if record['buffer_backed']:
                    raw = bytes(snapshot.controller.GetBufferData(descriptor.resource, offset, size)) if size else b''
                elif snapshot.api == 'Vulkan' and hasattr(snapshot.native, 'pushconsts'):
                    raw = bytes(snapshot.native.pushconsts)[offset:offset+size]
                else:
                    raise ValueError('CONSTANT_RAW_UNAVAILABLE: direct storage not verified for this API')
                record['raw']['actual_bytes'] = len(raw)
                if len(raw) != size:
                    raise ValueError('RESOURCE_QUERY_FAILED: constant short read for %s (expected %d bytes, actual %d bytes)' %
                                     (name, size, len(raw)))
                record['_raw'] = raw
                record['raw']['status'] = 'exported'
            except Exception as exc:
                record['raw']['reason'] = str(exc)
            if declaration is None or reflection is None:
                raise ValueError('CONSTANT_DECODE_UNAVAILABLE: reflection unavailable')
            record['layout'] = reflected_layout(declaration.variables)
            pipeline = snapshot.pipe.GetComputePipelineObject() if row['stage'] == 'compute' else snapshot.pipe.GetGraphicsPipelineObject()
            values = snapshot.controller.GetCBufferVariableContents(pipeline, snapshot.pipe.GetShader(stage),
                stage, snapshot.pipe.GetShaderEntryPoint(stage), index, descriptor.resource, offset, size)
            record['values'] = [full_value(v) for v in values]
            if declaration.variables and not values:
                raise ValueError('CONSTANT_DECODE_UNAVAILABLE: empty decoded constant tree')
            record.update(status='exported', values_status='exported')
        except Exception as exc:
            record.update(status='failed', values_status='failed', error=str(exc))
    return records

def write_constants(directory, records, provenance, label):
    folder = os.path.join(directory, 'constants')
    os.makedirs(folder, exist_ok=True)
    result = []
    for index, source in enumerate(records):
        row = dict(source)
        raw = row.pop('_raw', None)
        row['provenance'] = provenance
        if raw is not None:
            digest = hashlib.sha256(raw).hexdigest()
            path = os.path.join(folder, digest+'.bin')
            if os.path.isfile(path):
                with open(path, "rb") as handle:
                    if hashlib.sha256(handle.read()).hexdigest() != digest:
                        raise RuntimeError("ARTIFACT_HASH_MISMATCH: existing constant blob is corrupt")
            else:
                temporary = path+'.tmp'
                with open(temporary, 'wb') as handle:
                    handle.write(raw)
                os.replace(temporary, path)
            row.setdefault('raw', {}).update(path=path, sha256=digest, size_bytes=len(raw))
        path = os.path.join(folder, '%s_%d.json' % (label, index))
        atomic_json(path, row)
        with open(path, 'rb') as handle:
            payload = handle.read()
        result.append({k: row[k] for k in ('binding_key', 'stage', 'status', 'values_status', 'error', 'reason', 'raw') if k in row})
        result[-1].update(details_path=path, sha256=hashlib.sha256(payload).hexdigest(), size_bytes=len(payload))
    return result
