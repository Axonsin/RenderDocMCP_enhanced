
from typing import overload

class VKVertexBinding():
    # Original docstring
    """
    Describes a vertex binding.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKVertexBinding.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKVertexBinding'):
        """
        Construct a new VKVertexBinding with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def vertexBufferBinding(self) -> int:
        """
        The vertex binding where data will be sourced from.
        
        :type: int
        """
        pass
    
    @vertexBufferBinding.setter
    def vertexBufferBinding(self, value: int):
        pass
    
    @property
    def instanceDivisor(self) -> int:
        """
        The instance rate divisor.
        
        If this is ``0`` then every vertex gets the same value.
        
        If it's ``1`` then one element is read for each instance, and for ``N`` greater than ``1`` then
        ``N`` instances read the same element before advancing.
        
        :type: int
        """
        pass
    
    @instanceDivisor.setter
    def instanceDivisor(self, value: int):
        pass
    
    @property
    def perInstance(self) -> bool:
        """
        ``True`` if the vertex data is instance-rate.
        
        :type: bool
        """
        pass
    
    @perInstance.setter
    def perInstance(self, value: bool):
        pass
    
