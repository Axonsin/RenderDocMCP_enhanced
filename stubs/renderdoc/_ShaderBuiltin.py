from enum import IntEnum

class ShaderBuiltin(IntEnum):
    # Original docstring
    """
    Annotates a particular built-in input or output from a shader with a special meaning to
    the hardware or API.
    
    Some of the built-in inputs or outputs can be declared multiple times in arrays or otherwise indexed
    to apply to multiple related things - see :data:`ClipDistance`, :data:`CullDistance` and
    :data:`ColorOutput`.
    
    .. data:: Undefined
    
      Undefined built-in or no built-in is attached to this shader variable.
    
    .. data:: Position
    
      As an output from the final vertex processing shader stage, this feeds the vertex position to the
      rasterized. As an input to the pixel shader stage this receives the position from the rasterizer.
    
    .. data:: PointSize
    
      An output that controls the size of point primitives.
    
    .. data:: ClipDistance
    
      An output for the distance to a user-defined clipping plane. Any pixel with an interpolated value
      that is negative will not be rasterized. Typically there can be more than one such output.
    
    .. data:: CullDistance
    
      An output for the distance to a user-defined culling plane. Any primitive with all vertices having
      negative values will not be rasterized. Typically there can be more than one such output.
    
    .. data:: RTIndex
    
      An output for selecting the render target index in an array to render to. Available in geometry
      shaders and possibly earlier stages depending on hardware/API capability.
    
    .. data:: ViewportIndex
    
      An output for selecting the viewport index to render to. Available in geometry shaders and
      possibly earlier stages depending on hardware/API capability.
    
    .. data:: VertexIndex
    
      An input to the vertex shader listing the vertex index. The exact meaning of this index can vary
      by API but generally it refers to either a 0-based counter for non-indexed draws, or the index
      value for indexed draws. It may or may not be affected by offsets, depending on API semantics.
    
    .. data:: PrimitiveIndex
    
      A built-in indicating which primitive is being processed. This can be read by all primitive stages
      after the vertex shader, and written by the geometry shader.
    
    .. data:: InstanceIndex
    
      This built-in is defined similar to :data:`VertexIndex` but for instances within an instanced
      drawcall. It counts from 0 and as with :data:`VertexIndex` it may or may not be affected by
      drawcall offsets.
    
    .. data:: DispatchSize
    
      An input in compute shaders that gives the number of workgroups executed by the dispatch call.
    
    .. data:: DispatchThreadIndex
    
      An input in compute shaders giving a 3D shared index across all workgroups, such that the index
      varies across each thread in the workgroup up to its size, then the indices for workgroup
      ``(0,0,1)`` begin adjacent to where workgroup ``(0,0,0)`` ended.
    
      This is related to :data:`GroupThreadIndex` and :data:`GroupIndex`.
    
    .. data:: GroupIndex
    
      An input in compute shaders giving a 3D index of this current workgroup among all workgroups,
      up to the dispatch size.
    
      The index is constant across all threads in the workgroup.
    
      This is related to :data:`GroupThreadIndex` and :data:`DispatchThreadIndex`.
    
    .. data:: GroupSize
    
      The size of a workgroup, giving the number of threads in each dimension.
    
    .. data:: GroupFlatIndex
    
      An input in compute shaders giving a flat 1D index of the thread within the current workgroup.
      This index increments first in the ``X`` dimension, then in the ``Y`` dimension, then in the ``Z``
      dimension.
    
    .. data:: GroupThreadIndex
    
      An input in compute shaders giving a 3D index of this thread within its workgroup, up to the
      workgroup size.
    
      The input does not vary between one thread in a workgroup and the same thread in another
      workgroup.
    
      This is related to :data:`GroupIndex` and :data:`DispatchThreadIndex`.
    
    
    .. data:: GSInstanceIndex
    
      An input to the geometry shader giving the instance being run, if the geometry shader was setup to
      be invoked multiple times for each input primitive.
    
    .. data:: OutputControlPointIndex
    
      An input to the tessellation control or hull shader giving the output control point index or patch
      vertex being operated on.
    
    .. data:: DomainLocation
    
      An input to the tessellation evaluation or domain shader, giving the normalised location on the
      output patch where evaluation is occurring. E.g. for triangle output this is the barycentric
      co-ordinates of the output vertex.
    
    .. data:: IsFrontFace
    
      An input to the pixel shader indicating whether or not the contributing triangle was considered
      front-facing or not according to the API setup for winding order and backface orientation.
    
    .. data:: MSAACoverage
    
      An input or an output from the pixel shader. As an input, it specifies a bitmask of which samples
      in a pixel were covered by the rasterizer. As an output, it specifies which samples in the
      destination target should be updated.
    
    .. data:: MSAASamplePosition
    
      An input to the pixel shader that contains the location of the current sample relative to the
      pixel, when running the pixel shader at sample frequency.
    
    .. data:: MSAASampleIndex
    
      An input to the pixel shader that indicates which sample in the range ``0 .. N-1`` is currently
      being processed.
    
    .. data:: PatchNumVertices
    
      An input to the tessellation stages, this gives the number of vertices in each patch.
    
    .. data:: OuterTessFactor
    
      An output from the tessellation control or hull shader, this determines the level to which the
      outer edge of each primitive is tessellated by the fixed-function tessellator.
    
      It is also available for reading in the tessellation evaluation or domain shader.
    
    .. data:: InsideTessFactor
    
      Related to :data:`OuterTessFactor` this functions in the same way to determine the tessellation
      level inside the primitive.
    
    .. data:: ColorOutput
    
      An output from the pixel shader, this determines the color value written to the corresponding
      target. There will be as many color output built-ins as there are targets bound.
    
    .. data:: DepthOutput
    
      An output from the pixel shader, writes the depth of this pixel with no restrictions.
    
      Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutputLessEqual`.
    
    .. data:: DepthOutputGreaterEqual
    
      An output from the pixel shader, writes the depth of this pixel with the restriction that it will
      be greater than or equal to the original depth produced by the rasterizer.
    
      Related to :data:`DepthOutput` and :data:`DepthOutputLessEqual`.
    
    .. data:: DepthOutputLessEqual
    
      An output from the pixel shader, writes the depth of this pixel with the restriction that it will
      be less than or equal to the original depth produced by the rasterizer.
    
      Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutput`.
    
    .. data:: BaseVertex
    
      The first vertex processed in this draw, as specified by the ``firstVertex`` / ``baseVertex``
      parameter to the draw call.
    
    .. data:: BaseInstance
    
      The first instance processed in this draw call, as specified by the ``firstInstance`` parameter.
    
    .. data:: DrawIndex
    
      For indirect or multi-draw commands, the index of this draw call within the overall draw command.
    
    .. data:: StencilReference
    
      The stencil reference to be used for stenciling operations on this fragment.
    
    .. data:: PointCoord
    
      The fragments co-ordinates within a point primitive being rasterized.
    
    .. data:: IsHelper
    
      Indicates if the current invocation is a helper invocation.
    
    
    .. data:: SubgroupSize
    
      The number of invocations in a subgroup.
    
    .. data:: NumSubgroups
    
      The number of subgroups in the local workgroup.
    
    .. data:: SubgroupIndexInWorkgroup
    
      The index of the current subgroup within all subgroups in the workgroup, up to
      :data:`NumSubgroups` - 1.
    
    .. data:: IndexInSubgroup
    
      The index of the current thread in the current subgroup, up to :data:`SubgroupSize` - 1.
    
    .. data:: SubgroupEqualMask
    
      A bitmask where the bit corresponding to :data:`IndexInSubgroup` is set.
    
    .. data:: SubgroupGreaterEqualMask
    
      A bitmask where all bits greater or equal to the one corresponding to :data:`IndexInSubgroup` are
      set.
    
    .. data:: SubgroupGreaterMask
    
      A bitmask where all bits greater than the one corresponding to :data:`IndexInSubgroup` are set.
    
    .. data:: SubgroupLessEqualMask
    
      A bitmask where all bits less or equal to the one corresponding to :data:`IndexInSubgroup` are
      set.
    
    .. data:: SubgroupLessMask
    
      A bitmask where all bits less than the one corresponding to :data:`IndexInSubgroup` are set.
    
    .. data:: DeviceIndex
    
      The device index executing the shader, relative to the current device group.
    
    .. data:: IsFullyCovered
    
      Indicates if the current fragment area is fully covered by the generating primitive.
    
    .. data:: FragAreaSize
    
      Gives the dimensions of the area that the fragment covers.
    
    .. data:: FragInvocationCount
    
      Gives the maximum number of invocations for the fragment being covered.
    
    .. data:: PackedFragRate
    
      Contains the packed shading rate, with an API specific packing of X and Y. For example:
    
      1x being 0, 2x being 1, 4x being 2. Then the lower two bits being the Y rate and the next 2 bits
      being the X rate.
    
    .. data:: Barycentrics
    
      Contains the barycentric co-ordinates.
    
    .. data:: CullPrimitive
    
      An output to indicate whether or not a primitive should be culled.
    
    .. data:: OutputIndices
    
      An output containing the indices for a meshlet.
    
    .. data:: MultiViewIndex
    
      An input specifying the view being rendered to in multiview rendering. Only valid when multiview rendering is enabled.
    """
    
    
    # Enum values
    
    Undefined = 0
    """
    Undefined built-in or no built-in is attached to this shader variable.
    """
    
    Position = 1
    """
    As an output from the final vertex processing shader stage, this feeds the vertex position to the
    rasterized. As an input to the pixel shader stage this receives the position from the rasterizer.
    """
    
    PointSize = 2
    """
    An output that controls the size of point primitives.
    """
    
    ClipDistance = 3
    """
    An output for the distance to a user-defined clipping plane. Any pixel with an interpolated value
    that is negative will not be rasterized. Typically there can be more than one such output.
    """
    
    CullDistance = 4
    """
    An output for the distance to a user-defined culling plane. Any primitive with all vertices having
    negative values will not be rasterized. Typically there can be more than one such output.
    """
    
    RTIndex = 5
    """
    An output for selecting the render target index in an array to render to. Available in geometry
    shaders and possibly earlier stages depending on hardware/API capability.
    """
    
    ViewportIndex = 6
    """
    An output for selecting the viewport index to render to. Available in geometry shaders and
    possibly earlier stages depending on hardware/API capability.
    """
    
    VertexIndex = 7
    """
    An input to the vertex shader listing the vertex index. The exact meaning of this index can vary
    by API but generally it refers to either a 0-based counter for non-indexed draws, or the index
    value for indexed draws. It may or may not be affected by offsets, depending on API semantics.
    """
    
    PrimitiveIndex = 8
    """
    A built-in indicating which primitive is being processed. This can be read by all primitive stages
    after the vertex shader, and written by the geometry shader.
    """
    
    InstanceIndex = 9
    """
    This built-in is defined similar to :data:`VertexIndex` but for instances within an instanced
    drawcall. It counts from 0 and as with :data:`VertexIndex` it may or may not be affected by
    drawcall offsets.
    """
    
    DispatchSize = 10
    """
    An input in compute shaders that gives the number of workgroups executed by the dispatch call.
    """
    
    DispatchThreadIndex = 11
    """
    An input in compute shaders giving a 3D shared index across all workgroups, such that the index
    varies across each thread in the workgroup up to its size, then the indices for workgroup
    ``(0,0,1)`` begin adjacent to where workgroup ``(0,0,0)`` ended.
    
    This is related to :data:`GroupThreadIndex` and :data:`GroupIndex`.
    """
    
    GroupIndex = 12
    """
    An input in compute shaders giving a 3D index of this current workgroup among all workgroups,
    up to the dispatch size.
    
    The index is constant across all threads in the workgroup.
    
    This is related to :data:`GroupThreadIndex` and :data:`DispatchThreadIndex`.
    """
    
    GroupSize = 13
    """
    The size of a workgroup, giving the number of threads in each dimension.
    """
    
    GroupFlatIndex = 14
    """
    An input in compute shaders giving a flat 1D index of the thread within the current workgroup.
    This index increments first in the ``X`` dimension, then in the ``Y`` dimension, then in the ``Z``
    dimension.
    """
    
    GroupThreadIndex = 15
    """
    An input in compute shaders giving a 3D index of this thread within its workgroup, up to the
    workgroup size.
    
    The input does not vary between one thread in a workgroup and the same thread in another
    workgroup.
    
    This is related to :data:`GroupIndex` and :data:`DispatchThreadIndex`.
    """
    
    GSInstanceIndex = 16
    """
    An input to the geometry shader giving the instance being run, if the geometry shader was setup to
    be invoked multiple times for each input primitive.
    """
    
    OutputControlPointIndex = 17
    """
    An input to the tessellation control or hull shader giving the output control point index or patch
    vertex being operated on.
    """
    
    DomainLocation = 18
    """
    An input to the tessellation evaluation or domain shader, giving the normalised location on the
    output patch where evaluation is occurring. E.g. for triangle output this is the barycentric
    co-ordinates of the output vertex.
    """
    
    IsFrontFace = 19
    """
    An input to the pixel shader indicating whether or not the contributing triangle was considered
    front-facing or not according to the API setup for winding order and backface orientation.
    """
    
    MSAACoverage = 20
    """
    An input or an output from the pixel shader. As an input, it specifies a bitmask of which samples
    in a pixel were covered by the rasterizer. As an output, it specifies which samples in the
    destination target should be updated.
    """
    
    MSAASamplePosition = 21
    """
    An input to the pixel shader that contains the location of the current sample relative to the
    pixel, when running the pixel shader at sample frequency.
    """
    
    MSAASampleIndex = 22
    """
    An input to the pixel shader that indicates which sample in the range ``0 .. N-1`` is currently
    being processed.
    """
    
    PatchNumVertices = 23
    """
    An input to the tessellation stages, this gives the number of vertices in each patch.
    """
    
    OuterTessFactor = 24
    """
    An output from the tessellation control or hull shader, this determines the level to which the
    outer edge of each primitive is tessellated by the fixed-function tessellator.
    
    It is also available for reading in the tessellation evaluation or domain shader.
    """
    
    InsideTessFactor = 25
    """
    Related to :data:`OuterTessFactor` this functions in the same way to determine the tessellation
    level inside the primitive.
    """
    
    ColorOutput = 26
    """
    An output from the pixel shader, this determines the color value written to the corresponding
    target. There will be as many color output built-ins as there are targets bound.
    """
    
    DepthOutput = 27
    """
    An output from the pixel shader, writes the depth of this pixel with no restrictions.
    
    Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutputLessEqual`.
    """
    
    DepthOutputGreaterEqual = 28
    """
    An output from the pixel shader, writes the depth of this pixel with the restriction that it will
    be greater than or equal to the original depth produced by the rasterizer.
    
    Related to :data:`DepthOutput` and :data:`DepthOutputLessEqual`.
    """
    
    DepthOutputLessEqual = 29
    """
    An output from the pixel shader, writes the depth of this pixel with the restriction that it will
    be less than or equal to the original depth produced by the rasterizer.
    
    Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutput`.
    """
    
    BaseVertex = 30
    """
    The first vertex processed in this draw, as specified by the ``firstVertex`` / ``baseVertex``
    parameter to the draw call.
    """
    
    BaseInstance = 31
    """
    The first instance processed in this draw call, as specified by the ``firstInstance`` parameter.
    """
    
    DrawIndex = 32
    """
    For indirect or multi-draw commands, the index of this draw call within the overall draw command.
    """
    
    StencilReference = 33
    """
    The stencil reference to be used for stenciling operations on this fragment.
    """
    
    PointCoord = 34
    """
    The fragments co-ordinates within a point primitive being rasterized.
    """
    
    IsHelper = 35
    """
    Indicates if the current invocation is a helper invocation.
    """
    
    SubgroupSize = 36
    """
    The number of invocations in a subgroup.
    """
    
    NumSubgroups = 37
    """
    The number of subgroups in the local workgroup.
    """
    
    SubgroupIndexInWorkgroup = 38
    """
    The index of the current subgroup within all subgroups in the workgroup, up to
    :data:`NumSubgroups` - 1.
    """
    
    IndexInSubgroup = 39
    """
    The index of the current thread in the current subgroup, up to :data:`SubgroupSize` - 1.
    """
    
    SubgroupEqualMask = 40
    """
    A bitmask where the bit corresponding to :data:`IndexInSubgroup` is set.
    """
    
    SubgroupGreaterEqualMask = 41
    """
    A bitmask where all bits greater or equal to the one corresponding to :data:`IndexInSubgroup` are
    set.
    """
    
    SubgroupGreaterMask = 42
    """
    A bitmask where all bits greater than the one corresponding to :data:`IndexInSubgroup` are set.
    """
    
    SubgroupLessEqualMask = 43
    """
    A bitmask where all bits less or equal to the one corresponding to :data:`IndexInSubgroup` are
    set.
    """
    
    SubgroupLessMask = 44
    """
    A bitmask where all bits less than the one corresponding to :data:`IndexInSubgroup` are set.
    """
    
    DeviceIndex = 45
    """
    The device index executing the shader, relative to the current device group.
    """
    
    IsFullyCovered = 46
    """
    Indicates if the current fragment area is fully covered by the generating primitive.
    """
    
    FragAreaSize = 47
    """
    Gives the dimensions of the area that the fragment covers.
    """
    
    FragInvocationCount = 48
    """
    Gives the maximum number of invocations for the fragment being covered.
    """
    
    PackedFragRate = 49
    """
    Contains the packed shading rate, with an API specific packing of X and Y. For example:
    
    1x being 0, 2x being 1, 4x being 2. Then the lower two bits being the Y rate and the next 2 bits
    being the X rate.
    """
    
    Barycentrics = 50
    """
    Contains the barycentric co-ordinates.
    """
    
    CullPrimitive = 51
    """
    An output to indicate whether or not a primitive should be culled.
    """
    
    OutputIndices = 52
    """
    An output containing the indices for a meshlet.
    """
    
    MultiViewIndex = 53
    """
    An input specifying the view being rendered to in multiview rendering. Only valid when multiview rendering is enabled.
    """
    
    Count = 54
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

