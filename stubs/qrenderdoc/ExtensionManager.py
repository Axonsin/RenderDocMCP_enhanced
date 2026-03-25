# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ExtensionMetadata import ExtensionMetadata
from .MiniQtHelper import MiniQtHelper
from .DialogButton import DialogButton
from .ContextMenu import ContextMenu
from .PanelMenu import PanelMenu
from .WindowMenu import WindowMenu

class ExtensionManager(): # skipped bases: <class 'SwigPyObject'>
    """
    A manager for listing available and active extensions, as well as the interface for
    extensions to register hooks and additional functionality.
    
    This manager is retrieved by calling :meth:`CaptureContext.Extensions`.
    
    .. function:: ExtensionCallback(context, data)
    
      Not a member function - the signature for any ``ExtensionCallback`` callbacks.
    
      Callback for extensions to register entry points with, used in many situations depending on how it
      was registered.
    
      :param CaptureContext context: The current capture context.
      :param dict data: Additional data for the call, as a dictionary with string keys.
        Context-dependent based on what generated the callback
    """
    def ErrorDialog(self, text: str, title: str): # real signature unknown; restored from __doc__
        """
        ErrorDialog(text, title)
        ErrorDialog(text)
        
        Display an error message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param str title: The dialog title, optional.
        """
        pass

    def GetInstalledExtensions(self) -> List[ExtensionMetadata]: # real signature unknown; restored from __doc__
        """
        GetInstalledExtensions()
        
        Retrieve a list of installed extensions.
        
        :return: The list of installed extensions.
        :rtype: List[ExtensionMetadata]
        """
        pass

    def GetMiniQtHelper(self) -> MiniQtHelper: # real signature unknown; restored from __doc__
        """
        GetMiniQtHelper()
        
        Returns a handle to the mini Qt helper. See :class:`MiniQtHelper`.
        
        :return: The helper interface.
        :rtype: MiniQtHelper
        """
        pass

    def IsExtensionLoaded(self, name: str) -> bool: # real signature unknown; restored from __doc__
        """
        IsExtensionLoaded(name)
        
        Check if an installed extension is enabled.
        
        :param str name: The qualified name of the extension, e.g. ``foo.bar``
        :return: If the extension is enabled or not.
        :rtype: bool
        """
        pass

    def LoadExtension(self, name: str) -> str: # real signature unknown; restored from __doc__
        """
        LoadExtension(name)
        
        Enable an extension by name. If the extension is already enabled, this will reload it.
        
        :param str name: The qualified name of the extension, e.g. ``foo.bar``
        :return: If the extension loaded successfully, an empty string, otherwise the errors encountered
          while loading it.
        :rtype: str
        """
        pass

    def MessageDialog(self, text: str, title: str): # real signature unknown; restored from __doc__
        """
        MessageDialog(text, title)
        MessageDialog(text)
        
        Display a simple informational message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param str title: The dialog title, optional.
        """
        pass

    def OpenDirectoryName(self, caption: str, dir: str) -> str: # real signature unknown; restored from __doc__
        """
        OpenDirectoryName(caption, dir)
        OpenDirectoryName(caption)
        OpenDirectoryName()
        
        Browse for a directory to open.
        
        :param str caption: The dialog title, optional.
        :param str dir: The starting directory for browsing, optional.
        :return: The directory selected, or an empty string if nothing was selected.
        :rtype: str
        """
        pass

    def OpenFileName(self, caption: str, dir: str, filter: str) -> str: # real signature unknown; restored from __doc__
        """
        OpenFileName(caption, dir, filter)
        OpenFileName(caption, dir)
        OpenFileName(caption)
        OpenFileName()
        
        Browse for a filename to open.
        
        :param str caption: The dialog title, optional.
        :param str dir: The starting directory for browsing, optional.
        :param str filter: The filter to apply for filenames, optional.
        :return: The filename selected, or an empty string if nothing was selected.
        :rtype: str
        """
        pass

    def QuestionDialog(self, text: str, options: List[DialogButton], title: str) -> DialogButton: # real signature unknown; restored from __doc__
        """
        QuestionDialog(text, options, title)
        QuestionDialog(text, options)
        
        Display an error message dialog.
        
        :param str text: The text of the dialog itself, required.
        :param List[DialogButton] options: The buttons to display on the dialog.
        :param str title: The dialog title, optional.
        :return: The button that was clicked on.
        :rtype: DialogButton
        """
        pass

    def RegisterContextMenu(self, base: ContextMenu, submenus: List[str], callback: ExtensionCallback): # real signature unknown; restored from __doc__
        """
        RegisterContextMenu(base, submenus, callback)
        
        Register a context menu item in a panel for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param ContextMenu base: The panel to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry.
        :param ExtensionCallback callback: The function to callback when the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass

    def RegisterPanelMenu(self, base: PanelMenu, submenus: List[str], callback: ExtensionCallback): # real signature unknown; restored from __doc__
        """
        RegisterPanelMenu(base, submenus, callback)
        
        Register a menu item in a panel for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param PanelMenu base: The panel to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry.
        :param ExtensionCallback callback: The function to callback when the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass

    def RegisterWindowMenu(self, base: WindowMenu, submenus: List[str], callback: ExtensionCallback): # real signature unknown; restored from __doc__
        """
        RegisterWindowMenu(base, submenus, callback)
        
        Register a new menu item in the main window's menus for an extension.
        
        .. note:
          The intermediate submenu items will be created as needed, there's no need to register each item
          in the hierarchy. Registering a menu item and then registering a child is undefined, and the item
          with a child may not receive callbacks at the correct times.
        
        :param WindowMenu base: The base menu to add the item to.
        :param List[str] submenus: A list of strings containing the submenus to add before the item. The
          last string will be the name of the menu item itself. Must contain at least one entry, or two
          entries if ``base`` is :data:`WindowMenu.NewMenu`.
        :param ExtensionCallback callback: The function to callback when the menu item is selected.
          Callback function signature must match :func:`ExtensionCallback`.
        """
        pass

    def SaveFileName(self, caption: str, dir: str, filter: str) -> str: # real signature unknown; restored from __doc__
        """
        SaveFileName(caption, dir, filter)
        SaveFileName(caption, dir)
        SaveFileName(caption)
        SaveFileName()
        
        Browse for a filename to save to.
        
        :param str caption: The dialog title, optional.
        :param str dir: The starting directory for browsing, optional.
        :param str filter: The filter to apply for filenames, optional.
        :return: The filename selected, or an empty string if nothing was selected.
        :rtype: str
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50131BC0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ExtensionManager' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ExtensionManager' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ExtensionManager' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ExtensionManager' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ExtensionManager' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ExtensionManager' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ExtensionManager' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ExtensionManager' objects>, 'GetInstalledExtensions': <method 'GetInstalledExtensions' of 'qrenderdoc.ExtensionManager' objects>, 'IsExtensionLoaded': <method 'IsExtensionLoaded' of 'qrenderdoc.ExtensionManager' objects>, 'LoadExtension': <method 'LoadExtension' of 'qrenderdoc.ExtensionManager' objects>, 'RegisterWindowMenu': <method 'RegisterWindowMenu' of 'qrenderdoc.ExtensionManager' objects>, 'RegisterPanelMenu': <method 'RegisterPanelMenu' of 'qrenderdoc.ExtensionManager' objects>, 'RegisterContextMenu': <method 'RegisterContextMenu' of 'qrenderdoc.ExtensionManager' objects>, 'GetMiniQtHelper': <method 'GetMiniQtHelper' of 'qrenderdoc.ExtensionManager' objects>, 'MessageDialog': <method 'MessageDialog' of 'qrenderdoc.ExtensionManager' objects>, 'ErrorDialog': <method 'ErrorDialog' of 'qrenderdoc.ExtensionManager' objects>, 'QuestionDialog': <method 'QuestionDialog' of 'qrenderdoc.ExtensionManager' objects>, 'OpenFileName': <method 'OpenFileName' of 'qrenderdoc.ExtensionManager' objects>, 'OpenDirectoryName': <method 'OpenDirectoryName' of 'qrenderdoc.ExtensionManager' objects>, 'SaveFileName': <method 'SaveFileName' of 'qrenderdoc.ExtensionManager' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ExtensionManager' objects>, '__doc__': '\\nA manager for listing available and active extensions, as well as the interface for\\nextensions to register hooks and additional functionality.\\n\\nThis manager is retrieved by calling :meth:`CaptureContext.Extensions`.\\n\\n.. function:: ExtensionCallback(context, data)\\n\\n  Not a member function - the signature for any ``ExtensionCallback`` callbacks.\\n\\n  Callback for extensions to register entry points with, used in many situations depending on how it\\n  was registered.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param dict data: Additional data for the call, as a dictionary with string keys.\\n    Context-dependent based on what generated the callback\\n\\n'})"


