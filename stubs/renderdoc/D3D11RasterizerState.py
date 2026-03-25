# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ConservativeRaster import ConservativeRaster
from .CullMode import CullMode
from .FillMode import FillMode
from .ResourceId import ResourceId

class D3D11RasterizerState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a rasterizer state object. """
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
    def antialiasedLines(self) -> bool:
        """
``True`` if lines should be anti-aliased. Ignored if :data:`multisampleEnable` is  ``False``.

:type: bool

"""
        pass

    @antialiasedLines.setter
    def antialiasedLines(self, value: bool):
        pass

    @property
    def conservativeRasterization(self) -> ConservativeRaster:
        """
The current :class:`ConservativeRaster` mode.

:type: ConservativeRaster

"""
        pass

    @conservativeRasterization.setter
    def conservativeRasterization(self, value: ConservativeRaster):
        pass

    @property
    def cullMode(self) -> CullMode:
        """
The polygon :class:`CullMode`.

:type: CullMode

"""
        pass

    @cullMode.setter
    def cullMode(self, value: CullMode):
        pass

    @property
    def depthBias(self) -> int:
        """
The fixed depth bias value to apply to z-values.

:type: int

"""
        pass

    @depthBias.setter
    def depthBias(self, value: int):
        pass

    @property
    def depthBiasClamp(self) -> float:
        """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

:type: float

"""
        pass

    @depthBiasClamp.setter
    def depthBiasClamp(self, value: float):
        pass

    @property
    def depthClip(self) -> bool:
        """
``True`` if pixels outside of the near and far depth planes should be clipped.

:type: bool

"""
        pass

    @depthClip.setter
    def depthClip(self, value: bool):
        pass

    @property
    def fillMode(self) -> FillMode:
        """
The polygon :class:`FillMode`.

:type: FillMode

"""
        pass

    @fillMode.setter
    def fillMode(self, value: FillMode):
        pass

    @property
    def forcedSampleCount(self) -> int:
        """
A sample count to force rasterization to when UAV rendering or rasterizing, or 0 to
not force any sample count.

:type: int

"""
        pass

    @forcedSampleCount.setter
    def forcedSampleCount(self, value: int):
        pass

    @property
    def frontCCW(self) -> bool:
        """
``True`` if counter-clockwise polygons are front-facing.
``False`` if clockwise polygons are front-facing.

:type: bool

"""
        pass

    @frontCCW.setter
    def frontCCW(self, value: bool):
        pass

    @property
    def multisampleEnable(self) -> bool:
        """
``True`` if the quadrilateral MSAA algorithm should be used on MSAA targets.

:type: bool

"""
        pass

    @multisampleEnable.setter
    def multisampleEnable(self, value: bool):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the rasterizer state object.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    @property
    def scissorEnable(self) -> bool:
        """
``True`` if the scissor test should be applied.

:type: bool

"""
        pass

    @scissorEnable.setter
    def scissorEnable(self, value: bool):
        pass

    @property
    def slopeScaledDepthBias(self) -> float:
        """
The slope-scaled depth bias value to apply to z-values.

:type: float

"""
        pass

    @slopeScaledDepthBias.setter
    def slopeScaledDepthBias(self, value: float):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D7C60>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11RasterizerState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11RasterizerState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11RasterizerState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11RasterizerState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11RasterizerState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11RasterizerState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11RasterizerState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11RasterizerState' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.D3D11RasterizerState' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.D3D11RasterizerState' objects>, 'depthBiasClamp': <attribute 'depthBiasClamp' of 'renderdoc.D3D11RasterizerState' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.D3D11RasterizerState' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.D3D11RasterizerState' objects>, 'depthClip': <attribute 'depthClip' of 'renderdoc.D3D11RasterizerState' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D11RasterizerState' objects>, 'antialiasedLines': <attribute 'antialiasedLines' of 'renderdoc.D3D11RasterizerState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11RasterizerState' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.D3D11RasterizerState' objects>, 'multisampleEnable': <attribute 'multisampleEnable' of 'renderdoc.D3D11RasterizerState' objects>, 'forcedSampleCount': <attribute 'forcedSampleCount' of 'renderdoc.D3D11RasterizerState' objects>, 'scissorEnable': <attribute 'scissorEnable' of 'renderdoc.D3D11RasterizerState' objects>, 'conservativeRasterization': <attribute 'conservativeRasterization' of 'renderdoc.D3D11RasterizerState' objects>, '__doc__': 'Describes a rasterizer state object.'})"


