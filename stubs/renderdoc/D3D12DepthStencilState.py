# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .StencilFace import StencilFace
from .CompareFunction import CompareFunction

class D3D12DepthStencilState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the state of the depth-stencil state in the PSO. """
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
    def backFace(self) -> StencilFace:
        """
The stencil state for back-facing polygons.

:type: StencilFace

"""
        pass

    @backFace.setter
    def backFace(self, value: StencilFace):
        pass

    @property
    def depthBoundsEnable(self) -> bool:
        """
``True`` if depth bounds tests should be applied.

:type: bool

"""
        pass

    @depthBoundsEnable.setter
    def depthBoundsEnable(self, value: bool):
        pass

    @property
    def depthEnable(self) -> bool:
        """
``True`` if depth testing should be performed.

:type: bool

"""
        pass

    @depthEnable.setter
    def depthEnable(self, value: bool):
        pass

    @property
    def depthFunction(self) -> CompareFunction:
        """
The :class:`CompareFunction` to use for testing depth values.

:type: CompareFunction

"""
        pass

    @depthFunction.setter
    def depthFunction(self, value: CompareFunction):
        pass

    @property
    def depthWrites(self) -> bool:
        """
``True`` if depth values should be written to the depth target.

:type: bool

"""
        pass

    @depthWrites.setter
    def depthWrites(self, value: bool):
        pass

    @property
    def frontFace(self) -> StencilFace:
        """
The stencil state for front-facing polygons.

:type: StencilFace

"""
        pass

    @frontFace.setter
    def frontFace(self, value: StencilFace):
        pass

    @property
    def maxDepthBounds(self) -> float:
        """
The far plane bounding value.

:type: float

"""
        pass

    @maxDepthBounds.setter
    def maxDepthBounds(self, value: float):
        pass

    @property
    def minDepthBounds(self) -> float:
        """
The near plane bounding value.

:type: float

"""
        pass

    @minDepthBounds.setter
    def minDepthBounds(self, value: float):
        pass

    @property
    def stencilEnable(self) -> bool:
        """
``True`` if stencil operations should be performed.

:type: bool

"""
        pass

    @stencilEnable.setter
    def stencilEnable(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521FD80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12DepthStencilState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12DepthStencilState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12DepthStencilState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12DepthStencilState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12DepthStencilState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12DepthStencilState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12DepthStencilState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12DepthStencilState' objects>, 'frontFace': <attribute 'frontFace' of 'renderdoc.D3D12DepthStencilState' objects>, 'backFace': <attribute 'backFace' of 'renderdoc.D3D12DepthStencilState' objects>, 'depthFunction': <attribute 'depthFunction' of 'renderdoc.D3D12DepthStencilState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12DepthStencilState' objects>, 'depthBoundsEnable': <attribute 'depthBoundsEnable' of 'renderdoc.D3D12DepthStencilState' objects>, 'minDepthBounds': <attribute 'minDepthBounds' of 'renderdoc.D3D12DepthStencilState' objects>, 'maxDepthBounds': <attribute 'maxDepthBounds' of 'renderdoc.D3D12DepthStencilState' objects>, 'depthEnable': <attribute 'depthEnable' of 'renderdoc.D3D12DepthStencilState' objects>, 'depthWrites': <attribute 'depthWrites' of 'renderdoc.D3D12DepthStencilState' objects>, 'stencilEnable': <attribute 'stencilEnable' of 'renderdoc.D3D12DepthStencilState' objects>, '__doc__': 'Describes the state of the depth-stencil state in the PSO.'})"


