from ._AlphaMapping import AlphaMapping
from ._CompType import CompType
from ._FileType import FileType
from ._FloatVector import FloatVector
from ._ResourceId import ResourceId
from ._TextureComponentMapping import TextureComponentMapping
from ._TextureSampleMapping import TextureSampleMapping
from ._TextureSliceMapping import TextureSliceMapping

from typing import overload

class TextureSave():
    # Original docstring
    """
    Describes a texture to save and how to map it to the destination file format.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureSave.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureSave'):
        """
        Construct a new TextureSave with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def slice(self) -> TextureSliceMapping:
        """
        Controls mapping for arrayed textures (ignored if texture is not arrayed)
        
        :type: TextureSliceMapping
        """
        pass
    
    @slice.setter
    def slice(self, value: TextureSliceMapping):
        pass
    
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
    def alphaCol(self) -> FloatVector:
        """
        The background color if :data:`alpha` is set to :attr:`AlphaMapping.BlendToColor`.
        
        :type: FloatVector
        """
        pass
    
    @alphaCol.setter
    def alphaCol(self, value: FloatVector):
        pass
    
