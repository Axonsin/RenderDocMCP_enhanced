# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SectionFlags(__enum.IntFlag):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    ASCIIStored = 1
    """
    This section was stored as pure ASCII. This can be useful since it is possible to generate
      an ASCII section in a text editor by hand or with any simple printf style script, and then
      concatenate it to a .rdc and have a valid section.
    """

    LZ4Compressed = 2
    """ This section is compressed with LZ4 on disk. """

    NoFlags = 0
    """ No special section properties. """

    ZstdCompressed = 4
    """ This section is compressed with Zstd on disk. """



