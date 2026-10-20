from ._ResourceFormat import ResourceFormat
from ._ResourceId import ResourceId
from ._TextureCategory import TextureCategory
from ._TextureType import TextureType

from typing import overload

class TextureDescription():
    # Original docstring
    """
    A description of a texture resource.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureDescription'):
        """
        Construct a new TextureDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def resourceId(self) -> ResourceId:
        """
        The unique :class:`ResourceId` that identifies this texture.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
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
    def memoryOffset(self) -> int:
        """
        The byte offset in :data:`memory` where the texture is bound. If
        :data:`memory` is unset, this will be 0.
        
        :type: int
        """
        pass
    
    @memoryOffset.setter
    def memoryOffset(self, value: int):
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
    def memory(self) -> ResourceId:
        """
        The unique :class:`ResourceId` that identifies the memory object this
        texture has a fixed binding to. For objects that do not have an explicit memory binding
        or for sparse textures, this will not be set.
        
        :type: ResourceId
        """
        pass
    
    @memory.setter
    def memory(self, value: ResourceId):
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
    
