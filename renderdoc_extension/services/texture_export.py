"""Raw texture layout, aspect/ROI selection and bounded file transport."""
import base64
import hashlib
import json
import os
import struct
import tempfile
import uuid
from .texture_values import decoder, validate_region, MAX_SUBRESOURCE_BYTES

INLINE_LIMIT = 256 * 1024

def select(data, fmt, width, height, depth, aspect='all', region=None, verified_api=True):
    if aspect not in ('all', 'depth', 'stencil'):
        raise ValueError('INVALID_ASPECT: expected all, depth or stencil')
    if len(data) > MAX_SUBRESOURCE_BYTES:
        raise ValueError('RESOURCE_LIMIT: raw subresource exceeds 64 MiB')
    info = {'source_format': fmt.Name(), 'output_format': fmt.Name(), 'endianness': 'little',
            'coordinate_origin': 'top_left', 'value_domain': 'storage', 'aspect': aspect,
            'layout_available': False, 'layout': 'opaque', 'row_pitch': None, 'slice_pitch': None,
            'channel_layout': None}
    if not verified_api:
        if aspect != "all" or region is not None:
            raise ValueError("UNSUPPORTED_FORMAT: raw coordinate layout not verified for this API")
        info.update(coordinate_origin=None, endianness=None)
        return data, info, width, height
    try:
        size, count, read = decoder(fmt, aspect)
    except (ValueError, AttributeError):
        if aspect != 'all' or region is not None:
            raise ValueError('UNSUPPORTED_FORMAT: unverified texture selection/layout')
        return data, info, width, height
    expected = width*height*depth*size
    if len(data) != expected:
        raise ValueError('RESOURCE_QUERY_FAILED: raw layout/length mismatch %d != %d' % (len(data), expected))
    x, y, w, h = (0, 0, width, height) if region is None else validate_region(region, width, height)
    name = fmt.Name().upper()
    channel = {'format': fmt.Name(), 'components': count,
               'component_byte_width': getattr(fmt, 'compByteWidth', None),
               'component_type': str(getattr(fmt, 'compType', '')).split('.')[-1],
               'bgra_order': bool(fmt.BGRAOrder()) if hasattr(fmt, 'BGRAOrder') else False}
    if name.startswith('D24'):
        channel = {'depth': {'bit_offset': 0, 'bits': 24, 'encoding': 'UNorm'},
                   'stencil': {'bit_offset': 24, 'bits': 8, 'encoding': 'UInt'}}
    elif name.startswith('D16'):
        channel = {'depth': {'bit_offset': 0, 'bits': 16, 'encoding': 'UNorm'}}
    kind = str(getattr(getattr(fmt, 'type', None), 'name', getattr(fmt, 'type', '')))
    if kind in ('R10G10B10A2', 'R11G11B10'):
        widths = [10,10,10,2] if kind == 'R10G10B10A2' else [11,11,10]
        offset = 0
        channel = []
        for component, bits in zip('RGBA', widths):
            channel.append({'channel':component, 'bit_offset':offset, 'bits':bits,
                            'encoding':str(getattr(fmt.compType, 'name', fmt.compType))})
            offset += bits
    info.update(source_channel_layout=channel, source_row_pitch=width*size,
                source_slice_pitch=width*height*size)
    if aspect == 'all':
        if region is not None:
            data = b''.join(data[((z*height+yy)*width+x)*size:((z*height+yy)*width+x+w)*size]
                            for z in range(depth) for yy in range(y, y+h))
        output_size = size
    else:
        output = bytearray()
        for z in range(depth):
            for yy in range(y, y+h):
                for xx in range(x, x+w):
                    value = read(data, ((z*height+yy)*width+xx)*size, 'storage')[0]
                    output.extend(struct.pack('<f' if aspect == 'depth' else '<B', value))
        data = bytes(output)
        output_size = 4 if aspect == 'depth' else 1
        info['output_format'] = 'R32_FLOAT' if aspect == 'depth' else 'R8_UINT'
        channel = {'components': 1, 'encoding': 'normalized_float32' if aspect == 'depth' else 'uint8'}
    info.update(layout_available=True, layout='tightly_packed', channel_layout=channel,
                row_pitch=w*output_size, slice_pitch=w*h*output_size, region=region)
    return data, info, w, h

def transport(data, metadata, output_mode='auto', output_dir=None, session='unknown'):
    if output_mode not in ('auto', 'inline', 'file'):
        raise ValueError('INVALID_REQUEST: output_mode must be auto, inline or file')
    if output_dir is not None and (not isinstance(output_dir, str) or not os.path.isabs(output_dir)):
        raise ValueError('INVALID_OUTPUT_PATH: output_dir must be absolute')
    metadata.update(data_length=len(data), sha256=hashlib.sha256(data).hexdigest())
    if output_mode == 'inline' and len(data) > INLINE_LIMIT:
        raise ValueError('RESOURCE_LIMIT: inline payload exceeds 256 KiB; use file or auto')
    if output_mode == 'inline' or (output_mode == 'auto' and len(data) <= INLINE_LIMIT):
        metadata.update(output_mode='inline', content_base64=base64.b64encode(data).decode('ascii'))
        return metadata
    folder = os.path.join(output_dir or os.path.join(tempfile.gettempdir(), 'renderdoc_mcp', 'artifacts'),
                          session, uuid.uuid4().hex)
    os.makedirs(folder, exist_ok=False)
    path = os.path.join(folder, 'texture.bin')
    with open(path, 'wb') as handle:
        handle.write(data)
    metadata.update(output_mode='file', path=path, size_bytes=len(data), metadata_path=os.path.join(folder, 'texture.json'))
    with open(metadata['metadata_path'], 'w', encoding='utf-8') as handle:
        json.dump(metadata, handle, ensure_ascii=False, allow_nan=False, indent=2)
    return metadata
