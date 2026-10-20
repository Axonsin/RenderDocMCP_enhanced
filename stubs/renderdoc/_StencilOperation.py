from enum import IntEnum

class StencilOperation(IntEnum):
    # Original docstring
    """
    A stencil operation to apply in stencil processing.
    
    .. data:: Keep
    
      Keep the existing value unmodified.
    
    .. data:: Zero
    
      Set the value to ``0``.
    
    .. data:: Replace
    
      Replace the value with the stencil reference value.
    
    .. data:: IncSat
    
      Increment the value but saturate at the maximum representable value (typically ``255``).
    
    .. data:: DecSat
    
      Decrement the value but saturate at ``0``.
    
    .. data:: IncWrap
    
      Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``.
    
    .. data:: DecWrap
    
      Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``).
    
    .. data:: Invert
    
      Invert the bits in the stencil value (bitwise ``NOT``).
    """
    
    
    # Enum values
    
    Keep = 0
    """
    Keep the existing value unmodified.
    """
    
    Zero = 1
    """
    Set the value to ``0``.
    """
    
    Replace = 2
    """
    Replace the value with the stencil reference value.
    """
    
    IncSat = 3
    """
    Increment the value but saturate at the maximum representable value (typically ``255``).
    """
    
    DecSat = 4
    """
    Decrement the value but saturate at ``0``.
    """
    
    IncWrap = 5
    """
    Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``.
    """
    
    DecWrap = 6
    """
    Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``).
    """
    
    Invert = 7
    """
    Invert the bits in the stencil value (bitwise ``NOT``).
    """
    

# Assign __doc__ for enum values for easier introspection

StencilOperation.Keep.__doc__ = """
Keep the existing value unmodified.
"""

StencilOperation.Zero.__doc__ = """
Set the value to ``0``.
"""

StencilOperation.Replace.__doc__ = """
Replace the value with the stencil reference value.
"""

StencilOperation.IncSat.__doc__ = """
Increment the value but saturate at the maximum representable value (typically ``255``).
"""

StencilOperation.DecSat.__doc__ = """
Decrement the value but saturate at ``0``.
"""

StencilOperation.IncWrap.__doc__ = """
Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``.
"""

StencilOperation.DecWrap.__doc__ = """
Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``).
"""

StencilOperation.Invert.__doc__ = """
Invert the bits in the stencil value (bitwise ``NOT``).
"""

