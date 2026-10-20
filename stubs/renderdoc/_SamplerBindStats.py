from typing import List

from typing import overload

class SamplerBindStats():
    # Original docstring
    """
    Contains the statistics for sampler binds in a frame.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SamplerBindStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'SamplerBindStats'):
        """
        Construct a new SamplerBindStats with a deep copy of the input.
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
    def bindslots(self) -> List[int]:
        """
        A list where the Nth element contains the number of calls that bound N samplers.
        
        :type: List[int]
        """
        pass
    
    @bindslots.setter
    def bindslots(self, value: List[int]):
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
    
