from enum import IntEnum

class MessageSource(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    API = 0
    """
    This message comes from the API's debugging or validation layers.
    """
    
    RedundantAPIUse = 1
    """
    This message comes from detecting redundant API calls - calls with no side-effect or purpose, e.g.
    setting state that is already set.
    """
    
    IncorrectAPIUse = 2
    """
    This message comes from detecting incorrect use of the API.
    """
    
    GeneralPerformance = 3
    """
    This message comes from detecting general performance problems that are not hardware or platform
    specific.
    """
    
    GCNPerformance = 4
    """
    This message comes from detecting patterns that will cause performance problems on GCN-based
    hardware.
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
    

# Assign __doc__ for enum values for easier introspection

MessageSource.API.__doc__ = """
This message comes from the API's debugging or validation layers.
"""

MessageSource.RedundantAPIUse.__doc__ = """
This message comes from detecting redundant API calls - calls with no side-effect or purpose, e.g.
setting state that is already set.
"""

MessageSource.IncorrectAPIUse.__doc__ = """
This message comes from detecting incorrect use of the API.
"""

MessageSource.GeneralPerformance.__doc__ = """
This message comes from detecting general performance problems that are not hardware or platform
specific.
"""

MessageSource.GCNPerformance.__doc__ = """
This message comes from detecting patterns that will cause performance problems on GCN-based
hardware.
"""

MessageSource.RuntimeWarning.__doc__ = """
This message comes not from inspecting the log but something detected at runtime while in use,
for example exceptions generated during shader debugging.
"""

MessageSource.UnsupportedConfiguration.__doc__ = """
This message comes from replaying a capture in an environment with insufficient capability to
accurately reproduce the API work. Either this means the replay will be wrong, or it may be that
depending on the exact API work some inaccuracies might happen.
"""

