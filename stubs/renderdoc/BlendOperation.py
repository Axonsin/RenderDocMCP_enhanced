# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BlendOperation(__enum.IntEnum):
    """
    A blending operation to apply in color blending.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "destination" value is the value in the target being blended to.
    
      These values are multiplied by a given blend factor, see :class:`BlendMultiplier`.
    
    .. data:: Add
    
      Add the two values being processed together.
    
    .. data:: Subtract
    
      Subtract the destination value from the source value.
    
    .. data:: ReversedSubtract
    
      Subtract the source value from the destination value.
    
    .. data:: Minimum
    
      The minimum of the source and destination value.
    
    .. data:: Maximum
    
      The maximum of the source and destination value.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Add = 0
    """ Add the two values being processed together. """

    Maximum = 4
    """ The maximum of the source and destination value. """

    Minimum = 3
    """ The minimum of the source and destination value. """

    ReversedSubtract = 2
    """ Subtract the source value from the destination value. """

    Subtract = 1
    """ Subtract the destination value from the source value. """



