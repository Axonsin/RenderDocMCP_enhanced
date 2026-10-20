from ._ResourceId import ResourceId

from typing import overload

class D3D11Predication():
    # Original docstring
    """
    Describes the current state of D3D11 predicated rendering.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11Predication.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11Predication'):
        """
        Construct a new D3D11Predication with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def value(self) -> bool:
        """
        The value to go along with the predicate.
        
        :type: bool
        """
        pass
    
    @value.setter
    def value(self, value: bool):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the active predicate.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def isPassing(self) -> bool:
        """
        ``True`` if the current predicate would render.
        
        :type: bool
        """
        pass
    
    @isPassing.setter
    def isPassing(self, value: bool):
        pass
    
