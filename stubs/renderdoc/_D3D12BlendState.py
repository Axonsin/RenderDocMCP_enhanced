from ._ColorBlend import ColorBlend
from typing import List, Tuple

from typing import overload

class D3D12BlendState():
    # Original docstring
    """
    Describes the blend state in the PSO.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12BlendState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12BlendState'):
        """
        Construct a new D3D12BlendState with a deep copy of the input.
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
    def independentBlend(self) -> bool:
        """
        ``True`` if independent blending for each target should be used.
        
        ``False`` if the first blend should be applied to all targets.
        
        :type: bool
        """
        pass
    
    @independentBlend.setter
    def independentBlend(self, value: bool):
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
    def alphaToCoverage(self) -> bool:
        """
        ``True`` if alpha-to-coverage should be used when blending to an MSAA target.
        
        :type: bool
        """
        pass
    
    @alphaToCoverage.setter
    def alphaToCoverage(self, value: bool):
        pass
    
