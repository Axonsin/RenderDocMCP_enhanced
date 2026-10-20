from ._CompareFunction import CompareFunction

from typing import overload

class GLDepthState():
    # Original docstring
    """
    Describes the depth state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLDepthState.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLDepthState'):
        """
        Construct a new GLDepthState with a deep copy of the input.
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
    def nearBound(self) -> float:
        """
        The near plane bounding value.
        
        :type: float
        """
        pass
    
    @nearBound.setter
    def nearBound(self, value: float):
        pass
    
    @property
    def farBound(self) -> float:
        """
        The far plane bounding value.
        
        :type: float
        """
        pass
    
    @farBound.setter
    def farBound(self, value: float):
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
    
