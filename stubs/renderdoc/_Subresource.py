
from typing import overload

class Subresource():
    # Original docstring
    """
    Specifies a subresource within a texture.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Subresource.
        """
        pass
    
    @overload
    def __init__(self, other: 'Subresource'):
        """
        Construct a new Subresource with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, mip: int = 0, slice: int = 0, sample: int = 0):
        """
        Construct a new Subresource using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def slice(self) -> int:
        """
        The slice within the texture. For array textures this is an array slice. For 3D textures
        when a single depth slice can be referred to this refers to that depth slice. In some cases a 3D
        texture may not allow referring to a single depth slice - see where the Subresource is used.
        
        .. note::
          Cubemaps are simply 2D array textures with a special meaning, so the faces of a cubemap are the 2D
          array slices in the standard order: X+, X-, Y+, Y-, Z+, Z-. Cubemap arrays are 2D arrays with
          ``6 * N`` faces, where each cubemap within the array takes up 6 slices in the above order.
        
        :type: int
        """
        pass
    
    @slice.setter
    def slice(self, value: int):
        pass
    
    @property
    def sample(self) -> int:
        """
        The sample in a multisampled texture.
        
        :type: int
        """
        pass
    
    @sample.setter
    def sample(self, value: int):
        pass
    
    @property
    def mip(self) -> int:
        """
        The mip level in the texture.
        
        :type: int
        """
        pass
    
    @mip.setter
    def mip(self, value: int):
        pass
    
