from enum import IntEnum

class ResourceType(IntEnum):
    # Original docstring
    """
    The type of a resource referred to by binding or API usage.
    
    In some cases there is a little overlap or fudging when mapping API concepts - this is primarily
    just intended for e.g. fuzzy user filtering or rough categorisation. Precise mapping would require
    API-specific concepts.
    
    .. data:: Unknown
    
      An unknown type of resource.
    
    .. data:: Device
    
      A system-level object, typically unique.
    
    .. data:: Queue
    
      A queue representing the ability to execute commands in a single stream, possibly in parallel to
      other queues.
    
    .. data:: CommandBuffer
    
      A recorded set of commands that can then be subsequently executed.
    
    .. data:: Texture
    
      A texture - one- to three- dimensional, possibly with array layers and mip levels. See
      :class:`TextureDescription`.
    
    .. data:: Buffer
    
      A linear (possibly typed) view of memory. See :class:`BufferDescription`.
    
    .. data:: View
    
      A particular view into a texture or buffer, e.g. either accessing the underlying resource through
      a different type, or only a subset of the resource.
    
    .. data:: Sampler
    
      The information regarding how a texture is accessed including wrapping, minification/magnification
      and other information. The precise details are API-specific and listed in the API state when
      bound.
    
    .. data:: SwapchainImage
    
      A special class of :data:`Texture` that is owned by the swapchain and is used for presentation.
    
    .. data:: Memory
    
      An object corresponding to an actual memory allocation, which other resources can then be bound
      to.
    
    .. data:: Shader
    
      A single shader object for any shader stage. May be bound directly, or used to compose into a
      :data:`PipelineState` depending on the API.
    
    .. data:: ShaderBinding
    
      An object that determines some manner of shader binding. Since this varies significantly by API,
      different concepts used for shader resource binding fall under this type.
    
    .. data:: PipelineState
    
      A single object containing all information regarding the current GPU pipeline, containing both
      shader objects, potentially some shader binding information, and fixed-function state.
    
    .. data:: StateObject
    
      A single object encapsulating some amount of related state that can be set together, instead of
      setting each individual state separately.
    
    .. data:: RenderPass
    
      An object related to collecting render pass information together. This may not be an actual
      explicit render pass object if it doesn't exist in the API, it may also be a collection of
      textures in a framebuffer that are bound together to the API for rendering.
    
    .. data:: Query
    
      A query for retrieving some kind of feedback from the GPU, either as a fixed number or a boolean
      value which can be used in predicated rendering.
    
    .. data:: Sync
    
      A synchronisation object used for either synchronisation between GPU and CPU, or GPU-to-GPU work.
    
    .. data:: Pool
    
      An object which pools together other objects in an opaque way, either for runtime allocation and
      deallocation, or for caching purposes.
    
    .. data:: AccelerationStructure
    
      A structure used to carry implementation-defined spatial partitioning data and related
      information, used to accelerate geometry intersection queries (e.g. for ray tracing).
    
    .. data:: DescriptorStore
    
      A descriptor store, either driver or application managed. For example a Vulkan descriptor set or
      a D3D12 descriptor heap.
    
      APIs without an explicit concept of descriptor storage will have virtual objects corresponding to
      temporary bindings.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown type of resource.
    """
    
    Device = 1
    """
    A system-level object, typically unique.
    """
    
    Queue = 2
    """
    A queue representing the ability to execute commands in a single stream, possibly in parallel to
    other queues.
    """
    
    CommandBuffer = 3
    """
    A recorded set of commands that can then be subsequently executed.
    """
    
    Texture = 4
    """
    A texture - one- to three- dimensional, possibly with array layers and mip levels. See
    :class:`TextureDescription`.
    """
    
    Buffer = 5
    """
    A linear (possibly typed) view of memory. See :class:`BufferDescription`.
    """
    
    View = 6
    """
    A particular view into a texture or buffer, e.g. either accessing the underlying resource through
    a different type, or only a subset of the resource.
    """
    
    Sampler = 7
    """
    The information regarding how a texture is accessed including wrapping, minification/magnification
    and other information. The precise details are API-specific and listed in the API state when
    bound.
    """
    
    SwapchainImage = 8
    """
    A special class of :data:`Texture` that is owned by the swapchain and is used for presentation.
    """
    
    Memory = 9
    """
    An object corresponding to an actual memory allocation, which other resources can then be bound
    to.
    """
    
    Shader = 10
    """
    A single shader object for any shader stage. May be bound directly, or used to compose into a
    :data:`PipelineState` depending on the API.
    """
    
    ShaderBinding = 11
    """
    An object that determines some manner of shader binding. Since this varies significantly by API,
    different concepts used for shader resource binding fall under this type.
    """
    
    PipelineState = 12
    """
    A single object containing all information regarding the current GPU pipeline, containing both
    shader objects, potentially some shader binding information, and fixed-function state.
    """
    
    StateObject = 13
    """
    A single object encapsulating some amount of related state that can be set together, instead of
    setting each individual state separately.
    """
    
    RenderPass = 14
    """
    An object related to collecting render pass information together. This may not be an actual
    explicit render pass object if it doesn't exist in the API, it may also be a collection of
    textures in a framebuffer that are bound together to the API for rendering.
    """
    
    Query = 15
    """
    A query for retrieving some kind of feedback from the GPU, either as a fixed number or a boolean
    value which can be used in predicated rendering.
    """
    
    Sync = 16
    """
    A synchronisation object used for either synchronisation between GPU and CPU, or GPU-to-GPU work.
    """
    
    Pool = 17
    """
    An object which pools together other objects in an opaque way, either for runtime allocation and
    deallocation, or for caching purposes.
    """
    
    AccelerationStructure = 18
    """
    A structure used to carry implementation-defined spatial partitioning data and related
    information, used to accelerate geometry intersection queries (e.g. for ray tracing).
    """
    
    DescriptorStore = 19
    """
    A descriptor store, either driver or application managed. For example a Vulkan descriptor set or
    a D3D12 descriptor heap.
    
    APIs without an explicit concept of descriptor storage will have virtual objects corresponding to
    temporary bindings.
    """
    

