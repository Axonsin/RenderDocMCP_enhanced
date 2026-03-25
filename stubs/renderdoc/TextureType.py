# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureType(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Buffer = 1
    """ A texel buffer. """

    Count = 12
    First = 0
    Texture1D = 2
    """ A 1D texture. """

    Texture1DArray = 3
    """ A 1D texture array. """

    Texture2D = 4
    """ A 2D texture. """

    Texture2DArray = 6
    """ A 2D texture array. """

    Texture2DMS = 7
    """ A multi-sampled 2D texture. """

    Texture2DMSArray = 8
    """ A multi-sampled 2D texture array. """

    Texture3D = 9
    """ A 3D texture. """

    TextureCube = 10
    """ A Cubemap texture. """

    TextureCubeArray = 11
    """ A Cubemap texture array. """

    TextureRect = 5
    """ A rectangle texture, a legacy format for non-power of two textures. """

    Unknown = 0
    """ An unknown type of texture. """



