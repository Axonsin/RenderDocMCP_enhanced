from ._PathProperty import PathProperty

from typing import overload

class PathEntry():
    # Original docstring
    """
    Properties of a path on a remote filesystem.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PathEntry.
        """
        pass
    
    @overload
    def __init__(self, other: 'PathEntry'):
        """
        Construct a new PathEntry with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, filename: str, flags: PathProperty):
        """
        Construct a new PathEntry using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def lastmod(self) -> int:
        """
        The last modified date of this path, as a unix timestamp in UTC.
        
        :type: int
        """
        pass
    
    @lastmod.setter
    def lastmod(self, value: int):
        pass
    
    @property
    def size(self) -> int:
        """
        The size of the path in bytes.
        
        :type: int
        """
        pass
    
    @size.setter
    def size(self, value: int):
        pass
    
    @property
    def filename(self) -> str:
        """
        The filename of this path. This contains only the filename, not the full path.
        
        :type: str
        """
        pass
    
    @filename.setter
    def filename(self, value: str):
        pass
    
    @property
    def flags(self) -> PathProperty:
        """
        The :class:`PathProperty` flags for this path.
        
        :type: PathProperty
        """
        pass
    
    @flags.setter
    def flags(self, value: PathProperty):
        pass
    
