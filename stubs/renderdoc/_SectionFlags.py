from enum import IntFlag

class SectionFlags(IntFlag):
    # Original docstring
    """
    A set of flags describing the properties of a section in a renderdoc capture.
    
    .. data:: NoFlags
    
      No special section properties.
    
    .. data:: ASCIIStored
    
      This section was stored as pure ASCII. This can be useful since it is possible to generate
      an ASCII section in a text editor by hand or with any simple printf style script, and then
      concatenate it to a .rdc and have a valid section.
    
    .. data:: LZ4Compressed
    
      This section is compressed with LZ4 on disk.
    
    .. data:: ZstdCompressed
    
      This section is compressed with Zstd on disk.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    No special section properties.
    """
    
    ASCIIStored = 1
    """
    This section was stored as pure ASCII. This can be useful since it is possible to generate
    an ASCII section in a text editor by hand or with any simple printf style script, and then
    concatenate it to a .rdc and have a valid section.
    """
    
    LZ4Compressed = 2
    """
    This section is compressed with LZ4 on disk.
    """
    
    ZstdCompressed = 4
    """
    This section is compressed with Zstd on disk.
    """
    

# Assign __doc__ for enum values for easier introspection

SectionFlags.NoFlags.__doc__ = """
No special section properties.
"""

SectionFlags.ASCIIStored.__doc__ = """
This section was stored as pure ASCII. This can be useful since it is possible to generate
an ASCII section in a text editor by hand or with any simple printf style script, and then
concatenate it to a .rdc and have a valid section.
"""

SectionFlags.LZ4Compressed.__doc__ = """
This section is compressed with LZ4 on disk.
"""

SectionFlags.ZstdCompressed.__doc__ = """
This section is compressed with Zstd on disk.
"""

