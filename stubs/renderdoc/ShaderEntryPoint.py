# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderStage import ShaderStage

class ShaderEntryPoint(): # skipped bases: <class 'SwigPyObject'>
    """ Describes an entry point in a shader. """
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
    def name(self) -> str:
        """
The name of the entry point.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def stage(self) -> ShaderStage:
        """
The :class:`ShaderStage` for this entry point .

:type: ShaderStage

"""
        pass

    @stage.setter
    def stage(self, value: ShaderStage):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55229390>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderEntryPoint' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderEntryPoint' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderEntryPoint' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderEntryPoint' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderEntryPoint' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderEntryPoint' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderEntryPoint' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderEntryPoint' objects>, 'name': <attribute 'name' of 'renderdoc.ShaderEntryPoint' objects>, 'stage': <attribute 'stage' of 'renderdoc.ShaderEntryPoint' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderEntryPoint' objects>, '__doc__': 'Describes an entry point in a shader.'})"


