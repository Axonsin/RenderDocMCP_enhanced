# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class MessageSeverity(__enum.IntEnum):
    """
    How serious a debug message is
    
    .. data:: High
    
      This message is very serious, indicating a guaranteed problem or major flaw.
    
    .. data:: Medium
    
      This message is somewhat serious, indicating a problem that should be addressed or investigated.
    
    .. data:: Low
    
      This message is not very serious. This indicates something that might indicate a problem.
    
    .. data:: Info
    
      This message is not about a problem but is purely informational.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    High = 0
    """ This message is very serious, indicating a guaranteed problem or major flaw. """

    Info = 3
    """ This message is not about a problem but is purely informational. """

    Low = 2
    """ This message is not very serious. This indicates something that might indicate a problem. """

    Medium = 1
    """ This message is somewhat serious, indicating a problem that should be addressed or investigated. """



