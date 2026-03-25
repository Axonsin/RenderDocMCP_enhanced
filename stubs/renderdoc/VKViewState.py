# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKRenderArea import VKRenderArea
from .VKViewportScissor import VKViewportScissor

class VKViewState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the view state in the pipeline. """
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
    def depthNegativeOneToOne(self) -> bool:
        """
Whether depth clip range is set to [-1, 1] through VK_EXT_depth_clip_control.

:type: bool

"""
        pass

    @depthNegativeOneToOne.setter
    def depthNegativeOneToOne(self, value: bool):
        pass

    @property
    def discardRectangles(self) -> List[VKRenderArea]:
        """
The discard rectangles, if enabled.

:type: List[VKRenderArea]

"""
        pass

    @discardRectangles.setter
    def discardRectangles(self, value: List[VKRenderArea]):
        pass

    @property
    def discardRectanglesExclusive(self) -> bool:
        """
``True`` if a fragment in any one of the discard rectangles fails the discard test,
and a fragment in none of them passes.

``False`` if a fragment in any one of the discard rectangles passes the discard test,
and a fragment in none of them is discarded.

.. note::
  A ``True`` value and an empty list of :data:`discardRectangles` means the test is effectively
  disabled, since with no rectangles no fragment can be inside one.

:type: bool

"""
        pass

    @discardRectanglesExclusive.setter
    def discardRectanglesExclusive(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def viewportScissors(self) -> List[VKViewportScissor]:
        """
The bound viewports and scissors.

:type: List[VKViewportScissor]

"""
        pass

    @viewportScissors.setter
    def viewportScissors(self, value: List[VKViewportScissor]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F5830>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKViewState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKViewState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKViewState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKViewState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKViewState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKViewState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKViewState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKViewState' objects>, 'discardRectanglesExclusive': <attribute 'discardRectanglesExclusive' of 'renderdoc.VKViewState' objects>, 'discardRectangles': <attribute 'discardRectangles' of 'renderdoc.VKViewState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKViewState' objects>, 'viewportScissors': <attribute 'viewportScissors' of 'renderdoc.VKViewState' objects>, 'depthNegativeOneToOne': <attribute 'depthNegativeOneToOne' of 'renderdoc.VKViewState' objects>, '__doc__': 'Describes the view state in the pipeline.'})"


