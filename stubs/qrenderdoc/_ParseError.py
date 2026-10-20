
from typing import overload

class ParseError():
    # Original docstring
    """
    An error that occurred while parsing a buffer format string.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ParseError.
        """
        pass
    
    @overload
    def __init__(self, other: 'ParseError'):
        """
        Construct a new ParseError with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def error(self) -> str:
        """
        The text of the format parsing error.
        
        :type: str
        """
        pass
    
    @error.setter
    def error(self, value: str):
        pass
    
    @property
    def line(self) -> int:
        """
        The 0-based line number in the input string where the error occurred.
        
        :type: int
        """
        pass
    
    @line.setter
    def line(self, value: int):
        pass
    
