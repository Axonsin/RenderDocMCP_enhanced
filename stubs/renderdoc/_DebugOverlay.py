from enum import IntEnum

class DebugOverlay(IntEnum):
    # Original docstring
    """
    The type of overlay image to render on top of an existing texture view, for debugging
    purposes.
    
    In overlays that refer to the 'current pass', for any API that does not have an explicit notion of a
    render pass, it is defined as all previous drawcalls that render to the same set of render targets.
    Note that this is defined independently from any marker regions.
    
    See :ref:`the documentation for this feature <render-overlay>`.
    
    .. data:: NoOverlay
    
      No overlay should be rendered.
    
    .. data:: Drawcall
    
      An overlay highlighting the area rasterized by the drawcall on screen, no matter what tests or
      processes may be discarding the pixels actually rendered.
    
      The rest of the image should be dimmed slightly to make the draw on screen clearer.
    
    .. data:: Wireframe
    
      Similar to the :data:`Drawcall` overlay, this should render over the top of the image, but showing
      the wireframe of the object instead of a solid render.
    
    .. data:: Depth
    
      This overlay shows pixels from the object that passed all depth tests in green, and pixels that
      failed any depth test in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    
    .. data:: Stencil
    
      This overlay shows pixels from the object that passed all stencil tests in green, and pixels that
      failed any stencil test in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    
    .. data:: BackfaceCull
    
      This overlay shows pixels from the object that passed backface culling in green, and pixels that
      were backface culled in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    
    .. data:: ViewportScissor
    
      This overlay shows a rectangle on screen corresponding to both the current viewport, and if
      enabled the current scissor as well.
    
    .. data:: NaN
    
      This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
      any pixels that are ``NaN`` in red, any that are positive or negative infinity in green, and any
      that are negative in blue.
    
    .. data:: Clipping
    
      This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
      any pixels that are currently above the white point in green and any pixels that are below the
      black point in red.
    
      This is relative to the current black and white points used to display the texture.
    
    .. data:: ClearBeforePass
    
      This overlay clears the bound render targets before the current pass, allowing you to see only the
      contribution from the current pass.
    
      Note only color targets are cleared, depth-stencil targets are unchanged so any depth or stencil
      tests will still pass or fail in the same way.
    
    .. data:: ClearBeforeDraw
    
      This is the same as the :data:`ClearBeforePass` overlay, except it clears before the current
      drawcall, not the current pass.
    
    .. data:: QuadOverdrawPass
    
      This overlay shows pixel overdraw using 2x2 rasterized quad granularity instead of single-pixel
      overdraw. This represents the number of times the pixel shader was invoked along triangle edges
      even if each pixel is only overdrawn once.
    
      The overlay accounts for all draws in the current pass.
    
    .. data:: QuadOverdrawDraw
    
      This is the same as the :data:`QuadOverdrawPass` overlay, except it only shows the overdraw for
      the current drawcall, not the current pass.
    
    .. data:: TriangleSizePass
    
      This overlay shows the size of each triangle, starting from triangles with area ``16 (4x4)`` and above
      at the lower end to triangles with area ``0.125 (1/8th pixel)`` at the upper end.
    
      The overlay accounts for all draws in the current pass.
    
    .. data:: TriangleSizeDraw
    
      This is similar to the :data:`TriangleSizePass` overlay, except it only shows the triangle size
      for the current drawcall, not the current pass.
    """
    
    
    # Enum values
    
    NoOverlay = 0
    """
    No overlay should be rendered.
    """
    
    Drawcall = 1
    """
    An overlay highlighting the area rasterized by the drawcall on screen, no matter what tests or
    processes may be discarding the pixels actually rendered.
    
    The rest of the image should be dimmed slightly to make the draw on screen clearer.
    """
    
    Wireframe = 2
    """
    Similar to the :data:`Drawcall` overlay, this should render over the top of the image, but showing
    the wireframe of the object instead of a solid render.
    """
    
    Depth = 3
    """
    This overlay shows pixels from the object that passed all depth tests in green, and pixels that
    failed any depth test in red.
    
    If some pixel is overwritten more than once by the object, if any of the samples passed the result
    will be green (i.e. the failure overlay is conservative).
    """
    
    Stencil = 4
    """
    This overlay shows pixels from the object that passed all stencil tests in green, and pixels that
    failed any stencil test in red.
    
    If some pixel is overwritten more than once by the object, if any of the samples passed the result
    will be green (i.e. the failure overlay is conservative).
    """
    
    BackfaceCull = 5
    """
    This overlay shows pixels from the object that passed backface culling in green, and pixels that
    were backface culled in red.
    
    If some pixel is overwritten more than once by the object, if any of the samples passed the result
    will be green (i.e. the failure overlay is conservative).
    """
    
    ViewportScissor = 6
    """
    This overlay shows a rectangle on screen corresponding to both the current viewport, and if
    enabled the current scissor as well.
    """
    
    NaN = 7
    """
    This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
    any pixels that are ``NaN`` in red, any that are positive or negative infinity in green, and any
    that are negative in blue.
    """
    
    Clipping = 8
    """
    This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
    any pixels that are currently above the white point in green and any pixels that are below the
    black point in red.
    
    This is relative to the current black and white points used to display the texture.
    """
    
    ClearBeforePass = 9
    """
    This overlay clears the bound render targets before the current pass, allowing you to see only the
    contribution from the current pass.
    
    Note only color targets are cleared, depth-stencil targets are unchanged so any depth or stencil
    tests will still pass or fail in the same way.
    """
    
    ClearBeforeDraw = 10
    """
    This is the same as the :data:`ClearBeforePass` overlay, except it clears before the current
    drawcall, not the current pass.
    """
    
    QuadOverdrawPass = 11
    """
    This overlay shows pixel overdraw using 2x2 rasterized quad granularity instead of single-pixel
    overdraw. This represents the number of times the pixel shader was invoked along triangle edges
    even if each pixel is only overdrawn once.
    
    The overlay accounts for all draws in the current pass.
    """
    
    QuadOverdrawDraw = 12
    """
    This is the same as the :data:`QuadOverdrawPass` overlay, except it only shows the overdraw for
    the current drawcall, not the current pass.
    """
    
    TriangleSizePass = 13
    """
    This overlay shows the size of each triangle, starting from triangles with area ``16 (4x4)`` and above
    at the lower end to triangles with area ``0.125 (1/8th pixel)`` at the upper end.
    
    The overlay accounts for all draws in the current pass.
    """
    
    TriangleSizeDraw = 14
    """
    This is similar to the :data:`TriangleSizePass` overlay, except it only shows the triangle size
    for the current drawcall, not the current pass.
    """
    

