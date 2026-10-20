from renderdoc import PixelModification, ResourceId
from typing import List

# Dummy types
from . import QWidget

class TimelineBar():
    # Original docstring
    """
    The timeline bar.
    
    This window is retrieved by calling :meth:`CaptureContext.GetTimelineBar`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`TimelineBar` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def HighlightResourceUsage(self, id: ResourceId):
        """
        Highlights the frame usage of the specified resource.
        
        :param renderdoc.ResourceId id: The ID of the resource to highlight.
        """
        pass
    
    
    def HighlightHistory(self, id: ResourceId, history: List[PixelModification]):
        """
        Highlights the modifications in a frame of a given resource.
        
        :param renderdoc.ResourceId id: The ID of the resource that is being modified.
        :param List[renderdoc.PixelModification] history: A list of pixel events to display.
        """
        pass
    
