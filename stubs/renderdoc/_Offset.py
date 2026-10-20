
from typing import overload

class Offset():
    # Original docstring
    """
    Describes a 2-dimensional int offset
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Offset.
        """
        pass
    
    @overload
    def __init__(self, other: 'Offset'):
        """
        Construct a new Offset with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, x: int, y: int):
        """
        Construct a new Offset using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def x(self) -> int:
        """
        The X offset value.
        
        :type: int
        """
        pass
    
    @x.setter
    def x(self, value: int):
        pass
    
    @property
    def y(self) -> int:
        """
        The Y offset value.
        
        :type: int
        """
        pass
    
    @y.setter
    def y(self, value: int):
        pass
    
