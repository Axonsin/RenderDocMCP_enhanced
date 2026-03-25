# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ChromaSampleLocation(__enum.IntEnum):
    """
    Determines where in the pixel downsampled chrome samples are positioned.
    
    .. data:: CositedEven
    
      The chroma samples are positioned exactly in the same place as the even luma co-ordinates.
    
    .. data:: Midpoint
    
      The chrome samples are positioned half way between each even luma sample and the next highest odd
      luma sample.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    CositedEven = 0
    """ The chroma samples are positioned exactly in the same place as the even luma co-ordinates. """

    Midpoint = 1
    """
    The chrome samples are positioned half way between each even luma sample and the next highest odd
      luma sample.
    """



