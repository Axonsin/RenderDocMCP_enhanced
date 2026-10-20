from ._ResourceId import ResourceId

from typing import overload

class PointerVal():
    # Original docstring
    """
    A 64-bit pointer value with optional type information.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PointerVal.
        """
        pass
    
    @overload
    def __init__(self, other: 'PointerVal'):
        """
        Construct a new PointerVal with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def shader(self) -> ResourceId:
        """
        An optional :class:`ResourceId` identifying the shader containing the type info.
        
        :type: ResourceId
        """
        pass
    
    @shader.setter
    def shader(self, value: ResourceId):
        pass
    
    @property
    def pointer(self) -> int:
        """
        The actual pointer value itself.
        
        :type: int
        """
        pass
    
    @pointer.setter
    def pointer(self, value: int):
        pass
    
    @property
    def pointerTypeID(self) -> int:
        """
        The index into :data:`ShaderReflection.pointerTypes` of the pointed type.
        
        :type: int
        """
        pass
    
    @pointerTypeID.setter
    def pointerTypeID(self, value: int):
        pass
    
