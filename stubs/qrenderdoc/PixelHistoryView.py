# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.PixelModification import PixelModification

class PixelHistoryView(): # skipped bases: <class 'SwigPyObject'>
    """
    A pixel history window.
    
    This window is retrieved by calling :meth:`CaptureContext.ViewPixelHistory`.
    """
    def SetFailedDebug(self): # real signature unknown; restored from __doc__
        """
        SetFailedDebug()
        
        Indicates that the pixel history was launched as a result of failing to debug a shader,
        so a message will be displayed to explain.
        """
        pass

    def SetHistory(self, history: List[PixelModification]): # real signature unknown; restored from __doc__
        """
        SetHistory(history)
        
        Set the history displayed in this window.
        
        :param List[renderdoc.PixelModification] history: A list of pixel events to display.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`PixelHistoryView` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50140760>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.PixelHistoryView' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.PixelHistoryView' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.PixelHistoryView' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.PixelHistoryView' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.PixelHistoryView' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.PixelHistoryView' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.PixelHistoryView' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.PixelHistoryView' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.PixelHistoryView' objects>, 'SetHistory': <method 'SetHistory' of 'qrenderdoc.PixelHistoryView' objects>, 'SetFailedDebug': <method 'SetFailedDebug' of 'qrenderdoc.PixelHistoryView' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.PixelHistoryView' objects>, '__doc__': '\\nA pixel history window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.ViewPixelHistory`.\\n\\n'})"