ShaderBuiltin.Undefined.__doc__ = """
Undefined built-in or no built-in is attached to this shader variable.
"""

ShaderBuiltin.Position.__doc__ = """
As an output from the final vertex processing shader stage, this feeds the vertex position to the
rasterized. As an input to the pixel shader stage this receives the position from the rasterizer.
"""

ShaderBuiltin.PointSize.__doc__ = """
An output that controls the size of point primitives.
"""

ShaderBuiltin.ClipDistance.__doc__ = """
An output for the distance to a user-defined clipping plane. Any pixel with an interpolated value
that is negative will not be rasterized. Typically there can be more than one such output.
"""

ShaderBuiltin.CullDistance.__doc__ = """
An output for the distance to a user-defined culling plane. Any primitive with all vertices having
negative values will not be rasterized. Typically there can be more than one such output.
"""

ShaderBuiltin.RTIndex.__doc__ = """
An output for selecting the render target index in an array to render to. Available in geometry
shaders and possibly earlier stages depending on hardware/API capability.
"""

ShaderBuiltin.ViewportIndex.__doc__ = """
An output for selecting the viewport index to render to. Available in geometry shaders and
possibly earlier stages depending on hardware/API capability.
"""

ShaderBuiltin.VertexIndex.__doc__ = """
An input to the vertex shader listing the vertex index. The exact meaning of this index can vary
by API but generally it refers to either a 0-based counter for non-indexed draws, or the index
value for indexed draws. It may or may not be affected by offsets, depending on API semantics.
"""

