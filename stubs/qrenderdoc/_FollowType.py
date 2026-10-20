from enum import IntEnum

class FollowType(IntEnum):
    # Original docstring
    """
    Specifies a type of followed resource for the :class:`TextureViewer`.
    
    .. data:: OutputColor
    
      The index specifies which output color target to select. Shader stage and array index are ignored.
    
    .. data:: OutputDepth
    
      The resource followed is the depth/stencil output target. All other parameters are ignored.
    
    .. data:: ReadWrite
    
      The index specifies a resource within the given shader's
      :data:`~renderdoc.ShaderReflection.readWriteResources`. The array element
      then specifies the index within that resource's array, if applicable.
    
    .. data:: ReadOnly
    
      The index specifies a resource within the given shader's
      :data:`~renderdoc.ShaderReflection.readOnlyResources`. The array element
      then specifies the index within that resource's array, if applicable.
    
    .. data:: OutputDepthResolve
    
      The resource followed is the depth/stencil resolve output target. All other parameters are ignored.
    """
    
    
    # Enum values
    
    OutputColor = 0
    """
    The index specifies which output color target to select. Shader stage and array index are ignored.
    """
    
    OutputDepth = 1
    """
    The resource followed is the depth/stencil output target. All other parameters are ignored.
    """
    
    ReadWrite = 2
    """
    The index specifies a resource within the given shader's
    :data:`~renderdoc.ShaderReflection.readWriteResources`. The array element
    then specifies the index within that resource's array, if applicable.
    """
    
    ReadOnly = 3
    """
    The index specifies a resource within the given shader's
    :data:`~renderdoc.ShaderReflection.readOnlyResources`. The array element
    then specifies the index within that resource's array, if applicable.
    """
    
    OutputDepthResolve = 4
    """
    The resource followed is the depth/stencil resolve output target. All other parameters are ignored.
    """
    

# Assign __doc__ for enum values for easier introspection

FollowType.OutputColor.__doc__ = """
The index specifies which output color target to select. Shader stage and array index are ignored.
"""

FollowType.OutputDepth.__doc__ = """
The resource followed is the depth/stencil output target. All other parameters are ignored.
"""

FollowType.ReadWrite.__doc__ = """
The index specifies a resource within the given shader's
:data:`~renderdoc.ShaderReflection.readWriteResources`. The array element
then specifies the index within that resource's array, if applicable.
"""

FollowType.ReadOnly.__doc__ = """
The index specifies a resource within the given shader's
:data:`~renderdoc.ShaderReflection.readOnlyResources`. The array element
then specifies the index within that resource's array, if applicable.
"""

FollowType.OutputDepthResolve.__doc__ = """
The resource followed is the depth/stencil resolve output target. All other parameters are ignored.
"""

