# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class LogType(__enum.IntEnum):
    """
    The type of a log message
    
    .. data:: Debug
    
      The log message is a verbose debug-only message that can be discarded in release builds.
    
    .. data:: Comment
    
      The log message is informational.
    
    .. data:: Warning
    
      The log message describes a warning that could indicate a problem or be useful in diagnostics.
    
    .. data:: Error
    
      The log message indicates an error was encountered.
    
    .. data:: Fatal
    
      The log message indicates a fatal error occurred which is impossible to recover from.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Comment = 1
    """ The log message is informational. """

    Count = 5
    Debug = 0
    """ The log message is a verbose debug-only message that can be discarded in release builds. """

    Error = 3
    """ The log message indicates an error was encountered. """

    Fatal = 4
    """ The log message indicates a fatal error occurred which is impossible to recover from. """

    First = 0
    Warning = 2
    """ The log message describes a warning that could indicate a problem or be useful in diagnostics. """



