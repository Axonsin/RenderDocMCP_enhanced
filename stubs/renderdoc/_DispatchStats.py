
from typing import overload

class DispatchStats():
    # Original docstring
    """
    Contains the statistics for compute dispatches in a frame.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DispatchStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'DispatchStats'):
        """
        Construct a new DispatchStats with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def calls(self) -> int:
        """
        How many dispatch calls were made.
        
        :type: int
        """
        pass
    
    @calls.setter
    def calls(self, value: int):
        pass
    
    @property
    def indirect(self) -> int:
        """
        How many of :data:`calls` were indirect.
        
        :type: int
        """
        pass
    
    @indirect.setter
    def indirect(self, value: int):
        pass
    
