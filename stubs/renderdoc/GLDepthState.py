# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CompareFunction import CompareFunction

class GLDepthState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the depth state. """
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
    def depthBounds(self) -> bool:
        """
``True`` if depth bounds tests should be applied.

:type: bool

"""
        pass

    @depthBounds.setter
    def depthBounds(self, value: bool):
        pass

    @property
    def depthEnable(self) -> bool:
        """
``True`` if depth testing should be performed.

:type: bool

"""
        pass

    @depthEnable.setter
    def depthEnable(self, value: bool):
        pass

    @property
    def depthFunction(self) -> CompareFunction:
        """
The :class:`CompareFunction` to use for testing depth values.

:type: CompareFunction

"""
        pass

    @depthFunction.setter
    def depthFunction(self, value: CompareFunction):
        pass

    @property
    def depthWrites(self) -> bool:
        """
``True`` if depth values should be written to the depth target.

:type: bool

"""
        pass

    @depthWrites.setter
    def depthWrites(self, value: bool):
        pass

    @property
    def farBound(self) -> float:
        """
The far plane bounding value.

:type: float

"""
        pass

    @farBound.setter
    def farBound(self, value: float):
        pass

    @property
    def nearBound(self) -> float:
        """
The near plane bounding value.

:type: float

"""
        pass

    @nearBound.setter
    def nearBound(self, value: float):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55219170>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLDepthState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLDepthState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLDepthState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLDepthState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLDepthState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLDepthState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLDepthState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLDepthState' objects>, 'depthFunction': <attribute 'depthFunction' of 'renderdoc.GLDepthState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLDepthState' objects>, 'nearBound': <attribute 'nearBound' of 'renderdoc.GLDepthState' objects>, 'farBound': <attribute 'farBound' of 'renderdoc.GLDepthState' objects>, 'depthBounds': <attribute 'depthBounds' of 'renderdoc.GLDepthState' objects>, 'depthEnable': <attribute 'depthEnable' of 'renderdoc.GLDepthState' objects>, 'depthWrites': <attribute 'depthWrites' of 'renderdoc.GLDepthState' objects>, '__doc__': 'Describes the depth state.'})"


