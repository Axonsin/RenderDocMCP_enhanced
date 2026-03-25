# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderToolOutput(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the output from invoking a :class:`ShaderProcessingTool`, including both the
    actual output data desired as well as any stdout/stderr messages.
    """
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

    @property
    def log(self) -> str:
        """
The output log - containing the information about the tool run and any errors.

:type: str

"""
        pass

    @log.setter
    def log(self, value: str):
        pass

    @property
    def result(self) -> bytes:
        """
The actual output data from the tool

:type: bytes

"""
        pass

    @result.setter
    def result(self, value: bytes):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50143EC0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ShaderToolOutput' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ShaderToolOutput' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ShaderToolOutput' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ShaderToolOutput' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ShaderToolOutput' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ShaderToolOutput' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ShaderToolOutput' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ShaderToolOutput' objects>, 'log': <attribute 'log' of 'qrenderdoc.ShaderToolOutput' objects>, 'result': <attribute 'result' of 'qrenderdoc.ShaderToolOutput' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ShaderToolOutput' objects>, '__doc__': '\\nContains the output from invoking a :class:`ShaderProcessingTool`, including both the\\nactual output data desired as well as any stdout/stderr messages.\\n\\n'})"


