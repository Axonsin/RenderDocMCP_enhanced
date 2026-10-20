from enum import IntEnum

class CaptureModifications(IntEnum):
    # Original docstring
    """
    Details any changes that have been made to a capture in the UI which can be saved to
    disk but currently aren't. Note that detection is conservative - e.g. if a change is made, then
    cancelled out by reversing the change, this will still count as 'modified' even if the end result is
    the same data. In that sense it's analogous to adding and then deleting some characters in a text
    editor, since there is no actual undo system.
    
    This is a bitmask, so several values can be present at once.
    
    .. data:: NoModifications
    
      Fixed value of 0 indicating no modifications have been made.
    
    .. data:: Renames
    
      One or more resources have been given a custom name which hasn't been saved.
    
    .. data:: Bookmarks
    
      Event bookmarks have been added or removed.
    
    .. data:: Notes
    
      The general notes field has been changed.
    
    .. data:: EditedShaders
    
      There are shader editing changes (new edits or reverts).
    
    .. data:: All
    
      Fixed value with all bits set, indication all modifications have been made.
    """
    
    
    # Enum values
    
    NoModifications = 0
    """
    Fixed value of 0 indicating no modifications have been made.
    """
    
    Renames = 1
    """
    One or more resources have been given a custom name which hasn't been saved.
    """
    
    Bookmarks = 2
    """
    Event bookmarks have been added or removed.
    """
    
    Notes = 4
    """
    The general notes field has been changed.
    """
    
    EditedShaders = 8
    """
    There are shader editing changes (new edits or reverts).
    """
    
    All = -1
    """
    Fixed value with all bits set, indication all modifications have been made.
    """
    

# Assign __doc__ for enum values for easier introspection

CaptureModifications.NoModifications.__doc__ = """
Fixed value of 0 indicating no modifications have been made.
"""

CaptureModifications.Renames.__doc__ = """
One or more resources have been given a custom name which hasn't been saved.
"""

CaptureModifications.Bookmarks.__doc__ = """
Event bookmarks have been added or removed.
"""

CaptureModifications.Notes.__doc__ = """
The general notes field has been changed.
"""

CaptureModifications.EditedShaders.__doc__ = """
There are shader editing changes (new edits or reverts).
"""

CaptureModifications.All.__doc__ = """
Fixed value with all bits set, indication all modifications have been made.
"""

