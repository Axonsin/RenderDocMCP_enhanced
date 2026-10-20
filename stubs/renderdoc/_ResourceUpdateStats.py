from typing import List

from typing import overload

class ResourceUpdateStats():
    # Original docstring
    """
    Contains the statistics for resource updates in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ResourceUpdateStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'ResourceUpdateStats'):
        """
        Construct a new ResourceUpdateStats with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    BucketType = 1
    """
    The type of buckets being used. See :class:`BucketRecordType`.
    """
    
    BucketCount = 31
    """
    How many buckets there are in the arrays.
    """
    
    @property
    def calls(self) -> int:
        """
        How many function calls were made.
        
        :type: int
        """
        pass
    
    @calls.setter
    def calls(self, value: int):
        pass
    
    @property
    def sizes(self) -> List[int]:
        """
        A :class:`bucketed <BucketType>` list over the number of bytes in the update.
        
        :type: List[int]
        """
        pass
    
    @sizes.setter
    def sizes(self, value: List[int]):
        pass
    
    @property
    def servers(self) -> int:
        """
        How many of :data:`calls` were batched updates written in the command queue.
        
        :type: int
        """
        pass
    
    @servers.setter
    def servers(self, value: int):
        pass
    
    @property
    def types(self) -> List[int]:
        """
        A list with one element for each type in :class:`TextureType`.
        
        The Nth element contains the number of times a resource of that type was updated.
        
        :type: List[int]
        """
        pass
    
    @types.setter
    def types(self, value: List[int]):
        pass
    
    @property
    def clients(self) -> int:
        """
        How many of :data:`calls` were mapped pointers written by the CPU.
        
        :type: int
        """
        pass
    
    @clients.setter
    def clients(self, value: int):
        pass
    
