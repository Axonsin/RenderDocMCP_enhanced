"""Request-local resource identities and queries shared by resource tools."""

import re

from ..utils import Parsers


def enum_name(value):
    return getattr(value, "name", str(value).split(".")[-1])


def resource_type(value):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", enum_name(value)).lower()


def validate_page(offset, limit):
    if (type(offset) is not int or offset < 0 or
            type(limit) is not int or not 1 <= limit <= 500):
        raise ValueError("INVALID_PAGINATION: offset >= 0 and 1 <= limit <= 500 required")


def paginate(items, offset, limit):
    validate_page(offset, limit)
    page = items[offset:offset + limit]
    return {
        "items": page, "total_count": len(items), "offset": offset, "limit": limit,
        "returned_count": len(page), "has_more": offset + len(page) < len(items),
    }


def build_catalog(controller, descriptors=True):
    # Never silently turn a failed enumeration into an empty capture.
    catalog = {
        "resources": {int(r.resourceId): r for r in controller.GetResources()},
        "textures": {}, "buffers": {}, "cache": {},
    }
    if descriptors:
        catalog["textures"] = {int(r.resourceId): r for r in controller.GetTextures()}
        catalog["buffers"] = {int(r.resourceId): r for r in controller.GetBuffers()}
    return catalog


def resolve_resource(resource_id, catalog):
    try:
        numeric = Parsers.extract_numeric_id(resource_id)
    except (TypeError, ValueError):
        raise ValueError("INVALID_RESOURCE_ID: %s" % resource_id)
    resource = catalog["resources"].get(numeric)
    if resource is None:
        raise ValueError("RESOURCE_NOT_FOUND: %s" % resource_id)
    return resource


def identity(ctx, resource_id, catalog):
    numeric = Parsers.extract_numeric_id(resource_id)
    desc = catalog["resources"].get(numeric)
    raw_id = desc.resourceId if desc is not None else resource_id
    try:
        name = ctx.GetResourceName(raw_id)
    except Exception:
        name = desc.name if desc is not None else ""
    result = {
        "resource_id": Parsers.canonical_resource_id(raw_id),
        "name": str(name),
        "resource_type": resource_type(desc.type) if desc is not None else "unknown",
    }
    if desc is None:
        result["missing"] = True
    return result


def query_usage(controller, resource, catalog):
    """Return availability separately from successful but empty static usage."""
    numeric = int(resource.resourceId)
    if numeric not in catalog["textures"] and numeric not in catalog["buffers"]:
        return {"available": False, "reason": "unsupported_resource_type"}, []
    try:
        return {"available": True}, list(controller.GetUsage(resource.resourceId))
    except Exception as exc:
        raise ValueError("RESOURCE_QUERY_FAILED: %s" % exc)
