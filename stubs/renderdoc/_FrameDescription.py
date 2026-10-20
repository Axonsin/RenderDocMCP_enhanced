from ._DebugMessage import DebugMessage
from ._FrameStatistics import FrameStatistics
from typing import List

from typing import overload

class FrameDescription():
    # Original docstring
    """
    Contains frame-level global information
    
    .. data:: NoFrameNumber
    
      No frame number is available.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised FrameDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'FrameDescription'):
        """
        Construct a new FrameDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoFrameNumber = 4294967295
    """
    No frame number is available.
    """
    
    @property
    def persistentSize(self) -> int:
        """
        The byte size of the section of the file that must be kept in memory persistently.
        
        :type: int
        """
        pass
    
    @persistentSize.setter
    def persistentSize(self, value: int):
        pass
    
    @property
    def frameNumber(self) -> int:
        """
        Starting from frame #1 defined as the time from application startup to first present,
        this counts the frame number when the capture was made.
        
        .. note:: This value is only accurate if the capture was triggered through the default mechanism, if
          it was triggered from the application API it doesn't correspond to anything and will be set to
          :data:`NoFrameNumber`.
        
        :type: int
        """
        pass
    
    @frameNumber.setter
    def frameNumber(self, value: int):
        pass
    
    @property
    def captureTime(self) -> int:
        """
        The time when the capture was created, as a unix timestamp in UTC.
        
        :type: int
        """
        pass
    
    @captureTime.setter
    def captureTime(self, value: int):
        pass
    
    @property
    def fileOffset(self) -> int:
        """
        The offset into the file of the start of the frame.
        
        .. note:: Similarly to :data:`APIEvent.fileOffset` this should only be used as a relative measure,
          as it is not a literal number of bytes from the start of the file on disk.
        
        :type: int
        """
        pass
    
    @fileOffset.setter
    def fileOffset(self, value: int):
        pass
    
    @property
    def stats(self) -> FrameStatistics:
        """
        The frame statistics.
        
        :type: FrameStatistics
        """
        pass
    
    @stats.setter
    def stats(self, value: FrameStatistics):
        pass
    
    @property
    def containsAnnotations(self) -> bool:
        """
        Whether or not the capture contains any annotations.
        
        :type: bool
        """
        pass
    
    @containsAnnotations.setter
    def containsAnnotations(self, value: bool):
        pass
    
    @property
    def uncompressedFileSize(self) -> int:
        """
        The total file size of the whole capture in bytes, after decompression.
        
        :type: int
        """
        pass
    
    @uncompressedFileSize.setter
    def uncompressedFileSize(self, value: int):
        pass
    
    @property
    def compressedFileSize(self) -> int:
        """
        The total file size of the whole capture in bytes, before decompression.
        
        :type: int
        """
        pass
    
    @compressedFileSize.setter
    def compressedFileSize(self, value: int):
        pass
    
    @property
    def initDataSize(self) -> int:
        """
        The byte size of the section of the file that contains frame-initial contents.
        
        :type: int
        """
        pass
    
    @initDataSize.setter
    def initDataSize(self, value: int):
        pass
    
    @property
    def debugMessages(self) -> List[DebugMessage]:
        """
        The debug messages that are not associated with any particular event.
        
        :type: List[DebugMessage]
        """
        pass
    
    @debugMessages.setter
    def debugMessages(self, value: List[DebugMessage]):
        pass
    
