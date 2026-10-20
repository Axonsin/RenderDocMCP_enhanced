from typing import Callable

# Dummy types
from . import QWidget

class MainWindow():
    # Original docstring
    """
    The main parent window of the application.
    
    This window is retrieved by calling :meth:`CaptureContext.GetMainWindow`.
    
    .. function:: ShortcutCallback(QWidget focusWidget)
    
      Not a member function - the signature for any ``ShortcutCallback`` callbacks.
    
      :param QWidget focusWidget: The widget with focus at the time this shortcut was detected. May be
         ``None``.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`MainWindow` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def RegisterShortcut(self, shortcut: str, widget: QWidget, callback: Callable[[QWidget], None]):
        """
        Register a callback for a particular key shortcut.
        
        This creates a managed shortcut. Qt's shortcut system doesn't allow specialisation/duplication, so
        you can't use ``Ctrl+S`` for a shortcut in a window to update some changes if there's also a global
        ``Ctrl+S`` shortcut on the window. In the end, neither shortcut will be called.
        
        Instead this function allows the main window to manage shortcuts internally, and it will pick the
        closest shortcut to a given action. The search goes from the widget with the focus currently up the
        chain of parents, with the first match being used. If no matches are found, then a 'global' default
        will be invoked, if it exists.
        
        :param str shortcut: The text string representing the shortcut, e.g. :kbd:`Ctrl+S`.
        :param QWidget widget: A handle to the widget to use as the context for this shortcut, or ``None``
          for a global shortcut. Note that if an existing global shortcut exists the new one will not be
          registered.
        :param Callable[[QWidget], None] callback: The function to callback when the shortcut is hit.
          Callback function signature must match :func:`ShortcutCallback`.
        """
        pass
    
    
    def UnregisterShortcut(self, shortcut: str, widget: QWidget):
        """
        Unregister a callback for a particular key shortcut, made in a previous call to
        :meth:`RegisterShortcut`.
        
        See the documentation for :meth:`RegisterShortcut` for what these shortcuts are for.
        
        :param str shortcut: The text string representing the shortcut, e.g. :kbd:`Ctrl+S`. To unregister all
          shortcuts for a particular widget, you can pass an empty string here. In this case,
          :paramref:`UnregisterShortcut.widget` must not be ``None``.
        :param QWidget widget: A handle to the widget used as the context for the shortcut, or ``None``
          if referring to a global shortcut.
        """
        pass
    
    
    def BringToFront(self):
        """
        Attempts to bring the main window to the front to the user's focus.
        
        This may not be possible on all OSs, so the function is not guaranteed to succeed.
        """
        pass
    
    
    def PromptCloseCapture(self) -> bool:
        """
        Prompt the user to close the currently open capture file. This will go through the
        normal workflow and ask the user to save any unsaved capture.
        
        If no capture is open, this function returns True immediately.
        
        :return: True if no capture was open, or if it was successfully closed. False if the capture is
          still open due to user interactions.
        :rtype: bool
        """
        pass
    
