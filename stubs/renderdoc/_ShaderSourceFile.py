
from typing import overload

class ShaderSourceFile():
    # Original docstring
    """
    Contains a source file available in a debug-compiled shader.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderSourceFile.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderSourceFile'):
        """
        Construct a new ShaderSourceFile with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def contents(self) -> str:
        """
        The actual contents of the file.
        
        :type: str
        """
        pass
    
    @contents.setter
    def contents(self, value: str):
        pass
    
    @property
    def filename(self) -> str:
        """
        The filename of this source file.
        
        :type: str
        """
        pass
    
    @filename.setter
    def filename(self, value: str):
        pass
    
