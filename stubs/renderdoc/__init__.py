# Stubs for {module.__name__}

from typing import Any, Callable, List, Tuple

# Dummy types
from typing import NewType, Optional
ANativeWindow = Optional[NewType('ANativeWindow', int)]
CALayer = Optional[NewType('CALayer', int)]
Display = Optional[NewType('Display', int)]
Drawable = Optional[NewType('Drawable', int)]
HWND = Optional[NewType('HWND', int)]
NSView = Optional[NewType('NSView', int)]
wl_display = Optional[NewType('wl_display', int)]
wl_surface = Optional[NewType('wl_surface', int)]
xcb_connection_t = Optional[NewType('xcb_connection_t', int)]
xcb_window_t = Optional[NewType('xcb_window_t', int)]

# Classes
from ._APIEvent import APIEvent
from ._APIProperties import APIProperties
from ._APIUseData import APIUseData
from ._ActionDescription import ActionDescription
from ._ActionFlags import ActionFlags
from ._AddressMode import AddressMode
from ._AlphaMapping import AlphaMapping
from ._AndroidFlags import AndroidFlags
from ._AxisMapping import AxisMapping
from ._BindType import BindType
from ._BlendEquation import BlendEquation
from ._BlendMultiplier import BlendMultiplier
from ._BlendOperation import BlendOperation
from ._BlendStats import BlendStats
from ._BoundVBuffer import BoundVBuffer
from ._BucketRecordType import BucketRecordType
from ._BufferCategory import BufferCategory
from ._BufferDescription import BufferDescription
from ._BusyData import BusyData
from ._Camera import Camera
from ._CameraType import CameraType
from ._CaptureAccess import CaptureAccess
from ._CaptureFile import CaptureFile
from ._CaptureFileFormat import CaptureFileFormat
from ._CaptureOptions import CaptureOptions
from ._ChromaSampleLocation import ChromaSampleLocation
from ._ColorBlend import ColorBlend
from ._CompType import CompType
from ._CompareFunction import CompareFunction
from ._ConservativeRaster import ConservativeRaster
from ._ConstantBindStats import ConstantBindStats
from ._ConstantBlock import ConstantBlock
from ._CounterDescription import CounterDescription
from ._CounterResult import CounterResult
from ._CounterUnit import CounterUnit
from ._CounterValue import CounterValue
from ._CullMode import CullMode
from ._D3D11BlendState import D3D11BlendState
from ._D3D11DepthStencilState import D3D11DepthStencilState
from ._D3D11IndexBuffer import D3D11IndexBuffer
from ._D3D11InputAssembly import D3D11InputAssembly
from ._D3D11Layout import D3D11Layout
from ._D3D11OutputMerger import D3D11OutputMerger
from ._D3D11Predication import D3D11Predication
from ._D3D11Rasterizer import D3D11Rasterizer
from ._D3D11RasterizerState import D3D11RasterizerState
from ._D3D11Shader import D3D11Shader
from ._D3D11State import D3D11State
from ._D3D11StreamOut import D3D11StreamOut
from ._D3D11StreamOutBind import D3D11StreamOutBind
from ._D3D11VertexBuffer import D3D11VertexBuffer
from ._D3D12BlendState import D3D12BlendState
from ._D3D12DepthStencilState import D3D12DepthStencilState
from ._D3D12IndexBuffer import D3D12IndexBuffer
from ._D3D12InputAssembly import D3D12InputAssembly
from ._D3D12Layout import D3D12Layout
from ._D3D12OM import D3D12OM
from ._D3D12Predication import D3D12Predication
from ._D3D12Rasterizer import D3D12Rasterizer
from ._D3D12RasterizerState import D3D12RasterizerState
from ._D3D12ResourceData import D3D12ResourceData
from ._D3D12ResourceState import D3D12ResourceState
from ._D3D12RootParam import D3D12RootParam
from ._D3D12RootSignature import D3D12RootSignature
from ._D3D12RootTableRange import D3D12RootTableRange
from ._D3D12Shader import D3D12Shader
from ._D3D12State import D3D12State
from ._D3D12StaticSampler import D3D12StaticSampler
from ._D3D12StreamOut import D3D12StreamOut
from ._D3D12StreamOutBind import D3D12StreamOutBind
from ._D3D12VertexBuffer import D3D12VertexBuffer
from ._DebugMessage import DebugMessage
from ._DebugOverlay import DebugOverlay
from ._DebugPixelInputs import DebugPixelInputs
from ._DebugVariableReference import DebugVariableReference
from ._DebugVariableType import DebugVariableType
from ._DepthBiasMode import DepthBiasMode
from ._DepthStencilStats import DepthStencilStats
from ._DepthTestState import DepthTestState
from ._Descriptor import Descriptor
from ._DescriptorAccess import DescriptorAccess
from ._DescriptorCategory import DescriptorCategory
from ._DescriptorFlags import DescriptorFlags
from ._DescriptorLogicalLocation import DescriptorLogicalLocation
from ._DescriptorRange import DescriptorRange
from ._DescriptorStoreDescription import DescriptorStoreDescription
from ._DescriptorType import DescriptorType
from ._DeviceProtocolController import DeviceProtocolController
from ._DispatchStats import DispatchStats
from ._DrawcallStats import DrawcallStats
from ._DriverInformation import DriverInformation
from ._EnvMod import EnvMod
from ._EnvSep import EnvSep
from ._EnvironmentModification import EnvironmentModification
from ._EventUsage import EventUsage
from ._ExecuteResult import ExecuteResult
from ._FileType import FileType
from ._FillMode import FillMode
from ._FilterFunction import FilterFunction
from ._FilterMode import FilterMode
from ._FloatVector import FloatVector
from ._FrameDescription import FrameDescription
from ._FrameStatistics import FrameStatistics
from ._GLBlendState import GLBlendState
from ._GLDepthState import GLDepthState
from ._GLFBO import GLFBO
from ._GLFeedback import GLFeedback
from ._GLFixedVertexProcessing import GLFixedVertexProcessing
from ._GLFrameBuffer import GLFrameBuffer
from ._GLHints import GLHints
from ._GLRasterizer import GLRasterizer
from ._GLRasterizerState import GLRasterizerState
from ._GLShader import GLShader
from ._GLState import GLState
from ._GLStencilState import GLStencilState
from ._GLTextureCompleteness import GLTextureCompleteness
from ._GLVertexAttribute import GLVertexAttribute
from ._GLVertexBuffer import GLVertexBuffer
from ._GLVertexInput import GLVertexInput
from ._GPUCounter import GPUCounter
from ._GPUDevice import GPUDevice
from ._GPUVendor import GPUVendor
from ._GlobalEnvironment import GlobalEnvironment
from ._GraphicsAPI import GraphicsAPI
from ._IndexBindStats import IndexBindStats
from ._InstructionSourceInfo import InstructionSourceInfo
from ._KnownShaderTool import KnownShaderTool
from ._LayoutBindStats import LayoutBindStats
from ._LineColumnInfo import LineColumnInfo
from ._LineRaster import LineRaster
from ._LogType import LogType
from ._LogicOperation import LogicOperation
from ._MeshDataStage import MeshDataStage
from ._MeshDisplay import MeshDisplay
from ._MeshFormat import MeshFormat
from ._MeshletSize import MeshletSize
from ._MessageCategory import MessageCategory
from ._MessageSeverity import MessageSeverity
from ._MessageSource import MessageSource
from ._ModificationValue import ModificationValue
from ._NewCaptureData import NewCaptureData
from ._NewChildData import NewChildData
from ._Offset import Offset
from ._OutputTargetStats import OutputTargetStats
from ._PathEntry import PathEntry
from ._PathProperty import PathProperty
from ._PipeState import PipeState
from ._PixelModification import PixelModification
from ._PixelValue import PixelValue
from ._PointerVal import PointerVal
from ._QualityHint import QualityHint
from ._RasterState import RasterState
from ._RasterizationStats import RasterizationStats
from ._RemoteServer import RemoteServer
from ._ReplayController import ReplayController
from ._KillCallback import KillCallback
from ._ProgressCallback import ProgressCallback
from ._PreviewWindowCallback import PreviewWindowCallback
from ._ReplayOptimisationLevel import ReplayOptimisationLevel
from ._ReplayOptions import ReplayOptions
from ._ReplayOutput import ReplayOutput
from ._ReplayOutputType import ReplayOutputType
from ._ReplaySupport import ReplaySupport
from ._ResourceBindStats import ResourceBindStats
from ._ResourceDescription import ResourceDescription
from ._ResourceFormat import ResourceFormat
from ._ResourceFormatType import ResourceFormatType
from ._ResourceId import ResourceId
from ._ResourceType import ResourceType
from ._ResourceUpdateStats import ResourceUpdateStats
from ._ResourceUsage import ResourceUsage
from ._ResultCode import ResultCode
from ._ResultDetails import ResultDetails
from ._SDBasic import SDBasic
from ._SDChunk import SDChunk
from ._SDChunkFlags import SDChunkFlags
from ._SDChunkMetaData import SDChunkMetaData
from ._SDFile import SDFile
from ._SDObject import SDObject
from ._SDObjectData import SDObjectData
from ._SDObjectPODData import SDObjectPODData
from ._SDType import SDType
from ._SDTypeFlags import SDTypeFlags
from ._SamplerBindStats import SamplerBindStats
from ._SamplerDescriptor import SamplerDescriptor
from ._Scissor import Scissor
from ._SectionFlags import SectionFlags
from ._SectionProperties import SectionProperties
from ._SectionType import SectionType
from ._ShaderBindIndex import ShaderBindIndex
from ._ShaderBuiltin import ShaderBuiltin
from ._ShaderChangeStats import ShaderChangeStats
from ._ShaderCompileFlag import ShaderCompileFlag
from ._ShaderCompileFlags import ShaderCompileFlags
from ._ShaderComputeMessageLocation import ShaderComputeMessageLocation
from .renderdoc_circular1 import ShaderConstant
from .renderdoc_circular1 import ShaderConstantType
from ._ShaderDebugInfo import ShaderDebugInfo
from ._ShaderDebugState import ShaderDebugState
from ._ShaderDebugTrace import ShaderDebugTrace
from ._ShaderDebugger import ShaderDebugger
from ._ShaderDirectAccess import ShaderDirectAccess
from ._ShaderEncoding import ShaderEncoding
from ._ShaderEntryPoint import ShaderEntryPoint
from ._ShaderEvents import ShaderEvents
from ._ShaderGeometryMessageLocation import ShaderGeometryMessageLocation
from ._ShaderMeshMessageLocation import ShaderMeshMessageLocation
from ._ShaderMessage import ShaderMessage
from ._ShaderMessageLocation import ShaderMessageLocation
from ._ShaderPixelMessageLocation import ShaderPixelMessageLocation
from ._ShaderReflection import ShaderReflection
from ._ShaderResource import ShaderResource
from ._ShaderSampler import ShaderSampler
from ._ShaderSourceFile import ShaderSourceFile
from ._ShaderSourcePrefix import ShaderSourcePrefix
from ._ShaderStage import ShaderStage
from ._ShaderStageMask import ShaderStageMask
from ._ShaderValue import ShaderValue
from ._ShaderVariable import ShaderVariable
from ._ShaderVariableChange import ShaderVariableChange
from ._ShaderVariableFlags import ShaderVariableFlags
from ._ShaderVertexMessageLocation import ShaderVertexMessageLocation
from ._ShadingRateCombiner import ShadingRateCombiner
from ._SigParameter import SigParameter
from ._SourceVariableMapping import SourceVariableMapping
from ._StencilFace import StencilFace
from ._StencilOperation import StencilOperation
from ._StructuredBufferList import StructuredBufferList
from ._StructuredChunkList import StructuredChunkList
from ._StructuredObjectList import StructuredObjectList
from ._Subresource import Subresource
from ._TargetControl import TargetControl
from ._TargetControlMessage import TargetControlMessage
from ._TargetControlMessageType import TargetControlMessageType
from ._TaskGroupSize import TaskGroupSize
from ._TextureCategory import TextureCategory
from ._TextureComponentMapping import TextureComponentMapping
from ._TextureDescription import TextureDescription
from ._TextureDisplay import TextureDisplay
from ._TextureFilter import TextureFilter
from ._TextureSampleMapping import TextureSampleMapping
from ._TextureSave import TextureSave
from ._TextureSliceMapping import TextureSliceMapping
from ._TextureSwizzle import TextureSwizzle
from ._TextureSwizzle4 import TextureSwizzle4
from ._TextureType import TextureType
from ._Thumbnail import Thumbnail
from ._Topology import Topology
from ._UsedDescriptor import UsedDescriptor
from ._Uuid import Uuid
from ._VKColorBlendState import VKColorBlendState
from ._VKConditionalRendering import VKConditionalRendering
from ._VKCurrentPass import VKCurrentPass
from ._VKDepthStencil import VKDepthStencil
from ._VKDescriptorBuffer import VKDescriptorBuffer
from ._VKDescriptorSet import VKDescriptorSet
from ._VKDynamicOffset import VKDynamicOffset
from ._VKFramebuffer import VKFramebuffer
from ._VKImageData import VKImageData
from ._VKImageLayout import VKImageLayout
from ._VKIndexBuffer import VKIndexBuffer
from ._VKInputAssembly import VKInputAssembly
from ._VKMultiSample import VKMultiSample
from ._VKPipeline import VKPipeline
from ._VKRasterizer import VKRasterizer
from ._VKRenderArea import VKRenderArea
from ._VKRenderPass import VKRenderPass
from ._VKSampleLocations import VKSampleLocations
from ._VKShader import VKShader
from ._VKState import VKState
from ._VKTessellation import VKTessellation
from ._VKTransformFeedback import VKTransformFeedback
from ._VKVertexAttribute import VKVertexAttribute
from ._VKVertexBinding import VKVertexBinding
from ._VKVertexBuffer import VKVertexBuffer
from ._VKVertexInput import VKVertexInput
from ._VKViewState import VKViewState
from ._VKViewportScissor import VKViewportScissor
from ._VKXFBBuffer import VKXFBBuffer
from ._VarType import VarType
from ._VertexBindStats import VertexBindStats
from ._VertexInputAttribute import VertexInputAttribute
from ._Viewport import Viewport
from ._Visualisation import Visualisation
from ._VulkanLayerFlags import VulkanLayerFlags
from ._VulkanLayerRegistrationInfo import VulkanLayerRegistrationInfo
from ._WindowingData import WindowingData
from ._WindowingSystem import WindowingSystem
from ._YcbcrConversion import YcbcrConversion
from ._YcbcrRange import YcbcrRange

