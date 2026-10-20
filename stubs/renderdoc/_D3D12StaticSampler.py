from ._SamplerDescriptor import SamplerDescriptor
from ._ShaderStageMask import ShaderStageMask

from typing import overload

class D3D12StaticSampler():
    # Original docstring
    """
    Contains the details of a single static sampler in a root signature.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12StaticSampler.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12StaticSampler'):
        """
        Construct a new D3D12StaticSampler with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def reg(self) -> int:
        """
        The register number of this sampler.
        
        :type: int
        """
        pass
    
    @reg.setter
    def reg(self, value: int):
        pass
    
    @property
    def descriptor(self) -> SamplerDescriptor:
        """
        The details of the sampler descriptor itself.
        
        :type: SamplerDescriptor
        """
        pass
    
    @descriptor.setter
    def descriptor(self, value: SamplerDescriptor):
        pass
    
    @property
    def visibility(self) -> ShaderStageMask:
        """
        The shader stage that can access this sampler.
        
        :type: ShaderStageMask
        """
        pass
    
    @visibility.setter
    def visibility(self, value: ShaderStageMask):
        pass
    
    @property
    def space(self) -> int:
        """
        The register space of this sampler.
        
        :type: int
        """
        pass
    
    @space.setter
    def space(self, value: int):
        pass
    
