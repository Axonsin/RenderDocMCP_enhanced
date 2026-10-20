
from typing import overload

class VKRenderArea():
    # Original docstring
    """
    Describes a render area in the current framebuffer.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKRenderArea.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKRenderArea'):
        """
        Construct a new VKRenderArea with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def x(self) -> int:
        """
        The X co-ordinate of the render area.
        
        :type: int
        """
        pass
    
    @x.setter
    def x(self, value: int):
        pass
    
    @property
    def y(self) -> int:
        """
        The Y co-ordinate of the render area.
        
        :type: int
        """
        pass
    
    @y.setter
    def y(self, value: int):
        pass
    
    @property
    def height(self) -> int:
        """
        The height of the render area.
        
        :type: int
        """
        pass
    
    @height.setter
    def height(self, value: int):
        pass
    
    @property
    def width(self) -> int:
        """
        The width of the render area.
        
        :type: int
        """
        pass
    
    @width.setter
    def width(self, value: int):
        pass
    
