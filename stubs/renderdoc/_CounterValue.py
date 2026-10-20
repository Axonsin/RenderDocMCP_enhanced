
from typing import overload

class CounterValue():
    # Original docstring
    """
    A resulting value from a GPU counter. Only one member is valid, see
    :class:`CounterDescription`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CounterValue.
        """
        pass
    
    @overload
    def __init__(self, other: 'CounterValue'):
        """
        Construct a new CounterValue with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def f(self) -> float:
        """
        A ``float`` value.
        
        :type: float
        """
        pass
    
    @f.setter
    def f(self, value: float):
        pass
    
    @property
    def u64(self) -> int:
        """
        A 64-bit unsigned integer.
        
        :type: int
        """
        pass
    
    @u64.setter
    def u64(self, value: int):
        pass
    
    @property
    def u32(self) -> int:
        """
        A 32-bit unsigned integer.
        
        :type: int
        """
        pass
    
    @u32.setter
    def u32(self, value: int):
        pass
    
    @property
    def d(self) -> float:
        """
        A ``double`` value.
        
        :type: float
        """
        pass
    
    @d.setter
    def d(self, value: float):
        pass
    
