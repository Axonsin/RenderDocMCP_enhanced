# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .MessageCategory import MessageCategory
from .MessageSeverity import MessageSeverity
from .MessageSource import MessageSource

class DebugMessage(): # skipped bases: <class 'SwigPyObject'>
    """ A debugging message from the API validation or internal analysis and error detection. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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
    def source(self) -> MessageSource:
        """
The :class:`source <MessageSource>` of this debug message.

:type: MessageSource

"""
        pass

    @source.setter
    def source(self, value: MessageSource):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520F1D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DebugMessage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DebugMessage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DebugMessage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DebugMessage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DebugMessage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DebugMessage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DebugMessage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DebugMessage' objects>, 'severity': <attribute 'severity' of 'renderdoc.DebugMessage' objects>, 'messageID': <attribute 'messageID' of 'renderdoc.DebugMessage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DebugMessage' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.DebugMessage' objects>, 'source': <attribute 'source' of 'renderdoc.DebugMessage' objects>, 'category': <attribute 'category' of 'renderdoc.DebugMessage' objects>, 'description': <attribute 'description' of 'renderdoc.DebugMessage' objects>, '__doc__': 'A debugging message from the API validation or internal analysis and error detection.'})"


