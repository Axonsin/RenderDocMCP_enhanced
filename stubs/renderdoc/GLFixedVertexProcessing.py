# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GLFixedVertexProcessing(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the setup for fixed vertex processing operations. """
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
    def clipNegativeOneToOne(self) -> bool:
        """
``True`` if the clip-space Z goes from ``-1`` to ``1``.

``False`` if the clip-space Z goes from ``0`` to ``1``.

:type: bool

"""
        pass

    @clipNegativeOneToOne.setter
    def clipNegativeOneToOne(self, value: bool):
        pass

    @property
    def clipOriginLowerLeft(self) -> bool:
        """
``True`` if the clipping origin should be in the lower left.

``False`` if it's in the upper left.

:type: bool

"""
        pass

    @clipOriginLowerLeft.setter
    def clipOriginLowerLeft(self, value: bool):
        pass

    @property
    def clipPlanes(self) -> Tuple[bool,...]:
        """
An 8-tuple of ``bool`` determining which user clipping planes are enabled.

:type: Tuple[bool,...]

"""
        pass

    @clipPlanes.setter
    def clipPlanes(self, value: Tuple[bool,...]):
        pass

    @property
    def defaultInnerLevel(self) -> Tuple[float,float]:
        """
A tuple of ``float`` giving the default inner level of tessellation.

:type: Tuple[float,float]

"""
        pass

    @defaultInnerLevel.setter
    def defaultInnerLevel(self, value: Tuple[float,float]):
        pass

    @property
    def defaultOuterLevel(self) -> Tuple[float,float,float,float]:
        """
A tuple of ``float`` giving the default outer level of tessellation.

:type: Tuple[float,float,float,float]

"""
        pass

    @defaultOuterLevel.setter
    def defaultOuterLevel(self, value: Tuple[float,float,float,float]):
        pass

    @property
    def discard(self) -> bool:
        """
``True`` if primitives should be discarded during rasterization.

:type: bool

"""
        pass

    @discard.setter
    def discard(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B7320>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLFixedVertexProcessing' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLFixedVertexProcessing' objects>, 'defaultInnerLevel': <attribute 'defaultInnerLevel' of 'renderdoc.GLFixedVertexProcessing' objects>, 'defaultOuterLevel': <attribute 'defaultOuterLevel' of 'renderdoc.GLFixedVertexProcessing' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLFixedVertexProcessing' objects>, 'clipPlanes': <attribute 'clipPlanes' of 'renderdoc.GLFixedVertexProcessing' objects>, 'clipOriginLowerLeft': <attribute 'clipOriginLowerLeft' of 'renderdoc.GLFixedVertexProcessing' objects>, 'discard': <attribute 'discard' of 'renderdoc.GLFixedVertexProcessing' objects>, 'clipNegativeOneToOne': <attribute 'clipNegativeOneToOne' of 'renderdoc.GLFixedVertexProcessing' objects>, '__doc__': 'Describes the setup for fixed vertex processing operations.'})"


