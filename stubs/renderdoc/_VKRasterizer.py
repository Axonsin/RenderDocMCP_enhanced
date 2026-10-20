from ._ConservativeRaster import ConservativeRaster
from ._CullMode import CullMode
from ._DepthBiasMode import DepthBiasMode
from ._FillMode import FillMode
from ._LineRaster import LineRaster
from ._ShadingRateCombiner import ShadingRateCombiner
from typing import Tuple

from typing import overload

class VKRasterizer():
    # Original docstring
    """
    Describes the rasterizer state in the pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKRasterizer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKRasterizer'):
        """
        Construct a new VKRasterizer with a deep copy of the input.
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
    def pipelineShadingRate(self) -> Tuple[int, int]:
        """
        The current pipeline fragment shading rate. This will always be 1x1 when a fragment
        shading rate has not been specified.
        
        :type: Tuple[int,int]
        """
        pass
    
    @pipelineShadingRate.setter
    def pipelineShadingRate(self, value: Tuple[int, int]):
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
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner, ShadingRateCombiner]:
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
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner, ShadingRateCombiner]):
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
    def extraPrimitiveOverestimationSize(self) -> float:
        """
        The extra size in pixels to increase primitives by during conservative rasterization,
        in the x and y directions in screen space.
        
        See :data:`conservativeRasterization`
        
        :type: float
        """
        pass
    
    @extraPrimitiveOverestimationSize.setter
    def extraPrimitiveOverestimationSize(self, value: float):
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
    def depthBiasExact(self) -> bool:
        """
        Whether the depth bias least representable value is calculated exactly.
        
        :type: bool
        """
        pass
    
    @depthBiasExact.setter
    def depthBiasExact(self, value: bool):
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
    def depthBiasRepresentation(self) -> DepthBiasMode:
        """
        The mode used for calculating the depth bias least representable value.
        
        :type: DepthBiasMode
        """
        pass
    
    @depthBiasRepresentation.setter
    def depthBiasRepresentation(self, value: DepthBiasMode):
        pass
    
