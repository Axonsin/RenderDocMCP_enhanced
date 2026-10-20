from datetime import datetime

from typing import overload

class ConnectedTempCapture():
    # Original docstring
    """
    The details of a capture that has been made on a connection but may not
    have been saved to disk or local.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ConnectedTempCapture.
        """
        pass
    
    @overload
    def __init__(self, other: 'ConnectedTempCapture'):
        """
        Construct a new ConnectedTempCapture with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def captureID(self) -> int:
        """
        The ID of the capture, which is arbitrary. IDs are unique for the capture within
        a given connection, but two connections may have the same ID.
        
        :type: int
        """
        pass
    
    @captureID.setter
    def captureID(self, value: int):
        pass
    
    @property
    def frameNumber(self) -> int:
        """
        The frame number which was captured. May be ``-1`` if the capture was made via the RenderDoc
        API.
        
        :type: int
        """
        pass
    
    @frameNumber.setter
    def frameNumber(self, value: int):
        pass
    
    @property
    def api(self) -> str:
        """
        The name of the API used for this capture.
        
        :type: str
        """
        pass
    
    @api.setter
    def api(self, value: str):
        pass
    
    @property
    def timestamp(self) -> datetime:
        """
        The timestamp when the capture completed.
        
        :type: datetime
        """
        pass
    
    @timestamp.setter
    def timestamp(self, value: datetime):
        pass
    
