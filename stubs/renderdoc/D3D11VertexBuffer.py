# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class D3D11VertexBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a single D3D11 vertex buffer binding. """
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
    def byteOffset(self) -> int:
        """
The byte offset from the start of the buffer to the beginning of the vertex data.

:type: int

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: int):
        pass

    @property
    def byteStride(self) -> int:
        """
The byte stride between the start of one set of vertex data and the next.

:type: int

"""
        pass

    @byteStride.setter
    def byteStride(self, value: int):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the buffer bound to this slot.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D6C20>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11VertexBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11VertexBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11VertexBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11VertexBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11VertexBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11VertexBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11VertexBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11VertexBuffer' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D11VertexBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11VertexBuffer' objects>, 'byteStride': <attribute 'byteStride' of 'renderdoc.D3D11VertexBuffer' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.D3D11VertexBuffer' objects>, '__doc__': 'Describes a single D3D11 vertex buffer binding.'})"


