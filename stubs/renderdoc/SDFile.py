# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SDChunk import SDChunk

class SDFile(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the structured information in a file. Owns the buffers and chunks. """
    def Detach(self): # real signature unknown; restored from __doc__
        """
        Detach()
        
        Prepares the SDFile to remove any possible dependencies on what
        created it.
        """
        pass

    def Swap(self, other: SDFile): # real signature unknown; restored from __doc__
        """
        Swap(other)
        
        Swaps the contents of this file with another.
        
        :param SDFile other: The other file to swap with.
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552282D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDFile' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDFile' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDFile' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDFile' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDFile' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDFile' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDFile' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDFile' objects>, 'Swap': <method 'Swap' of 'renderdoc.SDFile' objects>, 'Detach': <method 'Detach' of 'renderdoc.SDFile' objects>, 'chunks': <attribute 'chunks' of 'renderdoc.SDFile' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDFile' objects>, 'version': <attribute 'version' of 'renderdoc.SDFile' objects>, 'buffers': <attribute 'buffers' of 'renderdoc.SDFile' objects>, '__doc__': 'Contains the structured information in a file. Owns the buffers and chunks.'})"


