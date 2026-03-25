# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class LogicOperation(__enum.IntEnum):
    """
    A logical operation to apply when writing texture values to an output.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "destination" value is the value in the target being written to.
    
    .. data:: NoOp
    
      No operation is performed, the destination is unmodified.
    
    .. data:: Clear
    
      A ``0`` in every bit.
    
    .. data:: Set
    
      A ``1`` in every bit.
    
    .. data:: Copy
    
      The contents of the source value.
    
    .. data:: CopyInverted
    
      The contents of the source value are bitwise inverted.
    
    .. data:: Invert
    
      The contents of the destination value are bitwise inverted, then written.
    
    .. data:: And
    
      The source and destination values are combined with the bitwise ``AND`` operator.
    
    .. data:: Nand
    
      The source and destination values are combined with the bitwise ``NAND`` operator.
    
    .. data:: Or
    
      The source and destination values are combined with the bitwise ``OR`` operator.
    
    .. data:: Xor
    
      The source and destination values are combined with the bitwise ``XOR`` operator.
    
    .. data:: Nor
    
      The source and destination values are combined with the bitwise ``NOR`` operator.
    
    .. data:: Equivalent
    
      The source and destination values are combined with the logical equivalence operator, defined as
      ``NOT (s XOR d)``.
    
    .. data:: AndReverse
    
      The source and inverted destination values are combined with the bitwise ``AND`` operator - i.e.
      ``s AND (NOT d)``.
    
    .. data:: AndInverted
    
      The inverted source and destination values are combined with the bitwise ``AND`` operator - i.e.
      ``(NOT s) AND d``.
    
    .. data:: OrReverse
    
      The source and inverted destination values are combined with the bitwise ``OR`` operator - i.e.
      ``s OR (NOT d)``.
    
    .. data:: OrInverted
    
      The inverted source and destination values are combined with the bitwise ``OR`` operator - i.e.
      ``(NOT s) OR d``.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    And = 6
    """ The source and destination values are combined with the bitwise ``AND`` operator. """

    AndInverted = 13
    """
    The inverted source and destination values are combined with the bitwise ``AND`` operator - i.e.
      ``(NOT s) AND d``.
    """

    AndReverse = 12
    """
    The source and inverted destination values are combined with the bitwise ``AND`` operator - i.e.
      ``s AND (NOT d)``.
    """

    Clear = 1
    """ A ``0`` in every bit. """

    Copy = 3
    """ The contents of the source value. """

    CopyInverted = 4
    """ The contents of the source value are bitwise inverted. """

    Equivalent = 11
    """
    The source and destination values are combined with the logical equivalence operator, defined as
      ``NOT (s XOR d)``.
    """

    Invert = 5
    """ The contents of the destination value are bitwise inverted, then written. """

    Nand = 7
    """ The source and destination values are combined with the bitwise ``NAND`` operator. """

    NoOp = 0
    """ No operation is performed, the destination is unmodified. """

    Nor = 10
    """ The source and destination values are combined with the bitwise ``NOR`` operator. """

    Or = 8
    """ The source and destination values are combined with the bitwise ``OR`` operator. """

    OrInverted = 15
    """
    The inverted source and destination values are combined with the bitwise ``OR`` operator - i.e.
      ``(NOT s) OR d``.
    """

    OrReverse = 14
    """
    The source and inverted destination values are combined with the bitwise ``OR`` operator - i.e.
      ``s OR (NOT d)``.
    """

    Set = 2
    """ A ``1`` in every bit. """

    Xor = 9
    """ The source and destination values are combined with the bitwise ``XOR`` operator. """



