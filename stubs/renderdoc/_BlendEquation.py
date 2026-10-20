from ._BlendMultiplier import BlendMultiplier
from ._BlendOperation import BlendOperation

from typing import overload

class BlendEquation():
    # Original docstring
    """
    Describes the details of a blend operation.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BlendEquation.
        """
        pass
    
    @overload
    def __init__(self, other: 'BlendEquation'):
        """
        Construct a new BlendEquation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def destination(self) -> BlendMultiplier:
        """
        The :class:`BlendMultiplier` for the destination blend value.
        
        :type: BlendMultiplier
        """
        pass
    
    @destination.setter
    def destination(self, value: BlendMultiplier):
        pass
    
    @property
    def source(self) -> BlendMultiplier:
        """
        The :class:`BlendMultiplier` for the source blend value.
        
        :type: BlendMultiplier
        """
        pass
    
    @source.setter
    def source(self, value: BlendMultiplier):
        pass
    
    @property
    def operation(self) -> BlendOperation:
        """
        The :class:`BlendOperation` to use in the blend calculation.
        
        :type: BlendOperation
        """
        pass
    
    @operation.setter
    def operation(self, value: BlendOperation):
        pass
    
