# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GPUCounter(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    ASInvocations = 14
    """ Number of times a :data:`amplification shader <ShaderStage.Amplification>` was invoked. """

    Count = 16
    CSInvocations = 13
    """ Number of times a :data:`compute shader <ShaderStage.Compute>` was invoked. """

    DSInvocations = 10
    """ Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked. """

    EventGPUDuration = 1
    """ Time taken for this event on the GPU, as measured by delta between two GPU timestamps. """

    First = 1
    FirstAMD = 1000000
    """ The AMD-specific counter IDs start from this value. """

    FirstARM = 5000000
    """ The ARM-specific counter IDs start from this value. """

    FirstIntel = 2000000
    """ The Intel-specific counter IDs start from this value. """

    FirstNvidia = 3000000
    """ The nVidia-specific counter IDs start from this value. """

    FirstVulkanExtended = 4000000
    """ The Vulkan extended counter IDs start from this value. """

    FSInvocations = 12
    """ Number of times a :data:`fragment shader <ShaderStage.Fragment>` was invoked. """

    GSInvocations = 11
    """ Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked. """

    GSPrimitives = 4
    """ Number of primitives output by a geometry shader. """

    HSInvocations = 9
    """ Number of times a :data:`hull shader <ShaderStage.Hull>` was invoked. """

    IAPrimitives = 3
    """ Number of primitives read by the input assembler. """

    InputVerticesRead = 2
    """ Number of vertices read by input assembler. """

    LastAMD = 1999999
    """ The AMD-specific counter IDs end with this value. """

    LastARM = 6000000
    """ The ARM-specific counter IDs end with this value. """

    LastIntel = 2999999
    """ The Intel-specific counter IDs end with this value. """

    LastNvidia = 3999999
    """ The nVidia-specific counter IDs end with this value. """

    LastVulkanExtended = 4999999
    """ The Vulkan extended counter IDs end with this value. """

    MSInvocations = 15
    """ Number of times a :data:`mesh shader <ShaderStage.Mesh>` was invoked. """

    PSInvocations = 12
    """ Number of times a :data:`pixel shader <ShaderStage.Pixel>` was invoked. """

    RasterizedPrimitives = 6
    """ Number of primitives that were rendered. """

    RasterizerInvocations = 5
    """ Number of primitives that were sent to the rasterizer. """

    SamplesPassed = 7
    """ Number of samples that passed depth/stencil test. """

    TCSInvocations = 9
    """ Number of times a :data:`tessellation control shader <ShaderStage.Tess_Control>` was invoked. """

    TESInvocations = 10
    """ Number of times a :data:`tessellation evaluation shader <ShaderStage.Tess_Eval>` was invoked. """

    TSInvocations = 14
    """ Number of times a :data:`task shader <ShaderStage.Task>` was invoked. """

    VSInvocations = 8
    """ Number of times a :data:`vertex shader <ShaderStage.Vertex>` was invoked. """



