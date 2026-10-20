from enum import IntEnum

class FilterFunction(IntEnum):
    # Original docstring
    """
    The function used to process the returned value after interpolation.
    
    .. data:: Normal
    
      No special processing is used, the value is returned directly to the shader.
    
    .. data:: Comparison
    
      The value from interpolation is compared to a reference value and the comparison result is
      returned to the shader.
    
    .. data:: Minimum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
      used instead to find the minimum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the min function.
    
    .. data:: Maximum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
      used instead to find the maximum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the max function.
    """
    
    
    # Enum values
    
    Normal = 0
    """
    No special processing is used, the value is returned directly to the shader.
    """
    
    Comparison = 1
    """
    The value from interpolation is compared to a reference value and the comparison result is
    returned to the shader.
    """
    
    Minimum = 2
    """
    Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
    used instead to find the minimum sample value.
    
    Texels that were weight to 0 during interpolation are not included in the min function.
    """
    
    Maximum = 3
    """
    Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
    used instead to find the maximum sample value.
    
    Texels that were weight to 0 during interpolation are not included in the max function.
    """
    

# Assign __doc__ for enum values for easier introspection

FilterFunction.Normal.__doc__ = """
No special processing is used, the value is returned directly to the shader.
"""

FilterFunction.Comparison.__doc__ = """
The value from interpolation is compared to a reference value and the comparison result is
returned to the shader.
"""

FilterFunction.Minimum.__doc__ = """
Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
used instead to find the minimum sample value.

Texels that were weight to 0 during interpolation are not included in the min function.
"""

FilterFunction.Maximum.__doc__ = """
Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
used instead to find the maximum sample value.

Texels that were weight to 0 during interpolation are not included in the max function.
"""

