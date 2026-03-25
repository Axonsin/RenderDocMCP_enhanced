# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class NewChildData(): # skipped bases: <class 'SwigPyObject'>
    """ Information about a new child process spawned by the target. """
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
    def ident(self) -> int:
        """
The ident where the new child's target control is active.

:type: int

"""
        pass

    @ident.setter
    def ident(self, value: int):
        pass

    @property
    def processId(self) -> int:
        """
The PID (Process ID) of the new child.

:type: int

"""
        pass

    @processId.setter
    def processId(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F7AA0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.NewChildData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.NewChildData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.NewChildData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.NewChildData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.NewChildData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.NewChildData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.NewChildData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.NewChildData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.NewChildData' objects>, 'ident': <attribute 'ident' of 'renderdoc.NewChildData' objects>, 'processId': <attribute 'processId' of 'renderdoc.NewChildData' objects>, '__doc__': 'Information about a new child process spawned by the target.'})"


