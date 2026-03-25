# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId

class PointerVal(): # skipped bases: <class 'SwigPyObject'>
    """ A 64-bit pointer value with optional type information. """
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
    def pointer(self) -> int:
        """
The actual pointer value itself.

:type: int

"""
        pass

    @pointer.setter
    def pointer(self, value: int):
        pass

    @property
    def pointerTypeID(self) -> int:
        """
The index into :data:`ShaderReflection.pointerTypes` of the pointed type.

:type: int

"""
        pass

    @pointerTypeID.setter
    def pointerTypeID(self, value: int):
        pass

    @property
    def shader(self) -> ResourceId:
        """
An optional :class:`ResourceId` identifying the shader containing the type info.

:type: ResourceId

"""
        pass

    @shader.setter
    def shader(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55215810>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PointerVal' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PointerVal' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PointerVal' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PointerVal' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PointerVal' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PointerVal' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PointerVal' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PointerVal' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PointerVal' objects>, 'shader': <attribute 'shader' of 'renderdoc.PointerVal' objects>, 'pointer': <attribute 'pointer' of 'renderdoc.PointerVal' objects>, 'pointerTypeID': <attribute 'pointerTypeID' of 'renderdoc.PointerVal' objects>, '__doc__': 'A 64-bit pointer value with optional type information.'})"


