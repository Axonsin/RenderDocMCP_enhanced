from ._ConnectedTempCapture import ConnectedTempCapture
from typing import Callable, List

# Dummy types
from . import QWidget

class CaptureConnection():
    # Original docstring
    """
    A capture connection window.
    
    When a program is successfully launched by :class:`CaptureDialog` and a connection is made,
    this window can be used to access the details of that connection and any captures that have
    been made.
    
    .. function:: ClosedCallback(connection)
    
      Not a member function - the signature for any ``ClosedCallback`` callbacks.
    
      Called whenever a capture connection is closed.
    
      :param CaptureConnection connection: The connection window. Invalid to use after the callback
         has returned.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`CaptureConnection` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def RegisterClosedCallback(self, method: Callable[['CaptureConnection'], None]):
        """
        Register a callback to be called when the connection window is closed for any reason.
        
        Because capture connections can self-close when a program exits with no captures having been made, it can
        be useful to get a callback to notify you that the connection is no longer legal to use.
        
        This callback happens on the UI thread.
        
        :param Callable[[CaptureConnection], None] method: The function to callback when closed.
          Callback function signature must match :func:`ClosedCallback`.
        """
        pass
    
    
    def IsConnected(self) -> bool:
        """
        Checks whether or not the connection is still active. If a program exits the connection
        will no longer be active.
        
        Note that there is an inherent race here - the connection could drop immediately after returning.
        
        :return: ``True`` if the window is set up for injecting.
        :rtype: bool
        """
        pass
    
    
    def PreventAutoClose(self):
        """
        Normally connection windows will self-close if the program exits and there are no captures
        made. This behaviour can be disabled by calling this function at which point the window will not close
        itself automatically.
        """
        pass
    
    
    def GetAPIs(self) -> List[str]:
        """
        Lists the names of APIs that have been used in the program. These APIs may not all
        be actively in use, as APIs are not removed from this list once they have been observed.
        
        Note that some APIs may be listed here that RenderDoc does not support, but does recognise. You
        should not assume that these names will match those in the :class:`~renderdoc.GraphicsAPI` enum.
        
        :return: The set of API names that have been used in the program.
        :rtype: List[str]
        """
        pass
    
    
    def QueueCapture(self, frameNumber: int, numFrames: int):
        """
        Asks the connected program to take captures beginning at a certain frame
        number.
        
        If the frame number has already passed when the request is received, no capture is made.
        
        :param int frameNumber: The first frame number to capture.
        :param int numFrames: How many frames to capture including the first. If set to 0, nothing
          is captured.
        """
        pass
    
    
    def TimedCapture(self, secondsDelay: float, numFrames: int):
        """
        Asks the connected program to take a capture after a certain number
        of seconds have passed, possibly 0 seconds to immediately capture. This has no effect
        if the connection is inactive and does not guarantee that the program will still be
        connected in the future - if the connection is lost no capture is made.
        
        While a delayed capture is waiting to be triggered, requests to trigger another delayed
        capture will be ignored. Only one can be active at once. If you need more complex or
        overlapping delayed captures you should do this yourself manually and call this function
        when each one is due.
        
        :param float secondsDelay: How many seconds to wait before triggering a capture.
        :param int numFrames: How many frames to capture including the first. If set to 0, nothing
          is captured.
        """
        pass
    
    
    def CycleActiveWindow(self):
        """
        Cycles which window is active on the connected device. Has no effect if there are
        not multiple windows or if the connection is inactive.
        """
        pass
    
    
    def Target(self) -> str:
        """
        Gets the name of the program connected to. Usually the name of the
        executable for the process.
        
        :return: The connection target.
        :rtype: str
        """
        pass
    
    
    def Hostname(self) -> str:
        """
        Gets the raw hostname for the connected target. This can be used elsewhere
        as a true hostname. For displaying to the user, prefer :meth:`FriendlyHostname`.
        
        :return: The raw hostname of the target this connection is to.
        :rtype: str
        """
        pass
    
    
    def FriendlyHostname(self) -> str:
        """
        Gets the user friendly hostname for the connected target. This may not be
        a true hostname but is suitable for displaying to users particularly for platforms where
        the raw hostname is not necessarily user-friendly and there may be a more descriptive name
        available.
        
        :return: The friendly hostname of the target this connection is to.
        :rtype: str
        """
        pass
    
    
    def Close(self, discardUnsaved: bool):
        """
        Closes the connection to the target program. Normally there will be
        a prompt to the user to ask them whether they would like to save any unsaved
        captures to prevent data loss. If they choose to cancel, the connection may not
        be closed.
        
        This prompt can be overridden with the parameter, at which point all unsaved captures
        will be deleted. You should ensure the user understands that this will happen.
        
        :param bool discardUnsaved: Whether to discard unsaved captures without prompting.
        """
        pass
    
    
    def GetCaptures(self) -> List[ConnectedTempCapture]:
        """
        Lists the captures that are known to have been made on this connection. Note
        that this reflects the UI and so the user is free to delete captures at any point, which
        will be reflected by them being removed from this list.
        
        Each :class:`capture <ConnectedTempCapture>` has an ID that is used to refer to it, note
        that this ID is not globally unique and is only unique within this connection.
        
        :return: The currently known captures on this connection.
        :rtype: List[ConnectedTempCapture]
        """
        pass
    
    
    def OpenCapture(self, ID: int):
        """
        Open the given capture, referred to by ID, in the UI for analysis. If the
        capture is remote, an appropriate remote host connection is required.
        
        This will prompt the user for closing any currently open capture and if the user
        chooses not to close the current capture the loading will be stopped.
        
        :param int ID: The ID of the capture to open.
        """
        pass
    
    
    def DeleteCapture(self, ID: int, promptForSave: bool):
        """
        Delete the given capture, referred to by ID. If the
        capture is remote, an appropriate remote host connection is required.
        
        Normally deleting a capture will prompt the user to prevent data loss, but this can be
        overridden with the argument.
        
        :param int ID: The ID of the capture to delete.
        :param bool promptForSave: ``True`` if the user should be prompted as normal to save the
          capture.
        """
        pass
    
    
    def SaveCapture(self, ID: int, filename: str = ""):
        """
        Save the given capture to disk, referred to by ID. If the
        capture is remote, an appropriate remote host connection is required.
        
        If the filename is omitted the user will be prompted to choose a file and the capture
        will only be saved if they select a filename.
        
        :param int ID: The ID of the capture to delete.
        :param str filename="": **Optional parameter**. The filename to save to on the local disk,
          if omitted the user will be prompted to choose a filename.
        """
        pass
    
    
    def GetChildProcesses(self) -> List[int]:
        """
        Lists the PIDs of child processes that are known to still be running.
        
        :return: The PIDs of each child process running under the connected program.
        :rtype: List[int]
        """
        pass
    
    
    def ConnectToChild(self, pid: int) -> 'CaptureConnection':
        """
        Connected to a given child process and return a connection window.
        
        The connection window will automatically be shown if the connection is successfully made.
        
        If the PID is unrecognised, no connection will be made.
        
        :param int pid: The PID of the child to connect to.
        :return: The connection window if successful, or ``None`` if no connection was made.
        :rtype: CaptureConnection
        """
        pass
    
