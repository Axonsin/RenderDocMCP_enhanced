from ._GPUDevice import GPUDevice
from ._ResultDetails import ResultDetails
from ._SectionProperties import SectionProperties
from ._SectionType import SectionType
from typing import Callable, List

class CaptureAccess():
    # Original docstring
    """
    An interface for accessing a capture, possibly over a network connection. This is a
    subset of the functionality provided in :class:`CaptureFile` which only supports import/export
    and construction of files.
    """
    
    
    
    def GetAvailableGPUs(self) -> List[GPUDevice]:
        """
        Returns the list of available GPUs, that can be used in combination with
        :class:`ReplayOptions` to force replay on a particular GPU.
        
        :return: The list of GPUs available.
        :rtype: List[GPUDevice]
        """
        pass
    
    
    def GetSectionCount(self) -> int:
        """
        Retrieve the total number of available sections.
        
        :return: The number of sections in the capture
        :rtype: int
        """
        pass
    
    
    def FindSectionByName(self, name: str) -> int:
        """
        Locate the index of a section by its name. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param str name: The name of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: int
        """
        pass
    
    
    def FindSectionByType(self, type: SectionType) -> int:
        """
        Locate the index of a section by its type. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param SectionType type: The type of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: int
        """
        pass
    
    
    def GetSectionProperties(self, index: int) -> SectionProperties:
        """
        Get the describing properties of the specified section.
        
        :param int index: The index of the section.
        :return: The properties of the section, if the index is valid.
        :rtype: SectionProperties
        """
        pass
    
    
    def GetSectionContents(self, index: int) -> bytes:
        """
        Get the raw byte contents of the specified section.
        
        :param int index: The index of the section.
        :return: The raw contents of the section, if the index is valid.
        :rtype: bytes
        """
        pass
    
    
    def WriteSection(self, props: SectionProperties, contents: bytes) -> ResultDetails:
        """
        Writes a new section with specified properties and contents. If an existing section
        already has the same type or name, it will be overwritten (two sections cannot share the same type
        or name).
        
        :param SectionProperties props: The properties of the section to be written.
        :param bytes contents: The raw contents of the section.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass
    
    
    def HasCallstacks(self) -> bool:
        """
        Query if callstacks are available.
        
        :return: ``True`` if any callstacks are available, ``False`` otherwise.
        :rtype: bool
        """
        pass
    
    
    def InitResolver(self, interactive: bool, progress: Callable[[float], None]) -> ResultDetails:
        """
        Begin initialising a callstack resolver, looking up symbol files and caching as
        necessary.
        
        This function blocks while trying to initialise callstack resolving, so it should be called on a
        separate thread.
        
        :param bool interactive: ``True`` if missing symbols or other prompts should be resolved interactively.
          If this is ``False``, the function will not interact or block forever on user interaction and will
          always assume the input is effectively 'cancel' or empty. This may cause the symbol resolution to
          fail.
        :param Callable[[float], None] progress: A callback that will be repeatedly called with an updated progress
          value for the resolver process. Can be ``None`` if no progress is desired.
          Callback function signature must match :func:`ProgressCallback`.
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass
    
    
    def GetResolve(self, callstack: List[int]) -> List[str]:
        """
        Retrieve the details of each stackframe in the provided callstack.
        
        Must only be called after :meth:`InitResolver` has returned ``True``.
        
        :param List[int] callstack: The integer addresses in the original callstack.
        :return: The list of resolved callstack entries as strings.
        :rtype: List[str]
        """
        pass
    
    
    def DriverName(self) -> str:
        """
        Retrieves the name of the driver that was used to create this capture.
        
        :return: A simple string identifying the driver used to make the capture.
        :rtype: str
        """
        pass
    
    
    def EmbedDependenciesIntoCapture(self) -> ResultDetails:
        """
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
    
    
    def RemoveDependenciesFromCapture(self) -> ResultDetails:
        """
        Removes the dependent files storage from the capture i.e. shader debug files.
        
        The files will be still be considered to be referenced by the capture and could be re-embedded
        by calling :meth:`EmbedDependenciesIntoCapture`.
        
        .. warning::
          Will directly modify the capture file on disk.
        
        :return: The result of the operation.
        :rtype: ResultDetails
        """
        pass
    
    
    def HasEmbeddedDependencies(self) -> bool:
        """
        Are there any dependent files embedded in the capture i.e. shader debug files.
        
        :return: ``True`` if the capture has embedded dependent files, or ``False`` if the capture does not any embedded dependent files.
        :rtype: bool
        """
        pass
    
    
    def HasPendingDependencies(self) -> bool:
        """
        Does the capture have references to dependencies i.e. shader debug files.
        
        :return: ``True`` if the capture has references to dependent files, or ``False`` if the capture does not contain references to dependent files.
        :rtype: bool
        """
        pass
    
    
    def GetPendingDependenciesNicknames(self) -> List[str]:
        """
        Retrieve a list of the nicknames of the externally referenced dependent files being referenced
        by the capture i.e. shader debug files.
        
        .. note::
          The nicknames can be arbitrary and do not have to be a filename or a file path.
        
        :return: A list of the nicknames used to reference dependencies.
        :rtype: List[str]
        """
        pass
    
