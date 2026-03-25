# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKVertexAttribute import VKVertexAttribute
from .VKVertexBinding import VKVertexBinding
from .VKVertexBuffer import VKVertexBuffer

class VKVertexInput(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the fixed-function vertex input fetch setup. """
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
    def attributes(self) -> List[VKVertexAttribute]:
        """
The vertex attributes.

:type: List[VKVertexAttribute]

"""
        pass

    @attributes.setter
    def attributes(self, value: List[VKVertexAttribute]):
        pass

    @property
    def bindings(self) -> List[VKVertexBinding]:
        """
The vertex bindings.

:type: List[VKVertexBinding]

"""
        pass

    @bindings.setter
    def bindings(self, value: List[VKVertexBinding]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexBuffers(self) -> List[VKVertexBuffer]:
        """
The vertex buffers.

:type: List[VKVertexBuffer]

"""
        pass

    @vertexBuffers.setter
    def vertexBuffers(self, value: List[VKVertexBuffer]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522A910>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKVertexInput' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKVertexInput' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKVertexInput' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKVertexInput' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKVertexInput' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKVertexInput' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKVertexInput' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKVertexInput' objects>, 'attributes': <attribute 'attributes' of 'renderdoc.VKVertexInput' objects>, 'vertexBuffers': <attribute 'vertexBuffers' of 'renderdoc.VKVertexInput' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKVertexInput' objects>, 'bindings': <attribute 'bindings' of 'renderdoc.VKVertexInput' objects>, '__doc__': 'Describes the fixed-function vertex input fetch setup.'})"


