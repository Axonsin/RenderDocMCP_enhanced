# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ReplayOptimisationLevel(__enum.IntEnum):
    """
    The level of optimisation used in
    
    .. data:: NoOptimisation
    
      Completely disabled, no optimisation will be used at all.
    
    .. data:: Conservative
    
      Optimisation is used when it doesn't interfere with replay correctness.
    
    .. data:: Balanced
    
      Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
      resources appearing cleared instead of containing contents from prior frames where those resources
      are written to before being read.
    
    .. data:: Fastest
    
      All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
      This could result in side-effects like data from one replay being visible early in another replay,
      if it's known that the data will be overwritten before being used.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Balanced = 2
    """
    Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
      resources appearing cleared instead of containing contents from prior frames where those resources
      are written to before being read.
    """

    Conservative = 1
    """ Optimisation is used when it doesn't interfere with replay correctness. """

    Count = 4
    Fastest = 3
    """
    All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
      This could result in side-effects like data from one replay being visible early in another replay,
      if it's known that the data will be overwritten before being used.
    """

    First = 0
    NoOptimisation = 0
    """ Completely disabled, no optimisation will be used at all. """



