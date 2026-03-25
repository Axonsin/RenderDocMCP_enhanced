# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class RGPInterop(): # skipped bases: <class 'SwigPyObject'>
    """ Controlling interface for interop with RGP tool. """
    def HasRGPEvent(self, eventId: int) -> bool: # real signature unknown; restored from __doc__
        """
        HasRGPEvent(eventId)
        
        Return true if the given :data:`eventId <renderdoc.APIEvent.eventId>` has and
        equivalent in RGP.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: ``True`` if there is an equivalent. This only confirms the equivalent exists, not that it
          will be selectable in all cases.
        :rtype: bool
        """
        pass

    def SelectRGPEvent(self, eventId: int) -> bool: # real signature unknown; restored from __doc__
        """
        SelectRGPEvent(eventId)
        
        Select the given :data:`eventId <renderdoc.APIEvent.eventId>` equivalent in RGP.
        
        :param int eventId: The :data:`eventId <renderdoc.APIEvent.eventId>` to query for.
        :return: ``True`` if the selection request succeeded. This only confirms the request was sent, not
          that the event was selected in RGP.
        :rtype: bool
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD501424D0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.RGPInterop' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.RGPInterop' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.RGPInterop' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.RGPInterop' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.RGPInterop' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.RGPInterop' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.RGPInterop' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.RGPInterop' objects>, 'HasRGPEvent': <method 'HasRGPEvent' of 'qrenderdoc.RGPInterop' objects>, 'SelectRGPEvent': <method 'SelectRGPEvent' of 'qrenderdoc.RGPInterop' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.RGPInterop' objects>, '__doc__': 'Controlling interface for interop with RGP tool.'})"


