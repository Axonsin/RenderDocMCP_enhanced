from enum import IntEnum

class PanelMenu(IntEnum):
    # Original docstring
    """
    Specifies the panel to add a menu item into.
    
    .. data:: Unknown
    
      Unknown/invalid panel.
    
    .. data:: EventBrowser
    
      The :class:`EventBrowser`.
    
    .. data:: PipelineStateViewer
    
      The :class:`PipelineStateViewer`.
    
    .. data:: MeshPreview
    
      The mesh previewing :class:`BufferViewer`.
    
    .. data:: TextureViewer
    
      The :class:`TextureViewer`.
    
    .. data:: BufferViewer
    
      Any non-mesh previewing :class:`BufferViewer`.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    Unknown/invalid panel.
    """
    
    EventBrowser = 1
    """
    The :class:`EventBrowser`.
    """
    
    PipelineStateViewer = 2
    """
    The :class:`PipelineStateViewer`.
    """
    
    MeshPreview = 3
    """
    The mesh previewing :class:`BufferViewer`.
    """
    
    TextureViewer = 4
    """
    The :class:`TextureViewer`.
    """
    
    BufferViewer = 5
    """
    Any non-mesh previewing :class:`BufferViewer`.
    """
    

# Assign __doc__ for enum values for easier introspection

PanelMenu.Unknown.__doc__ = """
Unknown/invalid panel.
"""

PanelMenu.EventBrowser.__doc__ = """
The :class:`EventBrowser`.
"""

PanelMenu.PipelineStateViewer.__doc__ = """
The :class:`PipelineStateViewer`.
"""

PanelMenu.MeshPreview.__doc__ = """
The mesh previewing :class:`BufferViewer`.
"""

PanelMenu.TextureViewer.__doc__ = """
The :class:`TextureViewer`.
"""

PanelMenu.BufferViewer.__doc__ = """
Any non-mesh previewing :class:`BufferViewer`.
"""

