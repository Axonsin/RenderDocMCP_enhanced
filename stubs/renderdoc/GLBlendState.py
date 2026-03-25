# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ColorBlend import ColorBlend

class GLBlendState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the blend pipeline state. """
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
    def blendFactor(self) -> Tuple[float,float,float,float]:
        """
The constant blend factor to use in blend equations.

:type: Tuple[float,float,float,float]

"""
        pass

    @blendFactor.setter
    def blendFactor(self, value: Tuple[float,float,float,float]):
        pass

    @property
    def blends(self) -> List[ColorBlend]:
        """
The blend operations for each target.

:type: List[ColorBlend]

"""
        pass

    @blends.setter
    def blends(self, value: List[ColorBlend]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E75A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLBlendState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLBlendState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLBlendState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLBlendState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLBlendState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLBlendState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLBlendState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLBlendState' objects>, 'blends': <attribute 'blends' of 'renderdoc.GLBlendState' objects>, 'blendFactor': <attribute 'blendFactor' of 'renderdoc.GLBlendState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLBlendState' objects>, '__doc__': 'Describes the blend pipeline state.'})"


