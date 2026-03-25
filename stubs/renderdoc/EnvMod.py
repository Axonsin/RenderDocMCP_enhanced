# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class EnvMod(__enum.IntEnum):
    """
    How to modify an environment variable.
    
    .. data:: Set
    
      Set the variable to the given value.
    
    .. data:: Append
    
      Add the given value to the end of the variable, using the separator.
    
    .. data:: Prepend
    
      Add the given value to the start of the variable, using the separator.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Append = 1
    """ Add the given value to the end of the variable, using the separator. """

    Prepend = 2
    """ Add the given value to the start of the variable, using the separator. """

    Set = 0
    """ Set the variable to the given value. """



