# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Scissor import Scissor
from .Viewport import Viewport

class VKViewportScissor(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a combined viewport and scissor region. """
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
    def scissor(self) -> Scissor:
        """
The scissor.

:type: Scissor

"""
        pass

    @scissor.setter
    def scissor(self, value: Scissor):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vp(self) -> Viewport:
        """
The viewport.

:type: Viewport

"""
        pass

    @vp.setter
    def vp(self, value: Viewport):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55207BC0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKViewportScissor' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKViewportScissor' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKViewportScissor' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKViewportScissor' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKViewportScissor' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKViewportScissor' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKViewportScissor' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKViewportScissor' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKViewportScissor' objects>, 'vp': <attribute 'vp' of 'renderdoc.VKViewportScissor' objects>, 'scissor': <attribute 'scissor' of 'renderdoc.VKViewportScissor' objects>, '__doc__': 'Describes a combined viewport and scissor region.'})"