# Functions


def BecomeRemoteServer(listenhost: str, port: int, killReplay: Callable[[], bool], previewWindow: Callable[[bool], WindowingData]):
    """
    This launches a remote server which will continually run in a loop to server requests
    from external sources.
    
    This function will block until a remote connection tells the server to shut down, or the
    ``killReplay`` callback returns ``True``.
    
    :param str listenhost: The name of the interface to listen on.
    :param int port: The port to listen on, or ``0`` to listen on the default port.
    :param Callable[[], bool] killReplay: A callback that returns a ``bool`` indicating if the server should
      be shut down or not.
      Callback function signature must match :func:`KillCallback`.
    :param Callable[[bool], WindowingData] previewWindow: A callback that returns information for a preview window
      when the server wants to display some preview of the ongoing replay.
      Callback function signature must match :func:`PreviewWindowCallback`.
    """
    pass



def CBUsage(stage: ShaderStage) -> ResourceUsage:
    """
    Calculate the ``ResourceUsage`` value for constant buffer use at a given shader stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for constant buffer usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass



def CanGlobalHook() -> bool:
    """
    Determines if the global hook is supported on the current platform and configuration.
    
    :return: ``True`` if global hooking can be used on the platform, ``False`` if not.
    :rtype: bool
    """
    pass



def CanSelfHostedCapture(dllname: str) -> bool:
    """
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function checks to see if a given self-hosted DLL is available.
    
    :param str dllname: The name of the self-hosted capture module.
    :return: Whether the specified DLL is loaded, ready for self-hosted capture.
    :rtype: bool
    """
    pass



def CategoryForDescriptorType(type: DescriptorType) -> DescriptorCategory:
    """
    Get the shader interface category for a given type of descriptor.
    
    :param DescriptorType type: The type of descriptor
    :return: The descriptor category.
    :rtype: DescriptorCategory
    """
    pass



def CheckAndroidPackage():
    """
    INTERNAL: Check remote Android package for requirements
    """
    pass



def CheckRemoteServerConnection(URL: str) -> ResultDetails:
    """
    Check the connection to a remote server running on given hostname.
    
    This should be preferred to :func:`CreateRemoteServerConnection` when no connection is desired, as
    the status can be checked without interfering with making connections.
    
    :param str URL: The hostname to connect to, if blank then localhost is used. If no protocol is
      specified then default TCP enumeration happens.
    :return: The status of the server.
    :rtype: ResultDetails
    """
    pass



def CreateAndroidWindowingData(window: ANativeWindow) -> WindowingData:
    """
    Create a :class:`WindowingData` for an Android ``ANativeWindow`` handle.
    
    :param ANativeWindow window: The native ``ANativeWindow`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def CreateHeadlessWindowingData(width: int, height: int) -> WindowingData:
    """
    Create a :class:`WindowingData` for no backing window, it will be headless.
    
    :param int width: The initial width for this virtual window.
    :param int height: The initial height for this virtual window.
    
    :return: A :class:`WindowingData` corresponding to an 'empty' backing window.
    :rtype: WindowingData
    """
    pass



def CreateMacOSWindowingData(view: NSView, layer: CALayer) -> WindowingData:
    """
    Create a :class:`WindowingData` for an Metal/OpenGL-compatible macOS ``CALayer`` handle
    and ``NSView`` handle (as void pointers).
    
    :param NSView view: The native ``NSView`` handle for this window.
    :param CALayer layer: The native ``CALayer`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def CreateRemoteServerConnection(URL: str) -> Tuple[ResultDetails, RemoteServer]:
    """
    Create a connection to a remote server running on given hostname.
    
    :param str URL: The hostname to connect to, if blank then localhost is used. If no protocol is
      specified then default TCP enumeration happens.
    :return: The status of opening the connection, whether success or failure, and a :class:`RemoteServer`
      instance if it were successful
    :rtype: Tuple[ResultDetails,RemoteServer]
    """
    pass



