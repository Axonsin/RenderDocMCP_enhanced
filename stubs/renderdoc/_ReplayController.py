from ._APIProperties import APIProperties
from ._ActionDescription import ActionDescription
from ._BufferDescription import BufferDescription
from ._CompType import CompType
from ._CounterDescription import CounterDescription
from ._CounterResult import CounterResult
from ._D3D11State import D3D11State
from ._D3D12State import D3D12State
from ._DebugMessage import DebugMessage
from ._DebugPixelInputs import DebugPixelInputs
from ._Descriptor import Descriptor
from ._DescriptorAccess import DescriptorAccess
from ._DescriptorLogicalLocation import DescriptorLogicalLocation
from ._DescriptorRange import DescriptorRange
from ._DescriptorStoreDescription import DescriptorStoreDescription
from ._EventUsage import EventUsage
from ._FrameDescription import FrameDescription
from ._GLState import GLState
from ._GPUCounter import GPUCounter
from ._MeshDataStage import MeshDataStage
from ._MeshFormat import MeshFormat
from ._PipeState import PipeState
from ._PixelModification import PixelModification
from ._PixelValue import PixelValue
from ._ReplayOutput import ReplayOutput
from ._ReplayOutputType import ReplayOutputType
from ._ResourceDescription import ResourceDescription
from ._ResourceId import ResourceId
from ._ResultDetails import ResultDetails
from ._SDFile import SDFile
from ._SamplerDescriptor import SamplerDescriptor
from ._ShaderCompileFlags import ShaderCompileFlags
from ._ShaderDebugState import ShaderDebugState
from ._ShaderDebugTrace import ShaderDebugTrace
from ._ShaderDebugger import ShaderDebugger
from ._ShaderEncoding import ShaderEncoding
from ._ShaderEntryPoint import ShaderEntryPoint
from ._ShaderReflection import ShaderReflection
from ._ShaderSourcePrefix import ShaderSourcePrefix
from ._ShaderStage import ShaderStage
from ._ShaderVariable import ShaderVariable
from ._Subresource import Subresource
from ._TextureDescription import TextureDescription
from ._TextureSave import TextureSave
from ._VKState import VKState
from ._WindowingData import WindowingData
from ._WindowingSystem import WindowingSystem
from typing import List, Tuple

