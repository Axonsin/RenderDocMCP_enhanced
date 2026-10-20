
from typing import overload

class ShaderPixelMessageLocation():
    # Original docstring
    """
    A pixel shader message's location.
    
    .. data:: NoLocation
    
      No frame number is available.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderPixelMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderPixelMessageLocation'):
        """
        Construct a new ShaderPixelMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoLocation = 4294967295
    """
    No frame number is available.
    """
    
    @property
    def x(self) -> int:
        """
        The x co-ordinate of the pixel.
        
        :type: int
        """
        pass
    
    @x.setter
    def x(self, value: int):
        pass
    
    @property
    def y(self) -> int:
        """
        The y co-ordinate of the pixel.
        
        :type: int
        """
        pass
    
    @y.setter
    def y(self, value: int):
        pass
    
    @property
    def view(self) -> int:
        """
        The multiview view for this fragment, or ``0`` if multiview is disabled.
        
        :type: int
        """
        pass
    
    @view.setter
    def view(self, value: int):
        pass
    
    @property
    def primitive(self) -> int:
        """
        The generating primitive, or :data:`NoLocation` if the primitive ID is unavailable.
        
        :type: int
        """
        pass
    
    @primitive.setter
    def primitive(self, value: int):
        pass
    
    @property
    def sample(self) -> int:
        """
        The sample, or :data:`NoLocation` if sample shading is disabled.
        
        :type: int
        """
        pass
    
    @sample.setter
    def sample(self, value: int):
        pass
    
