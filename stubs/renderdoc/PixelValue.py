# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PixelValue(): # skipped bases: <class 'SwigPyObject'>
    """ The contents of an RGBA pixel. """
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
    def floatValue(self) -> Tuple[float, float, float, float]:
        """
The RGBA value interpreted as ``float``.

:type: Tuple[float, float, float, float]

"""
        pass

    @floatValue.setter
    def floatValue(self, value: Tuple[float, float, float, float]):
        pass

    @property
    def intValue(self) -> Tuple[int, int, int, int]:
        """
The RGBA value interpreted as 32-bit signed integer.

:type: Tuple[int, int, int, int]

"""
        pass

    @intValue.setter
    def intValue(self, value: Tuple[int, int, int, int]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def uintValue(self) -> Tuple[int, int, int, int]:
        """
The RGBA value interpreted as 32-bit unsigned integer.

:type: Tuple[int, int, int, int]

"""
        pass

    @uintValue.setter
    def uintValue(self, value: Tuple[int, int, int, int]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F5410>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PixelValue' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PixelValue' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PixelValue' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PixelValue' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PixelValue' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PixelValue' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PixelValue' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PixelValue' objects>, 'uintValue': <attribute 'uintValue' of 'renderdoc.PixelValue' objects>, 'intValue': <attribute 'intValue' of 'renderdoc.PixelValue' objects>, 'floatValue': <attribute 'floatValue' of 'renderdoc.PixelValue' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PixelValue' objects>, '__doc__': 'The contents of an RGBA pixel.'})"


