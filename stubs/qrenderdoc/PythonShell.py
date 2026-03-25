# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PythonShell(): # skipped bases: <class 'SwigPyObject'>
    """
    The interactive python shell.
    
    This window is retrieved by calling :meth:`CaptureContext.GetPythonShell`.
    """
    def GetScriptText(self) -> str: # real signature unknown; restored from __doc__
        """
        GetScriptText()
        
        Returns the current script text.
        
        :return: The current script text.
        :rtype: str
        """
        pass

    def LoadScriptFromFilename(self, filename: str) -> bool: # real signature unknown; restored from __doc__
        """
        LoadScriptFromFilename(filename)
        
        Sets the current script in the python shell to the contents of the given file.
        
        :param str filename: The filename of the script to load.
        :return: Whether or not the script was successfully loaded.
        :rtype: bool
        """
        pass

    def RunScript(self): # real signature unknown; restored from __doc__
        """
        RunScript()
        
        Runs the current script in the python shell.
        """
        pass

    def SetScriptText(self, script: str): # real signature unknown; restored from __doc__
        """
        SetScriptText(script)
        
        Sets the current script in the python shell to the given string.
        
        :param str script: The text of the script to set.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`PythonShell` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5013F400>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.PythonShell' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.PythonShell' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.PythonShell' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.PythonShell' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.PythonShell' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.PythonShell' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.PythonShell' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.PythonShell' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.PythonShell' objects>, 'SetScriptText': <method 'SetScriptText' of 'qrenderdoc.PythonShell' objects>, 'LoadScriptFromFilename': <method 'LoadScriptFromFilename' of 'qrenderdoc.PythonShell' objects>, 'GetScriptText': <method 'GetScriptText' of 'qrenderdoc.PythonShell' objects>, 'RunScript': <method 'RunScript' of 'qrenderdoc.PythonShell' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.PythonShell' objects>, '__doc__': '\\nThe interactive python shell.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetPythonShell`.\\n\\n'})"


