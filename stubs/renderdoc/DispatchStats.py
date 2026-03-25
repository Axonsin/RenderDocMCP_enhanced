# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DispatchStats(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the statistics for compute dispatches in a frame. """
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
    def calls(self) -> int:
        """
How many dispatch calls were made.

:type: int

"""
        pass

    @calls.setter
    def calls(self, value: int):
        pass

    @property
    def indirect(self) -> int:
        """
How many of :data:`calls` were indirect.

:type: int

"""
        pass

    @indirect.setter
    def indirect(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551FE660>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DispatchStats' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DispatchStats' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DispatchStats' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DispatchStats' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DispatchStats' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DispatchStats' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DispatchStats' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DispatchStats' objects>, 'calls': <attribute 'calls' of 'renderdoc.DispatchStats' objects>, 'indirect': <attribute 'indirect' of 'renderdoc.DispatchStats' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DispatchStats' objects>, '__doc__': 'Contains the statistics for compute dispatches in a frame.'})"


