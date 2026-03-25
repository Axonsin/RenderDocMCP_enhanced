# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CaptureSettings import CaptureSettings

from renderdoc.EnvironmentModification import EnvironmentModification

class CaptureDialog(): # skipped bases: <class 'SwigPyObject'>
    """
    The executable capture window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetCaptureDialog`.
    """
    def IsInjectMode(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsInjectMode()
        
        Determines if the window is in inject or launch mode.
        
        :return: ``True`` if the window is set up for injecting.
        :rtype: bool
        """
        pass

    def LoadSettings(self, filename: str): # real signature unknown; restored from __doc__
        """
        LoadSettings(filename)
        
        Loads settings from a file and applies them. See :meth:`SetSettings`.
        
        :param str filename: The filename to load the settings from.
        """
        pass

    def SaveSettings(self, filename: str): # real signature unknown; restored from __doc__
        """
        SaveSettings(filename)
        
        Saves the current settings to a file. See :meth:`Settings`.
        
        :param str filename: The filename to save the settings to.
        """
        pass

    def SetCommandLine(self, cmd: str): # real signature unknown; restored from __doc__
        """
        SetCommandLine(cmd)
        
        Sets the command line string to use when launching an executable.
        
        :param str cmd: The command line to use.
        """
        pass

    def SetEnvironmentModifications(self, modifications: List[EnvironmentModification]): # real signature unknown; restored from __doc__
        """
        SetEnvironmentModifications(modifications)
        
        Sets the list of environment modifications to apply when launching.
        
        :param List[renderdoc.EnvironmentModification] modifications: The list of modifications to apply.
        """
        pass

    def SetExecutableFilename(self, filename: str): # real signature unknown; restored from __doc__
        """
        SetExecutableFilename(filename)
        
        Sets the executable filename to capture.
        
        :param str filename: The filename to execute.
        """
        pass

    def SetInjectMode(self, inject: bool): # real signature unknown; restored from __doc__
        """
        SetInjectMode(inject)
        
        Switches the window to or from inject mode.
        
        :param bool inject: ``True`` if the window should configure for injecting into processes.
        """
        pass

    def SetSettings(self, settings: CaptureSettings): # real signature unknown; restored from __doc__
        """
        SetSettings(settings)
        
        Configures the window based on a bulk structure of settings.
        
        :param CaptureSettings settings: The settings to apply.
        """
        pass

    def Settings(self) -> CaptureSettings: # real signature unknown; restored from __doc__
        """
        Settings()
        
        Retrieves the current state of the window as a structure of settings.
        
        :return: The settings describing the current window state.
        :rtype: CaptureSettings
        """
        pass

    def SetWorkingDirectory(self, dir: str): # real signature unknown; restored from __doc__
        """
        SetWorkingDirectory(dir)
        
        Sets the working directory for capture.
        
        :param str dir: The directory to use.
        """
        pass

    def TriggerCapture(self): # real signature unknown; restored from __doc__
        """
        TriggerCapture()
        
        Launches a capture of the current executable.
        """
        pass

    def UpdateGlobalHook(self): # real signature unknown; restored from __doc__
        """
        UpdateGlobalHook()
        
        Update the current state of the global hook, e.g. if it has been enabled.
        """
        pass

    def UpdateRemoteHost(self): # real signature unknown; restored from __doc__
        """
        UpdateRemoteHost()
        
        Update the current state based on the current remote host, when that changes.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`CaptureDialog` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5013D3D0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.CaptureDialog' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.CaptureDialog' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.CaptureDialog' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.CaptureDialog' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.CaptureDialog' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.CaptureDialog' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.CaptureDialog' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.CaptureDialog' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.CaptureDialog' objects>, 'IsInjectMode': <method 'IsInjectMode' of 'qrenderdoc.CaptureDialog' objects>, 'SetInjectMode': <method 'SetInjectMode' of 'qrenderdoc.CaptureDialog' objects>, 'SetExecutableFilename': <method 'SetExecutableFilename' of 'qrenderdoc.CaptureDialog' objects>, 'SetWorkingDirectory': <method 'SetWorkingDirectory' of 'qrenderdoc.CaptureDialog' objects>, 'SetCommandLine': <method 'SetCommandLine' of 'qrenderdoc.CaptureDialog' objects>, 'SetEnvironmentModifications': <method 'SetEnvironmentModifications' of 'qrenderdoc.CaptureDialog' objects>, 'SetSettings': <method 'SetSettings' of 'qrenderdoc.CaptureDialog' objects>, 'Settings': <method 'Settings' of 'qrenderdoc.CaptureDialog' objects>, 'TriggerCapture': <method 'TriggerCapture' of 'qrenderdoc.CaptureDialog' objects>, 'LoadSettings': <method 'LoadSettings' of 'qrenderdoc.CaptureDialog' objects>, 'SaveSettings': <method 'SaveSettings' of 'qrenderdoc.CaptureDialog' objects>, 'UpdateGlobalHook': <method 'UpdateGlobalHook' of 'qrenderdoc.CaptureDialog' objects>, 'UpdateRemoteHost': <method 'UpdateRemoteHost' of 'qrenderdoc.CaptureDialog' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.CaptureDialog' objects>, '__doc__': '\\nThe executable capture window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetCaptureDialog`.\\n\\n'})"


