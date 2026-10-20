from ._D3D12BlendState import D3D12BlendState
from ._D3D12DepthStencilState import D3D12DepthStencilState
from ._Descriptor import Descriptor
from typing import List

from typing import overload

class D3D12OM():
    # Original docstring
    """
    Describes the current state of the output-merger stage of the D3D12 pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12OM.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12OM'):
        """
        Construct a new D3D12OM with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def depthStencilState(self) -> D3D12DepthStencilState:
        """
        The current depth-stencil state details.
        
        :type: D3D12DepthStencilState
        """
        pass
    
    @depthStencilState.setter
    def depthStencilState(self, value: D3D12DepthStencilState):
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
    def blendState(self) -> D3D12BlendState:
        """
        The current blend state details.
        
        :type: D3D12BlendState
        """
        pass
    
    @blendState.setter
    def blendState(self, value: D3D12BlendState):
        pass
    
