from enum import IntEnum

class GraphicsAPI(IntEnum):
    # Original docstring
    """
    Identifies a Graphics API.
    
    .. data:: D3D11
    
      Direct3D 11.
    
    .. data:: D3D12
    
      Direct3D 12.
    
    .. data:: OpenGL
    
      OpenGL.
    
    .. data:: Vulkan
    
      Vulkan.
    """
    
    
    # Enum values
    
    D3D11 = 0
    """
    Direct3D 11.
    """
    
    D3D12 = 1
    """
    Direct3D 12.
    """
    
    OpenGL = 2
    """
    OpenGL.
    """
    
    Vulkan = 3
    """
    Vulkan.
    """
    

# Assign __doc__ for enum values for easier introspection

GraphicsAPI.D3D11.__doc__ = """
Direct3D 11.
"""

GraphicsAPI.D3D12.__doc__ = """
Direct3D 12.
"""

GraphicsAPI.OpenGL.__doc__ = """
OpenGL.
"""

GraphicsAPI.Vulkan.__doc__ = """
Vulkan.
"""

