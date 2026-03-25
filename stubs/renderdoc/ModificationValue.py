# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .PixelValue import PixelValue

class ModificationValue(): # skipped bases: <class 'SwigPyObject'>
    """ The value of pixel output at a particular event. """
    def IsValid(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsValid()
        
        
        :return: Returns whether or not this modification value is valid.
        :rtype: bool
        """
        pass

    def SetInvalid(self): # real signature unknown; restored from __doc__
        """
        SetInvalid()
        
        Sets this modification value to be invalid.
        """
        pass

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
    def col(self) -> PixelValue:
        """
The color value.

If the modifications are for a color target, tthe contents will all be ``0``.

:type: PixelValue

"""
        pass

    @col.setter
    def col(self, value: PixelValue):
        pass

    @property
    def depth(self) -> float:
        """
The depth value.

If depth is not available/in-use for this modification, it will be ``-1.0``.

:type: float

"""
        pass

    @depth.setter
    def depth(self, value: float):
        pass

    @property
    def stencil(self) -> int:
        """
The stencil value.

If stencil is not available for this modification, it will be negative. If stencil is not available
at all and not in use then the stencil value will be ``-1``. If stencil was in use but can't be
determined due to the pixel history implementation using stencil for its own purposes, the value
will be ``-2``. This will only happen when looking at multiple modifications from the same event.

:type: int

"""
        pass

    @stencil.setter
    def stencil(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522C930>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ModificationValue' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ModificationValue' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ModificationValue' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ModificationValue' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ModificationValue' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ModificationValue' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ModificationValue' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ModificationValue' objects>, 'IsValid': <method 'IsValid' of 'renderdoc.ModificationValue' objects>, 'SetInvalid': <method 'SetInvalid' of 'renderdoc.ModificationValue' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ModificationValue' objects>, 'depth': <attribute 'depth' of 'renderdoc.ModificationValue' objects>, 'col': <attribute 'col' of 'renderdoc.ModificationValue' objects>, 'stencil': <attribute 'stencil' of 'renderdoc.ModificationValue' objects>, '__doc__': 'The value of pixel output at a particular event.'})"


