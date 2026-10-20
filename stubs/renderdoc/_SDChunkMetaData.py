from ._SDChunkFlags import SDChunkFlags
from typing import List

from typing import overload

class SDChunkMetaData():
    # Original docstring
    """
    The metadata that goes along with a :class:`SDChunk` to detail how it was recorded.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SDChunkMetaData.
        """
        pass
    
    @overload
    def __init__(self, other: 'SDChunkMetaData'):
        """
        Construct a new SDChunkMetaData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def durationMicro(self) -> int:
        """
        The duration in microseconds that this chunk took. This is the time for the actual
        work, not the serialising.
        Since 0 is a possible value for this (for extremely fast calls), -1 is the invalid/not present value.
        
        :type: int
        """
        pass
    
    @durationMicro.setter
    def durationMicro(self, value: int):
        pass
    
    @property
    def callstack(self) -> List[int]:
        """
        The frames of the CPU-side callstack leading up to the chunk.
        
        :type: List[int]
        """
        pass
    
    @callstack.setter
    def callstack(self, value: List[int]):
        pass
    
    @property
    def length(self) -> int:
        """
        The length in bytes of this chunk - may be longer than the actual sum of the data if a
        conservative size estimate was used on creation to avoid seeking to fix-up the stored length.
        
        :type: int
        """
        pass
    
    @length.setter
    def length(self, value: int):
        pass
    
    @property
    def flags(self) -> SDChunkFlags:
        """
        The :class:`SDChunkFlags` for this chunk.
        
        :type: SDChunkFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: SDChunkFlags):
        pass
    
    @property
    def chunkID(self) -> int:
        """
        The internal chunk ID - unique given a particular driver in use.
        
        :type: int
        """
        pass
    
    @chunkID.setter
    def chunkID(self, value: int):
        pass
    
    @property
    def threadID(self) -> int:
        """
        The ID of the thread where this chunk was recorded.
        
        :type: int
        """
        pass
    
    @threadID.setter
    def threadID(self, value: int):
        pass
    
    @property
    def timestampMicro(self) -> int:
        """
        The point in time when this chunk was recorded, in microseconds since program start.
        
        :type: int
        """
        pass
    
    @timestampMicro.setter
    def timestampMicro(self, value: int):
        pass
    
