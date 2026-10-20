from enum import IntEnum

class YcbcrRange(IntEnum):
    # Original docstring
    """
    Specifies the range of encoded values and their interpretation.
    
    .. data:: ITUFull
    
      The full range of input values are valid and interpreted according to ITU "full range" rules.
    
    .. data:: ITUNarrow
    
      A head and foot are reserved in the encoded values, and the remaining values are expanded
      according to "narrow range" rules.
    """
    
    
    # Enum values
    
    ITUFull = 0
    """
    The full range of input values are valid and interpreted according to ITU "full range" rules.
    """
    
    ITUNarrow = 1
    """
    A head and foot are reserved in the encoded values, and the remaining values are expanded
    according to "narrow range" rules.
    """
    

# Assign __doc__ for enum values for easier introspection

YcbcrRange.ITUFull.__doc__ = """
The full range of input values are valid and interpreted according to ITU "full range" rules.
"""

YcbcrRange.ITUNarrow.__doc__ = """
A head and foot are reserved in the encoded values, and the remaining values are expanded
according to "narrow range" rules.
"""

