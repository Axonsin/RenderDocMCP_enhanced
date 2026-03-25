# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ReplayOutputType(__enum.IntEnum):
    """
    The type of :class:`ReplayOutput` to create
    
    .. data:: Headless
    
      A headless output that does nothing to display to windows but can still be controlled and
      queried the same way
    
    .. data:: Texture
    
      An output that is used for displaying textures, thumbnails and pixel context
    
    .. data:: Mesh
    
      An output that will display mesh data previews
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Headless = 0
    """
    A headless output that does nothing to display to windows but can still be controlled and
      queried the same way
    """

    Mesh = 2
    """ An output that will display mesh data previews """

    Texture = 1
    """ An output that is used for displaying textures, thumbnails and pixel context """



