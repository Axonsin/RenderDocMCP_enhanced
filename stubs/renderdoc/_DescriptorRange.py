from ._DescriptorAccess import DescriptorAccess
from ._DescriptorType import DescriptorType

from typing import overload

class DescriptorRange():
    # Original docstring
    """
    A range of sized descriptors.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DescriptorRange.
        """
        pass
    
    @overload
    def __init__(self, other: 'DescriptorRange'):
        """
        Construct a new DescriptorRange with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, access: DescriptorAccess):
        """
        Construct a new DescriptorRange using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def descriptorSize(self) -> int:
        """
        The size of each descriptor in the range.
        
        :type: int
        """
        pass
    
    @descriptorSize.setter
    def descriptorSize(self, value: int):
        pass
    
    @property
    def count(self) -> int:
        """
        The number of descriptors in this range.
        
        :type: int
        """
        pass
    
    @count.setter
    def count(self, value: int):
        pass
    
    @property
    def offset(self) -> int:
        """
        The offset in the descriptor storage where the descriptor range starts.
        
        :type: int
        """
        pass
    
    @offset.setter
    def offset(self, value: int):
        pass
    
    @property
    def type(self) -> DescriptorType:
        """
        The type of descriptor in the descriptor range.
        
        :type: DescriptorType
        """
        pass
    
    @type.setter
    def type(self, value: DescriptorType):
        pass
    
