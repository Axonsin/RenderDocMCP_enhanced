from ._StencilFace import StencilFace

from typing import overload

class GLStencilState():
    # Original docstring
    """
    Describes the stencil state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLStencilState.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLStencilState'):
        """
        Construct a new GLStencilState with a deep copy of the input.
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
    def stencilEnable(self) -> bool:
        """
        ``True`` if stencil operations should be performed.
        
        :type: bool
        """
        pass
    
    @stencilEnable.setter
    def stencilEnable(self, value: bool):
        pass
    
