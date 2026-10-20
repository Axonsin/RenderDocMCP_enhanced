from typing import List

from typing import overload

class RasterizationStats():
    # Original docstring
    """
    Contains the statistics for rasterizer state binds in a frame.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised RasterizationStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'RasterizationStats'):
        """
        Construct a new RasterizationStats with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def calls(self) -> int:
        """
        How many function calls were made.
        
        :type: int
        """
        pass
    
    @calls.setter
    def calls(self, value: int):
        pass
    
    @property
    def redundants(self) -> int:
        """
        How many calls made no change due to the existing bind being identical.
        
        :type: int
        """
        pass
    
    @redundants.setter
    def redundants(self, value: int):
        pass
    
    @property
    def rects(self) -> List[int]:
        """
        A list where the Nth element contains the number of calls that bound N scissor rects.
        
        :type: List[int]
        """
        pass
    
    @rects.setter
    def rects(self, value: List[int]):
        pass
    
    @property
    def sets(self) -> int:
        """
        How many objects were bound.
        
        :type: int
        """
        pass
    
    @sets.setter
    def sets(self, value: int):
        pass
    
    @property
    def viewports(self) -> List[int]:
        """
        A list where the Nth element contains the number of calls that bound N viewports.
        
        :type: List[int]
        """
        pass
    
    @viewports.setter
    def viewports(self, value: List[int]):
        pass
    
    @property
    def nulls(self) -> int:
        """
        How many objects were unbound.
        
        :type: int
        """
        pass
    
    @nulls.setter
    def nulls(self, value: int):
        pass
    
