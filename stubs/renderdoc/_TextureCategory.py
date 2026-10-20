from enum import IntFlag

class TextureCategory(IntFlag):
    # Original docstring
    """
    A set of flags describing how this texture may be used
    
    .. data:: NoFlags
    
      The texture will not be used for any of the uses below.
    
    .. data:: ShaderRead
    
      The texture will be read by a shader.
    
    .. data:: ColorTarget
    
      The texture will be written to as a color target.
    
    .. data:: DepthTarget
    
      The texture will be written to and tested against as a depth target.
    
    .. data:: ShaderReadWrite
    
      The texture will be read and written to by a shader.
    
    .. data:: SwapBuffer
    
      The texture is part of a window swapchain.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    The texture will not be used for any of the uses below.
    """
    
    ShaderRead = 1
    """
    The texture will be read by a shader.
    """
    
    ColorTarget = 2
    """
    The texture will be written to as a color target.
    """
    
    DepthTarget = 4
    """
    The texture will be written to and tested against as a depth target.
    """
    
    ShaderReadWrite = 8
    """
    The texture will be read and written to by a shader.
    """
    
    SwapBuffer = 16
    """
    The texture is part of a window swapchain.
    """
    

# Assign __doc__ for enum values for easier introspection

TextureCategory.NoFlags.__doc__ = """
The texture will not be used for any of the uses below.
"""

TextureCategory.ShaderRead.__doc__ = """
The texture will be read by a shader.
"""

TextureCategory.ColorTarget.__doc__ = """
The texture will be written to as a color target.
"""

TextureCategory.DepthTarget.__doc__ = """
The texture will be written to and tested against as a depth target.
"""

TextureCategory.ShaderReadWrite.__doc__ = """
The texture will be read and written to by a shader.
"""

TextureCategory.SwapBuffer.__doc__ = """
The texture is part of a window swapchain.
"""

