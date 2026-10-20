from ._GLBlendState import GLBlendState
from ._GLFBO import GLFBO

from typing import overload

class GLFrameBuffer():
    # Original docstring
    """
    Describes the current state of the framebuffer stage of the pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLFrameBuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLFrameBuffer'):
        """
        Construct a new GLFrameBuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def framebufferSRGB(self) -> bool:
        """
        ``True`` if sRGB correction should be applied when writing to an sRGB-formatted texture.
        
        :type: bool
        """
        pass
    
    @framebufferSRGB.setter
    def framebufferSRGB(self, value: bool):
        pass
    
    @property
    def drawFBO(self) -> GLFBO:
        """
        The draw framebuffer.
        
        :type: GLFBO
        """
        pass
    
    @drawFBO.setter
    def drawFBO(self, value: GLFBO):
        pass
    
    @property
    def dither(self) -> bool:
        """
        ``True`` if dithering should be used when writing to color buffers.
        
        :type: bool
        """
        pass
    
    @dither.setter
    def dither(self, value: bool):
        pass
    
    @property
    def blendState(self) -> GLBlendState:
        """
        The details of the blending state.
        
        :type: GLBlendState
        """
        pass
    
    @blendState.setter
    def blendState(self, value: GLBlendState):
        pass
    
    @property
    def readFBO(self) -> GLFBO:
        """
        The read framebuffer.
        
        :type: GLFBO
        """
        pass
    
    @readFBO.setter
    def readFBO(self, value: GLFBO):
        pass
    
