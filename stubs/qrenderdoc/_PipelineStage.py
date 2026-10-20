from enum import IntEnum

class PipelineStage(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    VertexInput = 0
    """
    The fixed function vertex input stage.
    """
    
    VertexShader = 1
    """
    The vertex shader.
    """
    
    HullShader = 2
    """
    The vertex shader.
    """
    
    DomainShader = 3
    """
    The domain shader.
    """
    
    GeometryShader = 4
    """
    The geometry shader, including stream-out/transform feedback.
    """
    
    Rasterizer = 5
    """
    The fixed function rasterizer stage.
    """
    
    PixelShader = 6
    """
    The pixel shader.
    """
    
    ColorDepthOutput = 7
    """
    The fixed function color and depth output stage, including color blending and depth/stencil
    testing state.
    """
    
    ComputeShader = 8
    """
    The compute shader.
    """
    
    SampleMask = 9
    """
    The sample mask.
    """
    
    # Aliases
    
    TessControlShader = 2
    """
    The tessellation control shader.
    """
    
    TessEvalShader = 3
    """
    The tessellation evaluation shader.
    """
    
    ViewportsScissors = 5
    """
    The viewports and scissors. Helper alias for :data:`Rasterizer`.
    """
    
    FragmentShader = 6
    """
    The fragment shader.
    """
    
    Blending = 7
    """
    The color blending state. Helper alias for :data:`ColorDepthOutput`.
    """
    
    DepthTest = 7
    """
    The depth test state. Helper alias for :data:`ColorDepthOutput`.
    """
    
    StencilTest = 7
    """
    The stencil test state. Helper alias for :data:`ColorDepthOutput`.
    """
    

# Assign __doc__ for enum values for easier introspection

PipelineStage.VertexInput.__doc__ = """
The fixed function vertex input stage.
"""

PipelineStage.VertexShader.__doc__ = """
The vertex shader.
"""

PipelineStage.HullShader.__doc__ = """
The vertex shader.
"""

PipelineStage.DomainShader.__doc__ = """
The domain shader.
"""

PipelineStage.GeometryShader.__doc__ = """
The geometry shader, including stream-out/transform feedback.
"""

PipelineStage.Rasterizer.__doc__ = """
The fixed function rasterizer stage.
"""

PipelineStage.PixelShader.__doc__ = """
The pixel shader.
"""

PipelineStage.ColorDepthOutput.__doc__ = """
The fixed function color and depth output stage, including color blending and depth/stencil
testing state.
"""

PipelineStage.ComputeShader.__doc__ = """
The compute shader.
"""

PipelineStage.SampleMask.__doc__ = """
The sample mask.
"""

PipelineStage.TessControlShader.__doc__ = """
The tessellation control shader.
"""

PipelineStage.TessEvalShader.__doc__ = """
The tessellation evaluation shader.
"""

PipelineStage.ViewportsScissors.__doc__ = """
The viewports and scissors. Helper alias for :data:`Rasterizer`.
"""

PipelineStage.FragmentShader.__doc__ = """
The fragment shader.
"""

PipelineStage.Blending.__doc__ = """
The color blending state. Helper alias for :data:`ColorDepthOutput`.
"""

PipelineStage.DepthTest.__doc__ = """
The depth test state. Helper alias for :data:`ColorDepthOutput`.
"""

PipelineStage.StencilTest.__doc__ = """
The stencil test state. Helper alias for :data:`ColorDepthOutput`.
"""

