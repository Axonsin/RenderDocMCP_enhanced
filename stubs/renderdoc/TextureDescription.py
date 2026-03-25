# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .TextureCategory import TextureCategory
from .ResourceFormat import ResourceFormat
from .ResourceId import ResourceId
from .TextureType import TextureType

class TextureDescription(): # skipped bases: <class 'SwigPyObject'>
    """ A description of a texture resource. """
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
    def arraysize(self) -> int:
        """
How many array elements this texture has, will be at least 1.

:type: int

"""
        pass

    @arraysize.setter
    def arraysize(self, value: int):
        pass

    @property
    def byteSize(self) -> int:
        """
How many bytes would be used to store this texture and all its mips/slices.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def creationFlags(self) -> TextureCategory:
        """
The way this texture will be used in the pipeline.

:type: TextureCategory

"""
        pass

    @creationFlags.setter
    def creationFlags(self, value: TextureCategory):
        pass

    @property
    def cubemap(self) -> bool:
        """
``True`` if this texture is used as a cubemap or cubemap array.

:type: bool

"""
        pass

    @cubemap.setter
    def cubemap(self, value: bool):
        pass

    @property
    def depth(self) -> int:
        """
The depth of the texture, or 1 if not applicable.

:type: int

"""
        pass

    @depth.setter
    def depth(self, value: int):
        pass

    @property
    def dimension(self) -> int:
        """
The base dimension of the texture - either 1, 2, or 3.

:type: int

"""
        pass

    @dimension.setter
    def dimension(self, value: int):
        pass

    @property
    def format(self) -> ResourceFormat:
        """
The format of each pixel in the texture.

:type: ResourceFormat

"""
        pass

    @format.setter
    def format(self, value: ResourceFormat):
        pass

    @property
    def height(self) -> int:
        """
The height of the texture, or 1 if not applicable.

:type: int

"""
        pass

    @height.setter
    def height(self, value: int):
        pass

    @property
    def mips(self) -> int:
        """
How many mips this texture has, will be at least 1.

:type: int

"""
        pass

    @mips.setter
    def mips(self, value: int):
        pass

    @property
    def msQual(self) -> int:
        """
The quality setting of this texture, or 0 if not applicable.

:type: int

"""
        pass

    @msQual.setter
    def msQual(self, value: int):
        pass

    @property
    def msSamp(self) -> int:
        """
How many multisampled samples this texture has, will be at least 1.

:type: int

"""
        pass

    @msSamp.setter
    def msSamp(self, value: int):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The unique :class:`ResourceId` that identifies this texture.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> TextureType:
        """
The :class:`TextureType` of the texture.

:type: TextureType

"""
        pass

    @type.setter
    def type(self, value: TextureType):
        pass

    @property
    def width(self) -> int:
        """
The width of the texture, or length for buffer textures.

:type: int

"""
        pass

    @width.setter
    def width(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B87F0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureDescription' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureDescription' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureDescription' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureDescription' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureDescription' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureDescription' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureDescription' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureDescription' objects>, 'cubemap': <attribute 'cubemap' of 'renderdoc.TextureDescription' objects>, 'mips': <attribute 'mips' of 'renderdoc.TextureDescription' objects>, 'msSamp': <attribute 'msSamp' of 'renderdoc.TextureDescription' objects>, 'dimension': <attribute 'dimension' of 'renderdoc.TextureDescription' objects>, 'height': <attribute 'height' of 'renderdoc.TextureDescription' objects>, 'creationFlags': <attribute 'creationFlags' of 'renderdoc.TextureDescription' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.TextureDescription' objects>, 'format': <attribute 'format' of 'renderdoc.TextureDescription' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureDescription' objects>, 'depth': <attribute 'depth' of 'renderdoc.TextureDescription' objects>, 'width': <attribute 'width' of 'renderdoc.TextureDescription' objects>, 'type': <attribute 'type' of 'renderdoc.TextureDescription' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.TextureDescription' objects>, 'msQual': <attribute 'msQual' of 'renderdoc.TextureDescription' objects>, 'arraysize': <attribute 'arraysize' of 'renderdoc.TextureDescription' objects>, '__doc__': 'A description of a texture resource.'})"


