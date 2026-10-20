from ._BlendEquation import BlendEquation
from ._LogicOperation import LogicOperation

from typing import overload

class ColorBlend():
    # Original docstring
    """
    Describes the blend configuration for a given output target.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ColorBlend.
        """
        pass
    
    @overload
    def __init__(self, other: 'ColorBlend'):
        """
        Construct a new ColorBlend with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def colorBlend(self) -> BlendEquation:
        """
        The blending equation for color values.
        
        :type: BlendEquation
        """
        pass
    
    @colorBlend.setter
    def colorBlend(self, value: BlendEquation):
        pass
    
    @property
    def enabled(self) -> bool:
        """
        ``True`` if blending is enabled for this target.
        
        :type: bool
        """
        pass
    
    @enabled.setter
    def enabled(self, value: bool):
        pass
    
    @property
    def logicOperationEnabled(self) -> bool:
        """
        ``True`` if the logic operation in :data:`logicOperation` should be used.
        
        :type: bool
        """
        pass
    
    @logicOperationEnabled.setter
    def logicOperationEnabled(self, value: bool):
        pass
    
    @property
    def writeMask(self) -> int:
        """
        The mask for writes to the render target.
        
        :type: int
        """
        pass
    
    @writeMask.setter
    def writeMask(self, value: int):
        pass
    
    @property
    def alphaBlend(self) -> BlendEquation:
        """
        The blending equation for alpha values.
        
        :type: BlendEquation
        """
        pass
    
    @alphaBlend.setter
    def alphaBlend(self, value: BlendEquation):
        pass
    
    @property
    def logicOperation(self) -> LogicOperation:
        """
        The :class:`LogicOperation` to use for logic operations, if
        :data:`logicOperationEnabled` is ``True``.
        
        :type: LogicOperation
        """
        pass
    
    @logicOperation.setter
    def logicOperation(self, value: LogicOperation):
        pass
    
