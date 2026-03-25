# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .QualityHint import QualityHint

class GLHints(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the current state of GL hints and smoothing. """
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
    def derivatives(self) -> QualityHint:
        """
A :class:`QualityHint` with the derivatives hint.

:type: QualityHint

"""
        pass

    @derivatives.setter
    def derivatives(self, value: QualityHint):
        pass

    @property
    def lineSmoothing(self) -> QualityHint:
        """
A :class:`QualityHint` with the line smoothing hint.

:type: QualityHint

"""
        pass

    @lineSmoothing.setter
    def lineSmoothing(self, value: QualityHint):
        pass

    @property
    def lineSmoothingEnabled(self) -> bool:
        """
``True`` if line smoothing is enabled.

:type: bool

"""
        pass

    @lineSmoothingEnabled.setter
    def lineSmoothingEnabled(self, value: bool):
        pass

    @property
    def polySmoothing(self) -> QualityHint:
        """
A :class:`QualityHint` with the polygon smoothing hint.

:type: QualityHint

"""
        pass

    @polySmoothing.setter
    def polySmoothing(self, value: QualityHint):
        pass

    @property
    def polySmoothingEnabled(self) -> bool:
        """
``True`` if polygon smoothing is enabled.

:type: bool

"""
        pass

    @polySmoothingEnabled.setter
    def polySmoothingEnabled(self, value: bool):
        pass

    @property
    def textureCompression(self) -> QualityHint:
        """
A :class:`QualityHint` with the texture compression hint.

:type: QualityHint

"""
        pass

    @textureCompression.setter
    def textureCompression(self, value: QualityHint):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55226670>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLHints' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLHints' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLHints' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLHints' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLHints' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLHints' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLHints' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLHints' objects>, 'lineSmoothingEnabled': <attribute 'lineSmoothingEnabled' of 'renderdoc.GLHints' objects>, 'polySmoothingEnabled': <attribute 'polySmoothingEnabled' of 'renderdoc.GLHints' objects>, 'derivatives': <attribute 'derivatives' of 'renderdoc.GLHints' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLHints' objects>, 'textureCompression': <attribute 'textureCompression' of 'renderdoc.GLHints' objects>, 'lineSmoothing': <attribute 'lineSmoothing' of 'renderdoc.GLHints' objects>, 'polySmoothing': <attribute 'polySmoothing' of 'renderdoc.GLHints' objects>, '__doc__': 'Describes the current state of GL hints and smoothing.'})"


