
from typing import overload

class CaptureOptions():
    # Original docstring
    """
    Sets up configuration and options for optional features either at capture time or at API
    initialisation time that the user can enable or disable at will.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised CaptureOptions.
        """
        pass
    
    @overload
    def __init__(self, other: 'CaptureOptions'):
        """
        Construct a new CaptureOptions with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def EncodeAsString(self) -> str:
        """
        Encode the current options to a string suitable for passing around between processes.
        
        :return: The encoded string, suitable for passing to :meth:`DecodeFromString`.
        :rtype: str
        """
        pass
    
    
    def DecodeFromString(self, encoded: str):
        """
        Decode the options from a string, as returned by :meth:`EncodeAsString`. Updates this
        object in place.
        
        :param str encoded: The encoded string, as returned by :meth:`EncodeAsString`.
        """
        pass
    
    @property
    def verifyBufferAccess(self) -> bool:
        """
        Verify buffer access. This includes checking the memory returned by a Map() call to
        detect any out-of-bounds modification, as well as initialising buffers with undefined contents to
        a marker value to catch use of uninitialised memory.
        
        .. note::
        
          This option is only valid for OpenGL and D3D11. Explicit APIs such as D3D12 and Vulkan do not
          do the same kind of interception & checking and undefined contents are really undefined.
        
        Default - disabled
        
        ``True`` - Verify buffer access.
        
        ``False`` - No verification is performed, and overwriting bounds may cause crashes or corruption in
        RenderDoc.
        
        :type: bool
        """
        pass
    
    @verifyBufferAccess.setter
    def verifyBufferAccess(self, value: bool):
        pass
    
    @property
    def allowVSync(self) -> bool:
        """
        Allow the application to enable vsync.
        
        Default - enabled
        
        ``True`` - The application can enable or disable vsync at will.
        
        ``False`` - vsync is force disabled.
        
        :type: bool
        """
        pass
    
    @allowVSync.setter
    def allowVSync(self, value: bool):
        pass
    
    @property
    def captureCallstacksOnlyActions(self) -> bool:
        """
        When capturing CPU callstacks, only capture them from actions.
        This option does nothing if :data:`captureCallstacks` is not enabled.
        
        Default - disabled
        
        ``True`` - Only captures callstacks for actions.
        
        ``False`` - Callstacks, if enabled, are captured for every event.
        
        :type: bool
        """
        pass
    
    @captureCallstacksOnlyActions.setter
    def captureCallstacksOnlyActions(self, value: bool):
        pass
    
    @property
    def captureAllCmdLists(self) -> bool:
        """
        In APIs that allow for the recording of command lists to be replayed later,
        RenderDoc may choose to not capture command lists before a frame capture is
        triggered, to reduce overheads. This means any command lists recorded once
        and replayed many times will not be available and may cause a failure to
        capture.
        
        .. note:: This is only true for APIs where multithreading is difficult or
          discouraged. Newer APIs like Vulkan and D3D12 will ignore this option
          and always capture all command lists since the API is heavily oriented
          around it and the overheads have been reduced by API design.
        
        ``True`` - All command lists are captured from the start of the application.
        
        ``False`` - Command lists are only captured if their recording begins during
        the period when a frame capture is in progress.
        
        :type: bool
        """
        pass
    
    @captureAllCmdLists.setter
    def captureAllCmdLists(self, value: bool):
        pass
    
    @property
    def apiValidation(self) -> bool:
        """
        Record API debugging events and messages
        
        Default - disabled
        
        ``True`` - Enable built-in API debugging features and records the results into
        the capture logfile, which is matched up with events on replay.
        
        ``False`` - no API debugging is forcibly enabled.
        
        :type: bool
        """
        pass
    
    @apiValidation.setter
    def apiValidation(self, value: bool):
        pass
    
    @property
    def softMemoryLimit(self) -> int:
        """
        Define a soft memory limit which some APIs may aim to keep overhead under where
        possible. Anything above this limit will where possible be saved directly to disk during capture.
        This will cause increased disk space use (which may cause a capture to fail if disk space is
        exhausted) as well as slower capture times.
        
        Not all memory allocations may be deferred like this so it is not a guarantee of a memory limit.
        
        Units are in MBs, suggested values would range from 200MB to 1000MB.
        
        Default - 0 Megabytes
        
        :type: int
        """
        pass
    
    @softMemoryLimit.setter
    def softMemoryLimit(self, value: int):
        pass
    
    @property
    def captureCallstacks(self) -> bool:
        """
        Capture CPU callstacks for API events
        
        Default - disabled
        
        ``True`` - Enables capturing of callstacks.
        
        ``False`` - no callstacks are captured.
        
        :type: bool
        """
        pass
    
    @captureCallstacks.setter
    def captureCallstacks(self, value: bool):
        pass
    
    @property
    def delayForDebugger(self) -> int:
        """
        Specify a delay in seconds to wait for a debugger to attach, after
        creating or injecting into a process, before continuing to allow it to run.
        
        ``0`` indicates no delay, and the process will run immediately after injection.
        
        Default - 0 seconds
        
        :type: int
        """
        pass
    
    @delayForDebugger.setter
    def delayForDebugger(self, value: int):
        pass
    
    @property
    def debugOutputMute(self) -> bool:
        """
        Mute API debugging output when the API validation mode option is enabled.
        
        Default - enabled
        
        ``True`` - Mute any API debug messages from being displayed or passed through.
        
        ``False`` - API debugging is displayed as normal.
        
        :type: bool
        """
        pass
    
    @debugOutputMute.setter
    def debugOutputMute(self, value: bool):
        pass
    
    @property
    def allowFullscreen(self) -> bool:
        """
        Allow the application to enable fullscreen.
        
        Default - enabled
        
        ``True`` - The application can enable or disable fullscreen at will.
        
        ``False`` - fullscreen is force disabled.
        
        :type: bool
        """
        pass
    
    @allowFullscreen.setter
    def allowFullscreen(self, value: bool):
        pass
    
    @property
    def hookIntoChildren(self) -> bool:
        """
        Hooks any system API calls that create child processes, and injects
        RenderDoc into them recursively with the same options.
        
        Default - disabled
        
        ``True`` - Hooks into spawned child processes.
        
        ``False`` - Child processes are not hooked by RenderDoc.
        
        :type: bool
        """
        pass
    
    @hookIntoChildren.setter
    def hookIntoChildren(self, value: bool):
        pass
    
    @property
    def refAllResources(self) -> bool:
        """
        By default RenderDoc only includes resources in the final logfile necessary
        for that frame, this allows you to override that behaviour.
        
        Default - disabled
        
        ``True`` - all live resources at the time of capture are included in the log
        and available for inspection.
        
        ``False`` - only the resources referenced by the captured frame are included.
        
        :type: bool
        """
        pass
    
    @refAllResources.setter
    def refAllResources(self, value: bool):
        pass
    
