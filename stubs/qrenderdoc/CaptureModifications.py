# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CaptureModifications(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    All = -1
    """ Fixed value with all bits set, indication all modifications have been made. """

    Bookmarks = 2
    """ Event bookmarks have been added or removed. """

    EditedShaders = 8
    """ There are shader editing changes (new edits or reverts). """

    NoModifications = 0
    """ Fixed value of 0 indicating no modifications have been made. """

    Notes = 4
    """ The general notes field has been changed. """

    Renames = 1
    """ One or more resources have been given a custom name which hasn't been saved. """