# Assign __doc__ for enum values for easier introspection

ResourceType.Unknown.__doc__ = """
An unknown type of resource.
"""

ResourceType.Device.__doc__ = """
A system-level object, typically unique.
"""

ResourceType.Queue.__doc__ = """
A queue representing the ability to execute commands in a single stream, possibly in parallel to
other queues.
"""

ResourceType.CommandBuffer.__doc__ = """
A recorded set of commands that can then be subsequently executed.
"""

ResourceType.Texture.__doc__ = """
A texture - one- to three- dimensional, possibly with array layers and mip levels. See
:class:`TextureDescription`.
"""

ResourceType.Buffer.__doc__ = """
A linear (possibly typed) view of memory. See :class:`BufferDescription`.
"""

ResourceType.View.__doc__ = """
A particular view into a texture or buffer, e.g. either accessing the underlying resource through
a different type, or only a subset of the resource.
"""

ResourceType.Sampler.__doc__ = """
The information regarding how a texture is accessed including wrapping, minification/magnification
and other information. The precise details are API-specific and listed in the API state when
bound.
"""

ResourceType.SwapchainImage.__doc__ = """
A special class of :data:`Texture` that is owned by the swapchain and is used for presentation.
"""

ResourceType.Memory.__doc__ = """
An object corresponding to an actual memory allocation, which other resources can then be bound
to.
"""

ResourceType.Shader.__doc__ = """
A single shader object for any shader stage. May be bound directly, or used to compose into a
:data:`PipelineState` depending on the API.
"""

ResourceType.ShaderBinding.__doc__ = """
An object that determines some manner of shader binding. Since this varies significantly by API,
different concepts used for shader resource binding fall under this type.
"""

ResourceType.PipelineState.__doc__ = """
A single object containing all information regarding the current GPU pipeline, containing both
shader objects, potentially some shader binding information, and fixed-function state.
"""

ResourceType.StateObject.__doc__ = """
A single object encapsulating some amount of related state that can be set together, instead of
setting each individual state separately.
"""

ResourceType.RenderPass.__doc__ = """
An object related to collecting render pass information together. This may not be an actual
explicit render pass object if it doesn't exist in the API, it may also be a collection of
textures in a framebuffer that are bound together to the API for rendering.
"""

ResourceType.Query.__doc__ = """
A query for retrieving some kind of feedback from the GPU, either as a fixed number or a boolean
value which can be used in predicated rendering.
"""

ResourceType.Sync.__doc__ = """
A synchronisation object used for either synchronisation between GPU and CPU, or GPU-to-GPU work.
"""

ResourceType.Pool.__doc__ = """
An object which pools together other objects in an opaque way, either for runtime allocation and
deallocation, or for caching purposes.
"""

ResourceType.AccelerationStructure.__doc__ = """
A structure used to carry implementation-defined spatial partitioning data and related
information, used to accelerate geometry intersection queries (e.g. for ray tracing).
"""

ResourceType.DescriptorStore.__doc__ = """
A descriptor store, either driver or application managed. For example a Vulkan descriptor set or
a D3D12 descriptor heap.

APIs without an explicit concept of descriptor storage will have virtual objects corresponding to
temporary bindings.
"""

