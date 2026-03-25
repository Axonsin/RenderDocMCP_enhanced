# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12BlendState import D3D12BlendState
from .D3D12DepthStencilState import D3D12DepthStencilState
from .Descriptor import Descriptor

class D3D12OM(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the current state of the output-merger stage of the D3D12 pipeline. """
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
    def blendState(self) -> D3D12BlendState:
        """
The current blend state details.

:type: D3D12BlendState

"""
        pass

    @blendState.setter
    def blendState(self, value: D3D12BlendState):
        pass

    @property
    def depthReadOnly(self) -> bool:
        """
``True`` if depth access to the depth-stencil target is read-only.

:type: bool

"""
        pass

    @depthReadOnly.setter
    def depthReadOnly(self, value: bool):
        pass

    @property
    def depthStencilState(self) -> D3D12DepthStencilState:
        """
The current depth-stencil state details.

:type: D3D12DepthStencilState

"""
        pass

    @depthStencilState.setter
    def depthStencilState(self, value: D3D12DepthStencilState):
        pass

    @property
    def depthTarget(self) -> Descriptor:
        """
The currently bound depth-stencil target.

:type: Descriptor

"""
        pass

    @depthTarget.setter
    def depthTarget(self, value: Descriptor):
        pass

    @property
    def multiSampleCount(self) -> int:
        """
The sample count used for rendering.

:type: int

"""
        pass

    @multiSampleCount.setter
    def multiSampleCount(self, value: int):
        pass

    @property
    def multiSampleQuality(self) -> int:
        """
The MSAA quality level used for rendering.

:type: int

"""
        pass

    @multiSampleQuality.setter
    def multiSampleQuality(self, value: int):
        pass

    @property
    def renderTargets(self) -> List[Descriptor]:
        """
The bound render targets.

:type: List[Descriptor]

"""
        pass

    @renderTargets.setter
    def renderTargets(self, value: List[Descriptor]):
        pass

    @property
    def stencilReadOnly(self) -> bool:
        """
``True`` if stenncil access to the depth-stencil target is read-only.

:type: bool

"""
        pass

    @stencilReadOnly.setter
    def stencilReadOnly(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552101F0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12OM' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12OM' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12OM' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12OM' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12OM' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12OM' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12OM' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12OM' objects>, 'depthStencilState': <attribute 'depthStencilState' of 'renderdoc.D3D12OM' objects>, 'multiSampleQuality': <attribute 'multiSampleQuality' of 'renderdoc.D3D12OM' objects>, 'depthTarget': <attribute 'depthTarget' of 'renderdoc.D3D12OM' objects>, 'depthReadOnly': <attribute 'depthReadOnly' of 'renderdoc.D3D12OM' objects>, 'stencilReadOnly': <attribute 'stencilReadOnly' of 'renderdoc.D3D12OM' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12OM' objects>, 'renderTargets': <attribute 'renderTargets' of 'renderdoc.D3D12OM' objects>, 'multiSampleCount': <attribute 'multiSampleCount' of 'renderdoc.D3D12OM' objects>, 'blendState': <attribute 'blendState' of 'renderdoc.D3D12OM' objects>, '__doc__': 'Describes the current state of the output-merger stage of the D3D12 pipeline.'})"


