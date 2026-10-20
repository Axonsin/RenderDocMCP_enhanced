from ._DescriptorType import DescriptorType
from ._ShaderConstantType import ShaderConstantType
from ._TextureType import TextureType

from typing import overload

class ShaderResource():
    # Original docstring
    """
    Contains the information for a shader resource that is made accessible to shaders
    directly by means of the API resource binding system.
    
    .. note:: that constant blocks and samplers will not have a shader resource entry, see
      :class:`ConstantBlock` and :class:`ShaderSampler`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderResource.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderResource'):
        """
        Construct a new ShaderResource with a deep copy of the input.
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
        The name of this resource.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def hasSampler(self) -> bool:
        """
        ``True`` if this texture resource has a sampler as well.
        
        :type: bool
        """
        pass
    
    @hasSampler.setter
    def hasSampler(self, value: bool):
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
    def isReadOnly(self) -> bool:
        """
        ``True`` if this resource is available to the shader for reading only, otherwise it is
        able to be read from and written to arbitrarily.
        
        :type: bool
        """
        pass
    
    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        pass
    
    @property
    def descriptorType(self) -> DescriptorType:
        """
        The :class:`DescriptorType` which this resource expects to access.
        
        :type: DescriptorType
        """
        pass
    
    @descriptorType.setter
    def descriptorType(self, value: DescriptorType):
        pass
    
    @property
    def isInputAttachment(self) -> bool:
        """
        ``True`` if this texture resource is a subpass input attachment.
        
        :type: bool
        """
        pass
    
    @isInputAttachment.setter
    def isInputAttachment(self, value: bool):
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
    
    @property
    def isTexture(self) -> bool:
        """
        ``True`` if this resource is a texture, otherwise it is a buffer.
        
        :type: bool
        """
        pass
    
    @isTexture.setter
    def isTexture(self, value: bool):
        pass
    
    @property
    def textureType(self) -> TextureType:
        """
        The :class:`TextureType` that describes the type of this resource.
        
        :type: TextureType
        """
        pass
    
    @textureType.setter
    def textureType(self, value: TextureType):
        pass
    
    @property
    def variableType(self) -> ShaderConstantType:
        """
        The type of each element of this resource.
        
        :type: ShaderConstantType
        """
        pass
    
    @variableType.setter
    def variableType(self, value: ShaderConstantType):
        pass
    
