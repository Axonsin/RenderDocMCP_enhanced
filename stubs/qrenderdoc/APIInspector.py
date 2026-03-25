# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.SDObject import SDObject

class APIInspector(): # skipped bases: <class 'SwigPyObject'>
    """
    The API inspector window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetAPIInspector`.
    """
    def Refresh(self): # real signature unknown; restored from __doc__
        """
        Refresh()
        
        Refresh the current API view - useful if callstacks are now available.
        """
        pass

    def RevealParameter(self, param: SDObject): # real signature unknown; restored from __doc__
        """
        RevealParameter(param)
        
        Expand the API view to reveal a given parameter and select it.
        
        :param renderdoc.SDObject param: The parameter to reveal and select.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`APIInspector` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50135D00>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.APIInspector' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.APIInspector' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.APIInspector' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.APIInspector' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.APIInspector' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.APIInspector' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.APIInspector' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.APIInspector' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.APIInspector' objects>, 'Refresh': <method 'Refresh' of 'qrenderdoc.APIInspector' objects>, 'RevealParameter': <method 'RevealParameter' of 'qrenderdoc.APIInspector' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.APIInspector' objects>, '__doc__': '\\nThe API inspector window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetAPIInspector`.\\n\\n'})"


