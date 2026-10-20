from ._ResourceId import ResourceId

from typing import overload

class D3D11StreamOutBind():
    # Original docstring
    """
    Describes a binding on the D3D11 stream-out stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11StreamOutBind.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11StreamOutBind'):
        """
        Construct a new D3D11StreamOutBind with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset of the stream-output binding.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
