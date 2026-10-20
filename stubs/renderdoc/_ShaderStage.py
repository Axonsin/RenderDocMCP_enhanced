from enum import IntEnum

class ShaderStage(IntEnum):
    # Original docstring
    """
    The stage in a pipeline where a shader runs
    
    .. data:: Vertex
    
      The vertex shader.
    
    .. data:: Hull
    
      The hull shader. See also :data:`Tess_Control`.
    
    .. data:: Tess_Control
    
      The tessellation control shader. See also :data:`Hull`.
    
    .. data:: Domain
    
      The domain shader. See also :data:`Tess_Eval`.
    
    .. data:: Tess_Eval
    
      The tessellation evaluation shader. See also :data:`Domain`.
    
    .. data:: Geometry
    
      The geometry shader.
    
    .. data:: Pixel
    
      The pixel shader. See also :data:`Fragment`.
    
    .. data:: Fragment
    
      The fragment shader. See also :data:`Pixel`.
    
    .. data:: Compute
    
      The compute shader.
    
    .. data:: Amplification
    
      The amplification shader. See also :data:`Task`.
    
    .. data:: Task
    
      The task shader. See also :data:`Amplification`.
    
    .. data:: Mesh
    
      The mesh shader.
    
    .. data:: RayGen
    
      A ray generation shader, called from a ray dispatch command to launch initial rays.
    
    .. data:: Intersection
    
      An intersection shader, used for procedural objects in a BLAS to calculate hits.
    
    .. data:: AnyHit
    
      An any-hit shader, called in an indeterminate order and number when a ray intersection has been
      found with an object but may not be the final hit.
    
    .. data:: ClosestHit
    
      A closest-hit shader, called once the closest hit on a ray has been found.
    
    .. data:: Miss
    
      A miss shader, called when a ray has no valid closest hit at all.
    
    .. data:: Callable
    
      A callable shader, called by shader code via index during ray processing.
    
    .. data:: Invalid
    
      An invalid/unknown shader stage.
    """
    
    
    # Enum values
    
    Vertex = 0
    """
    The vertex shader.
    """
    
    Hull = 1
    """
    The hull shader. See also :data:`Tess_Control`.
    """
    
    Domain = 2
    """
    The domain shader. See also :data:`Tess_Eval`.
    """
    
    Geometry = 3
    """
    The geometry shader.
    """
    
    Pixel = 4
    """
    The pixel shader. See also :data:`Fragment`.
    """
    
    Compute = 5
    """
    The compute shader.
    """
    
    Task = 6
    """
    The task shader. See also :data:`Amplification`.
    """
    
    Mesh = 7
    """
    The mesh shader.
    """
    
    RayGen = 8
    """
    A ray generation shader, called from a ray dispatch command to launch initial rays.
    """
    
    Intersection = 9
    """
    An intersection shader, used for procedural objects in a BLAS to calculate hits.
    """
    
    AnyHit = 10
    """
    An any-hit shader, called in an indeterminate order and number when a ray intersection has been
    found with an object but may not be the final hit.
    """
    
    ClosestHit = 11
    """
    A closest-hit shader, called once the closest hit on a ray has been found.
    """
    
    Miss = 12
    """
    A miss shader, called when a ray has no valid closest hit at all.
    """
    
    Callable = 13
    """
    A callable shader, called by shader code via index during ray processing.
    """
    
    Count = 14
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    
    Tess_Control = 1
    """
    The tessellation control shader. See also :data:`Hull`.
    """
    
    Tess_Eval = 2
    """
    The tessellation evaluation shader. See also :data:`Domain`.
    """
    
    Fragment = 4
    """
    The fragment shader. See also :data:`Pixel`.
    """
    
    Amplification = 6
    """
    The amplification shader. See also :data:`Task`.
    """
    
    Invalid = 14
    """
    An invalid/unknown shader stage.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderStage.Vertex.__doc__ = """
The vertex shader.
"""

ShaderStage.Hull.__doc__ = """
The hull shader. See also :data:`Tess_Control`.
"""

ShaderStage.Domain.__doc__ = """
The domain shader. See also :data:`Tess_Eval`.
"""

ShaderStage.Geometry.__doc__ = """
The geometry shader.
"""

ShaderStage.Pixel.__doc__ = """
The pixel shader. See also :data:`Fragment`.
"""

ShaderStage.Compute.__doc__ = """
The compute shader.
"""

ShaderStage.Task.__doc__ = """
The task shader. See also :data:`Amplification`.
"""

ShaderStage.Mesh.__doc__ = """
The mesh shader.
"""

ShaderStage.RayGen.__doc__ = """
A ray generation shader, called from a ray dispatch command to launch initial rays.
"""

ShaderStage.Intersection.__doc__ = """
An intersection shader, used for procedural objects in a BLAS to calculate hits.
"""

ShaderStage.AnyHit.__doc__ = """
An any-hit shader, called in an indeterminate order and number when a ray intersection has been
found with an object but may not be the final hit.
"""

ShaderStage.ClosestHit.__doc__ = """
A closest-hit shader, called once the closest hit on a ray has been found.
"""

ShaderStage.Miss.__doc__ = """
A miss shader, called when a ray has no valid closest hit at all.
"""

ShaderStage.Callable.__doc__ = """
A callable shader, called by shader code via index during ray processing.
"""

ShaderStage.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

ShaderStage.First.__doc__ = """
The first enum value, for ease of iteration.
"""

ShaderStage.Tess_Control.__doc__ = """
The tessellation control shader. See also :data:`Hull`.
"""

ShaderStage.Tess_Eval.__doc__ = """
The tessellation evaluation shader. See also :data:`Domain`.
"""

ShaderStage.Fragment.__doc__ = """
The fragment shader. See also :data:`Pixel`.
"""

ShaderStage.Amplification.__doc__ = """
The amplification shader. See also :data:`Task`.
"""

ShaderStage.Invalid.__doc__ = """
An invalid/unknown shader stage.
"""

