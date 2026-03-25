# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .StencilOperation import StencilOperation
from .CompareFunction import CompareFunction

class StencilFace(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the details of a stencil operation. """
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
    def compareMask(self) -> int:
        """
The mask for testing stencil values.

:type: int

"""
        pass

    @compareMask.setter
    def compareMask(self, value: int):
        pass

    @property
    def depthFailOperation(self) -> StencilOperation:
        """
the :class:`StencilOperation` to apply if the depth-test fails.

:type: StencilOperation

"""
        pass

    @depthFailOperation.setter
    def depthFailOperation(self, value: StencilOperation):
        pass

    @property
    def failOperation(self) -> StencilOperation:
        """
The :class:`StencilOperation` to apply if the stencil-test fails.

:type: StencilOperation

"""
        pass

    @failOperation.setter
    def failOperation(self, value: StencilOperation):
        pass

    @property
    def function(self) -> CompareFunction:
        """
the :class:`CompareFunction` to use for testing stencil values.

:type: CompareFunction

"""
        pass

    @function.setter
    def function(self, value: CompareFunction):
        pass

    @property
    def passOperation(self) -> StencilOperation:
        """
the :class:`StencilOperation` to apply if the stencil-test passes.

:type: StencilOperation

"""
        pass

    @passOperation.setter
    def passOperation(self, value: StencilOperation):
        pass

    @property
    def reference(self) -> int:
        """
The current stencil reference value.

:type: int

"""
        pass

    @reference.setter
    def reference(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def writeMask(self) -> int:
        """
The mask for writing stencil values.

:type: int

"""
        pass

    @writeMask.setter
    def writeMask(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551EA9D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.StencilFace' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.StencilFace' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.StencilFace' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.StencilFace' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.StencilFace' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.StencilFace' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.StencilFace' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.StencilFace' objects>, 'reference': <attribute 'reference' of 'renderdoc.StencilFace' objects>, 'function': <attribute 'function' of 'renderdoc.StencilFace' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.StencilFace' objects>, 'compareMask': <attribute 'compareMask' of 'renderdoc.StencilFace' objects>, 'writeMask': <attribute 'writeMask' of 'renderdoc.StencilFace' objects>, 'failOperation': <attribute 'failOperation' of 'renderdoc.StencilFace' objects>, 'depthFailOperation': <attribute 'depthFailOperation' of 'renderdoc.StencilFace' objects>, 'passOperation': <attribute 'passOperation' of 'renderdoc.StencilFace' objects>, '__doc__': 'Describes the details of a stencil operation.'})"


