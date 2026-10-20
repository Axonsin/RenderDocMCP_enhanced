from ._ResourceId import ResourceId

from typing import overload

class D3D12StreamOutBind():
    # Original docstring
    """
    Describes a binding on the D3D12 stream-out stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12StreamOutBind.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12StreamOutBind'):
        """
        Construct a new D3D12StreamOutBind with a deep copy of the input.
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
    def writtenCountResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer where the written count will be stored.
        
        :type: ResourceId
        """
        pass
    
    @writtenCountResourceId.setter
    def writtenCountResourceId(self, value: ResourceId):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset in :data:`resourceId` where the buffer view starts in the underlying
        buffer.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def writtenCountByteOffset(self) -> int:
        """
        The byte offset in :data:`writtenCountResourceId` where the stream-out count will be
        written.
        
        :type: int
        """
        pass
    
    @writtenCountByteOffset.setter
    def writtenCountByteOffset(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        How many bytes are in this stream-out buffer view.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
