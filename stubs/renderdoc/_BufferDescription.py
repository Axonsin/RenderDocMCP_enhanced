from ._BufferCategory import BufferCategory
from ._ResourceId import ResourceId

from typing import overload

class BufferDescription():
    # Original docstring
    """
    A description of a buffer resource.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BufferDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'BufferDescription'):
        """
        Construct a new BufferDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def creationFlags(self) -> BufferCategory:
        """
        The way this buffer will be used in the pipeline.
        
        :type: BufferCategory
        """
        pass
    
    @creationFlags.setter
    def creationFlags(self, value: BufferCategory):
        pass
    
    @property
    def length(self) -> int:
        """
        The byte length of the buffer.
        
        :type: int
        """
        pass
    
    @length.setter
    def length(self, value: int):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The unique :class:`ResourceId` that identifies this buffer.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def memoryOffset(self) -> int:
        """
        The byte offset in :data:`memory` where the buffer is bound. If
        :data:`memory` is unset, this will be 0.
        
        :type: int
        """
        pass
    
    @memoryOffset.setter
    def memoryOffset(self, value: int):
        pass
    
    @property
    def memory(self) -> ResourceId:
        """
        The unique :class:`ResourceId` that identifies the memory object this
        buffer has a fixed binding to. For objects that do not have an explicit memory binding
        or for sparse buffers, this will not be set.
        
        :type: ResourceId
        """
        pass
    
    @memory.setter
    def memory(self, value: ResourceId):
        pass
    
    @property
    def gpuAddress(self) -> int:
        """
        The known base GPU Address of this buffer. 0 if not applicable or available.
        
        :type: int
        """
        pass
    
    @gpuAddress.setter
    def gpuAddress(self, value: int):
        pass
    
