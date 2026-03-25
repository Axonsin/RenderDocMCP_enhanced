# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class APIUseData(): # skipped bases: <class 'SwigPyObject'>
    """ Information about the API that the target is using. """
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
    def name(self) -> str:
        """
The name of the API.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def presenting(self) -> bool:
        """
``True`` if the API is presenting to a swapchain

:type: bool

"""
        pass

    @presenting.setter
    def presenting(self, value: bool):
        pass

    @property
    def supported(self) -> bool:
        """
``True`` if the API can be captured.

:type: bool

"""
        pass

    @supported.setter
    def supported(self, value: bool):
        pass

    @property
    def supportMessage(self) -> str:
        """
A string message if the API is unsupported explaining why.

:type: str

"""
        pass

    @supportMessage.setter
    def supportMessage(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551EDCB0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.APIUseData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.APIUseData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.APIUseData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.APIUseData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.APIUseData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.APIUseData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.APIUseData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.APIUseData' objects>, 'name': <attribute 'name' of 'renderdoc.APIUseData' objects>, 'presenting': <attribute 'presenting' of 'renderdoc.APIUseData' objects>, 'supportMessage': <attribute 'supportMessage' of 'renderdoc.APIUseData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.APIUseData' objects>, 'supported': <attribute 'supported' of 'renderdoc.APIUseData' objects>, '__doc__': 'Information about the API that the target is using.'})"


