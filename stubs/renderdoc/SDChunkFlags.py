# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SDChunkFlags(__enum.IntFlag):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    HasCallstack = 2
    """
    This chunk has a callstack. Used to indicate the presence of a callstack even if it's empty
      (perhaps due to failure to collect the stack frames).
    """

    NoFlags = 0
    """ This chunk has no special properties. """

    OpaqueChunk = 1
    """
    This chunk wasn't supported for decoding or was skipped for another reason and was detailed as
      an opaque byte stream. It should be preserved as-is and will remain in native RDC format.
    """



