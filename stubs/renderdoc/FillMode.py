# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class FillMode(__enum.IntEnum):
    """
    The fill mode for polygons.
    
    .. data:: Solid
    
      Polygons are filled in and rasterized solidly.
    
    .. data:: Wireframe
    
      Polygons are rendered only with lines along their edges, forming a wireframe.
    
    .. data:: Point
    
      Only the points at the polygons vertices are rendered.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Point = 2
    """ Only the points at the polygons vertices are rendered. """

    Solid = 0
    """ Polygons are filled in and rasterized solidly. """

    Wireframe = 1
    """ Polygons are rendered only with lines along their edges, forming a wireframe. """



