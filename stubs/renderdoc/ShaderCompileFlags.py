# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderCompileFlag import ShaderCompileFlag

class ShaderCompileFlags(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the information about the compilation environment of a shader """
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
    def flags(self) -> List[ShaderCompileFlag]:
        """
The API or compiler specific flags used to compile this shader originally.

:type: List[ShaderCompileFlag]

"""
        pass

    @flags.setter
    def flags(self, value: List[ShaderCompileFlag]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551ABE20>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderCompileFlags' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderCompileFlags' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderCompileFlags' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderCompileFlags' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderCompileFlags' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderCompileFlags' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderCompileFlags' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderCompileFlags' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderCompileFlags' objects>, 'flags': <attribute 'flags' of 'renderdoc.ShaderCompileFlags' objects>, '__doc__': 'Contains the information about the compilation environment of a shader'})"


