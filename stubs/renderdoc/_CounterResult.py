from ._CounterValue import CounterValue
from ._GPUCounter import GPUCounter

from typing import overload

class CounterResult():
    # Original docstring
    """
    The resulting value from a counter at an event.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CounterResult.
        """
        pass
    
    @overload
    def __init__(self, other: 'CounterResult'):
        """
        Construct a new CounterResult with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, eventId: int, counter: GPUCounter, data: float):
        """
        Construct a new CounterResult using provided values.
        """
        pass
    
    @overload
    def __init__(self, eventId: int, counter: GPUCounter, data: int):
        """
        Construct a new CounterResult using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def value(self) -> CounterValue:
        """
        The value itself.
        
        :type: CounterValue
        """
        pass
    
    @value.setter
    def value(self, value: CounterValue):
        pass
    
    @property
    def counter(self) -> int:
        """
        The :data:`counter <GPUCounter>` that produced this value, stored as an int.
        
        .. note:: This is stored as an ``int`` not a :class:`GPUCounter` to allow for values that may not
          correspond to any of the predefined values if it's a hardware-specific counter value.
        
        :type: int
        """
        pass
    
    @counter.setter
    def counter(self, value: int):
        pass
    
    @property
    def eventId(self) -> int:
        """
        The :data:`eventId <APIEvent.eventId>` that produced this value.
        
        :type: int
        """
        pass
    
    @eventId.setter
    def eventId(self, value: int):
        pass
    
