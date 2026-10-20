from enum import IntFlag

class SDChunkFlags(IntFlag):
    # Original docstring
    """
    Bitfield flags that could be applied to an :class:`SDChunk`.
    
    .. data:: NoFlags
    
      This chunk has no special properties.
    
    .. data:: OpaqueChunk
    
      This chunk wasn't supported for decoding or was skipped for another reason and was detailed as
      an opaque byte stream. It should be preserved as-is and will remain in native RDC format.
    
    .. data:: HasCallstack
    
      This chunk has a callstack. Used to indicate the presence of a callstack even if it's empty
      (perhaps due to failure to collect the stack frames).
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    This chunk has no special properties.
    """
    
    OpaqueChunk = 1
    """
    This chunk wasn't supported for decoding or was skipped for another reason and was detailed as
    an opaque byte stream. It should be preserved as-is and will remain in native RDC format.
    """
    
    HasCallstack = 2
    """
    This chunk has a callstack. Used to indicate the presence of a callstack even if it's empty
    (perhaps due to failure to collect the stack frames).
    """
    

# Assign __doc__ for enum values for easier introspection

SDChunkFlags.NoFlags.__doc__ = """
This chunk has no special properties.
"""

SDChunkFlags.OpaqueChunk.__doc__ = """
This chunk wasn't supported for decoding or was skipped for another reason and was detailed as
an opaque byte stream. It should be preserved as-is and will remain in native RDC format.
"""

SDChunkFlags.HasCallstack.__doc__ = """
This chunk has a callstack. Used to indicate the presence of a callstack even if it's empty
(perhaps due to failure to collect the stack frames).
"""

