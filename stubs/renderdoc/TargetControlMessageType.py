# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TargetControlMessageType(__enum.IntEnum):
    """
    The type of message received from or sent to an application target control connection.
    
    .. data:: Unknown
    
      No message or an unknown message type.
    
    .. data:: Disconnected
    
      The other end of the connection disconnected.
    
    .. data:: Busy
    
      The other end of the connection was busy.
    
    .. data:: Noop
    
      Nothing happened, the connection is being kept alive.
    
    .. data:: NewCapture
    
      A new capture was made.
    
    .. data:: CaptureCopied
    
      A capture was successfully copied across the connection.
    
    .. data:: RegisterAPI
    
      The target has initialised a graphics API.
    
    .. data:: NewChild
    
      The target has created a child process.
    
    .. data:: CaptureProgress
    
      Progress update on an on-going frame capture.
    
    .. data:: CapturableWindowCount
    
      The number of capturable windows has changed.
    
    .. data:: RequestShow
    
      The client has requested that the controller show itself (raise its window to the top).
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Busy = 2
    """ The other end of the connection was busy. """

    CapturableWindowCount = 9
    """ The number of capturable windows has changed. """

    CaptureCopied = 5
    """ A capture was successfully copied across the connection. """

    CaptureProgress = 8
    """ Progress update on an on-going frame capture. """

    Disconnected = 1
    """ The other end of the connection disconnected. """

    NewCapture = 4
    """ A new capture was made. """

    NewChild = 7
    """ The target has created a child process. """

    Noop = 3
    """ Nothing happened, the connection is being kept alive. """

    RegisterAPI = 6
    """ The target has initialised a graphics API. """

    RequestShow = 10
    """ The client has requested that the controller show itself (raise its window to the top). """

    Unknown = 0
    """ No message or an unknown message type. """



