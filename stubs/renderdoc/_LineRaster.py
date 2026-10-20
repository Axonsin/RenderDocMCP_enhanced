from enum import IntEnum

class LineRaster(IntEnum):
    # Original docstring
    """
    The line rasterization mode.
    
    .. data:: Default
    
      Default line rasterization mode as defined by the API specification.
    
    .. data:: Rectangular
    
      Lines are rasterized as rectangles extruded from the line.
    
    .. data:: Bresenham
    
      Lines are rasterized according to the bresenham line algorithm.
    
    .. data:: RectangularSmooth
    
      Lines are rasterized as rectangles extruded from the line with coverage falloff being
      implementation independent.
    
    .. data:: RectangularD3D
    
      Lines are rasterized as rectangles extruded from the line, but with a width of 1.4 according to
      legacy D3D behaviour
    """
    
    
    # Enum values
    
    Default = 0
    """
    Default line rasterization mode as defined by the API specification.
    """
    
    Rectangular = 1
    """
    Lines are rasterized as rectangles extruded from the line.
    """
    
    Bresenham = 2
    """
    Lines are rasterized according to the bresenham line algorithm.
    """
    
    RectangularSmooth = 3
    """
    Lines are rasterized as rectangles extruded from the line with coverage falloff being
    implementation independent.
    """
    
    RectangularD3D = 4
    """
    Lines are rasterized as rectangles extruded from the line, but with a width of 1.4 according to
    legacy D3D behaviour
    """
    

# Assign __doc__ for enum values for easier introspection

LineRaster.Default.__doc__ = """
Default line rasterization mode as defined by the API specification.
"""

LineRaster.Rectangular.__doc__ = """
Lines are rasterized as rectangles extruded from the line.
"""

LineRaster.Bresenham.__doc__ = """
Lines are rasterized according to the bresenham line algorithm.
"""

LineRaster.RectangularSmooth.__doc__ = """
Lines are rasterized as rectangles extruded from the line with coverage falloff being
implementation independent.
"""

LineRaster.RectangularD3D.__doc__ = """
Lines are rasterized as rectangles extruded from the line, but with a width of 1.4 according to
legacy D3D behaviour
"""

