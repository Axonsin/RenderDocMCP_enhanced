from enum import IntEnum

class KnownShaderTool(IntEnum):
    # Original docstring
    """
    Identifies a particular known tool used for shader processing.
    
    .. data:: Unknown
    
      Corresponds to no known tool.
    
    .. data:: SPIRV_Cross
    
      `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targeting normal Vulkan flavoured SPIR-V.
    
    .. data:: SPIRV_Cross_OpenGL
    
      `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targeting OpenGL extension flavoured SPIR-V.
    
    .. data:: spirv_dis
    
      `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targeting normal Vulkan flavoured SPIR-V.
    
    .. data:: spirv_dis_OpenGL
    
      `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targeting OpenGL extension flavoured SPIR-V.
    
    .. data:: glslangValidatorGLSL
    
      `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targeting normal Vulkan flavoured SPIR-V.
    
    .. data:: glslangValidatorGLSL_OpenGL
    
      `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targeting OpenGL extension flavoured SPIR-V.
    
    .. data:: glslangValidatorHLSL
    
      `glslang compiler (HLSL) <https://github.com/KhronosGroup/glslang>`_.
    
    .. data:: spirv_as
    
      `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targeting normal Vulkan flavoured SPIR-V.
    
    .. data:: spirv_as_OpenGL
    
      `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targeting OpenGL extension flavoured SPIR-V.
    
    .. data:: dxcSPIRV
    
      `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with Vulkan SPIR-V
       output.
    
    .. data:: dxcDXIL
    
      `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with DXIL output.
    
    .. data:: fxc
    
      fxc Shader Compiler with DXBC output.
    
    .. data:: slangSPIRV
    
      `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with Vulkan SPIR-V output.
    
    .. data:: slangDXIL
    
      `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with DXIL output.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    Corresponds to no known tool.
    """
    
    SPIRV_Cross = 1
    """
    `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
     targeting normal Vulkan flavoured SPIR-V.
    """
    
    spirv_dis = 2
    """
    `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
     targeting normal Vulkan flavoured SPIR-V.
    """
    
    glslangValidatorGLSL = 3
    """
    `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
     targeting normal Vulkan flavoured SPIR-V.
    """
    
    glslangValidatorHLSL = 4
    """
    `glslang compiler (HLSL) <https://github.com/KhronosGroup/glslang>`_.
    """
    
    spirv_as = 5
    """
    `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
     targeting normal Vulkan flavoured SPIR-V.
    """
    
    dxcSPIRV = 6
    """
    `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with Vulkan SPIR-V
     output.
    """
    
    dxcDXIL = 7
    """
    `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with DXIL output.
    """
    
    fxc = 8
    """
    fxc Shader Compiler with DXBC output.
    """
    
    glslangValidatorGLSL_OpenGL = 9
    """
    `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
     targeting OpenGL extension flavoured SPIR-V.
    """
    
    SPIRV_Cross_OpenGL = 10
    """
    `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
     targeting OpenGL extension flavoured SPIR-V.
    """
    
    spirv_as_OpenGL = 11
    """
    `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
     targeting OpenGL extension flavoured SPIR-V.
    """
    
    spirv_dis_OpenGL = 12
    """
    `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
     targeting OpenGL extension flavoured SPIR-V.
    """
    
    slangSPIRV = 13
    """
    `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with Vulkan SPIR-V output.
    """
    
    slangDXIL = 14
    """
    `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with DXIL output.
    """
    
    Count = 15
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

KnownShaderTool.Unknown.__doc__ = """
Corresponds to no known tool.
"""

KnownShaderTool.SPIRV_Cross.__doc__ = """
`SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
 targeting normal Vulkan flavoured SPIR-V.
"""

KnownShaderTool.spirv_dis.__doc__ = """
`spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
 targeting normal Vulkan flavoured SPIR-V.
"""

KnownShaderTool.glslangValidatorGLSL.__doc__ = """
`glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
 targeting normal Vulkan flavoured SPIR-V.
"""

KnownShaderTool.glslangValidatorHLSL.__doc__ = """
`glslang compiler (HLSL) <https://github.com/KhronosGroup/glslang>`_.
"""

KnownShaderTool.spirv_as.__doc__ = """
`spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
 targeting normal Vulkan flavoured SPIR-V.
"""

KnownShaderTool.dxcSPIRV.__doc__ = """
`DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with Vulkan SPIR-V
 output.
"""

KnownShaderTool.dxcDXIL.__doc__ = """
`DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with DXIL output.
"""

KnownShaderTool.fxc.__doc__ = """
fxc Shader Compiler with DXBC output.
"""

KnownShaderTool.glslangValidatorGLSL_OpenGL.__doc__ = """
`glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
 targeting OpenGL extension flavoured SPIR-V.
"""

KnownShaderTool.SPIRV_Cross_OpenGL.__doc__ = """
`SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
 targeting OpenGL extension flavoured SPIR-V.
"""

KnownShaderTool.spirv_as_OpenGL.__doc__ = """
`spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
 targeting OpenGL extension flavoured SPIR-V.
"""

KnownShaderTool.spirv_dis_OpenGL.__doc__ = """
`spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
 targeting OpenGL extension flavoured SPIR-V.
"""

KnownShaderTool.slangSPIRV.__doc__ = """
`Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with Vulkan SPIR-V output.
"""

KnownShaderTool.slangDXIL.__doc__ = """
`Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with DXIL output.
"""

KnownShaderTool.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

KnownShaderTool.First.__doc__ = """
The first enum value, for ease of iteration.
"""

