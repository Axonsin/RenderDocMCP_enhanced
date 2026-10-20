from ._PixelValue import PixelValue
from ._ResourceFormat import ResourceFormat

from typing import overload

class GLVertexAttribute():
    # Original docstring
    """
    Describes the configuration for a single vertex attribute.
    
    .. note:: If old-style vertex attrib pointer setup was used for the vertex attributes then it will
      be decomposed into 1:1 attributes and buffers.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLVertexAttribute.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLVertexAttribute'):
        """
        Construct a new GLVertexAttribute with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def enabled(self) -> bool:
        """
        ``True`` if this vertex attribute is enabled.
        
        :type: bool
        """
        pass
    
    @enabled.setter
    def enabled(self, value: bool):
        pass
    
    @property
    def genericValue(self) -> PixelValue:
        """
        The generic value of the vertex attribute if no buffer is bound.
        
        :type: PixelValue
        """
        pass
    
    @genericValue.setter
    def genericValue(self, value: PixelValue):
        pass
    
    @property
    def format(self) -> ResourceFormat:
        """
        The format describing how the vertex attribute is interpreted.
        
        :type: ResourceFormat
        """
        pass
    
    @format.setter
    def format(self, value: ResourceFormat):
        pass
    
    @property
    def boundShaderInput(self) -> int:
        """
        This lists which shader input is bound to this attribute, as an index in the
        :data:`ShaderReflection.inputSignature` list.
        
        If any value is set to ``-1`` then the attribute is unbound.
        
        :type: int
        """
        pass
    
    @boundShaderInput.setter
    def boundShaderInput(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of the vertex data in the vertex buffer from
        :data:`vertexBufferSlot`.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def vertexBufferSlot(self) -> int:
        """
        The vertex buffer input slot where the data is sourced from.
        
        :type: int
        """
        pass
    
    @vertexBufferSlot.setter
    def vertexBufferSlot(self, value: int):
        pass
    
    @property
    def floatCast(self) -> bool:
        """
        Only valid for integer formatted attributes, ``True`` if they are cast to float.
        
        This is because they were specified with an integer format but ``glVertexAttribFormat`` (not
        ``glVertexAttribIFormat``) so they will be cast.
        
        :type: bool
        """
        pass
    
    @floatCast.setter
    def floatCast(self, value: bool):
        pass
    
