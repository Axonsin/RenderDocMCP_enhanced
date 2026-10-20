from ._ResourceId import ResourceId

from typing import overload

class VKDescriptorBuffer():
    # Original docstring
    """
    A single descriptor buffer binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKDescriptorBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKDescriptorBuffer'):
        """
        Construct a new VKDescriptorBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def pushDescriptor(self) -> bool:
        """
        Indicates if this is the 'push' descriptor buffer.
        
        :type: bool
        """
        pass
    
    @pushDescriptor.setter
    def pushDescriptor(self, value: bool):
        pass
    
    @property
    def pushBuffer(self) -> ResourceId:
        """
        For push descriptors where a buffer is required, the :class:`ResourceId` of the push buffer object.
        
        :type: ResourceId
        """
        pass
    
    @pushBuffer.setter
    def pushBuffer(self, value: ResourceId):
        pass
    
    @property
    def samplerBuffer(self) -> bool:
        """
        Indicates if this buffer can contain samplers.
        
        :type: bool
        """
        pass
    
    @samplerBuffer.setter
    def samplerBuffer(self, value: bool):
        pass
    
    @property
    def offset(self) -> int:
        """
        The offset in bytes from the base of the buffer object to the start of the bound region.
        
        :type: int
        """
        pass
    
    @offset.setter
    def offset(self, value: int):
        pass
    
    @property
    def buffer(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer object being bound.
        
        :type: ResourceId
        """
        pass
    
    @buffer.setter
    def buffer(self, value: ResourceId):
        pass
    
    @property
    def resourceBuffer(self) -> bool:
        """
        Indicates if this buffer can contain resources (buffers and images).
        
        :type: bool
        """
        pass
    
    @resourceBuffer.setter
    def resourceBuffer(self, value: bool):
        pass
    
