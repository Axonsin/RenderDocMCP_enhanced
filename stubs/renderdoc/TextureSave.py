# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .AlphaMapping import AlphaMapping
from .FloatVector import FloatVector
from .TextureComponentMapping import TextureComponentMapping
from .FileType import FileType
from .ResourceId import ResourceId
from .TextureSampleMapping import TextureSampleMapping
from .TextureSliceMapping import TextureSliceMapping
from .CompType import CompType

class TextureSave(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a texture to save and how to map it to the destination file format. """
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
    def alpha(self) -> AlphaMapping:
        """
Controls handling of alpha channel, only relevant for file formats that don't have
alpha.

It is an :class:`AlphaMapping` that controls what behaviour to use.

:type: AlphaMapping

"""
        pass

    @alpha.setter
    def alpha(self, value: AlphaMapping):
        pass

    @property
    def alphaCol(self) -> FloatVector:
        """
The background color if :data:`alpha` is set to :attr:`AlphaMapping.BlendToColor`.

:type: FloatVector

"""
        pass

    @alphaCol.setter
    def alphaCol(self, value: FloatVector):
        pass

    @property
    def channelExtract(self) -> int:
        """
Selects a single component out of a texture to save as grayscale, or -1 to save all.

:type: int

"""
        pass

    @channelExtract.setter
    def channelExtract(self, value: int):
        pass

    @property
    def comp(self) -> TextureComponentMapping:
        """
Controls black/white point mapping for output formats that are normal
:attr:`8-bit SRGB <CompType.UNorm>`, values are truncated so that values below the black point
and above the white point are clamped, and the values in between are evenly distributed.

:type: TextureComponentMapping

"""
        pass

    @comp.setter
    def comp(self, value: TextureComponentMapping):
        pass

    @property
    def destType(self) -> FileType:
        """
The :class:`FileType` to use when saving to the destination file.

:type: FileType

"""
        pass

    @destType.setter
    def destType(self, value: FileType):
        pass

    @property
    def jpegQuality(self) -> int:
        """
The quality to use when saving to a ``JPG`` file. Valid values are between 1 and 100.

:type: int

"""
        pass

    @jpegQuality.setter
    def jpegQuality(self, value: int):
        pass

    @property
    def mip(self) -> int:
        """
Selects the mip to be written out.

If set to ``-1`` then all mips are written, where allowed by file format. If not allowed, mip 0 is
written

:type: int

"""
        pass

    @mip.setter
    def mip(self, value: int):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the texture to save.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    @property
    def sample(self) -> TextureSampleMapping:
        """
Controls mapping for multisampled textures (ignored if texture is not multisampled)

:type: TextureSampleMapping

"""
        pass

    @sample.setter
    def sample(self, value: TextureSampleMapping):
        pass

    @property
    def slice(self) -> TextureSliceMapping:
        """
Controls mapping for arrayed textures (ignored if texture is not arrayed)

:type: TextureSliceMapping

"""
        pass

    @slice.setter
    def slice(self, value: TextureSliceMapping):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def typeCast(self) -> CompType:
        """
If possible interpret the texture with this type instead of its normal type.

If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the texture
data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned normalised
values.

:type: CompType

"""
        pass

    @typeCast.setter
    def typeCast(self, value: CompType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55215CC0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureSave' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureSave' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureSave' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureSave' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureSave' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureSave' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureSave' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureSave' objects>, 'destType': <attribute 'destType' of 'renderdoc.TextureSave' objects>, 'jpegQuality': <attribute 'jpegQuality' of 'renderdoc.TextureSave' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.TextureSave' objects>, 'comp': <attribute 'comp' of 'renderdoc.TextureSave' objects>, 'alpha': <attribute 'alpha' of 'renderdoc.TextureSave' objects>, 'channelExtract': <attribute 'channelExtract' of 'renderdoc.TextureSave' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureSave' objects>, 'slice': <attribute 'slice' of 'renderdoc.TextureSave' objects>, 'typeCast': <attribute 'typeCast' of 'renderdoc.TextureSave' objects>, 'sample': <attribute 'sample' of 'renderdoc.TextureSave' objects>, 'mip': <attribute 'mip' of 'renderdoc.TextureSave' objects>, 'alphaCol': <attribute 'alphaCol' of 'renderdoc.TextureSave' objects>, '__doc__': 'Describes a texture to save and how to map it to the destination file format.'})"


