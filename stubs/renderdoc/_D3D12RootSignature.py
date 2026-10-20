from ._D3D12RootParam import D3D12RootParam
from ._D3D12StaticSampler import D3D12StaticSampler
from ._ResourceId import ResourceId
from typing import List

from typing import overload

class D3D12RootSignature():
    # Original docstring
    """
    Contains the root signature structure and root parameters.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12RootSignature.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12RootSignature'):
        """
        Construct a new D3D12RootSignature with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def parameters(self) -> List[D3D12RootParam]:
        """
        The parameters in this root signature.
        
        :type: List[D3D12RootParam]
        """
        pass
    
    @parameters.setter
    def parameters(self, value: List[D3D12RootParam]):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the root signature object.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def staticSamplers(self) -> List[D3D12StaticSampler]:
        """
        The static samplers defined in this root signature.
        
        :type: List[D3D12StaticSampler]
        """
        pass
    
    @staticSamplers.setter
    def staticSamplers(self, value: List[D3D12StaticSampler]):
        pass
    
