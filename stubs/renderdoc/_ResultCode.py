from enum import IntEnum

class ResultCode(IntEnum):
    # Original docstring
    """
    The result from a replay operation such as opening a capture or connecting to
    a remote server.
    
    .. data:: Succeeded
    
      The operation succeeded.
    
    .. data:: UnknownError
    
      An unknown error occurred.
    
    .. data:: InternalError
    
      An internal error occurred indicating a bug or unexpected condition.
    
    .. data:: FileNotFound
    
      The specified file was not found.
    
    .. data:: InjectionFailed
    
      Injection or hooking into the target process failed.
    
    .. data:: IncompatibleProcess
    
      An incompatible process was found, e.g. a 32-bit process with 32-bit support not available.
    
    .. data:: NetworkIOFailed
    
      A network I/O operation failed.
    
    .. data:: NetworkRemoteBusy
    
      The remote side of the network connection was busy.
    
    .. data:: NetworkVersionMismatch
    
      The other side of the network connection was not at a compatible version.
    
    .. data:: FileIOFailed
    
      A filesystem I/O operation failed.
    
    .. data:: FileIncompatibleVersion
    
      The capture file had an incompatible version.
    
    .. data:: FileCorrupted
    
      The capture file is corrupted or otherwise unrecognisable.
    
    .. data:: FileUnrecognised
    
      The file was not recognised as any supported file type.
    
    .. data:: ImageUnsupported
    
      The image file or format is unrecognised or not supported in this form.
    
    .. data:: APIUnsupported
    
      The API used in the capture is not supported.
    
    .. data:: APIInitFailed
    
      The API used in the capture failed to initialise.
    
    .. data:: APIIncompatibleVersion
    
      The API data in the capture had an incompatible version.
    
    .. data:: APIHardwareUnsupported
    
      Current replaying hardware unsupported or incompatible with captured hardware.
    
    .. data:: APIDataCorrupted
    
      While loading the capture for replay, the driver encountered corrupted or invalid serialised data.
    
    .. data:: APIReplayFailed
    
      The API failed to replay the capture, with some runtime error that couldn't be determined until
      the replay began.
    
    .. data:: JDWPFailure
    
      Use of JDWP to launch and inject into the application failed, this most often indicates that some
      other JDWP-using program such as Android Studio is interfering.
    
    .. data:: AndroidGrantPermissionsFailed
    
      Failed to grant runtime permissions when installing Android remote server.
    
    .. data:: AndroidABINotFound
    
      Couldn't determine supported ABIs when installing Android remote server.
    
    .. data:: AndroidAPKFolderNotFound
    
      Couldn't find the folder which contains the Android remote server APK.
    
    .. data:: AndroidAPKInstallFailed
    
      Failed to install Android remote server for unknown reasons.
    
    .. data:: AndroidAPKVerifyFailed
    
      Failed to install Android remote server.
    
    .. data:: RemoteServerConnectionLost
    
      While replaying on a remote server, the connection was lost.
    
    .. data:: OutOfMemory
    
      An out of memory error was encountered.
    
    .. data:: DeviceLost
    
      A device lost fatal error was encountered.
    
    .. data:: DataNotAvailable
    
      Data was requested through RenderDoc's API which is not available.
    
    .. data:: InvalidParameter
    
      An invalid parameter was passed to RenderDoc's API.
    
    .. data:: CompressionFailed
    
      Compression or decompression failed.
    
    .. data:: AndroidLayerConfFailed
    
      Debug layer configuration failed on Android.
    """
    
    
    # Enum values
    
    Succeeded = 0
    """
    The operation succeeded.
    """
    
    UnknownError = 1
    """
    An unknown error occurred.
    """
    
    InternalError = 2
    """
    An internal error occurred indicating a bug or unexpected condition.
    """
    
    FileNotFound = 3
    """
    The specified file was not found.
    """
    
    InjectionFailed = 4
    """
    Injection or hooking into the target process failed.
    """
    
    IncompatibleProcess = 5
    """
    An incompatible process was found, e.g. a 32-bit process with 32-bit support not available.
    """
    
    NetworkIOFailed = 6
    """
    A network I/O operation failed.
    """
    
    NetworkRemoteBusy = 7
    """
    The remote side of the network connection was busy.
    """
    
    NetworkVersionMismatch = 8
    """
    The other side of the network connection was not at a compatible version.
    """
    
    FileIOFailed = 9
    """
    A filesystem I/O operation failed.
    """
    
    FileIncompatibleVersion = 10
    """
    The capture file had an incompatible version.
    """
    
    FileCorrupted = 11
    """
    The capture file is corrupted or otherwise unrecognisable.
    """
    
    FileUnrecognised = 12
    """
    The file was not recognised as any supported file type.
    """
    
    ImageUnsupported = 13
    """
    The image file or format is unrecognised or not supported in this form.
    """
    
    APIUnsupported = 14
    """
    The API used in the capture is not supported.
    """
    
    APIInitFailed = 15
    """
    The API used in the capture failed to initialise.
    """
    
    APIIncompatibleVersion = 16
    """
    The API data in the capture had an incompatible version.
    """
    
    APIHardwareUnsupported = 17
    """
    Current replaying hardware unsupported or incompatible with captured hardware.
    """
    
    APIDataCorrupted = 18
    """
    While loading the capture for replay, the driver encountered corrupted or invalid serialised data.
    """
    
    APIReplayFailed = 19
    """
    The API failed to replay the capture, with some runtime error that couldn't be determined until
    the replay began.
    """
    
    JDWPFailure = 20
    """
    Use of JDWP to launch and inject into the application failed, this most often indicates that some
    other JDWP-using program such as Android Studio is interfering.
    """
    
    AndroidGrantPermissionsFailed = 21
    """
    Failed to grant runtime permissions when installing Android remote server.
    """
    
    AndroidABINotFound = 22
    """
    Couldn't determine supported ABIs when installing Android remote server.
    """
    
    AndroidAPKFolderNotFound = 23
    """
    Couldn't find the folder which contains the Android remote server APK.
    """
    
    AndroidAPKInstallFailed = 24
    """
    Failed to install Android remote server for unknown reasons.
    """
    
    AndroidAPKVerifyFailed = 25
    """
    Failed to install Android remote server.
    """
    
    RemoteServerConnectionLost = 26
    """
    While replaying on a remote server, the connection was lost.
    """
    
    OutOfMemory = 27
    """
    An out of memory error was encountered.
    """
    
    DeviceLost = 28
    """
    A device lost fatal error was encountered.
    """
    
    DataNotAvailable = 29
    """
    Data was requested through RenderDoc's API which is not available.
    """
    
    InvalidParameter = 30
    """
    An invalid parameter was passed to RenderDoc's API.
    """
    
    CompressionFailed = 31
    """
    Compression or decompression failed.
    """
    
    AndroidLayerConfFailed = 32
    """
    Debug layer configuration failed on Android.
    """
    

