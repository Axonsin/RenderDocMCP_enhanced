
from typing import overload

class EventBookmark():
    # Original docstring
    """
    A description of a bookmark on an event
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised EventBookmark.
        """
        pass
    
    @overload
    def __init__(self, other: 'EventBookmark'):
        """
        Construct a new EventBookmark with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, eventId: int):
        """
        Construct a new EventBookmark using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def text(self) -> str:
        """
        The text associated with this bookmark - could be empty
        
        :type: str
        """
        pass
    
    @text.setter
    def text(self, value: str):
        pass
    
    @property
    def eventId(self) -> int:
        """
        The :data:`eventId <renderdoc.APIEvent.eventId>` at which this bookmark is placed.
        
        :type: int
        """
        pass
    
    @eventId.setter
    def eventId(self, value: int):
        pass
    
