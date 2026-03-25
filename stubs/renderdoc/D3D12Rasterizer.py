# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Scissor import Scissor
from .D3D12RasterizerState import D3D12RasterizerState
from .Viewport import Viewport

class D3D12Rasterizer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterization state of the D3D12 pipeline. """
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
    def sampleMask(self) -> int:
        """
The mask determining which samples are written to.

:type: int

"""
        pass

    @sampleMask.setter
    def sampleMask(self, value: int):
        pass

    @property
    def scissors(self) -> List[Scissor]:
        """
The bound scissor regions.

:type: List[Scissor]

"""
        pass

    @scissors.setter
    def scissors(self, value: List[Scissor]):
        pass

    @property
    def state(self) -> D3D12RasterizerState:
        """
The details of the rasterization state.

:type: D3D12RasterizerState

"""
        pass

    @state.setter
    def state(self, value: D3D12RasterizerState):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def viewports(self) -> List[Viewport]:
        """
The bound viewports.

:type: List[Viewport]

"""
        pass

    @viewports.setter
    def viewports(self, value: List[Viewport]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55228DD0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12Rasterizer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12Rasterizer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12Rasterizer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12Rasterizer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12Rasterizer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12Rasterizer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12Rasterizer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12Rasterizer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12Rasterizer' objects>, 'sampleMask': <attribute 'sampleMask' of 'renderdoc.D3D12Rasterizer' objects>, 'scissors': <attribute 'scissors' of 'renderdoc.D3D12Rasterizer' objects>, 'state': <attribute 'state' of 'renderdoc.D3D12Rasterizer' objects>, 'viewports': <attribute 'viewports' of 'renderdoc.D3D12Rasterizer' objects>, '__doc__': 'Describes the rasterization state of the D3D12 pipeline.'})"


