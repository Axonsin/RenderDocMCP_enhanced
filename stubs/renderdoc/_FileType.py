from enum import IntEnum

class FileType(IntEnum):
    # Original docstring
    """
    The format of an image file
    
    .. data:: DDS
    
      A DDS file
    
    .. data:: PNG
    
      A PNG file
    
    .. data:: JPG
    
      A JPG file
    
    .. data:: BMP
    
      A BMP file
    
    .. data:: TGA
    
      A TGA file
    
    .. data:: HDR
    
      An HDR file
    
    .. data:: EXR
    
      An EXR file
    
    .. data:: Raw
    
      Raw data, just the bytes of the image tightly packed with no metadata or compression/encoding
    """
    
    
    # Enum values
    
    DDS = 0
    """
    A DDS file
    """
    
    PNG = 1
    """
    A PNG file
    """
    
    JPG = 2
    """
    A JPG file
    """
    
    BMP = 3
    """
    A BMP file
    """
    
    TGA = 4
    """
    A TGA file
    """
    
    HDR = 5
    """
    An HDR file
    """
    
    EXR = 6
    """
    An EXR file
    """
    
    Raw = 7
    """
    Raw data, just the bytes of the image tightly packed with no metadata or compression/encoding
    """
    
    Count = 8
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

FileType.DDS.__doc__ = """
A DDS file
"""

FileType.PNG.__doc__ = """
A PNG file
"""

FileType.JPG.__doc__ = """
A JPG file
"""

FileType.BMP.__doc__ = """
A BMP file
"""

FileType.TGA.__doc__ = """
A TGA file
"""

FileType.HDR.__doc__ = """
An HDR file
"""

FileType.EXR.__doc__ = """
An EXR file
"""

FileType.Raw.__doc__ = """
Raw data, just the bytes of the image tightly packed with no metadata or compression/encoding
"""

FileType.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

FileType.First.__doc__ = """
The first enum value, for ease of iteration.
"""

