
from typing import overload

class ShaderSampler():
    # Original docstring
    """
    Contains the information for a separate sampler in a shader. If the API doesn't have
    the concept of separate samplers, this struct will be unused and only :class:`ShaderResource` is
    relevant.
    
    .. note:: that constant blocks will not have a shader resource entry, see :class:`ConstantBlock`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderSampler.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderSampler'):
        """
        Construct a new ShaderSampler with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def bindArraySize(self) -> int:
        """
        If this binding is natively arrayed, how large is the array size. If not arrayed, this
        will be set to 1.
        
        This value may be set to a very large number if the array is unbounded in the shader.
        
        :type: int
        """
        pass
    
    @bindArraySize.setter
    def bindArraySize(self, value: int):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of this sampler.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def fixedBindNumber(self) -> int:
        """
        The fixed binding number for this binding. The interpretation of this is API-specific
        and it is provided purely for informational purposes and has no bearing on how data is accessed or
        described. Similarly some bindings don't have a fixed bind number and the value here should not be
        relied on.
        
        For OpenGL only, this value is not used as bindings are dynamic and cannot be determined by the
        shader reflection. Bindings must be determined only by the descriptor mapped to.
        
        Generally speaking sorting by this number will give a reasonable ordering by binding if it exists.
        
        .. note::
          Because this number is API-specific, there is no guarantee that it will be unique across all
          resources, though generally it will be unique within all binds of the same type. It should be used
          only within contexts that can interpret it API-specifically, or else for purely
          informational/non-semantic purposes like sorting.
        
        :type: int
        """
        pass
    
    @fixedBindNumber.setter
    def fixedBindNumber(self, value: int):
        pass
    
    @property
    def fixedBindSetOrSpace(self) -> int:
        """
        The fixed binding set or space for this binding. This is API-specific, on Vulkan this
        gives the set and on D3D12 this gives the register space.
        It is provided purely for informational purposes and has no bearing on how data is accessed or
        described.
        
        Generally speaking sorting by this number before :data:`fixedBindNumber` will give a reasonable
        ordering by binding if it exists.
        
        :type: int
        """
        pass
    
    @fixedBindSetOrSpace.setter
    def fixedBindSetOrSpace(self, value: int):
        pass
    
