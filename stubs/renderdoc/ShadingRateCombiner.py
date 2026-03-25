# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShadingRateCombiner(__enum.IntEnum):
    """
    A combiner to apply when determining a pixel shading rate.
    
    .. data:: Keep
    
      Keep the first input to the combiner.
    
    .. data:: Passthrough
    
      Keep the first input to the combiner. Alias for :data:`Keep`, for D3D terminology.
    
    .. data:: Replace
    
      Replace with the second input to the combiner.
    
    .. data:: Override
    
      Replace with the second input to the combiner. Alias for :data:`Replace`, for D3D terminology.
    
    .. data:: Min
    
      Use the minimum (finest rate) of the two inputs.
    
    .. data:: Max
    
      Use the maximum (coarsest rate) of the two inputs.
    
    .. data:: Multiply
    
      Multiply the two rates together (e.g. 1x1 and 1x2 = 1x2, 2x2 and 2x2 = 4x4). Note that D3D names
      this 'sum' misleadingly.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Keep = 0
    """ Keep the first input to the combiner. """

    Max = 3
    """ Use the maximum (coarsest rate) of the two inputs. """

    Min = 2
    """ Use the minimum (finest rate) of the two inputs. """

    Multiply = 4
    """
    Multiply the two rates together (e.g. 1x1 and 1x2 = 1x2, 2x2 and 2x2 = 4x4). Note that D3D names
      this 'sum' misleadingly.
    """

    Override = 1
    """ Replace with the second input to the combiner. Alias for :data:`Replace`, for D3D terminology. """

    Passthrough = 0
    """ Keep the first input to the combiner. Alias for :data:`Keep`, for D3D terminology. """

    Replace = 1
    """ Replace with the second input to the combiner. """



