from ._GPUVendor import GPUVendor
from ._GraphicsAPI import GraphicsAPI
from typing import List

from typing import overload

class GPUDevice():
    # Original docstring
    """
    Describes a single GPU at replay time.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GPUDevice.
        """
        pass
    
    @overload
    def __init__(self, other: 'GPUDevice'):
        """
        Construct a new GPUDevice with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def deviceID(self) -> int:
        """
        The PCI device ID of this GPU.
        
        :type: int
        """
        pass
    
    @deviceID.setter
    def deviceID(self, value: int):
        pass
    
    @property
    def apis(self) -> List[GraphicsAPI]:
        """
        The APIs that this device supports.
        
        :type: List[GraphicsAPI]
        """
        pass
    
    @apis.setter
    def apis(self, value: List[GraphicsAPI]):
        pass
    
    @property
    def name(self) -> str:
        """
        The human-readable name of this GPU.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def driver(self) -> str:
        """
        The name of the driver of this GPU, if multiple drivers are available for it.
        
        :type: str
        """
        pass
    
    @driver.setter
    def driver(self, value: str):
        pass
    
    @property
    def vendor(self) -> GPUVendor:
        """
        The :class:`GPUVendor` of this GPU.
        
        :type: GPUVendor
        """
        pass
    
    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass
    
