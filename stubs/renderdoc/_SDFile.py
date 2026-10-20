from ._SDChunk import SDChunk
from typing import List

from typing import overload

class SDFile():
    # Original docstring
    """
    Contains the structured information in a file. Owns the buffers and chunks.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SDFile.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def Swap(self, other: 'SDFile'):
        """
        Swaps the contents of this file with another.
        
        :param SDFile other: The other file to swap with.
        """
        pass
    
    
    def Detach(self):
        """
        Prepares the SDFile to remove any possible dependencies on what
        created it.
        """
        pass
    
    @property
    def chunks(self) -> List[SDChunk]:
        """
        The chunks in the file in order.
        
        :type: List[SDChunk]
        """
        pass
    
    @chunks.setter
    def chunks(self, value: List[SDChunk]):
        pass
    
    @property
    def version(self) -> int:
        """
        The version of this structured stream, typically only used internally.
        
        :type: int
        """
        pass
    
    @version.setter
    def version(self, value: int):
        pass
    
    @property
    def buffers(self) -> List[bytes]:
        """
        The buffers in the file, as referenced by the chunks in :data:`chunks`.
        
        :type: List[bytes]
        """
        pass
    
    @buffers.setter
    def buffers(self, value: List[bytes]):
        pass
    
