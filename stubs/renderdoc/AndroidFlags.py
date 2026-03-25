# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class AndroidFlags(__enum.IntFlag):
    """
    INTERNAL: A set of flags giving details of the current status of Android tracability.
    
    .. data:: NoFlags
    
      There are no problems with the Android application setup.
    
    .. data:: Debuggable
    
      The application is debuggable.
    
    .. data:: RootAccess
    
       The device being targeted has root access.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Debuggable = 1
    """ The application is debuggable. """

    NoFlags = 0
    """ There are no problems with the Android application setup. """

    RootAccess = 2
    """ The device being targeted has root access. """



