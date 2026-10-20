from ._Descriptor import Descriptor
from ._ResourceId import ResourceId
from typing import List

from typing import overload

class VKFramebuffer():
    # Original docstring
    """
    Describes a framebuffer object and its attachments.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKFramebuffer.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKFramebuffer'):
        """
        Construct a new VKFramebuffer with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def attachments(self) -> List[Descriptor]:
        """
        The attachments of this framebuffer.
        
        :type: List[Descriptor]
        """
        pass
    
    @attachments.setter
    def attachments(self, value: List[Descriptor]):
        pass
    
    @property
    def height(self) -> int:
        """
        The height of this framebuffer in pixels.
        
        :type: int
        """
        pass
    
    @height.setter
    def height(self, value: int):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the framebuffer object.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def width(self) -> int:
        """
        The width of this framebuffer in pixels.
        
        :type: int
        """
        pass
    
    @width.setter
    def width(self, value: int):
        pass
    
    @property
    def layers(self) -> int:
        """
        The number of layers in this framebuffer.
        
        :type: int
        """
        pass
    
    @layers.setter
    def layers(self, value: int):
        pass
    
