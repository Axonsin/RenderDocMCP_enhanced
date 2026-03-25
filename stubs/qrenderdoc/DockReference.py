# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DockReference(__enum.IntEnum):
    """
    Specifies the relationship between the existing dock window and the new one when adding
    a new dock window or moving an existing dock window.
    
    .. data:: LastUsedArea
    
      The existing dock window is not used, the new dock window is placed wherever the last dock window
      was placed.
    
    .. data:: NewFloatingArea
    
      The existing dock window is not used, the new dock window is placed in a new floating area.
    
    .. data:: EmptySpace
    
      The existing dock window is not used, the new dock window is placed in empty area in the dockarea.
    
    .. data:: NoArea
    
      The existing dock window is not used, the new window is hidden.
    
    .. data:: AddTo
    
      The new dock window is placed in a tab set with the existing dock window.
    
    .. data:: LeftOf
    
      The new dock window is placed to the left of the existing dock window, at a specified proportion.
    
    .. data:: RightOf
    
      The new dock window is placed to the right of the existing dock window, at a specified proportion.
    
    .. data:: TopOf
    
      The new dock window is placed above the existing dock window, at a specified proportion.
    
    .. data:: BottomOf
    
      The new dock window is placed below the existing dock window, at a specified proportion.
    
    .. data:: LeftWindowSide
    
      The new dock window is placed left of *all* docks in the window, at a specified proportion.
    
    .. data:: RightWindowSide
    
      The new dock window is placed right of *all* docks in the window, at a specified proportion.
    
    .. data:: TopWindowSide
    
      The new dock window is placed above *all* docks in the window, at a specified proportion.
    
    .. data:: BottomWindowSide
    
      The new dock window is placed below *all* docks in the window, at a specified proportion.
    
    .. data:: MainToolArea
    
      The new dock window is placed in the 'main' tool area as defined by finding an existing known
      window and using that as the main area. In the default layout this is where most windows are
      placed.
    
    .. data:: LeftToolArea
    
      The new dock window is placed in the 'left' tool area as defined by finding an existing known
      window and using that as the main area, then adding to the left of that. In the default layout
      this is where the event browser is placed.
    
    .. data:: TransientPopupArea
    
      The new dock window is docked with other similar transient views like constant buffer or pixel
      history windows, if they exist, or else docked to the right of the main window.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AddTo = 4
    """ The new dock window is placed in a tab set with the existing dock window. """

    BottomOf = 8
    """ The new dock window is placed below the existing dock window, at a specified proportion. """

    BottomWindowSide = 12
    """ The new dock window is placed below *all* docks in the window, at a specified proportion. """

    EmptySpace = 2
    """ The existing dock window is not used, the new dock window is placed in empty area in the dockarea. """

    LastUsedArea = 0
    """
    The existing dock window is not used, the new dock window is placed wherever the last dock window
      was placed.
    """

    LeftOf = 5
    """ The new dock window is placed to the left of the existing dock window, at a specified proportion. """

    LeftToolArea = 14
    """
    The new dock window is placed in the 'left' tool area as defined by finding an existing known
      window and using that as the main area, then adding to the left of that. In the default layout
      this is where the event browser is placed.
    """

    LeftWindowSide = 9
    """ The new dock window is placed left of *all* docks in the window, at a specified proportion. """

    MainToolArea = 13
    """
    The new dock window is placed in the 'main' tool area as defined by finding an existing known
      window and using that as the main area. In the default layout this is where most windows are
      placed.
    """

    NewFloatingArea = 1
    """ The existing dock window is not used, the new dock window is placed in a new floating area. """

    NoArea = 3
    """ The existing dock window is not used, the new window is hidden. """

    RightOf = 6
    """ The new dock window is placed to the right of the existing dock window, at a specified proportion. """

    RightWindowSide = 10
    """ The new dock window is placed right of *all* docks in the window, at a specified proportion. """

    TopOf = 7
    """ The new dock window is placed above the existing dock window, at a specified proportion. """

    TopWindowSide = 11
    """ The new dock window is placed above *all* docks in the window, at a specified proportion. """

    TransientPopupArea = 15
    """
    The new dock window is docked with other similar transient views like constant buffer or pixel
      history windows, if they exist, or else docked to the right of the main window.
    """



