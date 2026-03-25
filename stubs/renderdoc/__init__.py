# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


# classes

from .ActionDescription import ActionDescription
from .ActionFlags import ActionFlags
from .AddressMode import AddressMode
from .AlphaMapping import AlphaMapping
from .AndroidFlags import AndroidFlags
from .APIEvent import APIEvent
from .APIProperties import APIProperties
from .APIUseData import APIUseData
from .AxisMapping import AxisMapping
from .BindType import BindType
from .BlendEquation import BlendEquation
from .BlendMultiplier import BlendMultiplier
from .BlendOperation import BlendOperation
from .BlendStats import BlendStats
from .BoundVBuffer import BoundVBuffer
from .BucketRecordType import BucketRecordType
from .BufferCategory import BufferCategory
from .BufferDescription import BufferDescription
from .BusyData import BusyData
from .Camera import Camera
from .CameraType import CameraType
from .CaptureAccess import CaptureAccess
from .CaptureFile import CaptureFile
from .CaptureFileFormat import CaptureFileFormat
from .CaptureOptions import CaptureOptions
from .ChromaSampleLocation import ChromaSampleLocation
from .ColorBlend import ColorBlend
from .CompareFunction import CompareFunction
from .CompType import CompType
from .ConservativeRaster import ConservativeRaster
from .ConstantBindStats import ConstantBindStats
from .ConstantBlock import ConstantBlock
from .CounterDescription import CounterDescription
from .CounterResult import CounterResult
from .CounterUnit import CounterUnit
from .CounterValue import CounterValue
from .CullMode import CullMode
from .D3D11BlendState import D3D11BlendState
from .D3D11DepthStencilState import D3D11DepthStencilState
from .D3D11IndexBuffer import D3D11IndexBuffer
from .D3D11InputAssembly import D3D11InputAssembly
from .D3D11Layout import D3D11Layout
from .D3D11OutputMerger import D3D11OutputMerger
from .D3D11Predication import D3D11Predication
from .D3D11Rasterizer import D3D11Rasterizer
from .D3D11RasterizerState import D3D11RasterizerState
from .D3D11Shader import D3D11Shader
from .D3D11State import D3D11State
from .D3D11StreamOut import D3D11StreamOut
from .D3D11StreamOutBind import D3D11StreamOutBind
from .D3D11VertexBuffer import D3D11VertexBuffer
from .D3D12BlendState import D3D12BlendState
from .D3D12DepthStencilState import D3D12DepthStencilState
from .D3D12IndexBuffer import D3D12IndexBuffer
from .D3D12InputAssembly import D3D12InputAssembly
from .D3D12Layout import D3D12Layout
from .D3D12OM import D3D12OM
from .D3D12Predication import D3D12Predication
from .D3D12Rasterizer import D3D12Rasterizer
from .D3D12RasterizerState import D3D12RasterizerState
from .D3D12ResourceData import D3D12ResourceData
from .D3D12ResourceState import D3D12ResourceState
from .D3D12RootParam import D3D12RootParam
from .D3D12RootSignature import D3D12RootSignature
from .D3D12RootTableRange import D3D12RootTableRange
from .D3D12Shader import D3D12Shader
from .D3D12State import D3D12State
from .D3D12StaticSampler import D3D12StaticSampler
from .D3D12StreamOut import D3D12StreamOut
from .D3D12StreamOutBind import D3D12StreamOutBind
from .D3D12VertexBuffer import D3D12VertexBuffer
from .DebugMessage import DebugMessage
from .DebugOverlay import DebugOverlay
from .DebugPixelInputs import DebugPixelInputs
from .DebugVariableReference import DebugVariableReference
from .DebugVariableType import DebugVariableType
from .DepthStencilStats import DepthStencilStats
from .Descriptor import Descriptor
from .DescriptorAccess import DescriptorAccess
from .DescriptorCategory import DescriptorCategory
from .DescriptorFlags import DescriptorFlags
from .DescriptorLogicalLocation import DescriptorLogicalLocation
from .DescriptorRange import DescriptorRange
from .DescriptorStoreDescription import DescriptorStoreDescription
from .DescriptorType import DescriptorType
from .DeviceProtocolController import DeviceProtocolController
from .DispatchStats import DispatchStats
from .DrawcallStats import DrawcallStats
from .DriverInformation import DriverInformation
from .EnvironmentModification import EnvironmentModification
from .EnvMod import EnvMod
from .EnvSep import EnvSep
from .EventUsage import EventUsage
from .ExecuteResult import ExecuteResult
from .FileType import FileType
from .FillMode import FillMode
from .FilterFunction import FilterFunction
from .FilterMode import FilterMode
from .FloatVector import FloatVector
from .FrameDescription import FrameDescription
from .FrameStatistics import FrameStatistics
from .GLBlendState import GLBlendState
from .GLDepthState import GLDepthState
from .GLFBO import GLFBO
from .GLFeedback import GLFeedback
from .GLFixedVertexProcessing import GLFixedVertexProcessing
from .GLFrameBuffer import GLFrameBuffer
from .GLHints import GLHints
from .GlobalEnvironment import GlobalEnvironment
from .GLRasterizer import GLRasterizer
from .GLRasterizerState import GLRasterizerState
from .GLShader import GLShader
from .GLState import GLState
from .GLStencilState import GLStencilState
from .GLTextureCompleteness import GLTextureCompleteness
from .GLVertexAttribute import GLVertexAttribute
from .GLVertexBuffer import GLVertexBuffer
from .GLVertexInput import GLVertexInput
from .GPUCounter import GPUCounter
from .GPUDevice import GPUDevice
from .GPUVendor import GPUVendor
from .GraphicsAPI import GraphicsAPI
from .IndexBindStats import IndexBindStats
from .InstructionSourceInfo import InstructionSourceInfo
from .KnownShaderTool import KnownShaderTool
from .LayoutBindStats import LayoutBindStats
from .LineColumnInfo import LineColumnInfo
from .LineRaster import LineRaster
from .LogicOperation import LogicOperation
from .LogType import LogType
from .MeshDataStage import MeshDataStage
from .MeshDisplay import MeshDisplay
from .MeshFormat import MeshFormat
from .MeshletSize import MeshletSize
from .MessageCategory import MessageCategory
from .MessageSeverity import MessageSeverity
from .MessageSource import MessageSource
from .ModificationValue import ModificationValue
from .NewCaptureData import NewCaptureData
from .NewChildData import NewChildData
from .Offset import Offset
from .OutputTargetStats import OutputTargetStats
from .PathEntry import PathEntry
from .PathProperty import PathProperty
from .PipeState import PipeState
from .PixelModification import PixelModification
from .PixelValue import PixelValue
from .PointerVal import PointerVal
from .QualityHint import QualityHint
from .RasterizationStats import RasterizationStats
from .rdcarray_of_ActionDescription import rdcarray_of_ActionDescription
from .rdcarray_of_APIEvent import rdcarray_of_APIEvent
from .rdcarray_of_BoundVBuffer import rdcarray_of_BoundVBuffer
from .rdcarray_of_BufferDescription import rdcarray_of_BufferDescription
from .rdcarray_of_CaptureFileFormat import rdcarray_of_CaptureFileFormat
from .rdcarray_of_ColorBlend import rdcarray_of_ColorBlend
from .rdcarray_of_ConstantBindStats import rdcarray_of_ConstantBindStats
from .rdcarray_of_ConstantBlock import rdcarray_of_ConstantBlock
from .rdcarray_of_CounterResult import rdcarray_of_CounterResult
from .rdcarray_of_D3D11Pipe_Layout import rdcarray_of_D3D11Pipe_Layout
from .rdcarray_of_D3D11Pipe_StreamOutBind import rdcarray_of_D3D11Pipe_StreamOutBind
from .rdcarray_of_D3D11Pipe_VertexBuffer import rdcarray_of_D3D11Pipe_VertexBuffer
from .rdcarray_of_D3D12Pipe_Layout import rdcarray_of_D3D12Pipe_Layout
from .rdcarray_of_D3D12Pipe_ResourceData import rdcarray_of_D3D12Pipe_ResourceData
from .rdcarray_of_D3D12Pipe_ResourceState import rdcarray_of_D3D12Pipe_ResourceState
from .rdcarray_of_D3D12Pipe_RootParam import rdcarray_of_D3D12Pipe_RootParam
from .rdcarray_of_D3D12Pipe_RootTableRange import rdcarray_of_D3D12Pipe_RootTableRange
from .rdcarray_of_D3D12Pipe_StaticSampler import rdcarray_of_D3D12Pipe_StaticSampler
from .rdcarray_of_D3D12Pipe_StreamOutBind import rdcarray_of_D3D12Pipe_StreamOutBind
from .rdcarray_of_D3D12Pipe_VertexBuffer import rdcarray_of_D3D12Pipe_VertexBuffer
from .rdcarray_of_DebugMessage import rdcarray_of_DebugMessage
from .rdcarray_of_DebugVariableReference import rdcarray_of_DebugVariableReference
from .rdcarray_of_Descriptor import rdcarray_of_Descriptor
from .rdcarray_of_DescriptorAccess import rdcarray_of_DescriptorAccess
from .rdcarray_of_DescriptorLogicalLocation import rdcarray_of_DescriptorLogicalLocation
from .rdcarray_of_DescriptorRange import rdcarray_of_DescriptorRange
from .rdcarray_of_DescriptorStoreDescription import rdcarray_of_DescriptorStoreDescription
from .rdcarray_of_EnvironmentModification import rdcarray_of_EnvironmentModification
from .rdcarray_of_EventUsage import rdcarray_of_EventUsage
from .rdcarray_of_float import rdcarray_of_float
from .rdcarray_of_FloatVector import rdcarray_of_FloatVector
from .rdcarray_of_GLPipe_TextureCompleteness import rdcarray_of_GLPipe_TextureCompleteness
from .rdcarray_of_GLPipe_VertexAttribute import rdcarray_of_GLPipe_VertexAttribute
from .rdcarray_of_GLPipe_VertexBuffer import rdcarray_of_GLPipe_VertexBuffer
from .rdcarray_of_GPUCounter import rdcarray_of_GPUCounter
from .rdcarray_of_GPUDevice import rdcarray_of_GPUDevice
from .rdcarray_of_GraphicsAPI import rdcarray_of_GraphicsAPI
from .rdcarray_of_InstructionSourceInfo import rdcarray_of_InstructionSourceInfo
from .rdcarray_of_int import rdcarray_of_int
from .rdcarray_of_LineColumnInfo import rdcarray_of_LineColumnInfo
from .rdcarray_of_MeshletSize import rdcarray_of_MeshletSize
from .rdcarray_of_Offset import rdcarray_of_Offset
from .rdcarray_of_PathEntry import rdcarray_of_PathEntry
from .rdcarray_of_PixelModification import rdcarray_of_PixelModification
from .rdcarray_of_rdcstr import rdcarray_of_rdcstr
from .rdcarray_of_ResourceBindStats import rdcarray_of_ResourceBindStats
from .rdcarray_of_ResourceDescription import rdcarray_of_ResourceDescription
from .rdcarray_of_ResourceId import rdcarray_of_ResourceId
from .rdcarray_of_SamplerBindStats import rdcarray_of_SamplerBindStats
from .rdcarray_of_SamplerDescriptor import rdcarray_of_SamplerDescriptor
from .rdcarray_of_Scissor import rdcarray_of_Scissor
from .rdcarray_of_ShaderChangeStats import rdcarray_of_ShaderChangeStats
from .rdcarray_of_ShaderCompileFlag import rdcarray_of_ShaderCompileFlag
from .rdcarray_of_ShaderConstant import rdcarray_of_ShaderConstant
from .rdcarray_of_ShaderConstantType import rdcarray_of_ShaderConstantType
from .rdcarray_of_ShaderDebugState import rdcarray_of_ShaderDebugState
from .rdcarray_of_ShaderEncoding import rdcarray_of_ShaderEncoding
from .rdcarray_of_ShaderEntryPoint import rdcarray_of_ShaderEntryPoint
from .rdcarray_of_ShaderMessage import rdcarray_of_ShaderMessage
from .rdcarray_of_ShaderResource import rdcarray_of_ShaderResource
from .rdcarray_of_ShaderSampler import rdcarray_of_ShaderSampler
from .rdcarray_of_ShaderSourceFile import rdcarray_of_ShaderSourceFile
from .rdcarray_of_ShaderSourcePrefix import rdcarray_of_ShaderSourcePrefix
from .rdcarray_of_ShaderVariable import rdcarray_of_ShaderVariable
from .rdcarray_of_ShaderVariableChange import rdcarray_of_ShaderVariableChange
from .rdcarray_of_SigParameter import rdcarray_of_SigParameter
from .rdcarray_of_SourceVariableMapping import rdcarray_of_SourceVariableMapping
from .rdcarray_of_TaskGroupSize import rdcarray_of_TaskGroupSize
from .rdcarray_of_TextureDescription import rdcarray_of_TextureDescription
from .rdcarray_of_uint32_t import rdcarray_of_uint32_t
from .rdcarray_of_uint64_t import rdcarray_of_uint64_t
from .rdcarray_of_UsedDescriptor import rdcarray_of_UsedDescriptor
from .rdcarray_of_VertexInputAttribute import rdcarray_of_VertexInputAttribute
from .rdcarray_of_Viewport import rdcarray_of_Viewport
from .rdcarray_of_VKPipe_DescriptorBuffer import rdcarray_of_VKPipe_DescriptorBuffer
from .rdcarray_of_VKPipe_DescriptorSet import rdcarray_of_VKPipe_DescriptorSet
from .rdcarray_of_VKPipe_DynamicOffset import rdcarray_of_VKPipe_DynamicOffset
from .rdcarray_of_VKPipe_ImageData import rdcarray_of_VKPipe_ImageData
from .rdcarray_of_VKPipe_ImageLayout import rdcarray_of_VKPipe_ImageLayout
from .rdcarray_of_VKPipe_RenderArea import rdcarray_of_VKPipe_RenderArea
from .rdcarray_of_VKPipe_VertexAttribute import rdcarray_of_VKPipe_VertexAttribute
from .rdcarray_of_VKPipe_VertexBinding import rdcarray_of_VKPipe_VertexBinding
from .rdcarray_of_VKPipe_VertexBuffer import rdcarray_of_VKPipe_VertexBuffer
from .rdcarray_of_VKPipe_ViewportScissor import rdcarray_of_VKPipe_ViewportScissor
from .rdcarray_of_VKPipe_XFBBuffer import rdcarray_of_VKPipe_XFBBuffer
from .rdcarray_of_WindowingSystem import rdcarray_of_WindowingSystem
from .RemoteServer import RemoteServer
from .ReplayController import ReplayController
from .ReplayOptimisationLevel import ReplayOptimisationLevel
from .ReplayOptions import ReplayOptions
from .ReplayOutput import ReplayOutput
from .ReplayOutputType import ReplayOutputType
from .ReplaySupport import ReplaySupport
from .ResourceBindStats import ResourceBindStats
from .ResourceDescription import ResourceDescription
from .ResourceFormat import ResourceFormat
from .ResourceFormatType import ResourceFormatType
from .ResourceId import ResourceId
from .ResourceType import ResourceType
from .ResourceUpdateStats import ResourceUpdateStats
from .ResourceUsage import ResourceUsage
from .ResultCode import ResultCode
from .ResultDetails import ResultDetails
from .SamplerBindStats import SamplerBindStats
from .SamplerDescriptor import SamplerDescriptor
from .Scissor import Scissor
from .SDBasic import SDBasic
from .SDObject import SDObject
from .SDChunk import SDChunk
from .SDChunkFlags import SDChunkFlags
from .SDChunkMetaData import SDChunkMetaData
from .SDFile import SDFile
from .SDObjectData import SDObjectData
from .SDObjectPODData import SDObjectPODData
from .SDType import SDType
from .SDTypeFlags import SDTypeFlags
from .SectionFlags import SectionFlags
from .SectionProperties import SectionProperties
from .SectionType import SectionType
from .ShaderBindIndex import ShaderBindIndex
from .ShaderBuiltin import ShaderBuiltin
from .ShaderChangeStats import ShaderChangeStats
from .ShaderCompileFlag import ShaderCompileFlag
from .ShaderCompileFlags import ShaderCompileFlags
from .ShaderComputeMessageLocation import ShaderComputeMessageLocation
from .ShaderConstant import ShaderConstant
from .ShaderConstantType import ShaderConstantType
from .ShaderDebugger import ShaderDebugger
from .ShaderDebugInfo import ShaderDebugInfo
from .ShaderDebugState import ShaderDebugState
from .ShaderDebugTrace import ShaderDebugTrace
from .ShaderDirectAccess import ShaderDirectAccess
from .ShaderEncoding import ShaderEncoding
from .ShaderEntryPoint import ShaderEntryPoint
from .ShaderEvents import ShaderEvents
from .ShaderGeometryMessageLocation import ShaderGeometryMessageLocation
from .ShaderMeshMessageLocation import ShaderMeshMessageLocation
from .ShaderMessage import ShaderMessage
from .ShaderMessageLocation import ShaderMessageLocation
from .ShaderPixelMessageLocation import ShaderPixelMessageLocation
from .ShaderReflection import ShaderReflection
from .ShaderResource import ShaderResource
from .ShaderSampler import ShaderSampler
from .ShaderSourceFile import ShaderSourceFile
from .ShaderSourcePrefix import ShaderSourcePrefix
from .ShaderStage import ShaderStage
from .ShaderStageMask import ShaderStageMask
from .ShaderValue import ShaderValue
from .ShaderVariable import ShaderVariable
from .ShaderVariableChange import ShaderVariableChange
from .ShaderVariableFlags import ShaderVariableFlags
from .ShaderVertexMessageLocation import ShaderVertexMessageLocation
from .ShadingRateCombiner import ShadingRateCombiner
from .SigParameter import SigParameter
from .SourceVariableMapping import SourceVariableMapping
from .StencilFace import StencilFace
from .StencilOperation import StencilOperation
from .StructuredBufferList import StructuredBufferList
from .StructuredChunkList import StructuredChunkList
from .StructuredObjectList import StructuredObjectList
from .Subresource import Subresource
from .TargetControl import TargetControl
from .TargetControlMessage import TargetControlMessage
from .TargetControlMessageType import TargetControlMessageType
from .TaskGroupSize import TaskGroupSize
from .TextureCategory import TextureCategory
from .TextureComponentMapping import TextureComponentMapping
from .TextureDescription import TextureDescription
from .TextureDisplay import TextureDisplay
from .TextureFilter import TextureFilter
from .TextureSampleMapping import TextureSampleMapping
from .TextureSave import TextureSave
from .TextureSliceMapping import TextureSliceMapping
from .TextureSwizzle import TextureSwizzle
from .TextureSwizzle4 import TextureSwizzle4
from .TextureType import TextureType
from .Thumbnail import Thumbnail
from .Topology import Topology
from .UsedDescriptor import UsedDescriptor
from .Uuid import Uuid
from .VarType import VarType
from .VertexBindStats import VertexBindStats
from .VertexInputAttribute import VertexInputAttribute
from .Viewport import Viewport
from .Visualisation import Visualisation
from .VKColorBlendState import VKColorBlendState
from .VKConditionalRendering import VKConditionalRendering
from .VKCurrentPass import VKCurrentPass
from .VKDepthStencil import VKDepthStencil
from .VKDescriptorBuffer import VKDescriptorBuffer
from .VKDescriptorSet import VKDescriptorSet
from .VKDynamicOffset import VKDynamicOffset
from .VKFramebuffer import VKFramebuffer
from .VKImageData import VKImageData
from .VKImageLayout import VKImageLayout
from .VKIndexBuffer import VKIndexBuffer
from .VKInputAssembly import VKInputAssembly
from .VKMultiSample import VKMultiSample
from .VKPipeline import VKPipeline
from .VKRasterizer import VKRasterizer
from .VKRenderArea import VKRenderArea
from .VKRenderPass import VKRenderPass
from .VKSampleLocations import VKSampleLocations
from .VKShader import VKShader
from .VKState import VKState
from .VKTessellation import VKTessellation
from .VKTransformFeedback import VKTransformFeedback
from .VKVertexAttribute import VKVertexAttribute
from .VKVertexBinding import VKVertexBinding
from .VKVertexBuffer import VKVertexBuffer
from .VKVertexInput import VKVertexInput
from .VKViewportScissor import VKViewportScissor
from .VKViewState import VKViewState
from .VKXFBBuffer import VKXFBBuffer
from .VulkanLayerFlags import VulkanLayerFlags
from .VulkanLayerRegistrationInfo import VulkanLayerRegistrationInfo
from .WindowingData import WindowingData
from .WindowingSystem import WindowingSystem
from .YcbcrConversion import YcbcrConversion
from .YcbcrRange import YcbcrRange

