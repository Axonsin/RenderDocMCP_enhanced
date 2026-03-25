# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureSliceMapping(): # skipped bases: <class 'SwigPyObject'>
    """
    How to map array textures for saving to non-arrayed file formats.
    
    If :data:`sliceIndex` is -1, :data:`cubeCruciform` == :data:`slicesAsGrid` == ``False`` and the file
    format doesn't support saving all slices, only slice 0 is saved.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55232970>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.TextureSliceMapping\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.TextureSliceMapping\' objects>, \'slicesAsGrid\': <attribute \'slicesAsGrid\' of \'renderdoc.TextureSliceMapping\' objects>, \'sliceIndex\': <attribute \'sliceIndex\' of \'renderdoc.TextureSliceMapping\' objects>, \'cubeCruciform\': <attribute \'cubeCruciform\' of \'renderdoc.TextureSliceMapping\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.TextureSliceMapping\' objects>, \'sliceGridWidth\': <attribute \'sliceGridWidth\' of \'renderdoc.TextureSliceMapping\' objects>, \'__doc__\': "\\nHow to map array textures for saving to non-arrayed file formats.\\n\\nIf :data:`sliceIndex` is -1, :data:`cubeCruciform` == :data:`slicesAsGrid` == ``False`` and the file\\nformat doesn\'t support saving all slices, only slice 0 is saved.\\n\\n"})'


