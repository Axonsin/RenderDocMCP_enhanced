
from typing import overload

class D3D12ResourceState():
    # Original docstring
    """
    Describes the current state that a sub-resource is in.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12ResourceState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12ResourceState'):
        """
        Construct a new D3D12ResourceState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        A human-readable name for the current state.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