def CreateTargetControl(URL: str, ident: int, clientName: str, forceConnection: bool) -> TargetControl:
    """
    Creates a :class:`TargetControl` connection to a given hostname and ident.
    
    This function will block until the control connection is ready, or an error occurs.
    
    :param str URL: The URL to connect to. If blank, the local machine is used. If no protocol is
      specified then default TCP enumeration happens.
    :param int ident: The ident for the particular target to connect to on that machine.
    :param str clientName: The client name to use when connecting. See
      :meth:`TargetControl.GetBusyClient`.
    :param bool forceConnection: Force the connection and kick off any existing client that is currently
      connected.
    :return: A handle to the target control connection, or ``None`` if something went wrong.
    :rtype: TargetControl
    """
    pass



def CreateWaylandWindowingData(display: wl_display, window: wl_surface) -> WindowingData:
    """
    Create a :class:`WindowingData` for an Wayland ``wl_surface`` handle.
    
    :param wl_display display: The ``wl_display`` connection used for this window.
    :param wl_surface window: The native ``wl_surface`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def CreateWin32WindowingData(window: HWND) -> WindowingData:
    """
    Create a :class:`WindowingData` for a Win32 ``HWND`` handle.
    
    :param HWND window: The native ``HWND`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def CreateXCBWindowingData(connection: xcb_connection_t, window: xcb_window_t) -> WindowingData:
    """
    Create a :class:`WindowingData` for an XCB ``xcb_window_t`` handle.
    
    :param xcb_connection_t connection: The ``xcb_connection_t`` connection used for this window.
    :param xcb_window_t window: The native ``xcb_window_t`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def CreateXlibWindowingData(display: Display, window: Drawable) -> WindowingData:
    """
    Create a :class:`WindowingData` for an Xlib ``Drawable`` handle.
    
    :param Display display: The ``Display`` connection used for this window.
    :param Drawable window: The native ``Drawable`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass



def DumpObject(obj: Any) -> str:
    """
    Returns a string representation of an object. This is quite similar to
    the built-in ``repr()`` function but it iterates over struct members and prints them out, where normally
    ``repr()`` would stop and say something like 'Swig Object of type ...'.
    
    :param Any obj: The object to dump
    :return: The string representation of the object.
    :rtype: str
    """
    pass



def EndSelfHostCapture(dllname: str):
    """
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to end a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass



