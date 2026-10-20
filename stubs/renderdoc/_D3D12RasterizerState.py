from ._ConservativeRaster import ConservativeRaster
from ._CullMode import CullMode
from ._FillMode import FillMode
from ._LineRaster import LineRaster
from ._ResourceId import ResourceId
from ._ShadingRateCombiner import ShadingRateCombiner
from typing import Tuple

from typing import overload

class D3D12RasterizerState():
    # Original docstring
    """
    Describes the rasterizer state in the PSO.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12RasterizerState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12RasterizerState'):
        """
        Construct a new D3D12RasterizerState with a deep copy of the input.
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
    def baseShadingRate(self) -> Tuple[int, int]:
        """
        The current base variable shading rate. This will always be 1x1 when variable shading
        is disabled.
        
        :type: Tuple[int,int]
        """
        pass
    
    @baseShadingRate.setter
    def baseShadingRate(self, value: Tuple[int, int]):
        pass
    
    @property
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner, ShadingRateCombiner]:
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
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner, ShadingRateCombiner]):
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
    def conservativeRasterization(self) -> ConservativeRaster:
        """
        The current :class:`ConservativeRaster` mode.
        
        :type: ConservativeRaster
        """
        pass
    
    @conservativeRasterization.setter
    def conservativeRasterization(self, value: ConservativeRaster):
        pass
    
