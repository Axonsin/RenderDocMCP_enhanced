# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FilterFunction import FilterFunction
from .FilterMode import FilterMode

class TextureFilter(): # skipped bases: <class 'SwigPyObject'>
    """ The details of a texture filter in a sampler. """
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
    def filter(self) -> FilterFunction:
        """
The :class:`FilterFunction` to apply after interpolating values.

:type: FilterFunction

"""
        pass

    @filter.setter
    def filter(self, value: FilterFunction):
        pass

    @property
    def magnify(self) -> FilterMode:
        """
The :class:`FilterMode` to use when magnifying the texture.

:type: FilterMode

"""
        pass

    @magnify.setter
    def magnify(self, value: FilterMode):
        pass

    @property
    def minify(self) -> FilterMode:
        """
The :class:`FilterMode` to use when minifying the texture.

:type: FilterMode

"""
        pass

    @minify.setter
    def minify(self, value: FilterMode):
        pass

    @property
    def mip(self) -> FilterMode:
        """
The :class:`FilterMode` to use when interpolating between mips.

:type: FilterMode

"""
        pass

    @mip.setter
    def mip(self, value: FilterMode):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55221DE0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureFilter' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureFilter' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureFilter' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureFilter' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureFilter' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureFilter' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureFilter' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureFilter' objects>, 'magnify': <attribute 'magnify' of 'renderdoc.TextureFilter' objects>, 'minify': <attribute 'minify' of 'renderdoc.TextureFilter' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureFilter' objects>, 'filter': <attribute 'filter' of 'renderdoc.TextureFilter' objects>, 'mip': <attribute 'mip' of 'renderdoc.TextureFilter' objects>, '__doc__': 'The details of a texture filter in a sampler.'})"


