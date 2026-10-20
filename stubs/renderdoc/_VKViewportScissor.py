from ._Scissor import Scissor
from ._Viewport import Viewport

from typing import overload

class VKViewportScissor():
    # Original docstring
    """
    Describes a combined viewport and scissor region.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKViewportScissor.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKViewportScissor'):
        """
        Construct a new VKViewportScissor with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def vp(self) -> Viewport:
        """
        The viewport.
        
        :type: Viewport
        """
        pass
    
    @vp.setter
    def vp(self, value: Viewport):
        pass
    
    @property
    def scissor(self) -> Scissor:
        """
        The scissor.
        
        :type: Scissor
        """
        pass
    
    @scissor.setter
    def scissor(self, value: Scissor):
        pass
    
