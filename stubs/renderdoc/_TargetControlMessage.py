from ._APIUseData import APIUseData
from ._BusyData import BusyData
from ._NewCaptureData import NewCaptureData
from ._NewChildData import NewChildData
from ._TargetControlMessageType import TargetControlMessageType

from typing import overload

class TargetControlMessage():
    # Original docstring
    """
    A message from a target control connection.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TargetControlMessage.
        """
        pass
    
    @overload
    def __init__(self, other: 'TargetControlMessage'):
        """
        Construct a new TargetControlMessage with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def type(self) -> TargetControlMessageType:
        """
        The :class:`type <TargetControlMessageType>` of message received
        
        :type: TargetControlMessageType
        """
        pass
    
    @type.setter
    def type(self, value: TargetControlMessageType):
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
    
