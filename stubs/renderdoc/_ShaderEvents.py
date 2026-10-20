from enum import IntFlag

class ShaderEvents(IntFlag):
    # Original docstring
    """
    A set of flags for events that may occur while debugging a shader
    
    .. data:: NoEvent
    
      No event has occurred.
    
    .. data:: SampleLoadGather
    
      A texture was sampled, loaded or gathered.
    
    .. data:: GeneratedNanOrInf
    
      A floating point operation generated a ``NaN`` or ``infinity`` result.
    
    .. data:: DebugBreak
    
      A ``debugbreak()`` event was emitted.
    """
    
    
    # Enum values
    
    NoEvent = 0
    """
    No event has occurred.
    """
    
    SampleLoadGather = 1
    """
    A texture was sampled, loaded or gathered.
    """
    
    GeneratedNanOrInf = 2
    """
    A floating point operation generated a ``NaN`` or ``infinity`` result.
    """
    
    DebugBreak = 4
    """
    A ``debugbreak()`` event was emitted.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderEvents.NoEvent.__doc__ = """
No event has occurred.
"""

ShaderEvents.SampleLoadGather.__doc__ = """
A texture was sampled, loaded or gathered.
"""

ShaderEvents.GeneratedNanOrInf.__doc__ = """
A floating point operation generated a ``NaN`` or ``infinity`` result.
"""

ShaderEvents.DebugBreak.__doc__ = """
A ``debugbreak()`` event was emitted.
"""

