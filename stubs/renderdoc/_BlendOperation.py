from enum import IntEnum

class BlendOperation(IntEnum):
    # Original docstring
    """
    A blending operation to apply in color blending.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "destination" value is the value in the target being blended to.
    
      These values are multiplied by a given blend factor, see :class:`BlendMultiplier`.
    
    .. data:: Add
    
      Add the two values being processed together.
    
    .. data:: Subtract
    
      Subtract the destination value from the source value.
    
    .. data:: ReversedSubtract
    
      Subtract the source value from the destination value.
    
    .. data:: Minimum
    
      The minimum of the source and destination value.
    
    .. data:: Maximum
    
      The maximum of the source and destination value.
    """
    
    
    # Enum values
    
    Add = 0
    """
    Add the two values being processed together.
    """
    
    Subtract = 1
    """
    Subtract the destination value from the source value.
    """
    
    ReversedSubtract = 2
    """
    Subtract the source value from the destination value.
    """
    
    Minimum = 3
    """
    The minimum of the source and destination value.
    """
    
    Maximum = 4
    """
    The maximum of the source and destination value.
    """
    

# Assign __doc__ for enum values for easier introspection

BlendOperation.Add.__doc__ = """
Add the two values being processed together.
"""

BlendOperation.Subtract.__doc__ = """
Subtract the destination value from the source value.
"""

BlendOperation.ReversedSubtract.__doc__ = """
Subtract the source value from the destination value.
"""

BlendOperation.Minimum.__doc__ = """
The minimum of the source and destination value.
"""

BlendOperation.Maximum.__doc__ = """
The maximum of the source and destination value.
"""

