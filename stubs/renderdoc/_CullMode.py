from enum import IntEnum

class CullMode(IntEnum):
    # Original docstring
    """
    The culling mode for polygons.
    
    .. data:: NoCull
    
      No polygon culling is performed.
    
    .. data:: Front
    
      Front-facing polygons are culled.
    
    .. data:: Back
    
      Back-facing polygons are culled.
    
    .. data:: FrontAndBack
    
      Both front-facing and back-facing polygons are culled.
    """
    
    
    # Enum values
    
    NoCull = 0
    """
    No polygon culling is performed.
    """
    
    Front = 1
    """
    Front-facing polygons are culled.
    """
    
    Back = 2
    """
    Back-facing polygons are culled.
    """
    
    FrontAndBack = 3
    """
    Both front-facing and back-facing polygons are culled.
    """
    

# Assign __doc__ for enum values for easier introspection

CullMode.NoCull.__doc__ = """
No polygon culling is performed.
"""

CullMode.Front.__doc__ = """
Front-facing polygons are culled.
"""

CullMode.Back.__doc__ = """
Back-facing polygons are culled.
"""

CullMode.FrontAndBack.__doc__ = """
Both front-facing and back-facing polygons are culled.
"""

