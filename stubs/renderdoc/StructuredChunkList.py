# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class StructuredChunkList(): # skipped bases: <class 'SwigPyObject'>
    """ INTERNAL: An array of SDChunk*, mapped to a pure list in python """
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F7540>, '__repr__': <slot wrapper '__repr__' of 'renderdoc.StructuredChunkList' objects>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.StructuredChunkList' objects>, '__str__': <slot wrapper '__str__' of 'renderdoc.StructuredChunkList' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.StructuredChunkList' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.StructuredChunkList' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.StructuredChunkList' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.StructuredChunkList' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.StructuredChunkList' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.StructuredChunkList' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.StructuredChunkList' objects>, '__getitem__': <slot wrapper '__getitem__' of 'renderdoc.StructuredChunkList' objects>, '__setitem__': <slot wrapper '__setitem__' of 'renderdoc.StructuredChunkList' objects>, '__delitem__': <slot wrapper '__delitem__' of 'renderdoc.StructuredChunkList' objects>, '__len__': <slot wrapper '__len__' of 'renderdoc.StructuredChunkList' objects>, '__add__': <slot wrapper '__add__' of 'renderdoc.StructuredChunkList' objects>, '__mul__': <slot wrapper '__mul__' of 'renderdoc.StructuredChunkList' objects>, '__rmul__': <slot wrapper '__rmul__' of 'renderdoc.StructuredChunkList' objects>, '__iadd__': <slot wrapper '__iadd__' of 'renderdoc.StructuredChunkList' objects>, '__imul__': <slot wrapper '__imul__' of 'renderdoc.StructuredChunkList' objects>, 'append': <method 'append' of 'renderdoc.StructuredChunkList' objects>, 'clear': <method 'clear' of 'renderdoc.StructuredChunkList' objects>, 'insert': <method 'insert' of 'renderdoc.StructuredChunkList' objects>, 'pop': <method 'pop' of 'renderdoc.StructuredChunkList' objects>, 'sort': <method 'sort' of 'renderdoc.StructuredChunkList' objects>, 'copy': <method 'copy' of 'renderdoc.StructuredChunkList' objects>, 'reverse': <method 'reverse' of 'renderdoc.StructuredChunkList' objects>, 'index': <method 'index' of 'renderdoc.StructuredChunkList' objects>, 'count': <method 'count' of 'renderdoc.StructuredChunkList' objects>, 'extend': <method 'extend' of 'renderdoc.StructuredChunkList' objects>, 'remove': <method 'remove' of 'renderdoc.StructuredChunkList' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.StructuredChunkList' objects>, '__doc__': 'INTERNAL: An array of SDChunk*, mapped to a pure list in python'})"


