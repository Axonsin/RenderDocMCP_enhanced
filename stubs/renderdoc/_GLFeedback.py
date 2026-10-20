from ._ResourceId import ResourceId
from typing import Tuple

from typing import overload

class GLFeedback():
    # Original docstring
    """
    Describes the current feedback state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLFeedback.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLFeedback'):
        """
        Construct a new GLFeedback with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def feedbackResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the transform feedback binding.
        
        :type: ResourceId
        """
        pass
    
    @feedbackResourceId.setter
    def feedbackResourceId(self, value: ResourceId):
        pass
    
    @property
    def bufferResourceId(self) -> Tuple[ResourceId, ResourceId, ResourceId, ResourceId]:
        """
        The buffer bindings.
        
        :type: Tuple[ResourceId,ResourceId,ResourceId,ResourceId]
        """
        pass
    
    @bufferResourceId.setter
    def bufferResourceId(self, value: Tuple[ResourceId, ResourceId, ResourceId, ResourceId]):
        pass
    
    @property
    def active(self) -> bool:
        """
        ``True`` if the transform feedback object is currently active.
        
        :type: bool
        """
        pass
    
    @active.setter
    def active(self, value: bool):
        pass
    
    @property
    def byteOffset(self) -> Tuple[int, int, int, int]:
        """
        The buffer byte offsets.
        
        :type: Tuple[int,int,int,int]
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: Tuple[int, int, int, int]):
        pass
    
    @property
    def byteSize(self) -> Tuple[int, int, int, int]:
        """
        The buffer byte sizes.
        
        :type: Tuple[int,int,int,int]
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: Tuple[int, int, int, int]):
        pass
    
    @property
    def paused(self) -> bool:
        """
        ``True`` if the transform feedback object is currently paused.
        
        :type: bool
        """
        pass
    
    @paused.setter
    def paused(self, value: bool):
        pass
    
