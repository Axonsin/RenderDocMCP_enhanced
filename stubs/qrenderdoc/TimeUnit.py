# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TimeUnit(__enum.IntEnum):
    """
    The unit that GPU durations are displayed in.
    
    .. data:: Seconds
    
      The durations are displayed as seconds (s).
    
    .. data:: Milliseconds
    
      The durations are displayed as milliseconds (ms).
    
    .. data:: Microseconds
    
      The durations are displayed as microseconds (µs).
    
    .. data:: Nanoseconds
    
      The durations are displayed as nanoseconds (ns).
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Count = 4
    Microseconds = 2
    """ The durations are displayed as microseconds (µs). """

    Milliseconds = 1
    """ The durations are displayed as milliseconds (ms). """

    Nanoseconds = 3
    """ The durations are displayed as nanoseconds (ns). """

    Seconds = 0
    """ The durations are displayed as seconds (s). """



