# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorFlags import DescriptorFlags
from .ResourceFormat import ResourceFormat
from .ResourceId import ResourceId
from .TextureSwizzle4 import TextureSwizzle4
from .TextureType import TextureType
from .DescriptorType import DescriptorType

class Descriptor(): # skipped bases: <class 'SwigPyObject'>
    """
    The contents of a descriptor. Not all contents will be valid depending on API and
    descriptor type, others will be set to sensible defaults.
    
    For sampler descriptors, the sampler-specific data can be queried separately and returned as
    :class:`SamplerDescriptor` for sampler types.
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
    def elementByteSize(self) -> int:
        """
The byte size of a single element in the view. Either the byte size of
:data:`viewFormat`, or the structured buffer element size, as appropriate.

:type: int

"""
        pass

    @elementByteSize.setter
    def elementByteSize(self, value: int):
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
    def textureType(self) -> TextureType:
        """
The specific type of a texture descriptor.

:type: TextureType

"""
        pass

    @textureType.setter
    def textureType(self, value: TextureType):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55214540>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.Descriptor' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.Descriptor' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.Descriptor' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.Descriptor' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.Descriptor' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.Descriptor' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.Descriptor' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.Descriptor' objects>, 'minLODClamp': <attribute 'minLODClamp' of 'renderdoc.Descriptor' objects>, 'swizzle': <attribute 'swizzle' of 'renderdoc.Descriptor' objects>, 'firstMip': <attribute 'firstMip' of 'renderdoc.Descriptor' objects>, 'view': <attribute 'view' of 'renderdoc.Descriptor' objects>, 'format': <attribute 'format' of 'renderdoc.Descriptor' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.Descriptor' objects>, 'numSlices': <attribute 'numSlices' of 'renderdoc.Descriptor' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.Descriptor' objects>, 'counterByteOffset': <attribute 'counterByteOffset' of 'renderdoc.Descriptor' objects>, 'bufferStructCount': <attribute 'bufferStructCount' of 'renderdoc.Descriptor' objects>, 'type': <attribute 'type' of 'renderdoc.Descriptor' objects>, 'flags': <attribute 'flags' of 'renderdoc.Descriptor' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.Descriptor' objects>, 'elementByteSize': <attribute 'elementByteSize' of 'renderdoc.Descriptor' objects>, 'firstSlice': <attribute 'firstSlice' of 'renderdoc.Descriptor' objects>, 'resource': <attribute 'resource' of 'renderdoc.Descriptor' objects>, 'secondary': <attribute 'secondary' of 'renderdoc.Descriptor' objects>, 'numMips': <attribute 'numMips' of 'renderdoc.Descriptor' objects>, 'textureType': <attribute 'textureType' of 'renderdoc.Descriptor' objects>, '__doc__': '\\nThe contents of a descriptor. Not all contents will be valid depending on API and\\ndescriptor type, others will be set to sensible defaults.\\n\\nFor sampler descriptors, the sampler-specific data can be queried separately and returned as\\n:class:`SamplerDescriptor` for sampler types.\\n\\n'})"


