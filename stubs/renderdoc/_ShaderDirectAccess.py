from ._DescriptorCategory import DescriptorCategory
from ._DescriptorType import DescriptorType
from ._ResourceId import ResourceId

from typing import overload

class ShaderDirectAccess():
    # Original docstring
    """
    References a particular resource accessed via the shader using direct heap access (as opposed to a direct binding).
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderDirectAccess.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderDirectAccess'):
        """
        Construct a new ShaderDirectAccess with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, category: DescriptorCategory, index: int):
        """
        Construct a new ShaderDirectAccess using provided values.
        """
        pass
    
    @overload
    def __init__(self, type: DescriptorType, descriptorStore: ResourceId, byteOffset: int, byteSize: int):
        """
        Construct a new ShaderDirectAccess using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
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
        The type of the resource being accessed.
        
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
    
