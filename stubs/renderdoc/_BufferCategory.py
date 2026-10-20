from enum import IntFlag

class BufferCategory(IntFlag):
    # Original docstring
    """
    A set of flags describing how this buffer may be used
    
    .. data:: NoFlags
    
      The buffer will not be used for any of the uses below.
    
    .. data:: Vertex
    
      The buffer will be used for sourcing vertex input data.
    
    .. data:: Index
    
      The buffer will be used for sourcing primitive index data.
    
    .. data:: Constants
    
      The buffer will be used for sourcing shader constant data.
    
    .. data:: ReadWrite
    
      The buffer will be used for read and write access from shaders.
    
    .. data:: Indirect
    
      The buffer will be used to provide indirect parameters for launching GPU-based actions.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    The buffer will not be used for any of the uses below.
    """
    
    Vertex = 1
    """
    The buffer will be used for sourcing vertex input data.
    """
    
    Index = 2
    """
    The buffer will be used for sourcing primitive index data.
    """
    
    Constants = 4
    """
    The buffer will be used for sourcing shader constant data.
    """
    
    ReadWrite = 8
    """
    The buffer will be used for read and write access from shaders.
    """
    
    Indirect = 16
    """
    The buffer will be used to provide indirect parameters for launching GPU-based actions.
    """
    

# Assign __doc__ for enum values for easier introspection

BufferCategory.NoFlags.__doc__ = """
The buffer will not be used for any of the uses below.
"""

BufferCategory.Vertex.__doc__ = """
The buffer will be used for sourcing vertex input data.
"""

BufferCategory.Index.__doc__ = """
The buffer will be used for sourcing primitive index data.
"""

BufferCategory.Constants.__doc__ = """
The buffer will be used for sourcing shader constant data.
"""

BufferCategory.ReadWrite.__doc__ = """
The buffer will be used for read and write access from shaders.
"""

BufferCategory.Indirect.__doc__ = """
The buffer will be used to provide indirect parameters for launching GPU-based actions.
"""

