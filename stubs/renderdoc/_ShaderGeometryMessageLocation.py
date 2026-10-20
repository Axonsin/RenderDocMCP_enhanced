
from typing import overload

class ShaderGeometryMessageLocation():
    # Original docstring
    """
    A geometry shader message's location.
    
    .. data:: NoLocation
    
      No frame number is available.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderGeometryMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderGeometryMessageLocation'):
        """
        Construct a new ShaderGeometryMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def view(self) -> int:
        """
        The multiview view for this primitive, or ``0`` if multiview is disabled.
        
        :type: int
        """
        pass
    
    @view.setter
    def view(self, value: int):
        pass
    
    @property
    def primitive(self) -> int:
        """
        The primitive index
        
        :type: int
        """
        pass
    
    @primitive.setter
    def primitive(self, value: int):
        pass
    