class ReplayController():
    # Original docstring
    """
    The primary interface to access the information in a capture and the current state, as
    well as control the replay and analysis functionality available.
    
    Available as a blocking interface in UI scripts via
    :meth:`~qrenderdoc.CaptureContext.GetBlockingController` or directly on the replay thread using
    :meth:`~qrenderdoc.ReplayManager.AsyncInvoke`.
    
    .. function:: KillCallback()
    
      Not an actual member function - the signature for any ``KillCallback`` callbacks.
    
      Called whenever some on-going blocking process needs to determine if it should close.
    
      :return: Whether or not the process should be killed.
      :rtype: bool
    
    .. function:: ProgressCallback()
    
      Not an actual member function - the signature for any ``ProgressCallback`` callbacks.
    
      Called by an on-going blocking process to update a progress bar or similar user feedback.
    
      The progress value will go from 0.0 to 1.0 as the process completes. Any other value will indicate
      that the process has completed
    
      :param float progress: The latest progress amount.
    
    .. function:: PreviewWindowCallback()
    
      Not an actual member function - the signature for any ``PreviewWindowCallback`` callbacks.
    
      Called when a preview window could optionally be opened to display some information. It will be
      called repeatedly with :paramref:`PreviewWindowCallback.active` set to ``True`` to allow any
      platform-specific message pumping.
    
      :param bool active: ``True`` if a preview window is active/opened, ``False`` if it has closed.
      :return: The windowing data for a preview window, or empty/default values if no window should be
        created.
      :rtype: WindowingData
    
    .. data:: NoPreference
    
      No preference for a particular value, see :meth:`ReplayController.DebugPixel`.
    """
    
    
    NoPreference = 4294967295
    """
    No preference for a particular value, see :meth:`ReplayController.DebugPixel`.
    """
    
    
    def GetAPIProperties(self) -> APIProperties:
        """
        Retrieve a :class:`APIProperties` object describing the current capture.
        
        :return: The properties of the current capture.
        :rtype: APIProperties
        """
        pass
    
    
    def GetSupportedWindowSystems(self) -> List[WindowingSystem]:
        """
        Retrieves the supported :class:`WindowingSystem` systems by the local system.
        
        :return: The list of supported systems.
        :rtype: List[WindowingSystem]
        """
        pass
    
    
    def CreateOutput(self, window: WindowingData, type: ReplayOutputType) -> ReplayOutput:
        """
        Creates a replay output of the given type to the given native window
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ReplayOutputType type: What type of output to create
        :return: A handle to the created output, or ``None`` on failure
        :rtype: ReplayOutput
        """
        pass
    
    
    def Shutdown(self):
        """
        Shutdown and destroy the current interface and all outputs that have been created.
        """
        pass
    
    
    def ReplayLoop(self, window: WindowingData, texid: ResourceId):
        """
        Goes into a blocking loop, repeatedly replaying the open capture as fast as possible,
        displaying the selected texture in a default unscaled manner to the given output window.
        
        The function won't return until :meth:`CancelReplayLoop` is called. Since this function is blocking, that
        function must be called from another thread.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ResourceId texid: The id of the texture to display.
        """
        pass
    
    
    def CreateRGPProfile(self, window: WindowingData) -> str:
        """
        Uses the given output window to create an RGP Profile.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :return: The path to the created RGP profile, or empty on failure
        :rtype: str
        """
        pass
    
    
    def CancelReplayLoop(self):
        """
        Cancels a replay loop begun in :meth:`ReplayLoop`. Does nothing if no loop is active.
        """
        pass
    
    
    def FileChanged(self):
        """
        Notify the interface that the file it has open has been changed on disk.
        """
        pass
    
    
    def SetFrameEvent(self, eventId: int, force: bool):
        """
        Move the replay to reflect the state immediately *after* the given
        :data:`eventId <APIEvent.eventId>`.
        
        :param int eventId: The :data:`eventId <APIEvent.eventId>` to move to.
        :param bool force: ``True`` if the internal replay should refresh even if the ``eventId`` is
          already current. This can be useful if external factors might cause the replay to vary.
        """
        pass
    
    
    def GetD3D11PipelineState(self) -> D3D11State:
        """
        Retrieve the current :class:`D3D11State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D11 API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current D3D11 pipeline state.
        :rtype: D3D11State
        """
        pass
    
    
    def GetD3D12PipelineState(self) -> D3D12State:
        """
        Retrieve the current :class:`D3D12State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D12 API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current D3D12 pipeline state.
        :rtype: D3D12State
        """
        pass
    
    
    def GetGLPipelineState(self) -> GLState:
        """
        Retrieve the current :class:`GLState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the OpenGL API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current OpenGL pipeline state.
        :rtype: GLState
        """
        pass
    
    
    def GetVulkanPipelineState(self) -> VKState:
        """
        Retrieve the current :class:`VKState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the Vulkan API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current Vulkan pipeline state.
        :rtype: VKState
        """
        pass
    
    
    def GetPipelineState(self) -> PipeState:
        """
        Retrieve the current :class:`PipeState` pipeline state abstraction.
        
        This pipeline state will always be valid, and allows queries that will work regardless of the
        capture's API.
        
        :return: The current pipeline state abstraction.
        :rtype: PipeState
        """
        pass
    
    
    def GetDescriptors(self, descriptorStore: ResourceId, ranges: List[DescriptorRange]) -> List[Descriptor]:
        """
        Retrieve the contents of a number of descriptors in a descriptor store. Multiple
        ranges within the store can be queried at once, and are returned in a contiguous array.
        
        :param ResourceId descriptorStore: The descriptor store to be queried from.
        :param List[DescriptorRange] ranges: The descriptor ranges to query.
        :return: The contents of the descriptors specified.
        :rtype: List[Descriptor]
        """
        pass
    
    
    def GetSamplerDescriptors(self, descriptorStore: ResourceId, ranges: List[DescriptorRange]) -> List[SamplerDescriptor]:
        """
        Retrieve the contents of a number of sampler descriptors in a descriptor store.
        Multiple ranges within the store can be queried at once, and are returned in a contiguous array.
        
        :param ResourceId descriptorStore: The descriptor store to be queried from.
        :param List[DescriptorRange] ranges: The descriptor ranges to query.
        :return: The contents of the descriptors specified.
        :rtype: List[SamplerDescriptor]
        """
        pass
    
    
    def GetDescriptorAccess(self) -> List[DescriptorAccess]:
        """
        Retrieve the descriptor accesses that happened at the current event.
        
        :return: The descriptor accesses.
        :rtype: List[DescriptorAccess]
        """
        pass
    
    
    def GetDescriptorLocations(self, descriptorStore: ResourceId, ranges: List[DescriptorRange]) -> List[DescriptorLogicalLocation]:
        """
        Retrieve the logical locations for descriptors in a given descriptor store.
        
        :param ResourceId descriptorStore: The descriptor store to be queried from.
        :param List[DescriptorRange] ranges: The descriptor ranges to query.
        :return: The descriptor logical locations.
        :rtype: List[DescriptorLogicalLocation]
        """
        pass
    
    
    def GetDisassemblyTargets(self, withPipeline: bool) -> List[str]:
        """
        Retrieve the list of possible disassembly targets for :meth:`DisassembleShader`. The
        values are implementation dependent but will always include a default target first which is the
        native disassembly of the shader. Further options may be available for additional disassembly views
        or hardware-specific ISA formats.
        
        :param bool withPipeline: More disassembly may be available when a pipeline is specified.
        :return: The list of disassembly targets available.
        :rtype: List[str]
        """
        pass
    
    
    def DisassembleShader(self, pipeline: ResourceId, refl: ShaderReflection, target: str) -> str:
        """
        Retrieve the disassembly for a given shader, for the given disassembly target.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ShaderReflection refl: The shader reflection details of the shader to disassemble
        :param str target: The name of the disassembly target to generate for. Must be one of the values
          returned by :meth:`GetDisassemblyTargets`, or empty to use the default generation.
        :return: The disassembly text, or an error message if something went wrong.
        :rtype: str
        """
        pass
    
    
    def SetCustomShaderIncludes(self, directories: List[str]):
        """
        Sets a list of directories to search for include files when compiling custom shaders
        with the internal shader compiler.
        
        .. note::
          This is currently only supported for D3D11 and D3D12. For Vulkan includes can be supported via
          configuring an external compiler to SPIR-V which is ingested.
        
        :param List[str] directories: The absolute paths of the directories.
        """
        pass
    
    
    def BuildCustomShader(self, entry: str, sourceEncoding: ShaderEncoding, source: bytes, compileFlags: ShaderCompileFlags, type: ShaderStage) -> Tuple[ResourceId, str]:
        """
        Builds a shader suitable for running on the local replay instance as a custom shader.
        
        System-level include directories can be set up via SetCustomShaderIncludes.
        
        See :data:`TextureDisplay.customShaderId`.
        
        :param str entry: The entry point to use when compiling.
        :param ShaderEncoding sourceEncoding: The encoding of the source data.
        :param bytes source: The source data itself.
        :param ShaderCompileFlags compileFlags: API-specific compilation flags.
        :param ShaderStage type: The stage that this shader will be executed at.
        :return: A ``tuple`` with the id of the new shader if compilation was successful,
          :meth:`ResourceId.Null` otherwise, and a ``str`` with any warnings/errors from compilation.
        :rtype: Tuple[ResourceId,str]
        """
        pass
    
    
    def FreeCustomShader(self, id: ResourceId):
        """
        Free a previously created custom shader.
        
        See :meth:`BuildCustomShader`.
        
        :param ResourceId id: The id of the custom shader to free.
        """
        pass
    
    
    def BuildTargetShader(self, entry: str, sourceEncoding: ShaderEncoding, source: bytes, compileFlags: ShaderCompileFlags, type: ShaderStage) -> Tuple[ResourceId, str]:
        """
        Builds a shader suitable for running in the capture's API as a replacement shader.
        
        :param str entry: The entry point to use when compiling.
        :param ShaderEncoding sourceEncoding: The encoding of the source data.
        :param bytes source: The source data itself.
        :param ShaderCompileFlags compileFlags: API-specific compilation flags.
        :param ShaderStage type: The stage that this shader will be executed at.
        :return: A ``tuple`` with the id of the new shader if compilation was successful,
          :meth:`ResourceId.Null` otherwise, and a ``str`` with any warnings/errors from compilation.
        :rtype: Tuple[ResourceId,str]
        """
        pass
    
    
    def GetTargetShaderEncodings(self) -> List[ShaderEncoding]:
        """
        Retrieve the list of supported :class:`ShaderEncoding` which can be build using
        :meth:`BuildTargetShader`.
        
        The list is sorted in priority order, so if the caller has a shader in a form but could
        compile/translate it to another, prefer to satisfy the first encoding before later encodings.
        
        This typically means the 'native' encoding is listed first, and then subsequent encodings are
        compiled internally - so compiling externally could be preferable as it allows better customisation
        of the compile process or using alternate/updated tools.
        
        :return: The list of target shader encodings available.
        :rtype: List[ShaderEncoding]
        """
        pass
    
    
    def GetCustomShaderEncodings(self) -> List[ShaderEncoding]:
        """
        Retrieve the list of supported :class:`ShaderEncoding` which can be build using
        :meth:`BuildCustomShader`.
        
        The list is sorted in priority order, so if the caller has a shader in a form but could
        compile/translate it to another, prefer to satisfy the first encoding before later encodings.
        
        This typically means the 'native' encoding is listed first, and then subsequent encodings are
        compiled internally - so compiling externally could be preferable as it allows better customisation
        of the compile process or using alternate/updated tools.
        
        :return: The list of target shader encodings available.
        :rtype: List[ShaderEncoding]
        """
        pass
    
    
    def GetCustomShaderSourcePrefixes(self) -> List[ShaderSourcePrefix]:
        """
        Retrieve a list of source prefixes that should be applied to custom shaders of each
        :class:`ShaderEncoding` before custom compilation prior to calling :meth:`BuildCustomShader`.
        
        This list provides source code prefixes which should be applied to a given custom shader in a
        :class:`ShaderEncoding` *if and only if* that shader is being compiled in a custom step to a
        different encoding, prior to being passed to :meth:`BuildCustomShader`. This allows source
        compatibility even when doing custom compilation.
        
        For example a shader written in :data:`ShaderEncoding.HLSL` may be custom compiled to
        :data:`ShaderEncoding.SPIRV` before being passed to :meth:`BuildCustomShader`. In this case any
        prefix for :data:`ShaderEncoding.HLSL` should be prepended to the source before custom compilation,
        to allow for defines and other helpers to be made available, since otherwise the shader may not
        compile.
        
        If a shader encoding is not in the list, no prefix is required. This may be possible even for a
        high level language such as :data:`ShaderEncoding.GLSL`.
        
        :return: A list of pairs, listing a prefix for each shader encoding referenced.
        :rtype: List[ShaderSourcePrefix]
        """
        pass
    
    
    def ReplaceResource(self, original: ResourceId, replacement: ResourceId):
        """
        Replace one resource with another for subsequent replay and analysis work.
        
        This is commonly used for modifying the capture by selectively replacing resources with newly
        created resources.
        
        See :meth:`BuildTargetShader`, :meth:`RemoveReplacement`.
        
        :param ResourceId original: The id of the resource that should be substituted.
        :param ResourceId replacement: The id of the new resource that should be used instead.
        """
        pass
    
    
    def ClearReplayCache(self):
        """
        Clear any cached data from previous replays and ensure subsequent replays fully
        re-initialise any data, including e.g. bindless feedback, printf results or mesh output data.
        """
        pass
    
    
    def ReloadShaderDebugInformation(self):
        """
        Reload the shader debug information for all shaders in the capture.
        """
        pass
    
    
    def RemoveReplacement(self, id: ResourceId):
        """
        Remove any previously specified replacement for an object.
        
        See :meth:`ReplaceResource`.
        
        :param ResourceId id: The id of the resource that was previously being substituted.
        """
        pass
    
    
    def FreeTargetResource(self, id: ResourceId):
        """
        Free a previously created target shader.
        
        See :meth:`BuildTargetShader`.
        
        :param ResourceId id: The id of the target shader to free.
        """
        pass
    
    
    def GetFrameInfo(self) -> FrameDescription:
        """
        Retrieve the information about the frame contained in the capture.
        
        :return: The frame information.
        :rtype: FrameDescription
        """
        pass
    
    
    def GetStructuredFile(self) -> SDFile:
        """
        Fetch the structured data representation of the capture loaded.
        
        :return: The structured file.
        :rtype: SDFile
        """
        pass
    
    
    def AddFakeMarkers(self):
        """
        Add fake marker regions to the list of actions in the capture, based on which
        textures are bound as outputs. Will not do anything if the capture already contains user marker
        regions.
        
        .. warning::
          This must be called *immediately* after capture load, calling it at a later time will cause
          corruption. No other functions should be called between load and this one.
        
        .. note::
          The event IDs for fake marker pushes and pops will not be contiguous with the surrounding actions
          and will be set to values above the last real event in the capture. This also means they break the
          typical rules that event IDs always increase. It's recommended that these events are not
          referenced directly in other calls such as SetFrameEvent, and fake markers should be used
          sparingly at all compared to proper application-provided markers.
        """
        pass
    
    
    def GetRootActions(self) -> List[ActionDescription]:
        """
        Retrieve the list of root-level actions in the capture.
        
        :return: The list of root-level actions in the capture.
        :rtype: List[ActionDescription]
        """
        pass
    
    
    def FetchCounters(self, counters: List[GPUCounter]) -> List[CounterResult]:
        """
        Retrieve the values of a specified set of counters.
        
        :param List[GPUCounter] counters: The list of counters to fetch results for.
        :return: The list of counter results generated.
        :rtype: List[CounterResult]
        """
        pass
    
    
    def EnumerateCounters(self) -> List[GPUCounter]:
        """
        Retrieve a list of which counters are available in the current capture analysis
        implementation.
        
        :return: The list of counters available.
        :rtype: List[GPUCounter]
        """
        pass
    
    
    def DescribeCounter(self, counter: GPUCounter) -> CounterDescription:
        """
        Get information about what a counter actually represents, in terms of a human-readable
        understanding as well as the type and unit of the resulting information.
        
        :param GPUCounter counter: The counter to query about.
        :return: The description of the counter.
        :rtype: CounterDescription
        """
        pass
    
    
    def GetResources(self) -> List[ResourceDescription]:
        """
        Retrieve the list of all resources in the capture.
        
        This includes any object allocated a :class:`ResourceId`, that don't have any other state or
        are only used as intermediary elements.
        
        :return: The list of resources in the capture.
        :rtype: List[ResourceDescription]
        """
        pass
    
    
    def GetTextures(self) -> List[TextureDescription]:
        """
        Retrieve the list of textures alive in the capture.
        
        :return: The list of textures in the capture.
        :rtype: List[TextureDescription]
        """
        pass
    
    
    def GetBuffers(self) -> List[BufferDescription]:
        """
        Retrieve the list of buffers alive in the capture.
        
        :return: The list of buffers in the capture.
        :rtype: List[BufferDescription]
        """
        pass
    
    
    def GetDescriptorStores(self) -> List[DescriptorStoreDescription]:
        """
        Retrieve the list of descriptor storage objects alive in the capture.
        
        :return: The list of descriptor storage objects in the capture.
        :rtype: List[DescriptorStoreDescription]
        """
        pass
    
    
    def GetDebugMessages(self) -> List[DebugMessage]:
        """
        Retrieve a list of any newly generated diagnostic messages.
        
        Every time this function is called, any debug messages returned will not be returned again. Only
        newly generated messages will be returned after that.
        
        :return: The list of the :class:`DebugMessage` messages.
        :rtype: List[DebugMessage]
        """
        pass
    
    
    def GetFatalErrorStatus(self) -> ResultDetails:
        """
        Poll for the current status of the replay.
        
        This function can be used to monitor to see if a fatal error has been encountered and react
        appropriately, such as by displaying a message to the user. The replay controller interface should
        remain stable and return null/empty data for the most part, but it's recommended for maximum
        stability to stop using the controller when a fatal error is encountered.
        
        If there has been no error, this will return :data:`ResultCode.Succeeded`. If there has been an
        error this will return the error code every time, it will not be 'consumed' so it's safe to have
        multiple things checking it.
        
        :return: The current fatal error status.
        :rtype: ResultDetails
        """
        pass
    
    
    def GetShaderEntryPoints(self, shader: ResourceId) -> List[ShaderEntryPoint]:
        """
        Retrieve a list of entry points for a shader.
        
        If the given ID doesn't specify a shader, an empty list will be return. On some APIs, the list will
        only ever have one result (only one entry point per shader).
        
        :param ResourceId shader: The shader to look up entry points for.
        :return: The list of the :class:`ShaderEntryPoint` messages.
        :rtype: List[ShaderEntryPoint]
        """
        pass
    
    
    def GetShader(self, pipeline: ResourceId, shader: ResourceId, entry: ShaderEntryPoint) -> ShaderReflection:
        """
        Retrieve the information about the frame contained in the capture.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ResourceId shader: The shader to get reflection data for.
        :param ShaderEntryPoint entry: The entry point within the shader to reflect. May be ignored on some
          APIs
        :return: The frame information.
        :rtype: ShaderReflection
        """
        pass
    
    
    def PickPixel(self, textureId: ResourceId, x: int, y: int, sub: Subresource, typeCast: CompType) -> PixelValue:
        """
        Retrieve the contents of a particular pixel in a texture.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param ResourceId textureId: The texture to pick the pixel from.
        :param int x: The x co-ordinate to pick from.
        :param int y: The y co-ordinate to pick from.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :return: The contents of the pixel.
        :rtype: PixelValue
        """
        pass
    
    
    def GetMinMax(self, textureId: ResourceId, sub: Subresource, typeCast: CompType) -> Tuple[PixelValue, PixelValue]:
        """
        Retrieves the minimum and maximum values in the specified texture.
        
        :param ResourceId textureId: The texture to get the values from.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :return: A tuple with the minimum and maximum pixel values respectively.
        :rtype: Tuple[PixelValue,PixelValue]
        """
        pass
    
    
    def GetHistogram(self, textureId: ResourceId, sub: Subresource, typeCast: CompType, minval: float, maxval: float, channels: Tuple[bool, bool, bool, bool]) -> List[int]:
        """
        Retrieve a list of values that can be used to show a histogram of values for the
        specified texture.
        
        The output list contains N buckets, and each bucket has the number of pixels that falls in each
        bucket when the pixel values are divided between ``minval`` and ``maxval``.
        
        :param ResourceId textureId: The texture to get the histogram from.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :param float minval: The lower end of the smallest bucket. If any values are below this, they are
          not added to any bucket.
        :param float maxval: The upper end of the largest bucket. If any values are above this, they are
          not added to any bucket.
        :param Tuple[bool,bool,bool,bool] channels: A set of four flags indicating whether each of RGBA
          respectively should be included in the count.
        :return: A list of the unnormalised bucket values.
        :rtype: List[int]
        """
        pass
    
    
    def PixelHistory(self, texture: ResourceId, x: int, y: int, sub: Subresource, typeCast: CompType) -> List[PixelModification]:
        """
        Retrieve the history of modifications to the selected pixel on the selected texture.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param ResourceId texture: The texture to search for modifications.
        :param int x: The x co-ordinate.
        :param int y: The y co-ordinate.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :return: The list of pixel history events.
        :rtype: List[PixelModification]
        """
        pass
    
    
    def DebugVertex(self, vertid: int, instid: int, idx: int, view: int) -> ShaderDebugTrace:
        """
        Retrieve a debugging trace from running a vertex shader.
        
        :param int vertid: The vertex ID as a 0-based index up to the number of vertices in the draw.
        :param int instid: The instance ID as a 0-based index up to the number of instances in the draw.
        :param int idx: The actual index used to look up vertex inputs, either from the vertex ID for non-
          indexed draws or drawn from the index buffer. This must have all drawcall offsets applied.
        :param int view: The index of the multiview viewport to use, or 0 if multiview is not in use.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass
    
    
    def DebugPixel(self, x: int, y: int, inputs: DebugPixelInputs) -> ShaderDebugTrace:
        """
        Retrieve a debugging trace from running a pixel shader.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param int x: The x co-ordinate.
        :param int y: The y co-ordinate.
        :param DebugPixelInputs inputs: Specific properties to select which fragment to debug e.g.
          sample: The multi-sampled sample. Ignored if non-multisampled texture.
          primitive: Debug the pixel from this primitive if there's ambiguity. If set to
          :data:`NoPreference` then a random fragment writing to the given co-ordinate is debugged.
          view: Debug the fragment writing to this view for layered or multiview rendering,
          ignored if set to :data:`NoPreference`.
        :return: The resulting trace resulting from debugging. Destroy with :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass
    
    
    def DebugThread(self, groupid: Tuple[int, int, int], threadid: Tuple[int, int, int]) -> ShaderDebugTrace:
        """
        Retrieve a debugging trace from running a compute thread.
        
        :param Tuple[int,int,int] groupid: A list containing the 3D workgroup index.
        :param Tuple[int,int,int] threadid: A list containing the 3D thread index within the workgroup.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass
    
    
    def DebugMeshThread(self, groupid: Tuple[int, int, int], threadid: Tuple[int, int, int]) -> ShaderDebugTrace:
        """
        Retrieve a debugging trace from running a mesh shader.
        
        :param Tuple[int,int,int] groupid: A list containing the 3D workgroup index.
        :param Tuple[int,int,int] threadid: A list containing the 3D thread index within the workgroup.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass
    
    
    def ContinueDebug(self, debugger: ShaderDebugger) -> List[ShaderDebugState]:
        """
        Continue a shader's debugging with a given shader debugger instance. This will run an
        implementation defined number of steps and then return those steps in a list. This may be a fixed
        number of steps or it may run for a fixed length of time and return as many steps as can be
        calculated in that time.
        
        This will always perform at least one step. If the list is empty, the debugging process has
        completed, further calls will return an empty list.
        
        :param ShaderDebugger debugger: The shader debugger to continue running.
        :return: A number of subsequent states.
        :rtype: List[ShaderDebugState]
        """
        pass
    
    
    def FreeTrace(self, trace: ShaderDebugTrace):
        """
        Free a debugging trace from running a shader invocation debug.
        
        :param ShaderDebugTrace trace: The shader debugging trace to free.
        """
        pass
    
    
    def GetUsage(self, id: ResourceId) -> List[EventUsage]:
        """
        Retrieve a list of ways a given resource is used.
        
        :param ResourceId id: The id of the texture or buffer resource to be queried.
        :return: The list of usages of the resource.
        :rtype: List[EventUsage]
        """
        pass
    
    
    def GetCBufferVariableContents(self, pipeline: ResourceId, shader: ResourceId, stage: ShaderStage, entryPoint: str, cbufslot: int, buffer: ResourceId, offset: int, length: int) -> List[ShaderVariable]:
        """
        Retrieve the contents of a constant block by reading from memory or their source
        otherwise.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ResourceId shader: The id of the shader to use for metadata.
        :param ShaderStage stage: The shader stage to fetch variables from.
        :param str entryPoint: The entry point of the shader being used. In some APIs, this is ignored.
        :param int cbufslot: The index in the :data:`ShaderReflection.constantBlocks` list to look up.
        :param ResourceId buffer: The id of the buffer to use for data. If
          :data:`ConstantBlock.bufferBacked` is ``False`` this is ignored.
        :param int offset: Retrieve buffer contents starting at this byte offset.
        :param int length: Retrieve this many bytes after :paramref:`GetCBufferVariableContents.offset`.
          May be 0 to fetch the rest of the buffer.
        :return: The shader variables with their contents.
        :rtype: List[ShaderVariable]
        """
        pass
    
    
    def SaveTexture(self, saveData: TextureSave, path: str) -> ResultDetails:
        """
        Save a texture to a file on disk, with possible transformation to map a complex
        texture to something compatible with the target file format.
        
        :param TextureSave saveData: The configuration settings of which texture to save, and how
        :param str path: The path to save to on disk.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass
    
    
    def GetPostVSData(self, instance: int, view: int, stage: MeshDataStage) -> MeshFormat:
        """
        Retrieve the generated data from one of the geometry processing shader stages.
        
        :param int instance: The index of the instance to retrieve data for, or 0 for non-instanced draws.
        :param int view: The index of the multiview view to retrieve data for, or 0 if multiview is disabled.
        :param MeshDataStage stage: The stage of the geometry processing pipeline to retrieve data from.
        :return: The information describing where the post-transform data is stored.
        :rtype: MeshFormat
        """
        pass
    
    
    def GetBufferData(self, buff: ResourceId, offset: int, len: int) -> bytes:
        """
        Retrieve the contents of a range of a buffer as a ``bytes``.
        
        :param ResourceId buff: The id of the buffer to retrieve data from.
        :param int offset: The byte offset to the start of the range.
        :param int len: The length of the range, or 0 to retrieve the rest of the bytes in the buffer.
        :return: The requested buffer contents.
        :rtype: bytes
        """
        pass
    
    
    def GetTextureData(self, tex: ResourceId, sub: Subresource) -> bytes:
        """
        Retrieve the contents of one subresource of a texture as a ``bytes``.
        
        .. note:: For 3D textures a whole width x height x depth mip is returned, you can't select a single
          depth slice using :data:`Subresource.slice`.
        
        :param ResourceId tex: The id of the texture to retrieve data from.
        :param Subresource sub: The subresource within this texture to use.
        :return: The requested texture contents.
        :rtype: bytes
        """
        pass
    
