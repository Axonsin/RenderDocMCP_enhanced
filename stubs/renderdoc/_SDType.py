from ._SDBasic import SDBasic
from ._SDTypeFlags import SDTypeFlags

class SDType():
    # Original docstring
    """
    Details the name and properties of a structured type
    """
    
    
    @property
    def name(self) -> str:
        """
        The name of this type.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size in bytes that an instance of this type takes up.
        
        This is only valid for whole chunks (where it contains the whole chunk size), for buffers that have
        an arbitrary size, or for basic types such as integers and floating point values where it gives the
        size/precision of the type.
        
        For variable size types like structs, arrays, etc it will be set to 0.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
    @property
    def basetype(self) -> SDBasic:
        """
        The :class:`SDBasic` category that this type belongs to.
        
        :type: SDBasic
        """
        pass
    
    @basetype.setter
    def basetype(self, value: SDBasic):
        pass
    
    @property
    def flags(self) -> SDTypeFlags:
        """
        The :class:`SDTypeFlags` flags for this type.
        
        :type: SDTypeFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: SDTypeFlags):
        pass
    
