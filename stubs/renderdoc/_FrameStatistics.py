from ._BlendStats import BlendStats
from ._ConstantBindStats import ConstantBindStats
from ._DepthStencilStats import DepthStencilStats
from ._DispatchStats import DispatchStats
from ._DrawcallStats import DrawcallStats
from ._IndexBindStats import IndexBindStats
from ._LayoutBindStats import LayoutBindStats
from ._OutputTargetStats import OutputTargetStats
from ._RasterizationStats import RasterizationStats
from ._ResourceBindStats import ResourceBindStats
from ._ResourceUpdateStats import ResourceUpdateStats
from ._SamplerBindStats import SamplerBindStats
from ._ShaderChangeStats import ShaderChangeStats
from ._VertexBindStats import VertexBindStats
from typing import List

from typing import overload

class FrameStatistics():
    # Original docstring
    """
    Contains all the available statistics about the captured frame.
    
    Currently this information is only available on D3D11 and is fairly API-centric.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised FrameStatistics.
        """
        pass
    
    @overload
    def __init__(self, other: 'FrameStatistics'):
        """
        Construct a new FrameStatistics with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def blends(self) -> BlendStats:
        """
        Information about blend state binds.
        
        :type: BlendStats
        """
        pass
    
    @blends.setter
    def blends(self, value: BlendStats):
        pass
    
    @property
    def draws(self) -> DrawcallStats:
        """
        Information about drawcalls.
        
        :type: DrawcallStats
        """
        pass
    
    @draws.setter
    def draws(self, value: DrawcallStats):
        pass
    
    @property
    def vertices(self) -> VertexBindStats:
        """
        Information about vertex buffer binds.
        
        :type: VertexBindStats
        """
        pass
    
    @vertices.setter
    def vertices(self, value: VertexBindStats):
        pass
    
    @property
    def layouts(self) -> LayoutBindStats:
        """
        Information about vertex layout binds.
        
        :type: LayoutBindStats
        """
        pass
    
    @layouts.setter
    def layouts(self, value: LayoutBindStats):
        pass
    
    @property
    def samplers(self) -> List[SamplerBindStats]:
        """
        A list of sampler bind statistics, one per each :class:`stage <ShaderStage>`.
        
        :type: List[SamplerBindStats]
        """
        pass
    
    @samplers.setter
    def samplers(self, value: List[SamplerBindStats]):
        pass
    
    @property
    def shaders(self) -> List[ShaderChangeStats]:
        """
        A list of shader bind statistics, one per each :class:`stage <ShaderStage>`.
        
        :type: List[ShaderChangeStats]
        """
        pass
    
    @shaders.setter
    def shaders(self, value: List[ShaderChangeStats]):
        pass
    
    @property
    def resources(self) -> List[ResourceBindStats]:
        """
        A list of resource bind statistics, one per each :class:`stage <ShaderStage>`.
        
        :type: List[ResourceBindStats]
        """
        pass
    
    @resources.setter
    def resources(self, value: List[ResourceBindStats]):
        pass
    
    @property
    def depths(self) -> DepthStencilStats:
        """
        Information about depth-stencil state binds.
        
        :type: DepthStencilStats
        """
        pass
    
    @depths.setter
    def depths(self, value: DepthStencilStats):
        pass
    
    @property
    def constants(self) -> List[ConstantBindStats]:
        """
        A list of constant buffer bind statistics, one per each :class:`stage <ShaderStage>`.
        
        :type: List[ConstantBindStats]
        """
        pass
    
    @constants.setter
    def constants(self, value: List[ConstantBindStats]):
        pass
    
    @property
    def updates(self) -> ResourceUpdateStats:
        """
        Information about resource contents updates.
        
        :type: ResourceUpdateStats
        """
        pass
    
    @updates.setter
    def updates(self, value: ResourceUpdateStats):
        pass
    
    @property
    def indices(self) -> IndexBindStats:
        """
        Information about index buffer binds.
        
        :type: IndexBindStats
        """
        pass
    
    @indices.setter
    def indices(self, value: IndexBindStats):
        pass
    
    @property
    def outputs(self) -> OutputTargetStats:
        """
        Information about output merger and UAV binds.
        
        :type: OutputTargetStats
        """
        pass
    
    @outputs.setter
    def outputs(self, value: OutputTargetStats):
        pass
    
    @property
    def rasters(self) -> RasterizationStats:
        """
        Information about rasterizer state binds.
        
        :type: RasterizationStats
        """
        pass
    
    @rasters.setter
    def rasters(self, value: RasterizationStats):
        pass
    
    @property
    def recorded(self) -> bool:
        """
        ``True`` if the statistics in this structure are valid.
        
        :type: bool
        """
        pass
    
    @recorded.setter
    def recorded(self, value: bool):
        pass
    
    @property
    def dispatches(self) -> DispatchStats:
        """
        Information about compute dispatches.
        
        :type: DispatchStats
        """
        pass
    
    @dispatches.setter
    def dispatches(self, value: DispatchStats):
        pass
    
