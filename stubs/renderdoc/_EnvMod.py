from enum import IntEnum

class EnvMod(IntEnum):
    # Original docstring
    """
    How to modify an environment variable.
    
    .. data:: Set
    
      Set the variable to the given value.
    
    .. data:: Append
    
      Add the given value to the end of the variable, using the separator.
    
    .. data:: Prepend
    
      Add the given value to the start of the variable, using the separator.
    """
    
    
    # Enum values
    
    Set = 0
    """
    Set the variable to the given value.
    """
    
    Append = 1
    """
    Add the given value to the end of the variable, using the separator.
    """
    
    Prepend = 2
    """
    Add the given value to the start of the variable, using the separator.
    """
    

# Assign __doc__ for enum values for easier introspection

EnvMod.Set.__doc__ = """
Set the variable to the given value.
"""

EnvMod.Append.__doc__ = """
Add the given value to the end of the variable, using the separator.
"""

EnvMod.Prepend.__doc__ = """
Add the given value to the start of the variable, using the separator.
"""

