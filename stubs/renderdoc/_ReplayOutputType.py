from enum import IntEnum

class ReplayOutputType(IntEnum):
    # Original docstring
    """
    The type of :class:`ReplayOutput` to create
    
    .. data:: Headless
    
      A headless output that does nothing to display to windows but can still be controlled and
      queried the same way
    
    .. data:: Texture
    
      An output that is used for displaying textures, thumbnails and pixel context
    
    .. data:: Mesh
    
      An output that will display mesh data previews
    """
    
    
    # Enum values
    
    Headless = 0
    """
    A headless output that does nothing to display to windows but can still be controlled and
    queried the same way
    """
    
    Texture = 1
    """
    An output that is used for displaying textures, thumbnails and pixel context
    """
    
    Mesh = 2
    """
    An output that will display mesh data previews
    """
    

# Assign __doc__ for enum values for easier introspection

ReplayOutputType.Headless.__doc__ = """
A headless output that does nothing to display to windows but can still be controlled and
queried the same way
"""

ReplayOutputType.Texture.__doc__ = """
An output that is used for displaying textures, thumbnails and pixel context
"""

ReplayOutputType.Mesh.__doc__ = """
An output that will display mesh data previews
"""

