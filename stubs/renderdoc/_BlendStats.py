
from typing import overload

class BlendStats():
    # Original docstring
    """
    Contains the statistics for blend state binds in a frame.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BlendStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'BlendStats'):
        """
        Construct a new BlendStats with a deep copy of the input.
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
    
