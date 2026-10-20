
# Dummy types
from . import Display
from . import wl_display

from typing import overload

class GlobalEnvironment():
    # Original docstring
    """
    Structure used for initialising environment in a replay application.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GlobalEnvironment.
        """
        pass
    
    @overload
    def __init__(self, other: 'GlobalEnvironment'):
        """
        Construct a new GlobalEnvironment with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def xlibDisplay(self) -> Display:
        """
        The handle to the X display to use internally. If left ``NULL``, one will be opened.
        
        :type: Display
        """
        pass
    
    @xlibDisplay.setter
    def xlibDisplay(self, value: Display):
        pass
    
    @property
    def waylandDisplay(self) -> wl_display:
        """
        The handle to the wayland display to use internally. If left ``NULL``, wayland cannot be used.
        
        :type: wl_display
        """
        pass
    
    @waylandDisplay.setter
    def waylandDisplay(self, value: wl_display):
        pass
    
    @property
    def enumerateGPUs(self) -> bool:
        """
        Whether to enumerate available GPUs. If the replay program is only being used for
        internal operation where enumerating GPUs would be too expensive or problematic, it can be disabled
        here.
        
        :type: bool
        """
        pass
    
    @enumerateGPUs.setter
    def enumerateGPUs(self, value: bool):
        pass
    
