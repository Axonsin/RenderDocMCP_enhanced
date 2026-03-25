# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderStage(__enum.IntEnum):
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
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Amplification = 6
    """ The amplification shader. See also :data:`Task`. """

    AnyHit = 10
    """
    An any-hit shader, called in an indeterminate order and number when a ray intersection has been
      found with an object but may not be the final hit.
    """

    Callable = 13
    """ A callable shader, called by shader code via index during ray processing. """

    ClosestHit = 11
    """ A closest-hit shader, called once the closest hit on a ray has been found. """

    Compute = 5
    """ The compute shader. """

    Count = 14
    Domain = 2
    """ The domain shader. See also :data:`Tess_Eval`. """

    First = 0
    Fragment = 4
    """ The fragment shader. See also :data:`Pixel`. """

    Geometry = 3
    """ The geometry shader. """

    Hull = 1
    """ The hull shader. See also :data:`Tess_Control`. """

    Intersection = 9
    """ An intersection shader, used for procedural objects in a BLAS to calculate hits. """

    Mesh = 7
    """ The mesh shader. """

    Miss = 12
    """ A miss shader, called when a ray has no valid closest hit at all. """

    Pixel = 4
    """ The pixel shader. See also :data:`Fragment`. """

    RayGen = 8
    """ A ray generation shader, called from a ray dispatch command to launch initial rays. """

    Task = 6
    """ The task shader. See also :data:`Amplification`. """

    Tess_Control = 1
    """ The tessellation control shader. See also :data:`Hull`. """

    Tess_Eval = 2
    """ The tessellation evaluation shader. See also :data:`Domain`. """

    Vertex = 0
    """ The vertex shader. """



