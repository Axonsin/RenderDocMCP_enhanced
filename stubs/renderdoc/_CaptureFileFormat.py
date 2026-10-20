
from typing import overload

class CaptureFileFormat():
    # Original docstring
    """
    The format for a capture file either supported to read from, or export to.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CaptureFileFormat.
        """
        pass
    
    @overload
    def __init__(self, other: 'CaptureFileFormat'):
        """
        Construct a new CaptureFileFormat with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        A human readable short phrase naming the file format.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def requiresBuffers(self) -> bool:
        """
        Indicates whether exporting to this format requires buffers or just structured data.
        If it doesn't require buffers then it can be exported directly from an opened capture, which by
        default has structured data but no buffers available.
        
        :type: bool
        """
        pass
    
    @requiresBuffers.setter
    def requiresBuffers(self, value: bool):
        pass
    
    @property
    def description(self) -> str:
        """
        A human readable long-form description of the file format.
        
        :type: str
        """
        pass
    
    @description.setter
    def description(self, value: str):
        pass
    
    @property
    def openSupported(self) -> bool:
        """
        Indicates whether or not files in this format can be opened and processed as
        structured data.
        
        :type: bool
        """
        pass
    
    @openSupported.setter
    def openSupported(self, value: bool):
        pass
    
    @property
    def convertSupported(self) -> bool:
        """
        Indicates whether captures or structured data can be saved out in this format.
        
        :type: bool
        """
        pass
    
    @convertSupported.setter
    def convertSupported(self, value: bool):
        pass
    
    @property
    def extension(self) -> str:
        """
        The file of the format as a single minimal string, e.g. ``rdc``.
        
        :type: str
        """
        pass
    
    @extension.setter
    def extension(self, value: str):
        pass
    
