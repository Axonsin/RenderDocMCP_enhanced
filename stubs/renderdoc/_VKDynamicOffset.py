
from typing import overload

class VKDynamicOffset():
    # Original docstring
    """
    A dynamic offset applied to a single descriptor access.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKDynamicOffset.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKDynamicOffset'):
        """
        Construct a new VKDynamicOffset with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def descriptorByteOffset(self) -> int:
        """
        The offset in bytes to the descriptor in the storage.
        
        :type: int
        """
        pass
    
    @descriptorByteOffset.setter
    def descriptorByteOffset(self, value: int):
        pass
    
    @property
    def dynamicBufferByteOffset(self) -> int:
        """
        The dynamic offset to apply to the buffer in bytes.
        
        :type: int
        """
        pass
    
    @dynamicBufferByteOffset.setter
    def dynamicBufferByteOffset(self, value: int):
        pass
    
