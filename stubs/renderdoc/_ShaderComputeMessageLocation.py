from typing import Tuple

from typing import overload

class ShaderComputeMessageLocation():
    # Original docstring
    """
    A compute shader message's location.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderComputeMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderComputeMessageLocation'):
        """
        Construct a new ShaderComputeMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def workgroup(self) -> Tuple[int, int, int]:
        """
        The workgroup index within the dispatch.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @workgroup.setter
    def workgroup(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def thread(self) -> Tuple[int, int, int]:
        """
        The thread index within the workgroup.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @thread.setter
    def thread(self, value: Tuple[int, int, int]):
        pass
    
