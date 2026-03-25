# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PanelMenu(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    BufferViewer = 5
    """ Any non-mesh previewing :class:`BufferViewer`. """

    EventBrowser = 1
    """ The :class:`EventBrowser`. """

    MeshPreview = 3
    """ The mesh previewing :class:`BufferViewer`. """

    PipelineStateViewer = 2
    """ The :class:`PipelineStateViewer`. """

    TextureViewer = 4
    """ The :class:`TextureViewer`. """

    Unknown = 0
    """ Unknown/invalid panel. """



