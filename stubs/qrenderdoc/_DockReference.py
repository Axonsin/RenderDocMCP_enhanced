from enum import IntEnum

class DockReference(IntEnum):
    # Original docstring
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
    
    
    # Enum values
    
    LastUsedArea = 0
    """
    The existing dock window is not used, the new dock window is placed wherever the last dock window
    was placed.
    """
    
    NewFloatingArea = 1
    """
    The existing dock window is not used, the new dock window is placed in a new floating area.
    """
    
    EmptySpace = 2
    """
    The existing dock window is not used, the new dock window is placed in empty area in the dockarea.
    """
    
    NoArea = 3
    """
    The existing dock window is not used, the new window is hidden.
    """
    
    AddTo = 4
    """
    The new dock window is placed in a tab set with the existing dock window.
    """
    
    LeftOf = 5
    """
    The new dock window is placed to the left of the existing dock window, at a specified proportion.
    """
    
    RightOf = 6
    """
    The new dock window is placed to the right of the existing dock window, at a specified proportion.
    """
    
    TopOf = 7
    """
    The new dock window is placed above the existing dock window, at a specified proportion.
    """
    
    BottomOf = 8
    """
    The new dock window is placed below the existing dock window, at a specified proportion.
    """
    
    LeftWindowSide = 9
    """
    The new dock window is placed left of *all* docks in the window, at a specified proportion.
    """
    
    RightWindowSide = 10
    """
    The new dock window is placed right of *all* docks in the window, at a specified proportion.
    """
    
    TopWindowSide = 11
    """
    The new dock window is placed above *all* docks in the window, at a specified proportion.
    """
    
    BottomWindowSide = 12
    """
    The new dock window is placed below *all* docks in the window, at a specified proportion.
    """
    
    MainToolArea = 13
    """
    The new dock window is placed in the 'main' tool area as defined by finding an existing known
    window and using that as the main area. In the default layout this is where most windows are
    placed.
    """
    
    LeftToolArea = 14
    """
    The new dock window is placed in the 'left' tool area as defined by finding an existing known
    window and using that as the main area, then adding to the left of that. In the default layout
    this is where the event browser is placed.
    """
    
    TransientPopupArea = 15
    """
    The new dock window is docked with other similar transient views like constant buffer or pixel
    history windows, if they exist, or else docked to the right of the main window.
    """
    

# Assign __doc__ for enum values for easier introspection

DockReference.LastUsedArea.__doc__ = """
The existing dock window is not used, the new dock window is placed wherever the last dock window
was placed.
"""

DockReference.NewFloatingArea.__doc__ = """
The existing dock window is not used, the new dock window is placed in a new floating area.
"""

DockReference.EmptySpace.__doc__ = """
The existing dock window is not used, the new dock window is placed in empty area in the dockarea.
"""

DockReference.NoArea.__doc__ = """
The existing dock window is not used, the new window is hidden.
"""

DockReference.AddTo.__doc__ = """
The new dock window is placed in a tab set with the existing dock window.
"""

DockReference.LeftOf.__doc__ = """
The new dock window is placed to the left of the existing dock window, at a specified proportion.
"""

DockReference.RightOf.__doc__ = """
The new dock window is placed to the right of the existing dock window, at a specified proportion.
"""

DockReference.TopOf.__doc__ = """
The new dock window is placed above the existing dock window, at a specified proportion.
"""

DockReference.BottomOf.__doc__ = """
The new dock window is placed below the existing dock window, at a specified proportion.
"""

DockReference.LeftWindowSide.__doc__ = """
The new dock window is placed left of *all* docks in the window, at a specified proportion.
"""

DockReference.RightWindowSide.__doc__ = """
The new dock window is placed right of *all* docks in the window, at a specified proportion.
"""

DockReference.TopWindowSide.__doc__ = """
The new dock window is placed above *all* docks in the window, at a specified proportion.
"""

DockReference.BottomWindowSide.__doc__ = """
The new dock window is placed below *all* docks in the window, at a specified proportion.
"""

DockReference.MainToolArea.__doc__ = """
The new dock window is placed in the 'main' tool area as defined by finding an existing known
window and using that as the main area. In the default layout this is where most windows are
placed.
"""

DockReference.LeftToolArea.__doc__ = """
The new dock window is placed in the 'left' tool area as defined by finding an existing known
window and using that as the main area, then adding to the left of that. In the default layout
this is where the event browser is placed.
"""

DockReference.TransientPopupArea.__doc__ = """
The new dock window is docked with other similar transient views like constant buffer or pixel
history windows, if they exist, or else docked to the right of the main window.
"""

