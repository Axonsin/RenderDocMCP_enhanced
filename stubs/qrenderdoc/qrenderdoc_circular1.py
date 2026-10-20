from ._APIInspector import APIInspector
from ._AnnotationViewer import AnnotationViewer
from ._BufferViewer import BufferViewer
from ._CaptureDialog import CaptureDialog
from ._CaptureModifications import CaptureModifications
from ._CaptureViewer import CaptureViewer
from ._CommentView import CommentView
from ._DebugMessageView import DebugMessageView
from ._DescriptorViewer import DescriptorViewer
from ._DiagnosticLogView import DiagnosticLogView
from ._DockReference import DockReference
from ._EventBookmark import EventBookmark
from ._MainWindow import MainWindow
from ._PerformanceCounterViewer import PerformanceCounterViewer
from ._PersistentConfig import PersistentConfig
from ._PipelineStateViewer import PipelineStateViewer
from ._PixelHistoryView import PixelHistoryView
from ._PythonShell import PythonShell
from ._RGPInterop import RGPInterop
from ._RemoteHost import RemoteHost
from ._ReplayManager import ReplayManager
from ._ResourceInspector import ResourceInspector
from ._ShaderMessageViewer import ShaderMessageViewer
from ._ShaderViewer import ShaderViewer
from ._StatisticsViewer import StatisticsViewer
from ._TextureViewer import TextureViewer
from ._TimelineBar import TimelineBar
from renderdoc import APIProperties, ActionDescription, BufferDescription, CaptureFileFormat, D3D11State, D3D12State, DebugMessage, Descriptor, DescriptorStoreDescription, FrameDescription, GLState, KnownShaderTool, PipeState, ReplayController, ReplayOptions, ResourceDescription, ResourceId, ResultDetails, SDFile, SamplerDescriptor, ShaderCompileFlags, ShaderDebugTrace, ShaderEncoding, ShaderReflection, ShaderSourcePrefix, ShaderStage, ShaderStageMask, Subresource, TextureDescription, TextureDisplay, VKState, WindowingData, WindowingSystem
from typing import Callable, List, Tuple

# Dummy types
from . import QWidget

