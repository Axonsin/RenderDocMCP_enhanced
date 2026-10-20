
from typing import overload

class NewChildData():
    # Original docstring
    """
    Information about a new child process spawned by the target.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised NewChildData.
        """
        pass
    
    @overload
    def __init__(self, other: 'NewChildData'):
        """
        Construct a new NewChildData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def ident(self) -> int:
        """
        The ident where the new child's target control is active.
        
        :type: int
        """
        pass
    
    @ident.setter
    def ident(self, value: int):
        pass
    
    @property
    def processId(self) -> int:
        """
        The PID (Process ID) of the new child.
        
        :type: int
        """
        pass
    
    @processId.setter
    def processId(self, value: int):
        pass
    
