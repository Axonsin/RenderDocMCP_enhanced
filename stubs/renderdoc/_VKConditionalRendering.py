from ._ResourceId import ResourceId

from typing import overload

class VKConditionalRendering():
    # Original docstring
    """
    Contains the current conditional rendering state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKConditionalRendering.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKConditionalRendering'):
        """
        Construct a new VKConditionalRendering with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def isInverted(self) -> bool:
        """
        ``True`` if predicate result is inverted.
        
        :type: bool
        """
        pass
    
    @isInverted.setter
    def isInverted(self, value: bool):
        pass
    
    @property
    def bufferId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the buffer containing the predicate for conditional rendering.
        
        :type: ResourceId
        """
        pass
    
    @bufferId.setter
    def bufferId(self, value: ResourceId):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset into buffer where the predicate is located.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def isPassing(self) -> bool:
        """
        ``True`` if the current predicate would render.
        
        :type: bool
        """
        pass
    
    @isPassing.setter
    def isPassing(self, value: bool):
        pass
    
