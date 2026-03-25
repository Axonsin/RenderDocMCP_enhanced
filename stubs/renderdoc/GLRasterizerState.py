# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CullMode import CullMode
from .FillMode import FillMode

class GLRasterizerState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state toggles. """
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
    def alphaToOne(self) -> bool:
        """
``True`` if alpha-to-one should be used when blending to an MSAA target.

:type: bool

"""
        pass

    @alphaToOne.setter
    def alphaToOne(self, value: bool):
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
    def depthClamp(self) -> bool:
        """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0`` and not clipped.

:type: bool

"""
        pass

    @depthClamp.setter
    def depthClamp(self, value: bool):
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
    def minSampleShadingRate(self) -> float:
        """
The minimum sample shading rate.

:type: float

"""
        pass

    @minSampleShadingRate.setter
    def minSampleShadingRate(self, value: float):
        pass

    @property
    def multisampleEnable(self) -> bool:
        """
``True`` if multisampling should be used during rendering.

:type: bool

"""
        pass

    @multisampleEnable.setter
    def multisampleEnable(self, value: bool):
        pass

    @property
    def offsetClamp(self) -> float:
        """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

:type: float

"""
        pass

    @offsetClamp.setter
    def offsetClamp(self, value: float):
        pass

    @property
    def pointFadeThreshold(self) -> float:
        """
The threshold value at which points are clipped if they exceed this size.

:type: float

"""
        pass

    @pointFadeThreshold.setter
    def pointFadeThreshold(self, value: float):
        pass

    @property
    def pointOriginUpperLeft(self) -> bool:
        """
``True`` if the point sprite texture origin is upper-left. ``False`` if lower-left.

:type: bool

"""
        pass

    @pointOriginUpperLeft.setter
    def pointOriginUpperLeft(self, value: bool):
        pass

    @property
    def pointSize(self) -> float:
        """
The fixed point size in pixels.

:type: float

"""
        pass

    @pointSize.setter
    def pointSize(self, value: float):
        pass

    @property
    def programmablePointSize(self) -> bool:
        """
``True`` if the point size can be programmably exported from a shader.

:type: bool

"""
        pass

    @programmablePointSize.setter
    def programmablePointSize(self, value: bool):
        pass

    @property
    def sampleCoverage(self) -> bool:
        """
``True`` if a temporary mask using :data:`sampleCoverageValue` should be used to
resolve the final output color.

:type: bool

"""
        pass

    @sampleCoverage.setter
    def sampleCoverage(self, value: bool):
        pass

    @property
    def sampleCoverageInvert(self) -> bool:
        """
``True`` if the temporary sample coverage mask should be inverted.

:type: bool

"""
        pass

    @sampleCoverageInvert.setter
    def sampleCoverageInvert(self, value: bool):
        pass

    @property
    def sampleCoverageValue(self) -> float:
        """
The sample coverage value used if :data:`sampleCoverage` is ``True``.

:type: float

"""
        pass

    @sampleCoverageValue.setter
    def sampleCoverageValue(self, value: float):
        pass

    @property
    def sampleMask(self) -> bool:
        """
``True`` if the generated samples should be bitwise ``AND`` masked with
:data:`sampleMaskValue`.

:type: bool

"""
        pass

    @sampleMask.setter
    def sampleMask(self, value: bool):
        pass

    @property
    def sampleMaskValue(self) -> int:
        """
The sample mask value that should be masked against the generated coverage.

:type: int

"""
        pass

    @sampleMaskValue.setter
    def sampleMaskValue(self, value: int):
        pass

    @property
    def sampleShading(self) -> bool:
        """
``True`` if rendering should happen at sample-rate frequency.

:type: bool

"""
        pass

    @sampleShading.setter
    def sampleShading(self, value: bool):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551A7BE0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLRasterizerState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLRasterizerState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLRasterizerState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLRasterizerState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLRasterizerState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLRasterizerState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLRasterizerState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLRasterizerState' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.GLRasterizerState' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.GLRasterizerState' objects>, 'sampleShading': <attribute 'sampleShading' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverageInvert': <attribute 'sampleCoverageInvert' of 'renderdoc.GLRasterizerState' objects>, 'programmablePointSize': <attribute 'programmablePointSize' of 'renderdoc.GLRasterizerState' objects>, 'pointSize': <attribute 'pointSize' of 'renderdoc.GLRasterizerState' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.GLRasterizerState' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.GLRasterizerState' objects>, 'minSampleShadingRate': <attribute 'minSampleShadingRate' of 'renderdoc.GLRasterizerState' objects>, 'offsetClamp': <attribute 'offsetClamp' of 'renderdoc.GLRasterizerState' objects>, 'sampleMaskValue': <attribute 'sampleMaskValue' of 'renderdoc.GLRasterizerState' objects>, 'alphaToOne': <attribute 'alphaToOne' of 'renderdoc.GLRasterizerState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLRasterizerState' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverageValue': <attribute 'sampleCoverageValue' of 'renderdoc.GLRasterizerState' objects>, 'pointOriginUpperLeft': <attribute 'pointOriginUpperLeft' of 'renderdoc.GLRasterizerState' objects>, 'depthClamp': <attribute 'depthClamp' of 'renderdoc.GLRasterizerState' objects>, 'multisampleEnable': <attribute 'multisampleEnable' of 'renderdoc.GLRasterizerState' objects>, 'sampleMask': <attribute 'sampleMask' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverage': <attribute 'sampleCoverage' of 'renderdoc.GLRasterizerState' objects>, 'alphaToCoverage': <attribute 'alphaToCoverage' of 'renderdoc.GLRasterizerState' objects>, 'lineWidth': <attribute 'lineWidth' of 'renderdoc.GLRasterizerState' objects>, 'pointFadeThreshold': <attribute 'pointFadeThreshold' of 'renderdoc.GLRasterizerState' objects>, '__doc__': 'Describes the rasterizer state toggles.'})"


