# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Descriptor import Descriptor
from .ResourceId import ResourceId

class VKFramebuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a framebuffer object and its attachments. """
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
    def attachments(self) -> List[Descriptor]:
        """
The attachments of this framebuffer.

:type: List[Descriptor]

"""
        pass

    @attachments.setter
    def attachments(self, value: List[Descriptor]):
        pass

    @property
    def height(self) -> int:
        """
The height of this framebuffer in pixels.

:type: int

"""
        pass

    @height.setter
    def height(self, value: int):
        pass

    @property
    def layers(self) -> int:
        """
The number of layers in this framebuffer.

:type: int

"""
        pass

    @layers.setter
    def layers(self, value: int):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the framebuffer object.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def width(self) -> int:
        """
The width of this framebuffer in pixels.

:type: int

"""
        pass

    @width.setter
    def width(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E5850>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKFramebuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKFramebuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKFramebuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKFramebuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKFramebuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKFramebuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKFramebuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKFramebuffer' objects>, 'attachments': <attribute 'attachments' of 'renderdoc.VKFramebuffer' objects>, 'height': <attribute 'height' of 'renderdoc.VKFramebuffer' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.VKFramebuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKFramebuffer' objects>, 'width': <attribute 'width' of 'renderdoc.VKFramebuffer' objects>, 'layers': <attribute 'layers' of 'renderdoc.VKFramebuffer' objects>, '__doc__': 'Describes a framebuffer object and its attachments.'})"


