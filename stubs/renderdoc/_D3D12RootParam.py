from ._D3D12RootTableRange import D3D12RootTableRange
from ._Descriptor import Descriptor
from ._ResourceId import ResourceId
from ._ShaderStageMask import ShaderStageMask
from typing import List

from typing import overload

class D3D12RootParam():
    # Original docstring
    """
    Contains the structure and content of a single root parameter.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12RootParam.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12RootParam'):
        """
        Construct a new D3D12RootParam with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def reg(self) -> int:
        """
        For a root parameter, the register of the binding.
        
        :type: int
        """
        pass
    
    @reg.setter
    def reg(self, value: int):
        pass
    
    @property
    def heap(self) -> ResourceId:
        """
        For a root table parameter, the descriptor heap bound to this parameter. See
        :data:`heapByteOffset` and :data:`tableRanges`.
        
        :type: ResourceId
        """
        pass
    
    @heap.setter
    def heap(self, value: ResourceId):
        pass
    
    @property
    def descriptor(self) -> Descriptor:
        """
        For a root descriptor parameter, the descriptor itself.
        
        :type: Descriptor
        """
        pass
    
    @descriptor.setter
    def descriptor(self, value: Descriptor):
        pass
    
    @property
    def visibility(self) -> ShaderStageMask:
        """
        The shader stage that can access this parameter.
        
        :type: ShaderStageMask
        """
        pass
    
    @visibility.setter
    def visibility(self, value: ShaderStageMask):
        pass
    
    @property
    def constants(self) -> bytes:
        """
        For a root constant parameter, the words defined.
        
        :type: bytes
        """
        pass
    
    @constants.setter
    def constants(self, value: bytes):
        pass
    
    @property
    def heapByteOffset(self) -> int:
        """
        For a root table parameter, the byte offset into the descriptor heap bound to this
        parameter. See :data:`heap` and :data:`tableRanges`.
        
        :type: int
        """
        pass
    
    @heapByteOffset.setter
    def heapByteOffset(self, value: int):
        pass
    
    @property
    def tableRanges(self) -> List[D3D12RootTableRange]:
        """
        For a root table parameter, the descriptor ranges that define this table. See
        :data:`heap` and :data:`heapByteOffset`.
        
        :type: List[D3D12RootTableRange]
        """
        pass
    
    @tableRanges.setter
    def tableRanges(self, value: List[D3D12RootTableRange]):
        pass
    
    @property
    def space(self) -> int:
        """
        For a root parameter, the register space of the binding.
        
        :type: int
        """
        pass
    
    @space.setter
    def space(self, value: int):
        pass
    
