from ._DescriptorFlags import DescriptorFlags
from ._DescriptorType import DescriptorType
from ._ResourceFormat import ResourceFormat
from ._ResourceId import ResourceId
from ._TextureSwizzle4 import TextureSwizzle4
from ._TextureType import TextureType

from typing import overload

class Descriptor():
    # Original docstring
    """
    The contents of a descriptor. Not all contents will be valid depending on API and
    descriptor type, others will be set to sensible defaults.
    
    For sampler descriptors, the sampler-specific data can be queried separately and returned as
    :class:`SamplerDescriptor` for sampler types.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Descriptor.
        """
        pass
    
    @overload
    def __init__(self, other: 'Descriptor'):
        """
        Construct a new Descriptor with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def minLODClamp(self) -> float:
        """
        The clamp applied to the minimum LOD by the resource view, separate and in addition to
        any clamp by a sampler used.
        
        :type: float
        """
        pass
    
    @minLODClamp.setter
    def minLODClamp(self, value: float):
        pass
    
    @property
    def swizzle(self) -> TextureSwizzle4:
        """
        The swizzle applied to texture descriptors.
        
        :type: TextureSwizzle4
        """
        pass
    
    @swizzle.setter
    def swizzle(self, value: TextureSwizzle4):
        pass
    
    @property
    def firstMip(self) -> int:
        """
        For texture descriptors, the first mip in the texture which is visible to the
        descriptor
        
        :type: int
        """
        pass
    
    @firstMip.setter
    def firstMip(self, value: int):
        pass
    
    @property
    def view(self) -> ResourceId:
        """
        The view object used to create this descriptor, which formats or subsets the
        bound resource referenced by :data:`resource`.
        
        :type: ResourceId
        """
        pass
    
    @view.setter
    def view(self, value: ResourceId):
        pass
    
    @property
    def format(self) -> ResourceFormat:
        """
        The format cast that the view uses, for typed buffer and image descriptors.
        
        :type: ResourceFormat
        """
        pass
    
    @format.setter
    def format(self, value: ResourceFormat):
        pass
    
    @property
    def numSlices(self) -> int:
        """
        For texture descriptors, the number of slices in a 3D or array texture which are visible
        to the descriptor
        
        :type: int
        """
        pass
    
    @numSlices.setter
    def numSlices(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        For any kind of buffer descriptor, the base byte offset within the resource where the
        referenced range by the descriptor begins.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def counterByteOffset(self) -> int:
        """
        The byte offset in :data:`secondary` where the counter is stored, for buffer
        descriptors with a secondary counter.
        
        :type: int
        """
        pass
    
    @counterByteOffset.setter
    def counterByteOffset(self, value: int):
        pass
    
    @property
    def bufferStructCount(self) -> int:
        """
        If the view has a hidden counter, this stores the current value of the counter.
        
        :type: int
        """
        pass
    
    @bufferStructCount.setter
    def bufferStructCount(self, value: int):
        pass
    
    @property
    def type(self) -> DescriptorType:
        """
        The type of this descriptor as a general category.
        
        :type: DescriptorType
        """
        pass
    
    @type.setter
    def type(self, value: DescriptorType):
        pass
    
    @property
    def flags(self) -> DescriptorFlags:
        """
        The flags for additional API-specific and generally non-semantically impactful
        properties.
        
        :type: DescriptorFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: DescriptorFlags):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        For any kind of buffer descriptor, the number of bytes in the range covered by the
        descriptor.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
    @property
    def elementByteSize(self) -> int:
        """
        The byte size of a single element in the view. Either the byte size of
        :data:`format`, or the structured buffer element size, as appropriate.
        
        :type: int
        """
        pass
    
    @elementByteSize.setter
    def elementByteSize(self, value: int):
        pass
    
    @property
    def firstSlice(self) -> int:
        """
        For texture descriptors, the first slice in a 3D or array texture which is visible
        to the descriptor
        
        :type: int
        """
        pass
    
    @firstSlice.setter
    def firstSlice(self, value: int):
        pass
    
    @property
    def resource(self) -> ResourceId:
        """
        The primary bound resource at this descriptor, either a buffer or an image resource.
        
        Note that sampler descriptors will not be listed here, see :data:`secondary`.
        
        :type: ResourceId
        """
        pass
    
    @resource.setter
    def resource(self, value: ResourceId):
        pass
    
    @property
    def secondary(self) -> ResourceId:
        """
        The secondary bound resource at this descriptor.
        
        For any descriptor containing a sampler, this will be the sampler. For buffer descriptors with an
        associated counter buffer this will be the counter buffer.
        
        :type: ResourceId
        """
        pass
    
    @secondary.setter
    def secondary(self, value: ResourceId):
        pass
    
    @property
    def numMips(self) -> int:
        """
        For texture descriptors, the number of mips in the texture which are visible to the
        descriptor
        
        :type: int
        """
        pass
    
    @numMips.setter
    def numMips(self, value: int):
        pass
    
    @property
    def textureType(self) -> TextureType:
        """
        The specific type of a texture descriptor.
        
        :type: TextureType
        """
        pass
    
    @textureType.setter
    def textureType(self, value: TextureType):
        pass
    
