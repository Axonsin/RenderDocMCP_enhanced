from ._ResourceId import ResourceId
from ._VKDescriptorBuffer import VKDescriptorBuffer
from ._VKDescriptorSet import VKDescriptorSet
from typing import List

from typing import overload

class VKPipeline():
    # Original docstring
    """
    Describes the object and descriptor set bindings of a Vulkan pipeline object.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKPipeline.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKPipeline'):
        """
        Construct a new VKPipeline with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def pipelineResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the pipeline object.
        
        :type: ResourceId
        """
        pass
    
    @pipelineResourceId.setter
    def pipelineResourceId(self, value: ResourceId):
        pass
    
    @property
    def pipelineComputeLayoutResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the compute pipeline layout object.
        
        :type: ResourceId
        """
        pass
    
    @pipelineComputeLayoutResourceId.setter
    def pipelineComputeLayoutResourceId(self, value: ResourceId):
        pass
    
    @property
    def pipelinePreRastLayoutResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the pre-rasterization pipeline layout object.
        
        When not using pipeline libraries, this will be identical to :data:`pipelineFragmentLayoutResourceId`.
        
        :type: ResourceId
        """
        pass
    
    @pipelinePreRastLayoutResourceId.setter
    def pipelinePreRastLayoutResourceId(self, value: ResourceId):
        pass
    
    @property
    def pipelineFragmentLayoutResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the fragment pipeline layout object.
        
        When not using pipeline libraries, this will be identical to :data:`pipelinePreRastLayoutResourceId`.
        
        :type: ResourceId
        """
        pass
    
    @pipelineFragmentLayoutResourceId.setter
    def pipelineFragmentLayoutResourceId(self, value: ResourceId):
        pass
    
    @property
    def descriptorBuffers(self) -> List[VKDescriptorBuffer]:
        """
        The bound descriptor buffers.
        
        :type: List[VKDescriptorBuffer]
        """
        pass
    
    @descriptorBuffers.setter
    def descriptorBuffers(self, value: List[VKDescriptorBuffer]):
        pass
    
    @property
    def flags(self) -> int:
        """
        The flags used to create the pipeline object.
        
        :type: int
        """
        pass
    
    @flags.setter
    def flags(self, value: int):
        pass
    
    @property
    def descriptorSets(self) -> List[VKDescriptorSet]:
        """
        The bound descriptor sets.
        
        :type: List[VKDescriptorSet]
        """
        pass
    
    @descriptorSets.setter
    def descriptorSets(self, value: List[VKDescriptorSet]):
        pass
    
