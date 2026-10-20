from enum import IntEnum

class WindowingSystem(IntEnum):
    # Original docstring
    """
    Specifies a windowing system to use for creating an output window.
    
    .. data:: Unknown
    
      Unknown window type, no windowing data is passed and no native window is described.
    
    .. data:: Headless
    
      The windowing data doesn't describe a real window but a virtual area, allowing all normal output
      rendering to happen off-screen.
      See :func:`CreateHeadlessWindowingData`.
    
    .. data:: Win32
    
      The windowing data refers to a Win32 window. See :func:`CreateWin32WindowingData`.
    
    .. data:: Xlib
    
      The windowing data refers to an Xlib window. See :func:`CreateXlibWindowingData`.
    
    .. data:: XCB
    
      The windowing data refers to an XCB window. See :func:`CreateXCBWindowingData`.
    
    .. data:: Android
    
      The windowing data refers to an Android window. See :func:`CreateAndroidWindowingData`.
    
    .. data:: MacOS
    
      The windowing data refers to a MacOS / OS X NSView & CALayer that is Metal/GL compatible.
      See :func:`CreateMacOSWindowingData`.
    
    .. data:: Wayland
    
      The windowing data refers to an Wayland window. See :func:`CreateWaylandWindowingData`.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    Unknown window type, no windowing data is passed and no native window is described.
    """
    
    Headless = 1
    """
    The windowing data doesn't describe a real window but a virtual area, allowing all normal output
    rendering to happen off-screen.
    See :func:`CreateHeadlessWindowingData`.
    """
    
    Win32 = 2
    """
    The windowing data refers to a Win32 window. See :func:`CreateWin32WindowingData`.
    """
    
    Xlib = 3
    """
    The windowing data refers to an Xlib window. See :func:`CreateXlibWindowingData`.
    """
    
    XCB = 4
    """
    The windowing data refers to an XCB window. See :func:`CreateXCBWindowingData`.
    """
    
    Android = 5
    """
    The windowing data refers to an Android window. See :func:`CreateAndroidWindowingData`.
    """
    
    MacOS = 6
    """
    The windowing data refers to a MacOS / OS X NSView & CALayer that is Metal/GL compatible.
    See :func:`CreateMacOSWindowingData`.
    """
    
    Wayland = 7
    """
    The windowing data refers to an Wayland window. See :func:`CreateWaylandWindowingData`.
    """
    

# Assign __doc__ for enum values for easier introspection

WindowingSystem.Unknown.__doc__ = """
Unknown window type, no windowing data is passed and no native window is described.
"""

WindowingSystem.Headless.__doc__ = """
The windowing data doesn't describe a real window but a virtual area, allowing all normal output
rendering to happen off-screen.
See :func:`CreateHeadlessWindowingData`.
"""

WindowingSystem.Win32.__doc__ = """
The windowing data refers to a Win32 window. See :func:`CreateWin32WindowingData`.
"""

WindowingSystem.Xlib.__doc__ = """
The windowing data refers to an Xlib window. See :func:`CreateXlibWindowingData`.
"""

WindowingSystem.XCB.__doc__ = """
The windowing data refers to an XCB window. See :func:`CreateXCBWindowingData`.
"""

WindowingSystem.Android.__doc__ = """
The windowing data refers to an Android window. See :func:`CreateAndroidWindowingData`.
"""

WindowingSystem.MacOS.__doc__ = """
The windowing data refers to a MacOS / OS X NSView & CALayer that is Metal/GL compatible.
See :func:`CreateMacOSWindowingData`.
"""

WindowingSystem.Wayland.__doc__ = """
The windowing data refers to an Wayland window. See :func:`CreateWaylandWindowingData`.
"""

