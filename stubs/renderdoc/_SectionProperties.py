from ._SectionFlags import SectionFlags
from ._SectionType import SectionType

from typing import overload

class SectionProperties():
    # Original docstring
    """
    Properties of a section in a renderdoc capture file.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SectionProperties.
        """
        pass
    
    @overload
    def __init__(self, other: 'SectionProperties'):
        """
        Construct a new SectionProperties with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        The name of this section.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def type(self) -> SectionType:
        """
        The type of this section, if it is a known pre-defined section.
        
        :type: SectionType
        """
        pass
    
    @type.setter
    def type(self, value: SectionType):
        pass
    
    @property
    def flags(self) -> SectionFlags:
        """
        The flags describing how this section is stored.
        
        :type: SectionFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: SectionFlags):
        pass
    
    @property
    def version(self) -> int:
        """
        The version of this section - the meaning of which is up to the type.
        
        :type: int
        """
        pass
    
    @version.setter
    def version(self, value: int):
        pass
    
    @property
    def uncompressedSize(self) -> int:
        """
        The number of bytes of data contained in this section, once uncompressed.
        
        :type: int
        """
        pass
    
    @uncompressedSize.setter
    def uncompressedSize(self, value: int):
        pass
    
    @property
    def compressedSize(self) -> int:
        """
        The number of bytes of data in this section when compressed on disk.
        
        :type: int
        """
        pass
    
    @compressedSize.setter
    def compressedSize(self, value: int):
        pass
    
