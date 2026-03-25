# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderEncoding(__enum.IntEnum):
    """
    Identifies a shader encoding used to pass shader code to an API.
    
    .. data:: Unknown
    
      Unknown or unprocessable format.
    
    .. data:: DXBC
    
      DXBC binary shader, used by D3D11 and D3D12.
    
    .. data:: GLSL
    
      GLSL in string format, used by OpenGL.
    
    .. data:: SPIRV
    
      SPIR-V binary shader, as used by Vulkan. This format is technically not distinct from
      :data:`OpenGLSPIRV` but is considered unique here since it really *should* have been a different
      format, and introducing a separation allows better selection of tools automatically.
    
    .. data:: SPIRVAsm
    
      Canonical SPIR-V assembly form, used (indirectly via :data:`SPIRV`) by Vulkan. See :data:`SPIRV`.
    
    .. data:: OpenGLSPIRV
    
      SPIR-V binary shader, as used by OpenGL. This format is technically not distinct from
      :data:`VulkanSPIRV` but is considered unique here since it really *should* have been a different
      format, and introducing a separation allows better selection of tools automatically.
    
    .. data:: OpenGLSPIRVAsm
    
      Canonical SPIR-V assembly form, used (indirectly via :data:`OpenGLSPIRV`) by OpenGL. See
      :data:`OpenGLSPIRV` and note that it's artificially differentiated from :data:`SPIRVAsm`.
    
    .. data:: HLSL
    
      HLSL in string format, used by D3D11, D3D12, and Vulkan/GL via compilation to SPIR-V.
    
    .. data:: DXIL
    
      DXIL binary shader, used by D3D12. Note that although the container is still DXBC format this is
      used to distinguish from :data:`DXBC` for compiler I/O matching.
    
    .. data:: Slang
    
      Slang in string format, used by the slang compiler for compilation to multiple backend formats.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Count = 10
    DXBC = 1
    """ DXBC binary shader, used by D3D11 and D3D12. """

    DXIL = 6
    """
    DXIL binary shader, used by D3D12. Note that although the container is still DXBC format this is
      used to distinguish from :data:`DXBC` for compiler I/O matching.
    """

    First = 0
    GLSL = 2
    """ GLSL in string format, used by OpenGL. """

    HLSL = 5
    """ HLSL in string format, used by D3D11, D3D12, and Vulkan/GL via compilation to SPIR-V. """

    OpenGLSPIRV = 7
    """
    SPIR-V binary shader, as used by OpenGL. This format is technically not distinct from
      :data:`VulkanSPIRV` but is considered unique here since it really *should* have been a different
      format, and introducing a separation allows better selection of tools automatically.
    """

    OpenGLSPIRVAsm = 8
    """
    Canonical SPIR-V assembly form, used (indirectly via :data:`OpenGLSPIRV`) by OpenGL. See
      :data:`OpenGLSPIRV` and note that it's artificially differentiated from :data:`SPIRVAsm`.
    """

    Slang = 9
    """ Slang in string format, used by the slang compiler for compilation to multiple backend formats. """

    SPIRV = 3
    """
    SPIR-V binary shader, as used by Vulkan. This format is technically not distinct from
      :data:`OpenGLSPIRV` but is considered unique here since it really *should* have been a different
      format, and introducing a separation allows better selection of tools automatically.
    """

    SPIRVAsm = 4
    """ Canonical SPIR-V assembly form, used (indirectly via :data:`SPIRV`) by Vulkan. See :data:`SPIRV`. """

    Unknown = 0
    """ Unknown or unprocessable format. """



