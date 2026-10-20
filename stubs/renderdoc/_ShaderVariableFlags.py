from enum import IntFlag

class ShaderVariableFlags(IntFlag):
    # Original docstring
    """
    A set of flags for events that control how a shader/buffer value is interpreted and
    displayed
    
    .. data:: NoFlags
    
      No flags are specified.
    
    .. data:: RowMajorMatrix
    
      This matrix is stored in row-major order in memory, instead of column-major. In RenderDoc values
      are always provided row-major regardless, for consistency of access, but if this flag is not
      present then the original values were in column order in memory, so the data has been transposed.
    
    .. data:: HexDisplay
    
      This value should be displayed using hexadecimal where possible.
    
    .. data:: BinaryDisplay
    
      This value should be displayed using binary where possible.
    
    .. data:: RGBDisplay
    
      This value should be interpreted as an RGB colour for display where possible.
    
    .. data:: R11G11B10
    
      This value should be decoded from a 32-bit integer in R11G11B10 packing format.
    
    .. data:: R10G10B10A2
    
      This value should be decoded from a 32-bit integer in R10G10B10A2 packing format.
    
    .. data:: UNorm
    
      This value should be treated as unsigned normalised floating point values when interpreting.
    
    .. data:: SNorm
    
      This value should be treated as signed normalised floating point values when interpreting.
    
    .. data:: Truncated
    
      This value was truncated when reading - the available range was exhausted.
    
    .. data:: SignedEnum
    
      For enums, the base type is a signed integer allowing signed values.
    
    .. data:: SingleElementArray
    
      In some cases it can be possible to represent and need to distinguish a variable declared as
      an array of size 1 from a scalar object. This flag indicates that even though elements == 1
      normally means 'not an array', in this case it means an array of size 1.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    No flags are specified.
    """
    
    RowMajorMatrix = 1
    """
    This matrix is stored in row-major order in memory, instead of column-major. In RenderDoc values
    are always provided row-major regardless, for consistency of access, but if this flag is not
    present then the original values were in column order in memory, so the data has been transposed.
    """
    
    HexDisplay = 2
    """
    This value should be displayed using hexadecimal where possible.
    """
    
    BinaryDisplay = 4
    """
    This value should be displayed using binary where possible.
    """
    
    RGBDisplay = 8
    """
    This value should be interpreted as an RGB colour for display where possible.
    """
    
    R11G11B10 = 16
    """
    This value should be decoded from a 32-bit integer in R11G11B10 packing format.
    """
    
    R10G10B10A2 = 32
    """
    This value should be decoded from a 32-bit integer in R10G10B10A2 packing format.
    """
    
    UNorm = 64
    """
    This value should be treated as unsigned normalised floating point values when interpreting.
    """
    
    SNorm = 128
    """
    This value should be treated as signed normalised floating point values when interpreting.
    """
    
    Truncated = 256
    """
    This value was truncated when reading - the available range was exhausted.
    """
    
    SignedEnum = 512
    """
    For enums, the base type is a signed integer allowing signed values.
    """
    
    SingleElementArray = 1024
    """
    In some cases it can be possible to represent and need to distinguish a variable declared as
    an array of size 1 from a scalar object. This flag indicates that even though elements == 1
    normally means 'not an array', in this case it means an array of size 1.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderVariableFlags.NoFlags.__doc__ = """
No flags are specified.
"""

ShaderVariableFlags.RowMajorMatrix.__doc__ = """
This matrix is stored in row-major order in memory, instead of column-major. In RenderDoc values
are always provided row-major regardless, for consistency of access, but if this flag is not
present then the original values were in column order in memory, so the data has been transposed.
"""

ShaderVariableFlags.HexDisplay.__doc__ = """
This value should be displayed using hexadecimal where possible.
"""

ShaderVariableFlags.BinaryDisplay.__doc__ = """
This value should be displayed using binary where possible.
"""

ShaderVariableFlags.RGBDisplay.__doc__ = """
This value should be interpreted as an RGB colour for display where possible.
"""

ShaderVariableFlags.R11G11B10.__doc__ = """
This value should be decoded from a 32-bit integer in R11G11B10 packing format.
"""

ShaderVariableFlags.R10G10B10A2.__doc__ = """
This value should be decoded from a 32-bit integer in R10G10B10A2 packing format.
"""

ShaderVariableFlags.UNorm.__doc__ = """
This value should be treated as unsigned normalised floating point values when interpreting.
"""

ShaderVariableFlags.SNorm.__doc__ = """
This value should be treated as signed normalised floating point values when interpreting.
"""

ShaderVariableFlags.Truncated.__doc__ = """
This value was truncated when reading - the available range was exhausted.
"""

ShaderVariableFlags.SignedEnum.__doc__ = """
For enums, the base type is a signed integer allowing signed values.
"""

ShaderVariableFlags.SingleElementArray.__doc__ = """
In some cases it can be possible to represent and need to distinguish a variable declared as
an array of size 1 from a scalar object. This flag indicates that even though elements == 1
normally means 'not an array', in this case it means an array of size 1.
"""

