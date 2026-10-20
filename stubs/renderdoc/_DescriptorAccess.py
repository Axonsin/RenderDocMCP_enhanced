from ._DescriptorType import DescriptorType
from ._ResourceId import ResourceId
from ._ShaderStage import ShaderStage

from typing import overload

class DescriptorAccess():
    # Original docstring
    """
    The details of a single accessed descriptor as fetched by a shader and which descriptor
    in the descriptor store was fetched.
    
    This may be a somewhat conservative access, reported as possible but not actually executed on the
    GPU itself.
    
    .. data:: NoShaderBinding
    
      No shader binding corresponds to this descriptor access, it happened directly without going
      through any kind of binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DescriptorAccess.
        """
        pass
    
    @overload
    def __init__(self, other: 'DescriptorAccess'):
        """
        Construct a new DescriptorAccess with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoShaderBinding = 65535
    """
    No shader binding corresponds to this descriptor access, it happened directly without going
    through any kind of binding.
    """
    
    @property
    def stage(self) -> ShaderStage:
        """
        The shader stage that this descriptor access came from.
        
        :type: ShaderStage
        """
        pass
    
    @stage.setter
    def stage(self, value: ShaderStage):
        pass
    
    @property
    def descriptorStore(self) -> ResourceId:
        """
        The backing storage of the descriptor.
        
        :type: ResourceId
        """
        pass
    
    @descriptorStore.setter
    def descriptorStore(self, value: ResourceId):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The offset in bytes to the descriptor in the descriptor store.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def type(self) -> DescriptorType:
        """
        The type of the descriptor being accessed.
        
        :type: DescriptorType
        """
        pass
    
    @type.setter
    def type(self, value: DescriptorType):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size in bytes of the descriptor.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
    @property
    def index(self) -> int:
        """
        The index within the shader's reflection list corresponding to :data:`type` of the
        accessing resource.
        
        If this value is set to :data:`NoShaderBinding` then the shader synthesised a direct access into
        descriptor storage without passing through a declared binding.
        
        :type: int
        """
        pass
    
    @index.setter
    def index(self, value: int):
        pass
    
    @property
    def staticallyUnused(self) -> bool:
        """
        For informational purposes, some descriptors that are declared in the shader
        interface but are provably unused may still be reported as descriptor accesses. This flag will be
        set to ``True`` to indicate that the descriptor was definitely not used.
        
        This flag only states that a descriptor is definitely unused on all paths. If set to ``False`` this
        does not necessarily guarantee that the descriptor was accessed on the GPU during execution.
        
        :type: bool
        """
        pass
    
    @staticallyUnused.setter
    def staticallyUnused(self, value: bool):
        pass
    
    @property
    def arrayElement(self) -> int:
        """
        For an arrayed resource declared in a shader, the array element used.
        
        :type: int
        """
        pass
    
    @arrayElement.setter
    def arrayElement(self, value: int):
        pass
    
