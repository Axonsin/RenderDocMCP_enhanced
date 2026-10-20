from ._Descriptor import Descriptor
from ._ResourceId import ResourceId
from typing import List

from typing import overload

class GLFBO():
    # Original docstring
    """
    Describes the contents of a framebuffer object.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLFBO.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLFBO'):
        """
        Construct a new GLFBO with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def colorAttachments(self) -> List[Descriptor]:
        """
        The framebuffer color attachments.
        
        :type: List[Descriptor]
        """
        pass
    
    @colorAttachments.setter
    def colorAttachments(self, value: List[Descriptor]):
        pass
    
    @property
    def readBuffer(self) -> int:
        """
        The read buffer index in the :data:`colorAttachments` attachment list.
        
        :type: int
        """
        pass
    
    @readBuffer.setter
    def readBuffer(self, value: int):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the framebuffer.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def drawBuffers(self) -> List[int]:
        """
        The draw buffer indices into the :data:`colorAttachments` attachment list.
        
        :type: List[int]
        """
        pass
    
    @drawBuffers.setter
    def drawBuffers(self, value: List[int]):
        pass
    
    @property
    def depthAttachment(self) -> Descriptor:
        """
        The framebuffer depth attachment.
        
        :type: Descriptor
        """
        pass
    
    @depthAttachment.setter
    def depthAttachment(self, value: Descriptor):
        pass
    
    @property
    def stencilAttachment(self) -> Descriptor:
        """
        The framebuffer stencil attachment.
        
        :type: Descriptor
        """
        pass
    
    @stencilAttachment.setter
    def stencilAttachment(self, value: Descriptor):
        pass
    
