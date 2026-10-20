from ._CompareFunction import CompareFunction
from ._StencilOperation import StencilOperation

from typing import overload

class StencilFace():
    # Original docstring
    """
    Describes the details of a stencil operation.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised StencilFace.
        """
        pass
    
    @overload
    def __init__(self, other: 'StencilFace'):
        """
        Construct a new StencilFace with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def reference(self) -> int:
        """
        The current stencil reference value.
        
        :type: int
        """
        pass
    
    @reference.setter
    def reference(self, value: int):
        pass
    
    @property
    def function(self) -> CompareFunction:
        """
        the :class:`CompareFunction` to use for testing stencil values.
        
        :type: CompareFunction
        """
        pass
    
    @function.setter
    def function(self, value: CompareFunction):
        pass
    
    @property
    def compareMask(self) -> int:
        """
        The mask for testing stencil values.
        
        :type: int
        """
        pass
    
    @compareMask.setter
    def compareMask(self, value: int):
        pass
    
    @property
    def writeMask(self) -> int:
        """
        The mask for writing stencil values.
        
        :type: int
        """
        pass
    
    @writeMask.setter
    def writeMask(self, value: int):
        pass
    
    @property
    def failOperation(self) -> StencilOperation:
        """
        The :class:`StencilOperation` to apply if the stencil-test fails.
        
        :type: StencilOperation
        """
        pass
    
    @failOperation.setter
    def failOperation(self, value: StencilOperation):
        pass
    
    @property
    def depthFailOperation(self) -> StencilOperation:
        """
        the :class:`StencilOperation` to apply if the depth-test fails.
        
        :type: StencilOperation
        """
        pass
    
    @depthFailOperation.setter
    def depthFailOperation(self, value: StencilOperation):
        pass
    
    @property
    def passOperation(self) -> StencilOperation:
        """
        the :class:`StencilOperation` to apply if the stencil-test passes.
        
        :type: StencilOperation
        """
        pass
    
    @passOperation.setter
    def passOperation(self, value: StencilOperation):
        pass
    
