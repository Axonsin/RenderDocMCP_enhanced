# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureCategory(__enum.IntFlag):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    ColorTarget = 2
    """ The texture will be written to as a color target. """

    DepthTarget = 4
    """ The texture will be written to and tested against as a depth target. """

    NoFlags = 0
    """ The texture will not be used for any of the uses below. """

    ShaderRead = 1
    """ The texture will be read by a shader. """

    ShaderReadWrite = 8
    """ The texture will be read and written to by a shader. """

    SwapBuffer = 16
    """ The texture is part of a window swapchain. """



