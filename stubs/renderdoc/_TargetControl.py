from ._TargetControlMessage import TargetControlMessage
from typing import Callable

class TargetControl():
    # Original docstring
    """
    A connection to a running application with RenderDoc injected, which allows limited
    control over the capture process as well as querying the current status.
    """
    
    
    
    def Shutdown(self):
        """
        Closes the connection without affecting the running application.
        """
        pass
    
    
    def Connected(self) -> bool:
        """
        Determines if the connection is still alive.
        
        :return: ``True`` if the connection still appears to be working, ``False`` if it has been closed.
        :rtype: bool
        """
        pass
    
    
    def GetTarget(self) -> str:
        """
        Retrieves the target's name or identifier - typically the name of the executable.
        
        :return: The target name.
        :rtype: str
        """
        pass
    
    
    def GetAPI(self) -> str:
        """
        Retrieves the API currently in use by the target.
        
        :return: The API name, or empty if no API is initialised yet.
        :rtype: str
        """
        pass
    
    
    def GetPID(self) -> int:
        """
        Retrieves the Process ID (PID) of the target on its local system.
        
        :return: The Process ID, or 0 if that's not applicable on the target platform.
        :rtype: int
        """
        pass
    
    
    def GetBusyClient(self) -> str:
        """
        If a busy message was received, determine the client keeping the target busy.
        
        :return: The name of the client currently connected to the target.
        :rtype: str
        """
        pass
    
    
    def TriggerCapture(self, numFrames: int):
        """
        Trigger a capture on the target, with the same semantics as if the capture key had
        been pressed - from the next presentation call after this message is processed on the target to the
        next after that.
        
        :param int numFrames: How many frames to capture. These will be captured sequentially and
          independently to separate files.
        """
        pass
    
    
    def QueueCapture(self, frameNumber: int, numFrames: int):
        """
        Queue up a capture to happen on a particular frame number. When this frame is about to
        begin a capture is begun, and it ends when this frame number ends.
        
        .. note:: Frame 0 is defined as starting when the device is created, up to the first swapchain
          present defined frame boundary.
        
        :param int frameNumber: The number of the frame to capture on.
        :param int numFrames: How many frames to capture. These will be captured sequentially and
          independently to separate files.
        """
        pass
    
    
    def CopyCapture(self, captureId: int, localpath: str):
        """
        Begin copying a given capture stored on a remote machine to the local machine over the
        target control connection.
        
        :param int captureId: The identifier of the remote capture.
        :param str localpath: The absolute path on the local system where the file should be saved.
        """
        pass
    
    
    def DeleteCapture(self, captureId: int):
        """
        Delete a capture from the remote machine.
        
        :param int captureId: The identifier of the remote capture.
        """
        pass
    
    
    def ReceiveMessage(self, progress: Callable[[float], None]) -> TargetControlMessage:
        """
        Query to see if a message has been received from the remote system.
        
        The details of the types of messages that can be received are listed under
        :class:`TargetControlMessage`.
        
        .. note:: If no message has been received, this function will pump the connection. You are expected
          to continually call this function and process any messages to keep the connection alive.
        
          This function will block but only to a limited degree. If no message is waiting after a small time
          it will return with a No-op message to allow further processing.
        
        :param Callable[[float], None] progress: A callback that will be repeatedly called with an updated progress
          value when a long blocking message is coming through, e.g. a capture copy. Can be ``None`` if no
          progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The message that was received.
        :rtype: TargetControlMessage
        """
        pass
    
    
    def CycleActiveWindow(self):
        """
        Cycle the currently active window if there are more windows to capture.
        """
        pass
    
