# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GPUVendor import GPUVendor

class DriverInformation(): # skipped bases: <class 'SwigPyObject'>
    """ Gives information about the driver for this API. """
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

    @property
    def vendor(self) -> GPUVendor:
        """
The :class:`GPUVendor` that provides this driver

:type: GPUVendor

"""
        pass

    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass

    @property
    def version(self) -> str:
        """
The version string for the driver

:type: str

"""
        pass

    @version.setter
    def version(self, value: str):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D8440>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DriverInformation' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DriverInformation' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DriverInformation' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DriverInformation' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DriverInformation' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DriverInformation' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DriverInformation' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DriverInformation' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DriverInformation' objects>, 'version': <attribute 'version' of 'renderdoc.DriverInformation' objects>, 'vendor': <attribute 'vendor' of 'renderdoc.DriverInformation' objects>, '__doc__': 'Gives information about the driver for this API.'})"


