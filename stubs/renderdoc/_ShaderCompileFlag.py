
from typing import overload

class ShaderCompileFlag():
    # Original docstring
    """
    Contains a single flag used at compile-time on a shader.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderCompileFlag.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderCompileFlag'):
        """
        Construct a new ShaderCompileFlag with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def value(self) -> str:
        """
        The value of the compile flag.
        
        :type: str
        """
        pass
    
    @value.setter
    def value(self, value: str):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of the compile flag.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
