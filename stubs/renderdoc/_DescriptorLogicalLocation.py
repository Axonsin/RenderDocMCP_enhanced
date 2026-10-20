from ._DescriptorCategory import DescriptorCategory
from ._ShaderStageMask import ShaderStageMask

from typing import overload

class DescriptorLogicalLocation():
    # Original docstring
    """
    In many cases there may be a logical location or fixed binding point for a particular
    descriptor which is not conveyed with a simple byte offset into a descriptor store.
    This is particularly true for any descriptor stores that are not equivalent to a buffer of bytes
    but actually have an API structure - for example D3D11 and GL with fixed binding points, or Vulkan
    with descriptor sets.
    
    In some cases on APIs with explicit descriptor storage this may convey information about virtualised
    descriptors that are not explicitly backed with real storage.
    
    This structure describes such a location queried for a given descriptor.
    
    For example on D3D11 this would give the register number of the binding, and on GL it would give the
    unit index. Both cases would be able to query the type and shader stage visibility of descriptors
    that are not accessed or even bound.
    
    On Vulkan this would give the set, binding, and visibility. In most cases this information will be
    available for all descriptors but in some cases the type of descriptor may not be available if it
    is unused and has not been initialised.
    
    On D3D12 this would only give the index into the heap, as no other information is available purely
    by the descriptor itself.
    
    .. note::
    
      This information may not be fully present on all APIs so the returned structures may be empty or
      partially filled out, depending on what information is relevant per API.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DescriptorLogicalLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'DescriptorLogicalLocation'):
        """
        Construct a new DescriptorLogicalLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def logicalBindName(self) -> str:
        """
        The logical binding name, as suitable for displaying to a user when displaying
        the contents of a descriptor queried directly from a heap.
        
        Depending on the API, this name may be identical or less specific than the one obtained from
        shader reflection. Generally speaking it's preferred to use any information from shader reflection
        first, and fall back to this name if no reflection information is available in the context.
        
        :type: str
        """
        pass
    
    @logicalBindName.setter
    def logicalBindName(self, value: str):
        pass
    
    @property
    def stageMask(self) -> ShaderStageMask:
        """
        The set of shader stages that this descriptor is intrinsically available to. This is
        primarily relevant for D3D11 with its fixed per-stage register binding points.
        
        Note this *only* shows if a descriptor itself can only ever be accessed by some shader stages by
        definition, not if a descriptor is generally available but happened to only be accessed by one or
        more stage. That information is available directly in the :class:`DescriptorAccess` itself.
        
        :type: ShaderStageMask
        """
        pass
    
    @stageMask.setter
    def stageMask(self, value: ShaderStageMask):
        pass
    
    @property
    def fixedBindNumber(self) -> int:
        """
        The fixed binding number for this descriptor. The interpretation of this is
        API-specific and it is provided purely for informational purposes and has no bearing on how data
        is accessed or described.
        
        Generally speaking sorting by this number will give a reasonable ordering by binding if it exists.
        
        .. note::
          Because this number is API-specific, there is no guarantee that it will be unique across all
          descriptors. It should be used only within contexts that can interpret it API-specifically, or
          else for purely informational/non-semantic purposes like sorting.
        
        :type: int
        """
        pass
    
    @fixedBindNumber.setter
    def fixedBindNumber(self, value: int):
        pass
    
    @property
    def category(self) -> DescriptorCategory:
        """
        The general category of a descriptor stored. This may not be available for
        uninitialised descriptors on all APIs.
        
        :type: DescriptorCategory
        """
        pass
    
    @category.setter
    def category(self, value: DescriptorCategory):
        pass
    
