# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderStage import ShaderStage
from .UsedDescriptor import UsedDescriptor
from .ColorBlend import ColorBlend
from .ResourceId import ResourceId
from .Descriptor import Descriptor
from .DescriptorAccess import DescriptorAccess
from .BoundVBuffer import BoundVBuffer
from .Topology import Topology
from .Scissor import Scissor
from .ShaderMessage import ShaderMessage
from .ShaderReflection import ShaderReflection
from .StencilFace import StencilFace
from .VertexInputAttribute import VertexInputAttribute
from .Viewport import Viewport
from .MeshDataStage import MeshDataStage

class PipeState(): # skipped bases: <class 'SwigPyObject'>
    """
    An API-agnostic view of the common aspects of the pipeline state. This allows simple
    access to e.g. find out the bound resources or vertex buffers, or certain pipeline state which is
    available on all APIs.
    
    For more detailed or precise information without abstraction, access the specific pipeline state
    for the capture that's open.
    """
    def Abbrev(self, stage: ShaderStage) -> str: # real signature unknown; restored from __doc__
        """
        Abbrev(stage)
        
        Retrieves a suitable two or three letter abbreviation of the given shader stage.
        
        :param ShaderStage stage: The shader stage to abbreviate.
        :return: The abbreviation of the stage.
        :rtype: str
        """
        pass

    def GetAllUsedDescriptors(self, onlyUsed: bool=False) -> List[UsedDescriptor]: # real signature unknown; restored from __doc__
        """
        GetAllUsedDescriptors(onlyUsed=False)
        GetAllUsedDescriptors()
        
        Retrieves all descriptor information for all descriptors accessed at the current event.
        
        :param bool onlyUsed: Omit descriptors bound or declared but not accessed.
        :return: All descriptors accessed at the current event.
        :rtype: List[UsedDescriptor]
        """
        pass

    def GetColorBlends(self) -> List[ColorBlend]: # real signature unknown; restored from __doc__
        """
        GetColorBlends()
        
        Retrieves the current color blending states, per target.
        
        :return: The currently color blend states.
        :rtype: List[ColorBlend]
        """
        pass

    def GetComputePipelineObject(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetComputePipelineObject()
        
        Retrieves the the compute pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass

    def GetConstantBlock(self, stage: ShaderStage, index: int, arrayIdx: int) -> UsedDescriptor: # real signature unknown; restored from __doc__
        """
        GetConstantBlock(stage, index, arrayIdx)
        
        Retrieves the constant block at a given binding.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param int index: The index in the shader's ConstantBlocks array to look up.
        :param int arrayIdx: For APIs that support arrays of constant buffers in a single binding, the index
          in that array to look up.
        :return: The constant buffer at the specified binding.
        :rtype: UsedDescriptor
        """
        pass

    def GetConstantBlocks(self, stage: ShaderStage, onlyUsed: bool=False) -> List[UsedDescriptor]: # real signature unknown; restored from __doc__
        """
        GetConstantBlocks(stage, onlyUsed=False)
        GetConstantBlocks(stage)
        
        Retrieves the constant blocks used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed: Omit descriptors bound or declared but not accessed.
        :return: The currently bound constant blocks.
        :rtype: List[UsedDescriptor]
        """
        pass

    def GetDepthResolveTarget(self) -> Descriptor: # real signature unknown; restored from __doc__
        """
        GetDepthResolveTarget()
        
        Retrieves the read/write resources bound to the depth-stencil resolve output.
        
        :return: The currently bound depth-stencil resolve resource.
        :rtype: Descriptor
        """
        pass

    def GetDepthTarget(self) -> Descriptor: # real signature unknown; restored from __doc__
        """
        GetDepthTarget()
        
        Retrieves the read/write resources bound to the depth-stencil output.
        
        :return: The currently bound depth-stencil resource.
        :rtype: Descriptor
        """
        pass

    def GetDescriptorAccess(self) -> List[DescriptorAccess]: # real signature unknown; restored from __doc__
        """
        GetDescriptorAccess()
        
        Retrieves the current list of descriptor accesses, as cached from a call to
        :meth:`ReplayController.GetDescriptorAccess`. The return value is identical, this is here for
        convenience of access.
        
        :return: The descriptor accesses.
        :rtype: List[DescriptorAccess]
        """
        pass

    def GetGraphicsPipelineObject(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetGraphicsPipelineObject()
        
        Retrieves the the graphics pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass

    def GetIBuffer(self) -> BoundVBuffer: # real signature unknown; restored from __doc__
        """
        GetIBuffer()
        
        Retrieves the current index buffer binding.
        
        .. note::
          On OpenGL the index stride/width is not part of any state, but is specified in each action.
          In this case the current stride is whichever was last specified to a action, as if there was
          implicit state set by a action.
        
        :return: A :class:`BoundVBuffer` with the index buffer details
        :rtype: BoundVBuffer
        """
        pass

    def GetOutputTargets(self) -> List[Descriptor]: # real signature unknown; restored from __doc__
        """
        GetOutputTargets()
        
        Retrieves the resources bound to the color outputs.
        
        :return: The currently bound output targets.
        :rtype: List[Descriptor]
        """
        pass

    def GetPrimitiveTopology(self) -> Topology: # real signature unknown; restored from __doc__
        """
        GetPrimitiveTopology()
        
        Returns the current primitive topology.
        
        .. note::
          On OpenGL the primitive topology is not part of any state, but is specified in each action.
          In this case the current topology is whichever was last specified to a action, as if there was
          implicit state set by a action.
        
        :return: The current primitive topology.
        :rtype: Topology
        """
        pass

    def GetRasterizedStream(self) -> int: # real signature unknown; restored from __doc__
        """
        GetRasterizedStream()
        
        Retrieves the rasterized stream, if multiple streams are being generated in the GS.
        
        :return: The rasterized stream, or -1 of no stream is being rasterized.
        :rtype: int
        """
        pass

    def GetReadOnlyResources(self, stage: ShaderStage, onlyUsed: bool=False) -> List[UsedDescriptor]: # real signature unknown; restored from __doc__
        """
        GetReadOnlyResources(stage, onlyUsed=False)
        GetReadOnlyResources(stage)
        
        Retrieves the read-only resources used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed: Omit descriptors bound or declared but not accessed.
        :return: The currently bound read-only resources.
        :rtype: List[UsedDescriptor]
        """
        pass

    def GetReadWriteResources(self, stage: ShaderStage, onlyUsed: bool=False) -> List[UsedDescriptor]: # real signature unknown; restored from __doc__
        """
        GetReadWriteResources(stage, onlyUsed=False)
        GetReadWriteResources(stage)
        
        Retrieves the read/write resources used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed: Omit descriptors bound or declared but not accessed.
        :return: The currently bound read/write resources.
        :rtype: List[UsedDescriptor]
        """
        pass

    def GetResourceLayout(self, id: ResourceId) -> str: # real signature unknown; restored from __doc__
        """
        GetResourceLayout(id)
        
        For APIs that have explicit barriers, retrieves the current layout of a resource.
        
        :param ResourceId id: The ID of the resource to query for
        :return: The name of the current layout of the first subresource in the resource.
        :rtype: str
        """
        pass

    def GetRestartIndex(self) -> int: # real signature unknown; restored from __doc__
        """
        GetRestartIndex()
        
        Retrieves the primitive restart index.
        
        :return: The index value that represents a primitive restart not a real index.
        :rtype: int
        """
        pass

    def GetSamplers(self, stage: ShaderStage, onlyUsed: bool=False) -> List[UsedDescriptor]: # real signature unknown; restored from __doc__
        """
        GetSamplers(stage, onlyUsed=False)
        GetSamplers(stage)
        
        Retrieves the samplers bound to a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed: Omit descriptors bound or declared but not accessed.
        :return: The currently bound sampler resources.
        :rtype: List[UsedDescriptor]
        """
        pass

    def GetScissor(self, index: int) -> Scissor: # real signature unknown; restored from __doc__
        """
        GetScissor(index)
        
        Retrieves the scissor region for a given index.
        
        :param int index: The index to retrieve.
        :return: The scissor region for the given index.
        :rtype: Scissor
        """
        pass

    def GetShader(self, stage: ShaderStage) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetShader(stage)
        
        Retrieves the object ID of the shader bound at a shader stage.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The object ID for the given shader.
        :rtype: ResourceId
        """
        pass

    def GetShaderEntryPoint(self, stage: ShaderStage) -> str: # real signature unknown; restored from __doc__
        """
        GetShaderEntryPoint(stage)
        
        Retrieves the name of the entry point function for a shader stage.
        
        For some APIs that don't distinguish by entry point, this may be empty.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The entry point name for the given shader.
        :rtype: str
        """
        pass

    def GetShaderMessages(self) -> List[ShaderMessage]: # real signature unknown; restored from __doc__
        """
        GetShaderMessages()
        
        Retrieves the shader messages obtained for the current action.
        
        :return: The shader messages obtained for the current action.
        :rtype: List[ShaderMessage]
        """
        pass

    def GetShaderReflection(self, stage: ShaderStage) -> ShaderReflection: # real signature unknown; restored from __doc__
        """
        GetShaderReflection(stage)
        
        Retrieves the shader reflection information for a shader stage.
        
        This returns ``None`` if no shader is bound.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The reflection data for the given shader.
        :rtype: ShaderReflection
        """
        pass

    def GetStencilFaces(self) -> Tuple[StencilFace, StencilFace]: # real signature unknown; restored from __doc__
        """
        GetStencilFaces()
        
        Retrieves the current stencil states.
        
        :return: The currently stencil states. Front facing first, back facing second.
        :rtype: Tuple[StencilFace, StencilFace]
        """
        pass

    def GetVBuffers(self) -> List[BoundVBuffer]: # real signature unknown; restored from __doc__
        """
        GetVBuffers()
        
        Retrieves the currently bound vertex buffers.
        
        :return: The list of bound vertex buffers.
        :rtype: List[BoundVBuffer]
        """
        pass

    def GetVertexInputs(self) -> List[VertexInputAttribute]: # real signature unknown; restored from __doc__
        """
        GetVertexInputs()
        
        Retrieves the currently specified vertex attributes.
        
        :return: The list of current vertex attributes.
        :rtype: List[VertexInputAttribute]
        """
        pass

    def GetViewport(self, index: int) -> Viewport: # real signature unknown; restored from __doc__
        """
        GetViewport(index)
        
        Retrieves the viewport for a given index.
        
        :param int index: The index to retrieve.
        :return: The viewport for the given index.
        :rtype: Viewport
        """
        pass

    def HasAlignedPostVSData(self, stage: MeshDataStage) -> bool: # real signature unknown; restored from __doc__
        """
        HasAlignedPostVSData(stage)
        
        Determines whether or not the PostVS data is aligned in the typical fashion (ie.
        vectors not crossing ``float4`` boundaries). APIs that use stream-out or transform feedback have
        tightly packed data, but APIs that rewrite shaders to dump data might have these alignment
        requirements.
        
        :param MeshDataStage stage: The mesh data stage for the output data.
        :return: A boolean indicating if post-VS data is aligned.
        :rtype: bool
        """
        pass

    def IsCaptureD3D11(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureD3D11()
        
        Determines whether or not a D3D11 capture is currently loaded.
        
        :return: A boolean indicating if a D3D11 capture is currently loaded.
        :rtype: bool
        """
        pass

    def IsCaptureD3D12(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureD3D12()
        
        Determines whether or not a D3D12 capture is currently loaded.
        
        :return: A boolean indicating if a D3D12 capture is currently loaded.
        :rtype: bool
        """
        pass

    def IsCaptureGL(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureGL()
        
        Determines whether or not an OpenGL capture is currently loaded.
        
        :return: A boolean indicating if an OpenGL capture is currently loaded.
        :rtype: bool
        """
        pass

    def IsCaptureLoaded(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureLoaded()
        
        Determines whether or not a capture is currently loaded.
        
        :return: A boolean indicating if a capture is currently loaded.
        :rtype: bool
        """
        pass

    def IsCaptureVK(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureVK()
        
        Determines whether or not a Vulkan capture is currently loaded.
        
        :return: A boolean indicating if a Vulkan capture is currently loaded.
        :rtype: bool
        """
        pass

    def IsIndependentBlendingEnabled(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsIndependentBlendingEnabled()
        
        Determines whether or not independent blending is enabled.
        
        :return: A boolean indicating if independent blending is enabled.
        :rtype: bool
        """
        pass

    def IsRestartEnabled(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsRestartEnabled()
        
        Determines whether or not primitive restart is enabled.
        
        :return: A boolean indicating if primitive restart is enabled.
        :rtype: bool
        """
        pass

    def IsTessellationEnabled(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsTessellationEnabled()
        
        Determines whether or not tessellation is currently enabled.
        
        :return: A boolean indicating if tessellation is currently enabled.
        :rtype: bool
        """
        pass

    def MultiviewBroadcastCount(self) -> int: # real signature unknown; restored from __doc__
        """
        MultiviewBroadcastCount()
        
        
        :return: The number of views being broadcast to simultaneously during rendering.
        :rtype: int
        """
        pass

    def OutputAbbrev(self) -> str: # real signature unknown; restored from __doc__
        """
        OutputAbbrev()
        
        Retrieves a suitable two or three letter abbreviation of the output stage. Typically
        'OM' or 'FBO'.
        
        :return: The abbreviation of the output stage.
        :rtype: str
        """
        pass

    def SupportsBarriers(self) -> bool: # real signature unknown; restored from __doc__
        """
        SupportsBarriers()
        
        Determines whether or not the current capture uses explicit barriers.
        
        :return: A boolean indicating if explicit barriers are used.
        :rtype: bool
        """
        pass

    def SupportsResourceArrays(self) -> bool: # real signature unknown; restored from __doc__
        """
        SupportsResourceArrays()
        
        Determines whether or not the current capture supports binding arrays of resources.
        
        :return: A boolean indicating if binding arrays of resources is supported.
        :rtype: bool
        """
        pass

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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55231450>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.PipeState\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.PipeState\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.PipeState\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.PipeState\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.PipeState\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.PipeState\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.PipeState\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.PipeState\' objects>, \'IsCaptureLoaded\': <method \'IsCaptureLoaded\' of \'renderdoc.PipeState\' objects>, \'IsCaptureD3D11\': <method \'IsCaptureD3D11\' of \'renderdoc.PipeState\' objects>, \'IsCaptureD3D12\': <method \'IsCaptureD3D12\' of \'renderdoc.PipeState\' objects>, \'IsCaptureGL\': <method \'IsCaptureGL\' of \'renderdoc.PipeState\' objects>, \'IsCaptureVK\': <method \'IsCaptureVK\' of \'renderdoc.PipeState\' objects>, \'IsTessellationEnabled\': <method \'IsTessellationEnabled\' of \'renderdoc.PipeState\' objects>, \'MultiviewBroadcastCount\': <method \'MultiviewBroadcastCount\' of \'renderdoc.PipeState\' objects>, \'SupportsResourceArrays\': <method \'SupportsResourceArrays\' of \'renderdoc.PipeState\' objects>, \'SupportsBarriers\': <method \'SupportsBarriers\' of \'renderdoc.PipeState\' objects>, \'HasAlignedPostVSData\': <method \'HasAlignedPostVSData\' of \'renderdoc.PipeState\' objects>, \'GetRasterizedStream\': <method \'GetRasterizedStream\' of \'renderdoc.PipeState\' objects>, \'GetResourceLayout\': <method \'GetResourceLayout\' of \'renderdoc.PipeState\' objects>, \'Abbrev\': <method \'Abbrev\' of \'renderdoc.PipeState\' objects>, \'OutputAbbrev\': <method \'OutputAbbrev\' of \'renderdoc.PipeState\' objects>, \'GetViewport\': <method \'GetViewport\' of \'renderdoc.PipeState\' objects>, \'GetScissor\': <method \'GetScissor\' of \'renderdoc.PipeState\' objects>, \'GetShaderReflection\': <method \'GetShaderReflection\' of \'renderdoc.PipeState\' objects>, \'GetComputePipelineObject\': <method \'GetComputePipelineObject\' of \'renderdoc.PipeState\' objects>, \'GetGraphicsPipelineObject\': <method \'GetGraphicsPipelineObject\' of \'renderdoc.PipeState\' objects>, \'GetShaderEntryPoint\': <method \'GetShaderEntryPoint\' of \'renderdoc.PipeState\' objects>, \'GetShader\': <method \'GetShader\' of \'renderdoc.PipeState\' objects>, \'GetPrimitiveTopology\': <method \'GetPrimitiveTopology\' of \'renderdoc.PipeState\' objects>, \'GetIBuffer\': <method \'GetIBuffer\' of \'renderdoc.PipeState\' objects>, \'IsRestartEnabled\': <method \'IsRestartEnabled\' of \'renderdoc.PipeState\' objects>, \'GetRestartIndex\': <method \'GetRestartIndex\' of \'renderdoc.PipeState\' objects>, \'GetVBuffers\': <method \'GetVBuffers\' of \'renderdoc.PipeState\' objects>, \'GetVertexInputs\': <method \'GetVertexInputs\' of \'renderdoc.PipeState\' objects>, \'GetDescriptorAccess\': <method \'GetDescriptorAccess\' of \'renderdoc.PipeState\' objects>, \'GetAllUsedDescriptors\': <method \'GetAllUsedDescriptors\' of \'renderdoc.PipeState\' objects>, \'GetConstantBlock\': <method \'GetConstantBlock\' of \'renderdoc.PipeState\' objects>, \'GetConstantBlocks\': <method \'GetConstantBlocks\' of \'renderdoc.PipeState\' objects>, \'GetReadOnlyResources\': <method \'GetReadOnlyResources\' of \'renderdoc.PipeState\' objects>, \'GetSamplers\': <method \'GetSamplers\' of \'renderdoc.PipeState\' objects>, \'GetReadWriteResources\': <method \'GetReadWriteResources\' of \'renderdoc.PipeState\' objects>, \'GetDepthTarget\': <method \'GetDepthTarget\' of \'renderdoc.PipeState\' objects>, \'GetDepthResolveTarget\': <method \'GetDepthResolveTarget\' of \'renderdoc.PipeState\' objects>, \'GetOutputTargets\': <method \'GetOutputTargets\' of \'renderdoc.PipeState\' objects>, \'GetColorBlends\': <method \'GetColorBlends\' of \'renderdoc.PipeState\' objects>, \'GetStencilFaces\': <method \'GetStencilFaces\' of \'renderdoc.PipeState\' objects>, \'IsIndependentBlendingEnabled\': <method \'IsIndependentBlendingEnabled\' of \'renderdoc.PipeState\' objects>, \'GetShaderMessages\': <method \'GetShaderMessages\' of \'renderdoc.PipeState\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.PipeState\' objects>, \'__doc__\': "\\nAn API-agnostic view of the common aspects of the pipeline state. This allows simple\\naccess to e.g. find out the bound resources or vertex buffers, or certain pipeline state which is\\navailable on all APIs.\\n\\nFor more detailed or precise information without abstraction, access the specific pipeline state\\nfor the capture that\'s open.\\n\\n"})'


