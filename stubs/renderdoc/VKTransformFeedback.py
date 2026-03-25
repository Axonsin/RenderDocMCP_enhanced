# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKXFBBuffer import VKXFBBuffer

class VKTransformFeedback(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the state of the fixed-function transform feedback. """
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
    def buffers(self) -> List[VKXFBBuffer]:
        """
The bound transform feedback buffers.

:type: List[VKXFBBuffer]

"""
        pass

    @buffers.setter
    def buffers(self, value: List[VKXFBBuffer]):
        pass

    @property
    def rasterizedStream(self) -> int:
        """
Which stream-out stream is being used for rasterization.

:type: int

"""
        pass

    @rasterizedStream.setter
    def rasterizedStream(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521EAD0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKTransformFeedback' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKTransformFeedback' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKTransformFeedback' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKTransformFeedback' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKTransformFeedback' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKTransformFeedback' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKTransformFeedback' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKTransformFeedback' objects>, 'buffers': <attribute 'buffers' of 'renderdoc.VKTransformFeedback' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKTransformFeedback' objects>, 'rasterizedStream': <attribute 'rasterizedStream' of 'renderdoc.VKTransformFeedback' objects>, '__doc__': 'Describes the state of the fixed-function transform feedback.'})"


