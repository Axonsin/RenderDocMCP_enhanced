from enum import IntEnum

class QualityHint(IntEnum):
    # Original docstring
    """
    An API specific hint for a certain behaviour. A legacy concept in OpenGL that controls
    hints to the implementation where there is room for interpretation within the range of valid
    behaviour.
    
    .. data:: DontCare
    
      The hinted behaviour can follow any valid path as the implementation decides.
    
    .. data:: Nicest
    
      The hinted behaviour should follow the most correct or highest quality path.
    
    .. data:: Fastest
    
      The hinted behaviour should follow the most efficient path.
    """
    
    
    # Enum values
    
    DontCare = 0
    """
    The hinted behaviour can follow any valid path as the implementation decides.
    """
    
    Nicest = 1
    """
    The hinted behaviour should follow the most correct or highest quality path.
    """
    
    Fastest = 2
    """
    The hinted behaviour should follow the most efficient path.
    """
    

# Assign __doc__ for enum values for easier introspection

QualityHint.DontCare.__doc__ = """
The hinted behaviour can follow any valid path as the implementation decides.
"""

QualityHint.Nicest.__doc__ = """
The hinted behaviour should follow the most correct or highest quality path.
"""

QualityHint.Fastest.__doc__ = """
The hinted behaviour should follow the most efficient path.
"""

