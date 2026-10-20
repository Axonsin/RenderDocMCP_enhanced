
class RGPInterop():
    # Original docstring
    """
    Controlling interface for interop with RGP tool.
    """
    
    
    
    def HasRGPEvent(self, eventId: int) -> bool:
        """
        Return true if the given :data:`eventId <renderdoc.APIEvent.eventId>` has and
        equivalent in RGP.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: ``True`` if there is an equivalent. This only confirms the equivalent exists, not that it
          will be selectable in all cases.
        :rtype: bool
        """
        pass
    
    
    def SelectRGPEvent(self, eventId: int) -> bool:
        """
        Select the given :data:`eventId <renderdoc.APIEvent.eventId>` equivalent in RGP.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: ``True`` if the selection request succeeded. This only confirms the request was sent, not
          that the event was selected in RGP.
        :rtype: bool
        """
        pass
    
