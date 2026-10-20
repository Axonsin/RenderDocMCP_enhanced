
# Dummy types
from . import QWidget

class PythonShell():
    # Original docstring
    """
    The interactive python shell.
    
    This window is retrieved by calling :meth:`CaptureContext.GetPythonShell`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`PythonShell` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def CheckUnsavedChanges(self) -> bool:
        """
        Checks if there are unsaved changes to python scripts, and prompts the user about whether to
        discard them or not.
        
        If it is OK to close the window (either because there are no unsaved changes, they were saved after a prompt,
        or the user chose to discard them then this function returns ``True``.
        
        :return: Whether or not it is OK to close without losing changes.
        :rtype: bool
        """
        pass
    
    
    def LoadScriptFromFilename(self, filename: str) -> bool:
        """
        Loads the given file and creates a new tab with the script contents. No tab is
        created if the file fails to load
        
        :param str filename: The filename of the script to load.
        :return: Whether or not the script was successfully loaded.
        :rtype: bool
        """
        pass
    
    
    def CreateNewScriptEditor(self, name: str, text: str):
        """
        Creates a new script editor with a given name and text contents.
        
        :param str name: The name to give the editor, does not have to be a filename.
        :param str text: The contents to start with in the editor, can be blank.
        """
        pass
    
    
    def GetScriptText(self) -> str:
        """
        Returns the text of the currently focussed script editor.
        
        :return: The current script text.
        :rtype: str
        """
        pass
    
    
    def RunScript(self):
        """
        Runs the current script in the python shell.
        """
        pass
    
    
    def AttachDebugger(self, extensionName: str):
        """
        Tries to launch a python debugger to attach to the current process, in the context
        of a given extension.
        
        Returns immediately if a debugger is already connected, or is not supported.
        
        If the extension name is not a loaded extension, no debugger will be launched.
        
        .. note::
          The extension name is only used if a new debugger instance is launched, it will target that
          particular extension's source location. An attached python debugger can debug all python code
          in the instance.
        
        :param str extensionName: The package name of the extension to use as context for launching a
          debugger program.
        """
        pass
    
    
    def SetExtensionOutputFilter(self, extensionName: str):
        """
        Sets the filter on the output panel to only show output from the given extension.
        
        If the extension does not exist or is not loaded, no change will be made to the output filter.
        
        :param str extensionName: The package name of the extension to show output from.
        """
        pass
    
    
    def SetScriptOutputFilter(self):
        """
        Sets the filter on the output panel to only show output from scripts run.
        
        This will hide any output from extensions that are loaded, and only show output that comes from the script
        run from inside the python window.
        """
        pass
    
    
    def RemoveOutputFilter(self):
        """
        Sets the filter on the output panel to show output from all python sources.
        
        This will show output from the running script, as well as any extensions that are loaded.
        """
        pass
    
    
    def ShowOutput(self):
        """
        Raises the output panel.
        
        This will ensure the panel showing the output from running python code is visible.
        """
        pass
    
    
    def ShowREPL(self):
        """
        Raises the REPL panel.
        
        This will ensure the panel with the interactive REPL is visible.
        """
        pass
    
    
    def ShowHelp(self):
        """
        Raises the help panel.
        
        This will ensure the panel showing the help browser is visible.
        """
        pass
    
