from enum import IntEnum

class ShaderEncoding(IntEnum):
    # Original docstring
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
      :data:`SPIRV` but is considered unique here since it really *should* have been a different
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
    
    
    # Enum values
    
    Unknown = 0
    """
    Unknown or unprocessable format.
    """
    
    DXBC = 1
    """
    DXBC binary shader, used by D3D11 and D3D12.
    """
    
    GLSL = 2
    """
    GLSL in string format, used by OpenGL.
    """
    
    SPIRV = 3
    """
    SPIR-V binary shader, as used by Vulkan. This format is technically not distinct from
    :data:`OpenGLSPIRV` but is considered unique here since it really *should* have been a different
    format, and introducing a separation allows better selection of tools automatically.
    """
    
    SPIRVAsm = 4
    """
    Canonical SPIR-V assembly form, used (indirectly via :data:`SPIRV`) by Vulkan. See :data:`SPIRV`.
    """
    
    HLSL = 5
    """
    HLSL in string format, used by D3D11, D3D12, and Vulkan/GL via compilation to SPIR-V.
    """
    
    DXIL = 6
    """
    DXIL binary shader, used by D3D12. Note that although the container is still DXBC format this is
    used to distinguish from :data:`DXBC` for compiler I/O matching.
    """
    
    OpenGLSPIRV = 7
    """
    SPIR-V binary shader, as used by OpenGL. This format is technically not distinct from
    :data:`SPIRV` but is considered unique here since it really *should* have been a different
    format, and introducing a separation allows better selection of tools automatically.
    """
    
    OpenGLSPIRVAsm = 8
    """
    Canonical SPIR-V assembly form, used (indirectly via :data:`OpenGLSPIRV`) by OpenGL. See
    :data:`OpenGLSPIRV` and note that it's artificially differentiated from :data:`SPIRVAsm`.
    """
    
    Slang = 9
    """
    Slang in string format, used by the slang compiler for compilation to multiple backend formats.
    """
    
    Count = 10
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderEncoding.Unknown.__doc__ = """
Unknown or unprocessable format.
"""

ShaderEncoding.DXBC.__doc__ = """
DXBC binary shader, used by D3D11 and D3D12.
"""

ShaderEncoding.GLSL.__doc__ = """
GLSL in string format, used by OpenGL.
"""

ShaderEncoding.SPIRV.__doc__ = """
SPIR-V binary shader, as used by Vulkan. This format is technically not distinct from
:data:`OpenGLSPIRV` but is considered unique here since it really *should* have been a different
format, and introducing a separation allows better selection of tools automatically.
"""

ShaderEncoding.SPIRVAsm.__doc__ = """
Canonical SPIR-V assembly form, used (indirectly via :data:`SPIRV`) by Vulkan. See :data:`SPIRV`.
"""

ShaderEncoding.HLSL.__doc__ = """
HLSL in string format, used by D3D11, D3D12, and Vulkan/GL via compilation to SPIR-V.
"""

ShaderEncoding.DXIL.__doc__ = """
DXIL binary shader, used by D3D12. Note that although the container is still DXBC format this is
used to distinguish from :data:`DXBC` for compiler I/O matching.
"""

ShaderEncoding.OpenGLSPIRV.__doc__ = """
SPIR-V binary shader, as used by OpenGL. This format is technically not distinct from
:data:`SPIRV` but is considered unique here since it really *should* have been a different
format, and introducing a separation allows better selection of tools automatically.
"""

ShaderEncoding.OpenGLSPIRVAsm.__doc__ = """
Canonical SPIR-V assembly form, used (indirectly via :data:`OpenGLSPIRV`) by OpenGL. See
:data:`OpenGLSPIRV` and note that it's artificially differentiated from :data:`SPIRVAsm`.
"""

ShaderEncoding.Slang.__doc__ = """
Slang in string format, used by the slang compiler for compilation to multiple backend formats.
"""

ShaderEncoding.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

ShaderEncoding.First.__doc__ = """
The first enum value, for ease of iteration.
"""

