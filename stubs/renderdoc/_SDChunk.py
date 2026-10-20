from ._SDChunkMetaData import SDChunkMetaData
from ._SDObject import SDObject

from typing import overload

class SDChunk(SDObject):
    # Original docstring
    """
    Defines a single structured chunk, which is a :class:`SDObject`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SDChunk.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def Duplicate(self) -> 'SDChunk':
        """
        :return: A new deep copy of this chunk, which the caller owns.
        :rtype: SDChunk
        """
        pass
    
    @property
    def metadata(self) -> SDChunkMetaData:
        """
        The :class:`SDChunkMetaData` with the metadata for this chunk.
        
        :type: SDChunkMetaData
        """
        pass
    
    @metadata.setter
    def metadata(self, value: SDChunkMetaData):
        pass
    