from renderdoc.ShaderEncoding import ShaderEncoding

# functions

def BecomeRemoteServer(listenhost: str, port: int, killReplay: KillCallback, previewWindow: PreviewWindowCallback): # real signature unknown; restored from __doc__
    """
    BecomeRemoteServer(listenhost, port, killReplay, previewWindow)
    
    This launches a remote server which will continually run in a loop to server requests
    from external sources.
    
    This function will block until a remote connection tells the server to shut down, or the
    ``killReplay`` callback returns ``True``.
    
    :param str listenhost: The name of the interface to listen on.
    :param int port: The port to listen on, or ``0`` to listen on the default port.
    :param KillCallback killReplay: A callback that returns a ``bool`` indicating if the server should
      be shut down or not.
      Callback function signature must match :func:`KillCallback`.
    :param PreviewWindowCallback previewWindow: A callback that returns information for a preview window
      when the server wants to display some preview of the ongoing replay.
      Callback function signature must match :func:`PreviewWindowCallback`.
    """
    pass

def CanGlobalHook() -> bool: # real signature unknown; restored from __doc__
    """
    CanGlobalHook()
    
    Determines if the global hook is supported on the current platform and configuration.
    
    :return: ``True`` if global hooking can be used on the platform, ``False`` if not.
    :rtype: bool
    """
    pass

