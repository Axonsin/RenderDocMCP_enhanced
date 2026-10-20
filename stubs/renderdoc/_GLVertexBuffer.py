from ._ResourceId import ResourceId

from typing import overload

class GLVertexBuffer():
    # Original docstring
    """
    Describes a single OpenGL vertex buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLVertexBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLVertexBuffer'):
        """
        Construct a new GLVertexBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def instanceDivisor(self) -> int:
        """
        The instance rate divisor.
        
        If this is ``0`` then the vertex buffer is read at vertex rate.
        
        If it's ``1`` then one element is read for each instance, and for ``N`` greater than ``1`` then
        ``N`` instances read the same element before advancing.
        
        :type: int
        """
        pass
    
    @instanceDivisor.setter
    def instanceDivisor(self, value: int):
        pass
    
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
    
