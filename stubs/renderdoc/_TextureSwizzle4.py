from ._TextureSwizzle import TextureSwizzle

from typing import overload

class TextureSwizzle4():
    # Original docstring
    """
    The four components of a texture swizzle.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureSwizzle4.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureSwizzle4'):
        """
        Construct a new TextureSwizzle4 with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def alpha(self) -> TextureSwizzle:
        """
        The alpha channel's :class:`TextureSwizzle`.
        
        :type: TextureSwizzle
        """
        pass
    
    @alpha.setter
    def alpha(self, value: TextureSwizzle):
        pass
    
    @property
    def blue(self) -> TextureSwizzle:
        """
        The blue channel's :class:`TextureSwizzle`.
        
        :type: TextureSwizzle
        """
        pass
    
    @blue.setter
    def blue(self, value: TextureSwizzle):
        pass
    
    @property
    def green(self) -> TextureSwizzle:
        """
        The green channel's :class:`TextureSwizzle`.
        
        :type: TextureSwizzle
        """
        pass
    
    @green.setter
    def green(self, value: TextureSwizzle):
        pass
    
    @property
    def red(self) -> TextureSwizzle:
        """
        The red channel's :class:`TextureSwizzle`.
        
        :type: TextureSwizzle
        """
        pass
    
    @red.setter
    def red(self, value: TextureSwizzle):
        pass
    
