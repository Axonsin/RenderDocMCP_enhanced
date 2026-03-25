# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ColorBlend import ColorBlend

class VKColorBlendState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the pipeline blending state. """
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
    def alphaToCoverageEnable(self) -> bool:
        """
``True`` if alpha-to-coverage should be used when blending to an MSAA target.

:type: bool

"""
        pass

    @alphaToCoverageEnable.setter
    def alphaToCoverageEnable(self, value: bool):
        pass

    @property
    def alphaToOneEnable(self) -> bool:
        """
``True`` if alpha-to-one should be used when blending to an MSAA target.

:type: bool

"""
        pass

    @alphaToOneEnable.setter
    def alphaToOneEnable(self, value: bool):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C9660>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKColorBlendState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKColorBlendState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKColorBlendState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKColorBlendState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKColorBlendState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKColorBlendState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKColorBlendState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKColorBlendState' objects>, 'blends': <attribute 'blends' of 'renderdoc.VKColorBlendState' objects>, 'blendFactor': <attribute 'blendFactor' of 'renderdoc.VKColorBlendState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKColorBlendState' objects>, 'alphaToCoverageEnable': <attribute 'alphaToCoverageEnable' of 'renderdoc.VKColorBlendState' objects>, 'alphaToOneEnable': <attribute 'alphaToOneEnable' of 'renderdoc.VKColorBlendState' objects>, '__doc__': 'Describes the pipeline blending state.'})"


