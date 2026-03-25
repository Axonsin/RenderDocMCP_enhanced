# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat
from .PixelValue import PixelValue

class GLVertexAttribute(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes the configuration for a single vertex attribute.
    
    .. note:: If old-style vertex attrib pointer setup was used for the vertex attributes then it will
      be decomposed into 1:1 attributes and buffers.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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
    def floatCast(self) -> bool:
        """
Only valid for integer formatted attributes, ``True`` if they are cast to float.

This is because they were specified with an integer format but glVertexAttribFormat (not
glVertexAttribIFormat) so they will be cast.

:type: bool

"""
        pass

    @floatCast.setter
    def floatCast(self, value: bool):
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
    def genericValue(self) -> PixelValue:
        """
The generic value of the vertex attribute if no buffer is bound.

:type: PixelValue

"""
        pass

    @genericValue.setter
    def genericValue(self, value: PixelValue):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522B580>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLVertexAttribute' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLVertexAttribute' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLVertexAttribute' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLVertexAttribute' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLVertexAttribute' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLVertexAttribute' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLVertexAttribute' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLVertexAttribute' objects>, 'enabled': <attribute 'enabled' of 'renderdoc.GLVertexAttribute' objects>, 'genericValue': <attribute 'genericValue' of 'renderdoc.GLVertexAttribute' objects>, 'format': <attribute 'format' of 'renderdoc.GLVertexAttribute' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLVertexAttribute' objects>, 'boundShaderInput': <attribute 'boundShaderInput' of 'renderdoc.GLVertexAttribute' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.GLVertexAttribute' objects>, 'vertexBufferSlot': <attribute 'vertexBufferSlot' of 'renderdoc.GLVertexAttribute' objects>, 'floatCast': <attribute 'floatCast' of 'renderdoc.GLVertexAttribute' objects>, '__doc__': '\\nDescribes the configuration for a single vertex attribute.\\n\\n.. note:: If old-style vertex attrib pointer setup was used for the vertex attributes then it will\\n  be decomposed into 1:1 attributes and buffers.\\n\\n'})"


