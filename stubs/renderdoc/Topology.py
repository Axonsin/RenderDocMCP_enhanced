# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class Topology(__enum.IntEnum):
    """
    A primitive topology used for processing vertex data.
    
    .. data:: Unknown
    
      An unknown or undefined topology.
    
    .. data:: PointList
    
      A point list.
    
    .. data:: LineList
    
      A line list.
    
    .. data:: LineStrip
    
      A line strip.
    
    .. data:: LineLoop
    
      A line loop.
    
    .. data:: TriangleList
    
      A triangle list.
    
    .. data:: TriangleStrip
    
      A triangle strip.
    
    .. data:: TriangleFan
    
      A triangle fan.
    
    .. data:: LineList_Adj
    
      A line list with adjacency information.
    
    .. data:: LineStrip_Adj
    
      A line strip with adjacency information.
    
    .. data:: TriangleList_Adj
    
      A triangle list with adjacency information.
    
    .. data:: TriangleStrip_Adj
    
      A triangle strip with adjacency information.
    
    .. data:: PatchList
    
      An alias for :data:`PatchList_1CPs`.
    
    .. data:: PatchList_1CPs
    
      A patch list with 1 control points.
    
    .. data:: PatchList_2CPs
    
      A patch list with 2 control points.
    
    .. data:: PatchList_3CPs
    
      A patch list with 3 control points.
    
    .. data:: PatchList_4CPs
    
      A patch list with 4 control points.
    
    .. data:: PatchList_5CPs
    
      A patch list with 5 control points.
    
    .. data:: PatchList_6CPs
    
      A patch list with 6 control points.
    
    .. data:: PatchList_7CPs
    
      A patch list with 7 control points.
    
    .. data:: PatchList_8CPs
    
      A patch list with 8 control points.
    
    .. data:: PatchList_9CPs
    
      A patch list with 9 control points.
    
    .. data:: PatchList_10CPs
    
      A patch list with 10 control points.
    
    .. data:: PatchList_11CPs
    
      A patch list with 11 control points.
    
    .. data:: PatchList_12CPs
    
      A patch list with 12 control points.
    
    .. data:: PatchList_13CPs
    
      A patch list with 13 control points.
    
    .. data:: PatchList_14CPs
    
      A patch list with 14 control points.
    
    .. data:: PatchList_15CPs
    
      A patch list with 15 control points.
    
    .. data:: PatchList_16CPs
    
      A patch list with 16 control points.
    
    .. data:: PatchList_17CPs
    
      A patch list with 17 control points.
    
    .. data:: PatchList_18CPs
    
      A patch list with 18 control points.
    
    .. data:: PatchList_19CPs
    
      A patch list with 19 control points.
    
    .. data:: PatchList_20CPs
    
      A patch list with 20 control points.
    
    .. data:: PatchList_21CPs
    
      A patch list with 21 control points.
    
    .. data:: PatchList_22CPs
    
      A patch list with 22 control points.
    
    .. data:: PatchList_23CPs
    
      A patch list with 23 control points.
    
    .. data:: PatchList_24CPs
    
      A patch list with 24 control points.
    
    .. data:: PatchList_25CPs
    
      A patch list with 25 control points.
    
    .. data:: PatchList_26CPs
    
      A patch list with 26 control points.
    
    .. data:: PatchList_27CPs
    
      A patch list with 27 control points.
    
    .. data:: PatchList_28CPs
    
      A patch list with 28 control points.
    
    .. data:: PatchList_29CPs
    
      A patch list with 29 control points.
    
    .. data:: PatchList_30CPs
    
      A patch list with 30 control points.
    
    .. data:: PatchList_31CPs
    
      A patch list with 31 control points.
    
    .. data:: PatchList_32CPs
    
      A patch list with 32 control points.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    LineList = 2
    """ A line list. """

    LineList_Adj = 8
    """ A line list with adjacency information. """

    LineLoop = 4
    """ A line loop. """

    LineStrip = 3
    """ A line strip. """

    LineStrip_Adj = 9
    """ A line strip with adjacency information. """

    PatchList = 12
    """ An alias for :data:`PatchList_1CPs`. """

    PatchList_10CPs = 21
    """ A patch list with 10 control points. """

    PatchList_11CPs = 22
    """ A patch list with 11 control points. """

    PatchList_12CPs = 23
    """ A patch list with 12 control points. """

    PatchList_13CPs = 24
    """ A patch list with 13 control points. """

    PatchList_14CPs = 25
    """ A patch list with 14 control points. """

    PatchList_15CPs = 26
    """ A patch list with 15 control points. """

    PatchList_16CPs = 27
    """ A patch list with 16 control points. """

    PatchList_17CPs = 28
    """ A patch list with 17 control points. """

    PatchList_18CPs = 29
    """ A patch list with 18 control points. """

    PatchList_19CPs = 30
    """ A patch list with 19 control points. """

    PatchList_1CPs = 12
    """ A patch list with 1 control points. """

    PatchList_20CPs = 31
    """ A patch list with 20 control points. """

    PatchList_21CPs = 32
    """ A patch list with 21 control points. """

    PatchList_22CPs = 33
    """ A patch list with 22 control points. """

    PatchList_23CPs = 34
    """ A patch list with 23 control points. """

    PatchList_24CPs = 35
    """ A patch list with 24 control points. """

    PatchList_25CPs = 36
    """ A patch list with 25 control points. """

    PatchList_26CPs = 37
    """ A patch list with 26 control points. """

    PatchList_27CPs = 38
    """ A patch list with 27 control points. """

    PatchList_28CPs = 39
    """ A patch list with 28 control points. """

    PatchList_29CPs = 40
    """ A patch list with 29 control points. """

    PatchList_2CPs = 13
    """ A patch list with 2 control points. """

    PatchList_30CPs = 41
    """ A patch list with 30 control points. """

    PatchList_31CPs = 42
    """ A patch list with 31 control points. """

    PatchList_32CPs = 43
    """ A patch list with 32 control points. """

    PatchList_3CPs = 14
    """ A patch list with 3 control points. """

    PatchList_4CPs = 15
    """ A patch list with 4 control points. """

    PatchList_5CPs = 16
    """ A patch list with 5 control points. """

    PatchList_6CPs = 17
    """ A patch list with 6 control points. """

    PatchList_7CPs = 18
    """ A patch list with 7 control points. """

    PatchList_8CPs = 19
    """ A patch list with 8 control points. """

    PatchList_9CPs = 20
    """ A patch list with 9 control points. """

    PointList = 1
    """ A point list. """

    TriangleFan = 7
    """ A triangle fan. """

    TriangleList = 5
    """ A triangle list. """

    TriangleList_Adj = 10
    """ A triangle list with adjacency information. """

    TriangleStrip = 6
    """ A triangle strip. """

    TriangleStrip_Adj = 11
    """ A triangle strip with adjacency information. """

    Unknown = 0
    """ An unknown or undefined topology. """



