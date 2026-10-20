
from typing import overload

class NewCaptureData():
    # Original docstring
    """
    Information about the a new capture created by the target.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised NewCaptureData.
        """
        pass
    
    @overload
    def __init__(self, other: 'NewCaptureData'):
        """
        Construct a new NewCaptureData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def frameNumber(self) -> int:
        """
        The frame number that this capture came from.
        
        :type: int
        """
        pass
    
    @frameNumber.setter
    def frameNumber(self, value: int):
        pass
    
    @property
    def title(self) -> str:
        """
        The custom title for this capture, if empty a default title can be used.
        
        :type: str
        """
        pass
    
    @title.setter
    def title(self, value: str):
        pass
    
    @property
    def thumbHeight(self) -> int:
        """
        The height of the image contained in :data:`thumbnail`.
        
        :type: int
        """
        pass
    
    @thumbHeight.setter
    def thumbHeight(self, value: int):
        pass
    
    @property
    def path(self) -> str:
        """
        The local path on the target system where the capture is saved.
        
        :type: str
        """
        pass
    
    @path.setter
    def path(self, value: str):
        pass
    
    @property
    def captureId(self) -> int:
        """
        An identifier to use to refer to this capture.
        
        :type: int
        """
        pass
    
    @captureId.setter
    def captureId(self, value: int):
        pass
    
    @property
    def byteSize(self) -> int:
        """
        The size of the capture, in bytes.
        
        :type: int
        """
        pass
    
    @byteSize.setter
    def byteSize(self, value: int):
        pass
    
    @property
    def local(self) -> bool:
        """
        ``True`` if the target is running on the local system.
        
        :type: bool
        """
        pass
    
    @local.setter
    def local(self, value: bool):
        pass
    
    @property
    def thumbWidth(self) -> int:
        """
        The width of the image contained in :data:`thumbnail`.
        
        :type: int
        """
        pass
    
    @thumbWidth.setter
    def thumbWidth(self, value: int):
        pass
    
    @property
    def timestamp(self) -> int:
        """
        The time the capture was created, as a unix timestamp in UTC.
        
        :type: int
        """
        pass
    
    @timestamp.setter
    def timestamp(self, value: int):
        pass
    
    @property
    def thumbnail(self) -> bytes:
        """
        The raw bytes that contain the capture thumbnail, as RGB8 data.
        
        :type: bytes
        """
        pass
    
    @thumbnail.setter
    def thumbnail(self, value: bytes):
        pass
    
    @property
    def api(self) -> str:
        """
        The API used for this capture, if available.
        
        .. note::
          May be empty if running with an older version of RenderDoc
        
        :type: str
        """
        pass
    
    @api.setter
    def api(self, value: str):
        pass
    
