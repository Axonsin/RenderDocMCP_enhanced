# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DebugPixelInputs(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the properties used to select which fragment to debug, used as an input to DebugPixel. """
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
    def primitive(self) -> int:
        """
The primitive index.

:type: int

"""
        pass

    @primitive.setter
    def primitive(self, value: int):
        pass

    @property
    def sample(self) -> int:
        """
The multi-sampled sample.

:type: int

"""
        pass

    @sample.setter
    def sample(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def view(self) -> int:
        """
The layered or multiview rendering view index.

:type: int

"""
        pass

    @view.setter
    def view(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552030D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DebugPixelInputs' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DebugPixelInputs' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DebugPixelInputs' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DebugPixelInputs' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DebugPixelInputs' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DebugPixelInputs' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DebugPixelInputs' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DebugPixelInputs' objects>, 'view': <attribute 'view' of 'renderdoc.DebugPixelInputs' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DebugPixelInputs' objects>, 'primitive': <attribute 'primitive' of 'renderdoc.DebugPixelInputs' objects>, 'sample': <attribute 'sample' of 'renderdoc.DebugPixelInputs' objects>, '__doc__': 'Contains the properties used to select which fragment to debug, used as an input to DebugPixel.'})"


