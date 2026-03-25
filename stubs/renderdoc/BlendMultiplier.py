# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BlendMultiplier(__enum.IntEnum):
    """
    A multiplier on one component in the blend equation.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "second source" value is provided when dual source blending is used.
    
      The "destination" value is the value in the target being blended to.
    
      These values are combined using a given blend operation, see :class:`BlendOperation`.
    
      Where a color is referenced, the value depends on where the multiplier appears in the blend
      equation. If it is a multiplier on the color component then it refers to the color component. If
      it is a multiplier on the alpha component then it refers to the alpha component.
    
      If alpha is referenced explicitly it always refers to alpha, in both color and alpha equations.
    
    .. data:: Zero
    
      The literal value ``0.0``.
    
    .. data:: One
    
      The literal value ``1.0``.
    
    .. data:: SrcCol
    
      The source value's color.
    
    .. data:: InvSrcCol
    
      ``1.0`` minus the source value's color.
    
    .. data:: DstCol
    
      The destination value's color.
    
    .. data:: InvDstCol
    
      ``1.0`` minus the destination value's color.
    
    .. data:: SrcAlpha
    
      The source value's alpha.
    
    .. data:: InvSrcAlpha
    
      ``1.0`` minus the source value's alpha.
    
    .. data:: DstAlpha
    
      The destination value's alpha.
    
    .. data:: InvDstAlpha
    
      ``1.0`` minus the destination value's alpha.
    
    .. data:: SrcAlphaSat
    
      The lowest value of :data:`SrcAlpha` and :data:`InvDstAlpha`. If used in the alpha equation, it takes the value :data:`One`.
    
    .. data:: FactorRGB
    
      The color components of the fixed blend factor constant.
    
    .. data:: InvFactorRGB
    
      ``1.0`` minus the color components of the fixed blend factor constant.
    
    .. data:: FactorAlpha
    
      The alpha component of the fixed blend factor constant.
    
    .. data:: InvFactorAlpha
    
      ``1.0`` minus the alpha components of the fixed blend factor constant.
    
    .. data:: Src1Col
    
      The second source value's color.
    
    .. data:: InvSrc1Col
    
      ``1.0`` minus the second source value's color.
    
    .. data:: Src1Alpha
    
      The second source value's alpha.
    
    .. data:: InvSrc1Alpha
    
      ``1.0`` minus the second source value's alpha.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    DstAlpha = 8
    """ The destination value's alpha. """

    DstCol = 4
    """ The destination value's color. """

    FactorAlpha = 13
    """ The alpha component of the fixed blend factor constant. """

    FactorRGB = 11
    """ The color components of the fixed blend factor constant. """

    InvDstAlpha = 9
    """ ``1.0`` minus the destination value's alpha. """

    InvDstCol = 5
    """ ``1.0`` minus the destination value's color. """

    InvFactorAlpha = 14
    """ ``1.0`` minus the alpha components of the fixed blend factor constant. """

    InvFactorRGB = 12
    """ ``1.0`` minus the color components of the fixed blend factor constant. """

    InvSrc1Alpha = 18
    """ ``1.0`` minus the second source value's alpha. """

    InvSrc1Col = 16
    """ ``1.0`` minus the second source value's color. """

    InvSrcAlpha = 7
    """ ``1.0`` minus the source value's alpha. """

    InvSrcCol = 3
    """ ``1.0`` minus the source value's color. """

    One = 1
    """ The literal value ``1.0``. """

    Src1Alpha = 17
    """ The second source value's alpha. """

    Src1Col = 15
    """ The second source value's color. """

    SrcAlpha = 6
    """ The source value's alpha. """

    SrcAlphaSat = 10
    """ The lowest value of :data:`SrcAlpha` and :data:`InvDstAlpha`. If used in the alpha equation, it takes the value :data:`One`. """

    SrcCol = 2
    """ The source value's color. """

    Zero = 0
    """ The literal value ``0.0``. """



