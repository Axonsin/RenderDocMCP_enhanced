# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderEvents(__enum.IntFlag):
    """
    A set of flags for events that may occur while debugging a shader
    
    .. data:: NoEvent
    
      No event has occurred.
    
    .. data:: SampleLoadGather
    
      A texture was sampled, loaded or gathered.
    
    .. data:: GeneratedNanOrInf
    
      A floating point operation generated a ``NaN`` or ``infinity`` result.
    
    .. data:: DebugBreak
    
      A debugbreak event was emitted.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    DebugBreak = 4
    """ A debugbreak event was emitted. """

    GeneratedNanOrInf = 2
    """ A floating point operation generated a ``NaN`` or ``infinity`` result. """

    NoEvent = 0
    """ No event has occurred. """

    SampleLoadGather = 1
    """ A texture was sampled, loaded or gathered. """