# Assign __doc__ for enum values for easier introspection

DebugOverlay.NoOverlay.__doc__ = """
No overlay should be rendered.
"""

DebugOverlay.Drawcall.__doc__ = """
An overlay highlighting the area rasterized by the drawcall on screen, no matter what tests or
processes may be discarding the pixels actually rendered.

The rest of the image should be dimmed slightly to make the draw on screen clearer.
"""

DebugOverlay.Wireframe.__doc__ = """
Similar to the :data:`Drawcall` overlay, this should render over the top of the image, but showing
the wireframe of the object instead of a solid render.
"""

DebugOverlay.Depth.__doc__ = """
This overlay shows pixels from the object that passed all depth tests in green, and pixels that
failed any depth test in red.

If some pixel is overwritten more than once by the object, if any of the samples passed the result
will be green (i.e. the failure overlay is conservative).
"""

DebugOverlay.Stencil.__doc__ = """
This overlay shows pixels from the object that passed all stencil tests in green, and pixels that
failed any stencil test in red.

If some pixel is overwritten more than once by the object, if any of the samples passed the result
will be green (i.e. the failure overlay is conservative).
"""

DebugOverlay.BackfaceCull.__doc__ = """
This overlay shows pixels from the object that passed backface culling in green, and pixels that
were backface culled in red.

If some pixel is overwritten more than once by the object, if any of the samples passed the result
will be green (i.e. the failure overlay is conservative).
"""

DebugOverlay.ViewportScissor.__doc__ = """
This overlay shows a rectangle on screen corresponding to both the current viewport, and if
enabled the current scissor as well.
"""

DebugOverlay.NaN.__doc__ = """
This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
any pixels that are ``NaN`` in red, any that are positive or negative infinity in green, and any
that are negative in blue.
"""

DebugOverlay.Clipping.__doc__ = """
This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
any pixels that are currently above the white point in green and any pixels that are below the
black point in red.

This is relative to the current black and white points used to display the texture.
"""

DebugOverlay.ClearBeforePass.__doc__ = """
This overlay clears the bound render targets before the current pass, allowing you to see only the
contribution from the current pass.

Note only color targets are cleared, depth-stencil targets are unchanged so any depth or stencil
tests will still pass or fail in the same way.
"""

DebugOverlay.ClearBeforeDraw.__doc__ = """
This is the same as the :data:`ClearBeforePass` overlay, except it clears before the current
drawcall, not the current pass.
"""

DebugOverlay.QuadOverdrawPass.__doc__ = """
This overlay shows pixel overdraw using 2x2 rasterized quad granularity instead of single-pixel
overdraw. This represents the number of times the pixel shader was invoked along triangle edges
even if each pixel is only overdrawn once.

The overlay accounts for all draws in the current pass.
"""

DebugOverlay.QuadOverdrawDraw.__doc__ = """
This is the same as the :data:`QuadOverdrawPass` overlay, except it only shows the overdraw for
the current drawcall, not the current pass.
"""

DebugOverlay.TriangleSizePass.__doc__ = """
This overlay shows the size of each triangle, starting from triangles with area ``16 (4x4)`` and above
at the lower end to triangles with area ``0.125 (1/8th pixel)`` at the upper end.

The overlay accounts for all draws in the current pass.
"""

DebugOverlay.TriangleSizeDraw.__doc__ = """
This is similar to the :data:`TriangleSizePass` overlay, except it only shows the triangle size
for the current drawcall, not the current pass.
"""

