from ._GPUVendor import GPUVendor
from ._GraphicsAPI import GraphicsAPI

from typing import overload

class APIProperties():
    # Original docstring
    """
    Gives some API-specific information about the capture.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised APIProperties.
        """
        pass
    
    @overload
    def __init__(self, other: 'APIProperties'):
        """
        Construct a new APIProperties with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def degraded(self) -> bool:
        """
        ``True`` if the capture was loaded successfully but running in a degraded mode - e.g.
        with software rendering, or with some functionality disabled due to lack of support.
        
        :type: bool
        """
        pass
    
    @degraded.setter
    def degraded(self, value: bool):
        pass
    
    @property
    def rgpCapture(self) -> bool:
        """
        ``True`` if the driver and system are configured to allow creating RGP captures.
        
        :type: bool
        """
        pass
    
    @rgpCapture.setter
    def rgpCapture(self, value: bool):
        pass
    
    @property
    def pixelHistory(self) -> bool:
        """
        ``True`` if the API supports viewing pixel history.
        
        :type: bool
        """
        pass
    
    @pixelHistory.setter
    def pixelHistory(self, value: bool):
        pass
    
    @property
    def remoteReplay(self) -> bool:
        """
        ``True`` if the capture is being replayed over a remote connection.
        
        :type: bool
        """
        pass
    
    @remoteReplay.setter
    def remoteReplay(self, value: bool):
        pass
    
    @property
    def pipelineType(self) -> GraphicsAPI:
        """
        The :class:`GraphicsAPI` of the actual log/capture.
        
        :type: GraphicsAPI
        """
        pass
    
    @pipelineType.setter
    def pipelineType(self, value: GraphicsAPI):
        pass
    
    @property
    def shaderDebugging(self) -> bool:
        """
        ``True`` if the API supports shader debugging.
        
        :type: bool
        """
        pass
    
    @shaderDebugging.setter
    def shaderDebugging(self, value: bool):
        pass
    
    @property
    def vendor(self) -> GPUVendor:
        """
        The :class:`GPUVendor` of the active GPU being used.
        
        :type: GPUVendor
        """
        pass
    
    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass
    
    @property
    def localRenderer(self) -> GraphicsAPI:
        """
        The :class:`GraphicsAPI` used to render the log. For remote replay this could be
        different to the above, and lets the UI make decisions e.g. to flip rendering of images.
        
        :type: GraphicsAPI
        """
        pass
    
    @localRenderer.setter
    def localRenderer(self, value: GraphicsAPI):
        pass
    
