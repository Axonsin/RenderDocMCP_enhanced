from ._CompareFunction import CompareFunction
from ._StencilFace import StencilFace

from typing import overload

class D3D12DepthStencilState():
    # Original docstring
    """
    Describes the state of the depth-stencil state in the PSO.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12DepthStencilState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12DepthStencilState'):
        """
        Construct a new D3D12DepthStencilState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def frontFace(self) -> StencilFace:
        """
        The stencil state for front-facing polygons.
        
        :type: StencilFace
        """
        pass
    
    @frontFace.setter
    def frontFace(self, value: StencilFace):
        pass
    
    @property
    def backFace(self) -> StencilFace:
        """
        The stencil state for back-facing polygons.
        
        :type: StencilFace
        """
        pass
    
    @backFace.setter
    def backFace(self, value: StencilFace):
        pass
    
    @property
    def depthFunction(self) -> CompareFunction:
        """
        The :class:`CompareFunction` to use for testing depth values.
        
        :type: CompareFunction
        """
        pass
    
    @depthFunction.setter
    def depthFunction(self, value: CompareFunction):
        pass
    
    @property
    def depthBoundsEnable(self) -> bool:
        """
        ``True`` if depth bounds tests should be applied.
        
        :type: bool
        """
        pass
    
    @depthBoundsEnable.setter
    def depthBoundsEnable(self, value: bool):
        pass
    
    @property
    def minDepthBounds(self) -> float:
        """
        The near plane bounding value.
        
        :type: float
        """
        pass
    
    @minDepthBounds.setter
    def minDepthBounds(self, value: float):
        pass
    
    @property
    def maxDepthBounds(self) -> float:
        """
        The far plane bounding value.
        
        :type: float
        """
        pass
    
    @maxDepthBounds.setter
    def maxDepthBounds(self, value: float):
        pass
    
    @property
    def depthEnable(self) -> bool:
        """
        ``True`` if depth testing should be performed.
        
        :type: bool
        """
        pass
    
    @depthEnable.setter
    def depthEnable(self, value: bool):
        pass
    
    @property
    def depthWrites(self) -> bool:
        """
        ``True`` if depth values should be written to the depth target.
        
        :type: bool
        """
        pass
    
    @depthWrites.setter
    def depthWrites(self, value: bool):
        pass
    
    @property
    def stencilEnable(self) -> bool:
        """
        ``True`` if stencil operations should be performed.
        
        :type: bool
        """
        pass
    
    @stencilEnable.setter
    def stencilEnable(self, value: bool):
        pass
    
