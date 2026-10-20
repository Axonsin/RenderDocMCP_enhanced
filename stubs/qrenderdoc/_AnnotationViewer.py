
# Dummy types
from . import QWidget

class AnnotationViewer():
    # Original docstring
    """
    The annotation viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetAnnotationViewer`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`AnnotationViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def RevealAnnotation(self, keyPath: str):
        """
        Expand the annotation view to reveal a given path and select it.
        
        If the path does not exist, this will do nothing.
        
        :param str keyPath: The key path to the annotation.
        """
        pass
    
