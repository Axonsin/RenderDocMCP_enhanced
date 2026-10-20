
# Dummy types
from . import QWidget

class DiagnosticLogView():
    # Original docstring
    """
    The diagnostic log viewing window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetDiagnosticLogView`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`DiagnosticLogView` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
