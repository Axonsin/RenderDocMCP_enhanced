from enum import IntFlag

class DescriptorFlags(IntFlag):
    # Original docstring
    """
    A set of flags for descriptor properties.
    
    .. data:: NoFlags
    
      The buffer will not be used for any of the uses below.
    
    .. data:: RawBuffer
    
      On D3D, a buffer is used as a raw (byte-addressed) buffer.
    
    .. data:: AppendBuffer
    
      On D3D, a buffer is used as a append/consume view.
    
    .. data:: CounterBuffer
    
      On D3D, a buffer is used with a structured buffer with associated hidden counter.
    
    .. data:: ReadOnlyAccess
    
      On GL, a storage image or buffer is bound with read-only access.
    
    .. data:: WriteOnlyAccess
    
      On GL, a storage image or buffer is bound with write-only access.
    
    .. data:: InlineData
    
      This descriptor isn't backed by an explicit buffer in the API (though a resource may be provided
      for data query purposes during replay), but instead by some virtual or in-line data. For example
      in-line constants set directly, or compile/creation time constants.
    
      The exact nature can be determined by the shader reflection data.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    The buffer will not be used for any of the uses below.
    """
    
    RawBuffer = 1
    """
    On D3D, a buffer is used as a raw (byte-addressed) buffer.
    """
    
    AppendBuffer = 2
    """
    On D3D, a buffer is used as a append/consume view.
    """
    
    CounterBuffer = 4
    """
    On D3D, a buffer is used with a structured buffer with associated hidden counter.
    """
    
    ReadOnlyAccess = 8
    """
    On GL, a storage image or buffer is bound with read-only access.
    """
    
    WriteOnlyAccess = 16
    """
    On GL, a storage image or buffer is bound with write-only access.
    """
    
    InlineData = 32
    """
    This descriptor isn't backed by an explicit buffer in the API (though a resource may be provided
    for data query purposes during replay), but instead by some virtual or in-line data. For example
    in-line constants set directly, or compile/creation time constants.
    
    The exact nature can be determined by the shader reflection data.
    """
    

# Assign __doc__ for enum values for easier introspection

DescriptorFlags.NoFlags.__doc__ = """
The buffer will not be used for any of the uses below.
"""

DescriptorFlags.RawBuffer.__doc__ = """
On D3D, a buffer is used as a raw (byte-addressed) buffer.
"""

DescriptorFlags.AppendBuffer.__doc__ = """
On D3D, a buffer is used as a append/consume view.
"""

DescriptorFlags.CounterBuffer.__doc__ = """
On D3D, a buffer is used with a structured buffer with associated hidden counter.
"""

DescriptorFlags.ReadOnlyAccess.__doc__ = """
On GL, a storage image or buffer is bound with read-only access.
"""

DescriptorFlags.WriteOnlyAccess.__doc__ = """
On GL, a storage image or buffer is bound with write-only access.
"""

DescriptorFlags.InlineData.__doc__ = """
This descriptor isn't backed by an explicit buffer in the API (though a resource may be provided
for data query purposes during replay), but instead by some virtual or in-line data. For example
in-line constants set directly, or compile/creation time constants.

The exact nature can be determined by the shader reflection data.
"""

