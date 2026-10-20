from enum import IntEnum

class FillMode(IntEnum):
    # Original docstring
    """
    The fill mode for polygons.
    
    .. data:: Solid
    
      Polygons are filled in and rasterized solidly.
    
    .. data:: Wireframe
    
      Polygons are rendered only with lines along their edges, forming a wireframe.
    
    .. data:: Point
    
      Only the points at the polygons vertices are rendered.
    """
    
    
    # Enum values
    
    Solid = 0
    """
    Polygons are filled in and rasterized solidly.
    """
    
    Wireframe = 1
    """
    Polygons are rendered only with lines along their edges, forming a wireframe.
    """
    
    Point = 2
    """
    Only the points at the polygons vertices are rendered.
    """
    

# Assign __doc__ for enum values for easier introspection

FillMode.Solid.__doc__ = """
Polygons are filled in and rasterized solidly.
"""

FillMode.Wireframe.__doc__ = """
Polygons are rendered only with lines along their edges, forming a wireframe.
"""

FillMode.Point.__doc__ = """
Only the points at the polygons vertices are rendered.
"""

