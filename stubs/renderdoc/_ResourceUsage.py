from enum import IntEnum

class ResourceUsage(IntEnum):
    # Original docstring
    """
    How a resource is being used in the pipeline at a particular point.
    
    Note that a resource may be used for more than one thing in one event, see :class:`EventUsage`.
    
    .. data:: Unused
    
      The resource is not being tracked for usage at any event.
    
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
    
    
    # Enum values
    
    Unused = 0
    """
    The resource is not being tracked for usage at any event.
    """
    
    VertexBuffer = 1
    """
    The resource is being used as a fixed-function vertex buffer input.
    """
    
    IndexBuffer = 2
    """
    The resource is being used as an index buffer.
    """
    
    VS_Constants = 3
    """
    The resource is being used for constants in the :data:`vertex shader <ShaderStage.Vertex>`.
    """
    
    HS_Constants = 4
    """
    The resource is being used for constants in the tessellation control or
    :data:`hull shader <ShaderStage.Hull>`.
    """
    
    DS_Constants = 5
    """
    The resource is being used for constants in the tessellation evaluation or
    :data:`domain shader <ShaderStage.Domain>`.
    """
    
    GS_Constants = 6
    """
    The resource is being used for constants in the :data:`geometry shader <ShaderStage.Geometry>`.
    """
    
    PS_Constants = 7
    """
    The resource is being used for constants in the :data:`pixel shader <ShaderStage.Pixel>`.
    """
    
    CS_Constants = 8
    """
    The resource is being used for constants in the :data:`compute shader <ShaderStage.Compute>`.
    """
    
    TS_Constants = 9
    """
    The resource is being used as a constants in the amplification or
    :data:`task shader <ShaderStage.Task>`.
    """
    
    MS_Constants = 10
    """
    The resource is being used as a constants in the :data:`mesh shader <ShaderStage.Mesh>`.
    """
    
    All_Constants = 11
    """
    The resource is being used for constants in all shader stages.
    """
    
    StreamOut = 12
    """
    The resource is being used for stream out/transform feedback storage after geometry processing.
    """
    
    VS_Resource = 13
    """
    The resource is being used as a read-only resource in the
    :data:`vertex shader <ShaderStage.Vertex>`.
    """
    
    HS_Resource = 14
    """
    The resource is being used as a read-only resource in the tessellation control or
    :data:`hull shader <ShaderStage.Hull>`.
    """
    
    DS_Resource = 15
    """
    The resource is being used as a read-only resource in the tessellation evaluation or
    :data:`domain shader <ShaderStage.Domain>`.
    """
    
    GS_Resource = 16
    """
    The resource is being used as a read-only resource in the
    :data:`geometry shader <ShaderStage.Geometry>`.
    """
    
    PS_Resource = 17
    """
    The resource is being used as a read-only resource in the
    :data:`pixel shader <ShaderStage.Pixel>`.
    """
    
    CS_Resource = 18
    """
    The resource is being used as a read-only resource in the
    :data:`compute shader <ShaderStage.Compute>`.
    """
    
    TS_Resource = 19
    """
    The resource is being used as a read-only resource in the amplification or
    :data:`task shader <ShaderStage.Task>`.
    """
    
    MS_Resource = 20
    """
    The resource is being used as a read-only resource in the
    :data:`mesh shader <ShaderStage.Mesh>`.
    """
    
    All_Resource = 21
    """
    The resource is being used as a read-only resource in all shader stages.
    """
    
    VS_RWResource = 22
    """
    The resource is being used as a read-write resource in the
    :data:`vertex shader <ShaderStage.Vertex>`.
    """
    
    HS_RWResource = 23
    """
    The resource is being used as a read-write resource in the tessellation control or
    :data:`hull shader <ShaderStage.Hull>`.
    """
    
    DS_RWResource = 24
    """
    The resource is being used as a read-write resource in the tessellation evaluation or
    :data:`domain shader <ShaderStage.Domain>`.
    """
    
    GS_RWResource = 25
    """
    The resource is being used as a read-write resource in the
    :data:`geometry shader <ShaderStage.Geometry>`.
    """
    
    PS_RWResource = 26
    """
    The resource is being used as a read-write resource in the
    :data:`pixel shader <ShaderStage.Pixel>`.
    """
    
    CS_RWResource = 27
    """
    The resource is being used as a read-write resource in the
    :data:`compute shader <ShaderStage.Compute>`.
    """
    
    TS_RWResource = 28
    """
    The resource is being used as a read-write resource in the amplification or
    :data:`task shader <ShaderStage.Task>`.
    """
    
    MS_RWResource = 29
    """
    The resource is being used as a read-write resource in the
    :data:`mesh shader <ShaderStage.Mesh>`.
    """
    
    All_RWResource = 30
    """
    The resource is being used as a read-write resource in all shader stages.
    """
    
    InputTarget = 31
    """
    The resource is being read as an input target for reading from the target currently being written.
    """
    
    ColorTarget = 32
    """
    The resource is being written to as a color output.
    """
    
    DepthStencilTarget = 33
    """
    The resource is being written to and tested against as a depth-stencil output.
    """
    
    Indirect = 34
    """
    The resource is being used for indirect arguments.
    """
    
    Clear = 35
    """
    The resource is being cleared.
    """
    
    Discard = 36
    """
    The resource contents are discarded explicitly or implicitly.
    """
    
    GenMips = 37
    """
    The resource is having mips generated for it.
    """
    
    Resolve = 38
    """
    The resource is being resolved or blitted, as both source and destination.
    """
    
    ResolveSrc = 39
    """
    The resource is being resolved or blitted from.
    """
    
    ResolveDst = 40
    """
    The resource is being resolved or blitted to.
    """
    
    Copy = 41
    """
    The resource is being copied, as both source and destination.
    """
    
    CopySrc = 42
    """
    The resource is being copied from.
    """
    
    CopyDst = 43
    """
    The resource is being copied to.
    """
    
    Barrier = 44
    """
    The resource is being specified in a barrier, as defined in Vulkan or Direct3D 12.
    """
    
    CPUWrite = 45
    """
    The resource is written from the CPU, either directly as mapped memory or indirectly via a
    synchronous update.
    """
    

# Assign __doc__ for enum values for easier introspection

ResourceUsage.Unused.__doc__ = """
The resource is not being tracked for usage at any event.
"""

ResourceUsage.VertexBuffer.__doc__ = """
The resource is being used as a fixed-function vertex buffer input.
"""

ResourceUsage.IndexBuffer.__doc__ = """
The resource is being used as an index buffer.
"""

ResourceUsage.VS_Constants.__doc__ = """
The resource is being used for constants in the :data:`vertex shader <ShaderStage.Vertex>`.
"""

ResourceUsage.HS_Constants.__doc__ = """
The resource is being used for constants in the tessellation control or
:data:`hull shader <ShaderStage.Hull>`.
"""

ResourceUsage.DS_Constants.__doc__ = """
The resource is being used for constants in the tessellation evaluation or
:data:`domain shader <ShaderStage.Domain>`.
"""

ResourceUsage.GS_Constants.__doc__ = """
The resource is being used for constants in the :data:`geometry shader <ShaderStage.Geometry>`.
"""

ResourceUsage.PS_Constants.__doc__ = """
The resource is being used for constants in the :data:`pixel shader <ShaderStage.Pixel>`.
"""

ResourceUsage.CS_Constants.__doc__ = """
The resource is being used for constants in the :data:`compute shader <ShaderStage.Compute>`.
"""

ResourceUsage.TS_Constants.__doc__ = """
The resource is being used as a constants in the amplification or
:data:`task shader <ShaderStage.Task>`.
"""

ResourceUsage.MS_Constants.__doc__ = """
The resource is being used as a constants in the :data:`mesh shader <ShaderStage.Mesh>`.
"""

ResourceUsage.All_Constants.__doc__ = """
The resource is being used for constants in all shader stages.
"""

ResourceUsage.StreamOut.__doc__ = """
The resource is being used for stream out/transform feedback storage after geometry processing.
"""

ResourceUsage.VS_Resource.__doc__ = """
The resource is being used as a read-only resource in the
:data:`vertex shader <ShaderStage.Vertex>`.
"""

ResourceUsage.HS_Resource.__doc__ = """
The resource is being used as a read-only resource in the tessellation control or
:data:`hull shader <ShaderStage.Hull>`.
"""

ResourceUsage.DS_Resource.__doc__ = """
The resource is being used as a read-only resource in the tessellation evaluation or
:data:`domain shader <ShaderStage.Domain>`.
"""

ResourceUsage.GS_Resource.__doc__ = """
The resource is being used as a read-only resource in the
:data:`geometry shader <ShaderStage.Geometry>`.
"""

ResourceUsage.PS_Resource.__doc__ = """
The resource is being used as a read-only resource in the
:data:`pixel shader <ShaderStage.Pixel>`.
"""

ResourceUsage.CS_Resource.__doc__ = """
The resource is being used as a read-only resource in the
:data:`compute shader <ShaderStage.Compute>`.
"""

ResourceUsage.TS_Resource.__doc__ = """
The resource is being used as a read-only resource in the amplification or
:data:`task shader <ShaderStage.Task>`.
"""

ResourceUsage.MS_Resource.__doc__ = """
The resource is being used as a read-only resource in the
:data:`mesh shader <ShaderStage.Mesh>`.
"""

ResourceUsage.All_Resource.__doc__ = """
The resource is being used as a read-only resource in all shader stages.
"""

ResourceUsage.VS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the
:data:`vertex shader <ShaderStage.Vertex>`.
"""

