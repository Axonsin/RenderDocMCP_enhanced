from enum import IntEnum

class ReplaySupport(IntEnum):
    # Original docstring
    """
    How supported a given API is on a particular replay instance.
    
    .. data:: Unsupported
    
      The API is not supported.
    
    .. data:: Supported
    
      The API is fully supported.
    
    .. data:: SuggestRemote
    
      The API is supported locally but the capture indicates it was made on a different type of machine
      so remote replay might be desired.
    """
    
    
    # Enum values
    
    Unsupported = 0
    """
    The API is not supported.
    """
    
    Supported = 1
    """
    The API is fully supported.
    """
    
    SuggestRemote = 2
    """
    The API is supported locally but the capture indicates it was made on a different type of machine
    so remote replay might be desired.
    """
    

# Assign __doc__ for enum values for easier introspection

ReplaySupport.Unsupported.__doc__ = """
The API is not supported.
"""

ReplaySupport.Supported.__doc__ = """
The API is fully supported.
"""

ReplaySupport.SuggestRemote.__doc__ = """
The API is supported locally but the capture indicates it was made on a different type of machine
so remote replay might be desired.
"""