ShaderBuiltin.PrimitiveIndex.__doc__ = """
A built-in indicating which primitive is being processed. This can be read by all primitive stages
after the vertex shader, and written by the geometry shader.
"""

ShaderBuiltin.InstanceIndex.__doc__ = """
This built-in is defined similar to :data:`VertexIndex` but for instances within an instanced
drawcall. It counts from 0 and as with :data:`VertexIndex` it may or may not be affected by
drawcall offsets.
"""

ShaderBuiltin.DispatchSize.__doc__ = """
An input in compute shaders that gives the number of workgroups executed by the dispatch call.
"""

ShaderBuiltin.DispatchThreadIndex.__doc__ = """
An input in compute shaders giving a 3D shared index across all workgroups, such that the index
varies across each thread in the workgroup up to its size, then the indices for workgroup
``(0,0,1)`` begin adjacent to where workgroup ``(0,0,0)`` ended.

This is related to :data:`GroupThreadIndex` and :data:`GroupIndex`.
"""

ShaderBuiltin.GroupIndex.__doc__ = """
An input in compute shaders giving a 3D index of this current workgroup among all workgroups,
up to the dispatch size.

The index is constant across all threads in the workgroup.

This is related to :data:`GroupThreadIndex` and :data:`DispatchThreadIndex`.
"""

