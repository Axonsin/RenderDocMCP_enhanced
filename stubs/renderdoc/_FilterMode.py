from enum import IntEnum

class FilterMode(IntEnum):
    # Original docstring
    """
    The texture filtering mode for a given direction (minification, magnification, or
    between mips).
    
    .. data:: NoFilter
    
      No filtering - this direction is disabled or there is no sampler.
    
    .. data:: Point
    
      Point or nearest filtering - the closest pixel or mip level to the sample location is used.
    
    .. data:: Linear
    
      Linear filtering - a linear interpolation happens between the pixels or mips on either side of the
      sample location in each direction.
    
    .. data:: Cubic
    
      Similar to linear filtering but with a cubic curve used for interpolation instead of linear.
    
    .. data:: Anisotropic
    
      This sampler is using anisotropic filtering.
    """
    
    
    # Enum values
    
    NoFilter = 0
    """
    No filtering - this direction is disabled or there is no sampler.
    """
    
    Point = 1
    """
    Point or nearest filtering - the closest pixel or mip level to the sample location is used.
    """
    
    Linear = 2
    """
    Linear filtering - a linear interpolation happens between the pixels or mips on either side of the
    sample location in each direction.
    """
    
    Cubic = 3
    """
    Similar to linear filtering but with a cubic curve used for interpolation instead of linear.
    """
    
    Anisotropic = 4
    """
    This sampler is using anisotropic filtering.
    """
    

# Assign __doc__ for enum values for easier introspection

FilterMode.NoFilter.__doc__ = """
No filtering - this direction is disabled or there is no sampler.
"""

FilterMode.Point.__doc__ = """
Point or nearest filtering - the closest pixel or mip level to the sample location is used.
"""

FilterMode.Linear.__doc__ = """
Linear filtering - a linear interpolation happens between the pixels or mips on either side of the
sample location in each direction.
"""

FilterMode.Cubic.__doc__ = """
Similar to linear filtering but with a cubic curve used for interpolation instead of linear.
"""

FilterMode.Anisotropic.__doc__ = """
This sampler is using anisotropic filtering.
"""

