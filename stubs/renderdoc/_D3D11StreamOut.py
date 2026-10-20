from ._D3D11StreamOutBind import D3D11StreamOutBind
from typing import List

from typing import overload

class D3D11StreamOut():
    # Original docstring
    """
    Describes the stream-out stage bindings.
    
    .. data:: NoRasterization
    
      Value for :data:`rasterizedStream` that indicates no stream is being rasterized.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11StreamOut.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11StreamOut'):
        """
        Construct a new D3D11StreamOut with a deep copy of the input.
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
    def outputs(self) -> List[D3D11StreamOutBind]:
        """
        The bound stream-out buffer bindings.
        
        :type: List[D3D11StreamOutBind]
        """
        pass
    
    @outputs.setter
    def outputs(self, value: List[D3D11StreamOutBind]):
        pass
    
