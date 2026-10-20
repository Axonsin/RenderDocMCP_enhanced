
from typing import overload

class APIUseData():
    # Original docstring
    """
    Information about the API that the target is using.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised APIUseData.
        """
        pass
    
    @overload
    def __init__(self, other: 'APIUseData'):
        """
        Construct a new APIUseData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def name(self) -> str:
        """
        The name of the API.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def presenting(self) -> bool:
        """
        ``True`` if the API is presenting to a swapchain
        
        :type: bool
        """
        pass
    
    @presenting.setter
    def presenting(self, value: bool):
        pass
    
    @property
    def supportMessage(self) -> str:
        """
        A string message if the API is unsupported explaining why.
        
        :type: str
        """
        pass
    
    @supportMessage.setter
    def supportMessage(self, value: str):
        pass
    
    @property
    def supported(self) -> bool:
        """
        ``True`` if the API can be captured.
        
        :type: bool
        """
        pass
    
    @supported.setter
    def supported(self, value: bool):
        pass
    
