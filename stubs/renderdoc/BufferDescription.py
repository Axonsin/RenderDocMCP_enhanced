# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .BufferCategory import BufferCategory
from .ResourceId import ResourceId

class BufferDescription(): # skipped bases: <class 'SwigPyObject'>
    """ A description of a buffer resource. """
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
    def creationFlags(self) -> BufferCategory:
        """
The way this buffer will be used in the pipeline.

:type: BufferCategory

"""
        pass

    @creationFlags.setter
    def creationFlags(self, value: BufferCategory):
        pass

    @property
    def gpuAddress(self) -> int:
        """
The known base GPU Address of this buffer. 0 if not applicable or available.

:type: int

"""
        pass

    @gpuAddress.setter
    def gpuAddress(self, value: int):
        pass

    @property
    def length(self) -> int:
        """
The byte length of the buffer.

:type: int

"""
        pass

    @length.setter
    def length(self, value: int):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The unique :class:`ResourceId` that identifies this buffer.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521CF00>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.BufferDescription' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.BufferDescription' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.BufferDescription' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.BufferDescription' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.BufferDescription' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.BufferDescription' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.BufferDescription' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.BufferDescription' objects>, 'creationFlags': <attribute 'creationFlags' of 'renderdoc.BufferDescription' objects>, 'length': <attribute 'length' of 'renderdoc.BufferDescription' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.BufferDescription' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.BufferDescription' objects>, 'gpuAddress': <attribute 'gpuAddress' of 'renderdoc.BufferDescription' objects>, '__doc__': 'A description of a buffer resource.'})"


