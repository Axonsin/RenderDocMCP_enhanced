# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SDBasic import SDBasic
from .SDTypeFlags import SDTypeFlags

class SDType(): # skipped bases: <class 'SwigPyObject'>
    """ Details the name and properties of a structured type """
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
    def basetype(self) -> SDBasic:
        """
The :class:`SDBasic` category that this type belongs to.

:type: SDBasic

"""
        pass

    @basetype.setter
    def basetype(self, value: SDBasic):
        pass

    @property
    def byteSize(self) -> int:
        """
The size in bytes that an instance of this type takes up.

This is only valid for whole chunks (where it contains the whole chunk size), for buffers that have
an arbitrary size, or for basic types such as integers and floating point values where it gives the
size/precision of the type.

For variable size types like structs, arrays, etc it will be set to 0.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def flags(self) -> SDTypeFlags:
        """
The :class:`SDTypeFlags` flags for this type.

:type: SDTypeFlags

"""
        pass

    @flags.setter
    def flags(self, value: SDTypeFlags):
        pass

    @property
    def name(self) -> str:
        """
The name of this type.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551AE5A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDType' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDType' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDType' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDType' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDType' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDType' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDType' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDType' objects>, 'name': <attribute 'name' of 'renderdoc.SDType' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDType' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.SDType' objects>, 'basetype': <attribute 'basetype' of 'renderdoc.SDType' objects>, 'flags': <attribute 'flags' of 'renderdoc.SDType' objects>, '__doc__': 'Details the name and properties of a structured type'})"


