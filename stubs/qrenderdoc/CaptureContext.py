# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CaptureViewer import CaptureViewer
from .DockReference import DockReference
from .PersistantConfig import PersistantConfig
from .RemoteHost import RemoteHost
from .ShaderViewer import ShaderViewer
from .ExtensionManager import ExtensionManager
from .AnnotationViewer import AnnotationViewer
from .APIInspector import APIInspector
from .EventBookmark import EventBookmark
from .CaptureDialog import CaptureDialog
from .CaptureModifications import CaptureModifications
from .CommentView import CommentView
from .DebugMessageView import DebugMessageView
from .DiagnosticLogView import DiagnosticLogView
from .EventBrowser import EventBrowser
from .MainWindow import MainWindow
from .BufferViewer import BufferViewer
from .PerformanceCounterViewer import PerformanceCounterViewer
from .PipelineStateViewer import PipelineStateViewer
from .PythonShell import PythonShell
from .ResourceInspector import ResourceInspector
from .RGPInterop import RGPInterop
from .StatisticsViewer import StatisticsViewer
from .TextureViewer import TextureViewer
from .TimelineBar import TimelineBar
from .ReplayManager import ReplayManager
from .DescriptorViewer import DescriptorViewer
from .PixelHistoryView import PixelHistoryView
from .ShaderMessageViewer import ShaderMessageViewer

from renderdoc.ActionDescription import ActionDescription

from renderdoc.APIProperties import APIProperties

from renderdoc.BufferDescription import BufferDescription

from renderdoc.CaptureFileFormat import CaptureFileFormat

from renderdoc.D3D11State import D3D11State

from renderdoc.D3D12State import D3D12State

from renderdoc.DebugMessage import DebugMessage

from renderdoc.Descriptor import Descriptor

from renderdoc.DescriptorStoreDescription import DescriptorStoreDescription

from renderdoc.FrameDescription import FrameDescription

from renderdoc.GLState import GLState

from renderdoc.KnownShaderTool import KnownShaderTool

from renderdoc.PipeState import PipeState

from renderdoc.ReplayOptions import ReplayOptions

from renderdoc.ResourceDescription import ResourceDescription

from renderdoc.ResourceId import ResourceId

from renderdoc.ResultDetails import ResultDetails

from renderdoc.SamplerDescriptor import SamplerDescriptor

from renderdoc.SDFile import SDFile

from renderdoc.ShaderCompileFlags import ShaderCompileFlags

from renderdoc.ShaderDebugTrace import ShaderDebugTrace

from renderdoc.ShaderEncoding import ShaderEncoding

from renderdoc.ShaderReflection import ShaderReflection

from renderdoc.ShaderSourcePrefix import ShaderSourcePrefix

from renderdoc.ShaderStage import ShaderStage

from renderdoc.ShaderStageMask import ShaderStageMask

from renderdoc.Subresource import Subresource

from renderdoc.TextureDescription import TextureDescription

from renderdoc.TextureDisplay import TextureDisplay

from renderdoc.VKState import VKState

from renderdoc.WindowingData import WindowingData

from renderdoc.WindowingSystem import WindowingSystem

from ShaderViewer.RevertCallback import RevertCallback

from ShaderViewer.SaveCallback import SaveCallback

