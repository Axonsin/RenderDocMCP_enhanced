from renderdoc import PixelModification
from typing import List

# Dummy types
from . import QWidget

class PixelHistoryView():
    # Original docstring
    """
    A pixel history window.
    
    This window is retrieved by calling :meth:`CaptureContext.ViewPixelHistory`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`PixelHistoryView` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def SetHistory(self, history: List[PixelModification]):
        """
        Set the history displayed in this window.
        
        :param List[renderdoc.PixelModification] history: A list of pixel events to display.
        """
        pass
    
    
    def SetFailedDebug(self):
        """
        Indicates that the pixel history was launched as a result of failing to debug a shader,
        so a message will be displayed to explain.
        """
        pass
    
