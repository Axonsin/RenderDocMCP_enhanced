from typing import List

from typing import overload

class ConstantBindStats():
    # Original docstring
    """
    Contains the statistics for constant binds in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ConstantBindStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'ConstantBindStats'):
        """
        Construct a new ConstantBindStats with a deep copy of the input.
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
        A :class:`bucketed <BucketType>` list over the sizes of buffers bound.
        
        :type: List[int]
        """
        pass
    
    @sizes.setter
    def sizes(self, value: List[int]):
        pass
    
    @property
    def sets(self) -> int:
        """
        How many objects were bound.
        
        :type: int
        """
        pass
    
    @sets.setter
    def sets(self, value: int):
        pass
    
    @property
    def bindslots(self) -> List[int]:
        """
        A list where the Nth element contains the number of calls that bound N buffers.
        
        :type: List[int]
        """
        pass
    
    @bindslots.setter
    def bindslots(self, value: List[int]):
        pass
    
    @property
    def nulls(self) -> int:
        """
        How many objects were unbound.
        
        :type: int
        """
        pass
    
    @nulls.setter
    def nulls(self, value: int):
        pass
    
