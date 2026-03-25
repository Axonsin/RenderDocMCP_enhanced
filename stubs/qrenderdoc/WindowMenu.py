# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class WindowMenu(__enum.IntEnum):
    """
    Specifies the base menu to add a menu item into.
    
    .. data:: Unknown
    
      Unknown/invalid window.
    
    .. data:: File
    
      The menu item will be in a section between Open/Save/Close captures and Import/Export.
    
    .. data:: Window
    
      The menu item will be in a new section at the end of the menu.
    
    .. data:: Tools
    
      The menu item will be added to a new section above Settings.
    
    .. data:: NewMenu
    
      The menu item will be a root menu, placed between Tools and Help.
    
    .. data:: Help
    
      The menu item will be added after the error reporting item.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    File = 1
    """ The menu item will be in a section between Open/Save/Close captures and Import/Export. """

    Help = 5
    """ The menu item will be added after the error reporting item. """

    NewMenu = 4
    """ The menu item will be a root menu, placed between Tools and Help. """

    Tools = 3
    """ The menu item will be added to a new section above Settings. """

    Unknown = 0
    """ Unknown/invalid window. """

    Window = 2
    """ The menu item will be in a new section at the end of the menu. """



