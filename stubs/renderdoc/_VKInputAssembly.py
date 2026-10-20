from ._Topology import Topology
from ._VKIndexBuffer import VKIndexBuffer

from typing import overload

class VKInputAssembly():
    # Original docstring
    """
    Describes the vulkan input assembly configuration.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKInputAssembly.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKInputAssembly'):
        """
        Construct a new VKInputAssembly with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def indexBuffer(self) -> VKIndexBuffer:
        """
        The index buffer binding.
        
        :type: VKIndexBuffer
        """
        pass
    
    @indexBuffer.setter
    def indexBuffer(self, value: VKIndexBuffer):
        pass
    
    @property
    def topology(self) -> Topology:
        """
        The current primitive topology.
        
        :type: Topology
        """
        pass
    
    @topology.setter
    def topology(self, value: Topology):
        pass
    
    @property
    def primitiveRestartEnable(self) -> bool:
        """
        ``True`` if primitive restart is enabled for strip primitives.
        
        :type: bool
        """
        pass
    
    @primitiveRestartEnable.setter
    def primitiveRestartEnable(self, value: bool):
        pass
    
