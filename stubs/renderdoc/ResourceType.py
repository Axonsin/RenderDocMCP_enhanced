# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ResourceType(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AccelerationStructure = 18
    """
    A structure used to carry implementation-defined spatial partitioning data and related
      information, used to accelerate geometry intersection queries (e.g. for ray tracing).
    """

    Buffer = 5
    """ A linear (possibly typed) view of memory. See :class:`BufferDescription`. """

    CommandBuffer = 3
    """ A recorded set of commands that can then be subsequently executed. """

    DescriptorStore = 19
    """
    A descriptor store, either driver or application managed. For example a Vulkan descriptor set or
      a D3D12 descriptor heap.
    
      APIs without an explicit concept of descriptor storage will have virtual objects corresponding to
      temporary bindings.
    """

    Device = 1
    """ A system-level object, typically unique. """

    Memory = 9
    """
    An object corresponding to an actual memory allocation, which other resources can then be bound
      to.
    """

    PipelineState = 12
    """
    A single object containing all information regarding the current GPU pipeline, containing both
      shader objects, potentially some shader binding information, and fixed-function state.
    """

    Pool = 17
    """
    An object which pools together other objects in an opaque way, either for runtime allocation and
      deallocation, or for caching purposes.
    """

    Query = 15
    """
    A query for retrieving some kind of feedback from the GPU, either as a fixed number or a boolean
      value which can be used in predicated rendering.
    """

    Queue = 2
    """
    A queue representing the ability to execute commands in a single stream, possibly in parallel to
      other queues.
    """

    RenderPass = 14
    """
    An object related to collecting render pass information together. This may not be an actual
      explicit render pass object if it doesn't exist in the API, it may also be a collection of
      textures in a framebuffer that are bound together to the API for rendering.
    """

    Sampler = 7
    """
    The information regarding how a texture is accessed including wrapping, minification/magnification
      and other information. The precise details are API-specific and listed in the API state when
      bound.
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

    StateObject = 13
    """
    A single object encapsulating some amount of related state that can be set together, instead of
      setting each individual state separately.
    """

    SwapchainImage = 8
    """ A special class of :data:`Texture` that is owned by the swapchain and is used for presentation. """

    Sync = 16
    """ A synchronisation object used for either synchronisation between GPU and CPU, or GPU-to-GPU work. """

    Texture = 4
    """
    A texture - one- to three- dimensional, possibly with array layers and mip levels. See
      :class:`TextureDescription`.
    """

    Unknown = 0
    """ An unknown type of resource. """

    View = 6
    """
    A particular view into a texture or buffer, e.g. either accessing the underlying resource through
      a different type, or only a subset of the resource.
    """



