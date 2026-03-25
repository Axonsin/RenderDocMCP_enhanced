# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class StructuredBufferList(): # skipped bases: <class 'SwigPyObject'>
    """ INTERNAL: An array of bytebuf*, mapped to a pure list of bytes in python """
    def append(self, value): # real signature unknown; restored from __doc__
        """ append(value) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear() """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy() """
        pass

    def count(self, item): # real signature unknown; restored from __doc__
        """ count(item) """
        pass

    def extend(self, items): # real signature unknown; restored from __doc__
        """ extend(items) """
        pass

    def index(self, item, start=None, end=None): # real signature unknown; restored from __doc__
        """ index(item, start=None, end=None) """
        pass

    def insert(self, index, value): # real signature unknown; restored from __doc__
        """ insert(index, value) """
        pass

    def pop(self, index=None): # real signature unknown; restored from __doc__
        """ pop(index=None) """
        pass

    def remove(self, item): # real signature unknown; restored from __doc__
        """ remove(item) """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """ reverse() """
        pass

    def sort(self, key=None, reverse=False): # real signature unknown; restored from __doc__
        """ sort(key=None, reverse=False) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551FBA60>, '__repr__': <slot wrapper '__repr__' of 'renderdoc.StructuredBufferList' objects>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.StructuredBufferList' objects>, '__str__': <slot wrapper '__str__' of 'renderdoc.StructuredBufferList' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.StructuredBufferList' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.StructuredBufferList' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.StructuredBufferList' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.StructuredBufferList' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.StructuredBufferList' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.StructuredBufferList' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.StructuredBufferList' objects>, '__getitem__': <slot wrapper '__getitem__' of 'renderdoc.StructuredBufferList' objects>, '__setitem__': <slot wrapper '__setitem__' of 'renderdoc.StructuredBufferList' objects>, '__delitem__': <slot wrapper '__delitem__' of 'renderdoc.StructuredBufferList' objects>, '__len__': <slot wrapper '__len__' of 'renderdoc.StructuredBufferList' objects>, '__add__': <slot wrapper '__add__' of 'renderdoc.StructuredBufferList' objects>, '__mul__': <slot wrapper '__mul__' of 'renderdoc.StructuredBufferList' objects>, '__rmul__': <slot wrapper '__rmul__' of 'renderdoc.StructuredBufferList' objects>, '__iadd__': <slot wrapper '__iadd__' of 'renderdoc.StructuredBufferList' objects>, '__imul__': <slot wrapper '__imul__' of 'renderdoc.StructuredBufferList' objects>, 'append': <method 'append' of 'renderdoc.StructuredBufferList' objects>, 'clear': <method 'clear' of 'renderdoc.StructuredBufferList' objects>, 'insert': <method 'insert' of 'renderdoc.StructuredBufferList' objects>, 'pop': <method 'pop' of 'renderdoc.StructuredBufferList' objects>, 'sort': <method 'sort' of 'renderdoc.StructuredBufferList' objects>, 'copy': <method 'copy' of 'renderdoc.StructuredBufferList' objects>, 'reverse': <method 'reverse' of 'renderdoc.StructuredBufferList' objects>, 'index': <method 'index' of 'renderdoc.StructuredBufferList' objects>, 'count': <method 'count' of 'renderdoc.StructuredBufferList' objects>, 'extend': <method 'extend' of 'renderdoc.StructuredBufferList' objects>, 'remove': <method 'remove' of 'renderdoc.StructuredBufferList' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.StructuredBufferList' objects>, '__doc__': 'INTERNAL: An array of bytebuf*, mapped to a pure list of bytes in python'})"


