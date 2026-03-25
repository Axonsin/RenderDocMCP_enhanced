# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class GLFeedback(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the current feedback state. """
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
``True`` if the transform feedback object is currently active.

:type: bool

"""
        pass

    @active.setter
    def active(self, value: bool):
        pass

    @property
    def bufferResourceId(self) -> Tuple[ResourceId,ResourceId,ResourceId,ResourceId]:
        """
The buffer bindings.

:type: Tuple[ResourceId,ResourceId,ResourceId,ResourceId]

"""
        pass

    @bufferResourceId.setter
    def bufferResourceId(self, value: Tuple[ResourceId,ResourceId,ResourceId,ResourceId]):
        pass

    @property
    def byteOffset(self) -> Tuple[int,int,int,int]:
        """
The buffer byte offsets.

:type: Tuple[int,int,int,int]

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: Tuple[int,int,int,int]):
        pass

    @property
    def byteSize(self) -> Tuple[int,int,int,int]:
        """
The buffer byte sizes.

:type: Tuple[int,int,int,int]

"""
        pass

    @byteSize.setter
    def byteSize(self, value: Tuple[int,int,int,int]):
        pass

    @property
    def feedbackResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the transform feedback binding.

:type: ResourceId

"""
        pass

    @feedbackResourceId.setter
    def feedbackResourceId(self, value: ResourceId):
        pass

    @property
    def paused(self) -> bool:
        """
``True`` if the transform feedback object is currently paused.

:type: bool

"""
        pass

    @paused.setter
    def paused(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D9BC0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLFeedback' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLFeedback' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLFeedback' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLFeedback' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLFeedback' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLFeedback' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLFeedback' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLFeedback' objects>, 'feedbackResourceId': <attribute 'feedbackResourceId' of 'renderdoc.GLFeedback' objects>, 'bufferResourceId': <attribute 'bufferResourceId' of 'renderdoc.GLFeedback' objects>, 'active': <attribute 'active' of 'renderdoc.GLFeedback' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLFeedback' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.GLFeedback' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.GLFeedback' objects>, 'paused': <attribute 'paused' of 'renderdoc.GLFeedback' objects>, '__doc__': 'Describes the current feedback state.'})"


