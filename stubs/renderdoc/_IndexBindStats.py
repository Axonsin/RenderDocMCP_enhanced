
from typing import overload

class IndexBindStats():
    # Original docstring
    """
    Contains the statistics for index buffer binds in a frame.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised IndexBindStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'IndexBindStats'):
        """
        Construct a new IndexBindStats with a deep copy of the input.
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
    def nulls(self) -> int:
        """
        How many objects were unbound.
        
        :type: int
        """
        pass
    
    @nulls.setter
    def nulls(self, value: int):
        pass
    
