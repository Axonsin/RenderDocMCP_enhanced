from ._ResourceId import ResourceId

from typing import overload

class DescriptorStoreDescription():
    # Original docstring
    """
    A description of a descriptor store.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DescriptorStoreDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'DescriptorStoreDescription'):
        """
        Construct a new DescriptorStoreDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The unique :class:`ResourceId` that identifies this descriptor store.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def descriptorCount(self) -> int:
        """
        The number of descriptors within this storage object.
        
        :type: int
        """
        pass
    
    @descriptorCount.setter
    def descriptorCount(self, value: int):
        pass
    
    @property
    def descriptorByteSize(self) -> int:
        """
        For descriptor stores which contain descriptors all of identical size, the size of each
        descriptor. Descriptors are assumed to be tightly packed so stride is equal to size.
        
        :type: int
        """
        pass
    
    @descriptorByteSize.setter
    def descriptorByteSize(self, value: int):
        pass
    
    @property
    def firstDescriptorOffset(self) -> int:
        """
        The byte offset within the store to the first descriptor.
        
        :type: int
        """
        pass
    
    @firstDescriptorOffset.setter
    def firstDescriptorOffset(self, value: int):
        pass
    
