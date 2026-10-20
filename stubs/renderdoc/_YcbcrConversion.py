from enum import IntEnum

class YcbcrConversion(IntEnum):
    # Original docstring
    """
    The color model conversion that a YCbCr sampler uses to convert from YCbCr to RGB.
    
    .. data:: Raw
    
      The input values are not converted at all.
    
    .. data:: RangeOnly
    
      There is no model conversion but the inputs are range expanded as for YCbCr.
    
    .. data:: BT709
    
      The conversion uses the BT.709 color model conversion.
    
    .. data:: BT601
    
      The conversion uses the BT.601 color model conversion.
    
    .. data:: BT2020
    
      The conversion uses the BT.2020 color model conversion.
    """
    
    
    # Enum values
    
    Raw = 0
    """
    The input values are not converted at all.
    """
    
    RangeOnly = 1
    """
    There is no model conversion but the inputs are range expanded as for YCbCr.
    """
    
    BT709 = 2
    """
    The conversion uses the BT.709 color model conversion.
    """
    
    BT601 = 3
    """
    The conversion uses the BT.601 color model conversion.
    """
    
    BT2020 = 4
    """
    The conversion uses the BT.2020 color model conversion.
    """
    

# Assign __doc__ for enum values for easier introspection

YcbcrConversion.Raw.__doc__ = """
The input values are not converted at all.
"""

YcbcrConversion.RangeOnly.__doc__ = """
There is no model conversion but the inputs are range expanded as for YCbCr.
"""

YcbcrConversion.BT709.__doc__ = """
The conversion uses the BT.709 color model conversion.
"""

YcbcrConversion.BT601.__doc__ = """
The conversion uses the BT.601 color model conversion.
"""

YcbcrConversion.BT2020.__doc__ = """
The conversion uses the BT.2020 color model conversion.
"""

