"""Bounded, one-level serialization of RenderDoc structured initialization data."""

import math

import renderdoc as rd

from .resource_catalog import enum_name, identity, validate_page


TEXT_LIMIT = 4096


def _text(result, field, value):
    value = str(value)
    result[field] = value[:TEXT_LIMIT]
    if len(value) > TEXT_LIMIT:
        result[field + "_truncated"] = True
        result[field + "_length"] = len(value)


def visible_children(node):
    for index in range(node.NumChildren()):
        child = node.GetChild(index)
        if not child.type.flags & rd.SDTypeFlags.Hidden:
            yield index, child


def serialize_node(node, path, ctx, catalog):
    basic = enum_name(node.type.basetype)
    result = {
        "name": str(node.name), "type": str(node.type.name), "basic_type": basic,
        "child_path": list(path), "child_count": node.NumChildren(),
    }
    if basic in ("Chunk", "Struct", "Array"):
        pass
    elif basic == "Null":
        result["value"] = None
    elif basic == "Buffer":
        result["byte_size"] = int(node.type.byteSize)
        result["content_omitted"] = True
    elif basic == "Resource":
        result["value"] = identity(ctx, node.AsResourceId(), catalog)
    elif basic in ("UnsignedInteger", "Enum", "GPUAddress"):
        result["value"] = int(node.data.basic.u)
    elif basic == "SignedInteger":
        result["value"] = int(node.data.basic.i)
    elif basic == "Float":
        value = float(node.AsFloat())
        result["value"] = value if math.isfinite(value) else None
        if not math.isfinite(value):
            result["non_finite"] = str(value)
    elif basic == "Boolean":
        result["value"] = bool(node.AsBool())
    elif basic == "Character":
        _text(result, "value", node.data.basic.c)
    elif basic == "String":
        _text(result, "value", node.AsString())
    else:
        result["value_unavailable"] = True
    if node.type.flags & rd.SDTypeFlags.HasCustomString:
        _text(result, "display_value", node.data.string)
    return result


def read_node(chunk, child_path, ctx, catalog, offset, limit):
    validate_page(offset, limit)
    if (not isinstance(child_path, list) or
            any(type(i) is not int or i < 0 for i in child_path)):
        raise ValueError("INVALID_CHILD_PATH: expected non-negative child indices")
    node = chunk
    for index in child_path:
        if index >= node.NumChildren():
            raise ValueError("INVALID_CHILD_PATH: child index out of range")
        node = node.GetChild(index)
    # Only serialize the requested page; large arrays stay bounded.
    items = []
    total = 0
    for index, child in visible_children(node):
        if offset <= total < offset + limit:
            items.append(serialize_node(child, child_path + [index], ctx, catalog))
        total += 1
    page = {"items": items, "offset": offset, "limit": limit, "total_count": total,
            "returned_count": len(items), "has_more": offset + len(items) < total}
    return {"node": serialize_node(node, child_path, ctx, catalog), "children": page}
