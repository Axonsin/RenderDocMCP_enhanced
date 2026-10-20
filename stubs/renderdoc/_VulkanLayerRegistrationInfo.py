from ._VulkanLayerFlags import VulkanLayerFlags
from typing import List

class VulkanLayerRegistrationInfo():
    # Original docstring
    """
    INTERNAL: Information about vulkan layer registration
    """
    
    
    @property
    def flags(self) -> VulkanLayerFlags:
        """
        :class:`VulkanLayerFlags` detailing the current registration.
        
        :type: VulkanLayerFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: VulkanLayerFlags):
        pass
    
    @property
    def myJSONs(self) -> List[str]:
        """
        A list of jsons that should be registered
        
        :type: List[str]
        """
        pass
    
    @myJSONs.setter
    def myJSONs(self, value: List[str]):
        pass
    
    @property
    def otherJSONs(self) -> List[str]:
        """
        A list of jsons that should be unregistered / updated
        
        :type: List[str]
        """
        pass
    
    @otherJSONs.setter
    def otherJSONs(self, value: List[str]):
        pass
    
