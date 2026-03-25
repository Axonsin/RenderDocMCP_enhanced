# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .BlendMultiplier import BlendMultiplier
from .BlendOperation import BlendOperation

class BlendEquation(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the details of a blend operation. """
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
    def destination(self) -> BlendMultiplier:
        """
The :class:`BlendMultiplier` for the destination blend value.

:type: BlendMultiplier

"""
        pass

    @destination.setter
    def destination(self, value: BlendMultiplier):
        pass

    @property
    def operation(self) -> BlendOperation:
        """
The :class:`BlendOperation` to use in the blend calculation.

:type: BlendOperation

"""
        pass

    @operation.setter
    def operation(self, value: BlendOperation):
        pass

    @property
    def source(self) -> BlendMultiplier:
        """
The :class:`BlendMultiplier` for the source blend value.

:type: BlendMultiplier

"""
        pass

    @source.setter
    def source(self, value: BlendMultiplier):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55213440>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.BlendEquation' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.BlendEquation' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.BlendEquation' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.BlendEquation' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.BlendEquation' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.BlendEquation' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.BlendEquation' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.BlendEquation' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.BlendEquation' objects>, 'destination': <attribute 'destination' of 'renderdoc.BlendEquation' objects>, 'source': <attribute 'source' of 'renderdoc.BlendEquation' objects>, 'operation': <attribute 'operation' of 'renderdoc.BlendEquation' objects>, '__doc__': 'Describes the details of a blend operation.'})"


