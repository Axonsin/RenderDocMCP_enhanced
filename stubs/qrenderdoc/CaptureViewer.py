# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CaptureViewer(): # skipped bases: <class 'SwigPyObject'>
    """ An interface implemented by any object wanting to be notified of capture events. """
    def OnCaptureClosed(self): # real signature unknown; restored from __doc__
        """
        OnCaptureClosed()
        
        Called whenever a capture is closed.
        """
        pass

    def OnCaptureLoaded(self): # real signature unknown; restored from __doc__
        """
        OnCaptureLoaded()
        
        Called whenever a capture is opened.
        """
        pass

    def OnEventChanged(self, eventId: int): # real signature unknown; restored from __doc__
        """
        OnEventChanged(eventId)
        
        Called whenever the effective current event changes.
        
        :param int eventId: The new :data:`eventId <renderdoc.APIEvent.eventId>`.
        """
        pass

    def OnSelectedEventChanged(self, eventId: int): # real signature unknown; restored from __doc__
        """
        OnSelectedEventChanged(eventId)
        
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50140C30>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.CaptureViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.CaptureViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.CaptureViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.CaptureViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.CaptureViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.CaptureViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.CaptureViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.CaptureViewer' objects>, 'OnCaptureLoaded': <method 'OnCaptureLoaded' of 'qrenderdoc.CaptureViewer' objects>, 'OnCaptureClosed': <method 'OnCaptureClosed' of 'qrenderdoc.CaptureViewer' objects>, 'OnSelectedEventChanged': <method 'OnSelectedEventChanged' of 'qrenderdoc.CaptureViewer' objects>, 'OnEventChanged': <method 'OnEventChanged' of 'qrenderdoc.CaptureViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.CaptureViewer' objects>, '__doc__': 'An interface implemented by any object wanting to be notified of capture events.'})"


