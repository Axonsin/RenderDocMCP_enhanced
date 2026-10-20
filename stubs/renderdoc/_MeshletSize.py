
from typing import overload

class MeshletSize():
    # Original docstring
    """
    The size information for a meshlet.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised MeshletSize.
        """
        pass
    
    @overload
    def __init__(self, other: 'MeshletSize'):
        """
        Construct a new MeshletSize with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def numIndices(self) -> int:
        """
        The number of indices in the meshlet.
        
        :type: int
        """
        pass
    
    @numIndices.setter
    def numIndices(self, value: int):
        pass
    
    @property
    def numVertices(self) -> int:
        """
        The number of vertices in this meshlet. This may be larger or smaller than the number
        of indices.
        
        :type: int
        """
        pass
    
    @numVertices.setter
    def numVertices(self, value: int):
        pass
    
