# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class FilterFunction(__enum.IntEnum):
    """
    The function used to process the returned value after interpolation.
    
    .. data:: Normal
    
      No special processing is used, the value is returned directly to the shader.
    
    .. data:: Comparison
    
      The value from interpolation is compared to a reference value and the comparison result is
      returned to the shader.
    
    .. data:: Minimum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
      used instead to find the minimum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the min function.
    
    .. data:: Maximum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
      used instead to find the maximum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the max function.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Comparison = 1
    """
    The value from interpolation is compared to a reference value and the comparison result is
      returned to the shader.
    """

    Maximum = 3
    """
    Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
      used instead to find the maximum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the max function.
    """

    Minimum = 2
    """
    Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
      used instead to find the minimum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the min function.
    """

    Normal = 0
    """ No special processing is used, the value is returned directly to the shader. """



