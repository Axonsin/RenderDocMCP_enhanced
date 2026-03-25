# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureComponentMapping(): # skipped bases: <class 'SwigPyObject'>
    """ How to map components to normalised ``[0, 255]`` for saving to 8-bit file formats. """
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
    def blackPoint(self) -> float:
        """
The value that should be mapped to ``0``

:type: float

"""
        pass

    @blackPoint.setter
    def blackPoint(self, value: float):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def whitePoint(self) -> float:
        """
The value that should be mapped to ``255``

:type: float

"""
        pass

    @whitePoint.setter
    def whitePoint(self, value: float):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55205BE0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureComponentMapping' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureComponentMapping' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureComponentMapping' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureComponentMapping' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureComponentMapping' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureComponentMapping' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureComponentMapping' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureComponentMapping' objects>, 'whitePoint': <attribute 'whitePoint' of 'renderdoc.TextureComponentMapping' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureComponentMapping' objects>, 'blackPoint': <attribute 'blackPoint' of 'renderdoc.TextureComponentMapping' objects>, '__doc__': 'How to map components to normalised ``[0, 255]`` for saving to 8-bit file formats.'})"


