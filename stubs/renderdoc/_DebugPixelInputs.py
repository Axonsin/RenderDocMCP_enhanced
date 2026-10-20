
from typing import overload

class DebugPixelInputs():
    # Original docstring
    """
    Contains the properties used to select which fragment to debug, used as an input
    to :meth:`ReplayController.DebugPixel`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DebugPixelInputs.
        """
        pass
    
    @overload
    def __init__(self, other: 'DebugPixelInputs'):
        """
        Construct a new DebugPixelInputs with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def view(self) -> int:
        """
        The layered or multiview rendering view index.
        
        :type: int
        """
        pass
    
    @view.setter
    def view(self, value: int):
        pass
    
    @property
    def primitive(self) -> int:
        """
        The primitive index.
        
        :type: int
        """
        pass
    
    @primitive.setter
    def primitive(self, value: int):
        pass
    
    @property
    def sample(self) -> int:
        """
        The multi-sampled sample.
        
        :type: int
        """
        pass
    
    @sample.setter
    def sample(self, value: int):
        pass
    
