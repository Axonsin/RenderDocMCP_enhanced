from ._ShaderMessageLocation import ShaderMessageLocation
from ._ShaderStage import ShaderStage

from typing import overload

class ShaderMessage():
    # Original docstring
    """
    A shader printed message.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderMessage.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderMessage'):
        """
        Construct a new ShaderMessage with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def disassemblyLine(self) -> int:
        """
        The line (starting from 1) of the disassembly where this message came from, or -1 if
        it is not associated with any line.
        
        :type: int
        """
        pass
    
    @disassemblyLine.setter
    def disassemblyLine(self, value: int):
        pass
    
    @property
    def location(self) -> ShaderMessageLocation:
        """
        The location (thread/invocation) of the shader that this message comes from.
        
        :type: ShaderMessageLocation
        """
        pass
    
    @location.setter
    def location(self, value: ShaderMessageLocation):
        pass
    
    @property
    def stage(self) -> ShaderStage:
        """
        The shader stage this message comes from.
        
        :type: ShaderStage
        """
        pass
    
    @stage.setter
    def stage(self, value: ShaderStage):
        pass
    
    @property
    def message(self) -> str:
        """
        The formatted message.
        
        :type: str
        """
        pass
    
    @message.setter
    def message(self, value: str):
        pass
    
