# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceUsage import ResourceUsage
from .ResourceId import ResourceId

class EventUsage(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`. """
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
    def eventId(self) -> int:
        """
The :data:`eventId <APIEvent.eventId>` where this usage happened.

:type: int

"""
        pass

    @eventId.setter
    def eventId(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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

    @property
    def view(self) -> ResourceId:
        """
An optional :class:`ResourceId` identifying the view through which the use happened.

:type: ResourceId

"""
        pass

    @view.setter
    def view(self, value: ResourceId):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C3EA0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.EventUsage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.EventUsage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.EventUsage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.EventUsage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.EventUsage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.EventUsage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.EventUsage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.EventUsage' objects>, 'view': <attribute 'view' of 'renderdoc.EventUsage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.EventUsage' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.EventUsage' objects>, 'usage': <attribute 'usage' of 'renderdoc.EventUsage' objects>, '__doc__': 'Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`.'})"


