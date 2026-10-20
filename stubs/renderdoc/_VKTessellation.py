
from typing import overload

class VKTessellation():
    # Original docstring
    """
    Describes the state of the fixed-function tessellator.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKTessellation.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKTessellation'):
        """
        Construct a new VKTessellation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def domainOriginUpperLeft(self) -> bool:
        """
        ``True`` if the tessellation domain origin is upper-left, ``False`` if lower-left.
        
        :type: bool
        """
        pass
    
    @domainOriginUpperLeft.setter
    def domainOriginUpperLeft(self, value: bool):
        pass
    
    @property
    def numControlPoints(self) -> int:
        """
        The number of control points in each input patch.
        
        :type: int
        """
        pass
    
    @numControlPoints.setter
    def numControlPoints(self, value: int):
        pass
    
