from enum import IntEnum

class EnvSep(IntEnum):
    # Original docstring
    """
    The separator to use if needed when modifying an environment variable.
    
    .. data:: Platform
    
      Use the character appropriate for separating items on the platform.
    
      On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
      ``:`` character will be used.
    
    .. data:: SemiColon
    
      Use a semi-colon ``;`` character.
    
    .. data:: Colon
    
      Use a colon ``:`` character.
    
    .. data:: NoSep
    
      No separator will be used.
    """
    
    
    # Enum values
    
    Platform = 0
    """
    Use the character appropriate for separating items on the platform.
    
    On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
    ``:`` character will be used.
    """
    
    SemiColon = 1
    """
    Use a semi-colon ``;`` character.
    """
    
    Colon = 2
    """
    Use a colon ``:`` character.
    """
    
    NoSep = 3
    """
    No separator will be used.
    """
    

# Assign __doc__ for enum values for easier introspection

EnvSep.Platform.__doc__ = """
Use the character appropriate for separating items on the platform.

On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
``:`` character will be used.
"""

EnvSep.SemiColon.__doc__ = """
Use a semi-colon ``;`` character.
"""

EnvSep.Colon.__doc__ = """
Use a colon ``:`` character.
"""

EnvSep.NoSep.__doc__ = """
No separator will be used.
"""