# Assign __doc__ for enum values for easier introspection

ResultCode.Succeeded.__doc__ = """
The operation succeeded.
"""

ResultCode.UnknownError.__doc__ = """
An unknown error occurred.
"""

ResultCode.InternalError.__doc__ = """
An internal error occurred indicating a bug or unexpected condition.
"""

ResultCode.FileNotFound.__doc__ = """
The specified file was not found.
"""

ResultCode.InjectionFailed.__doc__ = """
Injection or hooking into the target process failed.
"""

ResultCode.IncompatibleProcess.__doc__ = """
An incompatible process was found, e.g. a 32-bit process with 32-bit support not available.
"""

ResultCode.NetworkIOFailed.__doc__ = """
A network I/O operation failed.
"""

ResultCode.NetworkRemoteBusy.__doc__ = """
The remote side of the network connection was busy.
"""

ResultCode.NetworkVersionMismatch.__doc__ = """
The other side of the network connection was not at a compatible version.
"""

ResultCode.FileIOFailed.__doc__ = """
A filesystem I/O operation failed.
"""

ResultCode.FileIncompatibleVersion.__doc__ = """
The capture file had an incompatible version.
"""

ResultCode.FileCorrupted.__doc__ = """
The capture file is corrupted or otherwise unrecognisable.
"""

ResultCode.FileUnrecognised.__doc__ = """
The file was not recognised as any supported file type.
"""

ResultCode.ImageUnsupported.__doc__ = """
The image file or format is unrecognised or not supported in this form.
"""

ResultCode.APIUnsupported.__doc__ = """
The API used in the capture is not supported.
"""

ResultCode.APIInitFailed.__doc__ = """
The API used in the capture failed to initialise.
"""

ResultCode.APIIncompatibleVersion.__doc__ = """
The API data in the capture had an incompatible version.
"""

ResultCode.APIHardwareUnsupported.__doc__ = """
Current replaying hardware unsupported or incompatible with captured hardware.
"""

ResultCode.APIDataCorrupted.__doc__ = """
While loading the capture for replay, the driver encountered corrupted or invalid serialised data.
"""

ResultCode.APIReplayFailed.__doc__ = """
The API failed to replay the capture, with some runtime error that couldn't be determined until
the replay began.
"""

ResultCode.JDWPFailure.__doc__ = """
Use of JDWP to launch and inject into the application failed, this most often indicates that some
other JDWP-using program such as Android Studio is interfering.
"""

ResultCode.AndroidGrantPermissionsFailed.__doc__ = """
Failed to grant runtime permissions when installing Android remote server.
"""

ResultCode.AndroidABINotFound.__doc__ = """
Couldn't determine supported ABIs when installing Android remote server.
"""

ResultCode.AndroidAPKFolderNotFound.__doc__ = """
Couldn't find the folder which contains the Android remote server APK.
"""

ResultCode.AndroidAPKInstallFailed.__doc__ = """
Failed to install Android remote server for unknown reasons.
"""

ResultCode.AndroidAPKVerifyFailed.__doc__ = """
Failed to install Android remote server.
"""

ResultCode.RemoteServerConnectionLost.__doc__ = """
While replaying on a remote server, the connection was lost.
"""

ResultCode.OutOfMemory.__doc__ = """
An out of memory error was encountered.
"""

ResultCode.DeviceLost.__doc__ = """
A device lost fatal error was encountered.
"""

ResultCode.DataNotAvailable.__doc__ = """
Data was requested through RenderDoc's API which is not available.
"""

ResultCode.InvalidParameter.__doc__ = """
An invalid parameter was passed to RenderDoc's API.
"""

ResultCode.CompressionFailed.__doc__ = """
Compression or decompression failed.
"""

ResultCode.AndroidLayerConfFailed.__doc__ = """
Debug layer configuration failed on Android.
"""

