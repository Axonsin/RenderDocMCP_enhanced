# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .APIUseData import APIUseData
from .BusyData import BusyData
from .NewCaptureData import NewCaptureData
from .NewChildData import NewChildData
from .TargetControlMessageType import TargetControlMessageType

class TargetControlMessage(): # skipped bases: <class 'SwigPyObject'>
    """ A message from a target control connection. """
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
    def apiUse(self) -> APIUseData:
        """
The API use data.

:type: APIUseData

"""
        pass

    @apiUse.setter
    def apiUse(self, value: APIUseData):
        pass

    @property
    def busy(self) -> BusyData:
        """
The busy signal data.

:type: BusyData

"""
        pass

    @busy.setter
    def busy(self, value: BusyData):
        pass

    @property
    def capProgress(self) -> float:
        """
The progress of an on-going capture.

When valid, will be in the range of 0.0 to 1.0 (0 - 100%). If not valid when a capture isn't going
or has finished, it will be -1.0

:type: float

"""
        pass

    @capProgress.setter
    def capProgress(self, value: float):
        pass

    @property
    def capturableWindowCount(self) -> int:
        """
The number of the capturable windows

:type: int

"""
        pass

    @capturableWindowCount.setter
    def capturableWindowCount(self, value: int):
        pass

    @property
    def newCapture(self) -> NewCaptureData:
        """
The new capture data.

:type: NewCaptureData

"""
        pass

    @newCapture.setter
    def newCapture(self, value: NewCaptureData):
        pass

    @property
    def newChild(self) -> NewChildData:
        """
The new child process data.

:type: NewChildData

"""
        pass

    @newChild.setter
    def newChild(self, value: NewChildData):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> TargetControlMessageType:
        """
The :class:`type <TargetControlMessageType>` of message received

:type: TargetControlMessageType

"""
        pass

    @type.setter
    def type(self, value: TargetControlMessageType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551DF4C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TargetControlMessage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TargetControlMessage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TargetControlMessage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TargetControlMessage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TargetControlMessage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TargetControlMessage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TargetControlMessage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TargetControlMessage' objects>, 'newCapture': <attribute 'newCapture' of 'renderdoc.TargetControlMessage' objects>, 'busy': <attribute 'busy' of 'renderdoc.TargetControlMessage' objects>, 'apiUse': <attribute 'apiUse' of 'renderdoc.TargetControlMessage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TargetControlMessage' objects>, 'type': <attribute 'type' of 'renderdoc.TargetControlMessage' objects>, 'newChild': <attribute 'newChild' of 'renderdoc.TargetControlMessage' objects>, 'capProgress': <attribute 'capProgress' of 'renderdoc.TargetControlMessage' objects>, 'capturableWindowCount': <attribute 'capturableWindowCount' of 'renderdoc.TargetControlMessage' objects>, '__doc__': 'A message from a target control connection.'})"


