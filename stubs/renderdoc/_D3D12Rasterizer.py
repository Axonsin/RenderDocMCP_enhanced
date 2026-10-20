from ._D3D12RasterizerState import D3D12RasterizerState
from ._Scissor import Scissor
from ._Viewport import Viewport
from typing import List

from typing import overload

class D3D12Rasterizer():
    # Original docstring
    """
    Describes the rasterization state of the D3D12 pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12Rasterizer.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12Rasterizer'):
        """
        Construct a new D3D12Rasterizer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def sampleMask(self) -> int:
        """
        The mask determining which samples are written to.
        
        :type: int
        """
        pass
    
    @sampleMask.setter
    def sampleMask(self, value: int):
        pass
    
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
    def state(self) -> D3D12RasterizerState:
        """
        The details of the rasterization state.
        
        :type: D3D12RasterizerState
        """
        pass
    
    @state.setter
    def state(self, value: D3D12RasterizerState):
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
    
