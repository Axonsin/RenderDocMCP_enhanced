# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ConstantBindStats(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the statistics for constant binds in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
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
    def bindslots(self) -> List[int]:
        """
A list where the Nth element contains the number of calls that bound N buffers.

:type: List[int]

"""
        pass

    @bindslots.setter
    def bindslots(self, value: List[int]):
        pass

    @property
    def calls(self) -> int:
        """
How many function calls were made.

:type: int

"""
        pass

    @calls.setter
    def calls(self, value: int):
        pass

    @property
    def nulls(self) -> int:
        """
How many objects were unbound.

:type: int

"""
        pass

    @nulls.setter
    def nulls(self, value: int):
        pass

    @property
    def sets(self) -> int:
        """
How many objects were bound.

:type: int

"""
        pass

    @sets.setter
    def sets(self, value: int):
        pass

    @property
    def sizes(self) -> List[int]:
        """
A :class:`bucketed <BucketType>` list over the sizes of buffers bound.

:type: List[int]

"""
        pass

    @sizes.setter
    def sizes(self, value: List[int]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BucketCount = 31
    BucketType = 1
    __dict__ = None # (!) real value is "mappingproxy({'BucketType': 1, 'BucketCount': 31, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551BEF30>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ConstantBindStats' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ConstantBindStats' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ConstantBindStats' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ConstantBindStats' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ConstantBindStats' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ConstantBindStats' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ConstantBindStats' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ConstantBindStats' objects>, 'calls': <attribute 'calls' of 'renderdoc.ConstantBindStats' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ConstantBindStats' objects>, 'sizes': <attribute 'sizes' of 'renderdoc.ConstantBindStats' objects>, 'sets': <attribute 'sets' of 'renderdoc.ConstantBindStats' objects>, 'bindslots': <attribute 'bindslots' of 'renderdoc.ConstantBindStats' objects>, 'nulls': <attribute 'nulls' of 'renderdoc.ConstantBindStats' objects>, '__doc__': '\\nContains the statistics for constant binds in a frame.\\n\\n.. data:: BucketType\\n\\n  The type of buckets being used. See :class:`BucketRecordType`.\\n\\n.. data:: BucketCount\\n\\n  How many buckets there are in the arrays.\\n\\n'})"


