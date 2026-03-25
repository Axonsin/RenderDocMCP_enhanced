# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CompareFunction(__enum.IntEnum):
    """
    A comparison function to return a ``bool`` result from two inputs ``A`` and ``B``.
    
    .. data:: Never
    
      ``False``
    
    .. data:: AlwaysTrue
    
      ``True``
    
    .. data:: Less
    
      ``A < B``
    
    .. data:: LessEqual
    
      ``A <= B``
    
    .. data:: Greater
    
      ``A > B``
    
    .. data:: GreaterEqual
    
      ``A >= B``
    
    .. data:: Equal
    
      ``A == B``
    
    .. data:: NotEqual
    
      ``A != B``
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AlwaysTrue = 1
    """ ``True`` """

    Equal = 6
    """ ``A == B`` """

    Greater = 4
    """ ``A > B`` """

    GreaterEqual = 5
    """ ``A >= B`` """

    Less = 2
    """ ``A < B`` """

    LessEqual = 3
    """ ``A <= B`` """

    Never = 0
    """ ``False`` """

    NotEqual = 7
    """ ``A != B`` """



