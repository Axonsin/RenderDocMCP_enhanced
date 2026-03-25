# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .BlendStats import BlendStats
from .ConstantBindStats import ConstantBindStats
from .DepthStencilStats import DepthStencilStats
from .DispatchStats import DispatchStats
from .DrawcallStats import DrawcallStats
from .IndexBindStats import IndexBindStats
from .LayoutBindStats import LayoutBindStats
from .OutputTargetStats import OutputTargetStats
from .RasterizationStats import RasterizationStats
from .ResourceBindStats import ResourceBindStats
from .SamplerBindStats import SamplerBindStats
from .ShaderChangeStats import ShaderChangeStats
from .ResourceUpdateStats import ResourceUpdateStats
from .VertexBindStats import VertexBindStats

class FrameStatistics(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains all the available statistics about the captured frame.
    
    Currently this information is only available on D3D11 and is fairly API-centric.
    """
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
    def dispatches(self) -> DispatchStats:
        """
Information about compute dispatches.

:type: DispatchStats

"""
        pass

    @dispatches.setter
    def dispatches(self, value: DispatchStats):
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    def vertices(self) -> VertexBindStats:
        """
Information about vertex buffer binds.

:type: VertexBindStats

"""
        pass

    @vertices.setter
    def vertices(self, value: VertexBindStats):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C8AC0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.FrameStatistics' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.FrameStatistics' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.FrameStatistics' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.FrameStatistics' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.FrameStatistics' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.FrameStatistics' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.FrameStatistics' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.FrameStatistics' objects>, 'blends': <attribute 'blends' of 'renderdoc.FrameStatistics' objects>, 'draws': <attribute 'draws' of 'renderdoc.FrameStatistics' objects>, 'vertices': <attribute 'vertices' of 'renderdoc.FrameStatistics' objects>, 'layouts': <attribute 'layouts' of 'renderdoc.FrameStatistics' objects>, 'samplers': <attribute 'samplers' of 'renderdoc.FrameStatistics' objects>, 'shaders': <attribute 'shaders' of 'renderdoc.FrameStatistics' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.FrameStatistics' objects>, 'resources': <attribute 'resources' of 'renderdoc.FrameStatistics' objects>, 'depths': <attribute 'depths' of 'renderdoc.FrameStatistics' objects>, 'constants': <attribute 'constants' of 'renderdoc.FrameStatistics' objects>, 'updates': <attribute 'updates' of 'renderdoc.FrameStatistics' objects>, 'indices': <attribute 'indices' of 'renderdoc.FrameStatistics' objects>, 'outputs': <attribute 'outputs' of 'renderdoc.FrameStatistics' objects>, 'rasters': <attribute 'rasters' of 'renderdoc.FrameStatistics' objects>, 'recorded': <attribute 'recorded' of 'renderdoc.FrameStatistics' objects>, 'dispatches': <attribute 'dispatches' of 'renderdoc.FrameStatistics' objects>, '__doc__': '\\nContains all the available statistics about the captured frame.\\n\\nCurrently this information is only available on D3D11 and is fairly API-centric.\\n\\n'})"


