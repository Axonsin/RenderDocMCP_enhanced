from ._ResourceId import ResourceId

from typing import overload

class VKXFBBuffer():
    # Original docstring
    """
    Describes a single transform feedback binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKXFBBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKXFBBuffer'):
        """
        Construct a new VKXFBBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def active(self) -> bool:
        """
        A flag indicating if this buffer is active or not.
        
        :type: bool
        """
        pass
    
    @active.setter
    def active(self, value: bool):
        pass
    
    @property
    def bufferResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the bound data buffer.
        
        :type: ResourceId
        """
        pass
    
    @bufferResourceId.setter
    def bufferResourceId(self, value: ResourceId):
        pass
    
    @property
    def counterBufferResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer storing the counter value (if set).
        
        :type: ResourceId
        """
        pass
    
    @counterBufferResourceId.setter
    def counterBufferResourceId(self, value: ResourceId):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The offset in bytes to the start of the data in the :data:`bufferResourceId`.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size in bytes of the data buffer.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
    @property
    def counterBufferOffset(self) -> int:
        """
        The offset in bytes to the counter in the :data:`counterBufferResourceId`.
        
        :type: int
        """
        pass
    
    @counterBufferOffset.setter
    def counterBufferOffset(self, value: int):
        pass
    
