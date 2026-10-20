
from typing import overload

class VKImageLayout():
    # Original docstring
    """
    Contains the layout of a range of subresources in an image.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKImageLayout.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKImageLayout'):
        """
        Construct a new VKImageLayout with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        The name of the current image state.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def numMip(self) -> int:
        """
        The number of mip levels in the range.
        
        :type: int
        """
        pass
    
    @numMip.setter
    def numMip(self, value: int):
        pass
    
    @property
    def numLayer(self) -> int:
        """
        For 3D textures and texture arrays, the number of array slices in the range.
        
        :type: int
        """
        pass
    
    @numLayer.setter
    def numLayer(self, value: int):
        pass
    
    @property
    def baseLayer(self) -> int:
        """
        For 3D textures and texture arrays, the first slice used in the range.
        
        :type: int
        """
        pass
    
    @baseLayer.setter
    def baseLayer(self, value: int):
        pass
    
    @property
    def baseMip(self) -> int:
        """
        The first mip level used in the range.
        
        :type: int
        """
        pass
    
    @baseMip.setter
    def baseMip(self, value: int):
        pass
    
