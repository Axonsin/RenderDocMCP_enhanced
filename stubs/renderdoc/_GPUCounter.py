from enum import IntEnum

class GPUCounter(IntEnum):
    # Original docstring
    """
    Pre-defined GPU counters that can be supported by a given implementation.
    
    GPU counters actually available can be queried by :meth:`ReplayController.EnumerateCounters`. If any
    in this list are supported they will be returned with these counter IDs. More counters may be
    enumerated with IDs in the appropriate ranges.
    
    .. data:: EventGPUDuration
    
      Time taken for this event on the GPU, as measured by delta between two GPU timestamps.
    
    .. data:: InputVerticesRead
    
      Number of vertices read by input assembler.
    
    .. data:: IAPrimitives
    
      Number of primitives read by the input assembler.
    
    .. data:: GSPrimitives
    
      Number of primitives output by a geometry shader.
    
    .. data:: RasterizerInvocations
    
      Number of primitives that were sent to the rasterizer.
    
    .. data:: RasterizedPrimitives
    
      Number of primitives that were rendered.
    
    .. data:: SamplesPassed
    
      Number of samples that passed depth/stencil test.
    
    .. data:: VSInvocations
    
      Number of times a :data:`vertex shader <ShaderStage.Vertex>` was invoked.
    
    .. data:: HSInvocations
    
      Number of times a :data:`hull shader <ShaderStage.Hull>` was invoked.
    
    .. data:: TCSInvocations
    
      Number of times a :data:`tessellation control shader <ShaderStage.Tess_Control>` was invoked.
    
    .. data:: DSInvocations
    
      Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    
    .. data:: TESInvocations
    
      Number of times a :data:`tessellation evaluation shader <ShaderStage.Tess_Eval>` was invoked.
    
    .. data:: GSInvocations
    
      Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    
    .. data:: PSInvocations
    
      Number of times a :data:`pixel shader <ShaderStage.Pixel>` was invoked.
    
    .. data:: FSInvocations
    
      Number of times a :data:`fragment shader <ShaderStage.Fragment>` was invoked.
    
    .. data:: CSInvocations
    
      Number of times a :data:`compute shader <ShaderStage.Compute>` was invoked.
    
    .. data:: TSInvocations
    
      Number of times a :data:`task shader <ShaderStage.Task>` was invoked.
    
    .. data:: ASInvocations
    
      Number of times a :data:`amplification shader <ShaderStage.Amplification>` was invoked.
    
    .. data:: MSInvocations
    
      Number of times a :data:`mesh shader <ShaderStage.Mesh>` was invoked.
    
    .. data:: FirstAMD
    
      The AMD-specific counter IDs start from this value.
    
    .. data:: LastAMD
    
      The AMD-specific counter IDs end with this value.
    
    .. data:: FirstIntel
    
      The Intel-specific counter IDs start from this value.
    
    .. data:: LastIntel
    
      The Intel-specific counter IDs end with this value.
    
    .. data:: FirstNvidia
    
      The nVidia-specific counter IDs start from this value.
    
    .. data:: LastNvidia
    
      The nVidia-specific counter IDs end with this value.
    
    .. data:: FirstVulkanExtended
    
      The Vulkan extended counter IDs start from this value.
    
    .. data:: LastVulkanExtended
    
      The Vulkan extended counter IDs end with this value.
    
    .. data:: FirstARM
    
      The ARM-specific counter IDs start from this value.
    
    .. data:: LastARM
    
      The ARM-specific counter IDs end with this value.
    """
    
    
    # Enum values
    
    EventGPUDuration = 1
    """
    Time taken for this event on the GPU, as measured by delta between two GPU timestamps.
    """
    
    InputVerticesRead = 2
    """
    Number of vertices read by input assembler.
    """
    
    IAPrimitives = 3
    """
    Number of primitives read by the input assembler.
    """
    
    GSPrimitives = 4
    """
    Number of primitives output by a geometry shader.
    """
    
    RasterizerInvocations = 5
    """
    Number of primitives that were sent to the rasterizer.
    """
    
    RasterizedPrimitives = 6
    """
    Number of primitives that were rendered.
    """
    
    SamplesPassed = 7
    """
    Number of samples that passed depth/stencil test.
    """
    
    VSInvocations = 8
    """
    Number of times a :data:`vertex shader <ShaderStage.Vertex>` was invoked.
    """
    
    HSInvocations = 9
    """
    Number of times a :data:`hull shader <ShaderStage.Hull>` was invoked.
    """
    
    DSInvocations = 10
    """
    Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    """
    
    GSInvocations = 11
    """
    Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    """
    
    PSInvocations = 12
    """
    Number of times a :data:`pixel shader <ShaderStage.Pixel>` was invoked.
    """
    
    CSInvocations = 13
    """
    Number of times a :data:`compute shader <ShaderStage.Compute>` was invoked.
    """
    
    ASInvocations = 14
    """
    Number of times a :data:`amplification shader <ShaderStage.Amplification>` was invoked.
    """
    
    MSInvocations = 15
    """
    Number of times a :data:`mesh shader <ShaderStage.Mesh>` was invoked.
    """
    
    Count = 16
    """
    The number of values in the enum, for ease of iteration.
    """
    
    FirstAMD = 1000000
    """
    The AMD-specific counter IDs start from this value.
    """
    
    FirstIntel = 2000000
    """
    The Intel-specific counter IDs start from this value.
    """
    
    LastAMD = 1999999
    """
    The AMD-specific counter IDs end with this value.
    """
    
    FirstNvidia = 3000000
    """
    The nVidia-specific counter IDs start from this value.
    """
    
    LastIntel = 2999999
    """
    The Intel-specific counter IDs end with this value.
    """
    
    FirstVulkanExtended = 4000000
    """
    The Vulkan extended counter IDs start from this value.
    """
    
    LastNvidia = 3999999
    """
    The nVidia-specific counter IDs end with this value.
    """
    
    FirstARM = 5000000
    """
    The ARM-specific counter IDs start from this value.
    """
    
    LastVulkanExtended = 4999999
    """
    The Vulkan extended counter IDs end with this value.
    """
    
    LastARM = 6000000
    """
    The ARM-specific counter IDs end with this value.
    """
    
    # Aliases
    
    First = 1
    """
    The first enum value, for ease of iteration.
    """
    
    TCSInvocations = 9
    """
    Number of times a :data:`tessellation control shader <ShaderStage.Tess_Control>` was invoked.
    """
    
    TESInvocations = 10
    """
    Number of times a :data:`tessellation evaluation shader <ShaderStage.Tess_Eval>` was invoked.
    """
    
    FSInvocations = 12
    """
    Number of times a :data:`fragment shader <ShaderStage.Fragment>` was invoked.
    """
    
    TSInvocations = 14
    """
    Number of times a :data:`task shader <ShaderStage.Task>` was invoked.
    """
    

