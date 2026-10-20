from enum import IntEnum

class TextureType(IntEnum):
    # Original docstring
    """
    The dimensionality of a texture binding.
    
    .. data:: Unknown
    
      An unknown type of texture.
    
    .. data:: Buffer
    
      A texel buffer.
    
    .. data:: Texture1D
    
      A 1D texture.
    
    .. data:: Texture1DArray
    
      A 1D texture array.
    
    .. data:: Texture2D
    
      A 2D texture.
    
    .. data:: TextureRect
    
      A rectangle texture, a legacy format for non-power of two textures.
    
    .. data:: Texture2DArray
    
      A 2D texture array.
    
    .. data:: Texture2DMS
    
      A multi-sampled 2D texture.
    
    .. data:: Texture2DMSArray
    
      A multi-sampled 2D texture array.
    
    .. data:: Texture3D
    
      A 3D texture.
    
    .. data:: TextureCube
    
      A Cubemap texture.
    
    .. data:: TextureCubeArray
    
      A Cubemap texture array.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown type of texture.
    """
    
    Buffer = 1
    """
    A texel buffer.
    """
    
    Texture1D = 2
    """
    A 1D texture.
    """
    
    Texture1DArray = 3
    """
    A 1D texture array.
    """
    
    Texture2D = 4
    """
    A 2D texture.
    """
    
    TextureRect = 5
    """
    A rectangle texture, a legacy format for non-power of two textures.
    """
    
    Texture2DArray = 6
    """
    A 2D texture array.
    """
    
    Texture2DMS = 7
    """
    A multi-sampled 2D texture.
    """
    
    Texture2DMSArray = 8
    """
    A multi-sampled 2D texture array.
    """
    
    Texture3D = 9
    """
    A 3D texture.
    """
    
    TextureCube = 10
    """
    A Cubemap texture.
    """
    
    TextureCubeArray = 11
    """
    A Cubemap texture array.
    """
    
    Count = 12
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

TextureType.Unknown.__doc__ = """
An unknown type of texture.
"""

TextureType.Buffer.__doc__ = """
A texel buffer.
"""

TextureType.Texture1D.__doc__ = """
A 1D texture.
"""

TextureType.Texture1DArray.__doc__ = """
A 1D texture array.
"""

TextureType.Texture2D.__doc__ = """
A 2D texture.
"""

TextureType.TextureRect.__doc__ = """
A rectangle texture, a legacy format for non-power of two textures.
"""

TextureType.Texture2DArray.__doc__ = """
A 2D texture array.
"""

TextureType.Texture2DMS.__doc__ = """
A multi-sampled 2D texture.
"""

TextureType.Texture2DMSArray.__doc__ = """
A multi-sampled 2D texture array.
"""

TextureType.Texture3D.__doc__ = """
A 3D texture.
"""

TextureType.TextureCube.__doc__ = """
A Cubemap texture.
"""

TextureType.TextureCubeArray.__doc__ = """
A Cubemap texture array.
"""

TextureType.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

TextureType.First.__doc__ = """
The first enum value, for ease of iteration.
"""

