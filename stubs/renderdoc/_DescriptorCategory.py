from enum import IntEnum

class DescriptorCategory(IntEnum):
    # Original docstring
    """
    The category of a descriptor, corresponding to the interfaces in :class:`ShaderReflection`.
    
    .. data:: Unknown
    
      An unknown or uninitialised type of descriptor.
    
    .. data:: ConstantBlock
    
      A constant block.
    
    .. data:: Sampler
    
      A sampler object.
    
    .. data:: ReadOnlyResource
    
      A read-only resource.
    
    .. data:: ReadWriteResource
    
      A read-write resource.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown or uninitialised type of descriptor.
    """
    
    ConstantBlock = 1
    """
    A constant block.
    """
    
    Sampler = 2
    """
    A sampler object.
    """
    
    ReadOnlyResource = 3
    """
    A read-only resource.
    """
    
    ReadWriteResource = 4
    """
    A read-write resource.
    """
    

# Assign __doc__ for enum values for easier introspection

DescriptorCategory.Unknown.__doc__ = """
An unknown or uninitialised type of descriptor.
"""

DescriptorCategory.ConstantBlock.__doc__ = """
A constant block.
"""

DescriptorCategory.Sampler.__doc__ = """
A sampler object.
"""

DescriptorCategory.ReadOnlyResource.__doc__ = """
A read-only resource.
"""

DescriptorCategory.ReadWriteResource.__doc__ = """
A read-write resource.
"""

