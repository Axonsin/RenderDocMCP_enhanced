from ._CompType import CompType
from ._CounterUnit import CounterUnit
from ._Uuid import Uuid

from typing import overload

class CounterDescription():
    # Original docstring
    """
    Describes a GPU counter's purpose and result value.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CounterDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'CounterDescription'):
        """
        Construct a new CounterDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def uuid(self) -> Uuid:
        """
        The unique identifier for this counter that will not change across drivers or replays.
        
        :type: Uuid
        """
        pass
    
    @uuid.setter
    def uuid(self, value: Uuid):
        pass
    
    @property
    def name(self) -> str:
        """
        A short human-readable name for the counter.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def counter(self) -> int:
        """
        The :class:`GPUCounter` this counter represents.
        
        .. note:: This is stored as an ``int`` not a :class:`GPUCounter` to allow for values that may not
          correspond to any of the predefined values if it's a hardware-specific counter value.
        
        :type: int
        """
        pass
    
    @counter.setter
    def counter(self, value: int):
        pass
    
    @property
    def resultType(self) -> CompType:
        """
        The :class:`type of value <CompType>` returned by this counter.
        
        :type: CompType
        """
        pass
    
    @resultType.setter
    def resultType(self, value: CompType):
        pass
    
    @property
    def unit(self) -> CounterUnit:
        """
        The :class:`CounterUnit` for the result value.
        
        :type: CounterUnit
        """
        pass
    
    @unit.setter
    def unit(self, value: CounterUnit):
        pass
    
    @property
    def category(self) -> str:
        """
        The counter category. Can be empty for uncategorized counters.
        
        :type: str
        """
        pass
    
    @category.setter
    def category(self, value: str):
        pass
    
    @property
    def description(self) -> str:
        """
        If available, a longer human-readable description of the value this counter measures.
        
        :type: str
        """
        pass
    
    @description.setter
    def description(self, value: str):
        pass
    
    @property
    def resultByteWidth(self) -> int:
        """
        The number of bytes in the resulting value.
        
        :type: int
        """
        pass
    
    @resultByteWidth.setter
    def resultByteWidth(self, value: int):
        pass
    
