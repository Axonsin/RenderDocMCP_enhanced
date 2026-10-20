from ._ResourceId import ResourceId

from typing import overload

class VKVertexBuffer():
    # Original docstring
    """
    Describes a single Vulkan vertex buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKVertexBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKVertexBuffer'):
        """
        Construct a new VKVertexBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer bound to this slot.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def byteStride(self) -> int:
        """
        The byte stride between the start of one set of vertex data and the next.
        
        :type: int
        """
        pass
    
    @byteStride.setter
    def byteStride(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of the buffer to the beginning of the vertex data.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size of the vertex buffer.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
