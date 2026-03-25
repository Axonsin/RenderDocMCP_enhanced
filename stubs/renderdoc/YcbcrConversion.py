# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class YcbcrConversion(__enum.IntEnum):
    """
    The color model conversion that a YCbCr sampler uses to convert from YCbCr to RGB.
    
    .. data:: Raw
    
      The input values are not converted at all.
    
    .. data:: RangeOnly
    
      There is no model conversion but the inputs are range expanded as for YCbCr.
    
    .. data:: BT709
    
      The conversion uses the BT.709 color model conversion.
    
    .. data:: BT601
    
      The conversion uses the BT.601 color model conversion.
    
    .. data:: BT2020
    
      The conversion uses the BT.2020 color model conversion.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    BT2020 = 4
    """ The conversion uses the BT.2020 color model conversion. """

    BT601 = 3
    """ The conversion uses the BT.601 color model conversion. """

    BT709 = 2
    """ The conversion uses the BT.709 color model conversion. """

    RangeOnly = 1
    """ There is no model conversion but the inputs are range expanded as for YCbCr. """

    Raw = 0
    """ The input values are not converted at all. """