def EnumerateRemoteTargets(URL: str, nextIdent: int) -> int:
    """
    Repeatedly query to enumerate which targets are active on a given machine and their
    idents.
    
    Initially this should be called with ``nextIdent`` being 0, to retrieve the first target
    active. After that it can be called again and again with the previous return value to enumerate
    more targets.
    
    This function will block for a variable timeout depending on how many targets are scanned.
    
    :param str URL: The URL to connect to. If blank, the local machine is used. If no protocol is
      specified then default TCP enumeration happens.
    :param int nextIdent: The next ident to scan.
    :return: The ident of the next active target, or ``0`` if no other targets exist.
    :rtype: int
    """
    pass



def ExecuteAndInject(app: str, workingDir: str, cmdLine: str, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions, waitForExit: bool) -> ExecuteResult:
    """
    Launch an application and inject into it to allow capturing.
    
    :param str app: The path to the application to run.
    :param str workingDir: The working directory to use when running the application. If blank, the
      directory containing the application is used.
    :param str cmdLine: The command line to use when running the application, it will be processed in a
      platform specific way to generate arguments.
    :param List[EnvironmentModification] env: Any environment changes that should be made when running
      the program.
    :param str capturefile: The capture file path template, or blank to use a default location.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :param bool waitForExit: If ``True`` this function will block until the process exits.
    :return: The :class:`ExecuteResult` indicating both the status of the operation (success or failure)
      and any reason for failure, or else the ident where the new application is listening for target
      control if everything succeeded.
    :rtype: ExecuteResult
    """
    pass



