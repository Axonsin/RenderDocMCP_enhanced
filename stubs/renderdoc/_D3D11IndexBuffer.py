from ._ResourceId import ResourceId

from typing import overload

class D3D11IndexBuffer():
    # Original docstring
    """
    Describes the D3D11 index buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11IndexBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11IndexBuffer'):
        """
        Construct a new D3D11IndexBuffer with a deep copy of the input.
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
    
