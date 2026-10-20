from ._ShaderConstant import ShaderConstant
from typing import List

from typing import overload

class ConstantBlock():
    # Original docstring
    """
    Contains the information for a block of constant values. The values are not present,
    only the metadata about how the variables are stored in memory itself and their type/name
    information.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ConstantBlock.
        """
        pass
    
    @overload
    def __init__(self, other: 'ConstantBlock'):
        """
        Construct a new ConstantBlock with a deep copy of the input.
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
    def bufferBacked(self) -> bool:
        """
        ``True`` if the contents are stored in a buffer of memory. If not then they are set by
        some other API-specific method, such as direct function calls or they may be compile-time
        specialisation constants.
        
        :type: bool
        """
        pass
    
    @bufferBacked.setter
    def bufferBacked(self, value: bool):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of this constant block, may be empty on some APIs.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def inlineDataBytes(self) -> bool:
        """
        ``True`` if this is backed by in-line data bytes rather than a specific buffer.
        
        :type: bool
        """
        pass
    
    @inlineDataBytes.setter
    def inlineDataBytes(self, value: bool):
        pass
    
    @property
    def variables(self) -> List[ShaderConstant]:
        """
        The constants contained within this block.
        
        :type: List[ShaderConstant]
        """
        pass
    
    @variables.setter
    def variables(self, value: List[ShaderConstant]):
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
    def compileConstants(self) -> bool:
        """
        ``True`` if this is a virtual buffer listing compile-time specialisation constants.
        
        :type: bool
        """
        pass
    
    @compileConstants.setter
    def compileConstants(self, value: bool):
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
    def byteSize(self) -> int:
        """
        The total number of bytes consumed by all of the constants contained in this block.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
