from ._CullMode import CullMode
from ._FillMode import FillMode

from typing import overload

class RasterState():
    # Original docstring
    """
    Describes a common subset of rasterizing state.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised RasterState.
        """
        pass
    
    @overload
    def __init__(self, other: 'RasterState'):
        """
        Construct a new RasterState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def fillMode(self) -> FillMode:
        """
        The polygon :class:`FillMode`.
        
        :type: FillMode
        """
        pass
    
    @fillMode.setter
    def fillMode(self, value: FillMode):
        pass
    
    @property
    def cullMode(self) -> CullMode:
        """
        The polygon :class:`CullMode`.
        
        :type: CullMode
        """
        pass
    
    @cullMode.setter
    def cullMode(self, value: CullMode):
        pass
    
    @property
    def frontCCW(self) -> bool:
        """
        ``True`` if counter-clockwise polygons are front-facing.
        ``False`` if clockwise polygons are front-facing.
        
        :type: bool
        """
        pass
    
    @frontCCW.setter
    def frontCCW(self, value: bool):
        pass
    
