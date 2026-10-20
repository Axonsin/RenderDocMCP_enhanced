from enum import IntEnum

class LogicOperation(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    NoOp = 0
    """
    No operation is performed, the destination is unmodified.
    """
    
    Clear = 1
    """
    A ``0`` in every bit.
    """
    
    Set = 2
    """
    A ``1`` in every bit.
    """
    
    Copy = 3
    """
    The contents of the source value.
    """
    
    CopyInverted = 4
    """
    The contents of the source value are bitwise inverted.
    """
    
    Invert = 5
    """
    The contents of the destination value are bitwise inverted, then written.
    """
    
    And = 6
    """
    The source and destination values are combined with the bitwise ``AND`` operator.
    """
    
    Nand = 7
    """
    The source and destination values are combined with the bitwise ``NAND`` operator.
    """
    
    Or = 8
    """
    The source and destination values are combined with the bitwise ``OR`` operator.
    """
    
    Xor = 9
    """
    The source and destination values are combined with the bitwise ``XOR`` operator.
    """
    
    Nor = 10
    """
    The source and destination values are combined with the bitwise ``NOR`` operator.
    """
    
    Equivalent = 11
    """
    The source and destination values are combined with the logical equivalence operator, defined as
    ``NOT (s XOR d)``.
    """
    
    AndReverse = 12
    """
    The source and inverted destination values are combined with the bitwise ``AND`` operator - i.e.
    ``s AND (NOT d)``.
    """
    
    AndInverted = 13
    """
    The inverted source and destination values are combined with the bitwise ``AND`` operator - i.e.
    ``(NOT s) AND d``.
    """
    
    OrReverse = 14
    """
    The source and inverted destination values are combined with the bitwise ``OR`` operator - i.e.
    ``s OR (NOT d)``.
    """
    
    OrInverted = 15
    """
    The inverted source and destination values are combined with the bitwise ``OR`` operator - i.e.
    ``(NOT s) OR d``.
    """
    

# Assign __doc__ for enum values for easier introspection

LogicOperation.NoOp.__doc__ = """
No operation is performed, the destination is unmodified.
"""

LogicOperation.Clear.__doc__ = """
A ``0`` in every bit.
"""

LogicOperation.Set.__doc__ = """
A ``1`` in every bit.
"""

LogicOperation.Copy.__doc__ = """
The contents of the source value.
"""

LogicOperation.CopyInverted.__doc__ = """
The contents of the source value are bitwise inverted.
"""

LogicOperation.Invert.__doc__ = """
The contents of the destination value are bitwise inverted, then written.
"""

LogicOperation.And.__doc__ = """
The source and destination values are combined with the bitwise ``AND`` operator.
"""

LogicOperation.Nand.__doc__ = """
The source and destination values are combined with the bitwise ``NAND`` operator.
"""

LogicOperation.Or.__doc__ = """
The source and destination values are combined with the bitwise ``OR`` operator.
"""

LogicOperation.Xor.__doc__ = """
The source and destination values are combined with the bitwise ``XOR`` operator.
"""

LogicOperation.Nor.__doc__ = """
The source and destination values are combined with the bitwise ``NOR`` operator.
"""

LogicOperation.Equivalent.__doc__ = """
The source and destination values are combined with the logical equivalence operator, defined as
``NOT (s XOR d)``.
"""

LogicOperation.AndReverse.__doc__ = """
The source and inverted destination values are combined with the bitwise ``AND`` operator - i.e.
``s AND (NOT d)``.
"""

LogicOperation.AndInverted.__doc__ = """
The inverted source and destination values are combined with the bitwise ``AND`` operator - i.e.
``(NOT s) AND d``.
"""

LogicOperation.OrReverse.__doc__ = """
The source and inverted destination values are combined with the bitwise ``OR`` operator - i.e.
``s OR (NOT d)``.
"""

LogicOperation.OrInverted.__doc__ = """
The inverted source and destination values are combined with the bitwise ``OR`` operator - i.e.
``(NOT s) OR d``.
"""

