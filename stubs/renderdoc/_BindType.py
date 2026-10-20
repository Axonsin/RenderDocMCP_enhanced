from enum import IntEnum

class BindType(IntEnum):
    # Original docstring
    """
    The type of a shader resource bind.
    
    .. data:: Unknown
    
      An unknown type of binding.
    
    .. data:: ConstantBuffer
    
      A constant or uniform buffer.
    
    .. data:: Sampler
    
      A separate sampler object.
    
    .. data:: ImageSampler
    
      A combined image and sampler object.
    
    .. data:: ReadOnlyImage
    
      An image that can only be sampled from.
    
    .. data:: ReadWriteImage
    
      An image that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyTBuffer
    
      A texture buffer that can only be read from.
    
    .. data:: ReadWriteTBuffer
    
      A texture buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyBuffer
    
      A buffer that can only be read from, distinct from :data:`ConstantBuffer`.
    
    .. data:: ReadWriteBuffer
    
      A buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyResource
    
      A resource that can only be read from
    
    .. data:: ReadWriteResource
    
      A resource that can be read from and written to arbitrarily.
    
    .. data:: InputAttachment
    
      An input attachment for reading from the target currently being written.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown type of binding.
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
    
    ReadOnlyImage = 4
    """
    An image that can only be sampled from.
    """
    
    ReadWriteImage = 5
    """
    An image that can be read from and written to arbitrarily.
    """
    
    ReadOnlyTBuffer = 6
    """
    A texture buffer that can only be read from.
    """
    
    ReadWriteTBuffer = 7
    """
    A texture buffer that can be read from and written to arbitrarily.
    """
    
    ReadOnlyBuffer = 8
    """
    A buffer that can only be read from, distinct from :data:`ConstantBuffer`.
    """
    
    ReadWriteBuffer = 9
    """
    A buffer that can be read from and written to arbitrarily.
    """
    
    ReadOnlyResource = 10
    """
    A resource that can only be read from
    """
    
    ReadWriteResource = 11
    """
    A resource that can be read from and written to arbitrarily.
    """
    
    InputAttachment = 12
    """
    An input attachment for reading from the target currently being written.
    """
    

# Assign __doc__ for enum values for easier introspection

BindType.Unknown.__doc__ = """
An unknown type of binding.
"""

BindType.ConstantBuffer.__doc__ = """
A constant or uniform buffer.
"""

BindType.Sampler.__doc__ = """
A separate sampler object.
"""

BindType.ImageSampler.__doc__ = """
A combined image and sampler object.
"""

BindType.ReadOnlyImage.__doc__ = """
An image that can only be sampled from.
"""

BindType.ReadWriteImage.__doc__ = """
An image that can be read from and written to arbitrarily.
"""

BindType.ReadOnlyTBuffer.__doc__ = """
A texture buffer that can only be read from.
"""

BindType.ReadWriteTBuffer.__doc__ = """
A texture buffer that can be read from and written to arbitrarily.
"""

BindType.ReadOnlyBuffer.__doc__ = """
A buffer that can only be read from, distinct from :data:`ConstantBuffer`.
"""

BindType.ReadWriteBuffer.__doc__ = """
A buffer that can be read from and written to arbitrarily.
"""

BindType.ReadOnlyResource.__doc__ = """
A resource that can only be read from
"""

BindType.ReadWriteResource.__doc__ = """
A resource that can be read from and written to arbitrarily.
"""

BindType.InputAttachment.__doc__ = """
An input attachment for reading from the target currently being written.
"""

