# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DebugVariableType(__enum.IntEnum):
    """
    Represents the category of debugging variable that a source variable maps to.
    
    .. data:: Undefined
    
      Undefined type.
    
    .. data:: Input
    
      A constant input value, stored globally.
    
    .. data:: Constant
    
      A constant buffer value, stored globally.
    
    .. data:: Sampler
    
      A sampler, stored globally.
    
    .. data:: ReadOnlyResource
    
      A read-only resource, stored globally.
    
    .. data:: ReadWriteResource
    
      A read-write resource, stored globally.
    
    .. data:: Variable
    
      A mutable variable, stored per state.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Constant = 2
    """ A constant buffer value, stored globally. """

    Input = 1
    """ A constant input value, stored globally. """

    ReadOnlyResource = 4
    """ A read-only resource, stored globally. """

    ReadWriteResource = 5
    """ A read-write resource, stored globally. """

    Sampler = 3
    """ A sampler, stored globally. """

    Undefined = 0
    """ Undefined type. """

    Variable = 6
    """ A mutable variable, stored per state. """



