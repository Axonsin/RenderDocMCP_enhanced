from ._VKXFBBuffer import VKXFBBuffer
from typing import List

from typing import overload

class VKTransformFeedback():
    # Original docstring
    """
    Describes the state of the fixed-function transform feedback.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKTransformFeedback.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKTransformFeedback'):
        """
        Construct a new VKTransformFeedback with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def buffers(self) -> List[VKXFBBuffer]:
        """
        The bound transform feedback buffers.
        
        :type: List[VKXFBBuffer]
        """
        pass
    
    @buffers.setter
    def buffers(self, value: List[VKXFBBuffer]):
        pass
    
    @property
    def rasterizedStream(self) -> int:
        """
        Which stream-out stream is being used for rasterization.
        
        :type: int
        """
        pass
    
    @rasterizedStream.setter
    def rasterizedStream(self, value: int):
        pass
    
