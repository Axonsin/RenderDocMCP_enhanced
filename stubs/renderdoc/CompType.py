# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CompType(__enum.IntEnum):
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
    
      An opaque value storing depth information, either :data:`floating point <float>` for 32-bit depth
      values or else :data:`unsigned normalised <UNorm>` for other bit sizes.
    
    .. data:: UNormSRGB
    
      Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
      ``1.0``, but with an sRGB gamma curve applied.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Depth = 8
    """
    An opaque value storing depth information, either :data:`floating point <float>` for 32-bit depth
      values or else :data:`unsigned normalised <UNorm>` for other bit sizes.
    """

    Float = 1
    """ An IEEE floating point value of 64-bit, 32-bit or 16-bit size. """

    SInt = 5
    """ A signed integer value. """

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

    SScaled = 7
    """
    A signed scaled floating point value. This is converted from the input signed integer without
      any normalisation as with :data:`SNorm`, so the resulting values range from the minimum signed
      integer value ``-2^(N-1)`` to the maximum signed integer value ``2^(N-1) - 1``.
    """

    Typeless = 0
    """ A component that has no concrete type. """

    UInt = 4
    """ An unsigned integer value. """

    UNorm = 2
    """
    An unsigned normalised floating point value. This is converted by dividing the input value by
      the maximum representable unsigned integer value, to produce a value in the range ``[0, 1]``
    """

    UNormSRGB = 9
    """
    Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
      ``1.0``, but with an sRGB gamma curve applied.
    """

    UScaled = 6
    """
    An unsigned scaled floating point value. This is converted from the input unsigned integer without
      any normalisation as with :data:`UNorm`, so the resulting values range from ``0`` to the maximum
      unsigned integer value ``2^N - 1``.
    """



