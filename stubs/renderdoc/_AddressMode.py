from enum import IntEnum

class AddressMode(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    Wrap = 0
    """
    The texture is tiled at every multiple of 1.0.
    """
    
    Mirror = 1
    """
    The texture is tiled as with :data:`Wrap`, but with the absolute value of the texture co-ordinate.
    """
    
    MirrorOnce = 2
    """
    The texture is mirrored with :data:`Mirror`, but the texture does not tile as with
    :data:`ClampEdge`.
    """
    
    ClampEdge = 3
    """
    The texture is clamped to the range of ``[0.0, 1.0]`` and the texture value at each end used.
    """
    
    ClampBorder = 4
    """
    The texture is clamped such that texture co-ordinates outside the range of ``[0.0, 1.0]`` are set
    to the border color specified in the sampler.
    """
    
    # Aliases
    
    Repeat = 0
    """
    Alias of :data:`Wrap`.
    """
    
    MirrorRepeat = 1
    """
    Alias of :data:`Mirror`.
    """
    
    MirrorClamp = 2
    """
    Alias of :data:`MirrorOnce`.
    """
    

# Assign __doc__ for enum values for easier introspection

AddressMode.Wrap.__doc__ = """
The texture is tiled at every multiple of 1.0.
"""

AddressMode.Mirror.__doc__ = """
The texture is tiled as with :data:`Wrap`, but with the absolute value of the texture co-ordinate.
"""

AddressMode.MirrorOnce.__doc__ = """
The texture is mirrored with :data:`Mirror`, but the texture does not tile as with
:data:`ClampEdge`.
"""

AddressMode.ClampEdge.__doc__ = """
The texture is clamped to the range of ``[0.0, 1.0]`` and the texture value at each end used.
"""

AddressMode.ClampBorder.__doc__ = """
The texture is clamped such that texture co-ordinates outside the range of ``[0.0, 1.0]`` are set
to the border color specified in the sampler.
"""

AddressMode.Repeat.__doc__ = """
Alias of :data:`Wrap`.
"""

AddressMode.MirrorRepeat.__doc__ = """
Alias of :data:`Mirror`.
"""

AddressMode.MirrorClamp.__doc__ = """
Alias of :data:`MirrorOnce`.
"""

