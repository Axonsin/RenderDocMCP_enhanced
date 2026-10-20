from enum import IntEnum

class CompareFunction(IntEnum):
    # Original docstring
    """
    A comparison function to return a ``bool`` result from two inputs ``A`` and ``B``.
    
    .. data:: Never
    
      ``False``
    
    .. data:: AlwaysTrue
    
      ``True``
    
    .. data:: Less
    
      ``A < B``
    
    .. data:: LessEqual
    
      ``A <= B``
    
    .. data:: Greater
    
      ``A > B``
    
    .. data:: GreaterEqual
    
      ``A >= B``
    
    .. data:: Equal
    
      ``A == B``
    
    .. data:: NotEqual
    
      ``A != B``
    """
    
    
    # Enum values
    
    Never = 0
    """
    ``False``
    """
    
    AlwaysTrue = 1
    """
    ``True``
    """
    
    Less = 2
    """
    ``A < B``
    """
    
    LessEqual = 3
    """
    ``A <= B``
    """
    
    Greater = 4
    """
    ``A > B``
    """
    
    GreaterEqual = 5
    """
    ``A >= B``
    """
    
    Equal = 6
    """
    ``A == B``
    """
    
    NotEqual = 7
    """
    ``A != B``
    """
    

# Assign __doc__ for enum values for easier introspection

CompareFunction.Never.__doc__ = """
``False``
"""

CompareFunction.AlwaysTrue.__doc__ = """
``True``
"""

CompareFunction.Less.__doc__ = """
``A < B``
"""

CompareFunction.LessEqual.__doc__ = """
``A <= B``
"""

CompareFunction.Greater.__doc__ = """
``A > B``
"""

CompareFunction.GreaterEqual.__doc__ = """
``A >= B``
"""

CompareFunction.Equal.__doc__ = """
``A == B``
"""

CompareFunction.NotEqual.__doc__ = """
``A != B``
"""

