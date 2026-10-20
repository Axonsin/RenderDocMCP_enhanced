from ._CompareFunction import CompareFunction

from typing import overload

class DepthTestState():
    # Original docstring
    """
    Describes a common subset of depth testing state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DepthTestState.
        """
        pass
    
    @overload
    def __init__(self, other: 'DepthTestState'):
        """
        Construct a new DepthTestState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def depthBounds(self) -> bool:
        """
        ``True`` if depth bounds tests should be applied.
        
        :type: bool
        """
        pass
    
    @depthBounds.setter
    def depthBounds(self, value: bool):
        pass
    
    @property
    def minDepthBounds(self) -> float:
        """
        The near plane bounding value.
        
        :type: float
        """
        pass
    
    @minDepthBounds.setter
    def minDepthBounds(self, value: float):
        pass
    
    @property
    def maxDepthBounds(self) -> float:
        """
        The far plane bounding value.
        
        :type: float
        """
        pass
    
    @maxDepthBounds.setter
    def maxDepthBounds(self, value: float):
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
    
