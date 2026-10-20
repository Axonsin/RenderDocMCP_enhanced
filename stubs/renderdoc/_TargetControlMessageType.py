from enum import IntEnum

class TargetControlMessageType(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    Unknown = 0
    """
    No message or an unknown message type.
    """
    
    Disconnected = 1
    """
    The other end of the connection disconnected.
    """
    
    Busy = 2
    """
    The other end of the connection was busy.
    """
    
    Noop = 3
    """
    Nothing happened, the connection is being kept alive.
    """
    
    NewCapture = 4
    """
    A new capture was made.
    """
    
    CaptureCopied = 5
    """
    A capture was successfully copied across the connection.
    """
    
    RegisterAPI = 6
    """
    The target has initialised a graphics API.
    """
    
    NewChild = 7
    """
    The target has created a child process.
    """
    
    CaptureProgress = 8
    """
    Progress update on an on-going frame capture.
    """
    
    CapturableWindowCount = 9
    """
    The number of capturable windows has changed.
    """
    
    RequestShow = 10
    """
    The client has requested that the controller show itself (raise its window to the top).
    """
    

# Assign __doc__ for enum values for easier introspection

TargetControlMessageType.Unknown.__doc__ = """
No message or an unknown message type.
"""

TargetControlMessageType.Disconnected.__doc__ = """
The other end of the connection disconnected.
"""

TargetControlMessageType.Busy.__doc__ = """
The other end of the connection was busy.
"""

TargetControlMessageType.Noop.__doc__ = """
Nothing happened, the connection is being kept alive.
"""

TargetControlMessageType.NewCapture.__doc__ = """
A new capture was made.
"""

TargetControlMessageType.CaptureCopied.__doc__ = """
A capture was successfully copied across the connection.
"""

TargetControlMessageType.RegisterAPI.__doc__ = """
The target has initialised a graphics API.
"""

TargetControlMessageType.NewChild.__doc__ = """
The target has created a child process.
"""

TargetControlMessageType.CaptureProgress.__doc__ = """
Progress update on an on-going frame capture.
"""

TargetControlMessageType.CapturableWindowCount.__doc__ = """
The number of capturable windows has changed.
"""

TargetControlMessageType.RequestShow.__doc__ = """
The client has requested that the controller show itself (raise its window to the top).
"""

