from ._ResourceUsage import ResourceUsage

from typing import overload

class EventUsage():
    # Original docstring
    """
    Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised EventUsage.
        """
        pass
    
    @overload
    def __init__(self, other: 'EventUsage'):
        """
        Construct a new EventUsage with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, eventId: int, usage: ResourceUsage):
        """
        Construct a new EventUsage using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def eventId(self) -> int:
        """
        The :data:`eventId <APIEvent.eventId>` where this usage happened.
        
        :type: int
        """
        pass
    
    @eventId.setter
    def eventId(self, value: int):
        pass
    
    @property
    def usage(self) -> ResourceUsage:
        """
        The :class:`ResourceUsage` in question.
        
        :type: ResourceUsage
        """
        pass
    
    @usage.setter
    def usage(self, value: ResourceUsage):
        pass
    
