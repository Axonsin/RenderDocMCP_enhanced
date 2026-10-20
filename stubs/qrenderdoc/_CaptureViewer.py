
from typing import overload

class CaptureViewer():
    # Original docstring
    """
    An interface implemented by any object wanting to be notified of capture events.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CaptureViewer.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def OnCaptureLoaded(self):
        """
        Called whenever a capture is opened.
        """
        pass
    
    
    def OnCaptureClosed(self):
        """
        Called whenever a capture is closed.
        """
        pass
    
    
    def OnSelectedEventChanged(self, eventId: int):
        """
        Called whenever the current selected event changes. This is distinct from the actual
        effective current event, since for example selecting a marker region will change the current event
        to be the last event inside that region, to be consistent with selecting an item reflecting the
        current state after that item.
        
        The selected event shows the :data:`eventId <renderdoc.APIEvent.eventId>` that was actually selected,
        which will usually but not always be the same as the current effective
        :data:`eventId <renderdoc.APIEvent.eventId>`.
        
        The distinction for this callback is not normally desired, instead use :meth:`OnEventChanged` to
        be notified whenever the current event changes. The API inspector uses this to display API events up
        to a marker region.
        
        :param int eventId: The new :data:`eventId <renderdoc.APIEvent.eventId>`.
        """
        pass
    
    
    def OnEventChanged(self, eventId: int):
        """
        Called whenever the effective current event changes.
        
        :param int eventId: The new :data:`eventId <renderdoc.APIEvent.eventId>`.
        """
        pass
    
