# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CounterUnit(__enum.IntEnum):
    """
    The unit that GPU counter data is returned in.
    
    .. data:: Absolute
    
      The value is an absolute value and should be interpreted as unitless.
    
    .. data:: Seconds
    
      The value is a duration in seconds.
    
    .. data:: Percentage
    
      The value is a floating point percentage value between 0.0 and 1.0.
    
    .. data:: Ratio
    
      The value describes a ratio between two separate GPU units or counters.
    
    .. data:: Bytes
    
      The value is in bytes.
    
    .. data:: Cycles
    
      The value is a duration in clock cycles.
    
    .. data:: Hertz
    
      The value is a value in Hertz (cycles per second).
    
    .. data:: Volt
    
      The value is a value in Volts.
    
    .. data:: Celsius
    
      The value is a value in Celsius.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Absolute = 0
    """ The value is an absolute value and should be interpreted as unitless. """

    Bytes = 4
    """ The value is in bytes. """

    Celsius = 8
    """ The value is a value in Celsius. """

    Cycles = 5
    """ The value is a duration in clock cycles. """

    Hertz = 6
    """ The value is a value in Hertz (cycles per second). """

    Percentage = 2
    """ The value is a floating point percentage value between 0.0 and 1.0. """

    Ratio = 3
    """ The value describes a ratio between two separate GPU units or counters. """

    Seconds = 1
    """ The value is a duration in seconds. """

    Volt = 7
    """ The value is a value in Volts. """



