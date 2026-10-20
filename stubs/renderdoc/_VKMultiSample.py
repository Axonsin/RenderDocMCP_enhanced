from ._VKSampleLocations import VKSampleLocations

from typing import overload

class VKMultiSample():
    # Original docstring
    """
    Describes the multisampling state in the pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKMultiSample.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKMultiSample'):
        """
        Construct a new VKMultiSample with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def minSampleShading(self) -> float:
        """
        The minimum sample shading rate.
        
        :type: float
        """
        pass
    
    @minSampleShading.setter
    def minSampleShading(self, value: float):
        pass
    
    @property
    def rasterSamples(self) -> int:
        """
        How many samples to use when rasterizing.
        
        :type: int
        """
        pass
    
    @rasterSamples.setter
    def rasterSamples(self, value: int):
        pass
    
    @property
    def sampleShadingEnable(self) -> bool:
        """
        ``True`` if rendering should happen at sample-rate frequency.
        
        :type: bool
        """
        pass
    
    @sampleShadingEnable.setter
    def sampleShadingEnable(self, value: bool):
        pass
    
    @property
    def sampleMask(self) -> int:
        """
        A mask that generated samples should be masked with using bitwise ``AND``.
        
        :type: int
        """
        pass
    
    @sampleMask.setter
    def sampleMask(self, value: int):
        pass
    
    @property
    def sampleLocations(self) -> VKSampleLocations:
        """
        The custom sample locations configuration.
        
        :type: VKSampleLocations
        """
        pass
    
    @sampleLocations.setter
    def sampleLocations(self, value: VKSampleLocations):
        pass
    
