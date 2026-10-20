from ._CompareFunction import CompareFunction
from ._ResourceId import ResourceId
from ._StencilFace import StencilFace

from typing import overload

class D3D11DepthStencilState():
    # Original docstring
    """
    Describes a depth-stencil state object.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11DepthStencilState.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11DepthStencilState'):
        """
        Construct a new D3D11DepthStencilState with a deep copy of the input.
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
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the depth-stencil state object.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
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
    
