from ._ColorBlend import ColorBlend
from typing import List, Tuple

from typing import overload

class VKColorBlendState():
    # Original docstring
    """
    Describes the pipeline blending state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKColorBlendState.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKColorBlendState'):
        """
        Construct a new VKColorBlendState with a deep copy of the input.
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
    
    @property
    def alphaToCoverageEnable(self) -> bool:
        """
        ``True`` if alpha-to-coverage should be used when blending to an MSAA target.
        
        :type: bool
        """
        pass
    
    @alphaToCoverageEnable.setter
    def alphaToCoverageEnable(self, value: bool):
        pass
    
    @property
    def alphaToOneEnable(self) -> bool:
        """
        ``True`` if alpha-to-one should be used when blending to an MSAA target.
        
        :type: bool
        """
        pass
    
    @alphaToOneEnable.setter
    def alphaToOneEnable(self, value: bool):
        pass
    
