# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class WindowingSystem(__enum.IntEnum):
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
    
      The windowing data refers to an Xlib window. See :func:`CreateXLibWindowingData`.
    
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Android = 5
    """ The windowing data refers to an Android window. See :func:`CreateAndroidWindowingData`. """

    Headless = 1
    """
    The windowing data doesn't describe a real window but a virtual area, allowing all normal output
      rendering to happen off-screen.
      See :func:`CreateHeadlessWindowingData`.
    """

    MacOS = 6
    """
    The windowing data refers to a MacOS / OS X NSView & CALayer that is Metal/GL compatible.
      See :func:`CreateMacOSWindowingData`.
    """

    Unknown = 0
    """ Unknown window type, no windowing data is passed and no native window is described. """

    Wayland = 7
    """ The windowing data refers to an Wayland window. See :func:`CreateWaylandWindowingData`. """

    Win32 = 2
    """ The windowing data refers to a Win32 window. See :func:`CreateWin32WindowingData`. """

    XCB = 4
    """ The windowing data refers to an XCB window. See :func:`CreateXCBWindowingData`. """

    Xlib = 3
    """ The windowing data refers to an Xlib window. See :func:`CreateXLibWindowingData`. """



