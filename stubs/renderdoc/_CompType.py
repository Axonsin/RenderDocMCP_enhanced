from enum import IntEnum

class CompType(IntEnum):
    # Original docstring
    """
    Represents the component type of a channel in a texture or element in a structure.
    
    .. data:: Typeless
    
      A component that has no concrete type.
    
    .. data:: Float
    
      An IEEE floating point value of 64-bit, 32-bit or 16-bit size.
    
    .. data:: UNorm
    
      An unsigned normalised floating point value. This is converted by dividing the input value by
      the maximum representable unsigned integer value, to produce a value in the range ``[0, 1]``
    
    .. data:: SNorm
    
      A signed normalised floating point value in range. This is converted by dividing the input value
      by the maximum representable *positive signed* integer value, to produce a value in the range
      ``[-1, 1]``. As a special case, the maximum negative signed integer is also mapped to ``-1`` so
      there are two representations of -1. This means there is only one ``0`` value and that there is
      the same range of available values for positive and negative values.
    
      For example, signed 16-bit integers range from ``-32768`` to ``+32767``. ``-32768`` is mapped to
      ``-1``, and then any other value is divided by ``32767`` giving an equal set of values in the
      range ``[-1, 0]`` as in the range ``[0, 1]``.
    
    .. data:: UInt
    
      An unsigned integer value.
    
    .. data:: SInt
    
      A signed integer value.
    
    .. data:: UScaled
    
      An unsigned scaled floating point value. This is converted from the input unsigned integer without
      any normalisation as with :data:`UNorm`, so the resulting values range from ``0`` to the maximum
      unsigned integer value ``2^N - 1``.
    
    .. data:: SScaled
    
      A signed scaled floating point value. This is converted from the input signed integer without
      any normalisation as with :data:`SNorm`, so the resulting values range from the minimum signed
      integer value ``-2^(N-1)`` to the maximum signed integer value ``2^(N-1) - 1``.
    
    .. data:: Depth
    
      An opaque value storing depth information, either :data:`Float` for 32-bit depth
      values or else :data:`UNorm` for other bit sizes.
    
    .. data:: UNormSRGB
    
      Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
      ``1.0``, but with an sRGB gamma curve applied.
    """
    
    
    # Enum values
    
    Typeless = 0
    """
    A component that has no concrete type.
    """
    
    Float = 1
    """
    An IEEE floating point value of 64-bit, 32-bit or 16-bit size.
    """
    
    UNorm = 2
    """
    An unsigned normalised floating point value. This is converted by dividing the input value by
    the maximum representable unsigned integer value, to produce a value in the range ``[0, 1]``
    """
    
    SNorm = 3
    """
    A signed normalised floating point value in range. This is converted by dividing the input value
    by the maximum representable *positive signed* integer value, to produce a value in the range
    ``[-1, 1]``. As a special case, the maximum negative signed integer is also mapped to ``-1`` so
    there are two representations of -1. This means there is only one ``0`` value and that there is
    the same range of available values for positive and negative values.
    
    For example, signed 16-bit integers range from ``-32768`` to ``+32767``. ``-32768`` is mapped to
    ``-1``, and then any other value is divided by ``32767`` giving an equal set of values in the
    range ``[-1, 0]`` as in the range ``[0, 1]``.
    """
    
    UInt = 4
    """
    An unsigned integer value.
    """
    
    SInt = 5
    """
    A signed integer value.
    """
    
    UScaled = 6
    """
    An unsigned scaled floating point value. This is converted from the input unsigned integer without
    any normalisation as with :data:`UNorm`, so the resulting values range from ``0`` to the maximum
    unsigned integer value ``2^N - 1``.
    """
    
    SScaled = 7
    """
    A signed scaled floating point value. This is converted from the input signed integer without
    any normalisation as with :data:`SNorm`, so the resulting values range from the minimum signed
    integer value ``-2^(N-1)`` to the maximum signed integer value ``2^(N-1) - 1``.
    """
    
    Depth = 8
    """
    An opaque value storing depth information, either :data:`Float` for 32-bit depth
    values or else :data:`UNorm` for other bit sizes.
    """
    
    UNormSRGB = 9
    """
    Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
    ``1.0``, but with an sRGB gamma curve applied.
    """
    

# Assign __doc__ for enum values for easier introspection

CompType.Typeless.__doc__ = """
A component that has no concrete type.
"""

CompType.Float.__doc__ = """
An IEEE floating point value of 64-bit, 32-bit or 16-bit size.
"""

CompType.UNorm.__doc__ = """
An unsigned normalised floating point value. This is converted by dividing the input value by
the maximum representable unsigned integer value, to produce a value in the range ``[0, 1]``
"""

CompType.SNorm.__doc__ = """
A signed normalised floating point value in range. This is converted by dividing the input value
by the maximum representable *positive signed* integer value, to produce a value in the range
``[-1, 1]``. As a special case, the maximum negative signed integer is also mapped to ``-1`` so
there are two representations of -1. This means there is only one ``0`` value and that there is
the same range of available values for positive and negative values.

For example, signed 16-bit integers range from ``-32768`` to ``+32767``. ``-32768`` is mapped to
``-1``, and then any other value is divided by ``32767`` giving an equal set of values in the
range ``[-1, 0]`` as in the range ``[0, 1]``.
"""

CompType.UInt.__doc__ = """
An unsigned integer value.
"""

CompType.SInt.__doc__ = """
A signed integer value.
"""

CompType.UScaled.__doc__ = """
An unsigned scaled floating point value. This is converted from the input unsigned integer without
any normalisation as with :data:`UNorm`, so the resulting values range from ``0`` to the maximum
unsigned integer value ``2^N - 1``.
"""

CompType.SScaled.__doc__ = """
A signed scaled floating point value. This is converted from the input signed integer without
any normalisation as with :data:`SNorm`, so the resulting values range from the minimum signed
integer value ``-2^(N-1)`` to the maximum signed integer value ``2^(N-1) - 1``.
"""

CompType.Depth.__doc__ = """
An opaque value storing depth information, either :data:`Float` for 32-bit depth
values or else :data:`UNorm` for other bit sizes.
"""

CompType.UNormSRGB.__doc__ = """
Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
``1.0``, but with an sRGB gamma curve applied.
"""

