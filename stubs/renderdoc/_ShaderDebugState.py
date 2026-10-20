from ._ShaderEvents import ShaderEvents
from ._ShaderVariableChange import ShaderVariableChange
from typing import List

from typing import overload

class ShaderDebugState():
    # Original docstring
    """
    This stores the current state of shader debugging at one particular step in the shader,
    with all mutable variable contents.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderDebugState.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderDebugState'):
        """
        Construct a new ShaderDebugState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def callstack(self) -> List[str]:
        """
        The function names in the current callstack at this instruction.
        
        The oldest/outer function is first in the list, the newest/inner function is last.
        
        :type: List[str]
        """
        pass
    
    @callstack.setter
    def callstack(self, value: List[str]):
        pass
    
    @property
    def stepIndex(self) -> int:
        """
        The program counter within the debug trace. The initial state will be index 0, and it
        will increment linearly after that regardless of loops or branching.
        
        :type: int
        """
        pass
    
    @stepIndex.setter
    def stepIndex(self, value: int):
        pass
    
    @property
    def changes(self) -> List[ShaderVariableChange]:
        """
        The changes in mutable variables for this shader. The change documents the
        bidirectional change of variables, so that a single state can be updated either forwards or
        backwards using the information.
        
        :type: List[ShaderVariableChange]
        """
        pass
    
    @changes.setter
    def changes(self, value: List[ShaderVariableChange]):
        pass
    
    @property
    def flags(self) -> ShaderEvents:
        """
        A set of :class:`ShaderEvents` flags that indicate what events happened on this step.
        
        :type: ShaderEvents
        """
        pass
    
    @flags.setter
    def flags(self, value: ShaderEvents):
        pass
    
    @property
    def nextInstruction(self) -> int:
        """
        The next instruction to be executed after this state. The initial state before any
        shader execution happened will have ``nextInstruction == 0``.
        
        :type: int
        """
        pass
    
    @nextInstruction.setter
    def nextInstruction(self, value: int):
        pass
    
