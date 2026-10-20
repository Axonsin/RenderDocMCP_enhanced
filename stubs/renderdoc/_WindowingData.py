from typing import overload

class WindowingData():
    # Original docstring
    """
    An opaque structure created to hold windowing setup data
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised WindowingData.
        """
        pass
    
    @overload
    def __init__(self, other: 'WindowingData'):
        """
        Construct a new WindowingData with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
