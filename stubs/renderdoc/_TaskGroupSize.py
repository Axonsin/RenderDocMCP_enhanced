
from typing import overload

class TaskGroupSize():
    # Original docstring
    """
    The size information for a task group.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TaskGroupSize.
        """
        pass
    
    @overload
    def __init__(self, other: 'TaskGroupSize'):
        """
        Construct a new TaskGroupSize with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def x(self) -> int:
        """
        The size in the x dimension.
        
        :type: int
        """
        pass
    
    @x.setter
    def x(self, value: int):
        pass
    
    @property
    def y(self) -> int:
        """
        The size in the y dimension.
        
        :type: int
        """
        pass
    
    @y.setter
    def y(self, value: int):
        pass
    
    @property
    def z(self) -> int:
        """
        The size in the z dimension.
        
        :type: int
        """
        pass
    
    @z.setter
    def z(self, value: int):
        pass
    
