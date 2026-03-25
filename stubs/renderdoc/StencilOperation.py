# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class StencilOperation(__enum.IntEnum):
    """
    A stencil operation to apply in stencil processing.
    
    .. data:: Keep
    
      Keep the existing value unmodified.
    
    .. data:: Zero
    
      Set the value to ``0``.
    
    .. data:: Replace
    
      Replace the value with the stencil reference value.
    
    .. data:: IncSat
    
      Increment the value but saturate at the maximum representable value (typically ``255``).
    
    .. data:: DecSat
    
      Decrement the value but saturate at ``0``.
    
    .. data:: IncWrap
    
      Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``.
    
    .. data:: DecWrap
    
      Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``).
    
    .. data:: Invert
    
      Invert the bits in the stencil value (bitwise ``NOT``).
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    DecSat = 4
    """ Decrement the value but saturate at ``0``. """

    DecWrap = 6
    """ Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``). """

    IncSat = 3
    """ Increment the value but saturate at the maximum representable value (typically ``255``). """

    IncWrap = 5
    """ Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``. """

    Invert = 7
    """ Invert the bits in the stencil value (bitwise ``NOT``). """

    Keep = 0
    """ Keep the existing value unmodified. """

    Replace = 2
    """ Replace the value with the stencil reference value. """

    Zero = 1
    """ Set the value to ``0``. """



