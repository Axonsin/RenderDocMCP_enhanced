from ._ShaderStage import ShaderStage

from typing import overload

class ShaderEntryPoint():
    # Original docstring
    """
    Describes an entry point in a shader.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderEntryPoint.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderEntryPoint'):
        """
        Construct a new ShaderEntryPoint with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, name: str, stage: ShaderStage):
        """
        Construct a new ShaderEntryPoint using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        The name of the entry point.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def stage(self) -> ShaderStage:
        """
        The :class:`ShaderStage` for this entry point .
        
        :type: ShaderStage
        """
        pass
    
    @stage.setter
    def stage(self, value: ShaderStage):
        pass
    
