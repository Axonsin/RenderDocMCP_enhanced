from enum import IntFlag

class AndroidFlags(IntFlag):
    # Original docstring
    """
    INTERNAL: A set of flags giving details of the current status of Android tracability.
    
    .. data:: NoFlags
    
      There are no problems with the Android application setup.
    
    .. data:: Debuggable
    
      The application is debuggable.
    
    .. data:: RootAccess
    
       The device being targeted has root access.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    There are no problems with the Android application setup.
    """
    
    Debuggable = 1
    """
    The application is debuggable.
    """
    
    RootAccess = 2
    """
    The device being targeted has root access.
    """
    

# Assign __doc__ for enum values for easier introspection

AndroidFlags.NoFlags.__doc__ = """
There are no problems with the Android application setup.
"""

AndroidFlags.Debuggable.__doc__ = """
The application is debuggable.
"""

AndroidFlags.RootAccess.__doc__ = """
The device being targeted has root access.
"""

