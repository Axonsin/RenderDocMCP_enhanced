from ._ResourceId import ResourceId

from typing import overload

class D3D12Predication():
    # Original docstring
    """
    Describes the current state of D3D12 predicated rendering.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12Predication.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12Predication'):
        """
        Construct a new D3D12Predication with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer used for predicate data.
        
        If this is unset, predication is not enabled.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def offset(self) -> int:
        """
        The offset in the buffer where the value is read.
        
        :type: int
        """
        pass
    
    @offset.setter
    def offset(self, value: int):
        pass
    
    @property
    def skipIfZero(self) -> bool:
        """
        ``True`` if a value of zero in the buffer would lead to draws/dispatches being skipped when
        predication is enabled.
        
        If ``False`` then a zero in the buffer would lead to them being performed as normal.
        
        :type: bool
        """
        pass
    
    @skipIfZero.setter
    def skipIfZero(self, value: bool):
        pass
    
