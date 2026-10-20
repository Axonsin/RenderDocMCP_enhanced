from ._D3D11RasterizerState import D3D11RasterizerState
from ._Scissor import Scissor
from ._Viewport import Viewport
from typing import List

from typing import overload

class D3D11Rasterizer():
    # Original docstring
    """
    Describes the rasterization state of the D3D11 pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11Rasterizer.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11Rasterizer'):
        """
        Construct a new D3D11Rasterizer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def scissors(self) -> List[Scissor]:
        """
        The bound scissor regions.
        
        :type: List[Scissor]
        """
        pass
    
    @scissors.setter
    def scissors(self, value: List[Scissor]):
        pass
    
    @property
    def state(self) -> D3D11RasterizerState:
        """
        The details of the rasterization state.
        
        :type: D3D11RasterizerState
        """
        pass
    
    @state.setter
    def state(self, value: D3D11RasterizerState):
        pass
    
    @property
    def viewports(self) -> List[Viewport]:
        """
        The bound viewports.
        
        :type: List[Viewport]
        """
        pass
    
    @viewports.setter
    def viewports(self, value: List[Viewport]):
        pass
    
