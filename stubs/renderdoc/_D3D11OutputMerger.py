from ._D3D11BlendState import D3D11BlendState
from ._D3D11DepthStencilState import D3D11DepthStencilState
from ._Descriptor import Descriptor
from typing import List

from typing import overload

class D3D11OutputMerger():
    # Original docstring
    """
    Describes the current state of the output-merger stage of the D3D11 pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11OutputMerger.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11OutputMerger'):
        """
        Construct a new D3D11OutputMerger with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def depthStencilState(self) -> D3D11DepthStencilState:
        """
        The current depth-stencil state details.
        
        :type: D3D11DepthStencilState
        """
        pass
    
    @depthStencilState.setter
    def depthStencilState(self, value: D3D11DepthStencilState):
        pass
    
    @property
    def depthTarget(self) -> Descriptor:
        """
        The currently bound depth-stencil target.
        
        :type: Descriptor
        """
        pass
    
    @depthTarget.setter
    def depthTarget(self, value: Descriptor):
        pass
    
    @property
    def depthReadOnly(self) -> bool:
        """
        ``True`` if depth access to the depth-stencil target is read-only.
        
        :type: bool
        """
        pass
    
    @depthReadOnly.setter
    def depthReadOnly(self, value: bool):
        pass
    
    @property
    def stencilReadOnly(self) -> bool:
        """
        ``True`` if stencil access to the depth-stencil target is read-only.
        
        :type: bool
        """
        pass
    
    @stencilReadOnly.setter
    def stencilReadOnly(self, value: bool):
        pass
    
    @property
    def uavStartSlot(self) -> int:
        """
        Which slot in the output targets is the first UAV.
        
        :type: int
        """
        pass
    
    @uavStartSlot.setter
    def uavStartSlot(self, value: int):
        pass
    
    @property
    def renderTargets(self) -> List[Descriptor]:
        """
        The bound render targets.
        
        :type: List[Descriptor]
        """
        pass
    
    @renderTargets.setter
    def renderTargets(self, value: List[Descriptor]):
        pass
    
    @property
    def blendState(self) -> D3D11BlendState:
        """
        The current blend state details.
        
        :type: D3D11BlendState
        """
        pass
    
    @blendState.setter
    def blendState(self, value: D3D11BlendState):
        pass
    
