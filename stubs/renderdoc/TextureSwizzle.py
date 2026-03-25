# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureSwizzle(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Alpha = 3
    """ The Alpha component. """

    Blue = 2
    """ The Blue component. """

    Green = 1
    """ The Green component. """

    One = 5
    """ The fixed value ``1``. """

    Red = 0
    """ The Red component. """

    Zero = 4
    """ The fixed value ``0``. """



