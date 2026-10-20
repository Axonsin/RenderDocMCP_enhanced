from ._CaptureConnection import CaptureConnection
from ._CaptureSettings import CaptureSettings
from renderdoc import EnvironmentModification
from typing import List

# Dummy types
from . import QWidget

class CaptureDialog():
    # Original docstring
    """
    The executable capture window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetCaptureDialog`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`CaptureDialog` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def IsInjectMode(self) -> bool:
        """
        Determines if the window is in inject or launch mode.
        
        :return: ``True`` if the window is set up for injecting.
        :rtype: bool
        """
        pass
    
    
    def SetInjectMode(self, inject: bool):
        """
        Switches the window to or from inject mode.
        
        :param bool inject: ``True`` if the window should configure for injecting into processes.
        """
        pass
    
    
    def SetExecutableFilename(self, filename: str):
        """
        Sets the executable filename to capture.
        
        :param str filename: The filename to execute.
        """
        pass
    
    
    def SetWorkingDirectory(self, dir: str):
        """
        Sets the working directory for capture.
        
        :param str dir: The directory to use.
        """
        pass
    
    
    def SetCommandLine(self, cmd: str):
        """
        Sets the command line string to use when launching an executable.
        
        :param str cmd: The command line to use.
        """
        pass
    
    
    def SetEnvironmentModifications(self, modifications: List[EnvironmentModification]):
        """
        Sets the list of environment modifications to apply when launching.
        
        :param List[renderdoc.EnvironmentModification] modifications: The list of modifications to apply.
        """
        pass
    
    
    def SetSettings(self, settings: CaptureSettings):
        """
        Configures the window based on a bulk structure of settings.
        
        :param CaptureSettings settings: The settings to apply.
        """
        pass
    
    
    def Settings(self) -> CaptureSettings:
        """
        Retrieves the current state of the window as a structure of settings.
        
        :return: The settings describing the current window state.
        :rtype: CaptureSettings
        """
        pass
    
    
    def Launch(self) -> CaptureConnection:
        """
        Launches a capture of the current executable.
        
        :return: The connection window if successful, or ``None`` if no connection was made.
        :rtype: CaptureConnection
        """
        pass
    
    
    def LoadSettings(self, filename: str):
        """
        Loads settings from a file and applies them. See :meth:`SetSettings`.
        
        :param str filename: The filename to load the settings from.
        """
        pass
    
    
    def SaveSettings(self, filename: str):
        """
        Saves the current settings to a file. See :meth:`Settings`.
        
        :param str filename: The filename to save the settings to.
        """
        pass
    
    
    def UpdateGlobalHook(self):
        """
        Update the current state of the global hook, e.g. if it has been enabled.
        """
        pass
    
    
    def UpdateRemoteHost(self):
        """
        Update the current state based on the current remote host, when that changes.
        """
        pass
    
