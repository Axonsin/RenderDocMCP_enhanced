# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.PixelModification import PixelModification

from renderdoc.ResourceId import ResourceId

class TimelineBar(): # skipped bases: <class 'SwigPyObject'>
    """
    The timeline bar.
    
    This window is retrieved by calling :meth:`CaptureContext.GetTimelineBar`.
    """
    def HighlightHistory(self, id: ResourceId, history: List[PixelModification]): # real signature unknown; restored from __doc__
        """
        HighlightHistory(id, history)
        
        Highlights the modifications in a frame of a given resource.
        
        :param renderdoc.ResourceId id: The ID of the resource that is being modified.
        :param List[renderdoc.PixelModification] history: A list of pixel events to display.
        """
        pass

    def HighlightResourceUsage(self, id: ResourceId): # real signature unknown; restored from __doc__
        """
        HighlightResourceUsage(id)
        
        Highlights the frame usage of the specified resource.
        
        :param renderdoc.ResourceId id: The ID of the resource to highlight.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`TimelineBar` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5013EA80>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.TimelineBar' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.TimelineBar' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.TimelineBar' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.TimelineBar' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.TimelineBar' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.TimelineBar' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.TimelineBar' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.TimelineBar' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.TimelineBar' objects>, 'HighlightResourceUsage': <method 'HighlightResourceUsage' of 'qrenderdoc.TimelineBar' objects>, 'HighlightHistory': <method 'HighlightHistory' of 'qrenderdoc.TimelineBar' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.TimelineBar' objects>, '__doc__': '\\nThe timeline bar.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetTimelineBar`.\\n\\n'})"