# Assign __doc__ for enum values for easier introspection

GPUCounter.EventGPUDuration.__doc__ = """
Time taken for this event on the GPU, as measured by delta between two GPU timestamps.
"""

GPUCounter.InputVerticesRead.__doc__ = """
Number of vertices read by input assembler.
"""

GPUCounter.IAPrimitives.__doc__ = """
Number of primitives read by the input assembler.
"""

GPUCounter.GSPrimitives.__doc__ = """
Number of primitives output by a geometry shader.
"""

GPUCounter.RasterizerInvocations.__doc__ = """
Number of primitives that were sent to the rasterizer.
"""

GPUCounter.RasterizedPrimitives.__doc__ = """
Number of primitives that were rendered.
"""

GPUCounter.SamplesPassed.__doc__ = """
Number of samples that passed depth/stencil test.
"""

GPUCounter.VSInvocations.__doc__ = """
Number of times a :data:`vertex shader <ShaderStage.Vertex>` was invoked.
"""

GPUCounter.HSInvocations.__doc__ = """
Number of times a :data:`hull shader <ShaderStage.Hull>` was invoked.
"""

GPUCounter.DSInvocations.__doc__ = """
Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
"""

GPUCounter.GSInvocations.__doc__ = """
Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
"""

GPUCounter.PSInvocations.__doc__ = """
Number of times a :data:`pixel shader <ShaderStage.Pixel>` was invoked.
"""

GPUCounter.CSInvocations.__doc__ = """
Number of times a :data:`compute shader <ShaderStage.Compute>` was invoked.
"""

GPUCounter.ASInvocations.__doc__ = """
Number of times a :data:`amplification shader <ShaderStage.Amplification>` was invoked.
"""

GPUCounter.MSInvocations.__doc__ = """
Number of times a :data:`mesh shader <ShaderStage.Mesh>` was invoked.
"""

GPUCounter.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

GPUCounter.FirstAMD.__doc__ = """
The AMD-specific counter IDs start from this value.
"""

GPUCounter.FirstIntel.__doc__ = """
The Intel-specific counter IDs start from this value.
"""

GPUCounter.LastAMD.__doc__ = """
The AMD-specific counter IDs end with this value.
"""

GPUCounter.FirstNvidia.__doc__ = """
The nVidia-specific counter IDs start from this value.
"""

GPUCounter.LastIntel.__doc__ = """
The Intel-specific counter IDs end with this value.
"""

GPUCounter.FirstVulkanExtended.__doc__ = """
The Vulkan extended counter IDs start from this value.
"""

GPUCounter.LastNvidia.__doc__ = """
The nVidia-specific counter IDs end with this value.
"""

GPUCounter.FirstARM.__doc__ = """
The ARM-specific counter IDs start from this value.
"""

GPUCounter.LastVulkanExtended.__doc__ = """
The Vulkan extended counter IDs end with this value.
"""

GPUCounter.LastARM.__doc__ = """
The ARM-specific counter IDs end with this value.
"""

GPUCounter.First.__doc__ = """
The first enum value, for ease of iteration.
"""

GPUCounter.TCSInvocations.__doc__ = """
Number of times a :data:`tessellation control shader <ShaderStage.Tess_Control>` was invoked.
"""

GPUCounter.TESInvocations.__doc__ = """
Number of times a :data:`tessellation evaluation shader <ShaderStage.Tess_Eval>` was invoked.
"""

GPUCounter.FSInvocations.__doc__ = """
Number of times a :data:`fragment shader <ShaderStage.Fragment>` was invoked.
"""

GPUCounter.TSInvocations.__doc__ = """
Number of times a :data:`task shader <ShaderStage.Task>` was invoked.
"""

