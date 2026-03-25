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

class VertexInputAttribute(): # skipped bases: <class 'SwigPyObject'>
    """ Information about a vertex input attribute feeding the vertex shader. """
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
    def floatCastWrong(self) -> bool:
        """
Only valid for attributes on OpenGL. If the attribute has been set up for integers to
be converted to floats (glVertexAttribFormat with GL_INT) we store the format as integers. This is
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
    def perInstance(self) -> bool:
        """
``True`` if this attribute runs at instance rate.

:type: bool

"""
        pass

    @perInstance.setter
    def perInstance(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    def vertexBuffer(self) -> int:
        """
The index of the vertex buffer used to provide this attribute.

:type: int

"""
        pass

    @vertexBuffer.setter
    def vertexBuffer(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55213840>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VertexInputAttribute' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VertexInputAttribute' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VertexInputAttribute' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VertexInputAttribute' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VertexInputAttribute' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VertexInputAttribute' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VertexInputAttribute' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VertexInputAttribute' objects>, 'used': <attribute 'used' of 'renderdoc.VertexInputAttribute' objects>, 'name': <attribute 'name' of 'renderdoc.VertexInputAttribute' objects>, 'vertexBuffer': <attribute 'vertexBuffer' of 'renderdoc.VertexInputAttribute' objects>, 'genericValue': <attribute 'genericValue' of 'renderdoc.VertexInputAttribute' objects>, 'genericEnabled': <attribute 'genericEnabled' of 'renderdoc.VertexInputAttribute' objects>, 'format': <attribute 'format' of 'renderdoc.VertexInputAttribute' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VertexInputAttribute' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VertexInputAttribute' objects>, 'perInstance': <attribute 'perInstance' of 'renderdoc.VertexInputAttribute' objects>, 'instanceRate': <attribute 'instanceRate' of 'renderdoc.VertexInputAttribute' objects>, 'floatCastWrong': <attribute 'floatCastWrong' of 'renderdoc.VertexInputAttribute' objects>, '__doc__': 'Information about a vertex input attribute feeding the vertex shader.'})"


