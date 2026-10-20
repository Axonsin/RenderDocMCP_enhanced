
from typing import overload

class BusyData():
    # Original docstring
    """
    Information about why the target is busy.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BusyData.
        """
        pass
    
    @overload
    def __init__(self, other: 'BusyData'):
        """
        Construct a new BusyData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def clientName(self) -> str:
        """
        The name of the client currently connected to the target.
        
        :type: str
        """
        pass
    
    @clientName.setter
    def clientName(self, value: str):
        pass
    
