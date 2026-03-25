# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class VKXFBBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a single transform feedback binding. """
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
    def active(self) -> bool:
        """
A flag indicating if this buffer is active or not.

:type: bool

"""
        pass

    @active.setter
    def active(self, value: bool):
        pass

    @property
    def bufferResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the bound data buffer.

:type: ResourceId

"""
        pass

    @bufferResourceId.setter
    def bufferResourceId(self, value: ResourceId):
        pass

    @property
    def byteOffset(self) -> int:
        """
The offset in bytes to the start of the data in the :data:`bufferResourceId`.

:type: int

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: int):
        pass

    @property
    def byteSize(self) -> int:
        """
The size in bytes of the data buffer.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def counterBufferOffset(self) -> int:
        """
The offset in bytes to the counter in the :data:`counterBufferResourceId`.

:type: int

"""
        pass

    @counterBufferOffset.setter
    def counterBufferOffset(self, value: int):
        pass

    @property
    def counterBufferResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the buffer storing the counter value (if set).

:type: ResourceId

"""
        pass

    @counterBufferResourceId.setter
    def counterBufferResourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F5D30>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKXFBBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKXFBBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKXFBBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKXFBBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKXFBBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKXFBBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKXFBBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKXFBBuffer' objects>, 'active': <attribute 'active' of 'renderdoc.VKXFBBuffer' objects>, 'bufferResourceId': <attribute 'bufferResourceId' of 'renderdoc.VKXFBBuffer' objects>, 'counterBufferResourceId': <attribute 'counterBufferResourceId' of 'renderdoc.VKXFBBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKXFBBuffer' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VKXFBBuffer' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.VKXFBBuffer' objects>, 'counterBufferOffset': <attribute 'counterBufferOffset' of 'renderdoc.VKXFBBuffer' objects>, '__doc__': 'Describes a single transform feedback binding.'})"


