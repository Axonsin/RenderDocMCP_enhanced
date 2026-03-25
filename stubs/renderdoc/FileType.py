# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class FileType(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    BMP = 3
    """ A BMP file """

    Count = 8
    DDS = 0
    """ A DDS file """

    EXR = 6
    """ An EXR file """

    First = 0
    HDR = 5
    """ An HDR file """

    JPG = 2
    """ A JPG file """

    PNG = 1
    """ A PNG file """

    Raw = 7
    """ Raw data, just the bytes of the image tightly packed with no metadata or compression/encoding """

    TGA = 4
    """ A TGA file """



