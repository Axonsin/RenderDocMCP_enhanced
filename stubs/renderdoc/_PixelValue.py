from ._CounterValue import CounterValue
from typing import Tuple

from typing import overload

class PixelValue():
    # Original docstring
    """
    The contents of an RGBA pixel.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PixelValue.
        """
        pass
    
    @overload
    def __init__(self, other: CounterValue):
        """
        Construct a new PixelValue using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def uintValue(self) -> Tuple[int, int, int, int]:
        """
        The RGBA value interpreted as 32-bit unsigned integer.
        
        :type: Tuple[int, int, int, int]
        """
        pass
    
    @uintValue.setter
    def uintValue(self, value: Tuple[int, int, int, int]):
        pass
    
    @property
    def intValue(self) -> Tuple[int, int, int, int]:
        """
        The RGBA value interpreted as 32-bit signed integer.
        
        :type: Tuple[int, int, int, int]
        """
        pass
    
    @intValue.setter
    def intValue(self, value: Tuple[int, int, int, int]):
        pass
    
    @property
    def floatValue(self) -> Tuple[float, float, float, float]:
        """
        The RGBA value interpreted as ``float``.
        
        :type: Tuple[float, float, float, float]
        """
        pass
    
    @floatValue.setter
    def floatValue(self, value: Tuple[float, float, float, float]):
        pass
    
