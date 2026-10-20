from enum import IntEnum

class ShadingRateCombiner(IntEnum):
    # Original docstring
    """
    A combiner to apply when determining a pixel shading rate.
    
    .. data:: Keep
    
      Keep the first input to the combiner.
    
    .. data:: Passthrough
    
      Keep the first input to the combiner. Alias for :data:`Keep`, for D3D terminology.
    
    .. data:: Replace
    
      Replace with the second input to the combiner.
    
    .. data:: Override
    
      Replace with the second input to the combiner. Alias for :data:`Replace`, for D3D terminology.
    
    .. data:: Min
    
      Use the minimum (finest rate) of the two inputs.
    
    .. data:: Max
    
      Use the maximum (coarsest rate) of the two inputs.
    
    .. data:: Multiply
    
      Multiply the two rates together (e.g. 1x1 and 1x2 = 1x2, 2x2 and 2x2 = 4x4). Note that D3D names
      this 'sum' misleadingly.
    """
    
    
    # Enum values
    
    Keep = 0
    """
    Keep the first input to the combiner.
    """
    
    Replace = 1
    """
    Replace with the second input to the combiner.
    """
    
    Min = 2
    """
    Use the minimum (finest rate) of the two inputs.
    """
    
    Max = 3
    """
    Use the maximum (coarsest rate) of the two inputs.
    """
    
    Multiply = 4
    """
    Multiply the two rates together (e.g. 1x1 and 1x2 = 1x2, 2x2 and 2x2 = 4x4). Note that D3D names
    this 'sum' misleadingly.
    """
    
    # Aliases
    
    Passthrough = 0
    """
    Keep the first input to the combiner. Alias for :data:`Keep`, for D3D terminology.
    """
    
    Override = 1
    """
    Replace with the second input to the combiner. Alias for :data:`Replace`, for D3D terminology.
    """
    

# Assign __doc__ for enum values for easier introspection

ShadingRateCombiner.Keep.__doc__ = """
Keep the first input to the combiner.
"""

ShadingRateCombiner.Replace.__doc__ = """
Replace with the second input to the combiner.
"""

ShadingRateCombiner.Min.__doc__ = """
Use the minimum (finest rate) of the two inputs.
"""

ShadingRateCombiner.Max.__doc__ = """
Use the maximum (coarsest rate) of the two inputs.
"""

ShadingRateCombiner.Multiply.__doc__ = """
Multiply the two rates together (e.g. 1x1 and 1x2 = 1x2, 2x2 and 2x2 = 4x4). Note that D3D names
this 'sum' misleadingly.
"""

ShadingRateCombiner.Passthrough.__doc__ = """
Keep the first input to the combiner. Alias for :data:`Keep`, for D3D terminology.
"""

ShadingRateCombiner.Override.__doc__ = """
Replace with the second input to the combiner. Alias for :data:`Replace`, for D3D terminology.
"""

