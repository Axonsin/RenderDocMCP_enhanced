from ._DescriptorCategory import DescriptorCategory

from typing import overload

class D3D12RootTableRange():
    # Original docstring
    """
    Contains the structure of a single range within a root table definition.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12RootTableRange.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12RootTableRange'):
        """
        Construct a new D3D12RootTableRange with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def count(self) -> int:
        """
        The number of registers in this range.
        
        :type: int
        """
        pass
    
    @count.setter
    def count(self, value: int):
        pass
    
    @property
    def appended(self) -> bool:
        """
        Whether or not this table was appended after the previous, leading to an auto-calculated
        offset in :data:`tableByteOffset`.
        
        :type: bool
        """
        pass
    
    @appended.setter
    def appended(self, value: bool):
        pass
    
    @property
    def tableByteOffset(self) -> int:
        """
        The offset in bytes from the start of the table as defined in :class:`D3D12RootParam`.
        
        :type: int
        """
        pass
    
    @tableByteOffset.setter
    def tableByteOffset(self, value: int):
        pass
    
    @property
    def space(self) -> int:
        """
        The register space of this range.
        
        :type: int
        """
        pass
    
    @space.setter
    def space(self, value: int):
        pass
    
    @property
    def baseRegister(self) -> int:
        """
        The first register in this range.
        
        :type: int
        """
        pass
    
    @baseRegister.setter
    def baseRegister(self, value: int):
        pass
    
    @property
    def category(self) -> DescriptorCategory:
        """
        The descriptor category specified in this range.
        
        :type: DescriptorCategory
        """
        pass
    
    @category.setter
    def category(self, value: DescriptorCategory):
        pass
    
