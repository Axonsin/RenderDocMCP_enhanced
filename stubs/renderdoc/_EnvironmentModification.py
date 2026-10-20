from ._EnvMod import EnvMod
from ._EnvSep import EnvSep

from typing import overload

class EnvironmentModification():
    # Original docstring
    """
    A modification to a single environment variable.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised EnvironmentModification.
        """
        pass
    
    @overload
    def __init__(self, other: 'EnvironmentModification'):
        """
        Construct a new EnvironmentModification with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, mod: EnvMod, sep: EnvSep, name: str, value: str):
        """
        Construct a new EnvironmentModification using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def value(self) -> str:
        """
        The value to use with the modification specified in :data:`mod`.
        
        :type: str
        """
        pass
    
    @value.setter
    def value(self, value: str):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of the environment variable.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def mod(self) -> EnvMod:
        """
        The :class:`modification <EnvMod>` to use.
        
        :type: EnvMod
        """
        pass
    
    @mod.setter
    def mod(self, value: EnvMod):
        pass
    
    @property
    def sep(self) -> EnvSep:
        """
        The :class:`separator <EnvSep>` to use if needed.
        
        :type: EnvSep
        """
        pass
    
    @sep.setter
    def sep(self, value: EnvSep):
        pass
    
