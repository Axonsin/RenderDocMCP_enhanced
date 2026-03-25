# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CompType import CompType
from .CounterUnit import CounterUnit
from .Uuid import Uuid

class CounterDescription(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a GPU counter's purpose and result value. """
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
    def resultByteWidth(self) -> int:
        """
The number of bytes in the resulting value.

:type: int

"""
        pass

    @resultByteWidth.setter
    def resultByteWidth(self, value: int):
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    def uuid(self) -> Uuid:
        """
The unique identifier for this counter that will not change across drivers or replays.

:type: Uuid

"""
        pass

    @uuid.setter
    def uuid(self, value: Uuid):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E6430>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.CounterDescription\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.CounterDescription\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.CounterDescription\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.CounterDescription\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.CounterDescription\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.CounterDescription\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.CounterDescription\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.CounterDescription\' objects>, \'uuid\': <attribute \'uuid\' of \'renderdoc.CounterDescription\' objects>, \'name\': <attribute \'name\' of \'renderdoc.CounterDescription\' objects>, \'counter\': <attribute \'counter\' of \'renderdoc.CounterDescription\' objects>, \'resultType\': <attribute \'resultType\' of \'renderdoc.CounterDescription\' objects>, \'unit\': <attribute \'unit\' of \'renderdoc.CounterDescription\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.CounterDescription\' objects>, \'category\': <attribute \'category\' of \'renderdoc.CounterDescription\' objects>, \'description\': <attribute \'description\' of \'renderdoc.CounterDescription\' objects>, \'resultByteWidth\': <attribute \'resultByteWidth\' of \'renderdoc.CounterDescription\' objects>, \'__doc__\': "Describes a GPU counter\'s purpose and result value."})'


