from ._VKFramebuffer import VKFramebuffer
from ._VKRenderArea import VKRenderArea
from ._VKRenderPass import VKRenderPass

from typing import overload

class VKCurrentPass():
    # Original docstring
    """
    Describes the current pass instance at the current time.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKCurrentPass.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKCurrentPass'):
        """
        Construct a new VKCurrentPass with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def renderpass(self) -> VKRenderPass:
        """
        The renderpass and subpass that is currently active.
        
        :type: VKRenderPass
        """
        pass
    
    @renderpass.setter
    def renderpass(self, value: VKRenderPass):
        pass
    
    @property
    def framebuffer(self) -> VKFramebuffer:
        """
        The framebuffer that is currently being used.
        
        :type: VKFramebuffer
        """
        pass
    
    @framebuffer.setter
    def framebuffer(self, value: VKFramebuffer):
        pass
    
    @property
    def renderArea(self) -> VKRenderArea:
        """
        The render area that is currently being rendered to.
        
        :type: VKRenderArea
        """
        pass
    
    @renderArea.setter
    def renderArea(self, value: VKRenderArea):
        pass
    
    @property
    def colorFeedbackAllowed(self) -> bool:
        """
        If feedback loops are allowed on color attachments
        
        :type: bool
        """
        pass
    
    @colorFeedbackAllowed.setter
    def colorFeedbackAllowed(self, value: bool):
        pass
    
    @property
    def depthFeedbackAllowed(self) -> bool:
        """
        If feedback loops are allowed on depth attachments
        
        :type: bool
        """
        pass
    
    @depthFeedbackAllowed.setter
    def depthFeedbackAllowed(self, value: bool):
        pass
    
    @property
    def stencilFeedbackAllowed(self) -> bool:
        """
        If feedback loops are allowed on stencil attachments
        
        :type: bool
        """
        pass
    
    @stencilFeedbackAllowed.setter
    def stencilFeedbackAllowed(self, value: bool):
        pass
    
