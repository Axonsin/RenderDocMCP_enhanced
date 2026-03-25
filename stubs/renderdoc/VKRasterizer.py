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

class VKRasterizer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state in the pipeline. """
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
    def conservativeRasterization(self) -> ConservativeRaster:
        """
The active conservative rasterization mode.

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
    def depthBiasEnable(self) -> bool:
        """
Whether depth biasing is enabled.

:type: bool

"""
        pass

    @depthBiasEnable.setter
    def depthBiasEnable(self, value: bool):
        pass

    @property
    def depthClampEnable(self) -> bool:
        """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0``.

:type: bool

"""
        pass

    @depthClampEnable.setter
    def depthClampEnable(self, value: bool):
        pass

    @property
    def depthClipEnable(self) -> bool:
        """
``True`` if pixels outside of the near and far depth planes should be clipped.

.. note::
  In Vulkan 1.0 this value was implicitly set to the opposite of :data:`depthClampEnable`, but with
  later extensions & versions it can be set independently.

:type: bool

"""
        pass

    @depthClipEnable.setter
    def depthClipEnable(self, value: bool):
        pass

    @property
    def extraPrimitiveOverestimationSize(self) -> float:
        """
The extra size in pixels to increase primitives by during conservative rasterization,
in the x and y directions in screen space.

See :data:`conservativeRasterizationMode`

:type: float

"""
        pass

    @extraPrimitiveOverestimationSize.setter
    def extraPrimitiveOverestimationSize(self, value: float):
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
    def lineStippleFactor(self) -> int:
        """
The line stipple factor, or 0 if line stipple is disabled.

:type: int

"""
        pass

    @lineStippleFactor.setter
    def lineStippleFactor(self, value: int):
        pass

    @property
    def lineStipplePattern(self) -> int:
        """
The line stipple bit-pattern.

:type: int

"""
        pass

    @lineStipplePattern.setter
    def lineStipplePattern(self, value: int):
        pass

    @property
    def lineWidth(self) -> float:
        """
The fixed line width in pixels.

:type: float

"""
        pass

    @lineWidth.setter
    def lineWidth(self, value: float):
        pass

    @property
    def pipelineShadingRate(self) -> Tuple[int,int]:
        """
The current pipeline fragment shading rate. This will always be 1x1 when a fragment
shading rate has not been specified.

:type: Tuple[int,int]

"""
        pass

    @pipelineShadingRate.setter
    def pipelineShadingRate(self, value: Tuple[int,int]):
        pass

    @property
    def provokingVertexFirst(self) -> bool:
        """
Whether the provoking vertex is the first one (default behaviour).

:type: bool

"""
        pass

    @provokingVertexFirst.setter
    def provokingVertexFirst(self, value: bool):
        pass

    @property
    def rasterizerDiscardEnable(self) -> bool:
        """
``True`` if primitives should be discarded during rasterization.

:type: bool

"""
        pass

    @rasterizerDiscardEnable.setter
    def rasterizerDiscardEnable(self, value: bool):
        pass

    @property
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner,ShadingRateCombiner]:
        """
The fragment shading rate combiners.

The combiners are applied as follows, according to the Vulkan spec:

  ``intermediateRate = combiner[0] ( pipelineShadingRate,  shaderExportedShadingRate )``
  ``finalRate        = combiner[1] ( intermediateRate,     imageBasedShadingRate     )``

Where the first input is from :data:`pipelineShadingRate` and the second is the exported shading
rate from the last pre-rasterization shader stage, which defaults to 1x1 if not exported.

The intermediate result is then used as the first input to the second combiner, together with the
shading rate sampled from the fragment shading rate attachment.

:type: Tuple[ShadingRateCombiner,ShadingRateCombiner]

"""
        pass

    @shadingRateCombiners.setter
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner,ShadingRateCombiner]):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B0B80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKRasterizer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKRasterizer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKRasterizer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKRasterizer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKRasterizer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKRasterizer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKRasterizer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKRasterizer' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.VKRasterizer' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.VKRasterizer' objects>, 'depthBiasClamp': <attribute 'depthBiasClamp' of 'renderdoc.VKRasterizer' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.VKRasterizer' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.VKRasterizer' objects>, 'lineStippleFactor': <attribute 'lineStippleFactor' of 'renderdoc.VKRasterizer' objects>, 'pipelineShadingRate': <attribute 'pipelineShadingRate' of 'renderdoc.VKRasterizer' objects>, 'lineStipplePattern': <attribute 'lineStipplePattern' of 'renderdoc.VKRasterizer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKRasterizer' objects>, 'provokingVertexFirst': <attribute 'provokingVertexFirst' of 'renderdoc.VKRasterizer' objects>, 'shadingRateCombiners': <attribute 'shadingRateCombiners' of 'renderdoc.VKRasterizer' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.VKRasterizer' objects>, 'extraPrimitiveOverestimationSize': <attribute 'extraPrimitiveOverestimationSize' of 'renderdoc.VKRasterizer' objects>, 'depthBiasEnable': <attribute 'depthBiasEnable' of 'renderdoc.VKRasterizer' objects>, 'lineRasterMode': <attribute 'lineRasterMode' of 'renderdoc.VKRasterizer' objects>, 'depthClampEnable': <attribute 'depthClampEnable' of 'renderdoc.VKRasterizer' objects>, 'depthClipEnable': <attribute 'depthClipEnable' of 'renderdoc.VKRasterizer' objects>, 'rasterizerDiscardEnable': <attribute 'rasterizerDiscardEnable' of 'renderdoc.VKRasterizer' objects>, 'lineWidth': <attribute 'lineWidth' of 'renderdoc.VKRasterizer' objects>, 'conservativeRasterization': <attribute 'conservativeRasterization' of 'renderdoc.VKRasterizer' objects>, '__doc__': 'Describes the rasterizer state in the pipeline.'})"


