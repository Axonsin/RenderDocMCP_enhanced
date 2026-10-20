
from typing import overload

class PackingRules():
    # Original docstring
    """
    A description of individual rules for how data is packed in GPU-side structures and
    buffers.
    
    Each individual member rule is such that ``False`` is more restrictive on packing, and ``True``
    is less restrictive.
    
    Several helpers are available for the common formats, see :meth:`PackingRules.STD140`,
    :meth:`PackingRules.STD430`, :meth:`PackingRules.D3DCB`, :meth:`PackingRules.C` which provide
    a quick way to fetch a known set of packing rules.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PackingRules.
        """
        pass
    
    @overload
    def __init__(self, other: 'PackingRules'):
        """
        Construct a new PackingRules with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    @staticmethod
    def STD140() -> 'PackingRules':
        """
        :return: The GLSL std140 rules, used on OpenGL and Vulkan.
        :rtype: PackingRules
        """
        pass
    
    
    @staticmethod
    def STD430() -> 'PackingRules':
        """
        :return: The GLSL std430 rules, used on OpenGL and Vulkan.
        :rtype: PackingRules
        """
        pass
    
    
    @staticmethod
    def D3DCB() -> 'PackingRules':
        """
        :return: The D3D11 and D3D12 Constant Buffer rules.
        :rtype: PackingRules
        """
        pass
    
    
    @staticmethod
    def C() -> 'PackingRules':
        """
        .. note::
          This is the standard C ABI with no special packing directives such as ``#pragma pack()``.
        
        :return: The standard C packing rules.
        :rtype: PackingRules
        """
        pass
    
    
    @staticmethod
    def Scalar() -> 'PackingRules':
        """
        :return: Vulkan scalar block layout rules, which are almost the same as C but in some cases
          allow more tight packing than C by default.
        :rtype: PackingRules
        """
        pass
    
    
    @staticmethod
    def D3DUAV() -> 'PackingRules':
        """
        :return: The D3D Structured UAV buffer rules. This is considered to be the same as standard
          C packing rules.
        :rtype: PackingRules
        """
        pass
    
    @property
    def vectorStraddle16b(self) -> bool:
        """
        Flag indicating if vectors can straddle a 16-byte boundary with their components.
        
        If ``True`` this means vectors have no special restrictions and can be at any aligned byte offset.
        
        If ``False``, vectors must be at an offset such that the whole vector sits within the same
        16-byte aligned region.
        
        :type: bool
        """
        pass
    
    @vectorStraddle16b.setter
    def vectorStraddle16b(self, value: bool):
        pass
    
    @property
    def tightArrays(self) -> bool:
        """
        Flag indicating if arrays are tightly packed with the stride being their natural
        alignment.
        
        If ``True`` this means each array element is at a suitably aligned offset after the previous.
        
        If ``False``, each array element is at a 16-byte aligned offset after the previous regardless
        of the element size and alignment.
        
        :type: bool
        """
        pass
    
    @tightArrays.setter
    def tightArrays(self, value: bool):
        pass
    
    @property
    def tightBitfieldPacking(self) -> bool:
        """
        Flag indicating if bitfields allow bit-packed regions to straddle the base type.
        
        If ``True`` this means bit regions are tightly packed even if one region would cross two
        base elements. E.g. if the base type is uint then three 20-bit regions would only
        consume two uints as that is 60 bits total.
        
        If ``False`` this means each bit region ensures it only exists in one base element with
        padding/unused bits in elements as necessary. E.g. if the base type is uint then three 20-bit
        regions would consume three uints as each region would be padded into its own element.
        
        .. note::
          Bitfield packing is compiler defined on CPU but this mostly matches what happens with
          ``#pragma pack(1)``.
        
        :type: bool
        """
        pass
    
    @tightBitfieldPacking.setter
    def tightBitfieldPacking(self, value: bool):
        pass
    
    @property
    def vectorAlignComponent(self) -> bool:
        """
        Flag indicating if a vector's alignment is only equal to its component alignment.
        
        If ``True`` this means vectors have no special alignment, and a 3-component float vector is
        aligned to 4-byte the same as a scalar float.
        
        If ``False``, 2-wide vectors are aligned to their size, and 3-wide and 4-wide vectors are aligned
        to a 4-wide vector's size. E.g. ``float2`` has 8 byte alignment, ``float3`` and ``float4`` have
        16-byte alignment.
        
        :type: bool
        """
        pass
    
    @vectorAlignComponent.setter
    def vectorAlignComponent(self, value: bool):
        pass
    
    @property
    def trailingOverlap(self) -> bool:
        """
        Flag indicating if the trailing alignment padding space after a struct member can
        be used by the next member.
        
        If ``True`` then a struct that contains e.g. 2 bytes of padding at its end to align it to a 4-byte
        alignment can be followed by a 2-byte member which can have an offset inside that padding region.
        
        If ``False`` then a struct consumes its padding space and the next member starts after the struct
        even if it would otherwise fit and be aligned.
        
        .. warning::
          This is not supported by standard C layouts, but is supported by some GPU layouts.
        
        :type: bool
        """
        pass
    
    @trailingOverlap.setter
    def trailingOverlap(self, value: bool):
        pass
    
