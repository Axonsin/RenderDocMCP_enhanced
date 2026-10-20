from ._AddressMode import AddressMode
from ._ChromaSampleLocation import ChromaSampleLocation
from ._CompType import CompType
from ._CompareFunction import CompareFunction
from ._DescriptorType import DescriptorType
from ._FilterMode import FilterMode
from ._PixelValue import PixelValue
from ._ResourceId import ResourceId
from ._TextureFilter import TextureFilter
from ._TextureSwizzle4 import TextureSwizzle4
from ._YcbcrConversion import YcbcrConversion
from ._YcbcrRange import YcbcrRange

from typing import overload

class SamplerDescriptor():
    # Original docstring
    """
    The contents of a sampler descriptor. Not all contents will be valid depending on API
    and capabilities, others will be set to sensible defaults.
    
    For normal descriptors, the resource data should be queried and returned in :class:`Descriptor`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SamplerDescriptor.
        """
        pass
    
    @overload
    def __init__(self, other: 'SamplerDescriptor'):
        """
        Construct a new SamplerDescriptor with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def UseBorder(self) -> bool:
        """
        Check if the border color is used in this D3D11 sampler.
        
        :return: ``True`` if the border color is used, ``False`` otherwise.
        :rtype: bool
        """
        pass
    
    @property
    def borderColorValue(self) -> PixelValue:
        """
        The RGBA border color value. Typically the float tuple inside will be used,
        but the exact component type can be checked with :data:`borderColorType`.
        
        :type: PixelValue
        """
        pass
    
    @borderColorValue.setter
    def borderColorValue(self, value: PixelValue):
        pass
    
    @property
    def creationTimeConstant(self) -> bool:
        """
        ``True`` if this sampler was initialised at creation time for a pipeline or
        descriptor layout, the method being API specific. If so this sampler is not dynamic and was not
        explicitly set and may have no real descriptor storage.
        
        :type: bool
        """
        pass
    
    @creationTimeConstant.setter
    def creationTimeConstant(self, value: bool):
        pass
    
    @property
    def unnormalized(self) -> bool:
        """
        ``True`` if unnormalized co-ordinates are used in this sampler.
        
        :type: bool
        """
        pass
    
    @unnormalized.setter
    def unnormalized(self, value: bool):
        pass
    
    @property
    def swizzle(self) -> TextureSwizzle4:
        """
        The swizzle applied. Primarily for ycbcr samplers applied before
        conversion but for non-ycbcr samplers can be used for implementations that require sampler swizzle
        information for border colors.
        
        :type: TextureSwizzle4
        """
        pass
    
    @swizzle.setter
    def swizzle(self, value: TextureSwizzle4):
        pass
    
    @property
    def ycbcrSampler(self) -> ResourceId:
        """
        The :class:`ResourceId` of the ycbcr conversion object associated with
        this sampler.
        
        :type: ResourceId
        """
        pass
    
    @ycbcrSampler.setter
    def ycbcrSampler(self, value: ResourceId):
        pass
    
    @property
    def compareFunction(self) -> CompareFunction:
        """
        The :class:`CompareFunction` for comparison samplers.
        
        :type: CompareFunction
        """
        pass
    
    @compareFunction.setter
    def compareFunction(self, value: CompareFunction):
        pass
    
    @property
    def maxAnisotropy(self) -> float:
        """
        The maximum anisotropic filtering level to use.
        
        :type: float
        """
        pass
    
    @maxAnisotropy.setter
    def maxAnisotropy(self, value: float):
        pass
    
    @property
    def ycbcrModel(self) -> YcbcrConversion:
        """
        For ycbcr samplers - the :class:`YcbcrConversion` used for conversion.
        
        :type: YcbcrConversion
        """
        pass
    
    @ycbcrModel.setter
    def ycbcrModel(self, value: YcbcrConversion):
        pass
    
    @property
    def ycbcrRange(self) -> YcbcrRange:
        """
        For ycbcr samplers - the :class:`YcbcrRange` used for conversion.
        
        :type: YcbcrRange
        """
        pass
    
    @ycbcrRange.setter
    def ycbcrRange(self, value: YcbcrRange):
        pass
    
    @property
    def srgbBorder(self) -> bool:
        """
        ``True`` if the border colour is swizzled with an sRGB formatted image.
        
        :type: bool
        """
        pass
    
    @srgbBorder.setter
    def srgbBorder(self, value: bool):
        pass
    
    @property
    def seamlessCubemaps(self) -> bool:
        """
        ``True`` if this sampler is seamless across cubemap boundaries (the default).
        
        :type: bool
        """
        pass
    
    @seamlessCubemaps.setter
    def seamlessCubemaps(self, value: bool):
        pass
    
    @property
    def mipBias(self) -> float:
        """
        A bias to apply to the calculated mip level before sampling.
        
        :type: float
        """
        pass
    
    @mipBias.setter
    def mipBias(self, value: float):
        pass
    
    @property
    def addressU(self) -> AddressMode:
        """
        The :class:`AddressMode` in the U direction.
        
        :type: AddressMode
        """
        pass
    
    @addressU.setter
    def addressU(self, value: AddressMode):
        pass
    
    @property
    def borderColorType(self) -> CompType:
        """
        The RGBA border color type. This determines how the data in
        :data:`borderColorValue` will be interpreted.
        
        :type: CompType
        """
        pass
    
    @borderColorType.setter
    def borderColorType(self, value: CompType):
        pass
    
    @property
    def xChromaOffset(self) -> ChromaSampleLocation:
        """
        For ycbcr samplers - the :class:`ChromaSampleLocation` X-axis chroma offset.
        
        :type: ChromaSampleLocation
        """
        pass
    
    @xChromaOffset.setter
    def xChromaOffset(self, value: ChromaSampleLocation):
        pass
    
    @property
    def yChromaOffset(self) -> ChromaSampleLocation:
        """
        For ycbcr samplers - the :class:`ChromaSampleLocation` Y-axis chroma offset.
        
        :type: ChromaSampleLocation
        """
        pass
    
    @yChromaOffset.setter
    def yChromaOffset(self, value: ChromaSampleLocation):
        pass
    
    @property
    def addressV(self) -> AddressMode:
        """
        The :class:`AddressMode` in the V direction.
        
        :type: AddressMode
        """
        pass
    
    @addressV.setter
    def addressV(self, value: AddressMode):
        pass
    
    @property
    def filter(self) -> TextureFilter:
        """
        The filtering mode.
        
        :type: TextureFilter
        """
        pass
    
    @filter.setter
    def filter(self, value: TextureFilter):
        pass
    
    @property
    def chromaFilter(self) -> FilterMode:
        """
        For ycbcr samplers - the :class:`FilterMode` describing the chroma filtering mode.
        
        :type: FilterMode
        """
        pass
    
    @chromaFilter.setter
    def chromaFilter(self, value: FilterMode):
        pass
    
    @property
    def type(self) -> DescriptorType:
        """
        The type of this descriptor as a general category.
        
        If this is not set to :data:`DescriptorType.Sampler` or :data:`DescriptorType.ImageSampler` the rest
        of the contents of this structure are not valid as the descriptor is not a sampler descriptor.
        
        :type: DescriptorType
        """
        pass
    
    @type.setter
    def type(self, value: DescriptorType):
        pass
    
    @property
    def addressW(self) -> AddressMode:
        """
        The :class:`AddressMode` in the W direction.
        
        :type: AddressMode
        """
        pass
    
    @addressW.setter
    def addressW(self, value: AddressMode):
        pass
    
    @property
    def maxLOD(self) -> float:
        """
        The maximum mip level that can be used.
        
        :type: float
        """
        pass
    
    @maxLOD.setter
    def maxLOD(self, value: float):
        pass
    
    @property
    def object(self) -> ResourceId:
        """
        For APIs where samplers are an explicit object, the :class:`ResourceId` of the sampler
        itself
        
        :type: ResourceId
        """
        pass
    
    @object.setter
    def object(self, value: ResourceId):
        pass
    
    @property
    def minLOD(self) -> float:
        """
        The minimum mip level that can be used.
        
        :type: float
        """
        pass
    
    @minLOD.setter
    def minLOD(self, value: float):
        pass
    
    @property
    def forceExplicitReconstruction(self) -> bool:
        """
        For ycbcr samplers - ``True`` if explicit reconstruction is force enabled.
        
        :type: bool
        """
        pass
    
    @forceExplicitReconstruction.setter
    def forceExplicitReconstruction(self, value: bool):
        pass
    
