# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ColorBlend import ColorBlend

class D3D12BlendState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the blend state in the PSO. """
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
    def alphaToCoverage(self) -> bool:
        """
``True`` if alpha-to-coverage should be used when blending to an MSAA target.

:type: bool

"""
        pass

    @alphaToCoverage.setter
    def alphaToCoverage(self, value: bool):
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

    @property
    def independentBlend(self) -> bool:
        """
``True`` if independent blending for each target should be used.

``False`` if the first blend should be applied to all targets.

:type: bool

"""
        pass

    @independentBlend.setter
    def independentBlend(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551DA4E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12BlendState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12BlendState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12BlendState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12BlendState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12BlendState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12BlendState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12BlendState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12BlendState' objects>, 'blends': <attribute 'blends' of 'renderdoc.D3D12BlendState' objects>, 'independentBlend': <attribute 'independentBlend' of 'renderdoc.D3D12BlendState' objects>, 'blendFactor': <attribute 'blendFactor' of 'renderdoc.D3D12BlendState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12BlendState' objects>, 'alphaToCoverage': <attribute 'alphaToCoverage' of 'renderdoc.D3D12BlendState' objects>, '__doc__': 'Describes the blend state in the PSO.'})"


