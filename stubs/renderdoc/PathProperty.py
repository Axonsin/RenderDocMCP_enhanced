# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PathProperty(__enum.IntFlag):
    """
    A set of flags describing the properties of a path on a remote filesystem.
    
    .. data:: NoFlags
    
      No special file properties.
    
    .. data:: Directory
    
      This file is a directory or folder.
    
    .. data:: Hidden
    
      This file is considered hidden by the filesystem.
    
    .. data:: Executable
    
      This file has been identified as an executable program or script.
    
    .. data:: ErrorUnknown
    
      A special flag indicating that a query for this file failed, but for unknown reasons.
    
    .. data:: ErrorAccessDenied
    
      A special flag indicating that a query for this file failed because access to the path was
      denied.
    
    .. data:: ErrorInvalidPath
    
      A special flag indicating that a query for this file failed because the path was invalid.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Directory = 1
    """ This file is a directory or folder. """

    ErrorAccessDenied = 16384
    """
    A special flag indicating that a query for this file failed because access to the path was
      denied.
    """

    ErrorInvalidPath = 32768
    """ A special flag indicating that a query for this file failed because the path was invalid. """

    ErrorUnknown = 8192
    """ A special flag indicating that a query for this file failed, but for unknown reasons. """

    Executable = 4
    """ This file has been identified as an executable program or script. """

    Hidden = 2
    """ This file is considered hidden by the filesystem. """

    NoFlags = 0
    """ No special file properties. """



