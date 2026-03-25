# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ResultCode(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AndroidABINotFound = 22
    """ Couldn't determine supported ABIs when installing Android remote server. """

    AndroidAPKFolderNotFound = 23
    """ Couldn't find the folder which contains the Android remote server APK. """

    AndroidAPKInstallFailed = 24
    """ Failed to install Android remote server for unknown reasons. """

    AndroidAPKVerifyFailed = 25
    """ Failed to install Android remote server. """

    AndroidGrantPermissionsFailed = 21
    """ Failed to grant runtime permissions when installing Android remote server. """

    AndroidLayerConfFailed = 32
    """ Debug layer configuration failed on Android. """

    APIDataCorrupted = 18
    """ While loading the capture for replay, the driver encountered corrupted or invalid serialised data. """

    APIHardwareUnsupported = 17
    """ Current replaying hardware unsupported or incompatible with captured hardware. """

    APIIncompatibleVersion = 16
    """ The API data in the capture had an incompatible version. """

    APIInitFailed = 15
    """ The API used in the capture failed to initialise. """

    APIReplayFailed = 19
    """
    The API failed to replay the capture, with some runtime error that couldn't be determined until
      the replay began.
    """

    APIUnsupported = 14
    """ The API used in the capture is not supported. """

    CompressionFailed = 31
    """ Compression or decompression failed. """

    DataNotAvailable = 29
    """ Data was requested through RenderDoc's API which is not available. """

    DeviceLost = 28
    """ A device lost fatal error was encountered. """

    FileCorrupted = 11
    """ The capture file is corrupted or otherwise unrecognisable. """

    FileIncompatibleVersion = 10
    """ The capture file had an incompatible version. """

    FileIOFailed = 9
    """ A filesystem I/O operation failed. """

    FileNotFound = 3
    """ The specified file was not found. """

    FileUnrecognised = 12
    """ The file was not recognised as any supported file type. """

    ImageUnsupported = 13
    """ The image file or format is unrecognised or not supported in this form. """

    IncompatibleProcess = 5
    """ An incompatible process was found, e.g. a 32-bit process with 32-bit support not available. """

    InjectionFailed = 4
    """ Injection or hooking into the target process failed. """

    InternalError = 2
    """ An internal error occurred indicating a bug or unexpected condition. """

    InvalidParameter = 30
    """ An invalid parameter was passed to RenderDoc's API. """

    JDWPFailure = 20
    """
    Use of JDWP to launch and inject into the application failed, this most often indicates that some
      other JDWP-using program such as Android Studio is interfering.
    """

    NetworkIOFailed = 6
    """ A network I/O operation failed. """

    NetworkRemoteBusy = 7
    """ The remote side of the network connection was busy. """

    NetworkVersionMismatch = 8
    """ The other side of the network connection was not at a compatible version. """

    OutOfMemory = 27
    """ An out of memory error was encountered. """

    RemoteServerConnectionLost = 26
    """ While replaying on a remote server, the connection was lost. """

    Succeeded = 0
    """ The operation succeeded. """

    UnknownError = 1
    """ An unknown error occurred. """



