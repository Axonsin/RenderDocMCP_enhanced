from ._BugReport import BugReport
from ._OffsetSizeDisplayMode import OffsetSizeDisplayMode
from ._RemoteHost import RemoteHost
from ._ShaderProcessingTool import ShaderProcessingTool
from ._TimeUnit import TimeUnit
from datetime import datetime
from renderdoc import ReplayOptions
from typing import List

from typing import overload

class PersistentConfig():
    # Original docstring
    """
    A persistent config file that is automatically loaded and saved, which contains any
    settings and information that needs to be preserved from one run to the next.
    
    The config is retrieved by calling :meth:`CaptureContext.Config`.
    
    For more information about some of these settings that are user-facing see
    :ref:`the documentation for the settings window <settings-window>`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PersistentConfig.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def GetRemoteHosts(self) -> List[RemoteHost]:
        """
        Returns a list of all remote hosts.
        
        :return: The remote host list
        :rtype: List[RemoteHost]
        """
        pass
    
    
    def GetRemoteHost(self, hostname: str) -> RemoteHost:
        """
        Look up a remote host by hostname.
        
        :param str hostname: The hostname to look up
        :return: The remote host for the given hostname, or an invalid ``RemoteHost`` if no such exists.
        :rtype: RemoteHost
        """
        pass
    
    
    def AddRemoteHost(self, host: RemoteHost):
        """
        Adds a new remote host.
        
        :param RemoteHost host: The remote host to add.
        """
        pass
    
    
    def RemoveRemoteHost(self, host: RemoteHost):
        """
        Removes an existing remote host.
        
        :param RemoteHost host: The remote host to remove.
        """
        pass
    
    
    def UpdateEnumeratedProtocolDevices(self):
        """
        If configured, queries available device protocols to update auto-configured hosts.
        """
        pass
    
    
    def Load(self, filename: str) -> bool:
        """
        Loads the config from a given filename. This happens automatically on startup, so it's
        not recommended that you call this function manually.
        
        :param str filename: The filename to load from
        :return: A boolean status if the load was successful.
        :rtype: bool
        """
        pass
    
    
    def Save(self) -> bool:
        """
        Saves the config to disk. This can happen if you want to be sure a setting has been
        propagated and will not be forgotten in the case of crash or otherwise unexpected exit.
        
        :return: A boolean status if the save was successful.
        :rtype: bool
        """
        pass
    
    
    def Close(self):
        """
        Closes the config file so that subsequent calls to Save() will not write to disk at
        the file the config was loaded from.
        
        This function is rarely directly used, except in the case where RenderDoc is relaunching itself and
        wants to avoid file locking conflicts between the closing instance saving, and the loading instance
        loading. It can explicitly save and close before relaunching.
        """
        pass
    
    
    def SetupFormatting(self):
        """
        Configures the internal number formatter class with the settings from this config.
        """
        pass
    
    
    def SetStyle(self) -> bool:
        """
        Sets the UI style to the value in :data:`UIStyle`.
        
        Changing the style after the application has started may not properly update everything, so to be
        sure the new style is applied, the application should be restarted.
        
        :return: ``True`` if the style was set successfully, ``False`` if there was a problem e.g. the value
          of :data:`UIStyle` was unrecognised or empty.
        :rtype: bool
        """
        pass
    
    @property
    def UnsupportedAndroid_LastUpdate(self) -> datetime:
        """
        A date containing the last time that the user was warned about an Android device being older than is generally supported. This prevents the user being spammed if they consistently use an old Android device. If it has been more than 3 weeks since the last time an old device was seen, we re-warn the user, but if it's less than 3 weeks we silently update this date so continuous use doesn't nag.:type: datetime
        """
        pass
    
    @UnsupportedAndroid_LastUpdate.setter
    def UnsupportedAndroid_LastUpdate(self, value: datetime):
        pass
    
    @property
    def CheckUpdate_AllowChecks(self) -> bool:
        """
        ``True`` if the UI should be allowed to make update checks remotely to see if a new version is available.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @CheckUpdate_AllowChecks.setter
    def CheckUpdate_AllowChecks(self, value: bool):
        pass
    
    @property
    def CheckUpdate_LastUpdate(self) -> datetime:
        """
        A date containing the last time that update checks happened.:type: datetime
        """
        pass
    
    @CheckUpdate_LastUpdate.setter
    def CheckUpdate_LastUpdate(self, value: datetime):
        pass
    
    @property
    def DegradedCapture_LastUpdate(self) -> datetime:
        """
        A date containing the last time that the user was warned about captures being loaded in degraded support. This prevents the user being spammed if their hardware is low spec.:type: datetime
        """
        pass
    
    @DegradedCapture_LastUpdate.setter
    def DegradedCapture_LastUpdate(self, value: datetime):
        pass
    
    @property
    def Python_DebugEnabled(self) -> bool:
        """
        ``True`` if debugging should be enabled at startup for python, including UI extensions and scripts in the python shell.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @Python_DebugEnabled.setter
    def Python_DebugEnabled(self, value: bool):
        pass
    
    @property
    def CrashReport_EmailAddress(self) -> str:
        """
        The saved email address for pre-filling out in crash reports.:type: str
        """
        pass
    
    @CrashReport_EmailAddress.setter
    def CrashReport_EmailAddress(self, value: str):
        pass
    
    @property
    def MeshViewer_KeySettings(self) -> List[int]:
        """
        List of Qt keycodes for mesh viewer key bindings. Can be empty if no keys are configured which will revert to default behaviour of physical WASD (independent of local keyboard layout).
        Defaults to an empty list.:type: List[int]
        """
        pass
    
    @MeshViewer_KeySettings.setter
    def MeshViewer_KeySettings(self, value: List[int]):
        pass
    
    @property
    def RecentCaptureSettings(self) -> List[str]:
        """
        The recently opened capture settings files.
        
        :type: List[str]
        """
        pass
    
    @RecentCaptureSettings.setter
    def RecentCaptureSettings(self, value: List[str]):
        pass
    
    @property
    def TextureViewer_PerTexSettings(self) -> bool:
        """
        ``True`` if the :class:`TextureViewer` should store most visualisation settings on a per-texture basis instead of keeping it persistent across different textures.
        
        :Defaults to ``True``.:type: bool
        """
        pass
    
    @TextureViewer_PerTexSettings.setter
    def TextureViewer_PerTexSettings(self, value: bool):
        pass
    
    @property
    def ExternalTool_RadeonGPUProfiler(self) -> str:
        """
        The path to the executable of the external Radeon GPU Profiler tool.:type: str
        """
        pass
    
    @ExternalTool_RadeonGPUProfiler.setter
    def ExternalTool_RadeonGPUProfiler(self, value: str):
        pass
    
    @property
    def CheckUpdate_CurrentVersion(self) -> str:
        """
        The current version at the time of update checks. Used to determine if a cached pending update is no longer valid because we got updated through some other method.:type: str
        """
        pass
    
    @CheckUpdate_CurrentVersion.setter
    def CheckUpdate_CurrentVersion(self, value: str):
        pass
    
    @property
    def RecentCaptureFiles(self) -> List[str]:
        """
        The recently opened capture files.
        
        :type: List[str]
        """
        pass
    
    @RecentCaptureFiles.setter
    def RecentCaptureFiles(self, value: List[str]):
        pass
    
    @property
    def AllowProcessInject(self) -> bool:
        """
        ``True`` if process injection is enabled. Since it can often break and is almost always not want users want to do. New users can get confused by it being there and go to it first.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @AllowProcessInject.setter
    def AllowProcessInject(self, value: bool):
        pass
    
    @property
    def Python_DebugPyDir(self) -> str:
        """
        The path to an copy of the ``debugpy`` module which should be loaded for debugging.:type: str
        """
        pass
    
    @Python_DebugPyDir.setter
    def Python_DebugPyDir(self, value: str):
        pass
    
    @property
    def UIStyle(self) -> str:
        """
        The style to load for the UI. Possible values include 'Native', 'RDLight', 'RDDark'. If empty, the closest of RDLight and RDDark will be chosen, based on the overall light-on-dark or dark-on-light theme of the application native style.:type: str
        """
        pass
    
    @UIStyle.setter
    def UIStyle(self, value: str):
        pass
    
    @property
    def EventBrowser_TimeUnit(self) -> TimeUnit:
        """
        The :class:`TimeUnit` to use to display the duration column in the :class:`EventBrowser`.
        
        Defaults to microseconds.:type: TimeUnit
        """
        pass
    
    @EventBrowser_TimeUnit.setter
    def EventBrowser_TimeUnit(self, value: TimeUnit):
        pass
    
    @property
    def LastCapturePath(self) -> str:
        """
        The path containing the last executable that was captured, which is useful as a default location for browsing.:type: str
        """
        pass
    
    @LastCapturePath.setter
    def LastCapturePath(self, value: str):
        pass
    
    @property
    def Python_RecentFiles(self) -> List[str]:
        """
        List of files recently opened in the python scripting window.
        
        :type: List[str]
        """
        pass
    
    @Python_RecentFiles.setter
    def Python_RecentFiles(self, value: List[str]):
        pass
    
    @property
    def LastCaptureExe(self) -> str:
        """
        The filename of the last executable that was captured, inside :data:`LastCapturePath`.:type: str
        """
        pass
    
    @LastCaptureExe.setter
    def LastCaptureExe(self, value: str):
        pass
    
    @property
    def Formatter_MinFigures(self) -> int:
        """
        The minimum number of decimal places to show in formatted floating point values.
        
        .. note::
          The naming of 'MinFigures' is a historical artifact - this controls the number of   decimal places only, not the number of significant figures.
        
        Defaults to ``2``.:type: int
        """
        pass
    
    @Formatter_MinFigures.setter
    def Formatter_MinFigures(self, value: int):
        pass
    
    @property
    def Formatter_MaxFigures(self) -> int:
        """
        The maximum number of decimal places to show in formatted floating point values.
        
        .. note::
          The naming of 'MaxFigures' is a historical artifact - this controls the number of   decimal places only, not the number of significant figures.
        
        Defaults to ``5``.:type: int
        """
        pass
    
    @Formatter_MaxFigures.setter
    def Formatter_MaxFigures(self, value: int):
        pass
    
    @property
    def TemporaryCaptureDirectory(self) -> str:
        """
        The path to where temporary capture files should be stored until they're saved permanently.:type: str
        """
        pass
    
    @TemporaryCaptureDirectory.setter
    def TemporaryCaptureDirectory(self, value: str):
        pass
    
    @property
    def DefaultCaptureSaveDirectory(self) -> str:
        """
        The default path to save captures in, when browsing to save a temporary capture somewhere.:type: str
        """
        pass
    
    @DefaultCaptureSaveDirectory.setter
    def DefaultCaptureSaveDirectory(self, value: str):
        pass
    
    @property
    def CrashReport_ShouldRememberEmail(self) -> bool:
        """
        ``True`` if the email address entered in the crash reporter should be remembered for next time. If no email is entered then nothing happens (any previous saved email is kept).
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @CrashReport_ShouldRememberEmail.setter
    def CrashReport_ShouldRememberEmail(self, value: bool):
        pass
    
    @property
    def Comments_ShowOnLoad(self) -> bool:
        """
        ``True`` if when loading a new capture that contains a comments section, the comment viewer will be opened and focussed.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Comments_ShowOnLoad.setter
    def Comments_ShowOnLoad(self, value: bool):
        pass
    
    @property
    def TextureViewer_ResetRange(self) -> bool:
        """
        ``True`` if the :class:`TextureViewer` should reset the visible range when a new texture is selected.
        
        :Defaults to ``False``.:type: bool
        """
        pass
    
    @TextureViewer_ResetRange.setter
    def TextureViewer_ResetRange(self, value: bool):
        pass
    
    @property
    def Formatter_NegExp(self) -> int:
        """
        The cut-off on negative exponents of a normalised values to display using scientific notation.
        
        E.g. for a value of 5, anything below 1.0e-5 will be displayed using scientific notation.
        
        Defaults to ``5``.:type: int
        """
        pass
    
    @Formatter_NegExp.setter
    def Formatter_NegExp(self, value: int):
        pass
    
    @property
    def Font_PreferMonospaced(self) -> bool:
        """
        ``True`` if a monospaced font should be used in all places where data is displayed, even if the data is not tabular such as names.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Font_PreferMonospaced.setter
    def Font_PreferMonospaced(self, value: bool):
        pass
    
    @property
    def Font_Family(self) -> str:
        """
        The font family to use in the UI.
        
        Defaults to an empty string which means to use the system default.:type: str
        """
        pass
    
    @Font_Family.setter
    def Font_Family(self, value: str):
        pass
    
    @property
    def Font_MonoFamily(self) -> str:
        """
        The monospaced font family to use in the UI.
        
        Defaults to an empty string which means to use the system default.:type: str
        """
        pass
    
    @Font_MonoFamily.setter
    def Font_MonoFamily(self, value: str):
        pass
    
    @property
    def ResourceUsage_SplitByMarker(self) -> bool:
        """
        ``False`` if :class:`~renderdoc.ResourceUsage` should combine resource usage across marker boundaries.
        
        :Defaults to ``False``.:type: bool
        """
        pass
    
    @ResourceUsage_SplitByMarker.setter
    def ResourceUsage_SplitByMarker(self, value: bool):
        pass
    
    @property
    def ShaderProcessors(self) -> List[ShaderProcessingTool]:
        """
        A list of :class:`ShaderProcessingTool` detailing shader processing programs. The list comes in priority order, with earlier processors preferred over later ones.
        
        :type: List[ShaderProcessingTool]
        """
        pass
    
    @ShaderProcessors.setter
    def ShaderProcessors(self, value: List[ShaderProcessingTool]):
        pass
    
    @property
    def CrashReport_ReportedBugs(self) -> List[BugReport]:
        """
        A list of :class:`BugReport` detailing previously submitted bugs that we're watching for updates.
        
        :type: List[BugReport]
        """
        pass
    
    @CrashReport_ReportedBugs.setter
    def CrashReport_ReportedBugs(self, value: List[BugReport]):
        pass
    
    @property
    def MeshViewer_SpeedModifier(self) -> int:
        """
        The Qt modifier code for the mesh viewer 'speed' modifier.
        Defaults to ``-1`` which means Shift.:type: int
        """
        pass
    
    @MeshViewer_SpeedModifier.setter
    def MeshViewer_SpeedModifier(self, value: int):
        pass
    
    @property
    def TextureViewer_ShaderDirs(self) -> List[str]:
        """
        List of the directories containing custom shader files for the Texture Viewer.
        
        :type: List[str]
        """
        pass
    
    @TextureViewer_ShaderDirs.setter
    def TextureViewer_ShaderDirs(self, value: List[str]):
        pass
    
    @property
    def DefaultReplayOptions(self) -> ReplayOptions:
        """
        A :class:`~renderdoc.ReplayOptions` containing the configured default replay options to use in most scenarios when no specific options are given.
        
        :type: renderdoc.ReplayOptions
        """
        pass
    
    @DefaultReplayOptions.setter
    def DefaultReplayOptions(self, value: ReplayOptions):
        pass
    
    @property
    def AlwaysReplayLocally(self) -> bool:
        """
        ``True`` if when loading a capture that was originally captured on a remote device but uses an API that can be supported locally, should be loaded locally without prompting to switch to a remote context.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @AlwaysReplayLocally.setter
    def AlwaysReplayLocally(self, value: bool):
        pass
    
    @property
    def Python_VSCodePath(self) -> str:
        """
        The path to the VSCode ``code`` command line executable to use.:type: str
        """
        pass
    
    @Python_VSCodePath.setter
    def Python_VSCodePath(self, value: str):
        pass
    
    @property
    def Analytics_ManualCheck(self) -> bool:
        """
        ``True`` if the user has remained with analytics turned on, but has chosen to manually check each report that is sent out.
        collection and reporting.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Analytics_ManualCheck.setter
    def Analytics_ManualCheck(self, value: bool):
        pass
    
    @property
    def AlwaysLoad_Extensions(self) -> List[str]:
        """
        A list of strings with extension packages to always load on startup, without needing manual enabling.
        
        :type: List[str]
        """
        pass
    
    @AlwaysLoad_Extensions.setter
    def AlwaysLoad_Extensions(self, value: List[str]):
        pass
    
    @property
    def EventBrowser_AddFake(self) -> bool:
        """
        ``True`` if fake action marker regions should be added to captures that don't have any markers, for easier browsing. The regions are identified by grouping actions that write to the same targets together.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @EventBrowser_AddFake.setter
    def EventBrowser_AddFake(self, value: bool):
        pass
    
    @property
    def TextureViewer_PerTexYFlip(self) -> bool:
        """
        ``True`` if the :class:`TextureViewer` should treat y-flipping as a per-texture state rather than a global toggle.
        
        Does nothing if per-texture settings are disabled in general.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @TextureViewer_PerTexYFlip.setter
    def TextureViewer_PerTexYFlip(self, value: bool):
        pass
    
    @property
    def CheckUpdate_UpdateResponse(self) -> str:
        """
        Contains the response from the update server from the last update check, with any release notes for the new version.:type: str
        """
        pass
    
    @CheckUpdate_UpdateResponse.setter
    def CheckUpdate_UpdateResponse(self, value: str):
        pass
    
    @property
    def LocalProxyAPI(self) -> int:
        """
        The index of the local proxy API to use when using remote context replay. ``-1`` if the default proxy should be used.
        
        Defaults to ``-1``.:type: int
        """
        pass
    
    @LocalProxyAPI.setter
    def LocalProxyAPI(self, value: int):
        pass
    
    @property
    def Font_GlobalScale(self) -> float:
        """
        The global scale to apply to fonts in the application, expressed as a float.
        
        Defaults to ``1.0`` which means 100%.:type: float
        """
        pass
    
    @Font_GlobalScale.setter
    def Font_GlobalScale(self, value: float):
        pass
    
    @property
    def LastFileBrowsePath(self) -> str:
        """
        The path to the last file browsed to in any dialog. Used as a default location for all file browsers without another explicit default directory (such as opening capture files - see :data:`LastCaptureFilePath`).:type: str
        """
        pass
    
    @LastFileBrowsePath.setter
    def LastFileBrowsePath(self, value: str):
        pass
    
    @property
    def EventBrowser_ApplyColors(self) -> bool:
        """
        ``True`` if the :class:`EventBrowser` should apply any colors specified with API marker regions.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @EventBrowser_ApplyColors.setter
    def EventBrowser_ApplyColors(self, value: bool):
        pass
    
    @property
    def CrashReport_EmailNagged(self) -> bool:
        """
        ``True`` if the user has been prompted to enter their email address on a crash report. This really helps find fixes for bugs, so we prompt the user once only if they didn't enter an email. Once the prompt has happened, regardless of the answer this is set to true and remains there forever.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @CrashReport_EmailNagged.setter
    def CrashReport_EmailNagged(self, value: bool):
        pass
    
    @property
    def Python_LaunchVSCode(self) -> bool:
        """
        ``True`` if a new instance of VS Code should be launched when debugging a python script or UI extension.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @Python_LaunchVSCode.setter
    def Python_LaunchVSCode(self, value: bool):
        pass
    
    @property
    def BufferFormatter_SavedFormats(self) -> List[str]:
        """
        A list of strings with saved formats for the buffer formatter. The first line is the name and the rest of the contents are the formats.
        
        :type: List[str]
        """
        pass
    
    @BufferFormatter_SavedFormats.setter
    def BufferFormatter_SavedFormats(self, value: List[str]):
        pass
    
    @property
    def AllowGlobalHook(self) -> bool:
        """
        ``True`` if global hooking is enabled. Since it has potentially problematic side-effects and is dangerous, it requires explicit opt-in.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @AllowGlobalHook.setter
    def AllowGlobalHook(self, value: bool):
        pass
    
    @property
    def Analytics_TotalOptOut(self) -> bool:
        """
        ``True`` if the user has selected to completely opt-out from and disable all analytics collection and reporting.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Analytics_TotalOptOut.setter
    def Analytics_TotalOptOut(self, value: bool):
        pass
    
    @property
    def EventBrowser_ColorEventRow(self) -> bool:
        """
        ``True`` if when coloring marker regions in the :class:`EventBrowser`, the whole row should be colored instead of just a side-bar.
        
        Defaults to ``True``.:type: bool
        """
        pass
    
    @EventBrowser_ColorEventRow.setter
    def EventBrowser_ColorEventRow(self, value: bool):
        pass
    
    @property
    def Formatter_OffsetSizeDisplayMode(self) -> OffsetSizeDisplayMode:
        """
        The formatting mode to use for values marked as Offsets or Sizes.
        
        E.g. Auto: decimal by default and hexadecimal if above a certain threshold, Decimal: always use decimal, Hexadecimal: always use hexadecimal.
        Defaults to ``Auto``.:type: OffsetSizeDisplayMode
        """
        pass
    
    @Formatter_OffsetSizeDisplayMode.setter
    def Formatter_OffsetSizeDisplayMode(self, value: OffsetSizeDisplayMode):
        pass
    
    @property
    def CheckUpdate_UpdateAvailable(self) -> bool:
        """
        ``True`` if an update to a newer version is currently available.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @CheckUpdate_UpdateAvailable.setter
    def CheckUpdate_UpdateAvailable(self, value: bool):
        pass
    
    @property
    def Python_PromptReloadUnchanged(self) -> bool:
        """
        ``True`` if there should be a prompt when reloading script file changes from disk, even if the script has not been changed in the editor. Otherwise changes are reloaded silently.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Python_PromptReloadUnchanged.setter
    def Python_PromptReloadUnchanged(self, value: bool):
        pass
    
    @property
    def Formatter_PosExp(self) -> int:
        """
        The cut-off on positive exponents of a normalised values to display using scientific notation.
        
        E.g. for a value of 7, anything below 1.0e+7 will be displayed using scientific notation.
        
        Defaults to ``7``.:type: int
        """
        pass
    
    @Formatter_PosExp.setter
    def Formatter_PosExp(self, value: int):
        pass
    
    @property
    def Tips_HasSeenFirst(self) -> bool:
        """
        ``True`` if the user has seen the first tip, which should always be shown first before randomising.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Tips_HasSeenFirst.setter
    def Tips_HasSeenFirst(self, value: bool):
        pass
    
    @property
    def CrashReport_LastOpenedCapture(self) -> str:
        """
        The last opened capture, to send if any crash is encountered. This is different to the most recent opened file, because it's set before any processing happens (recent files are only added to the list when they successfully open), and it's cleared again when the capture is closed.:type: str
        """
        pass
    
    @CrashReport_LastOpenedCapture.setter
    def CrashReport_LastOpenedCapture(self, value: str):
        pass
    
    @property
    def MeshViewer_CameraNear(self) -> float:
        """
        The near plane used in the mesh viewers display.
        Defaults to ``0.1``.:type: float
        """
        pass
    
    @MeshViewer_CameraNear.setter
    def MeshViewer_CameraNear(self, value: float):
        pass
    
    @property
    def MeshViewer_CameraFar(self) -> float:
        """
        The far plane used in the mesh viewers display.
        Defaults to ``100000.0``.:type: float
        """
        pass
    
    @MeshViewer_CameraFar.setter
    def MeshViewer_CameraFar(self, value: float):
        pass
    
    @property
    def Python_StubDirs(self) -> List[str]:
        """
        List of extra directories to write python stubs into.
        
        :type: List[str]
        """
        pass
    
    @Python_StubDirs.setter
    def Python_StubDirs(self, value: List[str]):
        pass
    
    @property
    def LastCaptureFilePath(self) -> str:
        """
        The path to the last capture to be opened, which is useful as a default location for browsing.:type: str
        """
        pass
    
    @LastCaptureFilePath.setter
    def LastCaptureFilePath(self, value: str):
        pass
    
    @property
    def Annotations_HasAutoShown(self) -> bool:
        """
        ``True`` if the user has had the annotation viewer displayed when hidden upon loading a capture that contains annotations. After this is set to true, we won't auto-show the
        annotation viewer automatically.
        
        Defaults to ``False``.:type: bool
        """
        pass
    
    @Annotations_HasAutoShown.setter
    def Annotations_HasAutoShown(self, value: bool):
        pass
    
