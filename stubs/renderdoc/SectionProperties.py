# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SectionFlags import SectionFlags
from .SectionType import SectionType

class SectionProperties(): # skipped bases: <class 'SwigPyObject'>
    """ Properties of a section in a renderdoc capture file. """
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
    def compressedSize(self) -> int:
        """
The number of bytes of data in this section when compressed on disk.

:type: int

"""
        pass

    @compressedSize.setter
    def compressedSize(self, value: int):
        pass

    @property
    def flags(self) -> SectionFlags:
        """
The flags describing how this section is stored.

:type: SectionFlags

"""
        pass

    @flags.setter
    def flags(self, value: SectionFlags):
        pass

    @property
    def name(self) -> str:
        """
The name of this section.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> SectionType:
        """
The type of this section, if it is a known pre-defined section.

:type: SectionType

"""
        pass

    @type.setter
    def type(self, value: SectionType):
        pass

    @property
    def uncompressedSize(self) -> int:
        """
The number of bytes of data contained in this section, once uncompressed.

:type: int

"""
        pass

    @uncompressedSize.setter
    def uncompressedSize(self, value: int):
        pass

    @property
    def version(self) -> int:
        """
The version of this section - the meaning of which is up to the type.

:type: int

"""
        pass

    @version.setter
    def version(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552330C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SectionProperties' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SectionProperties' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SectionProperties' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SectionProperties' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SectionProperties' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SectionProperties' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SectionProperties' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SectionProperties' objects>, 'name': <attribute 'name' of 'renderdoc.SectionProperties' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SectionProperties' objects>, 'type': <attribute 'type' of 'renderdoc.SectionProperties' objects>, 'flags': <attribute 'flags' of 'renderdoc.SectionProperties' objects>, 'version': <attribute 'version' of 'renderdoc.SectionProperties' objects>, 'uncompressedSize': <attribute 'uncompressedSize' of 'renderdoc.SectionProperties' objects>, 'compressedSize': <attribute 'compressedSize' of 'renderdoc.SectionProperties' objects>, '__doc__': 'Properties of a section in a renderdoc capture file.'})"


