from ._GPUVendor import GPUVendor
from ._ReplayOptimisationLevel import ReplayOptimisationLevel

from typing import overload

class ReplayOptions():
    # Original docstring
    """
    The options controlling how replay of a capture should be performed.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ReplayOptions.
        """
        pass
    
    @overload
    def __init__(self, other: 'ReplayOptions'):
        """
        Construct a new ReplayOptions with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def forceGPUDeviceID(self) -> int:
        """
        Force the selection of a GPU by device ID. This allows overriding which GPU is used to
        replay on.
        
        When set to 0, specifies no particular device.
        
        See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.
        
        :type: int
        """
        pass
    
    @forceGPUDeviceID.setter
    def forceGPUDeviceID(self, value: int):
        pass
    
    @property
    def optimisation(self) -> ReplayOptimisationLevel:
        """
        How much optimisation should be done, potentially at the cost of correctness.
        
        The default is :data:`ReplayOptimisationLevel.Balanced`.
        
        :type: ReplayOptimisationLevel
        """
        pass
    
    @optimisation.setter
    def optimisation(self, value: ReplayOptimisationLevel):
        pass
    
    @property
    def apiValidation(self) -> bool:
        """
        Replay with API validation enabled and use debug messages from there, ignoring any
        that may be contained in the capture.
        
        The default is not to do any validation.
        
        .. note:: RenderDoc does not handle invalid API use in the general case so validation should still
          be performed at runtime in your program for ground truth results.
        
        :type: bool
        """
        pass
    
    @apiValidation.setter
    def apiValidation(self, value: bool):
        pass
    
    @property
    def forceGPUVendor(self) -> GPUVendor:
        """
        Force the selection of a GPU by vendor ID. This allows overriding which GPU is used to
        replay on, even if a different GPU would be the best match for the capture.
        
        When set to :data:`GPUVendor.Unknown`, specifies no particular vendor.
        
        See also :data:`forceGPUDeviceID` and :data:`forceGPUDriverName`. Available GPUs can be enumerated
        using :meth:`CaptureAccess.GetAvailableGPUs`.
        
        The default is not to do any override. The capture contains information about what GPU was used, and
        the closest matching GPU is used on replay.
        
        .. note::
          If a GPU is forced that is not available or not supported for a given capture, such as when GPUs
          are only available for some APIs and not others, the default GPU selection will be used. If a GPU
          is available for a capture but fails to open however then there is no fallback to a default GPU.
        
          OpenGL does not support GPU selection so the default method (which effectively does nothing) will
          always be used.
        
        :type: GPUVendor
        """
        pass
    
    @forceGPUVendor.setter
    def forceGPUVendor(self, value: GPUVendor):
        pass
    
    @property
    def forceGPUDriverName(self) -> str:
        """
        Force the selection of a GPU by driver name. This allows overriding which GPU is used
        to replay on.
        
        When set to an empty string, specifies no particular driver.
        
        See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.
        
        :type: str
        """
        pass
    
    @forceGPUDriverName.setter
    def forceGPUDriverName(self, value: str):
        pass
    
