from enum import IntEnum

class OffsetSizeDisplayMode(IntEnum):
    # Original docstring
    """
    The formatting mode used when displaying fields marked as Offsets or Sizes.
    
    .. data:: Auto
    
      The data is displayed as decimal values by default and hexadecimal if above a certain threshold.
    
    .. data:: Decimal
    
      The data is displayed as decimal values.
    
    .. data:: Hexadecimal
    
      The data is displayed as hexadecimal values.
    """
    
    
    # Enum values
    
    Auto = 0
    """
    The data is displayed as decimal values by default and hexadecimal if above a certain threshold.
    """
    
    Decimal = 1
    """
    The data is displayed as decimal values.
    """
    
    Hexadecimal = 2
    """
    The data is displayed as hexadecimal values.
    """
    
    Count = 3
    """
    The number of values in the enum, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

OffsetSizeDisplayMode.Auto.__doc__ = """
The data is displayed as decimal values by default and hexadecimal if above a certain threshold.
"""

OffsetSizeDisplayMode.Decimal.__doc__ = """
The data is displayed as decimal values.
"""

OffsetSizeDisplayMode.Hexadecimal.__doc__ = """
The data is displayed as hexadecimal values.
"""

OffsetSizeDisplayMode.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

