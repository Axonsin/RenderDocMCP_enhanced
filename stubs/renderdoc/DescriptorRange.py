# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorType import DescriptorType

class DescriptorRange(): # skipped bases: <class 'SwigPyObject'>
    """ A range of sized descriptors. """
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
    def count(self) -> int:
        """
The number of descriptors in this range.

:type: int

"""
        pass

    @count.setter
    def count(self, value: int):
        pass

    @property
    def descriptorSize(self) -> int:
        """
The size of each descriptor in the range.

:type: int

"""
        pass

    @descriptorSize.setter
    def descriptorSize(self, value: int):
        pass

    @property
    def offset(self) -> int:
        """
The offset in the descriptor storage where the descriptor range starts.

:type: int

"""
        pass

    @offset.setter
    def offset(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> DescriptorType:
        """
The type of descriptor in the descriptor range.

:type: DescriptorType

"""
        pass

    @type.setter
    def type(self, value: DescriptorType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B30F0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DescriptorRange' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DescriptorRange' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DescriptorRange' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DescriptorRange' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DescriptorRange' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DescriptorRange' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DescriptorRange' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DescriptorRange' objects>, 'descriptorSize': <attribute 'descriptorSize' of 'renderdoc.DescriptorRange' objects>, 'count': <attribute 'count' of 'renderdoc.DescriptorRange' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DescriptorRange' objects>, 'offset': <attribute 'offset' of 'renderdoc.DescriptorRange' objects>, 'type': <attribute 'type' of 'renderdoc.DescriptorRange' objects>, '__doc__': 'A range of sized descriptors.'})"


