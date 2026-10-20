from ._BoundVBuffer import BoundVBuffer
from ._ColorBlend import ColorBlend
from ._DepthTestState import DepthTestState
from ._Descriptor import Descriptor
from ._DescriptorAccess import DescriptorAccess
from ._MeshDataStage import MeshDataStage
from ._RasterState import RasterState
from ._ResourceId import ResourceId
from ._Scissor import Scissor
from ._ShaderMessage import ShaderMessage
from ._ShaderReflection import ShaderReflection
from ._ShaderStage import ShaderStage
from ._StencilFace import StencilFace
from ._Topology import Topology
from ._UsedDescriptor import UsedDescriptor
from ._VertexInputAttribute import VertexInputAttribute
from ._Viewport import Viewport
from typing import List, Tuple

from typing import overload

class PipeState():
    # Original docstring
    """
    An API-agnostic view of the common aspects of the pipeline state. This allows simple
    access to e.g. find out the bound resources or vertex buffers, or certain pipeline state which is
    available on all APIs.
    
    For more detailed or precise information without abstraction, access the specific pipeline state
    for the capture that's open.
    
    Available from :meth:`~qrenderdoc.CaptureContext.CurPipelineState` in the UI or
    :meth:`~renderdoc.ReplayController.GetPipelineState` from the replay API directly.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PipeState.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def IsCaptureLoaded(self) -> bool:
        """
        Determines whether or not a capture is currently loaded.
        
        :return: A boolean indicating if a capture is currently loaded.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureD3D11(self) -> bool:
        """
        Determines whether or not a D3D11 capture is currently loaded.
        
        :return: A boolean indicating if a D3D11 capture is currently loaded.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureD3D12(self) -> bool:
        """
        Determines whether or not a D3D12 capture is currently loaded.
        
        :return: A boolean indicating if a D3D12 capture is currently loaded.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureGL(self) -> bool:
        """
        Determines whether or not an OpenGL capture is currently loaded.
        
        :return: A boolean indicating if an OpenGL capture is currently loaded.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureVK(self) -> bool:
        """
        Determines whether or not a Vulkan capture is currently loaded.
        
        :return: A boolean indicating if a Vulkan capture is currently loaded.
        :rtype: bool
        """
        pass
    
    
    def IsTessellationEnabled(self) -> bool:
        """
        Determines whether or not tessellation is currently enabled.
        
        :return: A boolean indicating if tessellation is currently enabled.
        :rtype: bool
        """
        pass
    
    
    def MultiviewBroadcastCount(self) -> int:
        """
        :return: The number of views being broadcast to simultaneously during rendering.
        :rtype: int
        """
        pass
    
    
    def SupportsResourceArrays(self) -> bool:
        """
        Determines whether or not the current capture supports binding arrays of resources.
        
        :return: A boolean indicating if binding arrays of resources is supported.
        :rtype: bool
        """
        pass
    
    
    def SupportsBarriers(self) -> bool:
        """
        Determines whether or not the current capture uses explicit barriers.
        
        :return: A boolean indicating if explicit barriers are used.
        :rtype: bool
        """
        pass
    
    
    def HasAlignedPostVSData(self, stage: MeshDataStage) -> bool:
        """
        Determines whether or not the PostVS data is aligned in the typical fashion (i.e.
        vectors not crossing ``float4`` boundaries). APIs that use stream-out or transform feedback have
        tightly packed data, but APIs that rewrite shaders to dump data might have these alignment
        requirements.
        
        :param MeshDataStage stage: The mesh data stage for the output data.
        :return: A boolean indicating if post-VS data is aligned.
        :rtype: bool
        """
        pass
    
    
    def GetRasterizedStream(self) -> int:
        """
        Retrieves the rasterized stream, if multiple streams are being generated in the GS.
        
        :return: The rasterized stream, or -1 of no stream is being rasterized.
        :rtype: int
        """
        pass
    
    
    def GetResourceLayout(self, id: ResourceId) -> str:
        """
        For APIs that have explicit barriers, retrieves the current layout of a resource.
        
        :param ResourceId id: The ID of the resource to query for
        :return: The name of the current layout of the first subresource in the resource.
        :rtype: str
        """
        pass
    
    
    def Abbrev(self, stage: ShaderStage) -> str:
        """
        Retrieves a suitable two or three letter abbreviation of the given shader stage.
        
        :param ShaderStage stage: The shader stage to abbreviate.
        :return: The abbreviation of the stage.
        :rtype: str
        """
        pass
    
    
    def OutputAbbrev(self) -> str:
        """
        Retrieves a suitable two or three letter abbreviation of the output stage. Typically
        'OM' or 'FBO'.
        
        :return: The abbreviation of the output stage.
        :rtype: str
        """
        pass
    
    
    def GetViewport(self, index: int) -> Viewport:
        """
        Retrieves the viewport for a given index.
        
        :param int index: The index to retrieve.
        :return: The viewport for the given index.
        :rtype: Viewport
        """
        pass
    
    
    def GetScissor(self, index: int) -> Scissor:
        """
        Retrieves the scissor region for a given index.
        
        :param int index: The index to retrieve.
        :return: The scissor region for the given index.
        :rtype: Scissor
        """
        pass
    
    
    def GetShaderReflection(self, stage: ShaderStage) -> ShaderReflection:
        """
        Retrieves the shader reflection information for a shader stage.
        
        This returns ``None`` if no shader is bound.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The reflection data for the given shader.
        :rtype: ShaderReflection
        """
        pass
    
    
    def GetComputePipelineObject(self) -> ResourceId:
        """
        Retrieves the the compute pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass
    
    
    def GetGraphicsPipelineObject(self) -> ResourceId:
        """
        Retrieves the the graphics pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass
    
    
    def GetShaderEntryPoint(self, stage: ShaderStage) -> str:
        """
        Retrieves the name of the entry point function for a shader stage.
        
        For some APIs that don't distinguish by entry point, this may be empty.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The entry point name for the given shader.
        :rtype: str
        """
        pass
    
    
    def GetShader(self, stage: ShaderStage) -> ResourceId:
        """
        Retrieves the object ID of the shader bound at a shader stage.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The object ID for the given shader.
        :rtype: ResourceId
        """
        pass
    
    
    def GetPrimitiveTopology(self) -> Topology:
        """
        Returns the current primitive topology.
        
        .. note::
          On OpenGL the primitive topology is not part of any state, but is specified in each action.
          In this case the current topology is whichever was last specified to a action, as if there was
          implicit state set by a action.
        
        :return: The current primitive topology.
        :rtype: Topology
        """
        pass
    
    
    def GetIBuffer(self) -> BoundVBuffer:
        """
        Retrieves the current index buffer binding.
        
        .. note::
          On OpenGL the index stride/width is not part of any state, but is specified in each action.
          In this case the current stride is whichever was last specified to a action, as if there was
          implicit state set by a action.
        
        :return: A :class:`BoundVBuffer` with the index buffer details
        :rtype: BoundVBuffer
        """
        pass
    
    
    def IsRestartEnabled(self) -> bool:
        """
        Determines whether or not primitive restart is enabled.
        
        :return: A boolean indicating if primitive restart is enabled.
        :rtype: bool
        """
        pass
    
    
    def GetRestartIndex(self) -> int:
        """
        Retrieves the primitive restart index.
        
        :return: The index value that represents a primitive restart not a real index.
        :rtype: int
        """
        pass
    
    
    def GetVBuffers(self) -> List[BoundVBuffer]:
        """
        Retrieves the currently bound vertex buffers.
        
        :return: The list of bound vertex buffers.
        :rtype: List[BoundVBuffer]
        """
        pass
    
    
    def GetVertexInputs(self) -> List[VertexInputAttribute]:
        """
        Retrieves the currently specified vertex attributes.
        
        :return: The list of current vertex attributes.
        :rtype: List[VertexInputAttribute]
        """
        pass
    
    
    def GetDescriptorAccess(self) -> List[DescriptorAccess]:
        """
        Retrieves the current list of descriptor accesses, as cached from a call to
        :meth:`ReplayController.GetDescriptorAccess`. The return value is identical, this is here for
        convenience of access.
        
        :return: The descriptor accesses.
        :rtype: List[DescriptorAccess]
        """
        pass
    
    
    def GetAllUsedDescriptors(self, onlyUsed: bool = False) -> List[UsedDescriptor]:
        """
        Retrieves all descriptor information for all descriptors accessed at the current event.
        
        :param bool onlyUsed=False: **Optional parameter**. Omit descriptors bound or declared but not accessed.
        :return: All descriptors accessed at the current event.
        :rtype: List[UsedDescriptor]
        """
        pass
    
    
    def GetConstantBlock(self, stage: ShaderStage, index: int, arrayIdx: int) -> UsedDescriptor:
        """
        Retrieves the constant block at a given binding.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param int index: The index in the shader's ConstantBlocks array to look up.
        :param int arrayIdx: For APIs that support arrays of constant buffers in a single binding, the index
          in that array to look up.
        :return: The constant buffer at the specified binding.
        :rtype: UsedDescriptor
        """
        pass
    
    
    def GetConstantBlocks(self, stage: ShaderStage, onlyUsed: bool = False) -> List[UsedDescriptor]:
        """
        Retrieves the constant blocks used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed=False: **Optional parameter**. Omit descriptors bound or declared but not accessed.
        :return: The currently bound constant blocks.
        :rtype: List[UsedDescriptor]
        """
        pass
    
    
    def GetReadOnlyResources(self, stage: ShaderStage, onlyUsed: bool = False) -> List[UsedDescriptor]:
        """
        Retrieves the read-only resources used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed=False: **Optional parameter**. Omit descriptors bound or declared but not accessed.
        :return: The currently bound read-only resources.
        :rtype: List[UsedDescriptor]
        """
        pass
    
    
    def GetSamplers(self, stage: ShaderStage, onlyUsed: bool = False) -> List[UsedDescriptor]:
        """
        Retrieves the samplers bound to a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed=False: **Optional parameter**. Omit descriptors bound or declared but not accessed.
        :return: The currently bound sampler resources.
        :rtype: List[UsedDescriptor]
        """
        pass
    
    
    def GetReadWriteResources(self, stage: ShaderStage, onlyUsed: bool = False) -> List[UsedDescriptor]:
        """
        Retrieves the read/write resources used by a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param bool onlyUsed=False: **Optional parameter**. Omit descriptors bound or declared but not accessed.
        :return: The currently bound read/write resources.
        :rtype: List[UsedDescriptor]
        """
        pass
    
    
    def GetDepthTarget(self) -> Descriptor:
        """
        Retrieves the read/write resources bound to the depth-stencil output.
        
        :return: The currently bound depth-stencil resource.
        :rtype: Descriptor
        """
        pass
    
    
    def GetDepthResolveTarget(self) -> Descriptor:
        """
        Retrieves the read/write resources bound to the depth-stencil resolve output.
        
        :return: The currently bound depth-stencil resolve resource.
        :rtype: Descriptor
        """
        pass
    
    
    def GetOutputTargets(self) -> List[Descriptor]:
        """
        Retrieves the resources bound to the color outputs.
        
        :return: The currently bound output targets.
        :rtype: List[Descriptor]
        """
        pass
    
    
    def GetColorBlends(self) -> List[ColorBlend]:
        """
        Retrieves the current color blending states, per target.
        
        :return: The currently color blend states.
        :rtype: List[ColorBlend]
        """
        pass
    
    
    def GetBlendFactor(self) -> Tuple[float, float, float, float]:
        """
        Retrieves the current fixed blend factor.
        
        :return: The currently fixed blend factor.
        :rtype: Tuple[float,float,float,float]
        """
        pass
    
    
    def IsStencilTestEnabled(self) -> bool:
        """
        Checks whether stencil operations are enabled or not.
        
        :return: ``True`` if stencil testing is enabled.
        :rtype: bool
        """
        pass
    
    
    def GetStencilFaces(self) -> Tuple[StencilFace, StencilFace]:
        """
        Retrieves the current stencil states.
        
        :return: The currently stencil states. Front facing first, back facing second.
        :rtype: Tuple[StencilFace, StencilFace]
        """
        pass
    
    
    def GetDepthTestState(self) -> DepthTestState:
        """
        Retrieves some of the depth testing state.
        
        This doesn't contain all properties from all APIs but a common subset.
        
        :return: The currently depth testing state.
        :rtype: DepthTestState
        """
        pass
    
    
    def GetRasterState(self) -> RasterState:
        """
        Retrieves some of the rasterizer state.
        
        This doesn't contain all properties from all APIs but a common subset.
        
        :return: The currently depth testing state.
        :rtype: RasterState
        """
        pass
    
    
    def IsIndependentBlendingEnabled(self) -> bool:
        """
        Determines whether or not independent blending is enabled.
        
        :return: A boolean indicating if independent blending is enabled.
        :rtype: bool
        """
        pass
    
    
    def GetShaderMessages(self) -> List[ShaderMessage]:
        """
        Retrieves the shader messages obtained for the current action.
        
        :return: The shader messages obtained for the current action.
        :rtype: List[ShaderMessage]
        """
        pass
    
