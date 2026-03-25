# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class AlphaMapping(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    BlendToCheckerboard = 2
    """ Blend to a checkerboard pattern with the primary and secondary background colors. """

    BlendToColor = 1
    """ Blend to the primary background color using alpha. """

    Count = 4
    Discard = 0
    """ Completely discard the alpha channel and only write RGB to the file. """

    First = 0
    Preserve = 3
    """
    Preserve the alpha channel and save it to the file by itself.
    
      This is only valid for file formats that support alpha channels.
    """



