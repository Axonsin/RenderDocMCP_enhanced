# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKDynamicOffset(): # skipped bases: <class 'SwigPyObject'>
    """ A dynamic offset applied to a single descriptor access. """
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
    def descriptorByteOffset(self) -> int:
        """
The offset in bytes to the descriptor in the storage.

:type: int

"""
        pass

    @descriptorByteOffset.setter
    def descriptorByteOffset(self, value: int):
        pass

    @property
    def dynamicBufferByteOffset(self) -> int:
        """
The dynamic offset to apply to the buffer in bytes.

:type: int

"""
        pass

    @dynamicBufferByteOffset.setter
    def dynamicBufferByteOffset(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521DD80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKDynamicOffset' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKDynamicOffset' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKDynamicOffset' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKDynamicOffset' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKDynamicOffset' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKDynamicOffset' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKDynamicOffset' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKDynamicOffset' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKDynamicOffset' objects>, 'descriptorByteOffset': <attribute 'descriptorByteOffset' of 'renderdoc.VKDynamicOffset' objects>, 'dynamicBufferByteOffset': <attribute 'dynamicBufferByteOffset' of 'renderdoc.VKDynamicOffset' objects>, '__doc__': 'A dynamic offset applied to a single descriptor access.'})"


