from enum import IntEnum

class TimeUnit(IntEnum):
    # Original docstring
    """
    The unit that GPU durations are displayed in.
    
    .. data:: Seconds
    
      The durations are displayed as seconds (``s``).
    
    .. data:: Milliseconds
    
      The durations are displayed as milliseconds (``ms``).
    
    .. data:: Microseconds
    
      The durations are displayed as microseconds (``µs``).
    
    .. data:: Nanoseconds
    
      The durations are displayed as nanoseconds (``ns``).
    """
    
    
    # Enum values
    
    Seconds = 0
    """
    The durations are displayed as seconds (``s``).
    """
    
    Milliseconds = 1
    """
    The durations are displayed as milliseconds (``ms``).
    """
    
    Microseconds = 2
    """
    The durations are displayed as microseconds (``µs``).
    """
    
    Nanoseconds = 3
    """
    The durations are displayed as nanoseconds (``ns``).
    """
    
    Count = 4
    """
    The number of values in the enum, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

TimeUnit.Seconds.__doc__ = """
The durations are displayed as seconds (``s``).
"""

TimeUnit.Milliseconds.__doc__ = """
The durations are displayed as milliseconds (``ms``).
"""

TimeUnit.Microseconds.__doc__ = """
The durations are displayed as microseconds (``µs``).
"""

TimeUnit.Nanoseconds.__doc__ = """
The durations are displayed as nanoseconds (``ns``).
"""

TimeUnit.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

