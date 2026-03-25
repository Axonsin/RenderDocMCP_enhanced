# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class QualityHint(__enum.IntEnum):
    """
    An API specific hint for a certain behaviour. A legacy concept in OpenGL that controls
    hints to the implementation where there is room for interpretation within the range of valid
    behaviour.
    
    .. data:: DontCare
    
      The hinted behaviour can follow any valid path as the implementation decides.
    
    .. data:: Nicest
    
      The hinted behaviour should follow the most correct or highest quality path.
    
    .. data:: Fastest
    
      The hinted behaviour should follow the most efficient path.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    DontCare = 0
    """ The hinted behaviour can follow any valid path as the implementation decides. """

    Fastest = 2
    """ The hinted behaviour should follow the most efficient path. """

    Nicest = 1
    """ The hinted behaviour should follow the most correct or highest quality path. """



