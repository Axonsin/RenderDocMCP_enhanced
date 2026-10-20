from ._ResourceFormat import ResourceFormat

from typing import overload

class VKVertexAttribute():
    # Original docstring
    """
    Describes the configuration of a single vertex attribute.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKVertexAttribute.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKVertexAttribute'):
        """
        Construct a new VKVertexAttribute with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def binding(self) -> int:
        """
        The vertex binding where data will be sourced from.
        
        :type: int
        """
        pass
    
    @binding.setter
    def binding(self, value: int):
        pass
    
    @property
    def location(self) -> int:
        """
        The location in the shader that is bound to this attribute.
        
        :type: int
        """
        pass
    
    @location.setter
    def location(self, value: int):
        pass
    
    @property
    def format(self) -> ResourceFormat:
        """
        The format describing how the input element is interpreted.
        
        :type: ResourceFormat
        """
        pass
    
    @format.setter
    def format(self, value: ResourceFormat):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of each vertex data in the :data:`binding` to this attribute.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
