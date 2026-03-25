# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class VKDescriptorBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ A single descriptor buffer binding. """
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
    def buffer(self) -> ResourceId:
        """
The :class:`ResourceId` of the buffer object being bound.

:type: ResourceId

"""
        pass

    @buffer.setter
    def buffer(self, value: ResourceId):
        pass

    @property
    def offset(self) -> int:
        """
The offset in bytes from the base of the buffer object to the start of the bound region.

:type: int

"""
        pass

    @offset.setter
    def offset(self, value: int):
        pass

    @property
    def pushBuffer(self) -> ResourceId:
        """
For push descriptors where a buffer is required, the :class:`ResourceId` of the push buffer object.

:type: ResourceId

"""
        pass

    @pushBuffer.setter
    def pushBuffer(self, value: ResourceId):
        pass

    @property
    def pushDescriptor(self) -> bool:
        """
Indicates if this is the 'push' descriptor buffer.

:type: bool

"""
        pass

    @pushDescriptor.setter
    def pushDescriptor(self, value: bool):
        pass

    @property
    def resourceBuffer(self) -> bool:
        """
Indicates if this buffer can contain resources (buffers and images).

:type: bool

"""
        pass

    @resourceBuffer.setter
    def resourceBuffer(self, value: bool):
        pass

    @property
    def samplerBuffer(self) -> bool:
        """
Indicates if this buffer can contain samplers.

:type: bool

"""
        pass

    @samplerBuffer.setter
    def samplerBuffer(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552377D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKDescriptorBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKDescriptorBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKDescriptorBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKDescriptorBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKDescriptorBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKDescriptorBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKDescriptorBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKDescriptorBuffer' objects>, 'pushDescriptor': <attribute 'pushDescriptor' of 'renderdoc.VKDescriptorBuffer' objects>, 'pushBuffer': <attribute 'pushBuffer' of 'renderdoc.VKDescriptorBuffer' objects>, 'samplerBuffer': <attribute 'samplerBuffer' of 'renderdoc.VKDescriptorBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKDescriptorBuffer' objects>, 'offset': <attribute 'offset' of 'renderdoc.VKDescriptorBuffer' objects>, 'buffer': <attribute 'buffer' of 'renderdoc.VKDescriptorBuffer' objects>, 'resourceBuffer': <attribute 'resourceBuffer' of 'renderdoc.VKDescriptorBuffer' objects>, '__doc__': 'A single descriptor buffer binding.'})"


