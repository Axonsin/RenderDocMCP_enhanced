# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SDObject import SDObject

class APIEvent(): # skipped bases: <class 'SwigPyObject'>
    """
    An individual API-level event, generally corresponds one-to-one with an API call.
    
    .. data:: NoChunk
    
      No chunk is available.
    """
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
    def annotations(self) -> SDObject:
        """
An optional set of annotations associated with this event, may be ``None`` if
annotations are not used.

:type: SDObject

"""
        pass

    @annotations.setter
    def annotations(self, value: SDObject):
        pass

    @property
    def chunkIndex(self) -> int:
        """
The chunk index for this function call in the structured file.

If no chunk index is available this will be set to :data:`NoChunk`. This will only happen for fake
markers added to the capture after load.

:type: int

"""
        pass

    @chunkIndex.setter
    def chunkIndex(self, value: int):
        pass

    @property
    def eventId(self) -> int:
        """
The API event's Event ID.

This is a 1-based count of API events in the capture. The eventId is used as a reference point in
many places in the API to represent where in the capture the 'current state' is, and to perform
analysis in reference to the state at a particular point in the frame.

eventIds are generally increasing, positive, and contiguous, with a few exceptions. These are when
fake markers are added to a capture with :meth:`ReplayController.AddFakeMarkers`. Thus if strong
eventId guarantees are desired, this function should be avoided.

Also eventIds may not correspond directly to an actual function call - sometimes a function such as
a multi action indirect will be one function call that expands to multiple events to allow inspection
of results part way through the multi action.

:type: int

"""
        pass

    @eventId.setter
    def eventId(self, value: int):
        pass

    @property
    def fileOffset(self) -> int:
        """
A byte offset in the data stream where this event happens.

.. note:: This should only be used as a relative measure, it is not a literal number of bytes from
  the start of the file on disk.

:type: int

"""
        pass

    @fileOffset.setter
    def fileOffset(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    NoChunk = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoChunk': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521D920>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.APIEvent' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.APIEvent' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.APIEvent' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.APIEvent' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.APIEvent' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.APIEvent' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.APIEvent' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.APIEvent' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.APIEvent' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.APIEvent' objects>, 'fileOffset': <attribute 'fileOffset' of 'renderdoc.APIEvent' objects>, 'annotations': <attribute 'annotations' of 'renderdoc.APIEvent' objects>, 'chunkIndex': <attribute 'chunkIndex' of 'renderdoc.APIEvent' objects>, '__doc__': '\\nAn individual API-level event, generally corresponds one-to-one with an API call.\\n\\n.. data:: NoChunk\\n\\n  No chunk is available.\\n\\n'})"


