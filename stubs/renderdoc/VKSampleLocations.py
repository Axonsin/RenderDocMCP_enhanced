# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FloatVector import FloatVector

class VKSampleLocations(): # skipped bases: <class 'SwigPyObject'>
    """ Describes state of custom sample locations in the pipeline. """
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
    def customLocations(self) -> List[FloatVector]:
        """
The custom sample locations. Only x and y are valid, z and w are set to 0.0.

If the list is empty then the standard sample pattern is in use.

:type: List[FloatVector]

"""
        pass

    @customLocations.setter
    def customLocations(self, value: List[FloatVector]):
        pass

    @property
    def gridHeight(self) -> int:
        """
The height in pixels of the region configured.

:type: int

"""
        pass

    @gridHeight.setter
    def gridHeight(self, value: int):
        pass

    @property
    def gridWidth(self) -> int:
        """
The width in pixels of the region configured.

:type: int

"""
        pass

    @gridWidth.setter
    def gridWidth(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B06D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKSampleLocations' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKSampleLocations' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKSampleLocations' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKSampleLocations' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKSampleLocations' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKSampleLocations' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKSampleLocations' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKSampleLocations' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKSampleLocations' objects>, 'gridHeight': <attribute 'gridHeight' of 'renderdoc.VKSampleLocations' objects>, 'customLocations': <attribute 'customLocations' of 'renderdoc.VKSampleLocations' objects>, 'gridWidth': <attribute 'gridWidth' of 'renderdoc.VKSampleLocations' objects>, '__doc__': 'Describes state of custom sample locations in the pipeline.'})"


