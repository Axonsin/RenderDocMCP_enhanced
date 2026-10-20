
from typing import overload

class TextureComponentMapping():
    # Original docstring
    """
    How to map components to normalised ``[0, 255]`` for saving to 8-bit file formats.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureComponentMapping.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureComponentMapping'):
        """
        Construct a new TextureComponentMapping with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def whitePoint(self) -> float:
        """
        The value that should be mapped to ``255``
        
        :type: float
        """
        pass
    
    @whitePoint.setter
    def whitePoint(self, value: float):
        pass
    
    @property
    def blackPoint(self) -> float:
        """
        The value that should be mapped to ``0``
        
        :type: float
        """
        pass
    
    @blackPoint.setter
    def blackPoint(self, value: float):
        pass
    
