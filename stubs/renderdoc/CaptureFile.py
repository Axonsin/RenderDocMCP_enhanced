# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResultDetails import ResultDetails
from .SDFile import SDFile
from .CaptureFileFormat import CaptureFileFormat
from .FileType import FileType
from .Thumbnail import Thumbnail
from .ReplaySupport import ReplaySupport
from .ReplayController import ReplayController
from .ReplayOptions import ReplayOptions

from .CaptureAccess import CaptureAccess

class CaptureFile(CaptureAccess):
    """
    A handle to a capture file. Used for simple cheap processing and meta-data fetching
    without opening the capture for analysis.
    """
    def Convert(self, filename: str, filetype: str, file: SDFile, progress: ProgressCallback) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        Convert(filename, filetype, file, progress)
        
        Converts the currently loaded file to a given format and saves it to disk.
        
        This allows converting a native RDC to another representation, or vice-versa converting another
        representation back to native RDC.
        
        :param str filename: The filename to save to.
        :param str filetype: The format to convert to.
        :param SDFile file: An optional :class:`SDFile` with the structured data to source from. This is
          useful in case the format specifies that it doesn't need buffers, and you already have a
          :class:`ReplayController` open with the structured data. This saves the need to load the file
          again. If ``None`` then structured data will be fetched if not already present and used.
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value for the conversion. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def CopyFileTo(self, filename: str) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        CopyFileTo(filename)
        
        When a capture file is opened, an exclusive lock is held on the file on disk. This
        makes it impossible to copy the file to another location at the user's request. Calling this
        function will copy the file on disk to a new location but otherwise won't affect the capture handle.
        The new file will be locked, the old file will be unlocked - to allow deleting if necessary.
        
        It is invalid to call this function if :meth:`OpenFile` has not previously been called to open the
        file.
        
        :param str filename: The filename to copy to.
        :return: The result of the file copy operation.
        :rtype: ResultDetails
        """
        pass

    def GetCaptureFileFormats(self) -> List[CaptureFileFormat]: # real signature unknown; restored from __doc__
        """
        GetCaptureFileFormats()
        
        Returns the list of capture file formats.
        
        :return: The list of capture file formats available.
        :rtype: List[CaptureFileFormat]
        """
        pass

    def GetStructuredData(self) -> SDFile: # real signature unknown; restored from __doc__
        """
        GetStructuredData()
        
        Returns the structured data for this capture.
        
        The lifetime of this data is scoped to the lifetime of the capture handle, so it cannot be used
        after the handle is destroyed.
        
        :return: The structured data representing the file.
        :rtype: SDFile
        """
        pass

    def GetThumbnail(self, type: FileType, maxsize: int) -> Thumbnail: # real signature unknown; restored from __doc__
        """
        GetThumbnail(type, maxsize)
        
        Retrieves the embedded thumbnail from the capture.
        
        .. note:: The only supported values for :paramref:`GetThumbnail.type` are :attr:`FileType.JPG`,
          :attr:`FileType.PNG`, :attr:`FileType.TGA`, and :attr:`FileType.BMP`.
        
        :param FileType type: The image format to convert the thumbnail to.
        :param int maxsize: The largest width or height allowed. If the thumbnail is larger, it's resized.
        :return: The raw contents of the thumbnail, converted to the desired type at the desired max
          resolution.
        :rtype: Thumbnail
        """
        pass

    def LocalReplaySupport(self) -> ReplaySupport: # real signature unknown; restored from __doc__
        """
        LocalReplaySupport()
        
        Queries for how well a particular capture is supported on the local machine.
        
        If the file was opened with a format other than native ``rdc`` this will always return no
        replay support.
        
        :return: How much support for replay exists locally.
        :rtype: ReplaySupport
        """
        pass

    def OpenBuffer(self, buffer: bytes, filetype: str, progress: ProgressCallback) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        OpenBuffer(buffer, filetype, progress)
        
        Initialises the file handle from a raw memory buffer.
        
        This may be useful if you don't want to parse the whole file or already have the file in memory.
        
        For the :paramref:`OpenBuffer.filetype` parameter, see :meth:`OpenFile`.
        
        :param bytes buffer: The buffer containing the data to process.
        :param str filetype: The format of the given file.
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value if an import step occurs. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def OpenCapture(self, opts: ReplayOptions, progress: ProgressCallback) -> Tuple[ResultDetails,ReplayController]: # real signature unknown; restored from __doc__
        """
        OpenCapture(opts, progress)
        
        Opens a capture for replay locally and returns a handle to the capture. Only supported
        for handles opened with a native ``rdc`` capture, otherwise this will fail.
        
        This function will block until the capture is fully loaded and ready.
        
        Once the replay is created, this :class:`CaptureFile` can be shut down, there is no dependency on it
        by the :class:`ReplayController`.
        
        :param ReplayOptions opts: The options controlling how the capture should be replayed.
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value for the opening. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: A tuple containing the status of opening the capture, whether success or failure, and the
          resulting :class:`ReplayController` handle if successful.
        :rtype: Tuple[ResultDetails,ReplayController]
        """
        pass

    def OpenFile(self, filename: str, filetype: str, progress: ProgressCallback) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        OpenFile(filename, filetype, progress)
        
        Initialises the capture handle from a file.
        
        This method supports converting from non-native representations via structured data, by specifying
        the input format in the :paramref:`OpenFile.filetype` parameter. The list of supported formats can be retrieved
        by calling :meth:`GetCaptureFileFormats`.
        
        ``rdc`` is guaranteed to always be a supported filetype, and will be assumed if the filetype is
        empty or unrecognised.
        
        :param str filename: The filename of the file to open.
        :param str filetype: The format of the given file.
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value if an import step occurs. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def RecordedMachineIdent(self) -> str: # real signature unknown; restored from __doc__
        """
        RecordedMachineIdent()
        
        Retrieves the identifying string describing what type of machine created this capture.
        
        :return: A string identifying the machine ident used to make the capture.
        :rtype: str
        """
        pass

    def SetMetadata(self, driverName: str, machineIdent: int, thumbType: FileType, thumbWidth: int, thumbHeight: int, thumbData: bytes, timeBase: int, timeFreq: float): # real signature unknown; restored from __doc__
        """
        SetMetadata(driverName, machineIdent, thumbType, thumbWidth, thumbHeight, thumbData, timeBase, timeFreq)
        
        Sets the matadata for this capture handle.
        
        This function may only be called if the handle is 'empty' - i.e. no file has been opened with
        :meth:`OpenFile` or :meth:`OpenBuffer`.
        
        .. note:: The only supported values for :paramref:`SetMetadata.thumbType` are :attr:`FileType.JPG`,
          :attr:`FileType.PNG`, :attr:`FileType.TGA`, and :attr:`FileType.BMP`.
        
        :param str driverName: The name of the driver. Must be a recognised driver name (even if replay
          support for that driver is not compiled in locally.
        :param int machineIdent: The encoded machine identity value. Optional value and can be left to 0, as
          the bits to set are internally defined, so only generally useful if copying a machine ident from
          an existing capture.
        :param FileType thumbType: The file type of the thumbnail. Ignored if
          :paramref:`SetMetadata.thumbData` is empty.
        :param int thumbWidth: The width of the thumbnail. Ignored if :paramref:`SetMetadata.thumbData` is
          empty.
        :param int thumbHeight: The height of the thumbnail. Ignored if :paramref:`SetMetadata.thumbData` is
          empty.
        :param bytes thumbData: The raw data of the thumbnail. If empty, no thumbnail is set.
        :param int timeBase: The base value for timestamps in the capture. Can be set to 0 to indicate that
          timestamps are already capture relative.
        :param float timeFreq: The frequency for timestamps and durations to be divided by to convert to
          microseconds. Can be set to 1.0 to indicate that timestamps and durations are already in
          microseconds.
        """
        pass

    def SetStructuredData(self, file: SDFile): # real signature unknown; restored from __doc__
        """
        SetStructuredData(file)
        
        Sets the structured data for this capture.
        
        This allows calling code to populate a capture out of generated structured data. In combination with
        :meth:`SetMetadata` this allows a purely in-memory creation of a file to be saved out with
        :meth:`Convert`.
        
        The data is copied internally so it can be destroyed after calling this function.
        
        :param SDFile file: The structured data representing the file.
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Closes the file handle.
        """
        pass

    def TimestampBase(self) -> int: # real signature unknown; restored from __doc__
        """
        TimestampBase()
        
        Retrieves the timestamp basis that all timestamps in the capture are relative to. May
        be 0 if all timestamps are already absolute.
        
        :return: The timestamp base value
        :rtype: int
        """
        pass

    def TimestampFrequency(self) -> float: # real signature unknown; restored from __doc__
        """
        TimestampFrequency()
        
        Retrieves frequency for timestamps and durations to be divided by to convert to
        microseconds. May be 1.0 if all timestamps and durations are already in microseconds.
        
        :return: The timestamp frequency
        :rtype: float
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CF360>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CaptureFile' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CaptureFile' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CaptureFile' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CaptureFile' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CaptureFile' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CaptureFile' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CaptureFile' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CaptureFile' objects>, 'Shutdown': <method 'Shutdown' of 'renderdoc.CaptureFile' objects>, 'OpenFile': <method 'OpenFile' of 'renderdoc.CaptureFile' objects>, 'OpenBuffer': <method 'OpenBuffer' of 'renderdoc.CaptureFile' objects>, 'CopyFileTo': <method 'CopyFileTo' of 'renderdoc.CaptureFile' objects>, 'Convert': <method 'Convert' of 'renderdoc.CaptureFile' objects>, 'GetCaptureFileFormats': <method 'GetCaptureFileFormats' of 'renderdoc.CaptureFile' objects>, 'LocalReplaySupport': <method 'LocalReplaySupport' of 'renderdoc.CaptureFile' objects>, 'RecordedMachineIdent': <method 'RecordedMachineIdent' of 'renderdoc.CaptureFile' objects>, 'TimestampBase': <method 'TimestampBase' of 'renderdoc.CaptureFile' objects>, 'TimestampFrequency': <method 'TimestampFrequency' of 'renderdoc.CaptureFile' objects>, 'SetMetadata': <method 'SetMetadata' of 'renderdoc.CaptureFile' objects>, 'OpenCapture': <method 'OpenCapture' of 'renderdoc.CaptureFile' objects>, 'GetStructuredData': <method 'GetStructuredData' of 'renderdoc.CaptureFile' objects>, 'SetStructuredData': <method 'SetStructuredData' of 'renderdoc.CaptureFile' objects>, 'GetThumbnail': <method 'GetThumbnail' of 'renderdoc.CaptureFile' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CaptureFile' objects>, '__doc__': '\\nA handle to a capture file. Used for simple cheap processing and meta-data fetching\\nwithout opening the capture for analysis.\\n\\n'})"


