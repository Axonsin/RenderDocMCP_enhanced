# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DialogButton(__enum.IntFlag):
    """
    A button for a dialog prompt.
    
    .. data:: OK
    
      An OK button
    
    .. data:: Save
    
      A Save button
    
    .. data:: SaveAll
    
      A Save All button
    
    .. data:: Open
    
      An Open button
    
    .. data:: Yes
    
      A Yes button
    
    .. data:: YesToAll
    
      A Yes To All button
    
    .. data:: No
    
      A No button
    
    .. data:: NoToAll
    
      A No To All button
    
    .. data:: Abort
    
      An Abort button
    
    .. data:: Retry
    
      A Retry button
    
    .. data:: Ignore
    
      An Ignore button
    
    .. data:: Close
    
      A Close button
    
    .. data:: Cancel
    
      A Cancel button
    
    .. data:: Discard
    
      A Discard button
    
    .. data:: Help
    
      A Help button
    
    .. data:: Apply
    
      An Apply button
    
    .. data:: Reset
    
      A Reset button
    
    .. data:: RestoreDefaults
    
      A Restore Defaults button
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Abort = 262144
    """ An Abort button """

    Apply = 33554432
    """ An Apply button """

    Cancel = 4194304
    """ A Cancel button """

    Close = 2097152
    """ A Close button """

    Discard = 8388608
    """ A Discard button """

    Help = 16777216
    """ A Help button """

    Ignore = 1048576
    """ An Ignore button """

    No = 65536
    """ A No button """

    NoToAll = 131072
    """ A No To All button """

    OK = 1024
    """ An OK button """

    Open = 8192
    """ An Open button """

    Reset = 67108864
    """ A Reset button """

    RestoreDefaults = 134217728
    """ A Restore Defaults button """

    Retry = 524288
    """ A Retry button """

    Save = 2048
    """ A Save button """

    SaveAll = 4096
    """ A Save All button """

    Yes = 16384
    """ A Yes button """

    YesToAll = 32768
    """ A Yes To All button """



