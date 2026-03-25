# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .PathProperty import PathProperty

class PathEntry(): # skipped bases: <class 'SwigPyObject'>
    """ Properties of a path on a remote filesystem. """
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
    def filename(self) -> str:
        """
The filename of this path. This contains only the filename, not the full path.

:type: str

"""
        pass

    @filename.setter
    def filename(self, value: str):
        pass

    @property
    def flags(self) -> PathProperty:
        """
The :class:`PathProperty` flags for this path.

:type: PathProperty

"""
        pass

    @flags.setter
    def flags(self, value: PathProperty):
        pass

    @property
    def lastmod(self) -> int:
        """
The last modified date of this path, as a unix timestamp in UTC.

:type: int

"""
        pass

    @lastmod.setter
    def lastmod(self, value: int):
        pass

    @property
    def size(self) -> int:
        """
The size of the path in bytes.

:type: int

"""
        pass

    @size.setter
    def size(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551FC1A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PathEntry' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PathEntry' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PathEntry' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PathEntry' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PathEntry' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PathEntry' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PathEntry' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PathEntry' objects>, 'lastmod': <attribute 'lastmod' of 'renderdoc.PathEntry' objects>, 'size': <attribute 'size' of 'renderdoc.PathEntry' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PathEntry' objects>, 'filename': <attribute 'filename' of 'renderdoc.PathEntry' objects>, 'flags': <attribute 'flags' of 'renderdoc.PathEntry' objects>, '__doc__': 'Properties of a path on a remote filesystem.'})"


