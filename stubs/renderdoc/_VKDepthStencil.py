from ._CompareFunction import CompareFunction
from ._StencilFace import StencilFace

from typing import overload

class VKDepthStencil():
    # Original docstring
    """
    Describes the pipeline depth-stencil state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKDepthStencil.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKDepthStencil'):
        """
        Construct a new VKDepthStencil with a deep copy of the input.
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
    def depthWriteEnable(self) -> bool:
        """
        ``True`` if depth values should be written to the depth target.
        
        :type: bool
        """
        pass
    
    @depthWriteEnable.setter
    def depthWriteEnable(self, value: bool):
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
    def depthTestEnable(self) -> bool:
        """
        ``True`` if depth testing should be performed.
        
        :type: bool
        """
        pass
    
    @depthTestEnable.setter
    def depthTestEnable(self, value: bool):
        pass
    
    @property
    def stencilTestEnable(self) -> bool:
        """
        ``True`` if stencil operations should be performed.
        
        :type: bool
        """
        pass
    
    @stencilTestEnable.setter
    def stencilTestEnable(self, value: bool):
        pass
    
