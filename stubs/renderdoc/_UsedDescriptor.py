from ._Descriptor import Descriptor
from ._DescriptorAccess import DescriptorAccess
from ._SamplerDescriptor import SamplerDescriptor

from typing import overload

class UsedDescriptor():
    # Original docstring
    """
    Combined information about a single descriptor that has been used, both the information
    about its access and its contents.
    
    This is a helper struct for the common pipeline state abstraction to trade off simplicity of access
    against optimal access.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised UsedDescriptor.
        """
        pass
    
    @overload
    def __init__(self, other: 'UsedDescriptor'):
        """
        Construct a new UsedDescriptor with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def descriptor(self) -> Descriptor:
        """
        The contents of the accessed descriptor, if it is a normal non-sampler descriptor.
        
        For sampler descriptors this is empty.
        
        :type: Descriptor
        """
        pass
    
    @descriptor.setter
    def descriptor(self, value: Descriptor):
        pass
    
    @property
    def sampler(self) -> SamplerDescriptor:
        """
        The contents of the accessed descriptor, if it is a sampler descriptor.
        
        For normal descriptors this is empty.
        
        :type: SamplerDescriptor
        """
        pass
    
    @sampler.setter
    def sampler(self, value: SamplerDescriptor):
        pass
    
    @property
    def access(self) -> DescriptorAccess:
        """
        The access information of which shader reflection object accessed which descriptor.
        
        :type: DescriptorAccess
        """
        pass
    
    @access.setter
    def access(self, value: DescriptorAccess):
        pass
    
