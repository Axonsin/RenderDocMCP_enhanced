from enum import IntEnum

class ConservativeRaster(IntEnum):
    # Original docstring
    """
    The conservative rasterization mode.
    
    .. data:: Disabled
    
      No conservative rasterization, the default rasterization coverage algorithm is used.
    
    .. data:: Underestimate
    
      Fragments will only be generated if the primitive full covers all parts of the pixel, including
      edges and corners.
    
    .. data:: Overestimate
    
      Fragments will be generated if the primitive covers any part of the pixel, including edges and
      corners.
    """
    
    
    # Enum values
    
    Disabled = 0
    """
    No conservative rasterization, the default rasterization coverage algorithm is used.
    """
    
    Underestimate = 1
    """
    Fragments will only be generated if the primitive full covers all parts of the pixel, including
    edges and corners.
    """
    
    Overestimate = 2
    """
    Fragments will be generated if the primitive covers any part of the pixel, including edges and
    corners.
    """
    

# Assign __doc__ for enum values for easier introspection

ConservativeRaster.Disabled.__doc__ = """
No conservative rasterization, the default rasterization coverage algorithm is used.
"""

ConservativeRaster.Underestimate.__doc__ = """
Fragments will only be generated if the primitive full covers all parts of the pixel, including
edges and corners.
"""

ConservativeRaster.Overestimate.__doc__ = """
Fragments will be generated if the primitive covers any part of the pixel, including edges and
corners.
"""

