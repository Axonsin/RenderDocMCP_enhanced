# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CaptureFileFormat(): # skipped bases: <class 'SwigPyObject'>
    """ The format for a capture file either supported to read from, or export to """
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
    def convertSupported(self) -> bool:
        """
Indicates whether captures or structured data can be saved out in this format.

:type: bool

"""
        pass

    @convertSupported.setter
    def convertSupported(self, value: bool):
        pass

    @property
    def description(self) -> str:
        """
A human readable long-form description of the file format.

:type: str

"""
        pass

    @description.setter
    def description(self, value: str):
        pass

    @property
    def extension(self) -> str:
        """
The file of the format as a single minimal string, e.g. ``rdc``.

:type: str

"""
        pass

    @extension.setter
    def extension(self, value: str):
        pass

    @property
    def name(self) -> str:
        """
A human readable short phrase naming the file format.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def openSupported(self) -> bool:
        """
Indicates whether or not files in this format can be opened and processed as
structured data.

:type: bool

"""
        pass

    @openSupported.setter
    def openSupported(self, value: bool):
        pass

    @property
    def requiresBuffers(self) -> bool:
        """
Indicates whether exporting to this format requires buffers or just structured data.
If it doesn't require buffers then it can be exported directly from an opened capture, which by
default has structured data but no buffers available.

:type: bool

"""
        pass

    @requiresBuffers.setter
    def requiresBuffers(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D08D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CaptureFileFormat' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CaptureFileFormat' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CaptureFileFormat' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CaptureFileFormat' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CaptureFileFormat' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CaptureFileFormat' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CaptureFileFormat' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CaptureFileFormat' objects>, 'name': <attribute 'name' of 'renderdoc.CaptureFileFormat' objects>, 'requiresBuffers': <attribute 'requiresBuffers' of 'renderdoc.CaptureFileFormat' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CaptureFileFormat' objects>, 'description': <attribute 'description' of 'renderdoc.CaptureFileFormat' objects>, 'openSupported': <attribute 'openSupported' of 'renderdoc.CaptureFileFormat' objects>, 'convertSupported': <attribute 'convertSupported' of 'renderdoc.CaptureFileFormat' objects>, 'extension': <attribute 'extension' of 'renderdoc.CaptureFileFormat' objects>, '__doc__': 'The format for a capture file either supported to read from, or export to'})"


