
from typing import overload

class ShaderToolOutput():
    # Original docstring
    """
    Contains the output from invoking a :class:`ShaderProcessingTool`, including both the
    actual output data desired as well as any stdout/stderr messages.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderToolOutput.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderToolOutput'):
        """
        Construct a new ShaderToolOutput with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def log(self) -> str:
        """
        The output log - containing the information about the tool run and any errors.
        
        :type: str
        """
        pass
    
    @log.setter
    def log(self, value: str):
        pass
    
    @property
    def result(self) -> bytes:
        """
        The actual output data from the tool
        
        :type: bytes
        """
        pass
    
    @result.setter
    def result(self, value: bytes):
        pass
    