def CanSelfHostedCapture(dllname: str) -> bool: # real signature unknown; restored from __doc__
    """
    CanSelfHostedCapture(dllname)
    
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function checks to see if a given self-hosted DLL is available.
    
    :param str dllname: The name of the self-hosted capture module.
    :return: Whether the specified dll is loaded, ready for self-hosted capture.
    :rtype: bool
    """
    pass

def CategoryForDescriptorType(type: DescriptorType) -> DescriptorCategory: # real signature unknown; restored from __doc__
    """
    CategoryForDescriptorType(type)
    
    Get the shader interface category for a given type of descriptor.
    
    :param DescriptorType type: The type of descriptor
    :return: The descriptor category.
    :rtype: DescriptorCategory
    """
    pass

def CBUsage(stage: ShaderStage) -> ResourceUsage: # real signature unknown; restored from __doc__
    """
    CBUsage(stage)
    
    Calculate the ``ResourceUsage`` value for constant buffer use at a given shader stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for constant buffer usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def CheckAndroidPackage(URL, packageAndActivity, flags): # real signature unknown; restored from __doc__
    """
    CheckAndroidPackage(URL, packageAndActivity, flags)
    
    INTERNAL: Check remote Android package for requirements
    """
    pass

def CheckRemoteServerConnection(URL: str) -> ResultDetails: # real signature unknown; restored from __doc__
    """
    CheckRemoteServerConnection(URL)
    
    Check the connection to a remote server running on given hostname.
    
    This should be preferred to :func:`CreateRemoteServerConnection` when no connection is desired, as
    the status can be checked without interfering with making connections.
    
    :param str URL: The hostname to connect to, if blank then localhost is used. If no protocol is
      specified then default TCP enumeration happens.
    :return: The status of the server.
    :rtype: ResultDetails
    """
    pass

def CreateAndroidWindowingData(window: ANativeWindow) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateAndroidWindowingData(window)
    
    Create a :class:`WindowingData` for an Android ``ANativeWindow`` handle.
    
    :param ANativeWindow window: The native ``ANativeWindow`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateHeadlessWindowingData(width: int, height: int) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateHeadlessWindowingData(width, height)
    
    Create a :class:`WindowingData` for no backing window, it will be headless.
    
    :param int width: The initial width for this virtual window.
    :param int height: The initial height for this virtual window.
    
    :return: A :class:`WindowingData` corresponding to an 'empty' backing window.
    :rtype: WindowingData
    """
    pass

