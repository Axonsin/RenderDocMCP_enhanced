from typing import List

from typing import overload

class DrawcallStats():
    # Original docstring
    """
    Contains the statistics for draws in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketSize
    
      How many elements each bucket contains.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DrawcallStats.
        """
        pass
    
    @overload
    def __init__(self, other: 'DrawcallStats'):
        """
        Construct a new DrawcallStats with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    BucketType = 0
    """
    The type of buckets being used. See :class:`BucketRecordType`.
    """
    
    BucketSize = 1
    """
    How many elements each bucket contains.
    """
    
    BucketCount = 16
    """
    How many buckets there are in the arrays.
    """
    
    @property
    def calls(self) -> int:
        """
        How many draw calls were made.
        
        :type: int
        """
        pass
    
    @calls.setter
    def calls(self, value: int):
        pass
    
    @property
    def instanced(self) -> int:
        """
        How many of :data:`calls` were instanced.
        
        :type: int
        """
        pass
    
    @instanced.setter
    def instanced(self, value: int):
        pass
    
    @property
    def indirect(self) -> int:
        """
        How many of :data:`calls` were indirect.
        
        :type: int
        """
        pass
    
    @indirect.setter
    def indirect(self, value: int):
        pass
    
    @property
    def counts(self) -> List[int]:
        """
        A :class:`bucketed <BucketType>` list over the number of instances in the draw.
        
        :type: List[int]
        """
        pass
    
    @counts.setter
    def counts(self, value: List[int]):
        pass
    
