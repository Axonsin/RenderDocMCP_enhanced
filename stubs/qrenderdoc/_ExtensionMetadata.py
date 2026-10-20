
from typing import overload

class ExtensionMetadata():
    # Original docstring
    """
    The metadata for an extension.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ExtensionMetadata.
        """
        pass
    
    @overload
    def __init__(self, other: 'ExtensionMetadata'):
        """
        Construct a new ExtensionMetadata with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def package(self) -> str:
        """
        The python package for this extension, e.g. foo.bar
        
        :type: str
        """
        pass
    
    @package.setter
    def package(self, value: str):
        pass
    
    @property
    def failedLoad(self) -> bool:
        """
        A flag indicating that the extension failed to load properly.
        
        This will always be false if the extension is unloaded.
        
        :type: bool
        """
        pass
    
    @failedLoad.setter
    def failedLoad(self, value: bool):
        pass
    
    @property
    def version(self) -> str:
        """
        The version of the extension
        
        :type: str
        """
        pass
    
    @version.setter
    def version(self, value: str):
        pass
    
    @property
    def description(self) -> str:
        """
        A longer description of what the extension does
        
        :type: str
        """
        pass
    
    @description.setter
    def description(self, value: str):
        pass
    
    @property
    def hasChanges(self) -> bool:
        """
        A flag indicating that the extension has changed on disk since the last time it was loaded.
        
        This will always be false if the extension is unloaded.
        
        :type: bool
        """
        pass
    
    @hasChanges.setter
    def hasChanges(self, value: bool):
        pass
    
    @property
    def extensionAPI(self) -> int:
        """
        The version of the extension API that this extension is written against
        
        :type: int
        """
        pass
    
    @extensionAPI.setter
    def extensionAPI(self, value: int):
        pass
    
    @property
    def author(self) -> str:
        """
        The author of the extension, optionally with an email contact
        
        :type: str
        """
        pass
    
    @author.setter
    def author(self, value: str):
        pass
    
    @property
    def extensionURL(self) -> str:
        """
        The URL for where the extension is fetched from
        
        :type: str
        """
        pass
    
    @extensionURL.setter
    def extensionURL(self, value: str):
        pass
    
    @property
    def name(self) -> str:
        """
        The short friendly name for the extension
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def filePath(self) -> str:
        """
        The location of this package on disk
        
        :type: str
        """
        pass
    
    @filePath.setter
    def filePath(self, value: str):
        pass
    
