# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKImageLayout import VKImageLayout
from .ResourceId import ResourceId

class VKImageData(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the current layout of all subresources in the image. """
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
    def layouts(self) -> List[VKImageLayout]:
        """
The subresource regions in this resource.

:type: List[VKImageLayout]

"""
        pass

    @layouts.setter
    def layouts(self, value: List[VKImageLayout]):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the image.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C15D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKImageData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKImageData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKImageData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKImageData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKImageData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKImageData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKImageData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKImageData' objects>, 'layouts': <attribute 'layouts' of 'renderdoc.VKImageData' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.VKImageData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKImageData' objects>, '__doc__': 'Contains the current layout of all subresources in the image.'})"


