# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorCategory import DescriptorCategory
from .ShaderStageMask import ShaderStageMask

class DescriptorLogicalLocation(): # skipped bases: <class 'SwigPyObject'>
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CF980>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DescriptorLogicalLocation' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DescriptorLogicalLocation' objects>, 'logicalBindName': <attribute 'logicalBindName' of 'renderdoc.DescriptorLogicalLocation' objects>, 'stageMask': <attribute 'stageMask' of 'renderdoc.DescriptorLogicalLocation' objects>, 'fixedBindNumber': <attribute 'fixedBindNumber' of 'renderdoc.DescriptorLogicalLocation' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DescriptorLogicalLocation' objects>, 'category': <attribute 'category' of 'renderdoc.DescriptorLogicalLocation' objects>, '__doc__': '\\nIn many cases there may be a logical location or fixed binding point for a particular\\ndescriptor which is not conveyed with a simple byte offset into a descriptor store.\\nThis is particularly true for any descriptor stores that are not equivalent to a buffer of bytes\\nbut actually have an API structure - for example D3D11 and GL with fixed binding points, or Vulkan\\nwith descriptor sets.\\n\\nIn some cases on APIs with explicit descriptor storage this may convey information about virtualised\\ndescriptors that are not explicitly backed with real storage.\\n\\nThis structure describes such a location queried for a given descriptor.\\n\\nFor example on D3D11 this would give the register number of the binding, and on GL it would give the\\nunit index. Both cases would be able to query the type and shader stage visibility of descriptors\\nthat are not accessed or even bound.\\n\\nOn Vulkan this would give the set, binding, and visibility. In most cases this information will be\\navailable for all descriptors but in some cases the type of descriptor may not be available if it\\nis unused and has not been initialised.\\n\\nOn D3D12 this would only give the index into the heap, as no other information is available purely\\nby the descriptor itself.\\n\\n.. note::\\n\\n  This information may not be fully present on all APIs so the returned structures may be empty or\\n  partially filled out, depending on what information is relevant per API.\\n\\n'})"