def FirstStageForMask(stageMask: ShaderStageMask) -> ShaderStage:
    """
    For a shader stage mask that only covers one shader stage, return the shader stage.
    
    .. note::
      If the shader stage mask covers multiple stages, only the first matching stage will be returned.
      If the mask is empty, :data:`ShaderStage.Invalid` will be returned.
    
    :param ShaderStageMask stageMask: The shader stage mask.
    :return: The first shader stage covered by the mask.
    :rtype: ShaderStage
    """
    pass



def FloatToHalf(flt: float) -> int:
    """
    A utility function that converts a float to a half (stored in a 16-bit unsigned
    integer).
    
    :param float flt: The floating point value.
    :return: The nearest half-float equivalent stored as an int.
    :rtype: int
    """
    pass



def GPUVendorFromPCIVendor(vendorID: int) -> GPUVendor:
    """
    Get the GPUVendor for a given PCI Vendor ID.
    
    :param int vendorID: The PCI Vendor ID
    :return: The vendor identified
    :rtype: GPUVendor
    """
    pass



def GetCommitHash() -> str:
    """
    Retrieves the commit hash used to build.
    
    This will be in the form ``0123456789abcdef0123456789abcdef01234567``
    
    :return: The commit hash.
    :rtype: str
    """
    pass



def GetConfigSetting(name: str) -> SDObject:
    """
    Return a read-only handle to the :class:`SDObject` corresponding to a given setting's
    value object.
    
    If an empty string is passed, the root object is returned containing all settings and setting
    categories. Categories contain other categories and settings, settings contain children that include
    the setting's value, description, etc.
    
    If no such setting exists, `None` is returned.
    
    :param str name: The name of the setting.
    :return: The specified setting.
    :rtype: SDObject
    """
    pass



def GetCurrentProcessMemoryUsage() -> int:
    """
    Returns the current process's memory usage in bytes
    
    :return: The current memory usage in bytes.
    :rtype: int
    """
    pass



def GetDeviceProtocolController(protocol: str) -> DeviceProtocolController:
    """
    Creates a :class:`DeviceProtocolController` that provides device-specific controls.
    
    This interface is intended to allow closer integration with remote devices.
    
    .. note::
      Note that the use of scripting with Android is explicitly **not supported** due to the inherent
      fragility and unreliability of the Android platform. This interface is designed primarily for
      internal use and no support will be provided for Android-specific problems encountered using this.
    
    This function will not block, however the protocol may still be initialising when it is returned so
    immediate use of it may block.
    
    :param str protocol: The protocol to fetch a controller for.
    :return: A handle to the protocol controller, or ``None`` if something went wrong such as an
      unsupported protocol being specified.
    :rtype: DeviceProtocolController
    """
    pass



def GetDriverInformation(api: GraphicsAPI) -> DriverInformation:
    """
    Retrieves the driver information (if available) for a given graphics API.
    
    :param GraphicsAPI api: The API to get driver information for.
    :return: A :class:`DriverInformation` containing the driver information.
    :rtype: DriverInformation
    """
    pass



