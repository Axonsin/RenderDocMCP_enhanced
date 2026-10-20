from ._ColorBlend import ColorBlend
from typing import List, Tuple

from typing import overload

class GLBlendState():
    # Original docstring
    """
    Describes the blend pipeline state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLBlendState.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLBlendState'):
        """
        Construct a new GLBlendState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def blends(self) -> List[ColorBlend]:
        """
        The blend operations for each target.
        
        :type: List[ColorBlend]
        """
        pass
    
    @blends.setter
    def blends(self, value: List[ColorBlend]):
        pass
    
    @property
    def blendFactor(self) -> Tuple[float, float, float, float]:
        """
        The constant blend factor to use in blend equations.
        
        :type: Tuple[float,float,float,float]
        """
        pass
    
    @blendFactor.setter
    def blendFactor(self, value: Tuple[float, float, float, float]):
        pass
    
