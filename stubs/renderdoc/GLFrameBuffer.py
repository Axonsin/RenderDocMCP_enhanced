# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GLBlendState import GLBlendState
from .GLFBO import GLFBO

class GLFrameBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the current state of the framebuffer stage of the pipeline. """
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
    def blendState(self) -> GLBlendState:
        """
The details of the blending state.

:type: GLBlendState

"""
        pass

    @blendState.setter
    def blendState(self, value: GLBlendState):
        pass

    @property
    def dither(self) -> bool:
        """
``True`` if dithering should be used when writing to color buffers.

:type: bool

"""
        pass

    @dither.setter
    def dither(self, value: bool):
        pass

    @property
    def drawFBO(self) -> GLFBO:
        """
The draw framebuffer.

:type: GLFBO

"""
        pass

    @drawFBO.setter
    def drawFBO(self, value: GLFBO):
        pass

    @property
    def framebufferSRGB(self) -> bool:
        """
``True`` if sRGB correction should be applied when writing to an sRGB-formatted texture.

:type: bool

"""
        pass

    @framebufferSRGB.setter
    def framebufferSRGB(self, value: bool):
        pass

    @property
    def readFBO(self) -> GLFBO:
        """
The read framebuffer.

:type: GLFBO

"""
        pass

    @readFBO.setter
    def readFBO(self, value: GLFBO):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551BC350>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLFrameBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLFrameBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLFrameBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLFrameBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLFrameBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLFrameBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLFrameBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLFrameBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLFrameBuffer' objects>, 'framebufferSRGB': <attribute 'framebufferSRGB' of 'renderdoc.GLFrameBuffer' objects>, 'drawFBO': <attribute 'drawFBO' of 'renderdoc.GLFrameBuffer' objects>, 'dither': <attribute 'dither' of 'renderdoc.GLFrameBuffer' objects>, 'blendState': <attribute 'blendState' of 'renderdoc.GLFrameBuffer' objects>, 'readFBO': <attribute 'readFBO' of 'renderdoc.GLFrameBuffer' objects>, '__doc__': 'Describes the current state of the framebuffer stage of the pipeline.'})"