ShaderBuiltin.GroupSize.__doc__ = """
The size of a workgroup, giving the number of threads in each dimension.
"""

ShaderBuiltin.GroupFlatIndex.__doc__ = """
An input in compute shaders giving a flat 1D index of the thread within the current workgroup.
This index increments first in the ``X`` dimension, then in the ``Y`` dimension, then in the ``Z``
dimension.
"""

ShaderBuiltin.GroupThreadIndex.__doc__ = """
An input in compute shaders giving a 3D index of this thread within its workgroup, up to the
workgroup size.

The input does not vary between one thread in a workgroup and the same thread in another
workgroup.

This is related to :data:`GroupIndex` and :data:`DispatchThreadIndex`.
"""

ShaderBuiltin.GSInstanceIndex.__doc__ = """
An input to the geometry shader giving the instance being run, if the geometry shader was setup to
be invoked multiple times for each input primitive.
"""

ShaderBuiltin.OutputControlPointIndex.__doc__ = """
An input to the tessellation control or hull shader giving the output control point index or patch
vertex being operated on.
"""

ShaderBuiltin.DomainLocation.__doc__ = """
An input to the tessellation evaluation or domain shader, giving the normalised location on the
output patch where evaluation is occurring. E.g. for triangle output this is the barycentric
co-ordinates of the output vertex.
"""

