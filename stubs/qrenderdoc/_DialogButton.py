from enum import IntFlag

class DialogButton(IntFlag):
    # Original docstring
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
    
    
    # Enum values
    
    OK = 1024
    """
    An OK button
    """
    
    Save = 2048
    """
    A Save button
    """
    
    SaveAll = 4096
    """
    A Save All button
    """
    
    Open = 8192
    """
    An Open button
    """
    
    Yes = 16384
    """
    A Yes button
    """
    
    YesToAll = 32768
    """
    A Yes To All button
    """
    
    No = 65536
    """
    A No button
    """
    
    NoToAll = 131072
    """
    A No To All button
    """
    
    Abort = 262144
    """
    An Abort button
    """
    
    Retry = 524288
    """
    A Retry button
    """
    
    Ignore = 1048576
    """
    An Ignore button
    """
    
    Close = 2097152
    """
    A Close button
    """
    
    Cancel = 4194304
    """
    A Cancel button
    """
    
    Discard = 8388608
    """
    A Discard button
    """
    
    Help = 16777216
    """
    A Help button
    """
    
    Apply = 33554432
    """
    An Apply button
    """
    
    Reset = 67108864
    """
    A Reset button
    """
    
    RestoreDefaults = 134217728
    """
    A Restore Defaults button
    """
    

# Assign __doc__ for enum values for easier introspection

DialogButton.OK.__doc__ = """
An OK button
"""

DialogButton.Save.__doc__ = """
A Save button
"""

DialogButton.SaveAll.__doc__ = """
A Save All button
"""

DialogButton.Open.__doc__ = """
An Open button
"""

DialogButton.Yes.__doc__ = """
A Yes button
"""

DialogButton.YesToAll.__doc__ = """
A Yes To All button
"""

DialogButton.No.__doc__ = """
A No button
"""

DialogButton.NoToAll.__doc__ = """
A No To All button
"""

DialogButton.Abort.__doc__ = """
An Abort button
"""

DialogButton.Retry.__doc__ = """
A Retry button
"""

DialogButton.Ignore.__doc__ = """
An Ignore button
"""

DialogButton.Close.__doc__ = """
A Close button
"""

DialogButton.Cancel.__doc__ = """
A Cancel button
"""

DialogButton.Discard.__doc__ = """
A Discard button
"""

DialogButton.Help.__doc__ = """
A Help button
"""

DialogButton.Apply.__doc__ = """
An Apply button
"""

DialogButton.Reset.__doc__ = """
A Reset button
"""

DialogButton.RestoreDefaults.__doc__ = """
A Restore Defaults button
"""

