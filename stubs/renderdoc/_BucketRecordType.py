from enum import IntEnum

class BucketRecordType(IntEnum):
    # Original docstring
    """
    The type of bucketing method for recording statistics.
    
    .. data:: Linear
    
      Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
      too high for any of the buckets.
    
    .. data:: Pow2
    
      Each bucket holds twice as many elements as the previous one, with the first bucket containing
      just 1 (bucket index is ``log2(value)``).
    """
    
    
    # Enum values
    
    Linear = 0
    """
    Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
    too high for any of the buckets.
    """
    
    Pow2 = 1
    """
    Each bucket holds twice as many elements as the previous one, with the first bucket containing
    just 1 (bucket index is ``log2(value)``).
    """
    

# Assign __doc__ for enum values for easier introspection

BucketRecordType.Linear.__doc__ = """
Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
too high for any of the buckets.
"""

BucketRecordType.Pow2.__doc__ = """
Each bucket holds twice as many elements as the previous one, with the first bucket containing
just 1 (bucket index is ``log2(value)``).
"""

