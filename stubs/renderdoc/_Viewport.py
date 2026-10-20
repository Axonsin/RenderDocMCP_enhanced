
from typing import overload

class Viewport():
    # Original docstring
    """
    Information about a viewport.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Viewport.
        """
        pass
    
    @overload
    def __init__(self, other: 'Viewport'):
        """
        Construct a new Viewport with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float, enabled: bool):
        """
        Construct a new Viewport using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def x(self) -> float:
        """
        The X co-ordinate of the viewport.
        
        :type: float
        """
        pass
    
    @x.setter
    def x(self, value: float):
        pass
    
    @property
    def y(self) -> float:
        """
        The Y co-ordinate of the viewport.
        
        :type: float
        """
        pass
    
    @y.setter
    def y(self, value: float):
        pass
    
    @property
    def maxDepth(self) -> float:
        """
        The maximum depth of the viewport.
        
        :type: float
        """
        pass
    
    @maxDepth.setter
    def maxDepth(self, value: float):
        pass
    
    @property
    def height(self) -> float:
        """
        The height of the viewport.
        
        :type: float
        """
        pass
    
    @height.setter
    def height(self, value: float):
        pass
    
    @property
    def enabled(self) -> bool:
        """
        Is this viewport enabled.
        
        :type: bool
        """
        pass
    
    @enabled.setter
    def enabled(self, value: bool):
        pass
    
    @property
    def width(self) -> float:
        """
        The width of the viewport.
        
        :type: float
        """
        pass
    
    @width.setter
    def width(self, value: float):
        pass
    
    @property
    def minDepth(self) -> float:
        """
        The minimum depth of the viewport.
        
        :type: float
        """
        pass
    
    @minDepth.setter
    def minDepth(self, value: float):
        pass
    
