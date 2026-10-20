from renderdoc import CaptureOptions, EnvironmentModification
from typing import List

from typing import overload

class CaptureSettings():
    # Original docstring
    """
    Contains all of the settings that control how to capture an executable.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CaptureSettings.
        """
        pass
    
    @overload
    def __init__(self, other: 'CaptureSettings'):
        """
        Construct a new CaptureSettings with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def environment(self) -> List[EnvironmentModification]:
        """
        The environment changes to apply.
        
        :type: List[renderdoc.EnvironmentModification]
        """
        pass
    
    @environment.setter
    def environment(self, value: List[EnvironmentModification]):
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
    def queuedFrameCap(self) -> int:
        """
        The first queued frame to capture. Ignored if :data:`numQueuedFrames` is 0.
        
        :type: int
        """
        pass
    
    @queuedFrameCap.setter
    def queuedFrameCap(self, value: int):
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
    def workingDir(self) -> str:
        """
        The path to the working directory to run in, or blank for the executable's directory.
        
        :type: str
        """
        pass
    
    @workingDir.setter
    def workingDir(self, value: str):
        pass
    
