# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BufferCategory(__enum.IntFlag):
    """
    A set of flags describing how this buffer may be used
    
    .. data:: NoFlags
    
      The buffer will not be used for any of the uses below.
    
    .. data:: Vertex
    
      The buffer will be used for sourcing vertex input data.
    
    .. data:: Index
    
      The buffer will be used for sourcing primitive index data.
    
    .. data:: Constants
    
      The buffer will be used for sourcing shader constant data.
    
    .. data:: ReadWrite
    
      The buffer will be used for read and write access from shaders.
    
    .. data:: Indirect
    
      The buffer will be used to provide indirect parameters for launching GPU-based actions.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Constants = 4
    """ The buffer will be used for sourcing shader constant data. """

    Index = 2
    """ The buffer will be used for sourcing primitive index data. """

    Indirect = 16
    """ The buffer will be used to provide indirect parameters for launching GPU-based actions. """

    NoFlags = 0
    """ The buffer will not be used for any of the uses below. """

    ReadWrite = 8
    """ The buffer will be used for read and write access from shaders. """

    Vertex = 1
    """ The buffer will be used for sourcing vertex input data. """



