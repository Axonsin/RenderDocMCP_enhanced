# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKDescriptorBuffer import VKDescriptorBuffer
from .VKDescriptorSet import VKDescriptorSet
from .ResourceId import ResourceId

class VKPipeline(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the object and descriptor set bindings of a Vulkan pipeline object. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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
    def descriptorSets(self) -> List[VKDescriptorSet]:
        """
The bound descriptor sets.

:type: List[VKDescriptorSet]

"""
        pass

    @descriptorSets.setter
    def descriptorSets(self, value: List[VKDescriptorSet]):
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
    def pipelineResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the pipeline object.

:type: ResourceId

"""
        pass

    @pipelineResourceId.setter
    def pipelineResourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522C410>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKPipeline' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKPipeline' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKPipeline' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKPipeline' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKPipeline' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKPipeline' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKPipeline' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKPipeline' objects>, 'pipelineResourceId': <attribute 'pipelineResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelineComputeLayoutResourceId': <attribute 'pipelineComputeLayoutResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelinePreRastLayoutResourceId': <attribute 'pipelinePreRastLayoutResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelineFragmentLayoutResourceId': <attribute 'pipelineFragmentLayoutResourceId' of 'renderdoc.VKPipeline' objects>, 'descriptorBuffers': <attribute 'descriptorBuffers' of 'renderdoc.VKPipeline' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKPipeline' objects>, 'flags': <attribute 'flags' of 'renderdoc.VKPipeline' objects>, 'descriptorSets': <attribute 'descriptorSets' of 'renderdoc.VKPipeline' objects>, '__doc__': 'Describes the object and descriptor set bindings of a Vulkan pipeline object.'})"


