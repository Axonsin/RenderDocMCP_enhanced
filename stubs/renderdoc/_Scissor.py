
from typing import overload

class Scissor():
    # Original docstring
    """
    Describes a single scissor region.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Scissor.
        """
        pass
    
    @overload
    def __init__(self, other: 'Scissor'):
        """
        Construct a new Scissor with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, x: int, y: int, width: int, height: int, enabled: bool):
        """
        Construct a new Scissor using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def x(self) -> int:
        """
        X co-ordinate of the scissor region.
        
        :type: int
        """
        pass
    
    @x.setter
    def x(self, value: int):
        pass
    
    @property
    def y(self) -> int:
        """
        Y co-ordinate of the scissor region.
        
        :type: int
        """
        pass
    
    @y.setter
    def y(self, value: int):
        pass
    
    @property
    def height(self) -> int:
        """
        Height of the scissor region.
        
        :type: int
        """
        pass
    
    @height.setter
    def height(self, value: int):
        pass
    
    @property
    def enabled(self) -> bool:
        """
        ``True`` if this scissor region is enabled.
        
        :type: bool
        """
        pass
    
    @enabled.setter
    def enabled(self, value: bool):
        pass
    
    @property
    def width(self) -> int:
        """
        Width of the scissor region.
        
        :type: int
        """
        pass
    
    @width.setter
    def width(self, value: int):
        pass
    
