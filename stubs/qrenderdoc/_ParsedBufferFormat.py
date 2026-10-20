from ._PackingRules import PackingRules
from ._ParseError import ParseError
from renderdoc import ShaderConstant
from typing import List

from typing import overload

class ParsedBufferFormat():
    # Original docstring
    """
    The result of parsing a buffer format string.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ParsedBufferFormat.
        """
        pass
    
    @overload
    def __init__(self, other: 'ParsedBufferFormat'):
        """
        Construct a new ParsedBufferFormat with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def errors(self) -> List[ParseError]:
        """
        The list of errors encountered while processing the format string.
        
        :type: List[ParseError]
        """
        pass
    
    @errors.setter
    def errors(self, value: List[ParseError]):
        pass
    
    @property
    def structure(self) -> ShaderConstant:
        """
        The main structure of data described by the input buffer string.
        
        :type: renderdoc.ShaderConstant
        """
        pass
    
    @structure.setter
    def structure(self, value: ShaderConstant):
        pass
    
    @property
    def packing(self) -> PackingRules:
        """
        The packing rules specified in the buffer format string. If not explicitly
        stated then the estimated rules will be given here, as the most conservative packing that
        would work for the current API.
        
        :type: PackingRules
        """
        pass
    
    @packing.setter
    def packing(self, value: PackingRules):
        pass
    
    @property
    def fixedHeader(self) -> ShaderConstant:
        """
        The fixed SoA variables before any repeating structure, if present.
        
        On some APIs it is possible to declare a fixed size amount of SoA data before then
        an unbounded/runtime array of AoS data. If the format string is interpreted this
        way then the initial fixed data structure will be returned in this member
        
        :type: renderdoc.ShaderConstant
        """
        pass
    
    @fixedHeader.setter
    def fixedHeader(self, value: ShaderConstant):
        pass
    
