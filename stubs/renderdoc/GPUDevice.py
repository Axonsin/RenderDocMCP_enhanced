# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GraphicsAPI import GraphicsAPI
from .GPUVendor import GPUVendor

class GPUDevice(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a single GPU at replay time. """
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
    def apis(self) -> List[GraphicsAPI]:
        """
The APIs that this device supports.

:type: List[GraphicsAPI]

"""
        pass

    @apis.setter
    def apis(self, value: List[GraphicsAPI]):
        pass

    @property
    def deviceID(self) -> int:
        """
The PCI deviceID of this GPU.

:type: int

"""
        pass

    @deviceID.setter
    def deviceID(self, value: int):
        pass

    @property
    def driver(self) -> str:
        """
The name of the driver of this GPU, if multiple drivers are available for it.

:type: str

"""
        pass

    @driver.setter
    def driver(self, value: str):
        pass

    @property
    def name(self) -> str:
        """
The human-readable name of this GPU.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vendor(self) -> GPUVendor:
        """
The :class:`GPUVendor` of this GPU.

:type: GPUVendor

"""
        pass

    @vendor.setter
    def vendor(self, value: GPUVendor):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551E4920>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GPUDevice' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GPUDevice' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GPUDevice' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GPUDevice' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GPUDevice' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GPUDevice' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GPUDevice' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GPUDevice' objects>, 'deviceID': <attribute 'deviceID' of 'renderdoc.GPUDevice' objects>, 'apis': <attribute 'apis' of 'renderdoc.GPUDevice' objects>, 'name': <attribute 'name' of 'renderdoc.GPUDevice' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GPUDevice' objects>, 'driver': <attribute 'driver' of 'renderdoc.GPUDevice' objects>, 'vendor': <attribute 'vendor' of 'renderdoc.GPUDevice' objects>, '__doc__': 'Describes a single GPU at replay time.'})"


