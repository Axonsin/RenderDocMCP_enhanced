from ._CaptureAccess import CaptureAccess
from ._CaptureOptions import CaptureOptions
from ._EnvironmentModification import EnvironmentModification
from ._ExecuteResult import ExecuteResult
from ._PathEntry import PathEntry
from ._ReplayController import ReplayController
from ._ReplayOptions import ReplayOptions
from ._ResultDetails import ResultDetails
from typing import Callable, List, Tuple

class RemoteServer(CaptureAccess):
    # Original docstring
    """
    A connection to a running remote RenderDoc server on another machine. This allows the
    transfer of captures to and from the local machine, as well as remotely replaying a capture with a
    local proxy renderer, so that captures that are not supported locally can still be debugged with as
    much work as possible happening on the local machine.
    
    .. data:: NoPreference
    
      No preference for a particular value, see :meth:`ReplayController.DebugPixel`.
    """
    
    
    NoPreference = 4294967295
    """
    No preference for a particular value, see :meth:`ReplayController.DebugPixel`.
    """
    
    
    def ShutdownConnection(self):
        """
        Closes the connection without affecting the running server.
        """
        pass
    
    
    def ShutdownServerAndConnection(self):
        """
        Closes the connection and also tells the running server to close.
        """
        pass
    
    
    def Ping(self) -> ResultDetails:
        """
        Pings the remote server to ensure the connection is still alive.
        
        :return: The result of the operation - if a failure occurred the connection is no longer alive.
        :rtype: ResultDetails
        """
        pass
    
    
    def LocalProxies(self) -> List[str]:
        """
        Retrieve a list of renderers available for local proxying.
        
        These will be strings like "D3D11" or "OpenGL".
        
        :return: A list of names of the local proxies.
        :rtype: List[str]
        """
        pass
    
    
    def RemoteSupportedReplays(self) -> List[str]:
        """
        Retrieve a list of renderers supported by the remote server.
        
        These will be strings like "D3D11" or "OpenGL".
        
        :return: A list of names of the remote renderers.
        :rtype: List[str]
        """
        pass
    
    
    def GetHomeFolder(self) -> str:
        """
        Retrieve the path on the remote system where browsing can begin.
        
        :return: The 'home' path where browsing for files or folders can begin.
        :rtype: str
        """
        pass
    
    
    def ListFolder(self, path: str) -> List[PathEntry]:
        """
        Retrieve the contents of a folder path on the remote system.
        
        If an error occurs, a single :class:`PathEntry` will be returned with appropriate error flags.
        
        :param str path: The remote path to list.
        :return: The contents of the specified folder.
        :rtype: List[PathEntry]
        """
        pass
    
    
    def ExecuteAndInject(self, app: str, workingDir: str, cmdLine: str, env: List[EnvironmentModification], opts: CaptureOptions) -> ExecuteResult:
        """
        Launch an application and inject into it to allow capturing.
        
        This happens on the remote system, so all paths are relative to the remote filesystem.
        
        :param str app: The path to the application to run.
        :param str workingDir: The working directory to use when running the application. If blank, the
          directory containing the application is used.
        :param str cmdLine: The command line to use when running the application, it will be processed in a
          platform specific way to generate arguments.
        :param List[EnvironmentModification] env: Any environment changes that should be made when running
          the program.
        :param CaptureOptions opts: The capture options to use when injecting into the program.
        :return: The :class:`ExecuteResult` indicating both the status of the operation (success or failure)
          and any reason for failure, or else the ident where the new application is listening for target
          control if everything succeeded.
        :rtype: ExecuteResult
        """
        pass
    
    
    def TakeOwnershipCapture(self, filename: str):
        """
        Take ownership over a capture file.
        
        Initially when a capture is made, it is owned by the injected library in the application. It passes
        ownership to any program that is connected via target control that is notified about the capture,
        which is then responsible for either saving the file or deleting it if it's unwanted.
        
        Passing ownership of a file to the remote server means that it will be kept around for future use
        until the server closes, at which point it will delete any files it owns.
        
        :param str filename: The remote path to take ownership of.
        """
        pass
    
    
    def CopyCaptureToRemote(self, filename: str, progress: Callable[[float], None]) -> str:
        """
        Copy a capture file that is stored on the local system to the remote system.
        
        This function will block until the copy is fully complete, or an error has occurred.
        
        This is primarily useful for when a capture is only stored locally and must be replayed remotely, as
        the capture must be available on the machine where the replay happens.
        
        :param str filename: The path to the file on the local system.
        :param Callable[[float], None] progress: A callback that will be repeatedly called with an updated progress
          value for the copy. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The path on the remote system where the capture was saved temporarily.
        :rtype: str
        """
        pass
    
    
    def CopyCaptureFromRemote(self, remotepath: str, localpath: str, progress: Callable[[float], None]):
        """
        Copy a capture file that is stored on the remote system to the local system.
        
        This function will block until the copy is fully complete, or an error has occurred.
        
        :param str remotepath: The remote path where the file should be copied from.
        :param str localpath: The local path where the file should be saved.
        :param Callable[[float], None] progress: A callback that will be repeatedly called with an updated progress
          value for the copy. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        """
        pass
    
    
    def OpenCapture(self, proxyid: int, filename: str, opts: ReplayOptions, progress: Callable[[float], None]) -> Tuple[ResultDetails, ReplayController]:
        """
        Open a capture file for remote capture and replay. The capture will be opened and
        replayed on the remote system, and proxied to the local system with a given renderer. As much work
        as possible will happen locally to save on bandwidth, processing and latency.
        
        This function will block until the capture is fully opened on the remote system and ready for use,
        or an error has occurred.
        
        .. note:: You *must* close the resulting :class:`ReplayController` with the :meth:`CloseCapture`
          function to ensure the local proxy is correctly tidied up, instead of using
          :meth:`ReplayController.Shutdown`.
        
        :param int proxyid: The index in the array returned by :meth:`LocalProxies` to use as a local proxy,
          or :data:`NoPreference` to indicate no preference for any proxy.
        :param str filename: The path on the remote system where the file is. If the file is only available
          locally you can use :meth:`CopyCaptureToRemote` to transfer it over the remote connection.
        :param ReplayOptions opts: The options controlling how the capture should be replayed.
        :param Callable[[float], None] progress: A callback that will be repeatedly called with an updated progress
          value for the opening. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: A tuple containing the status of opening the capture, whether success or failure, and the
          resulting :class:`ReplayController` handle if successful.
        :rtype: Tuple[ResultDetails,ReplayController]
        """
        pass
    
    
    def CloseCapture(self, rend: ReplayController):
        """
        Close a capture analysis handle previously opened by :meth:`OpenCapture`.
        
        :param ReplayController rend: The ReplayController that is to be closed.
        """
        pass
    
