# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FileType import FileType

class Thumbnail(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the bytes and metadata describing a thumbnail. """
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
    def data(self) -> bytes:
        """
The ``bytes`` byte array containing the raw data.

:type: bytes

"""
        pass

    @data.setter
    def data(self, value: bytes):
        pass

    @property
    def height(self) -> int:
        """
The height of the thumbnail image.

:type: int

"""
        pass

    @height.setter
    def height(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> FileType:
        """
The :class:`FileType` of the data in the thumbnail.

:type: FileType

"""
        pass

    @type.setter
    def type(self, value: FileType):
        pass

    @property
    def width(self) -> int:
        """
The width of the thumbnail image.

:type: int

"""
        pass

    @width.setter
    def width(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55214060>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.Thumbnail' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.Thumbnail' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.Thumbnail' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.Thumbnail' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.Thumbnail' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.Thumbnail' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.Thumbnail' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.Thumbnail' objects>, 'height': <attribute 'height' of 'renderdoc.Thumbnail' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.Thumbnail' objects>, 'width': <attribute 'width' of 'renderdoc.Thumbnail' objects>, 'type': <attribute 'type' of 'renderdoc.Thumbnail' objects>, 'data': <attribute 'data' of 'renderdoc.Thumbnail' objects>, '__doc__': 'Contains the bytes and metadata describing a thumbnail.'})"


