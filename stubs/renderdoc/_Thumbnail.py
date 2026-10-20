from ._FileType import FileType

from typing import overload

class Thumbnail():
    # Original docstring
    """
    Contains the bytes and metadata describing a thumbnail.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Thumbnail.
        """
        pass
    
    @overload
    def __init__(self, other: 'Thumbnail'):
        """
        Construct a new Thumbnail with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def height(self) -> int:
        """
        The height of the thumbnail image.
        
        :type: int
        """
        pass
    
    @height.setter
    def height(self, value: int):
        pass
    
    @property
    def width(self) -> int:
        """
        The width of the thumbnail image.
        
        :type: int
        """
        pass
    
    @width.setter
    def width(self, value: int):
        pass
    
    @property
    def type(self) -> FileType:
        """
        The :class:`FileType` of the data in the thumbnail.
        
        :type: FileType
        """
        pass
    
    @type.setter
    def type(self, value: FileType):
        pass
    
    @property
    def data(self) -> bytes:
        """
        The ``bytes`` byte array containing the raw data.
        
        :type: bytes
        """
        pass
    
    @data.setter
    def data(self, value: bytes):
        pass
    
