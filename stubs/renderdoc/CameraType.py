# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CameraType(__enum.IntEnum):
    """
    The type of camera controls for an :class:`Camera`.
    
    .. data:: Arcball
    
      Arcball controls that rotate and zoom around the origin point.
    
    .. data:: FPSLook
    
      Traditional FPS style controls with movement in each axis relative to the current look direction.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Arcball = 0
    """ Arcball controls that rotate and zoom around the origin point. """

    FPSLook = 1
    """ Traditional FPS style controls with movement in each axis relative to the current look direction. """



