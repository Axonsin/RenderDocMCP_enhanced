# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderEncoding import ShaderEncoding

class ShaderSourcePrefix(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the source prefix to add to a given type of shader source """
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
    def encoding(self) -> ShaderEncoding:
        """
The encoding of the language this prefix applies to.

:type: ShaderEncoding

"""
        pass

    @encoding.setter
    def encoding(self, value: ShaderEncoding):
        pass

    @property
    def prefix(self) -> str:
        """
The source prefix to add.

:type: str

"""
        pass

    @prefix.setter
    def prefix(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C6050>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderSourcePrefix' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderSourcePrefix' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderSourcePrefix' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderSourcePrefix' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderSourcePrefix' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderSourcePrefix' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderSourcePrefix' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderSourcePrefix' objects>, 'prefix': <attribute 'prefix' of 'renderdoc.ShaderSourcePrefix' objects>, 'encoding': <attribute 'encoding' of 'renderdoc.ShaderSourcePrefix' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderSourcePrefix' objects>, '__doc__': 'Contains the source prefix to add to a given type of shader source'})"


