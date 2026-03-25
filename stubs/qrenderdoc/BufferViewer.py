# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.MeshDataStage import MeshDataStage

class BufferViewer(): # skipped bases: <class 'SwigPyObject'>
    """
    The buffer viewer window, either a raw buffer or the geometry pipeline.
    
    This mesh viewer is retrieved by calling :meth:`CaptureContext.GetMeshPreview`.
    
    A raw buffer viewer can be opened by calling :meth:`CaptureContext.ViewBuffer`,
    :meth:`CaptureContext.ViewTextureAsBuffer`, or :meth:`CaptureContext.ViewConstantBuffer`.
    """
    def ScrollToColumn(self, column: int, stage: MeshDataStage): # real signature unknown; restored from __doc__
        """
        ScrollToColumn(column, stage)
        ScrollToColumn(column)
        
        Scroll to the given column in the given stage's data.
        
        :param int column: the column to scroll to.
        :param renderdoc.MeshDataStage stage: The stage of the geometry pipeline to scroll within.
        """
        pass

    def ScrollToRow(self, row: int, stage: MeshDataStage): # real signature unknown; restored from __doc__
        """
        ScrollToRow(row, stage)
        ScrollToRow(row)
        
        Scroll to the given row in the given stage's data.
        
        :param int row: the row to scroll to.
        :param renderdoc.MeshDataStage stage: The stage of the geometry pipeline to scroll within.
        """
        pass

    def SetCurrentInstance(self, instance: int): # real signature unknown; restored from __doc__
        """
        SetCurrentInstance(instance)
        
        For a mesh view, set the current instance. This is ignored when called on a raw buffer
        view.
        
        :param int instance: The instance to select, will be clamped to the range [0, numInstances-1]
        """
        pass

    def SetCurrentView(self, view: int): # real signature unknown; restored from __doc__
        """
        SetCurrentView(view)
        
        For a mesh view, set the current multiview view. This is ignored when called on a raw
        buffer view.
        
        :param int view: The view to select, will be clamped to the range [0, numViews-1]
        """
        pass

    def SetPreviewStage(self, stage: MeshDataStage): # real signature unknown; restored from __doc__
        """
        SetPreviewStage(stage)
        
        For a mesh view, set the current preview stage. This is ignored when called on a raw
        buffer view.
        
        :param renderdoc.MeshDataStage stage: The stage to show
        """
        pass

    def ShowMeshData(self, stage: MeshDataStage): # real signature unknown; restored from __doc__
        """
        ShowMeshData(stage)
        
        Ensure the given stage's data is visible and raised, if it wasn't before.
        
        :param renderdoc.MeshDataStage stage: The stage of the geometry pipeline to show data for.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`BufferViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50139B70>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.BufferViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.BufferViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.BufferViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.BufferViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.BufferViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.BufferViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.BufferViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.BufferViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.BufferViewer' objects>, 'ScrollToRow': <method 'ScrollToRow' of 'qrenderdoc.BufferViewer' objects>, 'ScrollToColumn': <method 'ScrollToColumn' of 'qrenderdoc.BufferViewer' objects>, 'ShowMeshData': <method 'ShowMeshData' of 'qrenderdoc.BufferViewer' objects>, 'SetCurrentInstance': <method 'SetCurrentInstance' of 'qrenderdoc.BufferViewer' objects>, 'SetCurrentView': <method 'SetCurrentView' of 'qrenderdoc.BufferViewer' objects>, 'SetPreviewStage': <method 'SetPreviewStage' of 'qrenderdoc.BufferViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.BufferViewer' objects>, '__doc__': '\\nThe buffer viewer window, either a raw buffer or the geometry pipeline.\\n\\nThis mesh viewer is retrieved by calling :meth:`CaptureContext.GetMeshPreview`.\\n\\nA raw buffer viewer can be opened by calling :meth:`CaptureContext.ViewBuffer`,\\n:meth:`CaptureContext.ViewTextureAsBuffer`, or :meth:`CaptureContext.ViewConstantBuffer`.\\n\\n\\n'})"


