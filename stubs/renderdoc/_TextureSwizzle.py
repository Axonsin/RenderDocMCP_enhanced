from enum import IntEnum

class TextureSwizzle(IntEnum):
    # Original docstring
    """
    A single source component for a destination texture swizzle.
    
    .. data:: Red
    
      The Red component.
    
    .. data:: Green
    
      The Green component.
    
    .. data:: Blue
    
      The Blue component.
    
    .. data:: Alpha
    
      The Alpha component.
    
    .. data:: Zero
    
      The fixed value ``0``.
    
    .. data:: One
    
      The fixed value ``1``.
    """
    
    
    # Enum values
    
    Red = 0
    """
    The Red component.
    """
    
    Green = 1
    """
    The Green component.
    """
    
    Blue = 2
    """
    The Blue component.
    """
    
    Alpha = 3
    """
    The Alpha component.
    """
    
    Zero = 4
    """
    The fixed value ``0``.
    """
    
    One = 5
    """
    The fixed value ``1``.
    """
    

# Assign __doc__ for enum values for easier introspection

TextureSwizzle.Red.__doc__ = """
The Red component.
"""

TextureSwizzle.Green.__doc__ = """
The Green component.
"""

TextureSwizzle.Blue.__doc__ = """
The Blue component.
"""

TextureSwizzle.Alpha.__doc__ = """
The Alpha component.
"""

TextureSwizzle.Zero.__doc__ = """
The fixed value ``0``.
"""

TextureSwizzle.One.__doc__ = """
The fixed value ``1``.
"""

