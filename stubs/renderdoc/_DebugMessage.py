from ._MessageCategory import MessageCategory
from ._MessageSeverity import MessageSeverity
from ._MessageSource import MessageSource

from typing import overload

class DebugMessage():
    # Original docstring
    """
    A debugging message from the API validation or internal analysis and error detection.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DebugMessage.
        """
        pass
    
    @overload
    def __init__(self, other: 'DebugMessage'):
        """
        Construct a new DebugMessage with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def severity(self) -> MessageSeverity:
        """
        The :class:`severity <MessageSeverity>` of this debug message.
        
        :type: MessageSeverity
        """
        pass
    
    @severity.setter
    def severity(self, value: MessageSeverity):
        pass
    
    @property
    def messageID(self) -> int:
        """
        An ID that identifies this particular debug message uniquely.
        
        :type: int
        """
        pass
    
    @messageID.setter
    def messageID(self, value: int):
        pass
    
    @property
    def eventId(self) -> int:
        """
        The :data:`eventId <APIEvent.eventId>` where this debug message was found.
        
        :type: int
        """
        pass
    
    @eventId.setter
    def eventId(self, value: int):
        pass
    
    @property
    def source(self) -> MessageSource:
        """
        The :class:`source <MessageSource>` of this debug message.
        
        :type: MessageSource
        """
        pass
    
    @source.setter
    def source(self, value: MessageSource):
        pass
    
    @property
    def category(self) -> MessageCategory:
        """
        The :class:`category <MessageCategory>` of this debug message.
        
        :type: MessageCategory
        """
        pass
    
    @category.setter
    def category(self, value: MessageCategory):
        pass
    
    @property
    def description(self) -> str:
        """
        The string contents of the message.
        
        :type: str
        """
        pass
    
    @description.setter
    def description(self, value: str):
        pass
    
