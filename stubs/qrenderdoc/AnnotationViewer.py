# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class AnnotationViewer(): # skipped bases: <class 'SwigPyObject'>
    """
    The annotation viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetAnnotationViewer`.
    """
    def RevealAnnotation(self, keyPath: str): # real signature unknown; restored from __doc__
        """
        RevealAnnotation(keyPath)
        
        Expand the annotation view to reveal a given path and select it.
        
        If the path does not exist, this will do nothing.
        
        :param str keyPath: The key path to the annotation.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`AnnotationViewer` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD501365C0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.AnnotationViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.AnnotationViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.AnnotationViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.AnnotationViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.AnnotationViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.AnnotationViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.AnnotationViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.AnnotationViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.AnnotationViewer' objects>, 'RevealAnnotation': <method 'RevealAnnotation' of 'qrenderdoc.AnnotationViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.AnnotationViewer' objects>, '__doc__': '\\nThe annotation viewer window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetAnnotationViewer`.\\n\\n'})"


