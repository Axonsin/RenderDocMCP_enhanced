# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class SDObjectPODData(): # skipped bases: <class 'SwigPyObject'>
    """
    The plain-old-data contents of an :class:`SDObject`.
    
    Only one member is valid, as defined by the type of the :class:`SDObject`.
    """
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
    def b(self) -> bool:
        """
The value as a boolean.

:type: bool

"""
        pass

    @b.setter
    def b(self, value: bool):
        pass

    @property
    def c(self) -> str:
        """
The value as a single byte character.

:type: str

"""
        pass

    @c.setter
    def c(self, value: str):
        pass

    @property
    def d(self) -> float:
        """
The value as a floating point number.

:type: float

"""
        pass

    @d.setter
    def d(self, value: float):
        pass

    @property
    def i(self) -> int:
        """
The value as a signed integer.

:type: int

"""
        pass

    @i.setter
    def i(self, value: int):
        pass

    @property
    def id(self) -> ResourceId:
        """
The value as a :class:`ResourceId`

:type: ResourceId

"""
        pass

    @id.setter
    def id(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def u(self) -> int:
        """
The value as an unsigned integer.

:type: int

"""
        pass

    @u.setter
    def u(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551EE430>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDObjectPODData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDObjectPODData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDObjectPODData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDObjectPODData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDObjectPODData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDObjectPODData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDObjectPODData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDObjectPODData' objects>, 'i': <attribute 'i' of 'renderdoc.SDObjectPODData' objects>, 'b': <attribute 'b' of 'renderdoc.SDObjectPODData' objects>, 'c': <attribute 'c' of 'renderdoc.SDObjectPODData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDObjectPODData' objects>, 'd': <attribute 'd' of 'renderdoc.SDObjectPODData' objects>, 'id': <attribute 'id' of 'renderdoc.SDObjectPODData' objects>, 'u': <attribute 'u' of 'renderdoc.SDObjectPODData' objects>, '__doc__': '\\nThe plain-old-data contents of an :class:`SDObject`.\\n\\nOnly one member is valid, as defined by the type of the :class:`SDObject`.\\n\\n'})"


