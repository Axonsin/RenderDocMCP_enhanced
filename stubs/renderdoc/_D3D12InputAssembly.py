from ._D3D12IndexBuffer import D3D12IndexBuffer
from ._D3D12Layout import D3D12Layout
from ._D3D12VertexBuffer import D3D12VertexBuffer
from ._Topology import Topology
from typing import List

from typing import overload

class D3D12InputAssembly():
    # Original docstring
    """
    Describes the input assembler state in the PSO.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12InputAssembly.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12InputAssembly'):
        """
        Construct a new D3D12InputAssembly with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def layouts(self) -> List[D3D12Layout]:
        """
        The input layout elements in this layout.
        
        :type: List[D3D12Layout]
        """
        pass
    
    @layouts.setter
    def layouts(self, value: List[D3D12Layout]):
        pass
    
    @property
    def indexBuffer(self) -> D3D12IndexBuffer:
        """
        The bound index buffer.
        
        :type: D3D12IndexBuffer
        """
        pass
    
    @indexBuffer.setter
    def indexBuffer(self, value: D3D12IndexBuffer):
        pass
    
    @property
    def indexStripCutValue(self) -> int:
        """
        The index value to use for cutting strips. Either ``0``, ``0xffff`` or ``0xffffffff``.
        If the value is 0, strip cutting is disabled.
        
        :type: int
        """
        pass
    
    @indexStripCutValue.setter
    def indexStripCutValue(self, value: int):
        pass
    
    @property
    def vertexBuffers(self) -> List[D3D12VertexBuffer]:
        """
        The bound vertex buffers
        
        :type: List[D3D12VertexBuffer]
        """
        pass
    
    @vertexBuffers.setter
    def vertexBuffers(self, value: List[D3D12VertexBuffer]):
        pass
    
    @property
    def topology(self) -> Topology:
        """
        The current primitive topology.
        
        :type: Topology
        """
        pass
    
    @topology.setter
    def topology(self, value: Topology):
        pass
    
