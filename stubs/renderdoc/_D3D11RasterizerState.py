from ._ConservativeRaster import ConservativeRaster
from ._CullMode import CullMode
from ._FillMode import FillMode
from ._ResourceId import ResourceId

from typing import overload

class D3D11RasterizerState():
    # Original docstring
    """
    Describes a rasterizer state object.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11RasterizerState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11RasterizerState'):
        """
        Construct a new D3D11RasterizerState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def conservativeRasterization(self) -> ConservativeRaster:
        """
        The current :class:`ConservativeRaster` mode.
        
        :type: ConservativeRaster
        """
        pass
    
    @conservativeRasterization.setter
    def conservativeRasterization(self, value: ConservativeRaster):
        pass
    
