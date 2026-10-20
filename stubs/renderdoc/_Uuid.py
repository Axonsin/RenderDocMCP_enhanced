from typing import Tuple

from typing import overload

class Uuid():
    # Original docstring
    """
    A 128-bit UUID.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised Uuid.
        """
        pass
    
    @overload
    def __init__(self, other: 'Uuid'):
        """
        Construct a new Uuid with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, word1: int, word2: int, word3: int, word4: int):
        """
        Construct a new Uuid using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def words(self) -> Tuple[int, int, int, int]:
        """
        The UUID bytes as a tuple of four 32-bit integers.
        
        :type: Tuple[int,int,int,int]
        """
        pass
    
    @words.setter
    def words(self, value: Tuple[int, int, int, int]):
        pass
    
