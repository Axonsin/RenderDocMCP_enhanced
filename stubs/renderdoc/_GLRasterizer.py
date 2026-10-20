from ._GLRasterizerState import GLRasterizerState
from ._Scissor import Scissor
from ._Viewport import Viewport
from typing import List

from typing import overload

class GLRasterizer():
    # Original docstring
    """
    Describes the rasterization state of the OpenGL pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLRasterizer.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLRasterizer'):
        """
        Construct a new GLRasterizer with a deep copy of the input.
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
    def state(self) -> GLRasterizerState:
        """
        The details of the rasterization state.
        
        :type: GLRasterizerState
        """
        pass
    
    @state.setter
    def state(self, value: GLRasterizerState):
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
    