def CreateMacOSWindowingData(view: NSView, layer: CALayer) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateMacOSWindowingData(view, layer)
    
    Create a :class:`WindowingData` for an metal/opengl-compatible macOS ``CALayer`` handle
    and ``NSView`` handle (as void pointers).
    
    :param NSView view: The native ``NSView`` handle for this window.
    :param CALayer layer: The native ``CALayer`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateRemoteServerConnection(URL: str) -> Tuple[ResultDetails,RemoteServer]: # real signature unknown; restored from __doc__
    """
    CreateRemoteServerConnection(URL)
    
    Create a connection to a remote server running on given hostname.
    
    :param str URL: The hostname to connect to, if blank then localhost is used. If no protocol is
      specified then default TCP enumeration happens.
    :return: The status of opening the connection, whether success or failure, and a :class:`RemoteServer`
      instance if it were successful
    :rtype: Tuple[ResultDetails,RemoteServer]
    """
    pass

def CreateTargetControl(URL: str, ident: int, clientName: str, forceConnection: bool) -> TargetControl: # real signature unknown; restored from __doc__
    """
    CreateTargetControl(URL, ident, clientName, forceConnection)
    
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

def CreateWaylandWindowingData(display: wl_display, window: wl_surface) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateWaylandWindowingData(display, window)
    
    Create a :class:`WindowingData` for an Wayland ``wl_surface`` handle.
    
    :param wl_display display: The ``wl_display`` connection used for this window.
    :param wl_surface window: The native ``wl_surface`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateWin32WindowingData(window: HWND) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateWin32WindowingData(window)
    
    Create a :class:`WindowingData` for a Win32 ``HWND`` handle.
    
    :param HWND window: The native ``HWND`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateXCBWindowingData(connection: xcb_connection_t, window: xcb_window_t) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateXCBWindowingData(connection, window)
    
    Create a :class:`WindowingData` for an XCB ``xcb_window_t`` handle.
    
    :param xcb_connection_t connection: The ``xcb_connection_t`` connection used for this window.
    :param xcb_window_t window: The native ``xcb_window_t`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateXlibWindowingData(display: Display, window: Drawable) -> WindowingData: # real signature unknown; restored from __doc__
    """
    CreateXlibWindowingData(display, window)
    
    Create a :class:`WindowingData` for an Xlib ``Drawable`` handle.
    
    :param Display display: The ``Display`` connection used for this window.
    :param Drawable window: The native ``Drawable`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def DumpObject(obj: Any) -> str: # real signature unknown; restored from __doc__
    """
    DumpObject(obj)
    
    Returns a string representation of an object. This is quite similar to
    the built-in repr() function but it iterates over struct members and prints them out, where normally
    repr() would stop and say something like 'Swig Object of type ...'.
    
    :param Any obj: The object to dump
    :return: The string representation of the object.
    :rtype: str
    """
    pass

def EndSelfHostCapture(dllname: str): # real signature unknown; restored from __doc__
    """
    EndSelfHostCapture(dllname)
    
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to end a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass

def EnumerateRemoteTargets(URL: str, nextIdent: int) -> int: # real signature unknown; restored from __doc__
    """
    EnumerateRemoteTargets(URL, nextIdent)
    
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

def ExecuteAndInject(app: str, workingDir: str, cmdLine: str, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions, waitForExit: bool) -> ExecuteResult: # real signature unknown; restored from __doc__
    """
    ExecuteAndInject(app, workingDir, cmdLine, env, capturefile, opts, waitForExit)
    
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

def FirstStageForMask(stageMask: ShaderStageMask) -> ShaderStage: # real signature unknown; restored from __doc__
    """
    FirstStageForMask(stageMask)
    
    For a shader stage mask that only covers one shader stage, return the shader stage.
    
    .. note::
      If the shader stage mask covers multiple stages, only the first matching stage will be returned.
      If the mask is empty, :data:`ShaderStage.Count` will be returned.
    
    :param ShaderStageMask stageMask: The shader stage mask.
    :return: The first shader stage covered by the mask.
    :rtype: ShaderStage
    """
    pass

def FloatToHalf(flt: float) -> int: # real signature unknown; restored from __doc__
    """
    FloatToHalf(flt)
    
    A utility function that converts a float to a half (stored in a 16-bit unsigned
    integer).
    
    :param float flt: The floating point value.
    :return: The nearest half-float equivalent stored as an int.
    :rtype: int
    """
    pass

def GetCommitHash() -> str: # real signature unknown; restored from __doc__
    """
    GetCommitHash()
    
    Retrieves the commit hash used to build.
    
    This will be in the form "0123456789abcdef0123456789abcdef01234567"
    
    :return: The commit hash.
    :rtype: str
    """
    pass

def GetConfigSetting(name: str) -> SDObject: # real signature unknown; restored from __doc__
    """
    GetConfigSetting(name)
    
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

def GetCurrentProcessMemoryUsage() -> int: # real signature unknown; restored from __doc__
    """
    GetCurrentProcessMemoryUsage()
    
    Returns the current process's memory usage in bytes
    
    :return: The current memory usage in bytes.
    :rtype: int
    """
    pass

def GetDefaultCaptureOptions() -> CaptureOptions: # real signature unknown; restored from __doc__
    """
    GetDefaultCaptureOptions()
    
    Retrieve the default and recommended set of capture options.
    
    :return: The default capture options.
    :rtype: CaptureOptions
    """
    pass

def GetDeviceProtocolController(protocol: str) -> DeviceProtocolController: # real signature unknown; restored from __doc__
    """
    GetDeviceProtocolController(protocol)
    
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

def GetDriverInformation(api: GraphicsAPI) -> DriverInformation: # real signature unknown; restored from __doc__
    """
    GetDriverInformation(api)
    
    Retrieves the driver information (if available) for a given graphics API.
    
    :param GraphicsAPI api: The API to get driver information for.
    :return: A :class:`DriverInformation` containing the driver information.
    :rtype: DriverInformation
    """
    pass

def GetLogFile() -> str: # real signature unknown; restored from __doc__
    """
    GetLogFile()
    
    Gets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :return: The path to the current log file.
    :rtype: str
    """
    pass

def GetSupportedDeviceProtocols() -> List[str]: # real signature unknown; restored from __doc__
    """
    GetSupportedDeviceProtocols()
    
    Retrieve the set of device protocols supported (see :func:`GetDeviceProtocolController`).
    
    :return: The supported device protocols.
    :rtype: List[str]
    """
    pass

def GetVersionString() -> str: # real signature unknown; restored from __doc__
    """
    GetVersionString()
    
    Retrieves the version string.
    
    This will be in the form "MAJOR.MINOR"
    
    :return: The version string.
    :rtype: str
    """
    pass

def GPUVendorFromPCIVendor(vendorID: int) -> GPUVendor: # real signature unknown; restored from __doc__
    """
    GPUVendorFromPCIVendor(vendorID)
    
    Get the GPUVendor for a given PCI Vendor ID.
    
    :param int vendorID: The PCI Vendor ID
    :return: The vendor identified
    :rtype: GPUVendor
    """
    pass

def HalfToFloat(half: int) -> float: # real signature unknown; restored from __doc__
    """
    HalfToFloat(half)
    
    A utility function that converts a half (stored in a 16-bit unsigned integer) to a
    float.
    
    :param int half: The half stored as an int.
    :return: The floating point equivalent.
    :rtype: float
    """
    pass

