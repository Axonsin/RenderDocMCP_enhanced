# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CounterValue(): # skipped bases: <class 'SwigPyObject'>
    """
    A resulting value from a GPU counter. Only one member is valid, see
    :class:`CounterDescription`.
    """
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
    def d(self) -> float:
        """
A ``double`` value.

:type: float

"""
        pass

    @d.setter
    def d(self, value: float):
        pass

    @property
    def f(self) -> float:
        """
A ``float`` value.

:type: float

"""
        pass

    @f.setter
    def f(self, value: float):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def u32(self) -> int:
        """
A 32-bit unsigned integer.

:type: int

"""
        pass

    @u32.setter
    def u32(self, value: int):
        pass

    @property
    def u64(self) -> int:
        """
A 64-bit unsigned integer.

:type: int

"""
        pass

    @u64.setter
    def u64(self, value: int):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CC750>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CounterValue' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CounterValue' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CounterValue' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CounterValue' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CounterValue' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CounterValue' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CounterValue' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CounterValue' objects>, 'f': <attribute 'f' of 'renderdoc.CounterValue' objects>, 'u64': <attribute 'u64' of 'renderdoc.CounterValue' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CounterValue' objects>, 'u32': <attribute 'u32' of 'renderdoc.CounterValue' objects>, 'd': <attribute 'd' of 'renderdoc.CounterValue' objects>, '__doc__': '\\nA resulting value from a GPU counter. Only one member is valid, see\\n:class:`CounterDescription`.\\n\\n'})"


