# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKVertexBinding(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a vertex binding. """
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
    def instanceDivisor(self) -> int:
        """
The instance rate divisor.

If this is ``0`` then every vertex gets the same value.

If it's ``1`` then one element is read for each instance, and for ``N`` greater than ``1`` then
``N`` instances read the same element before advancing.

:type: int

"""
        pass

    @instanceDivisor.setter
    def instanceDivisor(self, value: int):
        pass

    @property
    def perInstance(self) -> bool:
        """
``True`` if the vertex data is instance-rate.

:type: bool

"""
        pass

    @perInstance.setter
    def perInstance(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexBufferBinding(self) -> int:
        """
The vertex binding where data will be sourced from.

:type: int

"""
        pass

    @vertexBufferBinding.setter
    def vertexBufferBinding(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E3E90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKVertexBinding' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKVertexBinding' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKVertexBinding' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKVertexBinding' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKVertexBinding' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKVertexBinding' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKVertexBinding' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKVertexBinding' objects>, 'vertexBufferBinding': <attribute 'vertexBufferBinding' of 'renderdoc.VKVertexBinding' objects>, 'instanceDivisor': <attribute 'instanceDivisor' of 'renderdoc.VKVertexBinding' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKVertexBinding' objects>, 'perInstance': <attribute 'perInstance' of 'renderdoc.VKVertexBinding' objects>, '__doc__': 'Describes a vertex binding.'})"


