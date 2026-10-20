from enum import IntEnum

class WindowMenu(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    Unknown = 0
    """
    Unknown/invalid window.
    """
    
    File = 1
    """
    The menu item will be in a section between Open/Save/Close captures and Import/Export.
    """
    
    Window = 2
    """
    The menu item will be in a new section at the end of the menu.
    """
    
    Tools = 3
    """
    The menu item will be added to a new section above Settings.
    """
    
    NewMenu = 4
    """
    The menu item will be a root menu, placed between Tools and Help.
    """
    
    Help = 5
    """
    The menu item will be added after the error reporting item.
    """
    

# Assign __doc__ for enum values for easier introspection

WindowMenu.Unknown.__doc__ = """
Unknown/invalid window.
"""

WindowMenu.File.__doc__ = """
The menu item will be in a section between Open/Save/Close captures and Import/Export.
"""

WindowMenu.Window.__doc__ = """
The menu item will be in a new section at the end of the menu.
"""

WindowMenu.Tools.__doc__ = """
The menu item will be added to a new section above Settings.
"""

WindowMenu.NewMenu.__doc__ = """
The menu item will be a root menu, placed between Tools and Help.
"""

WindowMenu.Help.__doc__ = """
The menu item will be added after the error reporting item.
"""

