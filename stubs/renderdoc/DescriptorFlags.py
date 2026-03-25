# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DescriptorFlags(__enum.IntFlag):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AppendBuffer = 2
    """ On D3D, a buffer is used as a append/consume view. """

    CounterBuffer = 4
    """ On D3D, a buffer is used with a structured buffer with associated hidden counter. """

    InlineData = 32
    """
    This descriptor isn't backed by an explicit buffer in the API (though a resource may be provided
      for data query purposes during replay), but instead by some virtual or in-line data. For example
      in-line constants set directly, or compile/creation time constants.
    
      The exact nature can be determined by the shader reflection data.
    """

    NoFlags = 0
    """ The buffer will not be used for any of the uses below. """

    RawBuffer = 1
    """ On D3D, a buffer is used as a raw (byte-addressed) buffer. """

    ReadOnlyAccess = 8
    """ On GL, a storage image or buffer is bound with read-only access. """

    WriteOnlyAccess = 16
    """ On GL, a storage image or buffer is bound with write-only access. """



