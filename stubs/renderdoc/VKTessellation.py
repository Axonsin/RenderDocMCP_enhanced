# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKTessellation(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the state of the fixed-function tessellator. """
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
    def domainOriginUpperLeft(self) -> bool:
        """
``True`` if the tessellation domain origin is upper-left, ``False`` if lower-left.

:type: bool

"""
        pass

    @domainOriginUpperLeft.setter
    def domainOriginUpperLeft(self, value: bool):
        pass

    @property
    def numControlPoints(self) -> int:
        """
The number of control points in each input patch.

:type: int

"""
        pass

    @numControlPoints.setter
    def numControlPoints(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CC3A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKTessellation' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKTessellation' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKTessellation' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKTessellation' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKTessellation' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKTessellation' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKTessellation' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKTessellation' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKTessellation' objects>, 'domainOriginUpperLeft': <attribute 'domainOriginUpperLeft' of 'renderdoc.VKTessellation' objects>, 'numControlPoints': <attribute 'numControlPoints' of 'renderdoc.VKTessellation' objects>, '__doc__': 'Describes the state of the fixed-function tessellator.'})"


