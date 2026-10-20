from ._ResourceId import ResourceId

from typing import overload

class BoundVBuffer():
    # Original docstring
    """
    Information about a single vertex or index buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BoundVBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'BoundVBuffer'):
        """
        Construct a new BoundVBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        A :class:`~renderdoc.ResourceId` identifying the buffer.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def byteStride(self) -> int:
        """
        The stride in bytes between the start of one element and the start of the next.
        
        :type: int
        """
        pass
    
    @byteStride.setter
    def byteStride(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The offset in bytes from the start of the buffer to the data.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size of the buffer binding, or ``0xFFFFFFFF`` if the whole buffer is bound.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
