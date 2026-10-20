from enum import IntFlag

class PathProperty(IntFlag):
    # Original docstring
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
    
    
    # Enum values
    
    NoFlags = 0
    """
    No special file properties.
    """
    
    Directory = 1
    """
    This file is a directory or folder.
    """
    
    Hidden = 2
    """
    This file is considered hidden by the filesystem.
    """
    
    Executable = 4
    """
    This file has been identified as an executable program or script.
    """
    
    ErrorUnknown = 8192
    """
    A special flag indicating that a query for this file failed, but for unknown reasons.
    """
    
    ErrorAccessDenied = 16384
    """
    A special flag indicating that a query for this file failed because access to the path was
    denied.
    """
    
    ErrorInvalidPath = 32768
    """
    A special flag indicating that a query for this file failed because the path was invalid.
    """
    

# Assign __doc__ for enum values for easier introspection

PathProperty.NoFlags.__doc__ = """
No special file properties.
"""

PathProperty.Directory.__doc__ = """
This file is a directory or folder.
"""

PathProperty.Hidden.__doc__ = """
This file is considered hidden by the filesystem.
"""

PathProperty.Executable.__doc__ = """
This file has been identified as an executable program or script.
"""

PathProperty.ErrorUnknown.__doc__ = """
A special flag indicating that a query for this file failed, but for unknown reasons.
"""

PathProperty.ErrorAccessDenied.__doc__ = """
A special flag indicating that a query for this file failed because access to the path was
denied.
"""

PathProperty.ErrorInvalidPath.__doc__ = """
A special flag indicating that a query for this file failed because the path was invalid.
"""

