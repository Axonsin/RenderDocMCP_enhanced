
from typing import overload

class ShaderVertexMessageLocation():
    # Original docstring
    """
    A vertex shader message's location.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderVertexMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderVertexMessageLocation'):
        """
        Construct a new ShaderVertexMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def view(self) -> int:
        """
        The multiview view for this vertex, or ``0`` if multiview is disabled.
        
        :type: int
        """
        pass
    
    @view.setter
    def view(self, value: int):
        pass
    
    @property
    def vertexIndex(self) -> int:
        """
        The vertex or index for this vertex.
        
        :type: int
        """
        pass
    
    @vertexIndex.setter
    def vertexIndex(self, value: int):
        pass
    
    @property
    def instance(self) -> int:
        """
        The instance for this vertex.
        
        :type: int
        """
        pass
    
    @instance.setter
    def instance(self, value: int):
        pass
    
