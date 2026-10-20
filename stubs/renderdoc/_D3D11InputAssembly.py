from ._D3D11IndexBuffer import D3D11IndexBuffer
from ._D3D11Layout import D3D11Layout
from ._D3D11VertexBuffer import D3D11VertexBuffer
from ._ResourceId import ResourceId
from ._ShaderReflection import ShaderReflection
from ._Topology import Topology
from typing import List

from typing import overload

class D3D11InputAssembly():
    # Original docstring
    """
    Describes the input assembler data.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11InputAssembly.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11InputAssembly'):
        """
        Construct a new D3D11InputAssembly with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def bytecode(self) -> ShaderReflection:
        """
        The shader reflection for the bytecode used to create the input layout.
        
        :type: ShaderReflection
        """
        pass
    
    @bytecode.setter
    def bytecode(self, value: ShaderReflection):
        pass
    
    @property
    def layouts(self) -> List[D3D11Layout]:
        """
        The input layout elements in this layout.
        
        :type: List[D3D11Layout]
        """
        pass
    
    @layouts.setter
    def layouts(self, value: List[D3D11Layout]):
        pass
    
    @property
    def indexBuffer(self) -> D3D11IndexBuffer:
        """
        The bound index buffer.
        
        :type: D3D11IndexBuffer
        """
        pass
    
    @indexBuffer.setter
    def indexBuffer(self, value: D3D11IndexBuffer):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the layout object.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def vertexBuffers(self) -> List[D3D11VertexBuffer]:
        """
        The bound vertex buffers
        
        :type: List[D3D11VertexBuffer]
        """
        pass
    
    @vertexBuffers.setter
    def vertexBuffers(self, value: List[D3D11VertexBuffer]):
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
    