def InitCamera(type: CameraType) -> Camera: # real signature unknown; restored from __doc__
    """
    InitCamera(type)
    
    Create a new camera of a given type.
    
    :param CameraType type: The type of controls to use
    :return: The handle to the new camera.
    :rtype: Camera
    """
    pass

def InitialiseReplay(globalEnv: GlobalEnvironment, args: List[str]): # real signature unknown; restored from __doc__
    """
    InitialiseReplay(globalEnv, args)
    
    Initialises RenderDoc for replay. Replay API functions should not be called before this
    has been called. It should be called exactly once, and before shutdown you must call
    :func:`ShutdownReplay`.
    
    :param GlobalEnvironment globalEnv: The path to the new log file.
    :param List[str] args: Any extra command-line arguments.
    """
    pass

def InjectIntoProcess(pid: int, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions, waitForExit: bool) -> ExecuteResult: # real signature unknown; restored from __doc__
    """
    InjectIntoProcess(pid, env, capturefile, opts, waitForExit)
    
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

def IsAMDCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsAMDCounter(c)
    
    Check whether or not this is an AMD private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an AMD private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass

def IsARMCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsARMCounter(c)
    
    Check whether or not this is an ARM private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an ARM private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass

def IsConstantBlockDescriptor(type: DescriptorType) -> bool: # real signature unknown; restored from __doc__
    """
    IsConstantBlockDescriptor(type)
    
    Checks if a descriptor type corresponds to a constant block in shader reflection.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a constant block descriptor.
    :rtype: bool
    """
    pass

def IsD3D(api: GraphicsAPI) -> bool: # real signature unknown; restored from __doc__
    """
    IsD3D(api)
    
    Check if an API is D3D or not
    
    :param GraphicsAPI api: The graphics API in question
    :return: ``True`` if api is a D3D-based API, ``False`` otherwise
    :rtype: bool
    """
    pass

def IsGenericCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsGenericCounter(c)
    
    Check whether or not this is a Generic counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is a generic counter, ``False`` if it's not.
    :rtype: bool
    """
    pass

def IsGlobalHookActive() -> bool: # real signature unknown; restored from __doc__
    """
    IsGlobalHookActive()
    
    Determines if the global hook is active or not.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`).
    
    :return: ``True`` if the hook is active, or ``False`` if the hook is inactive.
    :rtype: bool
    """
    pass

def IsIntelCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsIntelCounter(c)
    
    Check whether or not this is an Intel private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Intel private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass

def IsNvidiaCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsNvidiaCounter(c)
    
    Check whether or not this is an Nvidia private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Nvidia private counter, ``False`` if it's not.
    :rtype: bool
    """
    pass

def IsReadOnlyDescriptor(type: DescriptorType) -> bool: # real signature unknown; restored from __doc__
    """
    IsReadOnlyDescriptor(type)
    
    Checks if a descriptor type corresponds to a read only resource in shader reflection.
    Combined image/samplers are reported as read only resources.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a read-only resource descriptor.
    :rtype: bool
    """
    pass

def IsReadWriteDescriptor(type: DescriptorType) -> bool: # real signature unknown; restored from __doc__
    """
    IsReadWriteDescriptor(type)
    
    Checks if a descriptor type corresponds to a read write resource in shader reflection.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a read-write resource descriptor.
    :rtype: bool
    """
    pass

def IsReleaseBuild() -> bool: # real signature unknown; restored from __doc__
    """
    IsReleaseBuild()
    
    Determines if this is a release build of RenderDoc or not.
    
    :return: ``True`` if the replay is running on a release build.
    :rtype: bool
    """
    pass

def IsSamplerDescriptor(type: DescriptorType) -> bool: # real signature unknown; restored from __doc__
    """
    IsSamplerDescriptor(type)
    
    Checks if a descriptor type corresponds to a sampler in shader reflection. Only dedicated
    sampler types are sampler descriptors, combined image/samplers are reported only as read only
    resources.
    
    :param DescriptorType type: The type of descriptor
    :return: ``True`` if the descriptor type is a sampler descriptor.
    :rtype: bool
    """
    pass

def IsStrip(topology: Topology) -> bool: # real signature unknown; restored from __doc__
    """
    IsStrip(topology)
    
    Check whether or not this is a strip-type topology.
    
    :param Topology topology: The topology to check.
    :return: ``True`` if it describes a strip topology, ``False`` for a list.
    :rtype: bool
    """
    pass

def IsTextRepresentation(encoding: ShaderEncoding) -> bool: # real signature unknown; restored from __doc__
    """
    IsTextRepresentation(encoding)
    
    Check whether or not this is a human readable text representation.
    
    :param ShaderEncoding encoding: The encoding to check.
    :return: ``True`` if it describes a text representation, ``False`` for a bytecode representation.
    :rtype: bool
    """
    pass

def IsVulkanExtendedCounter(c: GPUCounter) -> bool: # real signature unknown; restored from __doc__
    """
    IsVulkanExtendedCounter(c)
    
    Check whether or not this is a KHR counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is a Vulkan counter reported through the VK_KHR_performance_query extension, ``False`` if it's not.
    :rtype: bool
    """
    pass

def LogMessage(type: LogType, project: str, file: str, line: int, text: str): # real signature unknown; restored from __doc__
    """
    LogMessage(type, project, file, line, text)
    
    Add a message to RenderDoc's logfile.
    
    :param LogType type: The type of the log message. Error messages will trigger a debugger breakpoint
      if a debugger is attached, and fatal errors will kill the process after logging.
    :param str project: A short project tag, which should be uppercase and either 3 or 4 characters.
    :param str file: The file where this log message came from.
    :param int line: The line number in :paramref:`file` where this log message came from.
    :param str text: The text of the message.
    """
    pass

def makeSDArray(name: str) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDArray(name)
    
    Make a structured object which is an array.
    
    The array will be created empty, and new members can be added using methods on :class:`SDObject`.
    
    :param str name: The name of the object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDBool(name: str, val: bool) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDBool(name, val)
    
    Make a structured object as a boolean value.
    
    :param str name: The name of the object.
    :param bool val: The bool which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDEnum(name: str, val: int) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDEnum(name, val)
    
    Make a structured object as an enum value.
    
    .. note::
      The enum will be stored just as an integer value, but the string name of the enumeration value can
      be set with :meth:`SDObject.SetCustomString` if desired.
    
    :param str name: The name of the object.
    :param int val: The integer value of the enum itself.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDFloat(name: str, val: float) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDFloat(name, val)
    
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

def makeSDInt32(name: str, val: int) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDInt32(name, val)
    
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

def makeSDInt64(name: str, val: int) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDInt64(name, val)
    
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

def makeSDResourceId(name: str, val: ResourceId) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDResourceId(name, val)
    
    Make a structured object as a ResourceId value.
    
    :param str name: The name of the object.
    :param ResourceId val: The ID which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDString(name: str, val: str) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDString(name, val)
    
    Make a structured object as a string value.
    
    :param str name: The name of the object.
    :param str val: The string which will be stored in the returned object.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDStruct(name: str, structtype: str) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDStruct(name, structtype)
    
    Make a structured object which is a struct.
    
    The struct will be created empty, and new members can be added using methods on :class:`SDObject`.
    
    :param str name: The name of the object.
    :param str structtype: The typename of the struct.
    :return: The new object, owner by the caller.
    :rtype: SDObject
    """
    pass

def makeSDUInt32(name: str, val: int) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDUInt32(name, val)
    
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

