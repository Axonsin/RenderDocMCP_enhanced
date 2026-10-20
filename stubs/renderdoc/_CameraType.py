from enum import IntEnum

class CameraType(IntEnum):
    # Original docstring
    """
    The type of camera controls for an :class:`Camera`.
    
    .. data:: Arcball
    
      Arcball controls that rotate and zoom around the origin point.
    
    .. data:: FPSLook
    
      Traditional FPS style controls with movement in each axis relative to the current look direction.
    """
    
    
    # Enum values
    
    Arcball = 0
    """
    Arcball controls that rotate and zoom around the origin point.
    """
    
    FPSLook = 1
    """
    Traditional FPS style controls with movement in each axis relative to the current look direction.
    """
    

# Assign __doc__ for enum values for easier introspection

CameraType.Arcball.__doc__ = """
Arcball controls that rotate and zoom around the origin point.
"""

CameraType.FPSLook.__doc__ = """
Traditional FPS style controls with movement in each axis relative to the current look direction.
"""

