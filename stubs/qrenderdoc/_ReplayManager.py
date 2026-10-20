from ._RemoteHost import RemoteHost
from renderdoc import CaptureAccess, CaptureFile, CaptureOptions, EnvironmentModification, ExecuteResult, PathEntry, ReplayController, ResultDetails
from typing import Callable, List

# Dummy types
from . import QWidget

class ReplayManager():
    # Original docstring
    """
    A manager for accessing the underlying replay information that isn't already abstracted
    in UI side structures. This manager controls and serialises access to the underlying
    :class:`~renderdoc.ReplayController`, as well as handling remote server connections.
    
    This manager is retrieved by calling :meth:`CaptureContext.Replay`.
    
    .. function:: ReplayInvokeCallback(controller)
    
      Not a member function - the signature for any ``ReplayInvokeCallback`` callbacks.
    
      :param renderdoc.ReplayController controller: The controller to access. Must not be cached or
        used after the callback returns.
    
    .. function:: DirectoryBrowseCallback(path, entries)
    
      Not a member function - the signature for any ``DirectoryBrowseCallback`` callbacks.
    
      :param str path: The path that was queried for.
      :param List[renderdoc.PathEntry] entries: The entries underneath the path, as relevant.
    """
    
    
    
    def DeleteCapture(self, capturefile: str, local: bool):
        """
        Delete a capture file, whether local or remote.
        
        :param str capturefile: The path to the file.
        :param bool local: ``True`` if the file is on the local machine.
        """
        pass
    
    
    def ConnectToRemoteServer(self, host: RemoteHost) -> ResultDetails:
        """
        Connect to a remote server.
        
        :param RemoteHost host: The host to connect to.
        :return: Whether or not the connection was successful.
        :rtype: renderdoc.ResultDetails
        """
        pass
    
    
    def DisconnectFromRemoteServer(self):
        """
        Disconnect from the server the manager is currently connected to.
        """
        pass
    
    
    def ShutdownServer(self):
        """
        Shutdown the server the manager is currently connected to.
        """
        pass
    
    
    def PingRemote(self):
        """
        Ping the remote server to ensure the connection is still alive.
        """
        pass
    
    
    def CancelReplayLoop(self):
        """
        Cancels the active replay loop. See :meth:`~renderdoc.ReplayController.ReplayLoop`.
        """
        pass
    
    
    def CurrentRemote(self) -> RemoteHost:
        """
        Retrieves the host that the manager is currently connected to.
        
        :return: The host connected to, or an invalid RemoteHost if no connection is active.
        :rtype: RemoteHost
        """
        pass
    
    
    def GetCaptureAccess(self) -> CaptureAccess:
        """
        Retrieves the capture access handle for the currently open file.
        
        :return: The file handle active, or ``None`` if no capture is open.
        :rtype: renderdoc.CaptureAccess
        """
        pass
    
    
    def GetCaptureFile(self) -> CaptureFile:
        """
        Retrieves the capture file handle for the currently open file, if it is available.
        
        If the capture is not open locally this will not be available, and only :meth:`GetCaptureAccess`
        will be usable.
        
        :return: The file handle active, or ``None`` if no capture is open or the capture is only available
          remotely.
        :rtype: renderdoc.CaptureFile
        """
        pass
    
    
    def ExecuteAndInject(self, exe: str, workingDir: str, cmdLine: str, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions) -> ExecuteResult:
        """
        Launch an application and inject into it to allow capturing.
        
        This happens either locally, or on the remote server, depending on whether a connection is active.
        
        :param str exe: The path to the executable to run.
        :param str workingDir: The working directory to use when running the application. If blank, the
          directory containing the executable is used.
        :param str cmdLine: The command line to use when running the executable, it will be processed in a
          platform specific way to generate arguments.
        :param List[renderdoc.EnvironmentModification] env: Any environment changes that should be made when
          running the program.
        :param str capturefile: The location to save any captures, if running locally.
        :param renderdoc.CaptureOptions opts: The capture options to use when injecting into the program.
        :return: The :class:`~renderdoc.ExecuteResult` indicating both the status of the operation (success
          or failure) and any reason for failure, or else the ident where the new application is listening
          for target control if everything succeeded.
        :rtype: renderdoc.ExecuteResult
        """
        pass
    
    
    def GetRemoteSupport(self) -> List[str]:
        """
        Retrieve a list of drivers that the current remote server supports.
        
        :return: The list of supported replay drivers.
        :rtype: List[str]
        """
        pass
    
    
    def GetHomeFolder(self, synchronous: bool, callback: Callable[[str, List[PathEntry]], None]):
        """
        Query the remote host for its home directory.
        
        If a capture is open, the callback will happen on the replay thread, otherwise it will happen in a
        blocking fashion on the current thread.
        
        :param bool synchronous: If a capture is open, then ``True`` will use :meth:`BlockInvoke` to call
          the callback. Otherwise if ``False`` then :meth:`AsyncInvoke` will be used.
        :param Callable[[str, List[renderdoc.PathEntry]], None] callback: The function to callback on the
          replay thread.
          Callback function signature must match :func:`DirectoryBrowseCallback`.
        """
        pass
    
    
    def ListFolder(self, path: str, synchronous: bool, callback: Callable[[str, List[PathEntry]], None]):
        """
        Query the remote host for the contents of a path.
        
        If a capture is open, the callback will happen on the replay thread, otherwise it will happen in a
        blocking fashion on the current thread.
        
        :param str path: The path to query the contents of.
        :param bool synchronous: If a capture is open, then ``True`` will use :meth:`BlockInvoke` to call
          the callback. Otherwise if ``False`` then :meth:`AsyncInvoke` will be used.
        :param Callable[[str, List[renderdoc.PathEntry]], None] callback: The function to callback on the
          replay thread.
          Callback function signature must match :func:`DirectoryBrowseCallback`.
        """
        pass
    
    
    def CopyCaptureToRemote(self, localpath: str, window: QWidget) -> str:
        """
        Copy a capture from the local machine to the remote host.
        
        :param str localpath: The path on the local machine to copy from.
        :param QWidget window: A handle to the window to use when showing a progress bar.
        :return: The path on the local machine where the file was saved, or empty if something went wrong.
        :rtype: str
        """
        pass
    
    
    def CopyCaptureFromRemote(self, remotepath: str, localpath: str, window: QWidget):
        """
        Copy a capture from the remote host to the local machine.
        
        :param str remotepath: The path on the remote server to copy from.
        :param str localpath: The path on the local machine to copy to.
        :param QWidget window: A handle to the window to use when showing a progress bar.
        """
        pass
    
    
    def GetCurrentProcessingTime(self) -> float:
        """
        Return the amount of time that the currently active command on the replay thread has
        been executing for.
        
        This can be used to identify if a command is long-running to display a progress bar or notification.
        
        :return: The time in seconds that the current command has been executing for, or 0.0 if no command
          is executing.
        :rtype: float
        """
        pass
    
    
    def AsyncInvoke(self, method: Callable[[ReplayController], None], tag: str = ""):
        """
        Make a non-blocking invoke call onto the replay thread.
        
        The callback can optionally have a tag provided.
        
        Tags are for cases when we might send a request - e.g. to pick a vertex or pixel -
        and want to preempt it with a new request before the first has returned. Either because some
        other work is taking a while or because we're sending requests faster than they can be
        processed.
        
        If a tag is present the manager processes only the request on the top of the queue, so when a
        new tagged invoke comes in, we remove any other requests in the queue before it that have the same tag.
        
        If no tag is present, the callback will be processed as normal.
        
        :param Callable[[renderdoc.ReplayController], None] method: The function to callback on the replay thread.
          Callback function signature must match :func:`ReplayInvokeCallback`.
        :param str tag="": **Optional parameter**. The tag to identify this callback.
        """
        pass
    
    
    def BlockInvoke(self, method: Callable[[ReplayController], None]):
        """
        Make a blocking invoke call onto the replay thread.
        
        :param Callable[[renderdoc.ReplayController], None] method: The function to callback on the replay thread.
          Callback function signature must match :func:`ReplayInvokeCallback`.
        """
        pass
    