def makeSDUInt64(name: str, val: int) -> SDObject: # real signature unknown; restored from __doc__
    """
    makeSDUInt64(name, val)
    
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

def MaskForStage(stage: ShaderStage) -> ShaderStageMask: # real signature unknown; restored from __doc__
    """
    MaskForStage(stage)
    
    Calculate the corresponding flag for a shader stage
    
    :param ShaderStage stage: The shader stage
    :return: The flag that corresponds to the input shader stage
    :rtype: ShaderStageMask
    """
    pass

def NeedVulkanLayerRegistration(info): # real signature unknown; restored from __doc__
    """
    NeedVulkanLayerRegistration(info)
    
    INTERNAL: Determine vulkan layer registration status.
    """
    pass

def NumVerticesPerPrimitive(topology: Topology) -> int: # real signature unknown; restored from __doc__
    """
    NumVerticesPerPrimitive(topology)
    
    A utility function that returns the number of vertices in a primitive of a given
    topology.
    
    .. note:: In strip topologies vertices are re-used.
    
    :param Topology topology: The topology to query about.
    :return: The number of vertices in a single primitive.
    :rtype: int
    """
    pass

def OpenCaptureFile() -> CaptureFile: # real signature unknown; restored from __doc__
    """
    OpenCaptureFile()
    
    Create a handle for a capture file.
    
    This function returns a new handle to a capture file. Once initialised by opening a file the handle
    can only be shut-down, it is not re-usable.
    
    :return: A handle to the specified path.
    :rtype: CaptureFile
    """
    pass

def PatchList_Count(topology: Topology) -> int: # real signature unknown; restored from __doc__
    """
    PatchList_Count(topology)
    
    Return the number of control points in a patch list ``Topology``
    
    ``t`` must be a patch list topology, the return value will be between 1 and 32 inclusive
    
    :param Topology topology: The patch list topology
    :return: The number of control points in the specified topology
    :rtype: int
    """
    pass

def PatchList_Topology(N: int) -> Topology: # real signature unknown; restored from __doc__
    """
    PatchList_Topology(N)
    
    Return the patch list ``Topology`` with N control points
    
    ``N`` must be between 1 and 32 inclusive.
    
    :param int N: The number of control points in the patch list
    :return: The patchlist topology with that number of control points
    :rtype: Topology
    """
    pass

def ResourceId_Null() -> ResourceId: # real signature unknown; restored from __doc__
    """
    ResourceId_Null()
    
    A helper function that explicitly creates an empty/invalid/null :class:`ResourceId`.
    
    :return: an empty/invalid/null :class:`ResourceId`.
    :rtype: ResourceId
    """
    pass

def ResUsage(stage: ShaderStage) -> ResourceUsage: # real signature unknown; restored from __doc__
    """
    ResUsage(stage)
    
    Calculate the ``ResourceUsage`` value for read-only resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-only resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def RWResUsage(stage: ShaderStage) -> ResourceUsage: # real signature unknown; restored from __doc__
    """
    RWResUsage(stage)
    
    Calculate the ``ResourceUsage`` value for read-write resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-write resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def SaveConfigSettings(): # real signature unknown; restored from __doc__
    """
    SaveConfigSettings()
    
    Flush the current config settings as they are in memory to the config file on disk.
    
    Without calling this function, settings changes will only be temporary. The settings are **not**
    saved to disk on exit implicitly.
    """
    pass

def SetColors(darkChecker: FloatVector, lightChecker: FloatVector, darkTheme: bool): # real signature unknown; restored from __doc__
    """
    SetColors(darkChecker, lightChecker, darkTheme)
    
    Configure the default colours used for checkerboards, this can broadly speaking help
    match the replay rendering to the overall theme of the replay application.
    
    :param FloatVector darkChecker: The color of dark squares in checkerboard patterns.
    :param FloatVector lightChecker: The color of light squares in checkerboard patterns.
    :param bool darkTheme: ``True`` if the theme is a 'dark' theme, used to pick different contrasting
      colors. ``False`` if the theme is 'light' and normal colors are used.
    """
    pass

def SetConfigSetting(name: str) -> SDObject: # real signature unknown; restored from __doc__
    """
    SetConfigSetting(name)
    
    Return a mutable handle to the :class:`SDObject` corresponding to a given setting's
    value object.
    
    If no such setting exists, `None` is returned.
    
    :param str name: The name of the setting.
    :return: The specified setting.
    :rtype: SDObject
    """
    pass

def SetDebugLogFile(filename: str): # real signature unknown; restored from __doc__
    """
    SetDebugLogFile(filename)
    
    Sets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :param str filename: The path to the new log file.
    """
    pass

def ShutdownReplay(): # real signature unknown; restored from __doc__
    """
    ShutdownReplay()
    
    Shutdown RenderDoc for replay. Replay API functions should not be called after this
    has been called. It is not safe to re-initialise replay after this function has been called so it
    should only be called at program shutdown. This function must only be called if
    :func:`InitialiseReplay` was previously called.
    """
    pass

def StartGlobalHook(pathmatch: str, logfile: str, opts: CaptureOptions) -> ResultDetails: # real signature unknown; restored from __doc__
    """
    StartGlobalHook(pathmatch, logfile, opts)
    
    Begin injecting speculatively into all new processes started on the system. Where
    supported by platform, configuration, and setup begin injecting speculatively into all new processes
    started on the system.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is not active (see :func:`IsGlobalHookActive`).
    
    The hook must be closed with :func:`StopGlobalHook` before the application is closed.
    
    This function must be called when the process is running with administrator/superuser permissions.
    
    :param str pathmatch: A string to match against each new process's executable path to determine
      which corresponds to the program we actually want to capture.
    :param str logfile: Where to store any captures.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :return: The result of the operation, if the result succeeded the hook is now active.
    :rtype: ResultDetails
    """
    pass

def StartSelfHostCapture(dllname: str): # real signature unknown; restored from __doc__
    """
    StartSelfHostCapture(dllname)
    
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to start a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass

def StopGlobalHook(): # real signature unknown; restored from __doc__
    """
    StopGlobalHook()
    
    Stop the global hook that was activated by :func:`StartGlobalHook`.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is active (see :func:`IsGlobalHookActive`).
    """
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

def ToolExecutable(tool: KnownShaderTool) -> str: # real signature unknown; restored from __doc__
    """
    ToolExecutable(tool)
    
    Returns the default executable name with no suffix for a given :class:`KnownShaderTool`.
    
    .. note::
      The executable name is returned with no suffix, e.g. ``foobar`` which may need a platform specific
      suffix like ``.exe`` appended.
    
    :param KnownShaderTool tool: The tool to get the executable name for.
    :return: The default executable name for this tool, or an empty string if the tool is unrecognised.
    :rtype: str
    """
    pass

def ToolInput(tool: KnownShaderTool) -> ShaderEncoding: # real signature unknown; restored from __doc__
    """
    ToolInput(tool)
    
    Returns the expected default input :class:`~renderdoc.ShaderEncoding` that a
    :class:`KnownShaderTool` expects. This may not be accurate and may be configurable depending on the
    tool.
    
    :param KnownShaderTool tool: The tool to get the input encoding for.
    :return: The encoding that this tool expects as an input by default.
    :rtype: renderdoc.ShaderEncoding
    """
    pass

def ToolOutput(tool: KnownShaderTool) -> ShaderEncoding: # real signature unknown; restored from __doc__
    """
    ToolOutput(tool)
    
    Returns the expected default output :class:`~renderdoc.ShaderEncoding` that a
    :class:`KnownShaderTool` produces. This may not be accurate and may be configurable depending on the
    tool.
    
    :param KnownShaderTool tool: The tool to get the output encoding for.
    :return: The encoding that this tool produces as an output by default.
    :rtype: renderdoc.ShaderEncoding
    """
    pass

def UpdateVulkanLayerRegistration(systemLevel): # real signature unknown; restored from __doc__
    """
    UpdateVulkanLayerRegistration(systemLevel)
    
    INTERNAL: Update vulkan layer registration.
    """
    pass

def VarTypeByteSize(type: VarType) -> int: # real signature unknown; restored from __doc__
    """
    VarTypeByteSize(type)
    
    Get the byte size of a variable type.
    
    :param VarType type: The variable type
    :return: The size in bytes of this type
    :rtype: int
    """
    pass

def VarTypeCompType(type: VarType) -> CompType: # real signature unknown; restored from __doc__
    """
    VarTypeCompType(type)
    
    Get the component type of a variable type.
    
    :param VarType type: The variable type
    :return: The base component type of this variable type
    :rtype: CompType
    """
    pass

