from ._ShaderEncoding import ShaderEncoding

from typing import overload

class ShaderSourcePrefix():
    # Original docstring
    """
    Contains the source prefix to add to a given type of shader source
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderSourcePrefix.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderSourcePrefix'):
        """
        Construct a new ShaderSourcePrefix with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def prefix(self) -> str:
        """
        The source prefix to add.
        
        :type: str
        """
        pass
    
    @prefix.setter
    def prefix(self, value: str):
        pass
    
    @property
    def encoding(self) -> ShaderEncoding:
        """
        The encoding of the language this prefix applies to.
        
        :type: ShaderEncoding
        """
        pass
    
    @encoding.setter
    def encoding(self, value: ShaderEncoding):
        pass
    