class CaptureContext(): # skipped bases: <class 'SwigPyObject'>
    """ The capture context that the python script is running in. """
    def AddCaptureViewer(self, viewer: CaptureViewer): # real signature unknown; restored from __doc__
        """
        AddCaptureViewer(viewer)
        
        Register a new instance of :class:`CaptureViewer` to receive capture event notifications.
        
        :param CaptureViewer viewer: The viewer to register.
        """
        pass

    def AddDockWindow(self, newWindow: QWidget, ref: DockReference, refWindow: QWidget, percentage: float=0.5): # real signature unknown; restored from __doc__
        """
        AddDockWindow(newWindow, ref, refWindow, percentage=0.5)
        AddDockWindow(newWindow, ref, refWindow)
        
        Adds a new window within the docking system.
        
        :param QWidget newWindow: The new window to add.
        :param DockReference ref: The location to add the new window, possibly relative to ``refWindow``.
        :param QWidget refWindow: The window to refer to if the new window is being added relative, or can
          be ``None`` if the new location is absolute.
        :param float percentage: Optionally the percentage to split the area. If omitted, a 50% split is
          used.
        """
        pass

    def AddMessages(self, msgs: List[DebugMessage]): # real signature unknown; restored from __doc__
        """
        AddMessages(msgs)
        
        Add messages into the list returned by :meth:`DebugMessages`. Initially set to unread.
        
        :param List[renderdoc.DebugMessage] msgs: A list of debug messages to add.
        """
        pass

    def APIProps(self) -> APIProperties: # real signature unknown; restored from __doc__
        """
        APIProps()
        
        Retrieve the :class:`~renderdoc.APIProperties` for the currently loaded capture.
        
        :return: The API properties.
        :rtype: renderdoc.APIProperties
        """
        pass

    def BuiltinWindowClosed(self, window: QWidget): # real signature unknown; restored from __doc__
        """
        BuiltinWindowClosed(window)
        
        Marks a built-in window as closed.
        
        This function is intended for internal use by the built-in windows for singleton management, and
        should not be called by user code.
        
        :param QWidget window: The built-in window that closed.
        """
        pass

    def ClearMessages(self): # real signature unknown; restored from __doc__
        """
        ClearMessages()
        
        Clear the currently stored messages, and mark all as unread. This can be used in
        combination with :meth:`DebugMessages` and :meth:`AddMessages` to filter the current set of messages.
        """
        pass

    def ClearReplayCache(self): # real signature unknown; restored from __doc__
        """
        ClearReplayCache()
        
        Clear any cached data from previous replays and ensure subsequent replays fully
        re-initialise any data, including e.g. bindless feedback, printf results or mesh output data.
        """
        pass

    def CloseCapture(self): # real signature unknown; restored from __doc__
        """
        CloseCapture()
        
        Close the currently open capture file.
        """
        pass

    def Config(self) -> PersistantConfig: # real signature unknown; restored from __doc__
        """
        Config()
        
        Retrieve the current persistant config.
        
        :return: The current persistant config manager.
        :rtype: PersistantConfig
        """
        pass

    def ConnectToRemoteServer(self, host: RemoteHost): # real signature unknown; restored from __doc__
        """
        ConnectToRemoteServer(host)
        
        Connect to a remote server.
        
        :param RemoteHost host: The host to connect to.
        """
        pass

    def CreateBuiltinWindow(self, objectName: str) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateBuiltinWindow(objectName)
        
        Creates and returns a built-in window.
        
        This function is intended for internal use for restoring layouts, and generally should not be used
        by user code.
        
        :param str objectName: The built-in name of a singleton window.
        :return: The handle to the existing or newly created window of this type.
        :rtype: QWidget
        """
        pass

    def CreateWindowingData(self, window: QWidget) -> WindowingData: # real signature unknown; restored from __doc__
        """
        CreateWindowingData(window)
        
        Create an opaque pointer suitable for passing to
        :meth:`~renderdoc.ReplayController.CreateOutput` or other functions that expect windowing data.
        
        .. note::
          This function must be called on the main UI thread.
        
        :param QWidget window: The window to create windowing data for.
        :return: The windowing data.
        :rtype: renderdoc.WindowingData
        """
        pass

    def CurAction(self) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        CurAction()
        
        Retrieve the current action.
        
        :return: The current action, or ``None`` if no action is selected.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def CurD3D11PipelineState(self) -> D3D11State: # real signature unknown; restored from __doc__
        """
        CurD3D11PipelineState()
        
        Retrieve the current :class:`~renderdoc.D3D11State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D11 API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current D3D11 pipeline state.
        :rtype: renderdoc.D3D11State
        """
        pass

    def CurD3D12PipelineState(self) -> D3D12State: # real signature unknown; restored from __doc__
        """
        CurD3D12PipelineState()
        
        Retrieve the current :class:`~renderdoc.D3D12State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D12 API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current D3D12 pipeline state.
        :rtype: renderdoc.D3D12State
        """
        pass

    def CurEvent(self) -> int: # real signature unknown; restored from __doc__
        """
        CurEvent()
        
        Retrieve the current :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        :return: The current event.
        :rtype: int
        """
        pass

    def CurGLPipelineState(self) -> GLState: # real signature unknown; restored from __doc__
        """
        CurGLPipelineState()
        
        Retrieve the current :class:`~renderdoc.GLState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the OpenGL API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current OpenGL pipeline state.
        :rtype: renderdoc.GLState
        """
        pass

    def CurPipelineState(self) -> PipeState: # real signature unknown; restored from __doc__
        """
        CurPipelineState()
        
        Retrieve the current :class:`~renderdoc.PipeState` abstracted pipeline state.
        
        This pipeline state will always be valid, and allows queries that will work regardless of the
        capture's API.
        
        :return: The current API-agnostic abstracted pipeline state.
        :rtype: renderdoc.PipeState
        """
        pass

    def CurRootActions(self) -> List[ActionDescription]: # real signature unknown; restored from __doc__
        """
        CurRootActions()
        
        Retrieve the root list of actions in the current capture.
        
        :return: The root actions.
        :rtype: List[renderdoc.ActionDescription]
        """
        pass

    def CurSelectedAction(self) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        CurSelectedAction()
        
        Retrieve the currently selected action.
        
        In most cases, prefer using :meth:`CurAction`. See :meth:`CaptureViewer.OnSelectedEventChanged` for
        more information for how this differs.
        
        :return: The currently selected action.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def CurSelectedEvent(self) -> int: # real signature unknown; restored from __doc__
        """
        CurSelectedEvent()
        
        Retrieve the currently selected :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        In most cases, prefer using :meth:`CurEvent`. See :meth:`CaptureViewer.OnSelectedEventChanged` for more
        information for how this differs.
        
        :return: The current selected event.
        :rtype: int
        """
        pass

    def CurVulkanPipelineState(self) -> VKState: # real signature unknown; restored from __doc__
        """
        CurVulkanPipelineState()
        
        Retrieve the current :class:`~renderdoc.VKState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the Vulkan API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current Vulkan pipeline state.
        :rtype: renderdoc.VKState
        """
        pass

    def CurWindowingSystem(self) -> WindowingSystem: # real signature unknown; restored from __doc__
        """
        CurWindowingSystem()
        
        Retrieve the current windowing system in use.
        
        :return: The active windowing system.
        :rtype: renderdoc.WindowingSystem
        """
        pass

    def CustomShaderEncodings(self) -> List[ShaderEncoding]: # real signature unknown; restored from __doc__
        """
        CustomShaderEncodings()
        
        Retrieve the list of :class:`~renderdoc.ShaderEncoding` that are available for
        building custom shaders for the currently loaded capture. See
        :meth:`~renderdoc.ReplayController.BuildCustomShader`.
        
        :return: The available encodings.
        :rtype: List[renderdoc.ShaderEncoding]
        """
        pass

    def CustomShaderSourcePrefixes(self) -> List[ShaderSourcePrefix]: # real signature unknown; restored from __doc__
        """
        CustomShaderSourcePrefixes()
        
        Retrieve the list of prefixes for each :class:`~renderdoc.ShaderEncoding` that should
        be added to custom compiled shaders. See
        :meth:`~renderdoc.ReplayController.GetCustomShaderSourcePrefixes`.
        
        :return: A list of pairs, listing a prefix for each shader encoding referenced.
        :rtype: List[renderdoc.ShaderSourcePrefix]
        """
        pass

    def DebugMessages(self) -> List[DebugMessage]: # real signature unknown; restored from __doc__
        """
        DebugMessages()
        
        Retrieve the current list of debug messages. This includes messages from the capture
        as well as messages generated during replay and analysis.
        
        :return: The debug messages generated to date.
        :rtype: List[renderdoc.DebugMessage]
        """
        pass

    def DebugShader(self, shader: ShaderReflection, pipeline: ResourceId, trace: ShaderDebugTrace, debugContext: str) -> ShaderViewer: # real signature unknown; restored from __doc__
        """
        DebugShader(shader, pipeline, trace, debugContext)
        
        Show a new :class:`ShaderViewer` window, showing a read-only view of a debug trace
        through the execution of a given shader.
        
        :param renderdoc.ShaderReflection shader: The reflection data for the shader to view.
        :param renderdoc.ResourceId pipeline: The pipeline state object, if applicable, that this shader is
          bound to.
        :param renderdoc.ShaderDebugTrace trace: The execution trace of the debugged shader.
        :param str debugContext: A human-readable context string describing which invocation of this shader
          was debugged. For example 'Pixel 12,34 at eventId 678'.
        :return: The new :class:`ShaderViewer` window opened, but not shown.
        :rtype: ShaderViewer
        """
        pass

    def DelayedCallback(self, milliseconds: int, callback: Callable[[], None]): # real signature unknown; restored from __doc__
        """
        DelayedCallback(milliseconds, callback)
        
        Registers a delayed callback to be called after a certain number of milliseconds
        on the UI thread.
        
        :param int milliseconds: The number of milliseconds (approximately) to wait before the callback.
        :param Callable[[], None] callback: The function to call
        """
        pass

    def EditShader(self, id: ResourceId, stage: ShaderStage, entryPoint: str, files: List[Tuple[str,str]], knownTool: KnownShaderTool, shaderEncoding: ShaderEncoding, flags: ShaderCompileFlags, saveCallback: SaveCallback, revertCallback: RevertCallback) -> ShaderViewer: # real signature unknown; restored from __doc__
        """
        EditShader(id, stage, entryPoint, files, knownTool, shaderEncoding, flags, saveCallback, revertCallback)
        
        Show a new :class:`ShaderViewer` window, showing an editable view of a given shader.
        
        :param renderdoc.ResourceId id: The shader object, if applicable, that's being edited. If this edit
          corresponds to no shader object (such as if it's a custom shader) this can be a null ID.
        :param renderdoc.ShaderStage stage: The shader stage for this shader.
        :param str entryPoint: The entry point to be used when compiling the edited shader.
        :param List[Tuple[str,str]] files: The source files, with each tuple being a pair of the filename
          and the file contents.
        :param renderdoc.KnownShaderTool knownTool: The preferred tool to use to compile, if known.
        :param renderdoc.ShaderEncoding shaderEncoding: The encoding of the input files.
        :param renderdoc.ShaderCompileFlags flags: The flags originally used to compile the shader.
        :param ShaderViewer.SaveCallback saveCallback: The callback function to call when a save/update is
          triggered.
          Callback function signature must match :func:`ShaderViewer.SaveCallback`.
        :param ShaderViewer.RevertCallback revertCallback: The callback function to call when the shader
          is to be reverted - either by user request or because the shader viewer was closed.
          Callback function signature must match :func:`ShaderViewer.RevertCallback`.
        :return: The new :class:`ShaderViewer` window opened but not shown for editing.
        :rtype: ShaderViewer
        """
        pass

    def EmbedDependentFiles(self): # real signature unknown; restored from __doc__
        """
        EmbedDependentFiles()
        
        Stores the dependent file data into the capture i.e. shader debug files.
        
        This reads the contents of the dependent files and stores their file contents into the capture.
        This can help the capture to be more portable by embedding all externally referenced dependent files.
        Use :meth:`RemoveDependentFiles` to remove the embedded file data.
        
        .. warning::
          Will remove all the existing embedded file data from the capture.
          Will directly modify the capture file on disk.
        
        .. note::
          This will increase the size of the capture file.
          Externally referenced files which can't be found on disk are skipped.
          For remote replay the modifications are performed on the remote machine and copied back to the local host.
        """
        pass

    def ExportCapture(self, fmt: CaptureFileFormat, exportfile: str): # real signature unknown; restored from __doc__
        """
        ExportCapture(fmt, exportfile)
        
        Exports the current capture file to a given path with a specified capture file format.
        
        The capture must be available locally, if it's not this function will fail.
        
        :param renderdoc.CaptureFileFormat fmt: The capture file format to export to.
        :param str exportfile: The path to export the capture file to.
        """
        pass

    def Extensions(self) -> ExtensionManager: # real signature unknown; restored from __doc__
        """
        Extensions()
        
        Retrieve the manager for extensions.
        
        :return: The current extension manager.
        :rtype: ExtensionManager
        """
        pass

    def FrameInfo(self) -> FrameDescription: # real signature unknown; restored from __doc__
        """
        FrameInfo()
        
        Retrieve the :class:`~renderdoc.FrameDescription` for the currently loaded capture.
        
        :return: The frame information.
        :rtype: renderdoc.FrameDescription
        """
        pass

    def GetAction(self, eventId: int) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        GetAction(eventId)
        
        Retrieve the information about an action at a given
        :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: The information about the action, or ``None`` if the
          :data:`eventId <renderdoc.APIEvent.eventId>` doesn't correspond to an action.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def GetAnnotationViewer(self) -> AnnotationViewer: # real signature unknown; restored from __doc__
        """
        GetAnnotationViewer()
        
        Retrieve the current singleton :class:`AnnotationViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: AnnotationViewer
        """
        pass

    def GetAPIInspector(self) -> APIInspector: # real signature unknown; restored from __doc__
        """
        GetAPIInspector()
        
        Retrieve the current singleton :class:`APIInspector`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: APIInspector
        """
        pass

    def GetBookmarks(self) -> List[EventBookmark]: # real signature unknown; restored from __doc__
        """
        GetBookmarks()
        
        Get the current list of bookmarks in the capture. Each bookmark is associated with an
        eventId and has some text attached. There will only be at most one bookmark for any given eventId.
        
        The list of bookmarks is not necessarily sorted by eventId. Thus, bookmark 1 is always bookmark 1
        until it is removed, the indices do not shift as new bookmarks are added or removed.
        
        :return: The currently set bookmarks.
        :rtype: List[EventBookmark]
        """
        pass

    def GetBuffer(self, id: ResourceId) -> BufferDescription: # real signature unknown; restored from __doc__
        """
        GetBuffer(id)
        
        Retrieve the information about a particular buffer.
        
        :param renderdoc.ResourceId id: The ID of the buffer to query about.
        :return: The information about a buffer, or ``None`` if the ID does not correspond to a buffer.
        :rtype: renderdoc.BufferDescription
        """
        pass

    def GetBuffers(self) -> List[BufferDescription]: # real signature unknown; restored from __doc__
        """
        GetBuffers()
        
        Retrieve the list of buffers in the current capture.
        
        :return: The list of buffers.
        :rtype: List[renderdoc.BufferDescription]
        """
        pass

    def GetCaptureDialog(self) -> CaptureDialog: # real signature unknown; restored from __doc__
        """
        GetCaptureDialog()
        
        Retrieve the current singleton :class:`CaptureDialog`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: CaptureDialog
        """
        pass

    def GetCaptureFilename(self) -> str: # real signature unknown; restored from __doc__
        """
        GetCaptureFilename()
        
        Retrieve the filename for the currently loaded capture.
        
        :return: The filename of the current capture.
        :rtype: str
        """
        pass

    def GetCaptureModifications(self) -> CaptureModifications: # real signature unknown; restored from __doc__
        """
        GetCaptureModifications()
        
        Get a bitmask indicating which modifications (if any) have been made to the capture in
        the UI which aren't reflected in the capture file on disk.
        
        :return: The modifications (if any) that have been made to the capture.
        :rtype: CaptureModifications
        """
        pass

    def GetCommentView(self) -> CommentView: # real signature unknown; restored from __doc__
        """
        GetCommentView()
        
        Retrieve the current singleton :class:`CommentView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: CommentView
        """
        pass

    def GetDebugMessageView(self) -> DebugMessageView: # real signature unknown; restored from __doc__
        """
        GetDebugMessageView()
        
        Retrieve the current singleton :class:`DebugMessageView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: DebugMessageView
        """
        pass

    def GetDescriptorStore(self, id: ResourceId) -> DescriptorStoreDescription: # real signature unknown; restored from __doc__
        """
        GetDescriptorStore(id)
        
        Retrieve the information about a particular descriptor store.
        
        :param renderdoc.ResourceId id: The ID of the buffer to query about.
        :return: The information about a descriptor store, or ``None`` if the ID does not correspond to a
          descriptor store.
        :rtype: renderdoc.DescriptorStoreDescription
        """
        pass

    def GetDiagnosticLogView(self) -> DiagnosticLogView: # real signature unknown; restored from __doc__
        """
        GetDiagnosticLogView()
        
        Retrieve the current singleton :class:`LogView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: DiagnosticLogView
        """
        pass

    def GetEventBrowser(self) -> EventBrowser: # real signature unknown; restored from __doc__
        """
        GetEventBrowser()
        
        Retrieve the current singleton :class:`EventBrowser`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: EventBrowser
        """
        pass

    def GetFatalError(self) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        GetFatalError()
        
        If a capture is loaded, return the current fatal error status.
        
        :return: If a capture is currently loaded, return the fatal error status.
        :rtype: renderdoc.ResultDetails
        """
        pass

    def GetFirstAction(self) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        GetFirstAction()
        
        Retrieve the first action in the capture.
        
        :return: The first action.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def GetLastAction(self) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        GetLastAction()
        
        Retrieve the last action in the capture.
        
        :return: The last action.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def GetMainWindow(self) -> MainWindow: # real signature unknown; restored from __doc__
        """
        GetMainWindow()
        
        Retrieve the current singleton :class:`MainWindow`.
        
        :return: The current window.
        :rtype: MainWindow
        """
        pass

    def GetMeshPreview(self) -> BufferViewer: # real signature unknown; restored from __doc__
        """
        GetMeshPreview()
        
        Retrieve the current singleton :class:`BufferViewer` configured for mesh viewing.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: BufferViewer
        """
        pass

    def GetNotes(self, key: str) -> str: # real signature unknown; restored from __doc__
        """
        GetNotes(key)
        
        Retrieve the contents for a given notes field.
        
        Examples of fields are:
        
        * 'comments' for generic comments to be displayed in a text field
        * 'hwinfo' for a plaintext summary of the hardware and driver configuration of the system.
        
        :param str key: The name of the notes field to retrieve.
        :return: The contents, or an empty string if the field doesn't exist.
        :rtype: str
        """
        pass

    def GetPerformanceCounterViewer(self) -> PerformanceCounterViewer: # real signature unknown; restored from __doc__
        """
        GetPerformanceCounterViewer()
        
        Retrieve the current singleton :class:`PerformanceCounterViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PerformanceCounterViewer
        """
        pass

    def GetPipelineViewer(self) -> PipelineStateViewer: # real signature unknown; restored from __doc__
        """
        GetPipelineViewer()
        
        Retrieve the current singleton :class:`PipelineStateViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PipelineStateViewer
        """
        pass

    def GetPythonShell(self) -> PythonShell: # real signature unknown; restored from __doc__
        """
        GetPythonShell()
        
        Retrieve the current singleton :class:`PythonShell`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PythonShell
        """
        pass

    def GetResource(self, id: ResourceId) -> ResourceDescription: # real signature unknown; restored from __doc__
        """
        GetResource(id)
        
        Retrieve the information about a particular resource.
        
        :param renderdoc.ResourceId id: The ID of the resource to query about.
        :return: The information about a resource, or ``None`` if the ID does not correspond to a resource.
        :rtype: renderdoc.ResourceDescription
        """
        pass

    def GetResourceInspector(self) -> ResourceInspector: # real signature unknown; restored from __doc__
        """
        GetResourceInspector()
        
        Retrieve the current singleton :class:`ResourceInspector`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: ResourceInspector
        """
        pass

    def GetResourceName(self, id: ResourceId) -> str: # real signature unknown; restored from __doc__
        """
        GetResourceName(id)
        
        Retrieve the human-readable name for the resource to display.
        
        This will first check to see if a custom name has been set for the resource, and if so use that. See
        :meth:`SetResourceCustomName`. If no custom name has been set, it will use the resource name found
        in the capture, either a name set via API-specific debug methods, or an auto-generated name based on
        the resource type.
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: The current name of the resource.
        :rtype: str
        """
        pass

    def GetResourceNameUnsuffixed(self, id: ResourceId) -> str: # real signature unknown; restored from __doc__
        """
        GetResourceNameUnsuffixed(id)
        
        Returns the same name as :meth:`GetResourceName` but without any added suffix, e.g. to
        indicate the resource's status such as (Edited).
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: The unsuffixed resource name.
        :rtype: str
        """
        pass

    def GetResourceReplacement(self, id: ResourceId) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetResourceReplacement(id)
        
        Return the id of a replacement for the given resource. See
        :meth:`RegisterReplacement` and :meth:`IsResourceReplaced`.
        
        :param renderdoc.ResourceId id: The id of the resource to check.
        :return: The replacement id, or a null id if the resource hasn't been replaced
        :rtype: renderdoc.ResourceId
        """
        pass

    def GetResources(self) -> List[ResourceDescription]: # real signature unknown; restored from __doc__
        """
        GetResources()
        
        Retrieve the list of resources in the current capture.
        
        :return: The list of resources.
        :rtype: List[renderdoc.ResourceDescription]
        """
        pass

    def GetRGPInterop(self) -> RGPInterop: # real signature unknown; restored from __doc__
        """
        GetRGPInterop()
        
        Returns the current interop handle for RGP.
        
        This may return ``None`` in several cases:
        
        - if there is no capture loaded
        - if no RGP profile has been associated with the current capture yet (See :meth:`OpenRGPProfile`)
        - if RGP failed to launch or connect.
        
        The handle returned is invalidated when the capture is closed, or if :meth:`OpenRGPProfile` is
        called.
        
        :return: The RGP interop connection handle.
        :rtype: RGPInterop
        """
        pass

    def GetStatisticsViewer(self) -> StatisticsViewer: # real signature unknown; restored from __doc__
        """
        GetStatisticsViewer()
        
        Retrieve the current singleton :class:`StatisticsViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: StatisticsViewer
        """
        pass

    def GetStructuredFile(self) -> SDFile: # real signature unknown; restored from __doc__
        """
        GetStructuredFile()
        
        Retrieve the :class:`~renderdoc.SDFile` for the currently open capture.
        
        :return: The structured file.
        :rtype: renderdoc.SDFile
        """
        pass

    def GetTexture(self, id: ResourceId) -> TextureDescription: # real signature unknown; restored from __doc__
        """
        GetTexture(id)
        
        Retrieve the information about a particular texture.
        
        :param renderdoc.ResourceId id: The ID of the texture to query about.
        :return: The information about a texture, or ``None`` if the ID does not correspond to a texture.
        :rtype: renderdoc.TextureDescription
        """
        pass

    def GetTextures(self) -> List[TextureDescription]: # real signature unknown; restored from __doc__
        """
        GetTextures()
        
        Retrieve the list of textures in the current capture.
        
        :return: The list of textures.
        :rtype: List[renderdoc.TextureDescription]
        """
        pass

    def GetTextureViewer(self) -> TextureViewer: # real signature unknown; restored from __doc__
        """
        GetTextureViewer()
        
        Retrieve the current singleton :class:`TextureViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: TextureViewer
        """
        pass

    def GetTimelineBar(self) -> TimelineBar: # real signature unknown; restored from __doc__
        """
        GetTimelineBar()
        
        Retrieve the current singleton :class:`TimelineBar`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: TimelineBar
        """
        pass

    def HasAnnotationViewer(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasAnnotationViewer()
        
        Check if there is a current :class:`AnnotationViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasAPIInspector(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasAPIInspector()
        
        Check if there is a current :class:`APIInspector` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasCaptureDialog(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasCaptureDialog()
        
        Check if there is a current :class:`CaptureDialog` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasCommentView(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasCommentView()
        
        Check if there is a current :class:`CommentView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasDebugMessageView(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasDebugMessageView()
        
        Check if there is a current :class:`DebugMessageView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasDiagnosticLogView(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasDiagnosticLogView()
        
        Check if there is a current :class:`DiagnosticLogView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasEventBrowser(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasEventBrowser()
        
        Check if there is a current :class:`EventBrowser` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasMeshPreview(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasMeshPreview()
        
        Check if there is a current mesh previewing :class:`BufferViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasPerformanceCounterViewer(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasPerformanceCounterViewer()
        
        Check if there is a current :class:`PerformanceCounterViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasPipelineViewer(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasPipelineViewer()
        
        Check if there is a current :class:`PipelineStateViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasPythonShell(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasPythonShell()
        
        Check if there is a current :class:`PythonShell` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasResourceCustomName(self, id: ResourceId) -> bool: # real signature unknown; restored from __doc__
        """
        HasResourceCustomName(id)
        
        Checks whether a runtime custom name has been set with :meth:`SetResourceCustomName`.
        
        In general, :meth:`IsAutogeneratedName` should be preferred to check if the resource name is default
        generated just from the ID, or if it has been set to some human readable name. This function will
        only check if a name has been set in the UI itself, a resource could still have a custom name that
        was set programmatically during capture time.
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: Whether the name for the resource has been customised with :meth:`SetResourceCustomName`.
        :rtype: bool
        """
        pass

    def HasResourceInspector(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasResourceInspector()
        
        Check if there is a current :class:`ResourceInspector` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasStatisticsViewer(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasStatisticsViewer()
        
        Check if there is a current :class:`StatisticsViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasTextureViewer(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasTextureViewer()
        
        Check if there is a current :class:`TextureViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def HasTimelineBar(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasTimelineBar()
        
        Check if there is a current :class:`TimelineBar` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass

    def ImportCapture(self, fmt: CaptureFileFormat, importfile: str, rdcfile: str) -> bool: # real signature unknown; restored from __doc__
        """
        ImportCapture(fmt, importfile, rdcfile)
        
        Imports a capture file from a non-native format, via conversion to temporary rdc.
        
        This converts the file to a specified temporary .rdc and loads it, closing any existing capture.
        
        The capture must be available locally, if it's not this function will fail.
        
        :param renderdoc.CaptureFileFormat fmt: The capture file format to import from.
        :param str importfile: The path to import from.
        :param str rdcfile: The temporary path to save the rdc file to.
        :return: ``True`` if the import operation was successful and the capture was loaded.
        :rtype: bool
        """
        pass

    def IsAutogeneratedName(self, id: ResourceId) -> bool: # real signature unknown; restored from __doc__
        """
        IsAutogeneratedName(id)
        
        Determines whether the name for the given resource has been customised at all, either
        during capture time or with :meth:`SetResourceCustomName`.
        
        If not, the name is just auto-generated based on the ID and resource type, so depending on
        circumstance it may be preferable to omit the name.
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: Whether the name for the resource has just been auto-generated.
        :rtype: bool
        """
        pass

    def IsCaptureLoaded(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureLoaded()
        
        Check whether or not a capture is currently loaded.
        
        :return: ``True`` if a capture is loaded.
        :rtype: bool
        """
        pass

    def IsCaptureLoading(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureLoading()
        
        Check whether or not a capture is currently loading in-progress.
        
        :return: ``True`` if a capture is currently loading.
        :rtype: bool
        """
        pass

    def IsCaptureLocal(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureLocal()
        
        Check whether or not the current capture is stored locally, or on a remote host.
        
        :return: ``True`` if a capture is local.
        :rtype: bool
        """
        pass

    def IsCaptureTemporary(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsCaptureTemporary()
        
        Check whether or not the current capture is considered temporary. Captures that were
        made by an application and then have not been explicitly saved anywhere are temporary and will be
        cleaned up on close (with a final prompt to save). Once they are save to disk, they are no longer
        temporary and treated like any other capture.
        
        :return: ``True`` if a capture is temporary.
        :rtype: bool
        """
        pass

    def IsResourceReplaced(self, id: ResourceId) -> bool: # real signature unknown; restored from __doc__
        """
        IsResourceReplaced(id)
        
        Determine if a resource has been replaced. See :meth:`RegisterReplacement`.
        
        :param renderdoc.ResourceId id: The id of the resource to check.
        :return: ``True`` if the resource has been replaced.
        :rtype: bool
        """
        pass

    def LoadCapture(self, captureFile: str, opts: ReplayOptions, origFilename: str, temporary: bool, local: bool): # real signature unknown; restored from __doc__
        """
        LoadCapture(captureFile, opts, origFilename, temporary, local)
        
        Open a capture file for replay.
        
        :param str captureFile: The actual path to the capture file.
        :param renderdoc.ReplayOptions opts: The options controlling how the capture should be replayed.
        :param str origFilename: The original filename, if the capture was copied remotely for replay.
        :param bool temporary: ``True`` if this is a temporary capture which should prompt the user for
          either save or delete on close.
        :param bool local: ``True`` if ``captureFile`` refers to a file on the local machine.
        """
        pass

    def MarkMessagesRead(self): # real signature unknown; restored from __doc__
        """
        MarkMessagesRead()
        
        Mark all messages as read, resets :meth:`UnreadMessageCount` to 0.
        """
        pass

    def OpenRGPProfile(self, filename: str) -> bool: # real signature unknown; restored from __doc__
        """
        OpenRGPProfile(filename)
        
        Sets the path to the RGP profile to use with :meth:`GetRGPInterop`, launches RGP and
        opens an interop connection. This function will block (with a progress dialog) until either an
        error is encountered or else the connection is successfully established.
        
        This could be newly created, or extracted from an embedded section in the RDC.
        
        The connection is automatically closed when the capture is closed. If OpenRGPProfile is called
        again, any previous connection will be closed.
        
        :param str filename: The filename of the extracted temporary RGP capture on disk.
        :return: Whether RGP launched successfully.
        :rtype: bool
        """
        pass

    def RaiseDockWindow(self, dockWindow: QWidget): # real signature unknown; restored from __doc__
        """
        RaiseDockWindow(dockWindow)
        
        Raises a window within its docking manager so it becomes the focus of wherever it is
        currently docked.
        
        :param QWidget dockWindow: The window to raise.
        """
        pass

    def RecompressCapture(self): # real signature unknown; restored from __doc__
        """
        RecompressCapture()
        
        Recompress the current capture as much as possible.
        """
        pass

    def RefreshStatus(self): # real signature unknown; restored from __doc__
        """
        RefreshStatus()
        
        Replay the capture to the current event again, to pick up any changes that might have
        been made.
        """
        pass

    def RegisterReplacement(self, arg2, to: ResourceId): # real signature unknown; restored from __doc__
        """
        RegisterReplacement(arg2, to)
        
        Register that a resource has replaced, so that the UI can be updated to reflect the
        change.
        
        This should be called at the same time as :meth:`ReplayController.ReplaceResource`.
        
        :param renderdoc.ResourceId from: The id of the resource being replaced.
        :param renderdoc.ResourceId to: The id of the resource replacing it.
        """
        pass

    def RemoveBookmark(self, eventId: int): # real signature unknown; restored from __doc__
        """
        RemoveBookmark(eventId)
        
        Remove a bookmark at a given eventId.
        
        If no bookmark exists, this function will do nothing.
        
        :param int eventId: The eventId of the bookmark to remove.
        """
        pass

    def RemoveCaptureViewer(self, viewer: CaptureViewer): # real signature unknown; restored from __doc__
        """
        RemoveCaptureViewer(viewer)
        
        Unregister an instance of :class:`CaptureViewer` from receiving notifications.
        
        :param CaptureViewer viewer: The viewer to unregister.
        """
        pass

    def RemoveDependentFiles(self): # real signature unknown; restored from __doc__
        """
        RemoveDependentFiles()
        
        Removes the dependent files storage from the capture i.e. shader debug files.
        
        The files will be still be considered to be referenced by the capture and could be re-embedded 
        by calling :meth:`EmbedDependentFiles`.
        
        .. warning::
          Will directly modify the capture file on disk.
        
        .. note::
          For remote replay the modifications are performed on the remote machine and copied back to the local host.
        """
        pass

    def Replay(self) -> ReplayManager: # real signature unknown; restored from __doc__
        """
        Replay()
        
        Retrieve the replay manager for access to the internal RenderDoc replay controller.
        
        :return: The current replay manager.
        :rtype: ReplayManager
        """
        pass

    def ResourceNameCacheID(self) -> int: # real signature unknown; restored from __doc__
        """
        ResourceNameCacheID()
        
        Returns an index that can be used to cache the results of resource naming.
        
        In some cases (e.g. formatting in widgets) there might be high frequency fetches to names without an
        easy way to force a refresh on a rename. Instead, the index here can be cached and compared each
        time to see if any names have changed.
        
        The index starts at 1, so initialising an internal cache to 0 will cause the first check to be
        considered out of date
        
        :return: An incrementing index that can be used as a quick check if any names have changed.
        :rtype: int
        """
        pass

    def SaveCaptureTo(self, captureFile: str) -> bool: # real signature unknown; restored from __doc__
        """
        SaveCaptureTo(captureFile)
        
        Saves the current capture file to a given path.
        
        If the capture was temporary, this save action means it is no longer temporary and will be treated
        like any other capture.
        
        Any modifications to the capture (see :meth:`GetCaptureModifications`) will be applied at the same
        time.
        
        :param str captureFile: The path to save the capture file to.
        :return: ``True`` if the save operation was successful.
        :rtype: bool
        """
        pass

    def SetBookmark(self, mark: EventBookmark): # real signature unknown; restored from __doc__
        """
        SetBookmark(mark)
        
        Set or update a bookmark.
        
        A bookmark will be added at the specified eventId, or if one already exists then the attached text
        will be replaced.
        
        :param EventBookmark mark: The bookmark to add.
        """
        pass

    def SetEventID(self, exclude: List[CaptureViewer], selectedEventId: int, eventId: int, force: bool=False): # real signature unknown; restored from __doc__
        """
        SetEventID(exclude, selectedEventId, eventId, force=False)
        SetEventID(exclude, selectedEventId, eventId)
        
        Move the current replay to a new event in the capture.
        
        :param List[CaptureViewer] exclude: A list of viewers to exclude from being notified of this change,
          to stop infinite recursion.
        :param int selectedEventId: The selected :data:`eventId <renderdoc.APIEvent.eventId>`. See
          :meth:`CaptureViewer.OnSelectedEventChanged` for more information.
        :param int eventId: The new current :data:`eventId <renderdoc.APIEvent.eventId>`. See
          :meth:`CaptureViewer.OnEventChanged` for more information.
        :param bool force: Optional parameter, if ``True`` then the replay will 'move' even if it is moving
          to the same :data:`eventId <renderdoc.APIEvent.eventId>` as it's currently on.
        """
        pass

    def SetNotes(self, key: str, contents: str): # real signature unknown; restored from __doc__
        """
        SetNotes(key, contents)
        
        Set the contents for a given notes field.
        
        See :meth:`GetNotes` for a list of possible common field keys.
        
        :param str key: The name of the notes field to set.
        :param str contents: The new contents to assign to that field.
        """
        pass

    def SetResourceCustomName(self, id: ResourceId, name: str): # real signature unknown; restored from __doc__
        """
        SetResourceCustomName(id, name)
        
        Set a custom name for a resource.
        
        This allows an override to the name returned by :meth:`GetResourceName`, most useful when there are
        no pre-existing debug names specified in the capture.
        
        To remove a custom name that has been set previously, specify the empty string as the name. Then the
        custom name will be removed, and instead :meth:`GetResourceName` will fall back to returning any
        name fetched from the capture.
        
        :param renderdoc.ResourceId id: The ID of the resource to name.
        :param str name: The name to provide, or an empty string to remove any previous custom name.
        """
        pass

    def ShowAnnotationViewer(self): # real signature unknown; restored from __doc__
        """
        ShowAnnotationViewer()
        
        Raise the current :class:`AnnotationViewer`, showing it in the default place if needed.
        """
        pass

    def ShowAPIInspector(self): # real signature unknown; restored from __doc__
        """
        ShowAPIInspector()
        
        Raise the current :class:`APIInspector`, showing it in the default place if needed.
        """
        pass

    def ShowCaptureDialog(self): # real signature unknown; restored from __doc__
        """
        ShowCaptureDialog()
        
        Raise the current :class:`CaptureDialog`, showing it in the default place if needed.
        """
        pass

    def ShowCommentView(self): # real signature unknown; restored from __doc__
        """
        ShowCommentView()
        
        Raise the current :class:`CommentView`, showing it in the default place if needed.
        """
        pass

    def ShowDebugMessageView(self): # real signature unknown; restored from __doc__
        """
        ShowDebugMessageView()
        
        Raise the current :class:`DebugMessageView`, showing it in the default place if needed.
        """
        pass

    def ShowDiagnosticLogView(self): # real signature unknown; restored from __doc__
        """
        ShowDiagnosticLogView()
        
        Raise the current :class:`DiagnosticLogView`, showing it in the default place if needed.
        """
        pass

    def ShowEventBrowser(self): # real signature unknown; restored from __doc__
        """
        ShowEventBrowser()
        
        Raise the current :class:`EventBrowser`, showing it in the default place if needed.
        """
        pass

    def ShowMeshPreview(self): # real signature unknown; restored from __doc__
        """
        ShowMeshPreview()
        
        Raise the current mesh previewing :class:`BufferViewer`, showing it in the default
        place if needed.
        """
        pass

    def ShowPerformanceCounterViewer(self): # real signature unknown; restored from __doc__
        """
        ShowPerformanceCounterViewer()
        
        Raise the current :class:`PerformanceCounterViewer`, showing it in the default place if needed.
        """
        pass

    def ShowPipelineViewer(self): # real signature unknown; restored from __doc__
        """
        ShowPipelineViewer()
        
        Raise the current :class:`PipelineStateViewer`, showing it in the default place if needed.
        """
        pass

    def ShowPythonShell(self): # real signature unknown; restored from __doc__
        """
        ShowPythonShell()
        
        Raise the current :class:`PythonShell`, showing it in the default place if needed.
        """
        pass

    def ShowResourceInspector(self): # real signature unknown; restored from __doc__
        """
        ShowResourceInspector()
        
        Raise the current :class:`ResourceInspector`, showing it in the default place if needed.
        """
        pass

    def ShowStatisticsViewer(self): # real signature unknown; restored from __doc__
        """
        ShowStatisticsViewer()
        
        Raise the current :class:`StatisticsViewer`, showing it in the default place if needed.
        """
        pass

    def ShowTextureViewer(self): # real signature unknown; restored from __doc__
        """
        ShowTextureViewer()
        
        Raise the current :class:`TextureViewer`, showing it in the default place if needed.
        """
        pass

    def ShowTimelineBar(self): # real signature unknown; restored from __doc__
        """
        ShowTimelineBar()
        
        Raise the current :class:`TimelineBar`, showing it in the default place if needed.
        """
        pass

    def TargetShaderEncodings(self) -> List[ShaderEncoding]: # real signature unknown; restored from __doc__
        """
        TargetShaderEncodings()
        
        Retrieve the list of :class:`~renderdoc.ShaderEncoding` that are available for
        building target shaders for the currently loaded capture. See
        :meth:`~renderdoc.ReplayController.BuildTargetShader`.
        
        :return: The available encodings.
        :rtype: List[renderdoc.ShaderEncoding]
        """
        pass

    def TempCaptureFilename(self, appname: str) -> str: # real signature unknown; restored from __doc__
        """
        TempCaptureFilename(appname)
        
        Retrieve the absolute path where a given temporary capture should be stored.
        data.
        
        :param str appname: The name of the application to use as part of the template.
        :return: The absolute path.
        :rtype: str
        """
        pass

    def UnreadMessageCount(self) -> int: # real signature unknown; restored from __doc__
        """
        UnreadMessageCount()
        
        Retrieve how many messages in :meth:`DebugMessages` are currently unread.
        
        :return: The number of unread messages.
        :rtype: int
        """
        pass

    def UnregisterReplacement(self, id: ResourceId): # real signature unknown; restored from __doc__
        """
        UnregisterReplacement(id)
        
        Register that a replacement has been removed, so that the UI can be updated to reflect
        the change.
        
        This should be called at the same time as :meth:`ReplayController.RemoveReplacement`.
        
        See :meth:`ReplaceResource`.
        
        :param renderdoc.ResourceId id: The id of the original resource that was previously replaced.
        """
        pass

    def ViewBuffer(self, byteOffset: int, byteSize: int, id: ResourceId, format: str) -> BufferViewer: # real signature unknown; restored from __doc__
        """
        ViewBuffer(byteOffset, byteSize, id, format)
        ViewBuffer(byteOffset, byteSize, id)
        
        Show a new :class:`BufferViewer` window, showing a read-only view of buffer data.
        
        :param int byteOffset: The offset in bytes to the start of the buffer data to show.
        :param int byteSize: The number of bytes in the buffer to show.
        :param renderdoc.ResourceId id: The ID of the buffer to fetch data from.
        :param str format: Optionally a HLSL/GLSL style formatting string.
        :return: The new :class:`BufferViewer` window opened, but not shown.
        :rtype: BufferViewer
        """
        pass

    def ViewConstantBuffer(self, stage: ShaderStage, slot: int, idx: int) -> BufferViewer: # real signature unknown; restored from __doc__
        """
        ViewConstantBuffer(stage, slot, idx)
        
        Show a new :class:`BufferViewer` window, showing a read-only view of a the
        variables in a constant buffer with their values.
        
        :param renderdoc.ShaderStage stage: The stage that the constant buffer is bound to.
        :param int slot: The index in the shader's constant buffer list to look up.
        :param int idx: For APIs that support arrayed resource binds, the index in the constant buffer
          array.
        :return: The new :class:`BufferViewer` window opened, but not shown.
        :rtype: BufferViewer
        """
        pass

    def ViewDescriptors(self, descriptors: List[Descriptor], samplerDescriptors: List[SamplerDescriptor]) -> DescriptorViewer: # real signature unknown; restored from __doc__
        """
        ViewDescriptors(descriptors, samplerDescriptors)
        
        Show a new :class:`DescriptorViewer` window, showing contents of an arbitrary list of
        descriptors.
        
        The descriptor lists should be in parallel, with identical sizes. If a non-sampler descriptor is
        to be displayed, the corresponding sampler descriptor should be uninitialised and vice-versa. If
        the lists are not the same length, only indices up to the minimum of the two lengths will be used.
        
        This function should not be used to view the entirety of a descriptor store - in that case the
        :func:`ViewDescriptorStore` function will be more efficient.
        
        :param List[renderdoc.Descriptor] descriptors: The list of descriptors to process and show.
        :param List[renderdoc.SamplerDescriptor] samplerDescriptors: The list of sampler descriptors to process and
          show.
        :return: The new :class:`DescriptorViewer` window opened, but not shown.
        :rtype: DescriptorViewer
        """
        pass

    def ViewDescriptorStore(self, id: ResourceId) -> DescriptorViewer: # real signature unknown; restored from __doc__
        """
        ViewDescriptorStore(id)
        
        Show a new :class:`DescriptorViewer` window, showing the full raw contents of a
        descriptor store.
        
        :param renderdoc.ResourceId id: The ID of the descriptor store to fetch data from.
        :return: The new :class:`DescriptorViewer` window opened, but not shown.
        :rtype: DescriptorViewer
        """
        pass

    def ViewPixelHistory(self, id: ResourceId, x: int, y: int, view: int, display: TextureDisplay) -> PixelHistoryView: # real signature unknown; restored from __doc__
        """
        ViewPixelHistory(id, x, y, view, display)
        
        Show a new :class:`PixelHistoryView` window, showing the results from a pixel history
        operation.
        
        :param renderdoc.ResourceId id: The ID of the texture to show the history of.
        :param int x: The x co-ordinate of the pixel to search for.
        :param int y: The y co-ordinate of the pixel to search for.
        :param int view: The layered or multiview rendering view index of the pixel to search for.
        :param renderdoc.TextureDisplay display: The texture display configuration to use when looking up
          the history.
        :return: The new :class:`PixelHistoryView` window opened, but not shown.
        :rtype: PixelHistoryView
        """
        pass

    def ViewShader(self, shader: ShaderReflection, pipeline: ResourceId) -> ShaderViewer: # real signature unknown; restored from __doc__
        """
        ViewShader(shader, pipeline)
        
        Show a new :class:`ShaderViewer` window, showing a read-only view of a given shader.
        
        :param renderdoc.ShaderReflection shader: The reflection data for the shader to view.
        :param renderdoc.ResourceId pipeline: The pipeline state object, if applicable, that this shader is
          bound to.
        :return: The new :class:`ShaderViewer` window opened, but not shown.
        :rtype: ShaderViewer
        """
        pass

    def ViewShaderMessages(self, stages: ShaderStageMask) -> ShaderMessageViewer: # real signature unknown; restored from __doc__
        """
        ViewShaderMessages(stages)
        
        Show a new :class:`ShaderMessageViewer` window, showing the current event's messages.
        
        :param renderdoc.ShaderStageMask stages: The initial stages being viewed.
        :return: The new :class:`ShaderMessageViewer` window opened, but not shown.
        :rtype: ShaderMessageViewer
        """
        pass

    def ViewTextureAsBuffer(self, id: ResourceId, sub: Subresource, format: str) -> BufferViewer: # real signature unknown; restored from __doc__
        """
        ViewTextureAsBuffer(id, sub, format)
        ViewTextureAsBuffer(id, sub)
        
        Show a new :class:`BufferViewer` window, showing a read-only view of a texture's raw
        bytes.
        
        :param renderdoc.ResourceId id: The ID of the texture itself.
        :param renderdoc.Subresource sub: The subresource within this texture to use.
        :param str format: Optionally a HLSL/GLSL style formatting string.
        :return: The new :class:`BufferViewer` window opened, but not shown.
        :rtype: BufferViewer
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50143A20>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.CaptureContext' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.CaptureContext' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.CaptureContext' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.CaptureContext' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.CaptureContext' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.CaptureContext' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.CaptureContext' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.CaptureContext' objects>, 'TempCaptureFilename': <method 'TempCaptureFilename' of 'qrenderdoc.CaptureContext' objects>, 'LoadCapture': <method 'LoadCapture' of 'qrenderdoc.CaptureContext' objects>, 'SaveCaptureTo': <method 'SaveCaptureTo' of 'qrenderdoc.CaptureContext' objects>, 'RecompressCapture': <method 'RecompressCapture' of 'qrenderdoc.CaptureContext' objects>, 'CloseCapture': <method 'CloseCapture' of 'qrenderdoc.CaptureContext' objects>, 'ImportCapture': <method 'ImportCapture' of 'qrenderdoc.CaptureContext' objects>, 'ExportCapture': <method 'ExportCapture' of 'qrenderdoc.CaptureContext' objects>, 'SetEventID': <method 'SetEventID' of 'qrenderdoc.CaptureContext' objects>, 'RefreshStatus': <method 'RefreshStatus' of 'qrenderdoc.CaptureContext' objects>, 'IsResourceReplaced': <method 'IsResourceReplaced' of 'qrenderdoc.CaptureContext' objects>, 'GetResourceReplacement': <method 'GetResourceReplacement' of 'qrenderdoc.CaptureContext' objects>, 'RegisterReplacement': <method 'RegisterReplacement' of 'qrenderdoc.CaptureContext' objects>, 'UnregisterReplacement': <method 'UnregisterReplacement' of 'qrenderdoc.CaptureContext' objects>, 'AddCaptureViewer': <method 'AddCaptureViewer' of 'qrenderdoc.CaptureContext' objects>, 'RemoveCaptureViewer': <method 'RemoveCaptureViewer' of 'qrenderdoc.CaptureContext' objects>, 'Replay': <method 'Replay' of 'qrenderdoc.CaptureContext' objects>, 'ConnectToRemoteServer': <method 'ConnectToRemoteServer' of 'qrenderdoc.CaptureContext' objects>, 'IsCaptureLoaded': <method 'IsCaptureLoaded' of 'qrenderdoc.CaptureContext' objects>, 'IsCaptureLocal': <method 'IsCaptureLocal' of 'qrenderdoc.CaptureContext' objects>, 'IsCaptureTemporary': <method 'IsCaptureTemporary' of 'qrenderdoc.CaptureContext' objects>, 'IsCaptureLoading': <method 'IsCaptureLoading' of 'qrenderdoc.CaptureContext' objects>, 'GetFatalError': <method 'GetFatalError' of 'qrenderdoc.CaptureContext' objects>, 'GetCaptureFilename': <method 'GetCaptureFilename' of 'qrenderdoc.CaptureContext' objects>, 'GetCaptureModifications': <method 'GetCaptureModifications' of 'qrenderdoc.CaptureContext' objects>, 'FrameInfo': <method 'FrameInfo' of 'qrenderdoc.CaptureContext' objects>, 'APIProps': <method 'APIProps' of 'qrenderdoc.CaptureContext' objects>, 'TargetShaderEncodings': <method 'TargetShaderEncodings' of 'qrenderdoc.CaptureContext' objects>, 'CustomShaderEncodings': <method 'CustomShaderEncodings' of 'qrenderdoc.CaptureContext' objects>, 'CustomShaderSourcePrefixes': <method 'CustomShaderSourcePrefixes' of 'qrenderdoc.CaptureContext' objects>, 'CurSelectedEvent': <method 'CurSelectedEvent' of 'qrenderdoc.CaptureContext' objects>, 'CurEvent': <method 'CurEvent' of 'qrenderdoc.CaptureContext' objects>, 'CurSelectedAction': <method 'CurSelectedAction' of 'qrenderdoc.CaptureContext' objects>, 'CurAction': <method 'CurAction' of 'qrenderdoc.CaptureContext' objects>, 'GetFirstAction': <method 'GetFirstAction' of 'qrenderdoc.CaptureContext' objects>, 'GetLastAction': <method 'GetLastAction' of 'qrenderdoc.CaptureContext' objects>, 'CurRootActions': <method 'CurRootActions' of 'qrenderdoc.CaptureContext' objects>, 'GetResource': <method 'GetResource' of 'qrenderdoc.CaptureContext' objects>, 'GetResources': <method 'GetResources' of 'qrenderdoc.CaptureContext' objects>, 'GetResourceName': <method 'GetResourceName' of 'qrenderdoc.CaptureContext' objects>, 'GetResourceNameUnsuffixed': <method 'GetResourceNameUnsuffixed' of 'qrenderdoc.CaptureContext' objects>, 'IsAutogeneratedName': <method 'IsAutogeneratedName' of 'qrenderdoc.CaptureContext' objects>, 'HasResourceCustomName': <method 'HasResourceCustomName' of 'qrenderdoc.CaptureContext' objects>, 'SetResourceCustomName': <method 'SetResourceCustomName' of 'qrenderdoc.CaptureContext' objects>, 'ResourceNameCacheID': <method 'ResourceNameCacheID' of 'qrenderdoc.CaptureContext' objects>, 'GetTexture': <method 'GetTexture' of 'qrenderdoc.CaptureContext' objects>, 'GetTextures': <method 'GetTextures' of 'qrenderdoc.CaptureContext' objects>, 'GetBuffer': <method 'GetBuffer' of 'qrenderdoc.CaptureContext' objects>, 'GetBuffers': <method 'GetBuffers' of 'qrenderdoc.CaptureContext' objects>, 'GetDescriptorStore': <method 'GetDescriptorStore' of 'qrenderdoc.CaptureContext' objects>, 'GetAction': <method 'GetAction' of 'qrenderdoc.CaptureContext' objects>, 'OpenRGPProfile': <method 'OpenRGPProfile' of 'qrenderdoc.CaptureContext' objects>, 'ClearReplayCache': <method 'ClearReplayCache' of 'qrenderdoc.CaptureContext' objects>, 'GetRGPInterop': <method 'GetRGPInterop' of 'qrenderdoc.CaptureContext' objects>, 'GetStructuredFile': <method 'GetStructuredFile' of 'qrenderdoc.CaptureContext' objects>, 'CurWindowingSystem': <method 'CurWindowingSystem' of 'qrenderdoc.CaptureContext' objects>, 'CreateWindowingData': <method 'CreateWindowingData' of 'qrenderdoc.CaptureContext' objects>, 'DebugMessages': <method 'DebugMessages' of 'qrenderdoc.CaptureContext' objects>, 'UnreadMessageCount': <method 'UnreadMessageCount' of 'qrenderdoc.CaptureContext' objects>, 'MarkMessagesRead': <method 'MarkMessagesRead' of 'qrenderdoc.CaptureContext' objects>, 'AddMessages': <method 'AddMessages' of 'qrenderdoc.CaptureContext' objects>, 'ClearMessages': <method 'ClearMessages' of 'qrenderdoc.CaptureContext' objects>, 'GetNotes': <method 'GetNotes' of 'qrenderdoc.CaptureContext' objects>, 'SetNotes': <method 'SetNotes' of 'qrenderdoc.CaptureContext' objects>, 'GetBookmarks': <method 'GetBookmarks' of 'qrenderdoc.CaptureContext' objects>, 'SetBookmark': <method 'SetBookmark' of 'qrenderdoc.CaptureContext' objects>, 'RemoveBookmark': <method 'RemoveBookmark' of 'qrenderdoc.CaptureContext' objects>, 'EmbedDependentFiles': <method 'EmbedDependentFiles' of 'qrenderdoc.CaptureContext' objects>, 'RemoveDependentFiles': <method 'RemoveDependentFiles' of 'qrenderdoc.CaptureContext' objects>, 'DelayedCallback': <method 'DelayedCallback' of 'qrenderdoc.CaptureContext' objects>, 'GetMainWindow': <method 'GetMainWindow' of 'qrenderdoc.CaptureContext' objects>, 'GetEventBrowser': <method 'GetEventBrowser' of 'qrenderdoc.CaptureContext' objects>, 'GetAPIInspector': <method 'GetAPIInspector' of 'qrenderdoc.CaptureContext' objects>, 'GetAnnotationViewer': <method 'GetAnnotationViewer' of 'qrenderdoc.CaptureContext' objects>, 'GetTextureViewer': <method 'GetTextureViewer' of 'qrenderdoc.CaptureContext' objects>, 'GetMeshPreview': <method 'GetMeshPreview' of 'qrenderdoc.CaptureContext' objects>, 'GetPipelineViewer': <method 'GetPipelineViewer' of 'qrenderdoc.CaptureContext' objects>, 'GetCaptureDialog': <method 'GetCaptureDialog' of 'qrenderdoc.CaptureContext' objects>, 'GetDebugMessageView': <method 'GetDebugMessageView' of 'qrenderdoc.CaptureContext' objects>, 'GetDiagnosticLogView': <method 'GetDiagnosticLogView' of 'qrenderdoc.CaptureContext' objects>, 'GetCommentView': <method 'GetCommentView' of 'qrenderdoc.CaptureContext' objects>, 'GetPerformanceCounterViewer': <method 'GetPerformanceCounterViewer' of 'qrenderdoc.CaptureContext' objects>, 'GetStatisticsViewer': <method 'GetStatisticsViewer' of 'qrenderdoc.CaptureContext' objects>, 'GetTimelineBar': <method 'GetTimelineBar' of 'qrenderdoc.CaptureContext' objects>, 'GetPythonShell': <method 'GetPythonShell' of 'qrenderdoc.CaptureContext' objects>, 'GetResourceInspector': <method 'GetResourceInspector' of 'qrenderdoc.CaptureContext' objects>, 'HasEventBrowser': <method 'HasEventBrowser' of 'qrenderdoc.CaptureContext' objects>, 'HasAPIInspector': <method 'HasAPIInspector' of 'qrenderdoc.CaptureContext' objects>, 'HasAnnotationViewer': <method 'HasAnnotationViewer' of 'qrenderdoc.CaptureContext' objects>, 'HasTextureViewer': <method 'HasTextureViewer' of 'qrenderdoc.CaptureContext' objects>, 'HasPipelineViewer': <method 'HasPipelineViewer' of 'qrenderdoc.CaptureContext' objects>, 'HasMeshPreview': <method 'HasMeshPreview' of 'qrenderdoc.CaptureContext' objects>, 'HasCaptureDialog': <method 'HasCaptureDialog' of 'qrenderdoc.CaptureContext' objects>, 'HasDebugMessageView': <method 'HasDebugMessageView' of 'qrenderdoc.CaptureContext' objects>, 'HasDiagnosticLogView': <method 'HasDiagnosticLogView' of 'qrenderdoc.CaptureContext' objects>, 'HasCommentView': <method 'HasCommentView' of 'qrenderdoc.CaptureContext' objects>, 'HasPerformanceCounterViewer': <method 'HasPerformanceCounterViewer' of 'qrenderdoc.CaptureContext' objects>, 'HasStatisticsViewer': <method 'HasStatisticsViewer' of 'qrenderdoc.CaptureContext' objects>, 'HasTimelineBar': <method 'HasTimelineBar' of 'qrenderdoc.CaptureContext' objects>, 'HasPythonShell': <method 'HasPythonShell' of 'qrenderdoc.CaptureContext' objects>, 'HasResourceInspector': <method 'HasResourceInspector' of 'qrenderdoc.CaptureContext' objects>, 'ShowEventBrowser': <method 'ShowEventBrowser' of 'qrenderdoc.CaptureContext' objects>, 'ShowAPIInspector': <method 'ShowAPIInspector' of 'qrenderdoc.CaptureContext' objects>, 'ShowAnnotationViewer': <method 'ShowAnnotationViewer' of 'qrenderdoc.CaptureContext' objects>, 'ShowTextureViewer': <method 'ShowTextureViewer' of 'qrenderdoc.CaptureContext' objects>, 'ShowMeshPreview': <method 'ShowMeshPreview' of 'qrenderdoc.CaptureContext' objects>, 'ShowPipelineViewer': <method 'ShowPipelineViewer' of 'qrenderdoc.CaptureContext' objects>, 'ShowCaptureDialog': <method 'ShowCaptureDialog' of 'qrenderdoc.CaptureContext' objects>, 'ShowDebugMessageView': <method 'ShowDebugMessageView' of 'qrenderdoc.CaptureContext' objects>, 'ShowDiagnosticLogView': <method 'ShowDiagnosticLogView' of 'qrenderdoc.CaptureContext' objects>, 'ShowCommentView': <method 'ShowCommentView' of 'qrenderdoc.CaptureContext' objects>, 'ShowPerformanceCounterViewer': <method 'ShowPerformanceCounterViewer' of 'qrenderdoc.CaptureContext' objects>, 'ShowStatisticsViewer': <method 'ShowStatisticsViewer' of 'qrenderdoc.CaptureContext' objects>, 'ShowTimelineBar': <method 'ShowTimelineBar' of 'qrenderdoc.CaptureContext' objects>, 'ShowPythonShell': <method 'ShowPythonShell' of 'qrenderdoc.CaptureContext' objects>, 'ShowResourceInspector': <method 'ShowResourceInspector' of 'qrenderdoc.CaptureContext' objects>, 'EditShader': <method 'EditShader' of 'qrenderdoc.CaptureContext' objects>, 'DebugShader': <method 'DebugShader' of 'qrenderdoc.CaptureContext' objects>, 'ViewShader': <method 'ViewShader' of 'qrenderdoc.CaptureContext' objects>, 'ViewShaderMessages': <method 'ViewShaderMessages' of 'qrenderdoc.CaptureContext' objects>, 'ViewDescriptorStore': <method 'ViewDescriptorStore' of 'qrenderdoc.CaptureContext' objects>, 'ViewDescriptors': <method 'ViewDescriptors' of 'qrenderdoc.CaptureContext' objects>, 'ViewBuffer': <method 'ViewBuffer' of 'qrenderdoc.CaptureContext' objects>, 'ViewTextureAsBuffer': <method 'ViewTextureAsBuffer' of 'qrenderdoc.CaptureContext' objects>, 'ViewConstantBuffer': <method 'ViewConstantBuffer' of 'qrenderdoc.CaptureContext' objects>, 'ViewPixelHistory': <method 'ViewPixelHistory' of 'qrenderdoc.CaptureContext' objects>, 'CreateBuiltinWindow': <method 'CreateBuiltinWindow' of 'qrenderdoc.CaptureContext' objects>, 'BuiltinWindowClosed': <method 'BuiltinWindowClosed' of 'qrenderdoc.CaptureContext' objects>, 'RaiseDockWindow': <method 'RaiseDockWindow' of 'qrenderdoc.CaptureContext' objects>, 'AddDockWindow': <method 'AddDockWindow' of 'qrenderdoc.CaptureContext' objects>, 'CurD3D11PipelineState': <method 'CurD3D11PipelineState' of 'qrenderdoc.CaptureContext' objects>, 'CurD3D12PipelineState': <method 'CurD3D12PipelineState' of 'qrenderdoc.CaptureContext' objects>, 'CurGLPipelineState': <method 'CurGLPipelineState' of 'qrenderdoc.CaptureContext' objects>, 'CurVulkanPipelineState': <method 'CurVulkanPipelineState' of 'qrenderdoc.CaptureContext' objects>, 'CurPipelineState': <method 'CurPipelineState' of 'qrenderdoc.CaptureContext' objects>, 'Config': <method 'Config' of 'qrenderdoc.CaptureContext' objects>, 'Extensions': <method 'Extensions' of 'qrenderdoc.CaptureContext' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.CaptureContext' objects>, '__doc__': 'The capture context that the python script is running in.'})"


