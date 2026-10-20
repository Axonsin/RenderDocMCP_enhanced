from ._DebugVariableType import DebugVariableType

from typing import overload

class DebugVariableReference():
    # Original docstring
    """
    A particular component of a debugging variable that a high-level variable component maps to
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DebugVariableReference.
        """
        pass
    
    @overload
    def __init__(self, other: 'DebugVariableReference'):
        """
        Construct a new DebugVariableReference with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, type: DebugVariableType, name: str, component: int):
        """
        Construct a new DebugVariableReference using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        The name of the base debug variable.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def component(self) -> int:
        """
        The component within the variable.
        
        :type: int
        """
        pass
    
    @component.setter
    def component(self, value: int):
        pass
    
    @property
    def type(self) -> DebugVariableType:
        """
        The type of variable this is referring to.
        
        :type: DebugVariableType
        """
        pass
    
    @type.setter
    def type(self, value: DebugVariableType):
        pass
    
