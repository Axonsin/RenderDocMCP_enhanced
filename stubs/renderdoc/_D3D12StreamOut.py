from ._D3D12StreamOutBind import D3D12StreamOutBind
from typing import List

from typing import overload

class D3D12StreamOut():
    # Original docstring
    """
    Describes the stream-out state in the PSO.
    
    .. data:: NoRasterization
    
      Value for :data:`rasterizedStream` that indicates no stream is being rasterized.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12StreamOut.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12StreamOut'):
        """
        Construct a new D3D12StreamOut with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoRasterization = 4294967295
    """
    Value for :data:`rasterizedStream` that indicates no stream is being rasterized.
    """
    
    @property
    def rasterizedStream(self) -> int:
        """
        Which stream-out stream is being used for rasterization.
        
        If the value is :data:`NoRasterization` then no stream has been selected for rasterization.
        
        :type: int
        """
        pass
    
    @rasterizedStream.setter
    def rasterizedStream(self, value: int):
        pass
    
    @property
    def outputs(self) -> List[D3D12StreamOutBind]:
        """
        The bound stream-out buffer bindings.
        
        :type: List[D3D12StreamOutBind]
        """
        pass
    
    @outputs.setter
    def outputs(self, value: List[D3D12StreamOutBind]):
        pass
    