def VertexOffset(topology: Topology, primitive: int) -> int: # real signature unknown; restored from __doc__
    """
    VertexOffset(topology, primitive)
    
    A utility function that returns the offset in the list of vertices of the first vertex
    in a particular primitive of a given topology. This calculation is simple but not trivial for the
    case of strip topologies.
    
    :param Topology topology: The topology to query about.
    :param int primitive: The primitive to query about.
    :return: The vertex offset where the primitive starts.
    :rtype: int
    """
    pass

# variables with complex values

__all__ = [
    'SWIG_PyInstanceMethod_New',
    'CreateHeadlessWindowingData',
    'CreateWin32WindowingData',
    'CreateXlibWindowingData',
    'CreateXCBWindowingData',
    'CreateWaylandWindowingData',
    'CreateAndroidWindowingData',
    'CreateMacOSWindowingData',
    'InitCamera',
    'HalfToFloat',
    'FloatToHalf',
    'NumVerticesPerPrimitive',
    'VertexOffset',
    'OpenCaptureFile',
    'CreateTargetControl',
    'EnumerateRemoteTargets',
    'CreateRemoteServerConnection',
    'CheckRemoteServerConnection',
    'BecomeRemoteServer',
    'GetDefaultCaptureOptions',
    'StartGlobalHook',
    'StopGlobalHook',
    'IsGlobalHookActive',
    'CanGlobalHook',
    'ExecuteAndInject',
    'InjectIntoProcess',
    'CanSelfHostedCapture',
    'StartSelfHostCapture',
    'EndSelfHostCapture',
    'NeedVulkanLayerRegistration',
    'UpdateVulkanLayerRegistration',
    'InitialiseReplay',
    'ShutdownReplay',
    'SetDebugLogFile',
    'GetLogFile',
    'LogMessage',
    'GetVersionString',
    'IsReleaseBuild',
    'GetCommitHash',
    'GetDriverInformation',
    'GetCurrentProcessMemoryUsage',
    'GetConfigSetting',
    'SetConfigSetting',
    'SaveConfigSettings',
    'SetColors',
    'CheckAndroidPackage',
    'GetSupportedDeviceProtocols',
    'GetDeviceProtocolController',
    'ResourceId_Null',
    'makeSDInt64',
    'makeSDUInt64',
    'makeSDInt32',
    'makeSDUInt32',
    'makeSDFloat',
    'makeSDBool',
    'makeSDString',
    'makeSDResourceId',
    'makeSDEnum',
    'makeSDArray',
    'makeSDStruct',
    'VarTypeByteSize',
    'VarTypeCompType',
    'CategoryForDescriptorType',
    'IsConstantBlockDescriptor',
    'IsSamplerDescriptor',
    'IsReadOnlyDescriptor',
    'IsReadWriteDescriptor',
    'GPUVendorFromPCIVendor',
    'IsD3D',
    'ToolExecutable',
    'ToolInput',
    'ToolOutput',
    'IsTextRepresentation',
    'PatchList_Topology',
    'PatchList_Count',
    'IsStrip',
    'CBUsage',
    'ResUsage',
    'RWResUsage',
    'IsGenericCounter',
    'IsAMDCounter',
    'IsIntelCounter',
    'IsNvidiaCounter',
    'IsVulkanExtendedCounter',
    'IsARMCounter',
    'MaskForStage',
    'FirstStageForMask',
    'DumpObject',
    'ReplayOutput',
    'ReplayController',
    'TargetControl',
    'CaptureAccess',
    'RemoteServer',
    'CaptureFile',
    'Camera',
    'VulkanLayerRegistrationInfo',
    'DeviceProtocolController',
    'ResourceId',
    'SDBasic',
    'SDTypeFlags',
    'SDChunkFlags',
    'SDType',
    'SDChunkMetaData',
    'SDObjectPODData',
    'StructuredObjectList',
    'SDObjectData',
    'SDObject',
    'SDChunk',
    'StructuredChunkList',
    'StructuredBufferList',
    'SDFile',
    'CaptureOptions',
    'TaskGroupSize',
    'MeshletSize',
    'MeshFormat',
    'MeshDisplay',
    'TextureDisplay',
    'TextureComponentMapping',
    'TextureSampleMapping',
    'TextureSliceMapping',
    'TextureSave',
    'DescriptorRange',
    'NewCaptureData',
    'APIUseData',
    'BusyData',
    'NewChildData',
    'TargetControlMessage',
    'EnvironmentModification',
    'CaptureFileFormat',
    'GPUDevice',
    'ReplayOptions',
    'WindowingData',
    'GlobalEnvironment',
    'ResultDetails',
    'ExecuteResult',
    'Viewport',
    'Scissor',
    'BlendEquation',
    'ColorBlend',
    'StencilFace',
    'BoundVBuffer',
    'Descriptor',
    'SamplerDescriptor',
    'DescriptorAccess',
    'DescriptorLogicalLocation',
    'UsedDescriptor',
    'Offset',
    'VertexInputAttribute',
    'ShaderMeshMessageLocation',
    'ShaderComputeMessageLocation',
    'ShaderVertexMessageLocation',
    'ShaderPixelMessageLocation',
    'ShaderGeometryMessageLocation',
    'ShaderMessageLocation',
    'ShaderMessage',
    'D3D11Layout',
    'D3D11VertexBuffer',
    'D3D11IndexBuffer',
    'D3D11InputAssembly',
    'D3D11Shader',
    'D3D11StreamOutBind',
    'D3D11StreamOut',
    'D3D11RasterizerState',
    'D3D11Rasterizer',
    'D3D11DepthStencilState',
    'D3D11BlendState',
    'D3D11OutputMerger',
    'D3D11Predication',
    'D3D11State',
    'D3D12Layout',
    'D3D12VertexBuffer',
    'D3D12IndexBuffer',
    'D3D12InputAssembly',
    'D3D12Shader',
    'D3D12StreamOutBind',
    'D3D12StreamOut',
    'D3D12RasterizerState',
    'D3D12Rasterizer',
    'D3D12DepthStencilState',
    'D3D12BlendState',
    'D3D12OM',
    'D3D12ResourceState',
    'D3D12ResourceData',
    'D3D12RootTableRange',
    'D3D12RootParam',
    'D3D12StaticSampler',
    'D3D12RootSignature',
    'D3D12Predication',
    'D3D12State',
    'FloatVector',
    'AxisMapping',
    'PathEntry',
    'SectionProperties',
    'ResourceFormat',
    'TextureFilter',
    'TextureSwizzle4',
    'ResourceDescription',
    'DescriptorStoreDescription',
    'BufferDescription',
    'TextureDescription',
    'APIEvent',
    'DebugMessage',
    'BucketRecordType',
    'ConstantBindStats',
    'SamplerBindStats',
    'ResourceBindStats',
    'ResourceUpdateStats',
    'DrawcallStats',
    'DispatchStats',
    'IndexBindStats',
    'VertexBindStats',
    'LayoutBindStats',
    'ShaderChangeStats',
    'BlendStats',
    'DepthStencilStats',
    'RasterizationStats',
    'OutputTargetStats',
    'FrameStatistics',
    'FrameDescription',
    'EventUsage',
    'Subresource',
    'ActionDescription',
    'APIProperties',
    'DriverInformation',
    'Uuid',
    'CounterDescription',
    'CounterValue',
    'CounterResult',
    'PixelValue',
    'ModificationValue',
    'PixelModification',
    'Thumbnail',
    'DebugPixelInputs',
    'GLVertexAttribute',
    'GLVertexBuffer',
    'GLVertexInput',
    'GLShader',
    'GLFixedVertexProcessing',
    'GLTextureCompleteness',
    'GLFeedback',
    'GLRasterizerState',
    'GLRasterizer',
    'GLDepthState',
    'GLStencilState',
    'GLFBO',
    'GLBlendState',
    'GLFrameBuffer',
    'GLHints',
    'GLState',
    'SectionType',
    'DebugVariableType',
    'VarType',
    'CompType',
    'TextureSwizzle',
    'AddressMode',
    'YcbcrConversion',
    'YcbcrRange',
    'ChromaSampleLocation',
    'ResourceType',
    'TextureType',
    'BindType',
    'DescriptorType',
    'DescriptorCategory',
    'ShaderBuiltin',
    'ReplayOutputType',
    'MeshDataStage',
    'DebugOverlay',
    'FileType',
    'AlphaMapping',
    'ResourceFormatType',
    'QualityHint',
    'GPUVendor',
    'GraphicsAPI',
    'ShaderEncoding',
    'KnownShaderTool',
    'Topology',
    'ShaderStage',
    'MessageCategory',
    'MessageSeverity',
    'MessageSource',
    'ResourceUsage',
    'Visualisation',
    'FillMode',
    'CullMode',
    'ConservativeRaster',
    'ShadingRateCombiner',
    'LineRaster',
    'FilterMode',
    'FilterFunction',
    'CompareFunction',
    'StencilOperation',
    'BlendMultiplier',
    'BlendOperation',
    'LogicOperation',
    'GPUCounter',
    'CounterUnit',
    'CameraType',
    'ReplaySupport',
    'ResultCode',
    'TargetControlMessageType',
    'EnvMod',
    'EnvSep',
    'LogType',
    'ReplayOptimisationLevel',
    'WindowingSystem',
    'PathProperty',
    'SectionFlags',
    'BufferCategory',
    'DescriptorFlags',
    'TextureCategory',
    'ShaderStageMask',
    'ShaderEvents',
    'ShaderVariableFlags',
    'ActionFlags',
    'VulkanLayerFlags',
    'AndroidFlags',
    'PointerVal',
    'ShaderBindIndex',
    'ShaderDirectAccess',
    'ShaderValue',
    'ShaderVariable',
    'DebugVariableReference',
    'SourceVariableMapping',
    'LineColumnInfo',
    'InstructionSourceInfo',
    'ShaderVariableChange',
    'ShaderDebugState',
    'ShaderDebugger',
    'ShaderDebugTrace',
    'SigParameter',
    'ShaderConstantType',
    'ShaderConstant',
    'ConstantBlock',
    'ShaderSampler',
    'ShaderResource',
    'ShaderEntryPoint',
    'ShaderCompileFlag',
    'ShaderCompileFlags',
    'ShaderSourcePrefix',
    'ShaderSourceFile',
    'ShaderDebugInfo',
    'ShaderReflection',
    'VKDynamicOffset',
    'VKDescriptorSet',
    'VKDescriptorBuffer',
    'VKPipeline',
    'VKIndexBuffer',
    'VKInputAssembly',
    'VKVertexAttribute',
    'VKVertexBinding',
    'VKVertexBuffer',
    'VKVertexInput',
    'VKShader',
    'VKTessellation',
    'VKXFBBuffer',
    'VKTransformFeedback',
    'VKRenderArea',
    'VKViewportScissor',
    'VKViewState',
    'VKRasterizer',
    'VKSampleLocations',
    'VKMultiSample',
    'VKColorBlendState',
    'VKDepthStencil',
    'VKRenderPass',
    'VKFramebuffer',
    'VKCurrentPass',
    'VKImageLayout',
    'VKImageData',
    'VKConditionalRendering',
    'VKState',
    'PipeState',
    'rdcarray_of_int',
    'rdcarray_of_float',
    'rdcarray_of_uint32_t',
    'rdcarray_of_uint64_t',
    'rdcarray_of_rdcstr',
    'rdcarray_of_WindowingSystem',
    'rdcarray_of_ActionDescription',
    'rdcarray_of_GPUCounter',
    'rdcarray_of_CounterResult',
    'rdcarray_of_APIEvent',
    'rdcarray_of_DescriptorStoreDescription',
    'rdcarray_of_BufferDescription',
    'rdcarray_of_CaptureFileFormat',
    'rdcarray_of_ConstantBlock',
    'rdcarray_of_DebugMessage',
    'rdcarray_of_EnvironmentModification',
    'rdcarray_of_EventUsage',
    'rdcarray_of_PathEntry',
    'rdcarray_of_PixelModification',
    'rdcarray_of_TaskGroupSize',
    'rdcarray_of_MeshletSize',
    'rdcarray_of_ResourceDescription',
    'rdcarray_of_ResourceId',
    'rdcarray_of_LineColumnInfo',
    'rdcarray_of_InstructionSourceInfo',
    'rdcarray_of_ShaderCompileFlag',
    'rdcarray_of_ShaderConstant',
    'rdcarray_of_ShaderDebugState',
    'rdcarray_of_ShaderMessage',
    'rdcarray_of_ShaderResource',
    'rdcarray_of_ShaderSampler',
    'rdcarray_of_ShaderSourceFile',
    'rdcarray_of_ShaderSourcePrefix',
    'rdcarray_of_ShaderVariable',
    'rdcarray_of_ShaderEncoding',
    'rdcarray_of_ShaderVariableChange',
    'rdcarray_of_DebugVariableReference',
    'rdcarray_of_SourceVariableMapping',
    'rdcarray_of_SigParameter',
    'rdcarray_of_TextureDescription',
    'rdcarray_of_ShaderEntryPoint',
    'rdcarray_of_Viewport',
    'rdcarray_of_Scissor',
    'rdcarray_of_ColorBlend',
    'rdcarray_of_BoundVBuffer',
    'rdcarray_of_Offset',
    'rdcarray_of_VertexInputAttribute',
    'rdcarray_of_FloatVector',
    'rdcarray_of_GraphicsAPI',
    'rdcarray_of_GPUDevice',
    'rdcarray_of_ShaderConstantType',
    'rdcarray_of_ShaderChangeStats',
    'rdcarray_of_ResourceBindStats',
    'rdcarray_of_SamplerBindStats',
    'rdcarray_of_ConstantBindStats',
    'rdcarray_of_DescriptorRange',
    'rdcarray_of_Descriptor',
    'rdcarray_of_SamplerDescriptor',
    'rdcarray_of_DescriptorAccess',
    'rdcarray_of_DescriptorLogicalLocation',
    'rdcarray_of_UsedDescriptor',
    'rdcarray_of_VKPipe_DynamicOffset',
    'rdcarray_of_VKPipe_DescriptorSet',
    'rdcarray_of_VKPipe_DescriptorBuffer',
    'rdcarray_of_VKPipe_ImageData',
    'rdcarray_of_VKPipe_ImageLayout',
    'rdcarray_of_VKPipe_RenderArea',
    'rdcarray_of_VKPipe_XFBBuffer',
    'rdcarray_of_VKPipe_VertexBuffer',
    'rdcarray_of_VKPipe_VertexAttribute',
    'rdcarray_of_VKPipe_VertexBinding',
    'rdcarray_of_VKPipe_ViewportScissor',
    'rdcarray_of_D3D11Pipe_Layout',
    'rdcarray_of_D3D11Pipe_StreamOutBind',
    'rdcarray_of_D3D11Pipe_VertexBuffer',
    'rdcarray_of_D3D12Pipe_Layout',
    'rdcarray_of_D3D12Pipe_ResourceData',
    'rdcarray_of_D3D12Pipe_ResourceState',
    'rdcarray_of_D3D12Pipe_StreamOutBind',
    'rdcarray_of_D3D12Pipe_VertexBuffer',
    'rdcarray_of_D3D12Pipe_RootTableRange',
    'rdcarray_of_D3D12Pipe_RootParam',
    'rdcarray_of_D3D12Pipe_StaticSampler',
    'rdcarray_of_GLPipe_VertexBuffer',
    'rdcarray_of_GLPipe_VertexAttribute',
    'rdcarray_of_GLPipe_TextureCompleteness',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000176CFC5C7D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='renderdoc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000176CFC5C7D0>, origin='C:\\\\Users\\\\13908\\\\Desktop\\\\works\\\\renderdoc_pythonmodules\\\\x64\\\\Development\\\\pymodules\\\\renderdoc.pyd')"

