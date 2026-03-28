"""
Parse utility functions for RenderDoc data types.
"""

import renderdoc as rd


class Parsers:
    """Parse utility functions (static methods)"""

    _STAGE_MAP = {
        "vertex": rd.ShaderStage.Vertex,
        "hull": rd.ShaderStage.Hull,
        "domain": rd.ShaderStage.Domain,
        "geometry": rd.ShaderStage.Geometry,
        "pixel": rd.ShaderStage.Pixel,
        "compute": rd.ShaderStage.Compute,
    }

    _STAGE_NAMES = {
        rd.ShaderStage.Vertex: "vertex",
        rd.ShaderStage.Hull: "hull",
        rd.ShaderStage.Domain: "domain",
        rd.ShaderStage.Geometry: "geometry",
        rd.ShaderStage.Pixel: "pixel",
        rd.ShaderStage.Compute: "compute",
    }

    @staticmethod
    def parse_stage(stage_str):
        """Convert stage string to ShaderStage enum"""
        stage_lower = stage_str.lower()
        if stage_lower not in Parsers._STAGE_MAP:
            raise ValueError("INVALID_STAGE: unknown shader stage: %s" % stage_str)
        return Parsers._STAGE_MAP[stage_lower]

    @staticmethod
    def stage_name(stage_value):
        """Convert a ShaderStage enum or string to canonical lowercase stage name"""
        if isinstance(stage_value, str):
            return Parsers.parse_stage_name(stage_value)
        return Parsers._STAGE_NAMES.get(stage_value, str(stage_value).lower())

    @staticmethod
    def parse_stage_name(stage_str):
        """Normalize stage string to canonical lowercase name"""
        stage_lower = stage_str.lower()
        if stage_lower not in Parsers._STAGE_MAP:
            raise ValueError("INVALID_STAGE: unknown shader stage: %s" % stage_str)
        return stage_lower

    @staticmethod
    def parse_resource_id(resource_id_str):
        """Parse resource ID string to ResourceId object"""
        # Handle formats like "ResourceId::123" or just "123"
        id_part = Parsers.extract_numeric_id(resource_id_str)
        try:
            rid = rd.ResourceId(id_part)
            if int(rid) == id_part:
                return rid
        except (TypeError, ValueError):
            pass

        rid = rd.ResourceId()
        rid.id = id_part
        return rid

    @staticmethod
    def canonical_resource_id(resource_id_value):
        """Convert a RenderDoc ResourceId or numeric/string id to canonical string form"""
        if hasattr(resource_id_value, "__int__"):
            try:
                return "ResourceId::%d" % int(resource_id_value)
            except (TypeError, ValueError):
                pass
        return "ResourceId::%d" % Parsers.extract_numeric_id(resource_id_value)

    @staticmethod
    def extract_numeric_id(resource_id_str):
        """Extract numeric ID from resource ID string"""
        if hasattr(resource_id_str, "__int__"):
            try:
                return int(resource_id_str)
            except (TypeError, ValueError):
                pass
        resource_id_text = str(resource_id_str)
        if "::" in resource_id_text:
            resource_id_text = resource_id_text.split("::")[-1]
        return int(resource_id_text)
