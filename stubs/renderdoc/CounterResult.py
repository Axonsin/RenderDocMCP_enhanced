# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CounterValue import CounterValue

class CounterResult(): # skipped bases: <class 'SwigPyObject'>
    """ The resulting value from a counter at an event. """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55225140>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CounterResult' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CounterResult' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CounterResult' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CounterResult' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CounterResult' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CounterResult' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CounterResult' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CounterResult' objects>, 'value': <attribute 'value' of 'renderdoc.CounterResult' objects>, 'counter': <attribute 'counter' of 'renderdoc.CounterResult' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CounterResult' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.CounterResult' objects>, '__doc__': 'The resulting value from a counter at an event.'})"


