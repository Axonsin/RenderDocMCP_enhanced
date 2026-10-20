
from typing import overload

class GLTextureCompleteness():
    # Original docstring
    """
    Describes the a texture completeness issue of a descriptor.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLTextureCompleteness.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLTextureCompleteness'):
        """
        Construct a new GLTextureCompleteness with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def descriptorByteOffset(self) -> int:
        """
        The byte offset in the GL descriptor storage of the problematic descriptor
        
        :type: int
        """
        pass
    
    @descriptorByteOffset.setter
    def descriptorByteOffset(self, value: int):
        pass
    
    @property
    def typeConflict(self) -> str:
        """
        The details of any type conflict on this binding. This can happen if
        multiple uniforms are pointing to the same binding but with different types. In this case it is
        impossible to disambiguate which binding was used.
        
        If this string is empty, no conflict is present. Otherwise it contains the bindings which are
        in conflict and their types.
        
        :type: str
        """
        pass
    
    @typeConflict.setter
    def typeConflict(self, value: str):
        pass
    
    @property
    def completeStatus(self) -> str:
        """
        The details of the texture's (in)completeness. If this string is empty, the texture is
        complete. Otherwise it contains an explanation of why the texture is believed to be incomplete.
        
        :type: str
        """
        pass
    
    @completeStatus.setter
    def completeStatus(self, value: str):
        pass
    
