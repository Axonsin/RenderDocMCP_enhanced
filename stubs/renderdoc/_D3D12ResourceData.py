from ._D3D12ResourceState import D3D12ResourceState
from ._ResourceId import ResourceId
from typing import List

from typing import overload

class D3D12ResourceData():
    # Original docstring
    """
    Contains the current state of a given resource.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12ResourceData.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12ResourceData'):
        """
        Construct a new D3D12ResourceData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the resource.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def states(self) -> List[D3D12ResourceState]:
        """
        The subresource states in this resource.
        
        :type: List[D3D12ResourceState]
        """
        pass
    
    @states.setter
    def states(self, value: List[D3D12ResourceState]):
        pass
    
