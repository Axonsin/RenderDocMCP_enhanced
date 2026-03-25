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
from .LineRaster import LineRaster
from .ShadingRateCombiner import ShadingRateCombiner
from .ResourceId import ResourceId

class D3D12RasterizerState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state in the PSO. """
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
    def baseShadingRate(self) -> Tuple[int,int]:
        """
The current base variable shading rate. This will always be 1x1 when variable shading
is disabled.

:type: Tuple[int,int]

"""
        pass

    @baseShadingRate.setter
    def baseShadingRate(self, value: Tuple[int,int]):
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
    def depthBias(self) -> float:
        """
The fixed depth bias value to apply to z-values.

:type: float

"""
        pass

    @depthBias.setter
    def depthBias(self, value: float):
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
    def lineRasterMode(self) -> LineRaster:
        """
The line rasterization mode.

:type: LineRaster

"""
        pass

    @lineRasterMode.setter
    def lineRasterMode(self, value: LineRaster):
        pass

    @property
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner,ShadingRateCombiner]:
        """
The shading rate combiners.

The combiners are applied as follows, according to the D3D spec:

  ``intermediateRate = combiner[0] ( baseShadingRate,  shaderExportedShadingRate )``
  ``finalRate        = combiner[1] ( intermediateRate, imageBasedShadingRate     )``

Where the first input is from :data:`baseShadingRate` and the second is the exported shading rate
from a vertex or geometry shader, which defaults to 1x1 if not exported.

The intermediate result is then used as the first input to the second combiner, together with the
shading rate sampled from the shading rate image.

:type: Tuple[ShadingRateCombiner,ShadingRateCombiner]

"""
        pass

    @shadingRateCombiners.setter
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner,ShadingRateCombiner]):
        pass

    @property
    def shadingRateImage(self) -> ResourceId:
        """
The image bound as a shading rate image.

:type: ResourceId

"""
        pass

    @shadingRateImage.setter
    def shadingRateImage(self, value: ResourceId):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E8A60>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12RasterizerState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12RasterizerState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12RasterizerState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12RasterizerState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12RasterizerState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12RasterizerState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12RasterizerState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12RasterizerState' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.D3D12RasterizerState' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.D3D12RasterizerState' objects>, 'depthBiasClamp': <attribute 'depthBiasClamp' of 'renderdoc.D3D12RasterizerState' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.D3D12RasterizerState' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.D3D12RasterizerState' objects>, 'depthClip': <attribute 'depthClip' of 'renderdoc.D3D12RasterizerState' objects>, 'baseShadingRate': <attribute 'baseShadingRate' of 'renderdoc.D3D12RasterizerState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12RasterizerState' objects>, 'shadingRateCombiners': <attribute 'shadingRateCombiners' of 'renderdoc.D3D12RasterizerState' objects>, 'shadingRateImage': <attribute 'shadingRateImage' of 'renderdoc.D3D12RasterizerState' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.D3D12RasterizerState' objects>, 'forcedSampleCount': <attribute 'forcedSampleCount' of 'renderdoc.D3D12RasterizerState' objects>, 'lineRasterMode': <attribute 'lineRasterMode' of 'renderdoc.D3D12RasterizerState' objects>, 'conservativeRasterization': <attribute 'conservativeRasterization' of 'renderdoc.D3D12RasterizerState' objects>, '__doc__': 'Describes the rasterizer state in the PSO.'})"


