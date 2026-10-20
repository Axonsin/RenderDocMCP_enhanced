
from typing import overload

class FloatVector():
    # Original docstring
    """
    A floating point four-component vector
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised FloatVector.
        """
        pass
    
    @overload
    def __init__(self, other: 'FloatVector'):
        """
        Construct a new FloatVector with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Construct a new FloatVector using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def w(self) -> float:
        """
        The w component.
        
        :type: float
        """
        pass
    
    @w.setter
    def w(self, value: float):
        pass
    
    @property
    def x(self) -> float:
        """
        The x component.
        
        :type: float
        """
        pass
    
    @x.setter
    def x(self, value: float):
        pass
    
    @property
    def y(self) -> float:
        """
        The y component.
        
        :type: float
        """
        pass
    
    @y.setter
    def y(self, value: float):
        pass
    
    @property
    def z(self) -> float:
        """
        The z component.
        
        :type: float
        """
        pass
    
    @z.setter
    def z(self, value: float):
        pass
    
