from ._ResourceId import ResourceId
from ._VKImageLayout import VKImageLayout
from typing import List

from typing import overload

class VKImageData():
    # Original docstring
    """
    Contains the current layout of all subresources in the image.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKImageData.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKImageData'):
        """
        Construct a new VKImageData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def layouts(self) -> List[VKImageLayout]:
        """
        The subresource regions in this resource.
        
        :type: List[VKImageLayout]
        """
        pass
    
    @layouts.setter
    def layouts(self, value: List[VKImageLayout]):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the image.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
