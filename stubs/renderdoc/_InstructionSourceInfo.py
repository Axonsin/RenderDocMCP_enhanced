from ._LineColumnInfo import LineColumnInfo
from ._SourceVariableMapping import SourceVariableMapping
from typing import List

from typing import overload

class InstructionSourceInfo():
    # Original docstring
    """
    Gives per-instruction source code mapping information, including what line(s) correspond
    to this instruction and which source variables exist
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised InstructionSourceInfo.
        """
        pass
    
    @overload
    def __init__(self, other: 'InstructionSourceInfo'):
        """
        Construct a new InstructionSourceInfo with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def lineInfo(self) -> LineColumnInfo:
        """
        The source location that this instruction corresponds to
        
        :type: LineColumnInfo
        """
        pass
    
    @lineInfo.setter
    def lineInfo(self, value: LineColumnInfo):
        pass
    
    @property
    def sourceVars(self) -> List[SourceVariableMapping]:
        """
        An optional mapping of which high-level source variables map to which debug variables
        and including extra type information.
        
        This list contains source variable mapping that is only valid at this instruction, and is fully
        complete & redundant including all previous source variables that are still valid at this
        instruction.
        
        :type: List[SourceVariableMapping]
        """
        pass
    
    @sourceVars.setter
    def sourceVars(self, value: List[SourceVariableMapping]):
        pass
    
    @property
    def instruction(self) -> int:
        """
        The instruction that this information is for.
        
        :type: int
        """
        pass
    
    @instruction.setter
    def instruction(self, value: int):
        pass
    
