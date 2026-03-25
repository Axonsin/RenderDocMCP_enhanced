# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResultDetails import ResultDetails
from .SectionType import SectionType
from .GPUDevice import GPUDevice
from .SectionProperties import SectionProperties

class CaptureAccess(): # skipped bases: <class 'SwigPyObject'>
    """
    An interface for accessing a capture, possibly over a network connection. This is a
    subset of the functionality provided in :class:`CaptureFile` which only supports import/export
    and construction of files.
    """
    def DriverName(self) -> str: # real signature unknown; restored from __doc__
        """
        DriverName()
        
        Retrieves the name of the driver that was used to create this capture.
        
        :return: A simple string identifying the driver used to make the capture.
        :rtype: str
        """
        pass

    def EmbedDependenciesIntoCapture(self) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        EmbedDependenciesIntoCapture()
        
        Stores the dependent file data into the capture i.e. shader debug files.
        
        This reads the contents of the dependent files and stores their file contents into the capture.
        This can help the capture to be more portable by embedding all externally referenced dependent files.
        Use :meth:`RemoveDependenciesFromCapture` to remove the embedded file data.
        
        .. warning::
          Will remove all the existing embedded file data from the capture.
          Will directly modify the capture file on disk.
        
        .. note::
          This will increase the size of the capture file.
          Externally referenced files which can't be found on disk are skipped.
        
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def FindSectionByName(self, name: str) -> int: # real signature unknown; restored from __doc__
        """
        FindSectionByName(name)
        
        Locate the index of a section by its name. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param str name: The name of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: int
        """
        pass

    def FindSectionByType(self, type: SectionType) -> int: # real signature unknown; restored from __doc__
        """
        FindSectionByType(type)
        
        Locate the index of a section by its type. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param SectionType type: The type of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: int
        """
        pass

    def GetAvailableGPUs(self) -> List[GPUDevice]: # real signature unknown; restored from __doc__
        """
        GetAvailableGPUs()
        
        Returns the list of available GPUs, that can be used in combination with
        :class:`ReplayOptions` to force replay on a particular GPU.
        
        :return: The list of GPUs available.
        :rtype: List[GPUDevice]
        """
        pass

    def GetPendingDependenciesNicknames(self) -> List[str]: # real signature unknown; restored from __doc__
        """
        GetPendingDependenciesNicknames()
        
        Retrieve a list of the nicknames of the externally referenced dependent files being referenced 
        by the capture i.e. shader debug files.
        
        .. note::
          The nicknames can be arbitary and do not have to be a filename or a file path.
        
        :return: A list of the nicknames used to reference dependencies.
        :rtype: List[str]
        """
        pass

    def GetResolve(self, callstack: List[int]) -> List[str]: # real signature unknown; restored from __doc__
        """
        GetResolve(callstack)
        
        Retrieve the details of each stackframe in the provided callstack.
        
        Must only be called after :meth:`InitResolver` has returned ``True``.
        
        :param List[int] callstack: The integer addresses in the original callstack.
        :return: The list of resolved callstack entries as strings.
        :rtype: List[str]
        """
        pass

    def GetSectionContents(self, index: int) -> bytes: # real signature unknown; restored from __doc__
        """
        GetSectionContents(index)
        
        Get the raw byte contents of the specified section.
        
        :param int index: The index of the section.
        :return: The raw contents of the section, if the index is valid.
        :rtype: bytes
        """
        pass

    def GetSectionCount(self) -> int: # real signature unknown; restored from __doc__
        """
        GetSectionCount()
        
        Retrieve the total number of available sections.
        
        :return: The number of sections in the capture
        :rtype: int
        """
        pass

    def GetSectionProperties(self, index: int) -> SectionProperties: # real signature unknown; restored from __doc__
        """
        GetSectionProperties(index)
        
        Get the describing properties of the specified section.
        
        :param int index: The index of the section.
        :return: The properties of the section, if the index is valid.
        :rtype: SectionProperties
        """
        pass

    def HasCallstacks(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasCallstacks()
        
        Query if callstacks are available.
        
        :return: ``True`` if any callstacks are available, ``False`` otherwise.
        :rtype: bool
        """
        pass

    def HasEmbeddedDependencies(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasEmbeddedDependencies()
        
        Are there any depdendent files embedded in the capture i.e. shader debug files.
        
        :return: ``True`` if the capture has embedded dependent files, or ``False`` if the capture does not any embedded dependent files.
        :rtype: bool
        """
        pass

    def HasPendingDependencies(self) -> bool: # real signature unknown; restored from __doc__
        """
        HasPendingDependencies()
        
        Does the capture have references to dependecies i.e. shader debug files.
        
        :return: ``True`` if the capture has references to dependent files, or ``False`` if the capture does not contain references to dependent files.
        :rtype: bool
        """
        pass

    def InitResolver(self, interactive: bool, progress: ProgressCallback) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        InitResolver(interactive, progress)
        
        Begin initialising a callstack resolver, looking up symbol files and caching as
        necessary.
        
        This function blocks while trying to initialise callstack resolving, so it should be called on a
        separate thread.
        
        :param bool interactive: ``True`` if missing symbols or other prompts should be resolved interactively.
          If this is ``False``, the function will not interact or block forever on user interaction and will
          always assume the input is effectively 'cancel' or empty. This may cause the symbol resolution to
          fail.
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value for the resolver process. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def RemoveDependenciesFromCapture(self) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        RemoveDependenciesFromCapture()
        
        Removes the dependent files storage from the capture i.e. shader debug files.
        
        The files will be still be considered to be referenced by the capture and could be re-embedded 
        by calling :meth:`EmbedDependenciesIntoCapture`.
        
        .. warning::
          Will directly modify the capture file on disk.
        
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass

    def WriteSection(self, props: SectionProperties, contents: bytes) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        WriteSection(props, contents)
        
        Writes a new section with specified properties and contents. If an existing section
        already has the same type or name, it will be overwritten (two sections cannot share the same type
        or name).
        
        :param SectionProperties props: The properties of the section to be written.
        :param bytes contents: The raw contents of the section.
        :return: The result of the operation.
        :rtype: ResultDetails
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551DE120>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CaptureAccess' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CaptureAccess' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CaptureAccess' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CaptureAccess' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CaptureAccess' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CaptureAccess' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CaptureAccess' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CaptureAccess' objects>, 'GetAvailableGPUs': <method 'GetAvailableGPUs' of 'renderdoc.CaptureAccess' objects>, 'GetSectionCount': <method 'GetSectionCount' of 'renderdoc.CaptureAccess' objects>, 'FindSectionByName': <method 'FindSectionByName' of 'renderdoc.CaptureAccess' objects>, 'FindSectionByType': <method 'FindSectionByType' of 'renderdoc.CaptureAccess' objects>, 'GetSectionProperties': <method 'GetSectionProperties' of 'renderdoc.CaptureAccess' objects>, 'GetSectionContents': <method 'GetSectionContents' of 'renderdoc.CaptureAccess' objects>, 'WriteSection': <method 'WriteSection' of 'renderdoc.CaptureAccess' objects>, 'HasCallstacks': <method 'HasCallstacks' of 'renderdoc.CaptureAccess' objects>, 'InitResolver': <method 'InitResolver' of 'renderdoc.CaptureAccess' objects>, 'GetResolve': <method 'GetResolve' of 'renderdoc.CaptureAccess' objects>, 'DriverName': <method 'DriverName' of 'renderdoc.CaptureAccess' objects>, 'EmbedDependenciesIntoCapture': <method 'EmbedDependenciesIntoCapture' of 'renderdoc.CaptureAccess' objects>, 'RemoveDependenciesFromCapture': <method 'RemoveDependenciesFromCapture' of 'renderdoc.CaptureAccess' objects>, 'HasEmbeddedDependencies': <method 'HasEmbeddedDependencies' of 'renderdoc.CaptureAccess' objects>, 'HasPendingDependencies': <method 'HasPendingDependencies' of 'renderdoc.CaptureAccess' objects>, 'GetPendingDependenciesNicknames': <method 'GetPendingDependenciesNicknames' of 'renderdoc.CaptureAccess' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CaptureAccess' objects>, '__doc__': '\\nAn interface for accessing a capture, possibly over a network connection. This is a\\nsubset of the functionality provided in :class:`CaptureFile` which only supports import/export\\nand construction of files.\\n\\n'})"


