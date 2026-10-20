from renderdoc import MeshDataStage

# Dummy types
from . import QWidget

class BufferViewer():
    # Original docstring
    """
    The buffer viewer window, either a raw buffer or the geometry pipeline.
    
    This mesh viewer is retrieved by calling :meth:`CaptureContext.GetMeshPreview`.
    
    A raw buffer viewer can be opened by calling :meth:`CaptureContext.ViewBuffer`,
    :meth:`CaptureContext.ViewTextureAsBuffer`, or :meth:`CaptureContext.ViewConstantBuffer`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`BufferViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def ScrollToRow(self, row: int, stage: MeshDataStage = MeshDataStage.VSIn):
        """
        Scroll to the given row in the given stage's data.
        
        :param int row: the row to scroll to.
        :param renderdoc.MeshDataStage stage=renderdoc.MeshDataStage.VSIn: **Optional parameter**. The stage of the
          geometry pipeline to scroll within. Ignored for non-mesh buffer viewers.
        """
        pass
    
    
    def ScrollToColumn(self, column: int, stage: MeshDataStage = MeshDataStage.VSIn):
        """
        Scroll to the given column in the given stage's data.
        
        :param int column: the column to scroll to.
        :param renderdoc.MeshDataStage stage=renderdoc.MeshDataStage.VSIn: **Optional parameter**. The stage of the
          geometry pipeline to scroll within. Ignored for non-mesh buffer viewers.
        """
        pass
    
    
    def ShowMeshData(self, stage: MeshDataStage):
        """
        Ensure the given stage's data is visible and raised, if it wasn't before.
        
        :param renderdoc.MeshDataStage stage: The stage of the geometry pipeline to show data for.
        """
        pass
    
    
    def SetCurrentInstance(self, instance: int):
        """
        For a mesh view, set the current instance. This is ignored when called on a raw buffer
        view.
        
        :param int instance: The instance to select, will be clamped to the range [0, numInstances-1]
        """
        pass
    
    
    def SetCurrentView(self, view: int):
        """
        For a mesh view, set the current multiview view. This is ignored when called on a raw
        buffer view.
        
        :param int view: The view to select, will be clamped to the range [0, numViews-1]
        """
        pass
    
    
    def SetPreviewStage(self, stage: MeshDataStage):
        """
        For a mesh view, set the current preview stage. This is ignored when called on a raw
        buffer view.
        
        :param renderdoc.MeshDataStage stage: The stage to show
        """
        pass
    
