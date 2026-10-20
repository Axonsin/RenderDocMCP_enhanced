from ._ShaderCompileFlag import ShaderCompileFlag
from typing import List

from typing import overload

class ShaderCompileFlags():
    # Original docstring
    """
    Contains the information about the compilation environment of a shader
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderCompileFlags.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderCompileFlags'):
        """
        Construct a new ShaderCompileFlags with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def flags(self) -> List[ShaderCompileFlag]:
        """
        The API or compiler specific flags used to compile this shader originally.
        
        :type: List[ShaderCompileFlag]
        """
        pass
    
    @flags.setter
    def flags(self, value: List[ShaderCompileFlag]):
        pass
    
