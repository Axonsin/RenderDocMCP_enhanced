from ._ResourceId import ResourceId

from typing import overload

class VKIndexBuffer():
    # Original docstring
    """
    Describes the Vulkan index buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKIndexBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKIndexBuffer'):
        """
        Construct a new VKIndexBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the index buffer.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def byteStride(self) -> int:
        """
        The number of bytes for each index in the index buffer. Typically 2 or 4 bytes but
        it can be 0 if no index buffer is bound.
        
        :type: int
        """
        pass
    
    @byteStride.setter
    def byteStride(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of the buffer to the beginning of the index data.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The byte size from the start offset to the end of the index data.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
