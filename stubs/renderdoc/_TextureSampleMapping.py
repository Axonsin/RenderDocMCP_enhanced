
from typing import overload

class TextureSampleMapping():
    # Original docstring
    """
    How to map multisampled textures for saving to non-multisampled file formats.
    
    .. data:: ResolveSamples
    
      Value for :data:`sampleIndex` if the samples should be averaged.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureSampleMapping.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureSampleMapping'):
        """
        Construct a new TextureSampleMapping with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    ResolveSamples = 4294967295
    """
    Value for :data:`sampleIndex` if the samples should be averaged.
    """
    
    @property
    def sampleIndex(self) -> int:
        """
        If :data:`mapToArray` is ``False`` this selects which sample should be extracted to treat as a
        normal 2D image. If set to :data:`ResolveSamples` then instead there's a default average resolve.
        
        :type: int
        """
        pass
    
    @sampleIndex.setter
    def sampleIndex(self, value: int):
        pass
    
    @property
    def mapToArray(self) -> bool:
        """
        ``True`` if the samples should be mapped to array slices. A multisampled array expands each slice
        in-place, so it would be slice 0: sample 0, slice 0: sample 1, slice 1: sample 0, etc.
        
        This then follows the mapping for array slices as with any other array texture. :data:`sampleIndex`
        is ignored.
        
        :type: bool
        """
        pass
    
    @mapToArray.setter
    def mapToArray(self, value: bool):
        pass
    
