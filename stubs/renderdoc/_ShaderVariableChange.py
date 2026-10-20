from ._ShaderVariable import ShaderVariable

from typing import overload

class ShaderVariableChange():
    # Original docstring
    """
    This stores the before and after state of a :class:`ShaderVariable`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderVariableChange.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderVariableChange'):
        """
        Construct a new ShaderVariableChange with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def after(self) -> ShaderVariable:
        """
        The value of the variable after the change. If this variable is uninitialised that
        means the variable stopped existing on this step.
        
        :type: ShaderVariable
        """
        pass
    
    @after.setter
    def after(self, value: ShaderVariable):
        pass
    
    @property
    def before(self) -> ShaderVariable:
        """
        The value of the variable before the change. If this variable is uninitialised that
        means the variable came into existence on this step.
        
        :type: ShaderVariable
        """
        pass
    
    @before.setter
    def before(self, value: ShaderVariable):
        pass
    
