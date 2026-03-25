# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PipelineStage(__enum.IntEnum):
    """
    Specifies a pipeline stage for the :class:`PipelineStateViewer`.
    
    .. data:: VertexInput
    
      The fixed function vertex input stage.
    
    .. data:: VertexShader
    
      The vertex shader.
    
    .. data:: HullShader
    
      The vertex shader.
    
    .. data:: TessControlShader
    
      The tessellation control shader.
    
    .. data:: DomainShader
    
      The domain shader.
    
    .. data:: TessEvalShader
    
      The tessellation evaluation shader.
    
    .. data:: GeometryShader
    
      The geometry shader, including stream-out/transform feedback.
    
    .. data:: Rasterizer
    
      The fixed function rasterizer stage.
    
    .. data:: ViewportsScissors
    
      The viewports and scissors. Helper alias for :data:`Rasterizer`.
    
    .. data:: PixelShader
    
      The pixel shader.
    
    .. data:: FragmentShader
    
      The fragment shader.
    
    .. data:: ColorDepthOutput
    
      The fixed function color and depth output stage, including color blending and depth/stencil
      testing state.
    
    .. data:: Blending
    
      The color blending state. Helper alias for :data:`ColorDepthOutput`.
    
    .. data:: DepthTest
    
      The depth test state. Helper alias for :data:`ColorDepthOutput`.
    
    .. data:: StencilTest
    
      The stencil test state. Helper alias for :data:`ColorDepthOutput`.
    
    .. data:: ComputeShader
    
      The compute shader.
    
    .. data:: SampleMask
    
      The sample mask.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Blending = 7
    """ The color blending state. Helper alias for :data:`ColorDepthOutput`. """

    ColorDepthOutput = 7
    """
    The fixed function color and depth output stage, including color blending and depth/stencil
      testing state.
    """

    ComputeShader = 8
    """ The compute shader. """

    DepthTest = 7
    """ The depth test state. Helper alias for :data:`ColorDepthOutput`. """

    DomainShader = 3
    """ The domain shader. """

    FragmentShader = 6
    """ The fragment shader. """

    GeometryShader = 4
    """ The geometry shader, including stream-out/transform feedback. """

    HullShader = 2
    """ The vertex shader. """

    PixelShader = 6
    """ The pixel shader. """

    Rasterizer = 5
    """ The fixed function rasterizer stage. """

    SampleMask = 9
    """ The sample mask. """

    StencilTest = 7
    """ The stencil test state. Helper alias for :data:`ColorDepthOutput`. """

    TessControlShader = 2
    """ The tessellation control shader. """

    TessEvalShader = 3
    """ The tessellation evaluation shader. """

    VertexInput = 0
    """ The fixed function vertex input stage. """

    VertexShader = 1
    """ The vertex shader. """

    ViewportsScissors = 5
    """ The viewports and scissors. Helper alias for :data:`Rasterizer`. """



