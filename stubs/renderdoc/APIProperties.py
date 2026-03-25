# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GraphicsAPI import GraphicsAPI
from .GPUVendor import GPUVendor

class APIProperties(): # skipped bases: <class 'SwigPyObject'>
    """ Gives some API-specific information about the capture. """
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
    def degraded(self) -> bool:
        """
``True`` if the capture was loaded successfully but running in a degraded mode - e.g.
with software rendering, or with some functionality disabled due to lack of support.

:type: bool

"""
        pass

    @degraded.setter
    def degraded(self, value: bool):
        pass

    @property
    def localRenderer(self) -> GraphicsAPI:
        """
The :class:`GraphicsAPI` used to render the log. For remote replay this could be
different to the above, and lets the UI make decisions e.g. to flip rendering of images.

:type: GraphicsAPI

"""
        pass

    @localRenderer.setter
    def localRenderer(self, value: GraphicsAPI):
        pass

    @property
    def pipelineType(self) -> GraphicsAPI:
        """
The :class:`GraphicsAPI` of the actual log/capture.

:type: GraphicsAPI

"""
        pass

    @pipelineType.setter
    def pipelineType(self, value: GraphicsAPI):
        pass

    @property
    def pixelHistory(self) -> bool:
        """
``True`` if the API supports viewing pixel history.

:type: bool

"""
        pass

    @pixelHistory.setter
    def pixelHistory(self, value: bool):
        pass

    @property
    def remoteReplay(self) -> bool:
        """
``True`` if the capture is being replayed over a remote connection.

:type: bool

"""
        pass

    @remoteReplay.setter
    def remoteReplay(self, value: bool):
        pass

    @property
    def rgpCapture(self) -> bool:
        """
``True`` if the driver and system are configured to allow creating RGP captures.

:type: bool

"""
        pass

    @rgpCapture.setter
    def rgpCapture(self, value: bool):
        pass

    @property
    def shaderDebugging(self) -> bool:
        """
``True`` if the API supports shader debugging.

:type: bool

"""
        pass

    @shaderDebugging.setter
    def shaderDebugging(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vendor(self) -> GPUVendor:
        """
The :class:`GPUVendor` of the active GPU being used.

:type: GPUVendor

"""
        pass

    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520D630>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.APIProperties' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.APIProperties' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.APIProperties' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.APIProperties' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.APIProperties' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.APIProperties' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.APIProperties' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.APIProperties' objects>, 'degraded': <attribute 'degraded' of 'renderdoc.APIProperties' objects>, 'rgpCapture': <attribute 'rgpCapture' of 'renderdoc.APIProperties' objects>, 'pixelHistory': <attribute 'pixelHistory' of 'renderdoc.APIProperties' objects>, 'remoteReplay': <attribute 'remoteReplay' of 'renderdoc.APIProperties' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.APIProperties' objects>, 'pipelineType': <attribute 'pipelineType' of 'renderdoc.APIProperties' objects>, 'shaderDebugging': <attribute 'shaderDebugging' of 'renderdoc.APIProperties' objects>, 'vendor': <attribute 'vendor' of 'renderdoc.APIProperties' objects>, 'localRenderer': <attribute 'localRenderer' of 'renderdoc.APIProperties' objects>, '__doc__': 'Gives some API-specific information about the capture.'})"


