# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class MeshDataStage(__enum.IntEnum):
    """
    Describes a particular stage in the geometry transformation pipeline.
    
    .. data:: VSIn
    
      The inputs to the vertex shader described by the explicit API vertex input bindings.
    
    .. data:: VSOut
    
      The outputs from the vertex shader corresponding one-to-one to the input elements.
    
    .. data:: GSOut
    
      The final output from the last stage in the pipeline, be that tessellation or geometry shader.
    
      This has possibly been expanded/multiplied from the inputs
    
    .. data:: TaskOut
    
      Data from a task/amplification shader.
    
    .. data:: AmpOut
    
      Data from an amplification shader (alias for :data:`TaskOut`).
    
    .. data:: MeshOut
    
      Data from a mesh shader.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AmpOut = 3
    """ Data from an amplification shader (alias for :data:`TaskOut`). """

    Count = 5
    First = 0
    GSOut = 2
    """
    The final output from the last stage in the pipeline, be that tessellation or geometry shader.
    
      This has possibly been expanded/multiplied from the inputs
    """

    MeshOut = 4
    """ Data from a mesh shader. """

    TaskOut = 3
    """ Data from a task/amplification shader. """

    VSIn = 0
    """ The inputs to the vertex shader described by the explicit API vertex input bindings. """

    VSOut = 1
    """ The outputs from the vertex shader corresponding one-to-one to the input elements. """



