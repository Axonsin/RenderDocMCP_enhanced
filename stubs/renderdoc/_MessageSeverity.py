from enum import IntEnum

class MessageSeverity(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    High = 0
    """
    This message is very serious, indicating a guaranteed problem or major flaw.
    """
    
    Medium = 1
    """
    This message is somewhat serious, indicating a problem that should be addressed or investigated.
    """
    
    Low = 2
    """
    This message is not very serious. This indicates something that might indicate a problem.
    """
    
    Info = 3
    """
    This message is not about a problem but is purely informational.
    """
    

# Assign __doc__ for enum values for easier introspection

MessageSeverity.High.__doc__ = """
This message is very serious, indicating a guaranteed problem or major flaw.
"""

MessageSeverity.Medium.__doc__ = """
This message is somewhat serious, indicating a problem that should be addressed or investigated.
"""

MessageSeverity.Low.__doc__ = """
This message is not very serious. This indicates something that might indicate a problem.
"""

MessageSeverity.Info.__doc__ = """
This message is not about a problem but is purely informational.
"""

