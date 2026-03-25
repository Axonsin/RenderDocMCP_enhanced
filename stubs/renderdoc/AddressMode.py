# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class AddressMode(__enum.IntEnum):
    """
    A texture addressing mode in a single direction (U,V or W).
    
    .. data:: Wrap
    
      The texture is tiled at every multiple of 1.0.
    
    .. data:: Repeat
    
      Alias of :data:`Wrap`.
    
    .. data:: Mirror
    
      The texture is tiled as with :data:`Wrap`, but with the absolute value of the texture co-ordinate.
    
    .. data:: MirrorRepeat
    
      Alias of :data:`Mirror`.
    
    .. data:: MirrorOnce
    
      The texture is mirrored with :data:`Mirror`, but the texture does not tile as with
      :data:`ClampEdge`.
    
    .. data:: MirrorClamp
    
      Alias of :data:`MirrorOnce`.
    
    .. data:: ClampEdge
    
      The texture is clamped to the range of ``[0.0, 1.0]`` and the texture value at each end used.
    
    .. data:: ClampBorder
    
      The texture is clamped such that texture co-ordinates outside the range of ``[0.0, 1.0]`` are set
      to the border color specified in the sampler.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    ClampBorder = 4
    """
    The texture is clamped such that texture co-ordinates outside the range of ``[0.0, 1.0]`` are set
      to the border color specified in the sampler.
    """

    ClampEdge = 3
    """ The texture is clamped to the range of ``[0.0, 1.0]`` and the texture value at each end used. """

    Mirror = 1
    """ The texture is tiled as with :data:`Wrap`, but with the absolute value of the texture co-ordinate. """

    MirrorClamp = 2
    """ Alias of :data:`MirrorOnce`. """

    MirrorOnce = 2
    """
    The texture is mirrored with :data:`Mirror`, but the texture does not tile as with
      :data:`ClampEdge`.
    """

    MirrorRepeat = 1
    """ Alias of :data:`Mirror`. """

    Repeat = 0
    """ Alias of :data:`Wrap`. """

    Wrap = 0
    """ The texture is tiled at every multiple of 1.0. """



