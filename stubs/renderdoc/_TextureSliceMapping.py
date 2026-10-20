
from typing import overload

class TextureSliceMapping():
    # Original docstring
    """
    How to map array textures for saving to non-arrayed file formats.
    
    If :data:`sliceIndex` is -1, :data:`cubeCruciform` == :data:`slicesAsGrid` == ``False`` and the file
    format doesn't support saving all slices, only slice 0 is saved.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureSliceMapping.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureSliceMapping'):
        """
        Construct a new TextureSliceMapping with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def slicesAsGrid(self) -> bool:
        """
        If ``True``, write out the slices as a 2D grid with the width given in :data:`sliceGridWidth`. Any
        empty slices in the grid are written as transparent black.
        
        :type: bool
        """
        pass
    
    @slicesAsGrid.setter
    def slicesAsGrid(self, value: bool):
        pass
    
    @property
    def sliceIndex(self) -> int:
        """
        Selects the (depth/array) slice to save.
        
        If this is -1, then all slices are written out as detailed below. This is only supported in formats
        that don't support slices natively, and will be done in RGBA8.
        
        :type: int
        """
        pass
    
    @sliceIndex.setter
    def sliceIndex(self, value: int):
        pass
    
    @property
    def cubeCruciform(self) -> bool:
        """
        Write out 6 slices in a cruciform pattern::
        
                  +----+
                  | +y |
                  |    |
             +----+----+----+----+
             | -x | +z | +x | -z |
             |    |    |    |    |
             +----+----+----+----+
                  | -y |
                  |    |
                  +----+
        
        With the gaps filled in with transparent black.
        
        :type: bool
        """
        pass
    
    @cubeCruciform.setter
    def cubeCruciform(self, value: bool):
        pass
    
    @property
    def sliceGridWidth(self) -> int:
        """
        The width of a grid if :data:`slicesAsGrid` is ``True``.
        
        :type: int
        """
        pass
    
    @sliceGridWidth.setter
    def sliceGridWidth(self, value: int):
        pass
    
