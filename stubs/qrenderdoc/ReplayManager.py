# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .RemoteHost import RemoteHost

from renderdoc.CaptureAccess import CaptureAccess

from renderdoc.CaptureFile import CaptureFile

from renderdoc.CaptureOptions import CaptureOptions

from renderdoc.EnvironmentModification import EnvironmentModification

from renderdoc.ExecuteResult import ExecuteResult

from renderdoc.ResultDetails import ResultDetails

class ReplayManager(): # skipped bases: <class 'SwigPyObject'>
    """
    A manager for accessing the underlying replay information that isn't already abstracted
    in UI side structures. This manager controls and serialises access to the underlying
    :class:`~renderdoc.ReplayController`, as well as handling remote server connections.
    
    This manager is retrieved by calling :meth:`CaptureContext.Replay`.
    
    .. function:: InvokeCallback(controller)
    
      Not a member function - the signature for any ``InvokeCallback`` callbacks.
    
      :param renderdoc.ReplayController controller: The controller to access. Must not be cached or
        used after the callback returns.
    
    .. function:: DirectoryBrowseCallback(path, entries)
    
      Not a member function - the signature for any ``DirectoryBrowseCallback`` callbacks.
    
      :param str path: The path that was queried for.
      :param List[renderdoc.PathEntry] entries: The entries underneath the path, as relevant.
    """
    def AsyncInvoke(self, tag: str, method: InvokeCallback): # real signature unknown; restored from __doc__
        """
        AsyncInvoke(tag, method)
        AsyncInvoke(method)
        
        Make a tagged non-blocking invoke call onto the replay thread.
        
        This tagged function is for cases when we might send a request - e.g. to pick a vertex or pixel -
        and want to pre-empt it with a new request before the first has returned. Either because some
        other work is taking a while or because we're sending requests faster than they can be
        processed.
        
        The manager processes only the request on the top of the queue, so when a new tagged invoke
        comes in, we remove any other requests in the queue before it that have the same tag.
        
        :param str tag: The tag to identify this callback.
        :param InvokeCallback method: The function to callback on the replay thread.
          Callback function signature must match :func:`InvokeCallback`.
        """
        pass

    def BlockInvoke(self, m): # real signature unknown; restored from __doc__
        """
        BlockInvoke(m)
        
        Make a blocking invoke call onto the replay thread.
        
        :param InvokeCallback method: The function to callback on the replay thread.
          Callback function signature must match :func:`InvokeCallback`.
        """
        pass

    def CancelReplayLoop(self): # real signature unknown; restored from __doc__
        """
        CancelReplayLoop()
        
        Cancels the active replay loop. See :meth:`~renderdoc.ReplayController.ReplayLoop`.
        """
        pass

    def ConnectToRemoteServer(self, host: RemoteHost) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        ConnectToRemoteServer(host)
        
        Connect to a remote server.
        
        :param RemoteHost host: The host to connect to.
        :return: Whether or not the connection was successful.
        :rtype: renderdoc.ResultDetails
        """
        pass

    def CopyCaptureFromRemote(self, remotepath: str, localpath: str, window: QWidget): # real signature unknown; restored from __doc__
        """
        CopyCaptureFromRemote(remotepath, localpath, window)
        
        Copy a capture from the remote host to the local machine.
        
        :param str remotepath: The path on the remote server to copy from.
        :param str localpath: The path on the local machine to copy to.
        :param QWidget window: A handle to the window to use when showing a progress bar.
        """
        pass

    def CopyCaptureToRemote(self, localpath: str, window: QWidget) -> str: # real signature unknown; restored from __doc__
        """
        CopyCaptureToRemote(localpath, window)
        
        Copy a capture from the local machine to the remote host.
        
        :param str localpath: The path on the local machine to copy from.
        :param QWidget window: A handle to the window to use when showing a progress bar.
        :return: The path on the local machine where the file was saved, or empty if something went wrong.
        :rtype: str
        """
        pass

    def CurrentRemote(self) -> RemoteHost: # real signature unknown; restored from __doc__
        """
        CurrentRemote()
        
        Retrieves the host that the manager is currently connected to.
        
        :return: The host connected to, or an invalid RemoteHost if no connection is active.
        :rtype: RemoteHost
        """
        pass

    def DeleteCapture(self, capturefile: str, local: bool): # real signature unknown; restored from __doc__
        """
        DeleteCapture(capturefile, local)
        
        Delete a capture file, whether local or remote.
        
        :param str capturefile: The path to the file.
        :param bool local: ``True`` if the file is on the local machine.
        """
        pass

    def DisconnectFromRemoteServer(self): # real signature unknown; restored from __doc__
        """
        DisconnectFromRemoteServer()
        
        Disconnect from the server the manager is currently connected to.
        """
        pass

    def ExecuteAndInject(self, exe: str, workingDir: str, cmdLine: str, env: List[EnvironmentModification], capturefile: str, opts: CaptureOptions) -> ExecuteResult: # real signature unknown; restored from __doc__
        """
        ExecuteAndInject(exe, workingDir, cmdLine, env, capturefile, opts)
        
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

    def GetCaptureAccess(self) -> CaptureAccess: # real signature unknown; restored from __doc__
        """
        GetCaptureAccess()
        
        Retrieves the capture access handle for the currently open file.
        
        :return: The file handle active, or ``None`` if no capture is open.
        :rtype: renderdoc.CaptureAccess
        """
        pass

    def GetCaptureFile(self) -> CaptureFile: # real signature unknown; restored from __doc__
        """
        GetCaptureFile()
        
        Retrieves the capture file handle for the currently open file, if it is available.
        
        If the capture is not open locally this will not be available, and only :meth:`GetCaptureAccess`
        will be usable.
        
        :return: The file handle active, or ``None`` if no capture is open or the capture is only available
          remotely.
        :rtype: renderdoc.CaptureFile
        """
        pass

    def GetCurrentProcessingTime(self) -> float: # real signature unknown; restored from __doc__
        """
        GetCurrentProcessingTime()
        
        Return the amount of time that the currently active command on the replay thread has
        been executing for.
        
        This can be used to identify if a command is long-running to display a progress bar or notification.
        
        :return: The time in seconds that the current command has been executing for, or 0.0 if no command
          is executing.
        :rtype: float
        """
        pass

    def GetHomeFolder(self, synchronous: bool, callback: DirectoryBrowseCallback): # real signature unknown; restored from __doc__
        """
        GetHomeFolder(synchronous, callback)
        
        Query the remote host for its home directory.
        
        If a capture is open, the callback will happen on the replay thread, otherwise it will happen in a
        blocking fashion on the current thread.
        
        :param bool synchronous: If a capture is open, then ``True`` will use :meth:`BlockInvoke` to call
          the callback. Otherwise if ``False`` then :meth:`AsyncInvoke` will be used.
        :param DirectoryBrowseCallback callback: The function to callback on the replay thread.
          Callback function signature must match :func:`DirectoryBrowseCallback`.
        """
        pass

    def GetRemoteSupport(self) -> List[str]: # real signature unknown; restored from __doc__
        """
        GetRemoteSupport()
        
        Retrieve a list of drivers that the current remote server supports.
        
        :return: The list of supported replay drivers.
        :rtype: List[str]
        """
        pass

    def ListFolder(self, path: str, synchronous: bool, callback: DirectoryBrowseCallback): # real signature unknown; restored from __doc__
        """
        ListFolder(path, synchronous, callback)
        
        Query the remote host for the contents of a path.
        
        If a capture is open, the callback will happen on the replay thread, otherwise it will happen in a
        blocking fashion on the current thread.
        
        :param str path: The path to query the contents of.
        :param bool synchronous: If a capture is open, then ``True`` will use :meth:`BlockInvoke` to call
          the callback. Otherwise if ``False`` then :meth:`AsyncInvoke` will be used.
        :param DirectoryBrowseCallback callback: The function to callback on the replay thread.
          Callback function signature must match :func:`DirectoryBrowseCallback`.
        """
        pass

    def PingRemote(self): # real signature unknown; restored from __doc__
        """
        PingRemote()
        
        Ping the remote server to ensure the connection is still alive.
        """
        pass

    def ShutdownServer(self): # real signature unknown; restored from __doc__
        """
        ShutdownServer()
        
        Shutdown the server the manager is currently connected to.
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


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD501412C0>, \'__hash__\': <slot wrapper \'__hash__\' of \'qrenderdoc.ReplayManager\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'qrenderdoc.ReplayManager\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'qrenderdoc.ReplayManager\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'qrenderdoc.ReplayManager\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'qrenderdoc.ReplayManager\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'qrenderdoc.ReplayManager\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'qrenderdoc.ReplayManager\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'qrenderdoc.ReplayManager\' objects>, \'DeleteCapture\': <method \'DeleteCapture\' of \'qrenderdoc.ReplayManager\' objects>, \'ConnectToRemoteServer\': <method \'ConnectToRemoteServer\' of \'qrenderdoc.ReplayManager\' objects>, \'DisconnectFromRemoteServer\': <method \'DisconnectFromRemoteServer\' of \'qrenderdoc.ReplayManager\' objects>, \'ShutdownServer\': <method \'ShutdownServer\' of \'qrenderdoc.ReplayManager\' objects>, \'PingRemote\': <method \'PingRemote\' of \'qrenderdoc.ReplayManager\' objects>, \'CancelReplayLoop\': <method \'CancelReplayLoop\' of \'qrenderdoc.ReplayManager\' objects>, \'CurrentRemote\': <method \'CurrentRemote\' of \'qrenderdoc.ReplayManager\' objects>, \'GetCaptureAccess\': <method \'GetCaptureAccess\' of \'qrenderdoc.ReplayManager\' objects>, \'GetCaptureFile\': <method \'GetCaptureFile\' of \'qrenderdoc.ReplayManager\' objects>, \'ExecuteAndInject\': <method \'ExecuteAndInject\' of \'qrenderdoc.ReplayManager\' objects>, \'GetRemoteSupport\': <method \'GetRemoteSupport\' of \'qrenderdoc.ReplayManager\' objects>, \'GetHomeFolder\': <method \'GetHomeFolder\' of \'qrenderdoc.ReplayManager\' objects>, \'ListFolder\': <method \'ListFolder\' of \'qrenderdoc.ReplayManager\' objects>, \'CopyCaptureToRemote\': <method \'CopyCaptureToRemote\' of \'qrenderdoc.ReplayManager\' objects>, \'CopyCaptureFromRemote\': <method \'CopyCaptureFromRemote\' of \'qrenderdoc.ReplayManager\' objects>, \'GetCurrentProcessingTime\': <method \'GetCurrentProcessingTime\' of \'qrenderdoc.ReplayManager\' objects>, \'AsyncInvoke\': <method \'AsyncInvoke\' of \'qrenderdoc.ReplayManager\' objects>, \'BlockInvoke\': <method \'BlockInvoke\' of \'qrenderdoc.ReplayManager\' objects>, \'__dict__\': <attribute \'__dict__\' of \'qrenderdoc.ReplayManager\' objects>, \'__doc__\': "\\nA manager for accessing the underlying replay information that isn\'t already abstracted\\nin UI side structures. This manager controls and serialises access to the underlying\\n:class:`~renderdoc.ReplayController`, as well as handling remote server connections.\\n\\nThis manager is retrieved by calling :meth:`CaptureContext.Replay`.\\n\\n.. function:: InvokeCallback(controller)\\n\\n  Not a member function - the signature for any ``InvokeCallback`` callbacks.\\n\\n  :param renderdoc.ReplayController controller: The controller to access. Must not be cached or\\n    used after the callback returns.\\n\\n.. function:: DirectoryBrowseCallback(path, entries)\\n\\n  Not a member function - the signature for any ``DirectoryBrowseCallback`` callbacks.\\n\\n  :param str path: The path that was queried for.\\n  :param List[renderdoc.PathEntry] entries: The entries underneath the path, as relevant.\\n\\n"})'