ShaderBuiltin.IsFrontFace.__doc__ = """
An input to the pixel shader indicating whether or not the contributing triangle was considered
front-facing or not according to the API setup for winding order and backface orientation.
"""

ShaderBuiltin.MSAACoverage.__doc__ = """
An input or an output from the pixel shader. As an input, it specifies a bitmask of which samples
in a pixel were covered by the rasterizer. As an output, it specifies which samples in the
destination target should be updated.
"""

ShaderBuiltin.MSAASamplePosition.__doc__ = """
An input to the pixel shader that contains the location of the current sample relative to the
pixel, when running the pixel shader at sample frequency.
"""

ShaderBuiltin.MSAASampleIndex.__doc__ = """
An input to the pixel shader that indicates which sample in the range ``0 .. N-1`` is currently
being processed.
"""

ShaderBuiltin.PatchNumVertices.__doc__ = """
An input to the tessellation stages, this gives the number of vertices in each patch.
"""

ShaderBuiltin.OuterTessFactor.__doc__ = """
An output from the tessellation control or hull shader, this determines the level to which the
outer edge of each primitive is tessellated by the fixed-function tessellator.

It is also available for reading in the tessellation evaluation or domain shader.
"""

ShaderBuiltin.InsideTessFactor.__doc__ = """
Related to :data:`OuterTessFactor` this functions in the same way to determine the tessellation
level inside the primitive.
"""

