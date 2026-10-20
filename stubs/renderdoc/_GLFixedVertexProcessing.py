from typing import Tuple

from typing import overload

class GLFixedVertexProcessing():
    # Original docstring
    """
    Describes the setup for fixed vertex processing operations.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLFixedVertexProcessing.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLFixedVertexProcessing'):
        """
        Construct a new GLFixedVertexProcessing with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def defaultInnerLevel(self) -> Tuple[float, float]:
        """
        A tuple of ``float`` giving the default inner level of tessellation.
        
        :type: Tuple[float,float]
        """
        pass
    
    @defaultInnerLevel.setter
    def defaultInnerLevel(self, value: Tuple[float, float]):
        pass
    
    @property
    def defaultOuterLevel(self) -> Tuple[float, float, float, float]:
        """
        A tuple of ``float`` giving the default outer level of tessellation.
        
        :type: Tuple[float,float,float,float]
        """
        pass
    
    @defaultOuterLevel.setter
    def defaultOuterLevel(self, value: Tuple[float, float, float, float]):
        pass
    
    @property
    def clipPlanes(self) -> Tuple[bool, ...]:
        """
        An 8-tuple of ``bool`` determining which user clipping planes are enabled.
        
        :type: Tuple[bool,...]
        """
        pass
    
    @clipPlanes.setter
    def clipPlanes(self, value: Tuple[bool, ...]):
        pass
    
    @property
    def clipOriginLowerLeft(self) -> bool:
        """
        ``True`` if the clipping origin should be in the lower left.
        
        ``False`` if it's in the upper left.
        
        :type: bool
        """
        pass
    
    @clipOriginLowerLeft.setter
    def clipOriginLowerLeft(self, value: bool):
        pass
    
    @property
    def discard(self) -> bool:
        """
        ``True`` if primitives should be discarded during rasterization.
        
        :type: bool
        """
        pass
    
    @discard.setter
    def discard(self, value: bool):
        pass
    
    @property
    def clipNegativeOneToOne(self) -> bool:
        """
        ``True`` if the clip-space Z goes from ``-1`` to ``1``.
        
        ``False`` if the clip-space Z goes from ``0`` to ``1``.
        
        :type: bool
        """
        pass
    
    @clipNegativeOneToOne.setter
    def clipNegativeOneToOne(self, value: bool):
        pass
    
