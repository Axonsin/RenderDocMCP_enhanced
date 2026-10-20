from enum import IntEnum

class DebugVariableType(IntEnum):
    # Original docstring
    """
    Represents the category of debugging variable that a source variable maps to.
    
    .. data:: Undefined
    
      Undefined type.
    
    .. data:: Input
    
      A constant input value, stored globally.
    
    .. data:: Constant
    
      A constant buffer value, stored globally.
    
    .. data:: Sampler
    
      A sampler, stored globally.
    
    .. data:: ReadOnlyResource
    
      A read-only resource, stored globally.
    
    .. data:: ReadWriteResource
    
      A read-write resource, stored globally.
    
    .. data:: Variable
    
      A mutable variable, stored per state.
    """
    
    
    # Enum values
    
    Undefined = 0
    """
    Undefined type.
    """
    
    Input = 1
    """
    A constant input value, stored globally.
    """
    
    Constant = 2
    """
    A constant buffer value, stored globally.
    """
    
    Sampler = 3
    """
    A sampler, stored globally.
    """
    
    ReadOnlyResource = 4
    """
    A read-only resource, stored globally.
    """
    
    ReadWriteResource = 5
    """
    A read-write resource, stored globally.
    """
    
    Variable = 6
    """
    A mutable variable, stored per state.
    """
    

# Assign __doc__ for enum values for easier introspection

DebugVariableType.Undefined.__doc__ = """
Undefined type.
"""

DebugVariableType.Input.__doc__ = """
A constant input value, stored globally.
"""

DebugVariableType.Constant.__doc__ = """
A constant buffer value, stored globally.
"""

DebugVariableType.Sampler.__doc__ = """
A sampler, stored globally.
"""

DebugVariableType.ReadOnlyResource.__doc__ = """
A read-only resource, stored globally.
"""

DebugVariableType.ReadWriteResource.__doc__ = """
A read-write resource, stored globally.
"""

DebugVariableType.Variable.__doc__ = """
A mutable variable, stored per state.
"""

