from enum import IntEnum

class MeshDataStage(IntEnum):
    # Original docstring
    """
    Describes a particular stage in the geometry transformation pipeline.
    
    .. data:: VSIn
    
      The inputs to the vertex shader described by the explicit API vertex input bindings.
    
    .. data:: VSOut
    
      The outputs from the vertex shader corresponding one-to-one to the input elements.
    
    .. data:: GSOut
    
      The final output from the last stage in the pipeline, be that tessellation or geometry shader.
    
      This has possibly been expanded/multiplied from the inputs
    
    .. data:: TaskOut
    
      Data from a task/amplification shader.
    
    .. data:: AmpOut
    
      Data from an amplification shader (alias for :data:`TaskOut`).
    
    .. data:: MeshOut
    
      Data from a mesh shader.
    """
    
    
    # Enum values
    
    VSIn = 0
    """
    The inputs to the vertex shader described by the explicit API vertex input bindings.
    """
    
    VSOut = 1
    """
    The outputs from the vertex shader corresponding one-to-one to the input elements.
    """
    
    GSOut = 2
    """
    The final output from the last stage in the pipeline, be that tessellation or geometry shader.
    
    This has possibly been expanded/multiplied from the inputs
    """
    
    TaskOut = 3
    """
    Data from a task/amplification shader.
    """
    
    MeshOut = 4
    """
    Data from a mesh shader.
    """
    
    Count = 5
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    
    AmpOut = 3
    """
    Data from an amplification shader (alias for :data:`TaskOut`).
    """
    

# Assign __doc__ for enum values for easier introspection

MeshDataStage.VSIn.__doc__ = """
The inputs to the vertex shader described by the explicit API vertex input bindings.
"""

MeshDataStage.VSOut.__doc__ = """
The outputs from the vertex shader corresponding one-to-one to the input elements.
"""

MeshDataStage.GSOut.__doc__ = """
The final output from the last stage in the pipeline, be that tessellation or geometry shader.

This has possibly been expanded/multiplied from the inputs
"""

MeshDataStage.TaskOut.__doc__ = """
Data from a task/amplification shader.
"""

MeshDataStage.MeshOut.__doc__ = """
Data from a mesh shader.
"""

MeshDataStage.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

MeshDataStage.First.__doc__ = """
The first enum value, for ease of iteration.
"""

MeshDataStage.AmpOut.__doc__ = """
Data from an amplification shader (alias for :data:`TaskOut`).
"""

