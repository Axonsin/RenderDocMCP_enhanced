from ._CullMode import CullMode
from ._FillMode import FillMode

from typing import overload

class GLRasterizerState():
    # Original docstring
    """
    Describes the rasterizer state toggles.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLRasterizerState.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLRasterizerState'):
        """
        Construct a new GLRasterizerState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def slopeScaledDepthBias(self) -> float:
        """
        The slope-scaled depth bias value to apply to z-values.
        
        :type: float
        """
        pass
    
    @slopeScaledDepthBias.setter
    def slopeScaledDepthBias(self, value: float):
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
    def pointFadeThreshold(self) -> float:
        """
        The threshold value at which points are clipped if they exceed this size.
        
        :type: float
        """
        pass
    
    @pointFadeThreshold.setter
    def pointFadeThreshold(self, value: float):
        pass
    