class CaptureContext():
    # Original docstring
    """
    The capture context that the python script is running in.
    
    Available as a ``pyrenderdoc`` global variable in any python scripts run from RenderDoc's UI.
    """
    
    
    
    def TempCaptureFilename(self, appname: str) -> str:
        """
        Retrieve the absolute path where a given temporary capture should be stored.
        data.
        
        :param str appname: The name of the application to use as part of the template.
        :return: The absolute path.
        :rtype: str
        """
        pass
    
    
    def LoadCapture(self, captureFile: str, opts: ReplayOptions, origFilename: str, temporary: bool, local: bool):
        """
        Open a capture file for replay.
        
        :param str captureFile: The actual path to the capture file.
        :param renderdoc.ReplayOptions opts: The options controlling how the capture should be replayed.
        :param str origFilename: The original filename, if the capture was copied remotely for replay.
        :param bool temporary: ``True`` if this is a temporary capture which should prompt the user for
          either save or delete on close.
        :param bool local: ``True`` if ``captureFile`` refers to a file on the local machine.
        """
        pass
    
    
    def SaveCaptureTo(self, captureFile: str) -> bool:
        """
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
    
    
    def RecompressCapture(self):
        """
        Recompress the current capture as much as possible.
        """
        pass
    
    
    def CloseCapture(self):
        """
        Close the currently open capture file.
        """
        pass
    
    
    def GetBlockingController(self) -> ReplayController:
        """
        Returns a blocking version of :class:`renderdoc.ReplayController`, which provides the
        same interface but will block for all calls and run them on the correct replay thread. This is
        provided only as a convenience to avoid calling :meth:`Replay` to obtain the
        :class:`ReplayManager` and use that to directly invoke asynchronously or synchronously onto the
        replay thread.
        
        This function will return ``None`` if no :class:`renderdoc.ReplayController` is available, for
        example if there is no capture loaded.
        
        The returned object *must not* be used if the capture is closed for any reason. It is strongly
        recommended that you do not cache this object and use it only in local areas of code when needed.
        
        .. warning::
          Care should be taken to ensure that this object is not confused with any other controller that is
          non-blocking.
        
        :return: A blocking version of the :class:`renderdoc.ReplayController`.
        :rtype: renderdoc.ReplayController
        """
        pass
    
    
    def ImportCapture(self, fmt: CaptureFileFormat, importfile: str, rdcfile: str) -> bool:
        """
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
    
    
    def ExportCapture(self, fmt: CaptureFileFormat, exportfile: str):
        """
        Exports the current capture file to a given path with a specified capture file format.
        
        The capture must be available locally, if it's not this function will fail.
        
        :param renderdoc.CaptureFileFormat fmt: The capture file format to export to.
        :param str exportfile: The path to export the capture file to.
        """
        pass
    
    
    def SetEventID(self, exclude: List[CaptureViewer], selectedEventId: int, eventId: int, force: bool = False):
        """
        Move the current replay to a new event in the capture.
        
        :param List[CaptureViewer] exclude: A list of viewers to exclude from being notified of this change,
          to stop infinite recursion.
        :param int selectedEventId: The selected :data:`eventId <renderdoc.APIEvent.eventId>`. See
          :meth:`CaptureViewer.OnSelectedEventChanged` for more information.
        :param int eventId: The new current :data:`eventId <renderdoc.APIEvent.eventId>`. See
          :meth:`CaptureViewer.OnEventChanged` for more information.
        :param bool force=False: **Optional parameter**. if ``True`` then the replay will 'move' even if it is moving
          to the same :data:`eventId <renderdoc.APIEvent.eventId>` as it's currently on.
        """
        pass
    
    
    def RefreshStatus(self):
        """
        Replay the capture to the current event again, to pick up any changes that might have
        been made.
        """
        pass
    
    
    def IsResourceReplaced(self, id: ResourceId) -> bool:
        """
        Determine if a resource has been replaced. See :meth:`RegisterReplacement`.
        
        :param renderdoc.ResourceId id: The id of the resource to check.
        :return: ``True`` if the resource has been replaced.
        :rtype: bool
        """
        pass
    
    
    def GetResourceReplacement(self, id: ResourceId) -> ResourceId:
        """
        Return the id of a replacement for the given resource. See
        :meth:`RegisterReplacement` and :meth:`IsResourceReplaced`.
        
        :param renderdoc.ResourceId id: The id of the resource to check.
        :return: The replacement id, or a null id if the resource hasn't been replaced
        :rtype: renderdoc.ResourceId
        """
        pass
    
    
    def RegisterReplacement(self, from_: ResourceId, to: ResourceId):
        """
        Register that a resource has replaced, so that the UI can be updated to reflect the
        change.
        
        This should be called at the same time as :meth:`~renderdoc.ReplayController.ReplaceResource`.
        
        :param renderdoc.ResourceId from: The id of the resource being replaced.
        :param renderdoc.ResourceId to: The id of the resource replacing it.
        """
        pass
    
    
    def UnregisterReplacement(self, id: ResourceId):
        """
        Register that a replacement has been removed, so that the UI can be updated to reflect
        the change.
        
        This should be called at the same time as :meth:`~renderdoc.ReplayController.RemoveReplacement`.
        
        See :meth:`RegisterReplacement`.
        
        :param renderdoc.ResourceId id: The id of the original resource that was previously replaced.
        """
        pass
    
    
    def AddCaptureViewer(self, viewer: CaptureViewer):
        """
        Register a new instance of :class:`CaptureViewer` to receive capture event notifications.
        
        :param CaptureViewer viewer: The viewer to register.
        """
        pass
    
    
    def RemoveCaptureViewer(self, viewer: CaptureViewer):
        """
        Unregister an instance of :class:`CaptureViewer` from receiving notifications.
        
        :param CaptureViewer viewer: The viewer to unregister.
        """
        pass
    
    
    def Replay(self) -> ReplayManager:
        """
        Retrieve the replay manager for access to the internal RenderDoc replay controller.
        
        :return: The current replay manager.
        :rtype: ReplayManager
        """
        pass
    
    
    def ConnectToRemoteServer(self, host: RemoteHost):
        """
        Connect to a remote server.
        
        :param RemoteHost host: The host to connect to.
        """
        pass
    
    
    def IsCaptureLoaded(self) -> bool:
        """
        Check whether or not a capture is currently loaded.
        
        :return: ``True`` if a capture is loaded.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureLocal(self) -> bool:
        """
        Check whether or not the current capture is stored locally, or on a remote host.
        
        :return: ``True`` if a capture is local.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureTemporary(self) -> bool:
        """
        Check whether or not the current capture is considered temporary. Captures that were
        made by an application and then have not been explicitly saved anywhere are temporary and will be
        cleaned up on close (with a final prompt to save). Once they are save to disk, they are no longer
        temporary and treated like any other capture.
        
        :return: ``True`` if a capture is temporary.
        :rtype: bool
        """
        pass
    
    
    def IsCaptureLoading(self) -> bool:
        """
        Check whether or not a capture is currently loading in-progress.
        
        :return: ``True`` if a capture is currently loading.
        :rtype: bool
        """
        pass
    
    
    def GetFatalError(self) -> ResultDetails:
        """
        If a capture is loaded, return the current fatal error status.
        
        :return: If a capture is currently loaded, return the fatal error status.
        :rtype: renderdoc.ResultDetails
        """
        pass
    
    
    def GetCaptureFilename(self) -> str:
        """
        Retrieve the filename for the currently loaded capture.
        
        :return: The filename of the current capture.
        :rtype: str
        """
        pass
    
    
    def GetCaptureModifications(self) -> CaptureModifications:
        """
        Get a bitmask indicating which modifications (if any) have been made to the capture in
        the UI which aren't reflected in the capture file on disk.
        
        :return: The modifications (if any) that have been made to the capture.
        :rtype: CaptureModifications
        """
        pass
    
    
    def FrameInfo(self) -> FrameDescription:
        """
        Retrieve the :class:`~renderdoc.FrameDescription` for the currently loaded capture.
        
        :return: The frame information.
        :rtype: renderdoc.FrameDescription
        """
        pass
    
    
    def APIProps(self) -> APIProperties:
        """
        Retrieve the :class:`~renderdoc.APIProperties` for the currently loaded capture.
        
        :return: The API properties.
        :rtype: renderdoc.APIProperties
        """
        pass
    
    
    def TargetShaderEncodings(self) -> List[ShaderEncoding]:
        """
        Retrieve the list of :class:`~renderdoc.ShaderEncoding` that are available for
        building target shaders for the currently loaded capture. See
        :meth:`~renderdoc.ReplayController.BuildTargetShader`.
        
        :return: The available encodings.
        :rtype: List[renderdoc.ShaderEncoding]
        """
        pass
    
    
    def CustomShaderEncodings(self) -> List[ShaderEncoding]:
        """
        Retrieve the list of :class:`~renderdoc.ShaderEncoding` that are available for
        building custom shaders for the currently loaded capture. See
        :meth:`~renderdoc.ReplayController.BuildCustomShader`.
        
        :return: The available encodings.
        :rtype: List[renderdoc.ShaderEncoding]
        """
        pass
    
    
    def CustomShaderSourcePrefixes(self) -> List[ShaderSourcePrefix]:
        """
        Retrieve the list of prefixes for each :class:`~renderdoc.ShaderEncoding` that should
        be added to custom compiled shaders. See
        :meth:`~renderdoc.ReplayController.GetCustomShaderSourcePrefixes`.
        
        :return: A list of pairs, listing a prefix for each shader encoding referenced.
        :rtype: List[renderdoc.ShaderSourcePrefix]
        """
        pass
    
    
    def CurSelectedEvent(self) -> int:
        """
        Retrieve the currently selected :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        In most cases, prefer using :meth:`CurEvent`. See :meth:`CaptureViewer.OnSelectedEventChanged` for more
        information for how this differs.
        
        :return: The current selected event.
        :rtype: int
        """
        pass
    
    
    def CurEvent(self) -> int:
        """
        Retrieve the current :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        :return: The current event.
        :rtype: int
        """
        pass
    
    
    def CurSelectedAction(self) -> ActionDescription:
        """
        Retrieve the currently selected action.
        
        In most cases, prefer using :meth:`CurAction`. See :meth:`CaptureViewer.OnSelectedEventChanged` for
        more information for how this differs.
        
        :return: The currently selected action.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def CurAction(self) -> ActionDescription:
        """
        Retrieve the current action.
        
        :return: The current action, or ``None`` if no action is selected.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def GetFirstAction(self) -> ActionDescription:
        """
        Retrieve the first action in the capture.
        
        :return: The first action.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def GetLastAction(self) -> ActionDescription:
        """
        Retrieve the last action in the capture.
        
        :return: The last action.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def CurRootActions(self) -> List[ActionDescription]:
        """
        Retrieve the root list of actions in the current capture.
        
        :return: The root actions.
        :rtype: List[renderdoc.ActionDescription]
        """
        pass
    
    
    def GetResource(self, id: ResourceId) -> ResourceDescription:
        """
        Retrieve the information about a particular resource.
        
        :param renderdoc.ResourceId id: The ID of the resource to query about.
        :return: The information about a resource, or ``None`` if the ID does not correspond to a resource.
        :rtype: renderdoc.ResourceDescription
        """
        pass
    
    
    def GetResources(self) -> List[ResourceDescription]:
        """
        Retrieve the list of resources in the current capture.
        
        :return: The list of resources.
        :rtype: List[renderdoc.ResourceDescription]
        """
        pass
    
    
    def GetResourceName(self, id: ResourceId) -> str:
        """
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
    
    
    def GetResourceNameUnsuffixed(self, id: ResourceId) -> str:
        """
        Returns the same name as :meth:`GetResourceName` but without any added suffix, e.g. to
        indicate the resource's status such as (Edited).
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: The unsuffixed resource name.
        :rtype: str
        """
        pass
    
    
    def IsAutogeneratedName(self, id: ResourceId) -> bool:
        """
        Determines whether the name for the given resource has been customised at all, either
        during capture time or with :meth:`SetResourceCustomName`.
        
        If not, the name is just auto-generated based on the ID and resource type, so depending on
        circumstance it may be preferable to omit the name.
        
        :param renderdoc.ResourceId id: The ID of the resource to query.
        :return: Whether the name for the resource has just been auto-generated.
        :rtype: bool
        """
        pass
    
    
    def HasResourceCustomName(self, id: ResourceId) -> bool:
        """
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
    
    
    def SetResourceCustomName(self, id: ResourceId, name: str):
        """
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
    
    
    def ResourceNameCacheID(self) -> int:
        """
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
    
    
    def GetTexture(self, id: ResourceId) -> TextureDescription:
        """
        Retrieve the information about a particular texture.
        
        :param renderdoc.ResourceId id: The ID of the texture to query about.
        :return: The information about a texture, or ``None`` if the ID does not correspond to a texture.
        :rtype: renderdoc.TextureDescription
        """
        pass
    
    
    def GetTextures(self) -> List[TextureDescription]:
        """
        Retrieve the list of textures in the current capture.
        
        :return: The list of textures.
        :rtype: List[renderdoc.TextureDescription]
        """
        pass
    
    
    def GetBuffer(self, id: ResourceId) -> BufferDescription:
        """
        Retrieve the information about a particular buffer.
        
        :param renderdoc.ResourceId id: The ID of the buffer to query about.
        :return: The information about a buffer, or ``None`` if the ID does not correspond to a buffer.
        :rtype: renderdoc.BufferDescription
        """
        pass
    
    
    def GetBuffers(self) -> List[BufferDescription]:
        """
        Retrieve the list of buffers in the current capture.
        
        :return: The list of buffers.
        :rtype: List[renderdoc.BufferDescription]
        """
        pass
    
    
    def GetDescriptorStore(self, id: ResourceId) -> DescriptorStoreDescription:
        """
        Retrieve the information about a particular descriptor store.
        
        :param renderdoc.ResourceId id: The ID of the buffer to query about.
        :return: The information about a descriptor store, or ``None`` if the ID does not correspond to a
          descriptor store.
        :rtype: renderdoc.DescriptorStoreDescription
        """
        pass
    
    
    def GetAction(self, eventId: int) -> ActionDescription:
        """
        Retrieve the information about an action at a given
        :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: The information about the action, or ``None`` if the
          :data:`eventId <renderdoc.APIEvent.eventId>` doesn't correspond to an action.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def OpenRGPProfile(self, filename: str) -> bool:
        """
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
    
    
    def ClearReplayCache(self):
        """
        Clear any cached data from previous replays and ensure subsequent replays fully
        re-initialise any data, including e.g. bindless feedback, printf results or mesh output data.
        """
        pass
    
    
    def GetRGPInterop(self) -> RGPInterop:
        """
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
    
    
    def GetStructuredFile(self) -> SDFile:
        """
        Retrieve the :class:`~renderdoc.SDFile` for the currently open capture.
        
        :return: The structured file.
        :rtype: renderdoc.SDFile
        """
        pass
    
    
    def CurWindowingSystem(self) -> WindowingSystem:
        """
        Retrieve the current windowing system in use.
        
        :return: The active windowing system.
        :rtype: renderdoc.WindowingSystem
        """
        pass
    
    
    def CreateWindowingData(self, window: QWidget) -> WindowingData:
        """
        Create an opaque pointer suitable for passing to
        :meth:`~renderdoc.ReplayController.CreateOutput` or other functions that expect windowing data.
        
        .. note::
          This function must be called on the main UI thread.
        
        :param QWidget window: The window to create windowing data for.
        :return: The windowing data.
        :rtype: renderdoc.WindowingData
        """
        pass
    
    
    def DebugMessages(self) -> List[DebugMessage]:
        """
        Retrieve the current list of debug messages. This includes messages from the capture
        as well as messages generated during replay and analysis.
        
        :return: The debug messages generated to date.
        :rtype: List[renderdoc.DebugMessage]
        """
        pass
    
    
    def UnreadMessageCount(self) -> int:
        """
        Retrieve how many messages in :meth:`DebugMessages` are currently unread.
        
        :return: The number of unread messages.
        :rtype: int
        """
        pass
    
    
    def MarkMessagesRead(self):
        """
        Mark all messages as read, resets :meth:`UnreadMessageCount` to 0.
        """
        pass
    
    
    def AddMessages(self, msgs: List[DebugMessage]):
        """
        Add messages into the list returned by :meth:`DebugMessages`. Initially set to unread.
        
        :param List[renderdoc.DebugMessage] msgs: A list of debug messages to add.
        """
        pass
    
    
    def ClearMessages(self):
        """
        Clear the currently stored messages, and mark all as unread. This can be used in
        combination with :meth:`DebugMessages` and :meth:`AddMessages` to filter the current set of messages.
        """
        pass
    
    
    def GetNotes(self, key: str) -> str:
        """
        Retrieve the contents for a given notes field.
        
        Examples of fields are:
        
        * ``comments`` for generic comments to be displayed in a text field
        * ``hwinfo`` for a plaintext summary of the hardware and driver configuration of the system.
        
        :param str key: The name of the notes field to retrieve.
        :return: The contents, or an empty string if the field doesn't exist.
        :rtype: str
        """
        pass
    
    
    def SetNotes(self, key: str, contents: str):
        """
        Set the contents for a given notes field.
        
        See :meth:`GetNotes` for a list of possible common field keys.
        
        :param str key: The name of the notes field to set.
        :param str contents: The new contents to assign to that field.
        """
        pass
    
    
    def GetBookmarks(self) -> List[EventBookmark]:
        """
        Get the current list of bookmarks in the capture. Each bookmark is associated with an
        eventId and has some text attached. There will only be at most one bookmark for any given eventId.
        
        The list of bookmarks is not necessarily sorted by eventId. Thus, bookmark 1 is always bookmark 1
        until it is removed, the indices do not shift as new bookmarks are added or removed.
        
        :return: The currently set bookmarks.
        :rtype: List[EventBookmark]
        """
        pass
    
    
    def SetBookmark(self, mark: EventBookmark):
        """
        Set or update a bookmark.
        
        A bookmark will be added at the specified eventId, or if one already exists then the attached text
        will be replaced.
        
        :param EventBookmark mark: The bookmark to add.
        """
        pass
    
    
    def RemoveBookmark(self, eventId: int):
        """
        Remove a bookmark at a given eventId.
        
        If no bookmark exists, this function will do nothing.
        
        :param int eventId: The eventId of the bookmark to remove.
        """
        pass
    
    
    def EmbedDependentFiles(self):
        """
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
    
    
    def RemoveDependentFiles(self):
        """
        Removes the dependent files storage from the capture i.e. shader debug files.
        
        The files will be still be considered to be referenced by the capture and could be re-embedded
        by calling :meth:`EmbedDependentFiles`.
        
        .. warning::
          Will directly modify the capture file on disk.
        
        .. note::
          For remote replay the modifications are performed on the remote machine and copied back to the local host.
        """
        pass
    
    
    def InvokeOntoUIThread(self, callback: Callable[[], None]):
        """
        Invoke a callback on the UI thread. All widget accesses must come from the UI thread,
        so if work has been done on the render thread then this function can be used to asynchronously and
        safely go back to the UI thread.
        
        This function is safe to call on the UI thread, but it will synchronously call the callback
        immediately before returning.
        
        .. note::
          No parameters are provided to the callback, it is assumed that the callback will maintain its own
          context as needed.
        
        :param Callable[[], None] callback: The callback to invoke on the UI thread.
        """
        pass
    
    
    def DelayedCallback(self, milliseconds: int, callback: Callable[[], None]):
        """
        Registers a delayed callback to be called after a certain number of milliseconds
        on the UI thread.
        
        :param int milliseconds: The number of milliseconds (approximately) to wait before the callback.
        :param Callable[[], None] callback: The function to call
        """
        pass
    
    
    def GetMainWindow(self) -> MainWindow:
        """
        Retrieve the current singleton :class:`MainWindow`.
        
        :return: The current window.
        :rtype: MainWindow
        """
        pass
    
    
    def GetEventBrowser(self) -> 'EventBrowser':
        """
        Retrieve the current singleton :class:`EventBrowser`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: EventBrowser
        """
        pass
    
    
    def GetAPIInspector(self) -> APIInspector:
        """
        Retrieve the current singleton :class:`APIInspector`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: APIInspector
        """
        pass
    
    
    def GetAnnotationViewer(self) -> AnnotationViewer:
        """
        Retrieve the current singleton :class:`AnnotationViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: AnnotationViewer
        """
        pass
    
    
    def GetTextureViewer(self) -> TextureViewer:
        """
        Retrieve the current singleton :class:`TextureViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: TextureViewer
        """
        pass
    
    
    def GetMeshPreview(self) -> BufferViewer:
        """
        Retrieve the current singleton :class:`BufferViewer` configured for mesh viewing.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: BufferViewer
        """
        pass
    
    
    def GetPipelineViewer(self) -> PipelineStateViewer:
        """
        Retrieve the current singleton :class:`PipelineStateViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PipelineStateViewer
        """
        pass
    
    
    def GetCaptureDialog(self) -> CaptureDialog:
        """
        Retrieve the current singleton :class:`CaptureDialog`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: CaptureDialog
        """
        pass
    
    
    def GetDebugMessageView(self) -> DebugMessageView:
        """
        Retrieve the current singleton :class:`DebugMessageView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: DebugMessageView
        """
        pass
    
    
    def GetDiagnosticLogView(self) -> DiagnosticLogView:
        """
        Retrieve the current singleton :class:`DiagnosticLogView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: DiagnosticLogView
        """
        pass
    
    
    def GetCommentView(self) -> CommentView:
        """
        Retrieve the current singleton :class:`CommentView`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: CommentView
        """
        pass
    
    
    def GetPerformanceCounterViewer(self) -> PerformanceCounterViewer:
        """
        Retrieve the current singleton :class:`PerformanceCounterViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PerformanceCounterViewer
        """
        pass
    
    
    def GetStatisticsViewer(self) -> StatisticsViewer:
        """
        Retrieve the current singleton :class:`StatisticsViewer`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: StatisticsViewer
        """
        pass
    
    
    def GetTimelineBar(self) -> TimelineBar:
        """
        Retrieve the current singleton :class:`TimelineBar`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: TimelineBar
        """
        pass
    
    
    def GetPythonShell(self) -> PythonShell:
        """
        Retrieve the current singleton :class:`PythonShell`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: PythonShell
        """
        pass
    
    
    def GetResourceInspector(self) -> ResourceInspector:
        """
        Retrieve the current singleton :class:`ResourceInspector`.
        
        :return: The current window, which is created (but not shown) it there wasn't one open.
        :rtype: ResourceInspector
        """
        pass
    
    
    def HasEventBrowser(self) -> bool:
        """
        Check if there is a current :class:`EventBrowser` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasAPIInspector(self) -> bool:
        """
        Check if there is a current :class:`APIInspector` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasAnnotationViewer(self) -> bool:
        """
        Check if there is a current :class:`AnnotationViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasTextureViewer(self) -> bool:
        """
        Check if there is a current :class:`TextureViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasPipelineViewer(self) -> bool:
        """
        Check if there is a current :class:`PipelineStateViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasMeshPreview(self) -> bool:
        """
        Check if there is a current mesh previewing :class:`BufferViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasCaptureDialog(self) -> bool:
        """
        Check if there is a current :class:`CaptureDialog` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasDebugMessageView(self) -> bool:
        """
        Check if there is a current :class:`DebugMessageView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasDiagnosticLogView(self) -> bool:
        """
        Check if there is a current :class:`DiagnosticLogView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasCommentView(self) -> bool:
        """
        Check if there is a current :class:`CommentView` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasPerformanceCounterViewer(self) -> bool:
        """
        Check if there is a current :class:`PerformanceCounterViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasStatisticsViewer(self) -> bool:
        """
        Check if there is a current :class:`StatisticsViewer` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasTimelineBar(self) -> bool:
        """
        Check if there is a current :class:`TimelineBar` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasPythonShell(self) -> bool:
        """
        Check if there is a current :class:`PythonShell` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def HasResourceInspector(self) -> bool:
        """
        Check if there is a current :class:`ResourceInspector` open.
        
        :return: ``True`` if there is a window open.
        :rtype: bool
        """
        pass
    
    
    def ShowEventBrowser(self):
        """
        Raise the current :class:`EventBrowser`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowAPIInspector(self):
        """
        Raise the current :class:`APIInspector`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowAnnotationViewer(self):
        """
        Raise the current :class:`AnnotationViewer`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowTextureViewer(self):
        """
        Raise the current :class:`TextureViewer`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowMeshPreview(self):
        """
        Raise the current mesh previewing :class:`BufferViewer`, showing it in the default
        place if needed.
        """
        pass
    
    
    def ShowPipelineViewer(self):
        """
        Raise the current :class:`PipelineStateViewer`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowCaptureDialog(self):
        """
        Raise the current :class:`CaptureDialog`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowDebugMessageView(self):
        """
        Raise the current :class:`DebugMessageView`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowDiagnosticLogView(self):
        """
        Raise the current :class:`DiagnosticLogView`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowCommentView(self):
        """
        Raise the current :class:`CommentView`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowPerformanceCounterViewer(self):
        """
        Raise the current :class:`PerformanceCounterViewer`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowStatisticsViewer(self):
        """
        Raise the current :class:`StatisticsViewer`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowTimelineBar(self):
        """
        Raise the current :class:`TimelineBar`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowPythonShell(self):
        """
        Raise the current :class:`PythonShell`, showing it in the default place if needed.
        """
        pass
    
    
    def ShowResourceInspector(self):
        """
        Raise the current :class:`ResourceInspector`, showing it in the default place if needed.
        """
        pass
    
    
    def EditShader(self, id: ResourceId, stage: ShaderStage, entryPoint: str, files: List[Tuple[str, str]], knownTool: KnownShaderTool, shaderEncoding: ShaderEncoding, flags: ShaderCompileFlags, saveCallback: Callable[['CaptureContext', ShaderViewer, ResourceId, ShaderStage, ShaderEncoding, ShaderCompileFlags, str, bytes], None], revertCallback: Callable[['CaptureContext', ShaderViewer, ResourceId], None]) -> ShaderViewer:
        """
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
        :param Callable[[CaptureContext,ShaderViewer,renderdoc.ResourceId,renderdoc.ShaderStage,renderdoc.ShaderEncoding,renderdoc.ShaderCompileFlags, str, bytes], None] saveCallback: The
          callback function to call when a save/update is triggered.
          Callback function signature must match :func:`SaveCallback`.
        :param Callable[[CaptureContext, ShaderViewer, renderdoc.ResourceId], None] revertCallback: The
          callback function to call when the shader is to be reverted - either by user request or because
          the shader viewer was closed.
          Callback function signature must match :func:`RevertCallback`.
        :return: The new :class:`ShaderViewer` window opened but not shown for editing.
        :rtype: ShaderViewer
        """
        pass
    
    
    def DebugShader(self, shader: ShaderReflection, pipeline: ResourceId, trace: ShaderDebugTrace, debugContext: str) -> ShaderViewer:
        """
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
    
    
    def ViewShader(self, shader: ShaderReflection, pipeline: ResourceId) -> ShaderViewer:
        """
        Show a new :class:`ShaderViewer` window, showing a read-only view of a given shader.
        
        :param renderdoc.ShaderReflection shader: The reflection data for the shader to view.
        :param renderdoc.ResourceId pipeline: The pipeline state object, if applicable, that this shader is
          bound to.
        :return: The new :class:`ShaderViewer` window opened, but not shown.
        :rtype: ShaderViewer
        """
        pass
    
    
    def ViewShaderMessages(self, stages: ShaderStageMask) -> ShaderMessageViewer:
        """
        Show a new :class:`ShaderMessageViewer` window, showing the current event's messages.
        
        :param renderdoc.ShaderStageMask stages: The initial stages being viewed.
        :return: The new :class:`ShaderMessageViewer` window opened, but not shown.
        :rtype: ShaderMessageViewer
        """
        pass
    
    
    def ViewDescriptorStore(self, id: ResourceId) -> DescriptorViewer:
        """
        Show a new :class:`DescriptorViewer` window, showing the full raw contents of a
        descriptor store.
        
        :param renderdoc.ResourceId id: The ID of the descriptor store to fetch data from.
        :return: The new :class:`DescriptorViewer` window opened, but not shown.
        :rtype: DescriptorViewer
        """
        pass
    
    
    def ViewDescriptors(self, descriptors: List[Descriptor], samplerDescriptors: List[SamplerDescriptor]) -> DescriptorViewer:
        """
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
    
    
    def ViewBuffer(self, byteOffset: int, byteSize: int, id: ResourceId, format: str = "") -> BufferViewer:
        """
        Show a new :class:`BufferViewer` window, showing a read-only view of buffer data.
        
        :param int byteOffset: The offset in bytes to the start of the buffer data to show.
        :param int byteSize: The number of bytes in the buffer to show.
        :param renderdoc.ResourceId id: The ID of the buffer to fetch data from.
        :param str format="": **Optional parameter**. A HLSL/GLSL style formatting string.
        :return: The new :class:`BufferViewer` window opened, but not shown.
        :rtype: BufferViewer
        """
        pass
    
    
    def ViewTextureAsBuffer(self, id: ResourceId, sub: Subresource, format: str = "") -> BufferViewer:
        """
        Show a new :class:`BufferViewer` window, showing a read-only view of a texture's raw
        bytes.
        
        :param renderdoc.ResourceId id: The ID of the texture itself.
        :param renderdoc.Subresource sub: The subresource within this texture to use.
        :param str format="": **Optional parameter**. A HLSL/GLSL style formatting string.
        :return: The new :class:`BufferViewer` window opened, but not shown.
        :rtype: BufferViewer
        """
        pass
    
    
    def ViewConstantBuffer(self, stage: ShaderStage, slot: int, idx: int) -> BufferViewer:
        """
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
    
    
    def ViewPixelHistory(self, id: ResourceId, x: int, y: int, view: int, display: TextureDisplay) -> PixelHistoryView:
        """
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
    
    
    def CreateBuiltinWindow(self, objectName: str) -> QWidget:
        """
        Creates and returns a built-in window.
        
        This function is intended for internal use for restoring layouts, and generally should not be used
        by user code.
        
        :param str objectName: The built-in name of a singleton window.
        :return: The handle to the existing or newly created window of this type.
        :rtype: QWidget
        """
        pass
    
    
    def BuiltinWindowClosed(self, window: QWidget):
        """
        Marks a built-in window as closed.
        
        This function is intended for internal use by the built-in windows for singleton management, and
        should not be called by user code.
        
        :param QWidget window: The built-in window that closed.
        """
        pass
    
    
    def RaiseDockWindow(self, dockWindow: QWidget):
        """
        Raises a window within its docking manager so it becomes the focus of wherever it is
        currently docked.
        
        :param QWidget dockWindow: The window to raise.
        """
        pass
    
    
    def AddDockWindow(self, newWindow: QWidget, ref: DockReference, refWindow: QWidget, percentage: float = 0.5):
        """
        Adds a new window within the docking system.
        
        :param QWidget newWindow: The new window to add.
        :param DockReference ref: The location to add the new window, possibly relative to ``refWindow``.
        :param QWidget refWindow: The window to refer to if the new window is being added relative, or can
          be ``None`` if the new location is absolute.
        :param float percentage=0.5: **Optional parameter**. The percentage to split the area. If omitted, a 50% split is
          used.
        """
        pass
    
    
    def CurD3D11PipelineState(self) -> D3D11State:
        """
        Retrieve the current :class:`~renderdoc.D3D11State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D11 API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current D3D11 pipeline state.
        :rtype: renderdoc.D3D11State
        """
        pass
    
    
    def CurD3D12PipelineState(self) -> D3D12State:
        """
        Retrieve the current :class:`~renderdoc.D3D12State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D12 API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current D3D12 pipeline state.
        :rtype: renderdoc.D3D12State
        """
        pass
    
    
    def CurGLPipelineState(self) -> GLState:
        """
        Retrieve the current :class:`~renderdoc.GLState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the OpenGL API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current OpenGL pipeline state.
        :rtype: renderdoc.GLState
        """
        pass
    
    
    def CurVulkanPipelineState(self) -> VKState:
        """
        Retrieve the current :class:`~renderdoc.VKState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the Vulkan API.
        You should determine the API of the capture first before fetching it.
        
        :return: The current Vulkan pipeline state.
        :rtype: renderdoc.VKState
        """
        pass
    
    
    def CurPipelineState(self) -> PipeState:
        """
        Retrieve the current :class:`~renderdoc.PipeState` abstracted pipeline state.
        
        This pipeline state will always be valid, and allows queries that will work regardless of the
        capture's API.
        
        :return: The current API-agnostic abstracted pipeline state.
        :rtype: renderdoc.PipeState
        """
        pass
    
    
    def Config(self) -> PersistentConfig:
        """
        Retrieve the current persistent config.
        
        :return: The current persistent config manager.
        :rtype: PersistentConfig
        """
        pass
    
    
    def Extensions(self) -> 'ExtensionManager':
        """
        Retrieve the manager for extensions.
        
        :return: The current extension manager.
        :rtype: ExtensionManager
        """
        pass
    
from renderdoc import APIEvent, ActionDescription, SDChunk
from typing import Callable, List

class EventBrowser():
    # Original docstring
    """
    The event browser window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetEventBrowser`.
    
    .. function:: EventFilterCallback(context, filter, params, eventId, chunk, action, name)
    
      Not a member function - the signature for any ``EventFilterCallback`` callbacks.
    
      Called for each event in a capture when performing filtering in the Event Browser. The associated
      :func:`FilterParseCallback` will be called first to parse the parameters, and is available for caching
      or syntax checking. The same filter name and params string will be passed to this function.
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The parameters to the filter function.
      :param int eventId: The event's :data:`eventId <renderdoc.APIEvent.eventId>`.
      :param renderdoc.SDChunk chunk: The structured data chunk for this event.
      :param renderdoc.ActionDescription action: The action that contains this event. If the event is
        the action itself then the event ID will be equal.
      :param str name: The name of the event as shown in the event browser, for string-based filtering.
      :return: Whether or not this event matches the filter
      :rtype: bool
    
    .. function:: FilterParseCallback(context, filter, params)
    
      Not a member function - the signature for any ``FilterParseCallback`` callbacks.
    
      Called once when the filter changes, to allow parsing any any data caching, as well as reporting
      of errors in the filter usage.
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The parameters to the filter function.
      :return: An empty string if the parse succeeded, otherwise any error messages to be displayed to
        the user, such as syntax or other errors.
      :rtype: str
    
    .. function:: AutoCompleteCallback(context, filter, params)
    
      Not a member function - the signature for any ``AutoCompleteCallback`` callbacks.
    
      Called when autocompletion is triggered inside a filter. The params passed are any previous
      text inside the filter's parameter list up to where the cursor is. The callback should return a
      list of identifiers used for auto-completion.
    
      The list does not have to be pre-filtered for matches to the :paramref:`AutoCompleteCallback.params`,
      that is provided to allow different autocompletion at different stages (e.g. if there are no
      parameters, you can autocomplete a property, if a property is already present you can
      autocomplete valid values for it)
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The previous parameter text to the filter function.
      :return: A list of strings giving identifiers to autocomplete, or an empty list of there are no
        such identifiers to prompt.
      :rtype: List[str]
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`EventBrowser` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def UpdateDurationColumn(self):
        """
        Updates the duration column if the selected time unit changes.
        """
        pass
    
    
    def GetAPIEventForEID(self, eventId: int) -> APIEvent:
        """
        Uses the existing caching in the event browser to return a :class:`~renderdoc.APIEvent`
        for a specified EID.
        
        If no capture is loaded or the EID doesn't correspond to a known event, an empty struct will be
        returned.
        
        :param int eventId: The EID to look up.
        :return: The event corresponding to the EID, or an empty struct if no such EID exists.
        :rtype: renderdoc.APIEvent
        """
        pass
    
    
    def GetActionForEID(self, eventId: int) -> ActionDescription:
        """
        Uses the existing caching in the event browser to return a
        :class:`~renderdoc.ActionDescription` for a specified EID. This action may not be the exact EID
        specified, but it will be the action that the EID is associated with. I.e. if you specify the EID for
        a state setting event the next action will be returned.
        
        If no capture is loaded or the EID doesn't correspond to a known event, ``None`` will be returned.
        
        :param int eventId: The EID to look up.
        :return: The action containing the EID, or ``None`` if no such EID exists.
        :rtype: renderdoc.ActionDescription
        """
        pass
    
    
    def GetEventName(self, eventId: int) -> str:
        """
        Returns the formatted name of an event according to the current settings, whether
        that be a custom name or an auto-generated name with/without parameter names.
        
        If no capture is loaded or the EID doesn't correspond to a known event, an empty string will be
        returned.
        
        :param int eventId: The EID to look up.
        :return: The formatted name of the specified event, or ``None`` if no such EID exists.
        :rtype: str
        """
        pass
    
    
    def IsAPIEventVisible(self, eventId: int) -> bool:
        """
        Determines if a given EID is visible with the current filters applied to the event
        browser.
        
        If no capture is loaded or the EID doesn't correspond to a known event, ``False`` will be returned.
        
        :param int eventId: The EID to look up.
        :return: Whether or not the event is currently visible (passing the filters).
        :rtype: bool
        """
        pass
    
    
    def RegisterEventFilterFunction(self, name: str, description: str, filter: Callable[['CaptureContext', str, str, int, SDChunk, ActionDescription, str], bool], parser: Callable[['CaptureContext', str, str], str], completer: Callable[['CaptureContext', str, str], List[str]]) -> bool:
        """
        Registers a new event browser filter function.
        
        Filter functions are available as $name() so long as they don't shadow an existing function. The
        filter callback will be called for each event to filter.
        
        The parser callback will be called once when a filter is first specified or the parameters change.
        Note that a filter can be used multiple times in a filter expression! For this reason the parser
        may be called multiple times and the filter callback takes the parameters string. If any expensive
        work is done then the parameters can be used as a cache key to cache any data once per filter
        expression.
        
        :param str name: The name of the filter function.
        :param str description: The description of the filter function. This should explain the available
          parameters (if applicable) and what the filter does. It will be used for documenting to users
          what each filter means.
        :param Callable[[CaptureContext,str,str,int,renderdoc.SDChunk,renderdoc.ActionDescription,str], bool] filter: The
          callback to call for each candidate event to perform filtering.
          Callback function signature must match :func:`EventFilterCallback`.
        :param Callable[[CaptureContext,str,str], str] parser: The callback to call when the parsing the
          parameters and checking for any errors. This can be ``None`` if no pre-parsing is required.
          Callback function signature must match :func:`FilterParseCallback`.
        :param Callable[[CaptureContext,str,str], List[str]] completer: The callback to call when trying
          to provide autocomplete suggestions. This can be ``None`` if no completion is desired/applicable.
          Callback function signature must match :func:`AutoCompleteCallback`.
        :return: Whether or not the registration was successful.
        :rtype: bool
        """
        pass
    
    
    def UnregisterEventFilterFunction(self, name: str) -> bool:
        """
        Unregisters an event browser filter function that was previously registered.
        
        :param str name: The name of the filter function.
        
        :return: Whether or not the unregistration was successful.
        :rtype: bool
        """
        pass
    
    
    def SetCurrentFilterText(self, text: str):
        """
        Sets the current filter text. This will not modify any saved filter but will modify
        the scratch filter. The filter is applied immediately.
        
        :param str text: The filter text.
        """
        pass
    
    
    def GetCurrentFilterText(self) -> str:
        """
        Returns the current filter text, whether temporary or a saved filter.
        
        :return: The current filter text.
        :rtype: str
        """
        pass
    
    
    def SetUseCustomActionNames(self, use: bool):
        """
        Sets whether or not custom action names are used. Certain actions such as indirect
        actions it is useful to show a custom action name which contains the actual indirect parameters
        instead of the 'raw' parameters.
        
        :param bool use: Whether or not custom action names will be used.
        """
        pass
    
    
    def SetShowParameterNames(self, show: bool):
        """
        Sets whether or not parameter names are shown in the events. If disabled, only the
        value is shown and the parameter is implicit.
        
        .. note::
          If custom action names are used this will not have an effect for any such actions. See
          :meth:`SetUseCustomActionNames`.
        
        :param bool show: Whether or not parameter names will be shown.
        """
        pass
    
    
    def SetShowAllParameters(self, show: bool):
        """
        Sets whether or not all parameters are shown in the events. By default only
        the most significant parameters are shown.
        
        .. note::
          If custom action names are used this will not have an effect for any such actions. See
          :meth:`SetUseCustomActionNames`.
        
        :param bool show: Whether or not parameter names will be shown.
        """
        pass
    
    
    def SetEmptyRegionsVisible(self, show: bool):
        """
        Sets whether or not marker regions which have no visible actions.
        
        :param bool show: Whether or not empty regions after filtering will be shown.
        """
        pass
    
    
    def SetHighlightedAnnotation(self, annotationPath: str):
        """
        Sets the current annotation key path. This will not display the annotation column if
        it is not already visible.
        
        :param str annotationPath: The new annotation path.
        """
        pass
    
    
    def GetHighlightedAnnotation(self) -> str:
        """
        Returns the current annotation key path as being highlighted in the annotation column.
        
        :return: The current annotation path.
        :rtype: str
        """
        pass
    
    
    def SetDurationColumnVisible(self, show: bool):
        """
        Sets whether or not the duration column is visible.
        
        :param bool show: If the duration column should be shown.
        """
        pass
    
    
    def SetAnnotationColumnVisible(self, show: bool):
        """
        Sets whether or not the annotation column is visible.
        
        :param bool show: If the duration column should be shown.
        """
        pass
    
from ._ContextMenu import ContextMenu
from ._DialogButton import DialogButton
from ._ExtensionMetadata import ExtensionMetadata
from ._PanelMenu import PanelMenu
from ._WindowMenu import WindowMenu
from typing import Any, Callable, Dict, List

class ExtensionManager():
    # Original docstring
    """
    A manager for listing available and active extensions, as well as the interface for
    extensions to register hooks and additional functionality.
    
    This manager is retrieved by calling :meth:`CaptureContext.Extensions`.
    
    .. function:: ExtensionCallback(context, data)
    
      Not a member function - the signature for any ``ExtensionCallback`` callbacks.
    
      Callback for extensions to register entry points with, used in many situations depending on how it
      was registered.
    
      :param CaptureContext context: The current capture context.
      :param Dict[str, Any] data: Additional data for the call, as a dictionary with string keys.
        Context-dependent based on what generated the callback
    """
    
    
    
    def GetInstalledExtensions(self) -> List[ExtensionMetadata]:
        """
        Retrieve a list of installed extensions.
        
        :return: The list of installed extensions.
        :rtype: List[ExtensionMetadata]
        """
        pass
    
    
    def IsExtensionLoaded(self, name: str) -> bool:
        """
        Check if an installed extension is enabled.
        
        :param str name: The qualified name of the extension, e.g. ``foo.bar``
        :return: If the extension is enabled or not.
        :rtype: bool
        """
        pass
    
    
    def GetLoadedExtensions(self) -> List[str]:
        """
        Retrieve a list of loaded extensions.
        
        :return: The list of installed extension names.
        :rtype: List[str]
        """
        pass
    
    
    def LoadExtension(self, name: str) -> str:
        """
        Enable an extension by name. If the extension is already enabled, this will reload it.
        
        :param str name: The qualified name of the extension, e.g. ``foo.bar``
        :return: If the extension loaded successfully, an empty string, otherwise the errors encountered
          while loading it.
        :rtype: str
        """
        pass
    
    
    def IsPythonDebuggerConnected(self) -> bool:
        """
        Check if a python debugger is connected.
        
        .. note::
          If python debugging is not supported or failed to load, this will return ``False``.
        
        :return: If a python debugger is connected.
        :rtype: bool
        """
        pass
    
    
    def RegisterWindowMenu(self, base: WindowMenu, submenus: List[str], callback: Callable[['CaptureContext', Dict[str, Any]], None]):
        """
        Register a new menu item in the main window's menus for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param WindowMenu base: The base menu to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry, or two
          entries if ``base`` is :data:`WindowMenu.NewMenu`.
        :param Callable[[CaptureContext, Dict[str, Any]], None] callback: The function to callback when
          the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass
    
    
    def RegisterPanelMenu(self, base: PanelMenu, submenus: List[str], callback: Callable[['CaptureContext', Dict[str, Any]], None]):
        """
        Register a menu item in a panel for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param PanelMenu base: The panel to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry.
        :param Callable[[CaptureContext, Dict[str, Any]], None] callback: The function to callback when
          the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass
    
    
    def RegisterContextMenu(self, base: ContextMenu, submenus: List[str], callback: Callable[['CaptureContext', Dict[str, Any]], None]):
        """
        Register a context menu item in a panel for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param ContextMenu base: The panel to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry.
        :param Callable[[CaptureContext, Dict[str, Any]], None] callback: The function to callback when
          the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass
    
    
    def GetMiniQtHelper(self) -> 'MiniQtHelper':
        """
        Returns a handle to the mini Qt helper. See :class:`MiniQtHelper`.
        
        :return: The helper interface.
        :rtype: MiniQtHelper
        """
        pass
    
    
    def MessageDialog(self, text: str, title: str = ""):
        """
        Display a simple informational message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param str title="": **Optional parameter**. The dialog title.
        """
        pass
    
    
    def ErrorDialog(self, text: str, title: str = ""):
        """
        Display an error message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param str title="": **Optional parameter**. The dialog title.
        """
        pass
    
    
    def QuestionDialog(self, text: str, options: List[DialogButton], title: str = "") -> DialogButton:
        """
        Display an error message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param List[DialogButton] options: The buttons to display on the dialog.
        :param str title="": **Optional parameter**. The dialog title.
        :return: The button that was clicked on.
        :rtype: DialogButton
        """
        pass
    
    
    def OpenFileName(self, caption: str = "", dir: str = "", filter: str = "") -> str:
        """
        Browse for a filename to open.
        
        :param str caption="": **Optional parameter**. The dialog title.
        :param str dir="": **Optional parameter**. The starting directory for browsing.
        :param str filter="": **Optional parameter**. The filter to apply for filenames.
        :return: The filename selected, or an empty string if nothing was selected.
        :rtype: str
        """
        pass
    
    
    def OpenDirectoryName(self, caption: str = "", dir: str = "") -> str:
        """
        Browse for a directory to open.
        
        :param str caption="": **Optional parameter**. The dialog title.
        :param str dir="": **Optional parameter**. The starting directory for browsing.
        :return: The directory selected, or an empty string if nothing was selected.
        :rtype: str
        """
        pass
    
    
    def SaveFileName(self, caption: str = "", dir: str = "", filter: str = "") -> str:
        """
        Browse for a filename to save to.
        
        :param str caption="": **Optional parameter**. The dialog title.
        :param str dir="": **Optional parameter**. The starting directory for browsing.
        :param str filter="": **Optional parameter**. The filter to apply for filenames.
        :return: The filename selected, or an empty string if nothing was selected.
        :rtype: str
        """
        pass
    
from renderdoc import ReplayOutput, WindowingData
from typing import Callable, List

class MiniQtHelper():
    # Original docstring
    """
    Python can have direct access to Qt via PySide2, but this is not always available in
    all RenderDoc builds. To aid extensions to manipulate widgets in a simple but portable fashion this
    helper exposes a small subset of Qt via RenderDoc's python bindings.
    
    The intention is not to allow fully flexible building of Qt panels, but to allow access to some
    basic UI building tools for simple data input and display which can be used on any RenderDoc build.
    
    This manager is retrieved by calling :meth:`ExtensionManager.GetMiniQtHelper`.
    
    .. note::
      The widget handles returned are PySide2 widgets where that is available, so this can be used to
      make a basic UI and optionally customise it further with PySide2 when possible.
    
    .. function:: WidgetCallback(context, widget, text)
    
      Not a member function - the signature for any ``WidgetCallback`` callbacks.
    
      Callback for widgets can be registered at creation time, the text field is optional and may be
      blank depending on the event, but the context and widget are always valid.
    
      :param CaptureContext context: The current capture context.
      :param QWidget widget: The widget sending the callback.
      :param str text: Additional data for the call, such as the current or selected text.
    
    .. function:: UIInvokeCallback()
    
      Not a member function - the signature for any ``UIInvokeCallback`` callbacks.
    
      Callback for invoking onto the UI thread from another thread (in particular the replay thread).
      Takes no parameters as the callback is expected to store its own state.
    """
    
    
    
    def InvokeOntoUIThread(self, callback: Callable[[], None]):
        """
        Invoke a callback on the UI thread. All widget accesses must come from the UI thread,
        so if work has been done on the render thread then this function can be used to asynchronously and
        safely go back to the UI thread.
        
        This function is safe to call on the UI thread, but it will synchronously call the callback
        immediately before returning.
        
        .. note::
          No parameters are provided to the callback, it is assumed that the callback will maintain its own
          context as needed.
        
        :param Callable[[], None] callback: The callback to invoke on the UI thread.
          Callback function signature must match :func:`UIInvokeCallback`.
        """
        pass
    
    
    def CreateToplevelWidget(self, windowTitle: str, closed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Creates and returns a top-level widget for creating layouts.
        
        The widget is not immediately visible. It should be shown either with :meth:`ShowWidgetAsDialog` or
        with :meth:`CaptureContext.AddDockWindow` once it's ready.
        
        This widget can have children added, but it is recommended to immediately add only one child which
        is a layout type widget, to allow customising how children are added. By default the children are
        added in a vertical layout.
        
        :param str windowTitle: The title of any window with this widget as its root.
        :param Callable[[CaptureContext, QWidget, str], None] closed=None: **Optional parameter**. A callback
          that will be called when the widget is closed by the user.
          This implicitly deletes the widget and all its children, which will no longer be valid even if a
          handle to them exists.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CloseToplevelWidget(self, widget: QWidget):
        """
        Closes a top-level widget as if the user had clicked to close.
        
        This function is undefined if used on a non top-level widget. It will invoke the closed widget
        callback.
        
        :param QWidget widget: The top-level widget to close.
        """
        pass
    
    
    def SetWidgetName(self, widget: QWidget, name: str):
        """
        Set the internal name of a widget. This is not displayed anywhere but can be used by
        :meth:`FindChildByName` to locate a widget within a hierarchy.
        
        .. note::
          Names are optional and only for your use. Nothing prevents from you from setting duplicate names,
          but this makes searches by name ambiguous.
        
        :param QWidget widget: The widget to set an internal name for.
        :param str name: The internal name to set for the widget.
        """
        pass
    
    
    def GetWidgetName(self, widget: QWidget) -> str:
        """
        Return the internal name of a widget, as set my :meth:`SetWidgetName`.
        
        :param QWidget widget: The widget to query.
        :return: The widget's internal name, which may be an empty string if no name has been set.
        :rtype: str
        """
        pass
    
    
    def GetWidgetType(self, widget: QWidget) -> str:
        """
        Return the type of the widget as a string. This type is the Qt type name so this
        should only be used for debugging as the name may change even if for the same type of widget.
        
        :param QWidget widget: The widget to query.
        :return: The widget's type name.
        :rtype: str
        """
        pass
    
    
    def FindChildByName(self, parent: QWidget, name: str) -> QWidget:
        """
        Find a child widget of a parent by internal name.
        
        :param QWidget parent: The widget to start the search from.
        :param str name: The internal name to search for.
        :return: The handle to the first widget with a matching name, or ``None`` if no widget is found.
        :rtype: QWidget
        """
        pass
    
    
    def GetParent(self, widget: QWidget) -> QWidget:
        """
        Return the parent of a widget in the widget hierarchy.
        
        .. note::
          The widget returned may not be a widget created through this helper interface if the specified
          widget has been docked somewhere. Beware making changes to any widgets returned as you may modify
          the RenderDoc UI itself.
        
        :param QWidget widget: The widget to query.
        :return: The handle to the parent widget with a matching name, or ``None`` if this widget is either
          not yet parented or is a top-level window.
        :rtype: QWidget
        """
        pass
    
    
    def GetNumChildren(self, widget: QWidget) -> int:
        """
        Return the number of children this widget has. This is generally only useful for
        layout type widgets.
        
        :param QWidget widget: The widget to query.
        :return: The number of child widgets this widget has.
        :rtype: int
        """
        pass
    
    
    def GetChild(self, parent: QWidget, index: int) -> QWidget:
        """
        Return a child widget for a parent.
        
        :param QWidget parent: The parent widget to look up.
        :param int index: The child index to return.
        :return: The specified child of the parent, or ``None`` if the index is out of bounds.
        :rtype: QWidget
        """
        pass
    
    
    def DestroyWidget(self, widget: QWidget):
        """
        Destroy a widget. Widgets stay alive unless explicitly destroyed here, OR in one other
        case when they are in a widget hierarchy under a top-level window which the user closes, which can
        be detected with the callback parameter in :meth:`CreateToplevelWidget`.
        
        If the widget being destroyed is a top-level window, it will be closed. Otherwise if it is part of a
        widget hierarchy it will be removed from its parent automatically. You can remove a widget and then
        destroy it if you wish, but you must not destroy a widget then attempt to remove it from its parent,
        as after the call to this function the widget is no longer valid to use.
        
        All children under this widget will be destroyed recursively as well, which will be made invalid
        even if a handle to them exists.
        
        :param QWidget widget: The widget to destroy.
        """
        pass
    
    
    def ShowWidgetAsDialog(self, widget: QWidget) -> bool:
        """
        Show a top-level widget as a blocking modal dialog. This is most useful to prompt the
        user for some specific information.
        
        The dialog is only closed when the user closes the window explicitly or if you call
        :meth:`CloseCurrentDialog` in a widget callback, e.g. upon a button press.
        
        :param QWidget widget: The top-level widget to show as a dialog.
        :return: Whether the dialog was closed successfully, via :meth:`CloseCurrentDialog`.
        :rtype: bool
        """
        pass
    
    
    def CloseCurrentDialog(self, success: bool):
        """
        Close the active modal dialog. This does nothing if no dialog is being shown.
        
        .. note::
          Closing a dialog 'successfully' does nothing except modify the return value of
          :meth:`ShowWidgetAsDialog`. It allows quick distinguishing between OK and Cancel actions without
          having to carry that information separately in a global or other state.
        
        :param bool success: ``True`` if the dialog was successful (the user clicked an OK/Accept type
          button).
        """
        pass
    
    
    def CreateHorizontalContainer(self) -> QWidget:
        """
        Creates and returns a horizontal layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are listed horizontally. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateVerticalContainer(self) -> QWidget:
        """
        Creates and returns a vertical layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are listed vertically. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateGridContainer(self) -> QWidget:
        """
        Creates and returns a grid layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are arranged in a grid. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space. This will not violate the grid constraint though.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateSpacer(self, horizontal: bool) -> QWidget:
        """
        Creates and returns a spacer widget.
        
        This widget is completely empty but consumes empty space, meaning all other non-greedy widgets in
        the same container will be minimally sized. This can be useful for simple layouts.
        
        :param bool horizontal: ``True`` if this spacer should consume horizontal space, ``False`` if this
          spacer should consume vertical space. Typically this matches the direction of the layout it is
          in.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def ClearContainedWidgets(self, parent: QWidget):
        """
        Removes all child widgets from a parent and makes them invisible.
        
        These widgets remain valid and can be re-added to another parent or the same parent.
        
        :param QWidget parent: The parent widget to clear of  children.
        """
        pass
    
    
    def AddGridWidget(self, parent: QWidget, row: int, column: int, child: QWidget, rowSpan: int, columnSpan: int):
        """
        Adds a child widget to a grid layout. If the parent is not a grid layout nothing will
        happen and the widget will not be added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param int row: The row at which to add the child widget.
        :param int column: The column at which to add the child widget.
        :param QWidget child: The child widget to add.
        :param int rowSpan: How many rows should this child span over.
        :param int columnSpan: How many columns should this child span over.
        """
        pass
    
    
    def AddWidget(self, parent: QWidget, child: QWidget):
        """
        Adds a child widget to the end of an ordered layout (either horizontal or vertical).
        If the parent is not an ordered layout nothing will happen and the widget will not be added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param QWidget child: The child widget to add.
        """
        pass
    
    
    def InsertWidget(self, parent: QWidget, index: int, child: QWidget):
        """
        Insert a child widget at the specified index in an ordered layout (either horizontal
        or vertical). If the parent is not an ordered layout nothing will happen and the widget will not be
        added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param int index: The index to insert the widget at. If this index is out of bounds it will be
          clamped, so that negative indices will be equivalent to index 0 and all indices above the number
          of children will append the widget
        :param QWidget child: The child widget to add.
        """
        pass
    
    
    def SetWidgetText(self, widget: QWidget, text: str):
        """
        Set the 'text' of a widget. How this manifests depends on the type of the widget, for
        example a text-box or label will set the text directly. For a checkbox or radio button this will
        add text next to it.
        
        :param QWidget widget: The widget to set text for.
        :param str text: The text to set for the widget.
        """
        pass
    
    
    def AppendText(self, widget: QWidget, text: str):
        """
        Appends to the 'text' of a widget. For most widgets this will not be different from
        getting the text with :meth:`GetWidgetText`, appending to the string, and setting with :meth:`SetWidgetText`
        but for multi-line widgets like text edits this can give a better experience with better scrolling.
        
        This will also scroll to and move the cursor to the end of the text.
        
        :param QWidget widget: The widget to append text for.
        :param str text: The text to append to the widget's text.
        """
        pass
    
    
    def GetWidgetText(self, widget: QWidget) -> str:
        """
        Return the current text of a widget. See :meth:`SetWidgetText`.
        
        :param QWidget widget: The widget to query.
        :return: The widget's current text, which may be an empty string if no valid text is available.
        :rtype: str
        """
        pass
    
    
    def ScrollToTop(self, widget: QWidget):
        """
        Scroll the widget's vertical scrollbar to the top. If the widget has no scrollbar
        this will do nothing
        
        :param QWidget widget: The widget to scroll in.
        """
        pass
    
    
    def ScrollToBottom(self, widget: QWidget):
        """
        Scroll the widget's vertical scrollbar to the bottom. If the widget has no scrollbar
        this will do nothing
        
        :param QWidget widget: The widget to scroll in.
        """
        pass
    
    
    def SetWidgetFont(self, widget: QWidget, font: str, fontSize: int, bold: bool, italic: bool):
        """
        Change the font properties of a widget.
        
        The font string can be set either to '_default' or '_fixed' to choose the user-selected default
        font or monospaced fonts respectively.
        
        :param QWidget widget: The widget to change font of.
        :param str font: The new font family to use, or an empty string to leave the font family the same.
        :param int fontSize: The new font point size to use, or 0 to leave the size the same.
        :param bool bold: ``True`` if the font should be bold.
        :param bool italic: ``True`` if the font should be italic.
        """
        pass
    
    
    def SetWidgetEnabled(self, widget: QWidget, enabled: bool):
        """
        Set whether the widget is enabled or not. This generally only affects interactive
        widgets and not fixed widgets, interactive widgets become read-only while still displaying the same
        data.
        
        .. note::
          Disabled widgets can still be modified programmatically, they are only disabled for the user.
        
        :param QWidget widget: The widget to enable or disable.
        :param bool enabled: ``True`` if the widget should be enabled.
        """
        pass
    
    
    def IsWidgetEnabled(self, widget: QWidget) -> bool:
        """
        Return the current enabled-state of a widget. See :meth:`SetWidgetEnabled`.
        
        :param QWidget widget: The widget to query.
        :return: ``True`` if the widget is currently enabled.
        :rtype: bool
        """
        pass
    
    
    def SetWidgetVisible(self, widget: QWidget, visible: bool):
        """
        Set whether the widget is visible or not. An invisible widget maintains its position
        in the hierarchy but is not visible and cannot be interacted with in any way.
        
        :param QWidget widget: The widget to show or hide.
        :param bool visible: ``True`` if the widget should be made visible (shown).
        """
        pass
    
    
    def IsWidgetVisible(self, widget: QWidget) -> bool:
        """
        Return the current visibility of a widget. See :meth:`SetWidgetVisible`.
        
        This query is recursive - a widget could be individually visible, but if it is under a parent which
        is invisible then this widget will be returned as invisible.
        
        :param QWidget widget: The widget to query.
        :return: ``True`` if the widget is currently visible.
        :rtype: bool
        """
        pass
    
    
    def CreateGroupBox(self, collapsible: bool) -> QWidget:
        """
        Create a groupbox widget which can optionally allow collapsing.
        
        This widget can have children added, but it is recommended to immediately add only one child which
        is a layout type widget, to allow customising how children are added. By default the children are
        added in a vertical layout.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        :param bool collapsible: ``True`` if the groupbox should have a toggle in its header to allow
          collapsing its contents down vertically.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateButton(self, pressed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Create a normal button widget.
        
        :param Callable[[CaptureContext, QWidget, str], None] pressed=None: **Optional parameter**. Callback
          to be called when the button is pressed.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateLabel(self) -> QWidget:
        """
        Create a read-only label widget.
        
        .. note::
          This widget will be blank by default, you can set the text with :meth:`SetWidgetText`.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def SetLabelImage(self, widget: QWidget, data: bytes, width: int, height: int, alpha: bool):
        """
        Set an image for a label widget. If the widget isn't a label, this call has no effect.
        
        The label will be resized to a fixed size to display the image at 100% scale. Any text in the label
        will not be displayed, but passing an empty image will revert the label back to being text-based.
        
        The data must be in RGB(A) format with the first byte of each texel being R.
        
        :param QWidget widget: The widget to set the picture for.
        :param bytes data: The image data itself, tightly packed.
        :param int width: The width of the image in pixels.
        :param int height: The height of the image in pixels.
        :param bool alpha: ``True`` if the image data contains an alpha channel.
        """
        pass
    
    
    def CreateOutputRenderingWidget(self) -> QWidget:
        """
        Create a widget suitable for rendering to with a :class:`renderdoc.ReplayOutput`. This
        widget takes care of painting on demand and recreating the internal display widget when necessary,
        however this means you must use :meth:`GetWidgetWindowingData` to retrieve the windowing data for
        creating the output as well as call :meth:`SetWidgetReplayOutput` to notify the widget of the
        current output.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def GetWidgetWindowingData(self, widget: QWidget) -> WindowingData:
        """
        Return the opaque pointer of windowing data suitable for passing to
        :meth:`~renderdoc.ReplayController.CreateOutput` or other functions that expect windowing data.
        
        If the widget is not a output rendering widget created with :meth:`CreateOutputRenderingWidget` this
        function will fail and return an invalid set of windowing data.
        
        It's important to note that the windowing data is not valid forever, so this function should be
        called as close to where you call :meth:`~renderdoc.ReplayController.CreateOutput` as possible.
        Also don't fetch windowing data unless you are going to create an output, because this function will
        cause the widget to go into an undefined state unless an output is created to render onto it.
        
        .. note::
          This function must be called on the main UI thread.
        
        :param QWidget widget: The widget to create windowing data for.
        :return: The windowing data.
        :rtype: renderdoc.WindowingData
        """
        pass
    
    
    def SetWidgetReplayOutput(self, widget: QWidget, output: ReplayOutput):
        """
        Set the current output for a widget. This only affects output rendering widgets. If
        another type of widget is passed nothing will happen.
        
        Passing ``None`` as the output will reset the widget and make it display the default background
        until another output is set.
        
        When a capture is closed and all outputs are destroyed, the widget will automatically unset the
        output so there is no need to do that manually.
        
        :param QWidget widget: The widget to set the output for.
        :param renderdoc.ReplayOutput output: The new output to set, or ``None`` to unset any previous
          output.
        """
        pass
    
    
    def SetWidgetBackgroundColor(self, widget: QWidget, red: float, green: float, blue: float):
        """
        Set the default background color for a rendering widget. This background color is
        used when no output is currently configured, e.g. when a capture is closed.
        
        For all other widget types this has no effect.
        
        To disable the background color pass negative values for the components, this will cause a default
        checkerboard to be rendered instead. This is the default behaviour when a widget is created.
        
        :param QWidget widget: The widget to set the background color of.
        :param float red: The red component of the color, in the range ``0.0 - 1.0``.
        :param float green: The green component of the color, in the range ``0.0 - 1.0``.
        :param float blue: The blue component of the color, in the range ``0.0 - 1.0``.
        """
        pass
    
    
    def CreateCheckbox(self, changed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Create a checkbox widget which can be toggled between unchecked and checked. When
        created the checkbox is unchecked.
        
        :param Callable[[CaptureContext, QWidget, str], None] changed=None: **Optional parameter**. Callback
          to be called when the widget is toggled.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateRadiobox(self, changed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Create a radio box widget which can be toggled between unchecked and checked but with
        at most one radio box in any group of sibling radio boxes being checked.
        
        Upon creation the radio box is unchecked, even in a group of other radio boxes that are unchecked.
        If you want a default radio box to be checked, you should use :meth:`SetWidgetChecked`.
        
        :param Callable[[CaptureContext, QWidget, str], None] changed=None: **Optional parameter**. Callback
          to be called when the widget is toggled.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def SetWidgetChecked(self, checkableWidget: QWidget, checked: bool):
        """
        Set whether the widget is checked or not. This only affects checkboxes and radio
        boxes and group box. If another type of widget is passed nothing will happen.
        
        :param QWidget checkableWidget: The widget to check or uncheck.
        :param bool checked: ``True`` if the widget should be checked.
        """
        pass
    
    
    def IsWidgetChecked(self, checkableWidget: QWidget) -> bool:
        """
        Return the current checked-state of a widget. See :meth:`SetWidgetChecked`. If another
        type of widget is passed other than a checkbox or radio box or group box ``False`` will be returned.
        
        :param QWidget checkableWidget: The widget to query.
        :return: ``True`` if the widget is currently checked.
        :rtype: bool
        """
        pass
    
    
    def CreateSpinbox(self, decimalPlaces: int, step: float) -> QWidget:
        """
        Create a spinbox widget with a numerical value and up/down buttons to change it.
        
        The number of decimal places can be set to 0 for an integer spinbox, and in that case the step
        should be set to 1.0.
        
        By default the spinbox has minimum and maximum values of 0.0 and 100.0, these can be changed with
        :meth:`SetSpinboxBounds`.
        
        :param int decimalPlaces: The number of decimal places to display when showing the number.
        :param float step: The step value to apply in each direction when clicking up or down.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def SetSpinboxBounds(self, spinbox: QWidget, minVal: float, maxVal: float):
        """
        Set the minimum and maximum values allowed in the spinbox. If another type of widget
        is passed nothing will happen.
        
        :param QWidget spinbox: The spinbox.
        :param float minVal: The minimum value allowed for the spinbox to reach. Lower values entered will
          be clamped to this.
        :param float maxVal: The maximum value allowed for the spinbox to reach. Higher values entered will
          be clamped to this.
        """
        pass
    
    
    def SetSpinboxValue(self, spinbox: QWidget, value: float):
        """
        Set the value contained in a spinbox. If another type of widget is passed nothing will
        happen.
        
        :param QWidget spinbox: The spinbox.
        :param float value: The value for the spinbox, which will be clamped by the current bounds.
        """
        pass
    
    
    def GetSpinboxValue(self, spinbox: QWidget) -> float:
        """
        Return the current value of a spinbox widget. If another type of widget is passed
        ``0.0`` will be returned.
        
        :param QWidget spinbox: The widget to query.
        :return: The current  value of the spinbox.
        :rtype: float
        """
        pass
    
    
    def CreateTextBox(self, singleLine: bool, changed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Create a text box widget for the user to enter text into.
        
        :param bool singleLine: ``True`` if the widget should be a single-line entry, otherwise it is a
          multi-line text box.
        :param Callable[[CaptureContext, QWidget, str], None] changed=None: **Optional parameter**. Callback
          to be called when the text in the textbox is changed.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def CreateComboBox(self, editable: bool, changed: Callable[['CaptureContext', QWidget, str], None] = None) -> QWidget:
        """
        Create a drop-down combo box widget.
        
        When created there are no pre-defined entries in the drop-down section. This can be changed with
        :meth:`SetComboOptions`.
        
        :param bool editable: ``True`` if the widget should allow the user to enter any text they wish as
          well as being able to select a pre-defined entry.
        :param Callable[[CaptureContext, QWidget, str], None] changed=None: **Optional parameter**. Callback
          to be called when the text in the combobox is changed. This
          will be called both when a new option is selected or when the user edits the text.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def SetComboOptions(self, combo: QWidget, options: List[str]):
        """
        Set the pre-defined options in a drop-down combo box. If another type of widget is
        passed nothing will happen.
        
        :param QWidget combo: The combo box.
        :param List[str] options: The new options for the combo box.
        """
        pass
    
    
    def GetComboCount(self, combo: QWidget) -> int:
        """
        Get the number of options in a drop-down combo box. If another type of widget is
        passed ``0`` will be returned.
        
        :param QWidget combo: The combo box.
        :return: The current number of options.
        :rtype: int
        """
        pass
    
    
    def SelectComboOption(self, combo: QWidget, option: str):
        """
        Select the current option in a drop-down combo box. If another type of widget or
        an unknown option is passed, nothing will happen.
        
        :param QWidget combo: The combo box.
        :param str option: The option to select.
        """
        pass
    
    
    def CreateProgressBar(self, horizontal: bool) -> QWidget:
        """
        Create a progress bar widget.
        
        By default the progress bar has minimum and maximum values of 0 and 100. These can be changed with
        :meth:`SetProgressBarRange`.
        
        :param bool horizontal: the progress bar orientation, true for horizontal otherwise vertical.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass
    
    
    def ResetProgressBar(self, pbar: QWidget):
        """
        Reset a progress bar widget.
        
        Rewinds the progress bar's indicator and hides the indicator's label (theme dependent). If you want
        to keep the label visible, call :meth:`SetProgressBarValue` with ``0`` instead. The minimum and maximum values
        are not changed.
        
        :param QWidget pbar: the progress bar.
        """
        pass
    
    
    def SetProgressBarValue(self, pbar: QWidget, value: int):
        """
        Set the progress bar's current value.
        
        Attempting to change the current value outside the minimum and maximum range does not affect
        the current value.
        
        :param QWidget pbar: the progress bar.
        :param int value: the new current value.
        """
        pass
    
    
    def UpdateProgressBarValue(self, pbar: QWidget, delta: int):
        """
        Set the progress bar's current value relative to the existing value.
        
        :param QWidget pbar: the progress bar.
        :param int delta: the relative value to update the current value.
        """
        pass
    
    
    def GetProgressBarValue(self, pbar: QWidget) -> int:
        """
        Get the progress bar's current value.
        
        :param QWidget pbar: the progress bar.
        :return: The current value of the progress bar.
        :rtype: int
        """
        pass
    
    
    def SetProgressBarRange(self, pbar: QWidget, minimum: int, maximum: int):
        """
        Set a progress bar's minimum and maximum values.
        
        If maximum is smaller than minimum, minimum is set as the maximum, too. If the current value falls
        outside the new range, the progress bar is reset. Use range (0, 0) to set the progress bar to
        indeterminate state (the progress cannot be estimated or is not being calculated).
        
        :param QWidget pbar: the progress bar.
        :param int minimum: the minimum value.
        :param int maximum: the maximum value.
        """
        pass
    
    
    def GetProgressBarMinimum(self, pbar: QWidget) -> int:
        """
        Get the minimum value of the progress bar's range.
        
        :param QWidget pbar: the progress bar.
        :return: The minimum value of the range.
        :rtype: int
        """
        pass
    
    
    def GetProgressBarMaximum(self, pbar: QWidget) -> int:
        """
        Get the maximum value of the progress bar's range.
        
        :param QWidget pbar: the progress bar.
        :return: The maximum value of the range.
        :rtype: int
        """
        pass
    
