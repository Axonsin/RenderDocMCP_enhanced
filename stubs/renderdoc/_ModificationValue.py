from ._PixelValue import PixelValue

from typing import overload

class ModificationValue():
    # Original docstring
    """
    The value of pixel output at a particular event.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ModificationValue.
        """
        pass
    
    @overload
    def __init__(self, other: 'ModificationValue'):
        """
        Construct a new ModificationValue with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def IsValid(self) -> bool:
        """
        :return: Returns whether or not this modification value is valid.
        :rtype: bool
        """
        pass
    
    
    def SetInvalid(self):
        """
        Sets this modification value to be invalid.
        """
        pass
    
    @property
    def depth(self) -> float:
        """
        The depth value.
        
        If depth is not available/in-use for this modification, it will be ``-1.0``.
        
        :type: float
        """
        pass
    
    @depth.setter
    def depth(self, value: float):
        pass
    
    @property
    def col(self) -> PixelValue:
        """
        The color value.
        
        If the modifications are for a color target, the contents will all be ``0``.
        
        :type: PixelValue
        """
        pass
    
    @col.setter
    def col(self, value: PixelValue):
        pass
    
    @property
    def stencil(self) -> int:
        """
        The stencil value.
        
        If stencil is not available for this modification, it will be negative. If stencil is not available
        at all and not in use then the stencil value will be ``-1``. If stencil was in use but can't be
        determined due to the pixel history implementation using stencil for its own purposes, the value
        will be ``-2``. This will only happen when looking at multiple modifications from the same event.
        
        :type: int
        """
        pass
    
    @stencil.setter
    def stencil(self, value: int):
        pass
    
