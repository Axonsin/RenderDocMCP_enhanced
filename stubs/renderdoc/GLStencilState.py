# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .StencilFace import StencilFace

class GLStencilState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the stencil state. """
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
    def backFace(self) -> StencilFace:
        """
The stencil state for back-facing polygons.

:type: StencilFace

"""
        pass

    @backFace.setter
    def backFace(self, value: StencilFace):
        pass

    @property
    def frontFace(self) -> StencilFace:
        """
The stencil state for front-facing polygons.

:type: StencilFace

"""
        pass

    @frontFace.setter
    def frontFace(self, value: StencilFace):
        pass

    @property
    def stencilEnable(self) -> bool:
        """
``True`` if stencil operations should be performed.

:type: bool

"""
        pass

    @stencilEnable.setter
    def stencilEnable(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B8F70>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLStencilState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLStencilState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLStencilState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLStencilState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLStencilState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLStencilState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLStencilState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLStencilState' objects>, 'frontFace': <attribute 'frontFace' of 'renderdoc.GLStencilState' objects>, 'backFace': <attribute 'backFace' of 'renderdoc.GLStencilState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLStencilState' objects>, 'stencilEnable': <attribute 'stencilEnable' of 'renderdoc.GLStencilState' objects>, '__doc__': 'Describes the stencil state.'})"


