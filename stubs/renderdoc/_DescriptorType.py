from enum import IntEnum

class DescriptorType(IntEnum):
    # Original docstring
    """
    The type of a descriptor.
    
    .. data:: Unknown
    
      An unknown or uninitialised type of descriptor.
    
    .. data:: ConstantBuffer
    
      A constant or uniform buffer.
    
    .. data:: Sampler
    
      A separate sampler object.
    
    .. data:: ImageSampler
    
      A combined image and sampler object.
    
    .. data:: Image
    
      An image that can only be sampled from.
    
    .. data:: Buffer
    
      A buffer that can only be read from, with data read literally in a shader via raw or structured
      access.
    
    .. data:: TypedBuffer
    
      A typed buffer that can only be read from, interpreting each element via a format decode.
    
    .. data:: ReadWriteImage
    
      An image that can be read from and written to arbitrarily.
    
    .. data:: ReadWriteTypedBuffer
    
      A typed/texture buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadWriteBuffer
    
      A buffer that can be read from and written to arbitrarily.
    
    .. data:: AccelerationStructure
    
      A ray-tracing acceleration structure, read-only in the shader.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown or uninitialised type of descriptor.
    """
    
    ConstantBuffer = 1
    """
    A constant or uniform buffer.
    """
    
    Sampler = 2
    """
    A separate sampler object.
    """
    
    ImageSampler = 3
    """
    A combined image and sampler object.
    """
    
    Image = 4
    """
    An image that can only be sampled from.
    """
    
    Buffer = 5
    """
    A buffer that can only be read from, with data read literally in a shader via raw or structured
    access.
    """
    
    TypedBuffer = 6
    """
    A typed buffer that can only be read from, interpreting each element via a format decode.
    """
    
    ReadWriteImage = 7
    """
    An image that can be read from and written to arbitrarily.
    """
    
    ReadWriteTypedBuffer = 8
    """
    A typed/texture buffer that can be read from and written to arbitrarily.
    """
    
    ReadWriteBuffer = 9
    """
    A buffer that can be read from and written to arbitrarily.
    """
    
    AccelerationStructure = 10
    """
    A ray-tracing acceleration structure, read-only in the shader.
    """
    

# Assign __doc__ for enum values for easier introspection

DescriptorType.Unknown.__doc__ = """
An unknown or uninitialised type of descriptor.
"""

DescriptorType.ConstantBuffer.__doc__ = """
A constant or uniform buffer.
"""

DescriptorType.Sampler.__doc__ = """
A separate sampler object.
"""

DescriptorType.ImageSampler.__doc__ = """
A combined image and sampler object.
"""

DescriptorType.Image.__doc__ = """
An image that can only be sampled from.
"""

DescriptorType.Buffer.__doc__ = """
A buffer that can only be read from, with data read literally in a shader via raw or structured
access.
"""

DescriptorType.TypedBuffer.__doc__ = """
A typed buffer that can only be read from, interpreting each element via a format decode.
"""

DescriptorType.ReadWriteImage.__doc__ = """
An image that can be read from and written to arbitrarily.
"""

DescriptorType.ReadWriteTypedBuffer.__doc__ = """
A typed/texture buffer that can be read from and written to arbitrarily.
"""

DescriptorType.ReadWriteBuffer.__doc__ = """
A buffer that can be read from and written to arbitrarily.
"""

DescriptorType.AccelerationStructure.__doc__ = """
A ray-tracing acceleration structure, read-only in the shader.
"""

