# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ContextMenu(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    EventBrowser_Event = 1
    """ Adds the item to the context menu for events in the :class:`EventBrowser`. """

    MeshPreview_GSOutVertex = 5
    """ Adds the item to the context menu for GS/Tess output in the mesh previewing :class:`BufferViewer`. """

    MeshPreview_MeshOutVertex = 7
    """ Adds the item to the context menu for mesh shader output in the mesh previewing :class:`BufferViewer`. """

    MeshPreview_TaskOutVertex = 6
    """ Adds the item to the context menu for task shader output in the mesh previewing :class:`BufferViewer`. """

    MeshPreview_Vertex = 2
    """ Adds the item to the context menu for all vertices in the mesh previewing :class:`BufferViewer`. """

    MeshPreview_VSInVertex = 3
    """ Adds the item to the context menu for vertex inputs in the mesh previewing :class:`BufferViewer`. """

    MeshPreview_VSOutVertex = 4
    """ Adds the item to the context menu for VS output in the mesh previewing :class:`BufferViewer`. """

    TextureViewer_InputThumbnail = 9
    """ Adds the item to the context menu for input thumbnails in the :class:`TextureViewer`. """

    TextureViewer_OutputThumbnail = 10
    """ Adds the item to the context menu for output thumbnails in the :class:`TextureViewer`. """

    TextureViewer_Thumbnail = 8
    """ Adds the item to the context menu for all thumbnails in the :class:`TextureViewer`. """

    Unknown = 0
    """ Unknown/invalid context menu. """