def GetLogFile() -> str:
    """
    Gets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :return: The path to the current log file.
    :rtype: str
    """
    pass



def GetSupportedDeviceProtocols() -> List[str]:
    """
    Retrieve the set of device protocols supported (see :func:`GetDeviceProtocolController`).
    
    :return: The supported device protocols.
    :rtype: List[str]
    """
    pass



def GetVersionString() -> str:
    """
    Retrieves the version string.
    
    This will be in the form "MAJOR.MINOR"
    
    :return: The version string.
    :rtype: str
    """
    pass



def HalfToFloat(half: int) -> float:
    """
    A utility function that converts a half (stored in a 16-bit unsigned integer) to a
    float.
    
    :param int half: The half stored as an int.
    :return: The floating point equivalent.
    :rtype: float
    """
    pass



def InitCamera(type: CameraType) -> Camera:
    """
    Create a new camera of a given type.
    
    :param CameraType type: The type of controls to use
    :return: The handle to the new camera.
    :rtype: Camera
    """
    pass



def InitialiseReplay(globalEnv: GlobalEnvironment, args: List[str]):
    """
    Initialises RenderDoc for replay. Replay API functions should not be called before this
    has been called. It should be called exactly once, and before shutdown you must call
    :func:`ShutdownReplay`.
    
    :param GlobalEnvironment globalEnv: The path to the new log file.
    :param List[str] args: Any extra command-line arguments.
    """
    pass



def InjectIntoProcess(pid: int, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions, waitForExit: bool) -> ExecuteResult:
    """
    Where supported by operating system and permissions, inject into a running process.
    
    :param int pid: The Process ID (PID) to inject into.
    :param List[EnvironmentModification] env: Any environment changes that should be made when running
      the program.
    :param str capturefile: The capture file path template, or blank to use a default location.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :param bool waitForExit: If ``True`` this function will block until the process exits.
    :return: The :class:`ExecuteResult` indicating both the status of the operation (success or failure)
      and any reason for failure, or else the ident where the new application is listening for target
      control if everything succeeded.
    :rtype: ExecuteResult
    """
    pass



def IsAMDCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is an AMD private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an AMD private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass



def IsARMCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is an ARM private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an ARM private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass



def IsConstantBlockDescriptor(type: DescriptorType) -> bool:
    """
    Checks if a descriptor type corresponds to a constant block in shader reflection.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a constant block descriptor.
    :rtype: bool
    """
    pass



def IsD3D(api: GraphicsAPI) -> bool:
    """
    Check if an API is D3D or not
    
    :param GraphicsAPI api: The graphics API in question
    :return: ``True`` if api is a D3D-based API, ``False`` otherwise
    :rtype: bool
    """
    pass



def IsGenericCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is a Generic counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is a generic counter, ``False`` if it's not.
    :rtype: bool
    """
    pass



def IsGlobalHookActive() -> bool:
    """
    Determines if the global hook is active or not.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`).
    
    :return: ``True`` if the hook is active, or ``False`` if the hook is inactive.
    :rtype: bool
    """
    pass



def IsIntelCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is an Intel private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Intel private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass



def IsNvidiaCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is an Nvidia private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Nvidia private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass



def IsReadOnlyDescriptor(type: DescriptorType) -> bool:
    """
    Checks if a descriptor type corresponds to a read only resource in shader reflection.
    Combined image/samplers are reported as read only resources.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a read-only resource descriptor.
    :rtype: bool
    """
    pass



def IsReadWriteDescriptor(type: DescriptorType) -> bool:
    """
    Checks if a descriptor type corresponds to a read write resource in shader reflection.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a read-write resource descriptor.
    :rtype: bool
    """
    pass



def IsReleaseBuild() -> bool:
    """
    Determines if this is a release build of RenderDoc or not.
    
    :return: ``True`` if the replay is running on a release build.
    :rtype: bool
    """
    pass



def IsSamplerDescriptor(type: DescriptorType) -> bool:
    """
    Checks if a descriptor type corresponds to a sampler in shader reflection. Only dedicated
    sampler types are sampler descriptors, combined image/samplers are reported only as read only
    resources.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a sampler descriptor.
    :rtype: bool
    """
    pass



def IsStrip(topology: Topology) -> bool:
    """
    Check whether or not this is a strip-type topology.
    
    :param Topology topology: The topology to check.
    :return: ``True`` if it describes a strip topology, ``False`` for a list.
    :rtype: bool
    """
    pass



def IsTextRepresentation(encoding: ShaderEncoding) -> bool:
    """
    Check whether or not this is a human readable text representation.
    
    :param ShaderEncoding encoding: The encoding to check.
    :return: ``True`` if it describes a text representation, ``False`` for a bytecode representation.
    :rtype: bool
    """
    pass



def IsVulkanExtendedCounter(c: GPUCounter) -> bool:
    """
    Check whether or not this is a KHR counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is a Vulkan counter reported through the VK_KHR_performance_query extension, ``False`` if it's not.
    :rtype: bool
    """
    pass



def LogMessage(type: LogType, project: str, file: str, line: int, text: str):
    """
    Add a message to RenderDoc's logfile.
    
    :param LogType type: The type of the log message. Error messages will trigger a debugger breakpoint
      if a debugger is attached, and fatal errors will kill the process after logging.
    :param str project: A short project tag, which should be uppercase and either 3 or 4 characters.
    :param str file: The file where this log message came from.
    :param int line: The line number in :paramref:`LogMessage.file` where this log message came from.
    :param str text: The text of the message.
    """
    pass



def MaskForStage(stage: ShaderStage) -> ShaderStageMask:
    """
    Calculate the corresponding flag for a shader stage
    
    :param ShaderStage stage: The shader stage
    :return: The flag that corresponds to the input shader stage
    :rtype: ShaderStageMask
    """
    pass



def NeedVulkanLayerRegistration():
    """
    INTERNAL: Determine vulkan layer registration status.
    """
    pass



def NumVerticesPerPrimitive(topology: Topology) -> int:
    """
    A utility function that returns the number of vertices in a primitive of a given
    topology.
    
    .. note:: In strip topologies vertices are re-used.
    
    :param Topology topology: The topology to query about.
    :return: The number of vertices in a single primitive.
    :rtype: int
    """
    pass



def OpenCaptureFile() -> CaptureFile:
    """
    Create a handle for a capture file.
    
    This function returns a new handle to a capture file. Once initialised by opening a file the handle
    can only be shut-down, it is not re-usable.
    
    :return: A handle to the specified path.
    :rtype: CaptureFile
    """
    pass



def PatchList_Count(topology: Topology) -> int:
    """
    Return the number of control points in a patch list ``Topology``
    
    ``t`` must be a patch list topology, the return value will be between 1 and 32 inclusive
    
    :param Topology topology: The patch list topology
    :return: The number of control points in the specified topology
    :rtype: int
    """
    pass



def PatchList_Topology(N: int) -> Topology:
    """
    Return the patch list ``Topology`` with N control points
    
    ``N`` must be between 1 and 32 inclusive.
    
    :param int N: The number of control points in the patch list
    :return: The patchlist topology with that number of control points
    :rtype: Topology
    """
    pass



def RWResUsage(stage: ShaderStage) -> ResourceUsage:
    """
    Calculate the ``ResourceUsage`` value for read-write resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-write resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass



def ResUsage(stage: ShaderStage) -> ResourceUsage:
    """
    Calculate the ``ResourceUsage`` value for read-only resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-only resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass



def SaveConfigSettings():
    """
    Flush the current config settings as they are in memory to the config file on disk.
    
    Without calling this function, settings changes will only be temporary. The settings are **not**
    saved to disk on exit implicitly.
    """
    pass



def SetColors(darkChecker: FloatVector, lightChecker: FloatVector, darkTheme: bool):
    """
    Configure the default colours used for checkerboards, this can broadly speaking help
    match the replay rendering to the overall theme of the replay application.
    
    :param FloatVector darkChecker: The color of dark squares in checkerboard patterns.
    :param FloatVector lightChecker: The color of light squares in checkerboard patterns.
    :param bool darkTheme: ``True`` if the theme is a 'dark' theme, used to pick different contrasting
      colors. ``False`` if the theme is 'light' and normal colors are used.
    """
    pass



def SetConfigSetting(name: str) -> SDObject:
    """
    Return a mutable handle to the :class:`SDObject` corresponding to a given setting's
    value object.
    
    If no such setting exists, `None` is returned.
    
    :param str name: The name of the setting.
    :return: The specified setting.
    :rtype: SDObject
    """
    pass



def SetDebugLogFile(filename: str):
    """
    Sets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :param str filename: The path to the new log file.
    """
    pass



def ShutdownReplay():
    """
    Shutdown RenderDoc for replay. Replay API functions should not be called after this
    has been called. It is not safe to re-initialise replay after this function has been called so it
    should only be called at program shutdown. This function must only be called if
    :func:`InitialiseReplay` was previously called.
    """
    pass



def StartGlobalHook(pathmatch: str, capturefile: str, opts: CaptureOptions) -> ResultDetails:
    """
    Begin injecting speculatively into all new processes started on the system. Where
    supported by platform, configuration, and setup begin injecting speculatively into all new processes
    started on the system.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is not active (see :func:`IsGlobalHookActive`).
    
    The hook must be closed with :func:`StopGlobalHook` before the application is closed.
    
    This function must be called when the process is running with administrator/superuser permissions.
    
    :param str pathmatch: A string to match against each new process's executable path to determine
      which corresponds to the program we actually want to capture.
    :param str capturefile: Where to store any captures.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :return: The result of the operation, if the result succeeded the hook is now active.
    :rtype: ResultDetails
    """
    pass



def StartSelfHostCapture(dllname: str):
    """
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to start a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass



def StopGlobalHook():
    """
    Stop the global hook that was activated by :func:`StartGlobalHook`.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is active (see :func:`IsGlobalHookActive`).
    """
    pass



def ToolExecutable(tool: KnownShaderTool) -> str:
    """
    Returns the default executable name with no suffix for a given :class:`KnownShaderTool`.
    
    .. note::
      The executable name is returned with no suffix, e.g. ``foobar`` which may need a platform specific
      suffix like ``.exe`` appended.
    
    :param KnownShaderTool tool: The tool to get the executable name for.
    :return: The default executable name for this tool, or an empty string if the tool is unrecognised.
    :rtype: str
    """
    pass



def ToolInput(tool: KnownShaderTool) -> ShaderEncoding:
    """
    Returns the expected default input :class:`~renderdoc.ShaderEncoding` that a
    :class:`KnownShaderTool` expects. This may not be accurate and may be configurable depending on the
    tool.
    
    :param KnownShaderTool tool: The tool to get the input encoding for.
    :return: The encoding that this tool expects as an input by default.
    :rtype: ShaderEncoding
    """
    pass



def ToolOutput(tool: KnownShaderTool) -> ShaderEncoding:
    """
    Returns the expected default output :class:`~renderdoc.ShaderEncoding` that a
    :class:`KnownShaderTool` produces. This may not be accurate and may be configurable depending on the
    tool.
    
    :param KnownShaderTool tool: The tool to get the output encoding for.
    :return: The encoding that this tool produces as an output by default.
    :rtype: ShaderEncoding
    """
    pass



def UpdateVulkanLayerRegistration():
    """
    INTERNAL: Update vulkan layer registration.
    """
    pass



def VarTypeByteSize(type: VarType) -> int:
    """
    Get the byte size of a variable type.
    
    :param VarType type: The variable type
    :return: The size in bytes of this type
    :rtype: int
    """
    pass



def VarTypeCompType(type: VarType) -> CompType:
    """
    Get the component type of a variable type.
    
    :param VarType type: The variable type
    :return: The base component type of this variable type
    :rtype: CompType
    """
    pass



def VertexOffset(topology: Topology, primitive: int) -> int:
    """
    A utility function that returns the offset in the list of vertices of the first vertex
    in a particular primitive of a given topology. This calculation is simple but not trivial for the
    case of strip topologies.
    
    :param Topology topology: The topology to query about.
    :param int primitive: The primitive to query about.
    :return: The vertex offset where the primitive starts.
    :rtype: int
    """
    pass



def makeSDArray(name: str) -> SDObject:
    """
    Make a structured object which is an array.
    
    The array will be created empty, and new members can be added using methods on :class:`SDObject`.
    
    :param str name: The name of the object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDBool(name: str, val: bool) -> SDObject:
    """
    Make a structured object as a boolean value.
    
    :param str name: The name of the object.
    :param bool val: The bool which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDEnum(name: str, val: int) -> SDObject:
    """
    Make a structured object as an enum value.
    
    .. note::
      The enum will be stored just as an integer value, but the string name of the enumeration value can
      be set by changing the string data member if desired.
    
    :param str name: The name of the object.
    :param int val: The integer value of the enum itself.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDFloat(name: str, val: float) -> SDObject:
    """
    Make a structured object as a 32-bit float.
    
    .. note::
      You should ensure that the value you pass in has already been truncated to the appropriate range
      for the storage, as the resulting object will be undefined if the value is out of the valid range.
    
    :param str name: The name of the object.
    :param float val: The float which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDInt32(name: str, val: int) -> SDObject:
    """
    Make a structured object as a signed 32-bit integer.
    
    .. note::
      You should ensure that the value you pass in has already been truncated to the appropriate range
      for the storage, as the resulting object will be undefined if the value is out of the valid range.
    
    :param str name: The name of the object.
    :param int val: The integer which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDInt64(name: str, val: int) -> SDObject:
    """
    Make a structured object as a signed 64-bit integer.
    
    .. note::
      You should ensure that the value you pass in has already been truncated to the appropriate range
      for the storage, as the resulting object will be undefined if the value is out of the valid range.
    
    :param str name: The name of the object.
    :param int val: The integer which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDResourceId(name: str, val: ResourceId) -> SDObject:
    """
    Make a structured object as a ResourceId value.
    
    :param str name: The name of the object.
    :param ResourceId val: The ID which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDString(name: str, val: str) -> SDObject:
    """
    Make a structured object as a string value.
    
    :param str name: The name of the object.
    :param str val: The string which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDStruct(name: str, structtype: str) -> SDObject:
    """
    Make a structured object which is a struct.
    
    The struct will be created empty, and new members can be added using methods on :class:`SDObject`.
    
    :param str name: The name of the object.
    :param str structtype: The typename of the struct.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDUInt32(name: str, val: int) -> SDObject:
    """
    Make a structured object as an unsigned 32-bit integer.
    
    .. note::
      You should ensure that the value you pass in has already been truncated to the appropriate range
      for the storage, as the resulting object will be undefined if the value is out of the valid range.
    
    :param str name: The name of the object.
    :param int val: The integer which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass



def makeSDUInt64(name: str, val: int) -> SDObject:
    """
    Make a structured object as an unsigned 64-bit integer.
    
    .. note::
      You should ensure that the value you pass in has already been truncated to the appropriate range
      for the storage, as the resulting object will be undefined if the value is out of the valid range.
    
    :param str name: The name of the object.
    :param int val: The integer which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

