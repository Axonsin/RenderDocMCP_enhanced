from ._FilterFunction import FilterFunction
from ._FilterMode import FilterMode

from typing import overload

class TextureFilter():
    # Original docstring
    """
    The details of a texture filter in a sampler.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureFilter.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureFilter'):
        """
        Construct a new TextureFilter with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def magnify(self) -> FilterMode:
        """
        The :class:`FilterMode` to use when magnifying the texture.
        
        :type: FilterMode
        """
        pass
    
    @magnify.setter
    def magnify(self, value: FilterMode):
        pass
    
    @property
    def minify(self) -> FilterMode:
        """
        The :class:`FilterMode` to use when minifying the texture.
        
        :type: FilterMode
        """
        pass
    
    @minify.setter
    def minify(self, value: FilterMode):
        pass
    
    @property
    def filter(self) -> FilterFunction:
        """
        The :class:`FilterFunction` to apply after interpolating values.
        
        :type: FilterFunction
        """
        pass
    
    @filter.setter
    def filter(self, value: FilterFunction):
        pass
    
    @property
    def mip(self) -> FilterMode:
        """
        The :class:`FilterMode` to use when interpolating between mips.
        
        :type: FilterMode
        """
        pass
    
    @mip.setter
    def mip(self, value: FilterMode):
        pass
    
