from enum import IntEnum

class AlphaMapping(IntEnum):
    # Original docstring
    """
    What to do with the alpha channel from a texture while saving out to a file.
    
    .. data:: Discard
    
      Completely discard the alpha channel and only write RGB to the file.
    
    .. data:: BlendToColor
    
      Blend to the primary background color using alpha.
    
    .. data:: BlendToCheckerboard
    
      Blend to a checkerboard pattern with the primary and secondary background colors.
    
    .. data:: Preserve
    
      Preserve the alpha channel and save it to the file by itself.
    
      This is only valid for file formats that support alpha channels.
    """
    
    
    # Enum values
    
    Discard = 0
    """
    Completely discard the alpha channel and only write RGB to the file.
    """
    
    BlendToColor = 1
    """
    Blend to the primary background color using alpha.
    """
    
    BlendToCheckerboard = 2
    """
    Blend to a checkerboard pattern with the primary and secondary background colors.
    """
    
    Preserve = 3
    """
    Preserve the alpha channel and save it to the file by itself.
    
    This is only valid for file formats that support alpha channels.
    """
    
    Count = 4
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

AlphaMapping.Discard.__doc__ = """
Completely discard the alpha channel and only write RGB to the file.
"""

AlphaMapping.BlendToColor.__doc__ = """
Blend to the primary background color using alpha.
"""

AlphaMapping.BlendToCheckerboard.__doc__ = """
Blend to a checkerboard pattern with the primary and secondary background colors.
"""

AlphaMapping.Preserve.__doc__ = """
Preserve the alpha channel and save it to the file by itself.

This is only valid for file formats that support alpha channels.
"""

AlphaMapping.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

AlphaMapping.First.__doc__ = """
The first enum value, for ease of iteration.
"""

