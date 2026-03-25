# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.ShaderMessage import ShaderMessage

class ShaderMessageViewer(): # skipped bases: <class 'SwigPyObject'>
    """
    A shader message list window.
    
    This window is retrieved by calling :meth:`CaptureContext.ViewShaderMessages`.
    """
    def GetEvent(self) -> int: # real signature unknown; restored from __doc__
        """
        GetEvent()
        
        Return the EID that this viewer is displaying messages from.
        
        :return: The EID.
        :rtype: int
        """
        pass

    def GetShaderMessages(self) -> List[ShaderMessage]: # real signature unknown; restored from __doc__
        """
        GetShaderMessages()
        
        Return the shader messages displayed in this viewer.
        
        :return: The shader messages.
        :rtype: List[renderdoc.ShaderMessage]
        """
        pass

    def IsOutOfDate(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsOutOfDate()
        
        Returns whether or not this viewer is out of date - if the shaders have been edited
        since the messages were fetched.
        
        :return: ``True`` if the viewer is out of date.
        :rtype: bool
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`ShaderMessageViewer` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5013FE40>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ShaderMessageViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.ShaderMessageViewer' objects>, 'GetEvent': <method 'GetEvent' of 'qrenderdoc.ShaderMessageViewer' objects>, 'GetShaderMessages': <method 'GetShaderMessages' of 'qrenderdoc.ShaderMessageViewer' objects>, 'IsOutOfDate': <method 'IsOutOfDate' of 'qrenderdoc.ShaderMessageViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ShaderMessageViewer' objects>, '__doc__': '\\nA shader message list window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.ViewShaderMessages`.\\n\\n'})"


