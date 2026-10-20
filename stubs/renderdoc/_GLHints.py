from ._QualityHint import QualityHint

from typing import overload

class GLHints():
    # Original docstring
    """
    Describes the current state of GL hints and smoothing.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLHints.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLHints'):
        """
        Construct a new GLHints with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def lineSmoothingEnabled(self) -> bool:
        """
        ``True`` if line smoothing is enabled.
        
        :type: bool
        """
        pass
    
    @lineSmoothingEnabled.setter
    def lineSmoothingEnabled(self, value: bool):
        pass
    
    @property
    def polySmoothingEnabled(self) -> bool:
        """
        ``True`` if polygon smoothing is enabled.
        
        :type: bool
        """
        pass
    
    @polySmoothingEnabled.setter
    def polySmoothingEnabled(self, value: bool):
        pass
    
    @property
    def derivatives(self) -> QualityHint:
        """
        A :class:`QualityHint` with the derivatives hint.
        
        :type: QualityHint
        """
        pass
    
    @derivatives.setter
    def derivatives(self, value: QualityHint):
        pass
    
    @property
    def textureCompression(self) -> QualityHint:
        """
        A :class:`QualityHint` with the texture compression hint.
        
        :type: QualityHint
        """
        pass
    
    @textureCompression.setter
    def textureCompression(self, value: QualityHint):
        pass
    
    @property
    def lineSmoothing(self) -> QualityHint:
        """
        A :class:`QualityHint` with the line smoothing hint.
        
        :type: QualityHint
        """
        pass
    
    @lineSmoothing.setter
    def lineSmoothing(self, value: QualityHint):
        pass
    
    @property
    def polySmoothing(self) -> QualityHint:
        """
        A :class:`QualityHint` with the polygon smoothing hint.
        
        :type: QualityHint
        """
        pass
    
    @polySmoothing.setter
    def polySmoothing(self, value: QualityHint):
        pass
    
