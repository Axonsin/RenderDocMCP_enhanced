# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKFramebuffer import VKFramebuffer
from .VKRenderArea import VKRenderArea
from .VKRenderPass import VKRenderPass

class VKCurrentPass(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the current pass instance at the current time. """
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
    def colorFeedbackAllowed(self) -> bool:
        """
If feedback loops are allowed on color attachments

:type: bool

"""
        pass

    @colorFeedbackAllowed.setter
    def colorFeedbackAllowed(self, value: bool):
        pass

    @property
    def depthFeedbackAllowed(self) -> bool:
        """
If feedback loops are allowed on depth attachments

:type: bool

"""
        pass

    @depthFeedbackAllowed.setter
    def depthFeedbackAllowed(self, value: bool):
        pass

    @property
    def framebuffer(self) -> VKFramebuffer:
        """
The framebuffer that is currently being used.

:type: VKFramebuffer

"""
        pass

    @framebuffer.setter
    def framebuffer(self, value: VKFramebuffer):
        pass

    @property
    def renderArea(self) -> VKRenderArea:
        """
The render area that is currently being rendered to.

:type: VKRenderArea

"""
        pass

    @renderArea.setter
    def renderArea(self, value: VKRenderArea):
        pass

    @property
    def renderpass(self) -> VKRenderPass:
        """
The renderpass and subpass that is currently active.

:type: VKRenderPass

"""
        pass

    @renderpass.setter
    def renderpass(self, value: VKRenderPass):
        pass

    @property
    def stencilFeedbackAllowed(self) -> bool:
        """
If feedback loops are allowed on stencil attachments

:type: bool

"""
        pass

    @stencilFeedbackAllowed.setter
    def stencilFeedbackAllowed(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552064B0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKCurrentPass' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKCurrentPass' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKCurrentPass' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKCurrentPass' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKCurrentPass' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKCurrentPass' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKCurrentPass' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKCurrentPass' objects>, 'renderpass': <attribute 'renderpass' of 'renderdoc.VKCurrentPass' objects>, 'framebuffer': <attribute 'framebuffer' of 'renderdoc.VKCurrentPass' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKCurrentPass' objects>, 'renderArea': <attribute 'renderArea' of 'renderdoc.VKCurrentPass' objects>, 'colorFeedbackAllowed': <attribute 'colorFeedbackAllowed' of 'renderdoc.VKCurrentPass' objects>, 'depthFeedbackAllowed': <attribute 'depthFeedbackAllowed' of 'renderdoc.VKCurrentPass' objects>, 'stencilFeedbackAllowed': <attribute 'stencilFeedbackAllowed' of 'renderdoc.VKCurrentPass' objects>, '__doc__': 'Describes the current pass instance at the current time.'})"


