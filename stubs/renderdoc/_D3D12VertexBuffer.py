from ._ResourceId import ResourceId

from typing import overload

class D3D12VertexBuffer():
    # Original docstring
    """
    Describes a single D3D12 vertex buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12VertexBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12VertexBuffer'):
        """
        Construct a new D3D12VertexBuffer with a deep copy of the input.
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
        The number of bytes available in this vertex buffer.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
