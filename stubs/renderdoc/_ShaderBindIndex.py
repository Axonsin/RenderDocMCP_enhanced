from ._DescriptorAccess import DescriptorAccess
from ._DescriptorCategory import DescriptorCategory

from typing import overload

class ShaderBindIndex():
    # Original docstring
    """
    References a particular individual binding element in a shader interface.
    
    This is the shader interface side of a :class:`DescriptorAccess` and so can be compared to one to
    check if an access refers to a given index or not.
    
    The context of which shader reflection this index refers to must be provided to properly interpret
    this information, as it is relative to a particular :class:`ShaderReflection`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderBindIndex.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderBindIndex'):
        """
        Construct a new ShaderBindIndex with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, category: DescriptorCategory, index: int):
        """
        Construct a new ShaderBindIndex using provided values.
        """
        pass
    
    @overload
    def __init__(self, category: DescriptorCategory, index: int, arrayElement: int):
        """
        Construct a new ShaderBindIndex using provided values.
        """
        pass
    
    @overload
    def __init__(self, access: DescriptorAccess):
        """
        Construct a new ShaderBindIndex using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def category(self) -> DescriptorCategory:
        """
        The type of binding this refers to, with each category referring to a different
        shader interface in the :data:`ShaderReflection`.
        
        :type: DescriptorCategory
        """
        pass
    
    @category.setter
    def category(self, value: DescriptorCategory):
        pass
    
    @property
    def index(self) -> int:
        """
        The index within the given :data:`category` for the binding.
        
        :type: int
        """
        pass
    
    @index.setter
    def index(self, value: int):
        pass
    
    @property
    def arrayElement(self) -> int:
        """
        If the binding identified by :data:`category` and :data:`index` is arrayed, this
        identifies the particular array index being referred to.
        
        :type: int
        """
        pass
    
    @arrayElement.setter
    def arrayElement(self, value: int):
        pass
    
