# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class FollowType(__enum.IntEnum):
    """
    Specifies a type of followed resource for the :class:`TextureViewer`.
    
    .. data:: OutputColor
    
      The index specifies which output color target to select. Shader stage and array index are ignored.
    
    .. data:: OutputDepth
    
      The resource followed is the depth/stencil output target. All other parameters are ignored.
    
    .. data:: ReadWrite
    
      The index specifies a resource within the given shader's
      :data:`read-write resources <~renderdoc.ShaderReflection.readWriteResources>`. The array element
      then specifies the index within that resource's array, if applicable.
    
    .. data:: ReadOnly
    
      The index specifies a resource within the given shader's
      :data:`read-only resources <~renderdoc.ShaderReflection.readOnlyResources>`. The array element
      then specifies the index within that resource's array, if applicable.
    
    .. data:: OutputDepthResolve
    
      The resource followed is the depth/stencil resolve output target. All other parameters are ignored.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    OutputColor = 0
    """ The index specifies which output color target to select. Shader stage and array index are ignored. """

    OutputDepth = 1
    """ The resource followed is the depth/stencil output target. All other parameters are ignored. """

    OutputDepthResolve = 4
    """ The resource followed is the depth/stencil resolve output target. All other parameters are ignored. """

    ReadOnly = 3
    """
    The index specifies a resource within the given shader's
      :data:`read-only resources <~renderdoc.ShaderReflection.readOnlyResources>`. The array element
      then specifies the index within that resource's array, if applicable.
    """

    ReadWrite = 2
    """
    The index specifies a resource within the given shader's
      :data:`read-write resources <~renderdoc.ShaderReflection.readWriteResources>`. The array element
      then specifies the index within that resource's array, if applicable.
    """



