from enum import IntEnum

class DepthBiasMode(IntEnum):
    # Original docstring
    """
    The mode for calculating the r least representable value in depth bias.
    
    .. data:: Default
    
      The default calculation is used which may be vendor-specific and depends on the
      format of the depth attachment. It may vary across different primitives at
      different depths.
    
    .. data:: ForceUNorm
    
      A forced calculation based purely on the bit-size of either the fixed point or
      floating point mantissa representation in the attachment format.
    
    .. data:: One
    
      A literal ``1.0`` value is used
    """
    
    
    # Enum values
    
    Default = 0
    """
    The default calculation is used which may be vendor-specific and depends on the
    format of the depth attachment. It may vary across different primitives at
    different depths.
    """
    
    ForceUNorm = 1
    """
    A forced calculation based purely on the bit-size of either the fixed point or
    floating point mantissa representation in the attachment format.
    """
    
    One = 2
    """
    A literal ``1.0`` value is used
    """
    

# Assign __doc__ for enum values for easier introspection

DepthBiasMode.Default.__doc__ = """
The default calculation is used which may be vendor-specific and depends on the
format of the depth attachment. It may vary across different primitives at
different depths.
"""

DepthBiasMode.ForceUNorm.__doc__ = """
A forced calculation based purely on the bit-size of either the fixed point or
floating point mantissa representation in the attachment format.
"""

DepthBiasMode.One.__doc__ = """
A literal ``1.0`` value is used
"""

