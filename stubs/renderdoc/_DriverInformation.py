from ._GPUVendor import GPUVendor

from typing import overload

class DriverInformation():
    # Original docstring
    """
    Gives information about the driver for this API.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised DriverInformation.
        """
        pass
    
    @overload
    def __init__(self, other: 'DriverInformation'):
        """
        Construct a new DriverInformation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def version(self) -> str:
        """
        The version string for the driver
        
        :type: str
        """
        pass
    
    @version.setter
    def version(self, value: str):
        pass
    
    @property
    def vendor(self) -> GPUVendor:
        """
        The :class:`GPUVendor` that provides this driver
        
        :type: GPUVendor
        """
        pass
    
    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass
    
