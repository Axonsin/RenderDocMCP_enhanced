from enum import IntEnum

class ChromaSampleLocation(IntEnum):
    # Original docstring
    """
    Determines where in the pixel downsampled chrome samples are positioned.
    
    .. data:: CositedEven
    
      The chroma samples are positioned exactly in the same place as the even luma co-ordinates.
    
    .. data:: Midpoint
    
      The chrome samples are positioned half way between each even luma sample and the next highest odd
      luma sample.
    """
    
    
    # Enum values
    
    CositedEven = 0
    """
    The chroma samples are positioned exactly in the same place as the even luma co-ordinates.
    """
    
    Midpoint = 1
    """
    The chrome samples are positioned half way between each even luma sample and the next highest odd
    luma sample.
    """
    

# Assign __doc__ for enum values for easier introspection

ChromaSampleLocation.CositedEven.__doc__ = """
The chroma samples are positioned exactly in the same place as the even luma co-ordinates.
"""

ChromaSampleLocation.Midpoint.__doc__ = """
The chrome samples are positioned half way between each even luma sample and the next highest odd
luma sample.
"""

