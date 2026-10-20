from ._CaptureContext import CaptureContext
from renderdoc import ActionDescription, SDChunk


# Synthetic function
def EventFilterCallback(context: CaptureContext, filter: str, params: str, eventId: int, chunk: SDChunk, action: ActionDescription, name: str) -> bool:
    """
    Not a member function - the signature for any ``EventFilterCallback`` callbacks.
    
    Called for each event in a capture when performing filtering in the Event Browser. The associated
    :func:`FilterParseCallback` will be called first to parse the parameters, and is available for caching
    or syntax checking. The same filter name and params string will be passed to this function.
    
    :param CaptureContext context: The current capture context.
    :param str filter: The name of the filter function.
    :param str params: The parameters to the filter function.
    :param int eventId: The event's :data:`eventId <renderdoc.APIEvent.eventId>`.
    :param renderdoc.SDChunk chunk: The structured data chunk for this event.
    :param renderdoc.ActionDescription action: The action that contains this event. If the event is
      the action itself then the event ID will be equal.
    :param str name: The name of the event as shown in the event browser, for string-based filtering.
    :return: Whether or not this event matches the filter
    :rtype: bool
    """
    pass