ShaderBuiltin.ColorOutput.__doc__ = """
An output from the pixel shader, this determines the color value written to the corresponding
target. There will be as many color output built-ins as there are targets bound.
"""

ShaderBuiltin.DepthOutput.__doc__ = """
An output from the pixel shader, writes the depth of this pixel with no restrictions.

Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutputLessEqual`.
"""

ShaderBuiltin.DepthOutputGreaterEqual.__doc__ = """
An output from the pixel shader, writes the depth of this pixel with the restriction that it will
be greater than or equal to the original depth produced by the rasterizer.

Related to :data:`DepthOutput` and :data:`DepthOutputLessEqual`.
"""

ShaderBuiltin.DepthOutputLessEqual.__doc__ = """
An output from the pixel shader, writes the depth of this pixel with the restriction that it will
be less than or equal to the original depth produced by the rasterizer.

Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutput`.
"""

ShaderBuiltin.BaseVertex.__doc__ = """
The first vertex processed in this draw, as specified by the ``firstVertex`` / ``baseVertex``
parameter to the draw call.
"""

ShaderBuiltin.BaseInstance.__doc__ = """
The first instance processed in this draw call, as specified by the ``firstInstance`` parameter.
"""

ShaderBuiltin.DrawIndex.__doc__ = """
For indirect or multi-draw commands, the index of this draw call within the overall draw command.
"""

