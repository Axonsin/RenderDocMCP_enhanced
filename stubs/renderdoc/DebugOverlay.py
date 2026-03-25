# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DebugOverlay(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    BackfaceCull = 5
    """
    This overlay shows pixels from the object that passed backface culling in green, and pixels that
      were backface culled in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    """

    ClearBeforeDraw = 10
    """
    This is the same as the :data:`ClearBeforePass` overlay, except it clears before the current
      drawcall, not the current pass.
    """

    ClearBeforePass = 9
    """
    This overlay clears the bound render targets before the current pass, allowing you to see only the
      contribution from the current pass.
    
      Note only color targets are cleared, depth-stencil targets are unchanged so any depth or stencil
      tests will still pass or fail in the same way.
    """

    Clipping = 8
    """
    This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
      any pixels that are currently above the white point in green and any pixels that are below the
      black point in red.
    
      This is relative to the current black and white points used to display the texture.
    """

    Depth = 3
    """
    This overlay shows pixels from the object that passed all depth tests in green, and pixels that
      failed any depth test in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    """

    Drawcall = 1
    """
    An overlay highlighting the area rasterized by the drawcall on screen, no matter what tests or
      processes may be discarding the pixels actually rendered.
    
      The rest of the image should be dimmed slightly to make the draw on screen clearer.
    """

    NaN = 7
    """
    This overlay renders the image in greyscale using a simple luminosity calculation, then highlights
      any pixels that are ``NaN`` in red, any that are positive or negative infinity in green, and any
      that are negative in blue.
    """

    NoOverlay = 0
    """ No overlay should be rendered. """

    QuadOverdrawDraw = 12
    """
    This is the same as the :data:`QuadOverdrawPass` overlay, except it only shows the overdraw for
      the current drawcall, not the current pass.
    """

    QuadOverdrawPass = 11
    """
    This overlay shows pixel overdraw using 2x2 rasterized quad granularity instead of single-pixel
      overdraw. This represents the number of times the pixel shader was invoked along triangle edges
      even if each pixel is only overdrawn once.
    
      The overlay accounts for all draws in the current pass.
    """

    Stencil = 4
    """
    This overlay shows pixels from the object that passed all stencil tests in green, and pixels that
      failed any stencil test in red.
    
      If some pixel is overwritten more than once by the object, if any of the samples passed the result
      will be green (i.e. the failure overlay is conservative).
    """

    TriangleSizeDraw = 14
    """
    This is similar to the :data:`TriangleSizePass` overlay, except it only shows the triangle size
      for the current drawcall, not the current pass.
    """

    TriangleSizePass = 13
    """
    This overlay shows the size of each triangle, starting from triangles with area ``16 (4x4)`` and above
      at the lower end to triangles with area ``0.125 (1/8th pixel)`` at the upper end.
    
      The overlay accounts for all draws in the current pass.
    """

    ViewportScissor = 6
    """
    This overlay shows a rectangle on screen corresponding to both the current viewport, and if
      enabled the current scissor as well.
    """

    Wireframe = 2
    """
    Similar to the :data:`Drawcall` overlay, this should render over the top of the image, but showing
      the wireframe of the object instead of a solid render.
    """



