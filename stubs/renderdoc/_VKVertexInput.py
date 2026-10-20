from ._VKVertexAttribute import VKVertexAttribute
from ._VKVertexBinding import VKVertexBinding
from ._VKVertexBuffer import VKVertexBuffer
from typing import List

from typing import overload

class VKVertexInput():
    # Original docstring
    """
    Describes the fixed-function vertex input fetch setup.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKVertexInput.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKVertexInput'):
        """
        Construct a new VKVertexInput with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def attributes(self) -> List[VKVertexAttribute]:
        """
        The vertex attributes.
        
        :type: List[VKVertexAttribute]
        """
        pass
    
    @attributes.setter
    def attributes(self, value: List[VKVertexAttribute]):
        pass
    
    @property
    def vertexBuffers(self) -> List[VKVertexBuffer]:
        """
        The vertex buffers.
        
        :type: List[VKVertexBuffer]
        """
        pass
    
    @vertexBuffers.setter
    def vertexBuffers(self, value: List[VKVertexBuffer]):
        pass
    
    @property
    def bindings(self) -> List[VKVertexBinding]:
        """
        The vertex bindings.
        
        :type: List[VKVertexBinding]
        """
        pass
    
    @bindings.setter
    def bindings(self, value: List[VKVertexBinding]):
        pass
    
