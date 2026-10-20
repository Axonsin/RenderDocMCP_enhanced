from ._ResourceId import ResourceId
from ._VKDynamicOffset import VKDynamicOffset
from typing import List

from typing import overload

class VKDescriptorSet():
    # Original docstring
    """
    The contents of a descriptor set.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKDescriptorSet.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKDescriptorSet'):
        """
        Construct a new VKDescriptorSet with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def pushDescriptor(self) -> bool:
        """
        Indicates if this is a virtual 'push' descriptor set.
        
        :type: bool
        """
        pass
    
    @pushDescriptor.setter
    def pushDescriptor(self, value: bool):
        pass
    
    @property
    def layoutResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the descriptor set layout that matches this set.
        
        :type: ResourceId
        """
        pass
    
    @layoutResourceId.setter
    def layoutResourceId(self, value: ResourceId):
        pass
    
    @property
    def descriptorSetResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the descriptor set object, if a real descriptor set is bound.
        
        .. note::
          If using descriptor buffers this value may be unset, see :data:`descriptorBufferIndex`.
        
        :type: ResourceId
        """
        pass
    
    @descriptorSetResourceId.setter
    def descriptorSetResourceId(self, value: ResourceId):
        pass
    
    @property
    def descriptorBufferEmbeddedSamplers(self) -> bool:
        """
        Indicates if this is a virtual descriptor set for binding embedded immutable samplers.
        
        :type: bool
        """
        pass
    
    @descriptorBufferEmbeddedSamplers.setter
    def descriptorBufferEmbeddedSamplers(self, value: bool):
        pass
    
    @property
    def dynamicOffsets(self) -> List[VKDynamicOffset]:
        """
        A list of dynamic offsets to be applied to specific bindings, on top of the contents
        of their descriptors.
        
        .. note::
          The returned values from :meth:`PipeState.GetConstantBlock` already have these offsets applied.
        
        :type: List[VKDynamicOffset]
        """
        pass
    
    @dynamicOffsets.setter
    def dynamicOffsets(self, value: List[VKDynamicOffset]):
        pass
    
    @property
    def descriptorBufferByteOffset(self) -> int:
        """
        The byte offset from the start of the descriptor buffer at index :data:`descriptorBufferIndex` where this set's data is.
        
        :type: int
        """
        pass
    
    @descriptorBufferByteOffset.setter
    def descriptorBufferByteOffset(self, value: int):
        pass
    
    @property
    def descriptorBufferIndex(self) -> int:
        """
        The index of the descriptor buffer to be used, or ``-1`` if no descriptor buffer is used.
        
        :type: int
        """
        pass
    
    @descriptorBufferIndex.setter
    def descriptorBufferIndex(self, value: int):
        pass
    