ShaderBuiltin.StencilReference.__doc__ = """
The stencil reference to be used for stenciling operations on this fragment.
"""

ShaderBuiltin.PointCoord.__doc__ = """
The fragments co-ordinates within a point primitive being rasterized.
"""

ShaderBuiltin.IsHelper.__doc__ = """
Indicates if the current invocation is a helper invocation.
"""

ShaderBuiltin.SubgroupSize.__doc__ = """
The number of invocations in a subgroup.
"""

ShaderBuiltin.NumSubgroups.__doc__ = """
The number of subgroups in the local workgroup.
"""

ShaderBuiltin.SubgroupIndexInWorkgroup.__doc__ = """
The index of the current subgroup within all subgroups in the workgroup, up to
:data:`NumSubgroups` - 1.
"""

ShaderBuiltin.IndexInSubgroup.__doc__ = """
The index of the current thread in the current subgroup, up to :data:`SubgroupSize` - 1.
"""

ShaderBuiltin.SubgroupEqualMask.__doc__ = """
A bitmask where the bit corresponding to :data:`IndexInSubgroup` is set.
"""

ShaderBuiltin.SubgroupGreaterEqualMask.__doc__ = """
A bitmask where all bits greater or equal to the one corresponding to :data:`IndexInSubgroup` are
set.
"""

ShaderBuiltin.SubgroupGreaterMask.__doc__ = """
A bitmask where all bits greater than the one corresponding to :data:`IndexInSubgroup` are set.
"""

ShaderBuiltin.SubgroupLessEqualMask.__doc__ = """
A bitmask where all bits less or equal to the one corresponding to :data:`IndexInSubgroup` are
set.
"""

ShaderBuiltin.SubgroupLessMask.__doc__ = """
A bitmask where all bits less than the one corresponding to :data:`IndexInSubgroup` are set.
"""

ShaderBuiltin.DeviceIndex.__doc__ = """
The device index executing the shader, relative to the current device group.
"""

ShaderBuiltin.IsFullyCovered.__doc__ = """
Indicates if the current fragment area is fully covered by the generating primitive.
"""

ShaderBuiltin.FragAreaSize.__doc__ = """
Gives the dimensions of the area that the fragment covers.
"""

ShaderBuiltin.FragInvocationCount.__doc__ = """
Gives the maximum number of invocations for the fragment being covered.
"""

ShaderBuiltin.PackedFragRate.__doc__ = """
Contains the packed shading rate, with an API specific packing of X and Y. For example:

1x being 0, 2x being 1, 4x being 2. Then the lower two bits being the Y rate and the next 2 bits
being the X rate.
"""

ShaderBuiltin.Barycentrics.__doc__ = """
Contains the barycentric co-ordinates.
"""

ShaderBuiltin.CullPrimitive.__doc__ = """
An output to indicate whether or not a primitive should be culled.
"""

ShaderBuiltin.OutputIndices.__doc__ = """
An output containing the indices for a meshlet.
"""

ShaderBuiltin.MultiViewIndex.__doc__ = """
An input specifying the view being rendered to in multiview rendering. Only valid when multiview rendering is enabled.
"""

ShaderBuiltin.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

ShaderBuiltin.First.__doc__ = """
The first enum value, for ease of iteration.
"""

