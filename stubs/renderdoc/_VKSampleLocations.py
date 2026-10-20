from ._FloatVector import FloatVector
from typing import List

from typing import overload

class VKSampleLocations():
    # Original docstring
    """
    Describes state of custom sample locations in the pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKSampleLocations.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKSampleLocations'):
        """
        Construct a new VKSampleLocations with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def gridHeight(self) -> int:
        """
        The height in pixels of the region configured.
        
        :type: int
        """
        pass
    
    @gridHeight.setter
    def gridHeight(self, value: int):
        pass
    
    @property
    def customLocations(self) -> List[FloatVector]:
        """
        The custom sample locations. Only x and y are valid, z and w are set to 0.0.
        
        If the list is empty then the standard sample pattern is in use.
        
        :type: List[FloatVector]
        """
        pass
    
    @customLocations.setter
    def customLocations(self, value: List[FloatVector]):
        pass
    
    @property
    def gridWidth(self) -> int:
        """
        The width in pixels of the region configured.
        
        :type: int
        """
        pass
    
    @gridWidth.setter
    def gridWidth(self, value: int):
        pass
    
