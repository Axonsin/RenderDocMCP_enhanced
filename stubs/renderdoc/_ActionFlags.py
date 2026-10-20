from enum import IntFlag

class ActionFlags(IntFlag):
    # Original docstring
    """
    A set of flags describing the properties of a particular action. An action is a call
    such as a draw, a compute dispatch, clears, copies, resolves, etc. Any GPU event which may have
    deliberate visible side-effects to application-visible memory, typically resources such as textures
    and buffers. It also includes markers, which provide a user-generated annotation of events and
    actions.
    
    .. data:: NoFlags
    
      The action has no special properties.
    
    .. data:: Clear
    
      The action is a clear call. See :data:`ClearColor` and :data:`ClearDepthStencil`.
    
    .. data:: Drawcall
    
      The action renders primitives using the graphics pipeline.
    
    .. data:: Dispatch
    
      The action issues a number of compute workgroups.
    
    .. data:: MeshDispatch
    
      The action issues a number of mesh groups for a draw.
    
    .. data:: CmdList
    
      The action calls into a previously recorded child command list.
    
    .. data:: SetMarker
    
      The action inserts a single debugging marker.
    
    .. data:: PushMarker
    
      The action begins a debugging marker region that has children.
    
    .. data:: PopMarker
    
      The action ends a debugging marker region.
    
    .. data:: Present
    
      The action is a presentation call that hands a swapchain image to the presentation engine.
    
    .. data:: MultiAction
    
      The action is a multi-action that contains several specified child actions. Typically a MultiDraw
      or ExecuteIndirect on D3D12.
    
    .. data:: Copy
    
      The action performs a resource copy operation.
    
    .. data:: Resolve
    
      The action performs a resource resolve or blit operation.
    
    .. data:: GenMips
    
      The action performs a resource mip-generation operation.
    
    .. data:: PassBoundary
    
      The action marks the beginning or end of a render pass. See :data:`BeginPass` and
      :data:`EndPass`.
    
    .. data:: DispatchRay
    
      This action issues a number of rays.
    
    .. data:: BuildAccStruct
    
      This action builds or copies to and implicitly fills an acceleration structure.
    
    .. data:: Indexed
    
      The action uses an index buffer.
    
    .. data:: Instanced
    
      The action uses instancing. This does not mean it renders more than one instanced, simply that
      it uses the instancing feature.
    
    .. data:: Auto
    
      The action interacts with stream-out to render all vertices previously written. This is a
      Direct3D 11 specific feature.
    
    .. data:: Indirect
    
      The action uses a buffer on the GPU to source some or all of its parameters in an indirect way.
    
    .. data:: ClearColor
    
      The action clears a color target.
    
    .. data:: ClearDepthStencil
    
      The action clears a depth-stencil target.
    
    .. data:: BeginPass
    
      The action marks the beginning of a render pass.
    
    .. data:: EndPass
    
      The action marks the end of a render pass.
    
    .. data:: CommandBufferBoundary
    
      The action is a virtual marker added to show command buffer boundaries.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    The action has no special properties.
    """
    
    Clear = 1
    """
    The action is a clear call. See :data:`ClearColor` and :data:`ClearDepthStencil`.
    """
    
    Drawcall = 2
    """
    The action renders primitives using the graphics pipeline.
    """
    
    Dispatch = 4
    """
    The action issues a number of compute workgroups.
    """
    
    MeshDispatch = 8
    """
    The action issues a number of mesh groups for a draw.
    """
    
    CmdList = 16
    """
    The action calls into a previously recorded child command list.
    """
    
    SetMarker = 32
    """
    The action inserts a single debugging marker.
    """
    
    PushMarker = 64
    """
    The action begins a debugging marker region that has children.
    """
    
    PopMarker = 128
    """
    The action ends a debugging marker region.
    """
    
    Present = 256
    """
    The action is a presentation call that hands a swapchain image to the presentation engine.
    """
    
    MultiAction = 512
    """
    The action is a multi-action that contains several specified child actions. Typically a MultiDraw
    or ExecuteIndirect on D3D12.
    """
    
    Copy = 1024
    """
    The action performs a resource copy operation.
    """
    
    Resolve = 2048
    """
    The action performs a resource resolve or blit operation.
    """
    
    GenMips = 4096
    """
    The action performs a resource mip-generation operation.
    """
    
    PassBoundary = 8192
    """
    The action marks the beginning or end of a render pass. See :data:`BeginPass` and
    :data:`EndPass`.
    """
    
    DispatchRay = 16384
    """
    This action issues a number of rays.
    """
    
    BuildAccStruct = 32768
    """
    This action builds or copies to and implicitly fills an acceleration structure.
    """
    
    Indexed = 65536
    """
    The action uses an index buffer.
    """
    
    Instanced = 131072
    """
    The action uses instancing. This does not mean it renders more than one instanced, simply that
    it uses the instancing feature.
    """
    
    Auto = 262144
    """
    The action interacts with stream-out to render all vertices previously written. This is a
    Direct3D 11 specific feature.
    """
    
    Indirect = 524288
    """
    The action uses a buffer on the GPU to source some or all of its parameters in an indirect way.
    """
    
    ClearColor = 1048576
    """
    The action clears a color target.
    """
    
    ClearDepthStencil = 2097152
    """
    The action clears a depth-stencil target.
    """
    
    BeginPass = 4194304
    """
    The action marks the beginning of a render pass.
    """
    
    EndPass = 8388608
    """
    The action marks the end of a render pass.
    """
    
    CommandBufferBoundary = 16777216
    """
    The action is a virtual marker added to show command buffer boundaries.
    """
    

