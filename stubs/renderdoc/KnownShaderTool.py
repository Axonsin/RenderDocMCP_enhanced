# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class KnownShaderTool(__enum.IntEnum):
    """
    Identifies a particular known tool used for shader processing.
    
    .. data:: Unknown
    
      Corresponds to no known tool.
    
    .. data:: SPIRV_Cross
    
      `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targetting normal Vulkan flavoured SPIR-V.
    
    .. data:: SPIRV_Cross_OpenGL
    
      `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targetting OpenGL extension flavoured SPIR-V.
    
    .. data:: spirv_dis
    
      `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting normal Vulkan flavoured SPIR-V.
    
    .. data:: spirv_dis_OpenGL
    
      `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting OpenGL extension flavoured SPIR-V.
    
    .. data:: glslangValidatorGLSL
    
      `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targetting normal Vulkan flavoured SPIR-V.
    
    .. data:: glslangValidatorGLSL_OpenGL
    
      `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targetting OpenGL extension flavoured SPIR-V.
    
    .. data:: glslangValidatorHLSL
    
      `glslang compiler (HLSL) <https://github.com/KhronosGroup/glslang>`_.
    
    .. data:: spirv_as
    
      `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting normal Vulkan flavoured SPIR-V.
    
    .. data:: spirv_as_OpenGL
    
      `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting OpenGL extension flavoured SPIR-V.
    
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Count = 15
    dxcDXIL = 7
    """ `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with DXIL output. """

    dxcSPIRV = 6
    """
    `DirectX Shader Compiler <https://github.com/microsoft/DirectXShaderCompiler>`_ with Vulkan SPIR-V
       output.
    """

    First = 0
    fxc = 8
    """ fxc Shader Compiler with DXBC output. """

    glslangValidatorGLSL = 3
    """
    `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targetting normal Vulkan flavoured SPIR-V.
    """

    glslangValidatorGLSL_OpenGL = 9
    """
    `glslang compiler (GLSL) <https://github.com/KhronosGroup/glslang>`_
       targetting OpenGL extension flavoured SPIR-V.
    """

    glslangValidatorHLSL = 4
    """ `glslang compiler (HLSL) <https://github.com/KhronosGroup/glslang>`_. """

    slangDXIL = 14
    """ `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with DXIL output. """

    slangSPIRV = 13
    """ `Slang Shader Compiler <https://github.com/shader-slang/slang>`_ with Vulkan SPIR-V output. """

    spirv_as = 5
    """
    `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting normal Vulkan flavoured SPIR-V.
    """

    spirv_as_OpenGL = 11
    """
    `spirv-as from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting OpenGL extension flavoured SPIR-V.
    """

    SPIRV_Cross = 1
    """
    `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targetting normal Vulkan flavoured SPIR-V.
    """

    SPIRV_Cross_OpenGL = 10
    """
    `SPIRV-Cross <https://github.com/KhronosGroup/SPIRV-Cross>`_
       targetting OpenGL extension flavoured SPIR-V.
    """

    spirv_dis = 2
    """
    `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting normal Vulkan flavoured SPIR-V.
    """

    spirv_dis_OpenGL = 12
    """
    `spirv-dis from SPIRV-Tools <https://github.com/KhronosGroup/SPIRV-Tools>`_
       targetting OpenGL extension flavoured SPIR-V.
    """

    Unknown = 0
    """ Corresponds to no known tool. """



