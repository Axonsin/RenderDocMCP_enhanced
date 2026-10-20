from ._SDObject import SDObject

from typing import overload

class APIEvent():
    # Original docstring
    """
    An individual API-level event, generally corresponds one-to-one with an API call.
    
    .. data:: NoChunk
    
      No chunk is available.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised APIEvent.
        """
        pass
    
    @overload
    def __init__(self, other: 'APIEvent'):
        """
        Construct a new APIEvent with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoChunk = 4294967295
    """
    No chunk is available.
    """
    
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
    
