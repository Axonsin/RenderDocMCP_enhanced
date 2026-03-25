# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderStageMask(__enum.IntFlag):
    """
    A set of flags for ``ShaderStage`` stages
    
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    All = 16383
    """ A shorthand version with flags set for all stages together. """

    Amplification = 64
    """ The flag for :data:`ShaderStage.Amplification`. """

    AnyHit = 1024
    """ The flag for :data:`ShaderStage.AnyHit`. """

    Callable = 8192
    """ The flag for :data:`ShaderStage.Callable`. """

    ClosestHit = 2048
    """ The flag for :data:`ShaderStage.ClosestHit`. """

    Compute = 32
    """ The flag for :data:`ShaderStage.Compute`. """

    Domain = 4
    """ The flag for :data:`ShaderStage.Domain`. """

    Fragment = 16
    """ The flag for :data:`ShaderStage.Fragment`. """

    Geometry = 8
    """ The flag for :data:`ShaderStage.Geometry`. """

    Hull = 2
    """ The flag for :data:`ShaderStage.Hull`. """

    Intersection = 512
    """ The flag for :data:`ShaderStage.Intersection`. """

    Mesh = 128
    """ The flag for :data:`ShaderStage.Mesh`. """

    Miss = 4096
    """ The flag for :data:`ShaderStage.Miss`. """

    Pixel = 16
    """ The flag for :data:`ShaderStage.Pixel`. """

    RayGen = 256
    """ The flag for :data:`ShaderStage.RayGen`. """

    Task = 64
    """ The flag for :data:`ShaderStage.Task`. """

    Tess_Control = 2
    """ The flag for :data:`ShaderStage.Tess_Control`. """

    Tess_Eval = 4
    """ The flag for :data:`ShaderStage.Tess_Eval`. """

    Unknown = 0
    """ No flags set for any shader stages. """

    Vertex = 1
    """ The flag for :data:`ShaderStage.Vertex`. """



