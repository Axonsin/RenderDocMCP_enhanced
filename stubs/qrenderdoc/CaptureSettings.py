# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.CaptureOptions import CaptureOptions

from renderdoc.EnvironmentModification import EnvironmentModification

class CaptureSettings(): # skipped bases: <class 'SwigPyObject'>
    """ Contains all of the settings that control how to capture an executable. """
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
    def autoStart(self) -> bool:
        """
``True`` if this capture settings object should be immediately executed upon load.

:type: bool

"""
        pass

    @autoStart.setter
    def autoStart(self, value: bool):
        pass

    @property
    def commandLine(self) -> str:
        """
The command line to pass when running :data:`executable`.

:type: str

"""
        pass

    @commandLine.setter
    def commandLine(self, value: str):
        pass

    @property
    def environment(self) -> EnvironmentModification]:
        """
The environment changes to apply.

:type: List[renderdoc.EnvironmentModification]

"""
        pass

    @environment.setter
    def environment(self, value: EnvironmentModification]):
        pass

    @property
    def executable(self) -> str:
        """
The path to the executable to run.

:type: str

"""
        pass

    @executable.setter
    def executable(self, value: str):
        pass

    @property
    def inject(self) -> bool:
        """
``True`` if the described capture is an inject-into-process instead of a launched executable.

:type: bool

"""
        pass

    @inject.setter
    def inject(self, value: bool):
        pass

    @property
    def numQueuedFrames(self) -> int:
        """
The number of queued frames to capture, or 0 if no frames are queued to be captured.

:type: int

"""
        pass

    @numQueuedFrames.setter
    def numQueuedFrames(self, value: int):
        pass

    @property
    def options(self) -> CaptureOptions:
        """
The settings for the capture.

:type: renderdoc.CaptureOptions

"""
        pass

    @options.setter
    def options(self, value: CaptureOptions):
        pass

    @property
    def queuedFrameCap(self) -> int:
        """
The first queued frame to capture. Ignored if :data:`numQueuedFrames` is 0.

:type: int

"""
        pass

    @queuedFrameCap.setter
    def queuedFrameCap(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def workingDir(self) -> str:
        """
The path to the working directory to run in, or blank for the executable's directory.

:type: str

"""
        pass

    @workingDir.setter
    def workingDir(self, value: str):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50133D10>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.CaptureSettings' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.CaptureSettings' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.CaptureSettings' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.CaptureSettings' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.CaptureSettings' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.CaptureSettings' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.CaptureSettings' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.CaptureSettings' objects>, 'numQueuedFrames': <attribute 'numQueuedFrames' of 'qrenderdoc.CaptureSettings' objects>, 'environment': <attribute 'environment' of 'qrenderdoc.CaptureSettings' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.CaptureSettings' objects>, 'executable': <attribute 'executable' of 'qrenderdoc.CaptureSettings' objects>, 'commandLine': <attribute 'commandLine' of 'qrenderdoc.CaptureSettings' objects>, 'inject': <attribute 'inject' of 'qrenderdoc.CaptureSettings' objects>, 'queuedFrameCap': <attribute 'queuedFrameCap' of 'qrenderdoc.CaptureSettings' objects>, 'options': <attribute 'options' of 'qrenderdoc.CaptureSettings' objects>, 'autoStart': <attribute 'autoStart' of 'qrenderdoc.CaptureSettings' objects>, 'workingDir': <attribute 'workingDir' of 'qrenderdoc.CaptureSettings' objects>, '__doc__': 'Contains all of the settings that control how to capture an executable.'})"


