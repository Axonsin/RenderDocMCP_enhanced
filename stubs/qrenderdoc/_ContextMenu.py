from enum import IntEnum

class ContextMenu(IntEnum):
    # Original docstring
    """
    Specifies the panel to add a menu item into.
    
    .. data:: Unknown
    
      Unknown/invalid context menu.
    
    .. data:: EventBrowser_Event
    
      Adds the item to the context menu for events in the :class:`EventBrowser`.
    
    .. data:: MeshPreview_Vertex
    
      Adds the item to the context menu for all vertices in the mesh previewing :class:`BufferViewer`.
    
    .. data:: MeshPreview_VSInVertex
    
      Adds the item to the context menu for vertex inputs in the mesh previewing :class:`BufferViewer`.
    
    .. data:: MeshPreview_VSOutVertex
    
      Adds the item to the context menu for VS output in the mesh previewing :class:`BufferViewer`.
    
    .. data:: MeshPreview_GSOutVertex
    
      Adds the item to the context menu for GS/Tess output in the mesh previewing :class:`BufferViewer`.
    
    .. data:: MeshPreview_TaskOutVertex
    
      Adds the item to the context menu for task shader output in the mesh previewing :class:`BufferViewer`.
    
    .. data:: MeshPreview_MeshOutVertex
    
      Adds the item to the context menu for mesh shader output in the mesh previewing :class:`BufferViewer`.
    
    .. data:: TextureViewer_Thumbnail
    
      Adds the item to the context menu for all thumbnails in the :class:`TextureViewer`.
    
    .. data:: TextureViewer_InputThumbnail
    
      Adds the item to the context menu for input thumbnails in the :class:`TextureViewer`.
    
    .. data:: TextureViewer_OutputThumbnail
    
      Adds the item to the context menu for output thumbnails in the :class:`TextureViewer`.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    Unknown/invalid context menu.
    """
    
    EventBrowser_Event = 1
    """
    Adds the item to the context menu for events in the :class:`EventBrowser`.
    """
    
    MeshPreview_Vertex = 2
    """
    Adds the item to the context menu for all vertices in the mesh previewing :class:`BufferViewer`.
    """
    
    MeshPreview_VSInVertex = 3
    """
    Adds the item to the context menu for vertex inputs in the mesh previewing :class:`BufferViewer`.
    """
    
    MeshPreview_VSOutVertex = 4
    """
    Adds the item to the context menu for VS output in the mesh previewing :class:`BufferViewer`.
    """
    
    MeshPreview_GSOutVertex = 5
    """
    Adds the item to the context menu for GS/Tess output in the mesh previewing :class:`BufferViewer`.
    """
    
    MeshPreview_TaskOutVertex = 6
    """
    Adds the item to the context menu for task shader output in the mesh previewing :class:`BufferViewer`.
    """
    
    MeshPreview_MeshOutVertex = 7
    """
    Adds the item to the context menu for mesh shader output in the mesh previewing :class:`BufferViewer`.
    """
    
    TextureViewer_Thumbnail = 8
    """
    Adds the item to the context menu for all thumbnails in the :class:`TextureViewer`.
    """
    
    TextureViewer_InputThumbnail = 9
    """
    Adds the item to the context menu for input thumbnails in the :class:`TextureViewer`.
    """
    
    TextureViewer_OutputThumbnail = 10
    """
    Adds the item to the context menu for output thumbnails in the :class:`TextureViewer`.
    """
    

# Assign __doc__ for enum values for easier introspection

ContextMenu.Unknown.__doc__ = """
Unknown/invalid context menu.
"""

ContextMenu.EventBrowser_Event.__doc__ = """
Adds the item to the context menu for events in the :class:`EventBrowser`.
"""

ContextMenu.MeshPreview_Vertex.__doc__ = """
Adds the item to the context menu for all vertices in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.MeshPreview_VSInVertex.__doc__ = """
Adds the item to the context menu for vertex inputs in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.MeshPreview_VSOutVertex.__doc__ = """
Adds the item to the context menu for VS output in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.MeshPreview_GSOutVertex.__doc__ = """
Adds the item to the context menu for GS/Tess output in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.MeshPreview_TaskOutVertex.__doc__ = """
Adds the item to the context menu for task shader output in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.MeshPreview_MeshOutVertex.__doc__ = """
Adds the item to the context menu for mesh shader output in the mesh previewing :class:`BufferViewer`.
"""

ContextMenu.TextureViewer_Thumbnail.__doc__ = """
Adds the item to the context menu for all thumbnails in the :class:`TextureViewer`.
"""

ContextMenu.TextureViewer_InputThumbnail.__doc__ = """
Adds the item to the context menu for input thumbnails in the :class:`TextureViewer`.
"""

ContextMenu.TextureViewer_OutputThumbnail.__doc__ = """
Adds the item to the context menu for output thumbnails in the :class:`TextureViewer`.
"""

