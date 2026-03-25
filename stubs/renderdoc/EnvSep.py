# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class EnvSep(__enum.IntEnum):
    """
    The separator to use if needed when modifying an environment variable.
    
    .. data:: Platform
    
      Use the character appropriate for separating items on the platform.
    
      On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
      ``:`` character will be used.
    
    .. data:: SemiColon
    
      Use a semi-colon ``;`` character.
    
    .. data:: Colon
    
      Use a colon ``:`` character.
    
    .. data:: NoSep
    
      No separator will be used.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Colon = 2
    """ Use a colon ``:`` character. """

    NoSep = 3
    """ No separator will be used. """

    Platform = 0
    """
    Use the character appropriate for separating items on the platform.
    
      On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
      ``:`` character will be used.
    """

    SemiColon = 1
    """ Use a semi-colon ``;`` character. """



