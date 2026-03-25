# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class MainWindow(): # skipped bases: <class 'SwigPyObject'>
    """
    The main parent window of the application.
    
    This window is retrieved by calling :meth:`CaptureContext.GetMainWindow`.
    
    .. function:: ShortcutCallback(QWidget focusWidget)
    
      Not a member function - the signature for any ``ShortcutCallback`` callbacks.
    
      :param QWidget focusWidget: The widget with focus at the time this shortcut was detected. May be
         ``None``.
    """
    def BringToFront(self): # real signature unknown; restored from __doc__
        """
        BringToFront()
        
        Attempts to bring the main window to the front to the user's focus.
        
        This may not be possible on all OSs, so the function is not guaranteed to succeed.
        """
        pass

    def RegisterShortcut(self, shortcut: str, widget: QWidget, callback: ShortcutCallback): # real signature unknown; restored from __doc__
        """
        RegisterShortcut(shortcut, widget, callback)
        
        Register a callback for a particular key shortcut.
        
        This creates a managed shortcut. Qt's shortcut system doesn't allow specialisation/duplication, so
        you can't use ``Ctrl+S`` for a shortcut in a window to update some changes if there's also a global
        ``Ctrl+S`` shortcut on the window. In the end, neither shortcut will be called.
        
        Instead this function allows the main window to manage shortcuts internally, and it will pick the
        closest shortcut to a given action. The search goes from the widget with the focus currently up the
        chain of parents, with the first match being used. If no matches are found, then a 'global' default
        will be invoked, if it exists.
        
        :param str shortcut: The text string representing the shortcut, e.g. 'Ctrl+S'.
        :param QWidget widget: A handle to the widget to use as the context for this shortcut, or ``None``
          for a global shortcut. Note that if an existing global shortcut exists the new one will not be
          registered.
        :param ShortcutCallback callback: The function to callback when the shortcut is hit.
          Callback function signature must match :func:`ShortcutCallback`.
        """
        pass

    def UnregisterShortcut(self, shortcut: str, widget: QWidget): # real signature unknown; restored from __doc__
        """
        UnregisterShortcut(shortcut, widget)
        
        Unregister a callback for a particular key shortcut, made in a previous call to
        :meth:`RegisterShortcut`.
        
        See the documentation for :meth:`RegisterShortcut` for what these shortcuts are for.
        
        :param str shortcut: The text string representing the shortcut, e.g. 'Ctrl+S'. To unregister all
          shortcuts for a particular widget, you can pass an empty string here. In this case,
          :paramref:`UnregisterShortcut.widget` must not be ``None``.
        :param QWidget widget: A handle to the widget used as the context for the shortcut, or ``None``
          if referring to a global shortcut.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`MainWindow` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50134800>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.MainWindow' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.MainWindow' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.MainWindow' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.MainWindow' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.MainWindow' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.MainWindow' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.MainWindow' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.MainWindow' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.MainWindow' objects>, 'RegisterShortcut': <method 'RegisterShortcut' of 'qrenderdoc.MainWindow' objects>, 'UnregisterShortcut': <method 'UnregisterShortcut' of 'qrenderdoc.MainWindow' objects>, 'BringToFront': <method 'BringToFront' of 'qrenderdoc.MainWindow' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.MainWindow' objects>, '__doc__': '\\nThe main parent window of the application.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetMainWindow`.\\n\\n.. function:: ShortcutCallback(QWidget focusWidget)\\n\\n  Not a member function - the signature for any ``ShortcutCallback`` callbacks.\\n\\n  :param QWidget focusWidget: The widget with focus at the time this shortcut was detected. May be\\n     ``None``.\\n\\n'})"


