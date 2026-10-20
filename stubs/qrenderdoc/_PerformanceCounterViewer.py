
# Dummy types
from . import QWidget

class PerformanceCounterViewer():
    # Original docstring
    """
    The performance counter view window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetPerformanceCounterViewer`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`PerformanceCounterViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def UpdateDurationColumn(self):
        """
        Updates duration columns if the selected time unit changes.
        """
        pass
    
