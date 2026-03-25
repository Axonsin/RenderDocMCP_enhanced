# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class MessageSource(__enum.IntEnum):
    """
    Where a debug message was reported from
    
    .. data:: API
    
      This message comes from the API's debugging or validation layers.
    
    .. data:: RedundantAPIUse
    
      This message comes from detecting redundant API calls - calls with no side-effect or purpose, e.g.
      setting state that is already set.
    
    .. data:: IncorrectAPIUse
    
      This message comes from detecting incorrect use of the API.
    
    .. data:: GeneralPerformance
    
      This message comes from detecting general performance problems that are not hardware or platform
      specific.
    
    .. data:: GCNPerformance
    
      This message comes from detecting patterns that will cause performance problems on GCN-based
      hardware.
    
    .. data:: RuntimeWarning
    
      This message comes not from inspecting the log but something detected at runtime while in use,
      for example exceptions generated during shader debugging.
    
    .. data:: UnsupportedConfiguration
    
      This message comes from replaying a capture in an environment with insufficient capability to
      accurately reproduce the API work. Either this means the replay will be wrong, or it may be that
      depending on the exact API work some inaccuracies might happen.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    API = 0
    """ This message comes from the API's debugging or validation layers. """

    GCNPerformance = 4
    """
    This message comes from detecting patterns that will cause performance problems on GCN-based
      hardware.
    """

    GeneralPerformance = 3
    """
    This message comes from detecting general performance problems that are not hardware or platform
      specific.
    """

    IncorrectAPIUse = 2
    """ This message comes from detecting incorrect use of the API. """

    RedundantAPIUse = 1
    """
    This message comes from detecting redundant API calls - calls with no side-effect or purpose, e.g.
      setting state that is already set.
    """

    RuntimeWarning = 5
    """
    This message comes not from inspecting the log but something detected at runtime while in use,
      for example exceptions generated during shader debugging.
    """

    UnsupportedConfiguration = 6
    """
    This message comes from replaying a capture in an environment with insufficient capability to
      accurately reproduce the API work. Either this means the replay will be wrong, or it may be that
      depending on the exact API work some inaccuracies might happen.
    """



