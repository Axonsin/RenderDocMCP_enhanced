from enum import IntEnum

class LogType(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    Debug = 0
    """
    The log message is a verbose debug-only message that can be discarded in release builds.
    """
    
    Comment = 1
    """
    The log message is informational.
    """
    
    Warning = 2
    """
    The log message describes a warning that could indicate a problem or be useful in diagnostics.
    """
    
    Error = 3
    """
    The log message indicates an error was encountered.
    """
    
    Fatal = 4
    """
    The log message indicates a fatal error occurred which is impossible to recover from.
    """
    
    Count = 5
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

LogType.Debug.__doc__ = """
The log message is a verbose debug-only message that can be discarded in release builds.
"""

LogType.Comment.__doc__ = """
The log message is informational.
"""

LogType.Warning.__doc__ = """
The log message describes a warning that could indicate a problem or be useful in diagnostics.
"""

LogType.Error.__doc__ = """
The log message indicates an error was encountered.
"""

LogType.Fatal.__doc__ = """
The log message indicates a fatal error occurred which is impossible to recover from.
"""

LogType.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

LogType.First.__doc__ = """
The first enum value, for ease of iteration.
"""

