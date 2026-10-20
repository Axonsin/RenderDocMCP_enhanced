"""Shallow ShaderVariable/ShaderConstant adapter using parameter-tree paths."""

from .resource_catalog import enum_name, paginate, validate_page
from .pipeline_snapshot import plain
from .structured_data import TEXT_LIMIT


VALUE_FIELDS = {
    "Float": "f32v", "Double": "f64v", "Half": "f16v",
    "Int": "s32v", "UInt": "u32v", "Bool": "u32v",
    "SLong": "s64v", "ULong": "u64v", "SShort": "s16v", "UShort": "u16v",
    "SByte": "s8v", "UByte": "u8v",
}


def read_variables(variables, declarations, path, offset, limit):
    validate_page(offset, limit)
    if not isinstance(path, list) or any(type(i) is not int or i < 0 for i in path):
        raise ValueError("INVALID_CHILD_PATH: expected non-negative child indices")

    # Each node holds a decoded value and its corresponding reflected layout.
    def children(node):
        value, declaration, array_element = node
        values = variables if value is None else value.members
        layouts = declarations if value is None else getattr(
            getattr(declaration, "type", None), "members", [])
        array = (value is not None and declaration is not None and
                 getattr(declaration.type, "elements", 1) > 1 and not array_element)
        return [(v, declaration if array else layouts[i] if i < len(layouts) else None,
                 array) for i, v in enumerate(values)]

    def serialize(node, current_path):
        value, declaration, array_element = node
        if value is None:
            return {"name": "variables", "child_path": current_path, "child_count": len(variables)}
        result = {"name": str(value.name)[:TEXT_LIMIT], "type": enum_name(value.type),
                  "rows": value.rows, "columns": value.columns,
                  "child_path": current_path, "child_count": len(value.members)}
        if len(str(value.name)) > TEXT_LIMIT:
            result["name_truncated"] = True
        if declaration is not None:
            typ = declaration.type
            result["layout"] = {
                "byte_offset": declaration.byteOffset,
                "offset_basis": "parent",
                "type_name": str(typ.name)[:TEXT_LIMIT],
                "array_elements": getattr(typ, "elements", None),
                "array_byte_stride": getattr(typ, "arrayByteStride", None),
                "matrix_byte_stride": getattr(typ, "matrixByteStride", None),
            }
            if array_element:
                result["layout"]["array_index"] = current_path[-1]
                result["layout"]["byte_offset"] += current_path[-1] * typ.arrayByteStride
        if not value.members:
            field = VALUE_FIELDS.get(enum_name(value.type))
            if field and hasattr(value.value, field):
                result["value"] = plain(list(getattr(value.value, field))[:value.rows * value.columns])
            else:
                result["value_available"] = False
        return result

    node = (None, None, False)
    for index in path:
        nodes = children(node)
        if index >= len(nodes):
            raise ValueError("INVALID_CHILD_PATH: child index out of range")
        node = nodes[index]
    nodes = children(node)
    page = paginate(nodes, offset, limit)
    page["items"] = [serialize(n, path + [offset + i]) for i, n in enumerate(page["items"])]
    return {"node": serialize(node, path), "children": page}
