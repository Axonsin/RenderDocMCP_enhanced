from enum import IntFlag

class ShaderStageMask(IntFlag):
    # Original docstring
    """
    A set of flags for :class:`ShaderStage` stages
    
    .. data:: Unknown
    
      No flags set for any shader stages.
    
    .. data:: Vertex
    
      The flag for :data:`ShaderStage.Vertex`.
    
    .. data:: Hull
    
      The flag for :data:`ShaderStage.Hull`.
    
    .. data:: Tess_Control
    
      The flag for :data:`ShaderStage.Tess_Control`.
    
    .. data:: Domain
    
      The flag for :data:`ShaderStage.Domain`.
    
    .. data:: Tess_Eval
    
      The flag for :data:`ShaderStage.Tess_Eval`.
    
    .. data:: Geometry
    
      The flag for :data:`ShaderStage.Geometry`.
    
    .. data:: Pixel
    
      The flag for :data:`ShaderStage.Pixel`.
    
    .. data:: Fragment
    
      The flag for :data:`ShaderStage.Fragment`.
    
    .. data:: Compute
    
      The flag for :data:`ShaderStage.Compute`.
    
    .. data:: Task
    
      The flag for :data:`ShaderStage.Task`.
    
    .. data:: Amplification
    
      The flag for :data:`ShaderStage.Amplification`.
    
    .. data:: Mesh
    
      The flag for :data:`ShaderStage.Mesh`.
    
    .. data:: RayGen
    
      The flag for :data:`ShaderStage.RayGen`.
    
    .. data:: Intersection
    
      The flag for :data:`ShaderStage.Intersection`.
    
    .. data:: AnyHit
    
      The flag for :data:`ShaderStage.AnyHit`.
    
    .. data:: ClosestHit
    
      The flag for :data:`ShaderStage.ClosestHit`.
    
    .. data:: Miss
    
      The flag for :data:`ShaderStage.Miss`.
    
    .. data:: Callable
    
      The flag for :data:`ShaderStage.Callable`.
    
    .. data:: All
    
      A shorthand version with flags set for all stages together.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    No flags set for any shader stages.
    """
    
    Vertex = 1
    """
    The flag for :data:`ShaderStage.Vertex`.
    """
    
    Hull = 2
    """
    The flag for :data:`ShaderStage.Hull`.
    """
    
    Domain = 4
    """
    The flag for :data:`ShaderStage.Domain`.
    """
    
    Geometry = 8
    """
    The flag for :data:`ShaderStage.Geometry`.
    """
    
    Pixel = 16
    """
    The flag for :data:`ShaderStage.Pixel`.
    """
    
    Compute = 32
    """
    The flag for :data:`ShaderStage.Compute`.
    """
    
    Task = 64
    """
    The flag for :data:`ShaderStage.Task`.
    """
    
    Mesh = 128
    """
    The flag for :data:`ShaderStage.Mesh`.
    """
    
    RayGen = 256
    """
    The flag for :data:`ShaderStage.RayGen`.
    """
    
    Intersection = 512
    """
    The flag for :data:`ShaderStage.Intersection`.
    """
    
    AnyHit = 1024
    """
    The flag for :data:`ShaderStage.AnyHit`.
    """
    
    ClosestHit = 2048
    """
    The flag for :data:`ShaderStage.ClosestHit`.
    """
    
    Miss = 4096
    """
    The flag for :data:`ShaderStage.Miss`.
    """
    
    Callable = 8192
    """
    The flag for :data:`ShaderStage.Callable`.
    """
    
    All = 16383
    """
    A shorthand version with flags set for all stages together.
    """
    
    # Aliases
    
    Tess_Control = 2
    """
    The flag for :data:`ShaderStage.Tess_Control`.
    """
    
    Tess_Eval = 4
    """
    The flag for :data:`ShaderStage.Tess_Eval`.
    """
    
    Fragment = 16
    """
    The flag for :data:`ShaderStage.Fragment`.
    """
    
    Amplification = 64
    """
    The flag for :data:`ShaderStage.Amplification`.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderStageMask.Unknown.__doc__ = """
No flags set for any shader stages.
"""

ShaderStageMask.Vertex.__doc__ = """
The flag for :data:`ShaderStage.Vertex`.
"""

ShaderStageMask.Hull.__doc__ = """
The flag for :data:`ShaderStage.Hull`.
"""

ShaderStageMask.Domain.__doc__ = """
The flag for :data:`ShaderStage.Domain`.
"""

ShaderStageMask.Geometry.__doc__ = """
The flag for :data:`ShaderStage.Geometry`.
"""

ShaderStageMask.Pixel.__doc__ = """
The flag for :data:`ShaderStage.Pixel`.
"""

ShaderStageMask.Compute.__doc__ = """
The flag for :data:`ShaderStage.Compute`.
"""

ShaderStageMask.Task.__doc__ = """
The flag for :data:`ShaderStage.Task`.
"""

ShaderStageMask.Mesh.__doc__ = """
The flag for :data:`ShaderStage.Mesh`.
"""

ShaderStageMask.RayGen.__doc__ = """
The flag for :data:`ShaderStage.RayGen`.
"""

ShaderStageMask.Intersection.__doc__ = """
The flag for :data:`ShaderStage.Intersection`.
"""

ShaderStageMask.AnyHit.__doc__ = """
The flag for :data:`ShaderStage.AnyHit`.
"""

ShaderStageMask.ClosestHit.__doc__ = """
The flag for :data:`ShaderStage.ClosestHit`.
"""

ShaderStageMask.Miss.__doc__ = """
The flag for :data:`ShaderStage.Miss`.
"""

ShaderStageMask.Callable.__doc__ = """
The flag for :data:`ShaderStage.Callable`.
"""

ShaderStageMask.All.__doc__ = """
A shorthand version with flags set for all stages together.
"""

ShaderStageMask.Tess_Control.__doc__ = """
The flag for :data:`ShaderStage.Tess_Control`.
"""

ShaderStageMask.Tess_Eval.__doc__ = """
The flag for :data:`ShaderStage.Tess_Eval`.
"""

ShaderStageMask.Fragment.__doc__ = """
The flag for :data:`ShaderStage.Fragment`.
"""

ShaderStageMask.Amplification.__doc__ = """
The flag for :data:`ShaderStage.Amplification`.
"""

