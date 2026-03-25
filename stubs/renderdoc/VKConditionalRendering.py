# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class VKConditionalRendering(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the current conditional rendering state. """
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
    def bufferId(self) -> ResourceId:
        """
The :class:`ResourceId` of the buffer containing the predicate for conditional rendering.

:type: ResourceId

"""
        pass

    @bufferId.setter
    def bufferId(self, value: ResourceId):
        pass

    @property
    def byteOffset(self) -> int:
        """
The byte offset into buffer where the predicate is located.

:type: int

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: int):
        pass

    @property
    def isInverted(self) -> bool:
        """
``True`` if predicate result is inverted.

:type: bool

"""
        pass

    @isInverted.setter
    def isInverted(self, value: bool):
        pass

    @property
    def isPassing(self) -> bool:
        """
``True`` if the current predicate would render.

:type: bool

"""
        pass

    @isPassing.setter
    def isPassing(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551DB020>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKConditionalRendering' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKConditionalRendering' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKConditionalRendering' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKConditionalRendering' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKConditionalRendering' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKConditionalRendering' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKConditionalRendering' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKConditionalRendering' objects>, 'isInverted': <attribute 'isInverted' of 'renderdoc.VKConditionalRendering' objects>, 'bufferId': <attribute 'bufferId' of 'renderdoc.VKConditionalRendering' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKConditionalRendering' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VKConditionalRendering' objects>, 'isPassing': <attribute 'isPassing' of 'renderdoc.VKConditionalRendering' objects>, '__doc__': 'Contains the current conditional rendering state.'})"