ResourceUsage.HS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the tessellation control or
:data:`hull shader <ShaderStage.Hull>`.
"""

ResourceUsage.DS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the tessellation evaluation or
:data:`domain shader <ShaderStage.Domain>`.
"""

ResourceUsage.GS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the
:data:`geometry shader <ShaderStage.Geometry>`.
"""

ResourceUsage.PS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the
:data:`pixel shader <ShaderStage.Pixel>`.
"""

ResourceUsage.CS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the
:data:`compute shader <ShaderStage.Compute>`.
"""

ResourceUsage.TS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the amplification or
:data:`task shader <ShaderStage.Task>`.
"""

ResourceUsage.MS_RWResource.__doc__ = """
The resource is being used as a read-write resource in the
:data:`mesh shader <ShaderStage.Mesh>`.
"""

ResourceUsage.All_RWResource.__doc__ = """
The resource is being used as a read-write resource in all shader stages.
"""

ResourceUsage.InputTarget.__doc__ = """
The resource is being read as an input target for reading from the target currently being written.
"""

ResourceUsage.ColorTarget.__doc__ = """
The resource is being written to as a color output.
"""

ResourceUsage.DepthStencilTarget.__doc__ = """
The resource is being written to and tested against as a depth-stencil output.
"""

ResourceUsage.Indirect.__doc__ = """
The resource is being used for indirect arguments.
"""

ResourceUsage.Clear.__doc__ = """
The resource is being cleared.
"""

ResourceUsage.Discard.__doc__ = """
The resource contents are discarded explicitly or implicitly.
"""

ResourceUsage.GenMips.__doc__ = """
The resource is having mips generated for it.
"""

ResourceUsage.Resolve.__doc__ = """
The resource is being resolved or blitted, as both source and destination.
"""

ResourceUsage.ResolveSrc.__doc__ = """
The resource is being resolved or blitted from.
"""

ResourceUsage.ResolveDst.__doc__ = """
The resource is being resolved or blitted to.
"""

ResourceUsage.Copy.__doc__ = """
The resource is being copied, as both source and destination.
"""

ResourceUsage.CopySrc.__doc__ = """
The resource is being copied from.
"""

ResourceUsage.CopyDst.__doc__ = """
The resource is being copied to.
"""

ResourceUsage.Barrier.__doc__ = """
The resource is being specified in a barrier, as defined in Vulkan or Direct3D 12.
"""

ResourceUsage.CPUWrite.__doc__ = """
The resource is written from the CPU, either directly as mapped memory or indirectly via a
synchronous update.
"""

