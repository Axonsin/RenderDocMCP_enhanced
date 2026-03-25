# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class Visualisation(__enum.IntEnum):
    """
    What kind of visualisation to use when rendering a mesh.
    
    .. data:: NoSolid
    
      No solid shading should be done.
    
    .. data:: Solid
    
      The mesh should be rendered in a single flat unshaded color.
    
    .. data:: Lit
    
      The mesh should be rendered with face normals generated on the primitives and used for lighting.
    
    .. data:: Secondary
    
      The mesh should be rendered using the secondary element as color.
    
    .. data:: Explode
    
      The mesh should be rendered with vertices displaced and coloured by vertex ID.
    
    .. data:: Meshlet
    
      The mesh should be rendered colorising each meshlet differently.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Count = 6
    Explode = 4
    """ The mesh should be rendered with vertices displaced and coloured by vertex ID. """

    Lit = 2
    """ The mesh should be rendered with face normals generated on the primitives and used for lighting. """

    Meshlet = 5
    """ The mesh should be rendered colorising each meshlet differently. """

    NoSolid = 0
    """ No solid shading should be done. """

    Secondary = 3
    """ The mesh should be rendered using the secondary element as color. """

    Solid = 1
    """ The mesh should be rendered in a single flat unshaded color. """



