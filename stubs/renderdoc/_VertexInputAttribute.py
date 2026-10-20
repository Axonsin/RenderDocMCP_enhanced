from ._PixelValue import PixelValue
from ._ResourceFormat import ResourceFormat

from typing import overload

class VertexInputAttribute():
    # Original docstring
    """
    Information about a vertex input attribute feeding the vertex shader.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VertexInputAttribute.
        """
        pass
    
    @overload
    def __init__(self, other: 'VertexInputAttribute'):
        """
        Construct a new VertexInputAttribute with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def used(self) -> bool:
        """
        ``True`` if this attribute is enabled and used by the vertex shader.
        
        :type: bool
        """
        pass
    
    @used.setter
    def used(self, value: bool):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of this input. This may be a variable name or a semantic name.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def vertexBuffer(self) -> int:
        """
        The index of the vertex buffer used to provide this attribute.
        
        :type: int
        """
        pass
    
    @vertexBuffer.setter
    def vertexBuffer(self, value: int):
        pass
    
    @property
    def genericValue(self) -> PixelValue:
        """
        The generic value for this attribute if it has no vertex buffer bound.
        
        :type: PixelValue
        """
        pass
    
    @genericValue.setter
    def genericValue(self, value: PixelValue):
        pass
    
    @property
    def genericEnabled(self) -> bool:
        """
        ``True`` if this attribute is using :data:`genericValue` for its data.
        
        :type: bool
        """
        pass
    
    @genericEnabled.setter
    def genericEnabled(self, value: bool):
        pass
    
    @property
    def format(self) -> ResourceFormat:
        """
        The interpreted format of this attribute.
        
        :type: ResourceFormat
        """
        pass
    
    @format.setter
    def format(self, value: ResourceFormat):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of the vertex data for this VB to this attribute.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def perInstance(self) -> bool:
        """
        ``True`` if this attribute runs at instance rate.
        
        :type: bool
        """
        pass
    
    @perInstance.setter
    def perInstance(self, value: bool):
        pass
    
    @property
    def instanceRate(self) -> int:
        """
        If :data:`perInstance` is ``True``, the number of instances that source the same value
        from the vertex buffer before advancing to the next value.
        
        :type: int
        """
        pass
    
    @instanceRate.setter
    def instanceRate(self, value: int):
        pass
    
    @property
    def floatCastWrong(self) -> bool:
        """
        Only valid for attributes on OpenGL. If the attribute has been set up for integers to
        be converted to floats (``glVertexAttribFormat`` with ``GL_INT``) we store the format as integers. This is
        fine if the application has a float input in the shader it just means we display the raw integer
        instead of the casted float. However if the shader has an integer input this is invalid and it will
        read something undefined - possibly the int bits of the casted float.
        
        This property is set to ``True`` if the cast happens to an integer input and that bad cast needs to
        be emulated.
        
        :type: bool
        """
        pass
    
    @floatCastWrong.setter
    def floatCastWrong(self, value: bool):
        pass
    