# Assign __doc__ for enum values for easier introspection

ActionFlags.NoFlags.__doc__ = """
The action has no special properties.
"""

ActionFlags.Clear.__doc__ = """
The action is a clear call. See :data:`ClearColor` and :data:`ClearDepthStencil`.
"""

ActionFlags.Drawcall.__doc__ = """
The action renders primitives using the graphics pipeline.
"""

ActionFlags.Dispatch.__doc__ = """
The action issues a number of compute workgroups.
"""

ActionFlags.MeshDispatch.__doc__ = """
The action issues a number of mesh groups for a draw.
"""

ActionFlags.CmdList.__doc__ = """
The action calls into a previously recorded child command list.
"""

ActionFlags.SetMarker.__doc__ = """
The action inserts a single debugging marker.
"""

ActionFlags.PushMarker.__doc__ = """
The action begins a debugging marker region that has children.
"""

ActionFlags.PopMarker.__doc__ = """
The action ends a debugging marker region.
"""

ActionFlags.Present.__doc__ = """
The action is a presentation call that hands a swapchain image to the presentation engine.
"""

ActionFlags.MultiAction.__doc__ = """
The action is a multi-action that contains several specified child actions. Typically a MultiDraw
or ExecuteIndirect on D3D12.
"""

ActionFlags.Copy.__doc__ = """
The action performs a resource copy operation.
"""

ActionFlags.Resolve.__doc__ = """
The action performs a resource resolve or blit operation.
"""

ActionFlags.GenMips.__doc__ = """
The action performs a resource mip-generation operation.
"""

ActionFlags.PassBoundary.__doc__ = """
The action marks the beginning or end of a render pass. See :data:`BeginPass` and
:data:`EndPass`.
"""

ActionFlags.DispatchRay.__doc__ = """
This action issues a number of rays.
"""

ActionFlags.BuildAccStruct.__doc__ = """
This action builds or copies to and implicitly fills an acceleration structure.
"""

ActionFlags.Indexed.__doc__ = """
The action uses an index buffer.
"""

ActionFlags.Instanced.__doc__ = """
The action uses instancing. This does not mean it renders more than one instanced, simply that
it uses the instancing feature.
"""

ActionFlags.Auto.__doc__ = """
The action interacts with stream-out to render all vertices previously written. This is a
Direct3D 11 specific feature.
"""

ActionFlags.Indirect.__doc__ = """
The action uses a buffer on the GPU to source some or all of its parameters in an indirect way.
"""

ActionFlags.ClearColor.__doc__ = """
The action clears a color target.
"""

ActionFlags.ClearDepthStencil.__doc__ = """
The action clears a depth-stencil target.
"""

ActionFlags.BeginPass.__doc__ = """
The action marks the beginning of a render pass.
"""

ActionFlags.EndPass.__doc__ = """
The action marks the end of a render pass.
"""

ActionFlags.CommandBufferBoundary.__doc__ = """
The action is a virtual marker added to show command buffer boundaries.
"""

