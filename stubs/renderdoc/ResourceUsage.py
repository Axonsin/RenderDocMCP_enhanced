# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ResourceUsage(__enum.IntEnum):
    """
    How a resource is being used in the pipeline at a particular point.
    
    Note that a resource may be used for more than one thing in one event, see :class:`EventUsage`.
    
    .. data:: Unused
    
      The resource is not being used.
    
    .. data:: VertexBuffer
    
      The resource is being used as a fixed-function vertex buffer input.
    
    .. data:: IndexBuffer
    
      The resource is being used as an index buffer.
    
    .. data:: VS_Constants
    
      The resource is being used for constants in the :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_Constants
    
      The resource is being used for constants in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_Constants
    
      The resource is being used for constants in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_Constants
    
      The resource is being used for constants in the :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_Constants
    
      The resource is being used for constants in the :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_Constants
    
      The resource is being used for constants in the :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: TS_Constants
    
      The resource is being used as a constants in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    
    .. data:: MS_Constants
    
      The resource is being used as a constants in the :data:`mesh shader <ShaderStage.Mesh>`.
    
    .. data:: All_Constants
    
      The resource is being used for constants in all shader stages.
    
    .. data:: StreamOut
    
      The resource is being used for stream out/transform feedback storage after geometry processing.
    
    .. data:: VS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_Resource
    
      The resource is being used as a read-only resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_Resource
    
      The resource is being used as a read-only resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: TS_Resource
    
      The resource is being used as a read-only resource in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    
    .. data:: MS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`mesh shader <ShaderStage.Mesh>`.
    
    .. data:: All_Resource
    
      The resource is being used as a read-only resource in all shader stages.
    
    
    .. data:: VS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_RWResource
    
      The resource is being used as a read-write resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_RWResource
    
      The resource is being used as a read-write resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: TS_RWResource
    
      The resource is being used as a read-write resource in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    
    .. data:: MS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`mesh shader <ShaderStage.Mesh>`.
    
    .. data:: All_RWResource
    
      The resource is being used as a read-write resource in all shader stages.
    
    .. data:: InputTarget
    
      The resource is being read as an input target for reading from the target currently being written.
    
    .. data:: ColorTarget
    
      The resource is being written to as a color output.
    
    .. data:: DepthStencilTarget
    
      The resource is being written to and tested against as a depth-stencil output.
    
    .. data:: Indirect
    
      The resource is being used for indirect arguments.
    
    .. data:: Clear
    
      The resource is being cleared.
    
    .. data:: Discard
    
      The resource contents are discarded explicitly or implicitly.
    
    .. data:: GenMips
    
      The resource is having mips generated for it.
    
    .. data:: Resolve
    
      The resource is being resolved or blitted, as both source and destination.
    
    .. data:: ResolveSrc
    
      The resource is being resolved or blitted from.
    
    .. data:: ResolveDst
    
      The resource is being resolved or blitted to.
    
    .. data:: Copy
    
      The resource is being copied, as both source and destination.
    
    .. data:: CopySrc
    
      The resource is being copied from.
    
    .. data:: CopyDst
    
      The resource is being copied to.
    
    .. data:: Barrier
    
      The resource is being specified in a barrier, as defined in Vulkan or Direct3D 12.
    
    .. data:: CPUWrite
    
      The resource is written from the CPU, either directly as mapped memory or indirectly via a
      synchronous update.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    All_Constants = 11
    """ The resource is being used for constants in all shader stages. """

    All_Resource = 21
    """ The resource is being used as a read-only resource in all shader stages. """

    All_RWResource = 30
    """ The resource is being used as a read-write resource in all shader stages. """

    Barrier = 44
    """ The resource is being specified in a barrier, as defined in Vulkan or Direct3D 12. """

    Clear = 35
    """ The resource is being cleared. """

    ColorTarget = 32
    """ The resource is being written to as a color output. """

    Copy = 41
    """ The resource is being copied, as both source and destination. """

    CopyDst = 43
    """ The resource is being copied to. """

    CopySrc = 42
    """ The resource is being copied from. """

    CPUWrite = 45
    """
    The resource is written from the CPU, either directly as mapped memory or indirectly via a
      synchronous update.
    """

    CS_Constants = 8
    """ The resource is being used for constants in the :data:`compute shader <ShaderStage.Compute>`. """

    CS_Resource = 18
    """
    The resource is being used as a read-only resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    """

    CS_RWResource = 27
    """
    The resource is being used as a read-write resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    """

    DepthStencilTarget = 33
    """ The resource is being written to and tested against as a depth-stencil output. """

    Discard = 36
    """ The resource contents are discarded explicitly or implicitly. """

    DS_Constants = 5
    """
    The resource is being used for constants in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    """

    DS_Resource = 15
    """
    The resource is being used as a read-only resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    """

    DS_RWResource = 24
    """
    The resource is being used as a read-write resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    """

    GenMips = 37
    """ The resource is having mips generated for it. """

    GS_Constants = 6
    """ The resource is being used for constants in the :data:`geometry shader <ShaderStage.Geometry>`. """

    GS_Resource = 16
    """
    The resource is being used as a read-only resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    """

    GS_RWResource = 25
    """
    The resource is being used as a read-write resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    """

    HS_Constants = 4
    """
    The resource is being used for constants in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    """

    HS_Resource = 14
    """
    The resource is being used as a read-only resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    """

    HS_RWResource = 23
    """
    The resource is being used as a read-write resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    """

    IndexBuffer = 2
    """ The resource is being used as an index buffer. """

    Indirect = 34
    """ The resource is being used for indirect arguments. """

    InputTarget = 31
    """ The resource is being read as an input target for reading from the target currently being written. """

    MS_Constants = 10
    """ The resource is being used as a constants in the :data:`mesh shader <ShaderStage.Mesh>`. """

    MS_Resource = 20
    """
    The resource is being used as a read-only resource in the
      :data:`mesh shader <ShaderStage.Mesh>`.
    """

    MS_RWResource = 29
    """
    The resource is being used as a read-write resource in the
      :data:`mesh shader <ShaderStage.Mesh>`.
    """

    PS_Constants = 7
    """ The resource is being used for constants in the :data:`pixel shader <ShaderStage.Pixel>`. """

    PS_Resource = 17
    """
    The resource is being used as a read-only resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    """

    PS_RWResource = 26
    """
    The resource is being used as a read-write resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    """

    Resolve = 38
    """ The resource is being resolved or blitted, as both source and destination. """

    ResolveDst = 40
    """ The resource is being resolved or blitted to. """

    ResolveSrc = 39
    """ The resource is being resolved or blitted from. """

    StreamOut = 12
    """ The resource is being used for stream out/transform feedback storage after geometry processing. """

    TS_Constants = 9
    """
    The resource is being used as a constants in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    """

    TS_Resource = 19
    """
    The resource is being used as a read-only resource in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    """

    TS_RWResource = 28
    """
    The resource is being used as a read-write resource in the amplification or
      :data:`task shader <ShaderStage.Task>`.
    """

    Unused = 0
    """ The resource is not being used. """

    VertexBuffer = 1
    """ The resource is being used as a fixed-function vertex buffer input. """

    VS_Constants = 3
    """ The resource is being used for constants in the :data:`vertex shader <ShaderStage.Vertex>`. """

    VS_Resource = 13
    """
    The resource is being used as a read-only resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    """

    VS_RWResource = 22
    """
    The resource is being used as a read-write resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    """



